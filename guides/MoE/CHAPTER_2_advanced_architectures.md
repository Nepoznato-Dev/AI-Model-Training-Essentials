# Mixture of Experts (MoE) - Chapter 2: Advanced Architectures

## Introduction

Building on the fundamentals from Chapter 1, this chapter explores advanced MoE architectures that have pushed the boundaries of model scale and efficiency. We'll examine production-ready designs from Google's Switch Transformer and GShard to Mistral AI's Mixtral, along with innovative variations like hierarchical MoE and attention-based routing.

---

## 1. Switch Transformer: Single-Expert Routing

Switch Transformer simplifies MoE by routing each token to exactly **one expert** instead of multiple, dramatically improving efficiency while maintaining performance.

### Key Innovations

- **Top-1 Routing**: Each token goes to only one expert
- **Simplified Load Balancing**: Easier to balance with single routing decision
- **Massive Scale**: Enables trillion-parameter models
- **Efficient Training**: Reduced communication overhead in distributed settings

### Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class SwitchRouter(nn.Module):
    """Switch Transformer router with top-1 routing."""
    
    def __init__(self, d_model: int, num_experts: int):
        super().__init__()
        self.num_experts = num_experts
        self.gate = nn.Linear(d_model, num_experts, bias=False)
    
    def forward(self, x: torch.Tensor):
        """
        Args:
            x: [..., d_model] input tensor
        
        Returns:
            expert_indices: [batch*seq] expert assignment for each token
            router_probs: [batch*seq] probability distribution over experts
            load_balance_loss: auxiliary loss for balancing
        """
        # Compute router logits
        router_logits = self.gate(x)  # [..., num_experts]
        
        # Get top-1 expert
        router_probs = F.softmax(router_logits, dim=-1)
        expert_weights, expert_indices = torch.max(router_probs, dim=-1)
        
        # Compute load balance loss
        load_balance_loss = self._compute_load_balance_loss(router_logits)
        
        return expert_indices, expert_weights, load_balance_loss
    
    def _compute_load_balance_loss(self, router_logits: torch.Tensor) -> torch.Tensor:
        """
        Switch Transformer load balancing loss.
        
        Encourages uniform distribution of tokens across experts.
        """
        # Probability distribution over experts
        probs = F.softmax(router_logits, dim=-1)
        
        # Fraction of tokens per expert (expected)
        fraction_of_tokens = probs.mean(dim=tuple(range(probs.dim()-1)))
        
        # Fraction of capacity per expert (actual via hard selection)
        _, expert_indices = torch.max(probs, dim=-1)
        one_hot = F.one_hot(expert_indices, self.num_experts).float()
        fraction_of_capacity = one_hot.mean(dim=tuple(range(one_hot.dim()-1)))
        
        # Loss encourages both fractions to be uniform
        loss = (fraction_of_tokens * fraction_of_capacity).sum() * self.num_experts
        
        return loss


class SwitchMoELayer(nn.Module):
    """Switch Transformer MoE layer with top-1 routing."""
    
    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_experts: int,
        capacity_factor: float = 1.0
    ):
        super().__init__()
        self.num_experts = num_experts
        self.capacity_factor = capacity_factor
        
        # Experts (standard FFN)
        self.experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, d_ff),
                nn.GELU(),
                nn.Linear(d_ff, d_model)
            )
            for _ in range(num_experts)
        ])
        
        # Router
        self.router = SwitchRouter(d_model, num_experts)
    
    def forward(self, x: torch.Tensor):
        """
        Args:
            x: [batch, seq_len, d_model]
        
        Returns:
            output: [batch, seq_len, d_model]
            aux_loss: load balancing auxiliary loss
            tokens_dropped: number of tokens dropped due to capacity
        """
        batch_size, seq_len, d_model = x.shape
        total_tokens = batch_size * seq_len
        
        # Flatten input
        x_flat = x.reshape(-1, d_model)
        
        # Route tokens
        expert_indices, expert_weights, aux_loss = self.router(x_flat)
        
        # Calculate capacity per expert
        tokens_per_expert = int(self.capacity_factor * total_tokens / self.num_experts)
        
        # Initialize output
        output = torch.zeros_like(x_flat)
        tokens_dropped = 0
        
        # Process each expert
        for expert_idx in range(self.num_experts):
            # Find tokens assigned to this expert
            expert_mask = (expert_indices == expert_idx)
            num_tokens = expert_mask.sum()
            
            if num_tokens == 0:
                continue
            
            # Handle capacity constraints
            if num_tokens > tokens_per_expert:
                tokens_dropped += num_tokens - tokens_per_expert
                # Select first tokens_per_expert tokens
                selected_indices = expert_mask.nonzero(as_tuple=True)[0][:tokens_per_expert]
                expert_mask_selected = torch.zeros_like(expert_mask)
                expert_mask_selected[selected_indices] = True
            else:
                expert_mask_selected = expert_mask
            
            # Process through expert
            expert_input = x_flat[expert_mask_selected]
            expert_output = self.experts[expert_idx](expert_input)
            
            # Apply routing weights and accumulate
            output[expert_mask_selected] += expert_output * \
                                           expert_weights[expert_mask_selected, None]
        
        # Reshape output
        output = output.reshape(batch_size, seq_len, d_model)
        
        return output, aux_loss, tokens_dropped
```

### Advantages of Top-1 Routing

| Metric | Top-1 (Switch) | Top-2 (Standard) |
|--------|---------------|------------------|
| **Compute Efficiency** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Communication Cost** | Low | Medium |
| **Load Balancing** | Easier | Harder |
| **Model Quality** | Comparable | Slightly better |
| **Implementation Complexity** | Simple | Complex |

---

## 2. GShard: Distributed MoE Training

GShard extends MoE for massive-scale distributed training across hundreds of TPU/GPU cores.

### Key Features

- **Expert Parallelism**: Distribute experts across devices
- **Automatic Sharding**: Compiler-driven device placement
- **Capacity Factor Tuning**: Dynamic adjustment during training
- **Random Routing**: Stochastic expert assignment for load balancing

### Distributed Expert Placement

```python
class DistributedMoE(nn.Module):
    """MoE layer designed for distributed training."""
    
    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_experts: int,
        k: int = 2,
        num_devices: int = 8
    ):
        super().__init__()
        self.num_experts = num_experts
        self.k = k
        self.num_devices = num_devices
        self.experts_per_device = num_experts // num_devices
        
        # Local experts (only store experts for this device)
        self.local_experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, d_ff),
                nn.GELU(),
                nn.Linear(d_ff, d_model)
            )
            for _ in range(self.experts_per_device)
        ])
        
        # Router (replicated across devices)
        self.router = nn.Linear(d_model, num_experts, bias=False)
    
    def forward(self, x: torch.Tensor, device_id: int):
        """
        Args:
            x: [batch, seq_len, d_model] local input
            device_id: ID of current device (0 to num_devices-1)
        
        Returns:
            output: processed output
            tokens_sent: number of tokens sent to other devices
            tokens_received: number of tokens received from other devices
        """
        batch_size, seq_len, d_model = x.shape
        x_flat = x.reshape(-1, d_model)
        
        # Route tokens
        router_logits = self.router(x_flat)
        topk_weights, topk_indices = torch.topk(router_logits, self.k, dim=-1)
        routing_weights = F.softmax(topk_weights, dim=-1)
        
        # Determine which tokens need to be sent to other devices
        tokens_to_send = {}  # device_id -> list of (token_idx, expert_idx, weight)
        tokens_to_process_locally = []
        
        for token_idx in range(len(x_flat)):
            for k_idx in range(self.k):
                expert_idx = topk_indices[token_idx, k_idx].item()
                target_device = expert_idx // self.experts_per_device
                
                if target_device == device_id:
                    # Process locally
                    tokens_to_process_locally.append((
                        token_idx,
                        expert_idx % self.experts_per_device,  # local expert index
                        routing_weights[token_idx, k_idx].item()
                    ))
                else:
                    # Send to other device
                    if target_device not in tokens_to_send:
                        tokens_to_send[target_device] = []
                    tokens_to_send[target_device].append((
                        token_idx,
                        expert_idx,
                        routing_weights[token_idx, k_idx].item()
                    ))
        
        # In real implementation, use NCCL or similar for communication
        # This is a simplified placeholder
        output = torch.zeros_like(x_flat)
        
        # Process local tokens
        for token_idx, local_expert_idx, weight in tokens_to_process_locally:
            expert_output = self.local_experts[local_expert_idx](
                x_flat[token_idx:token_idx+1]
            )
            output[token_idx] += expert_output.squeeze(0) * weight
        
        # Placeholder for cross-device communication
        # In practice: all-to-all communication, process remote tokens, send back
        
        return output.reshape(batch_size, seq_len, d_model)
```

### Capacity Factor Scheduling

```python
class AdaptiveCapacityScheduler:
    """Dynamically adjust capacity factor during training."""
    
    def __init__(
        self,
        initial_capacity: float = 2.0,
        min_capacity: float = 1.0,
        decay_steps: int = 10000
    ):
        self.initial_capacity = initial_capacity
        self.min_capacity = min_capacity
        self.decay_steps = decay_steps
    
    def get_capacity_factor(self, step: int) -> float:
        """Get capacity factor for given training step."""
        if step >= self.decay_steps:
            return self.min_capacity
        
        # Linear decay
        progress = step / self.decay_steps
        return self.initial_capacity - progress * (
            self.initial_capacity - self.min_capacity
        )
    
    def adjust_based_on_drop_rate(
        self,
        current_capacity: float,
        drop_rate: float,
        target_drop_rate: float = 0.01
    ) -> float:
        """Adjust capacity based on token drop rate."""
        if drop_rate > target_drop_rate:
            # Increase capacity to reduce dropping
            return min(current_capacity * 1.1, 2.5)
        elif drop_rate < target_drop_rate / 2:
            # Decrease capacity for efficiency
            return max(current_capacity * 0.95, 1.0)
        return current_capacity
```

---

## 3. Mixtral 8x7B: Fine-Grained Sparse MoE

Mixtral demonstrates that carefully designed sparse MoE can outperform dense models at similar compute budgets.

### Architecture Highlights

- **8 Experts per Layer**: Each transformer block has its own set of 8 experts
- **Top-2 Routing**: Each token uses exactly 2 experts
- **No Capacity Constraints**: Simplified training without token dropping
- **High Sparsity**: Only ~13B active parameters out of 47B total

### Mixtral-Style Implementation

```python
class MixtralMoEBlock(nn.Module):
    """MoE block inspired by Mixtral 8x7B."""
    
    def __init__(
        self,
        d_model: int = 4096,
        d_ff: int = 14336,
        num_experts: int = 8,
        k: int = 2
    ):
        super().__init__()
        self.num_experts = num_experts
        self.k = k
        
        # Experts with SwiGLU activation (as in Mixtral)
        self.experts = nn.ModuleList([
            SwiGLUFFN(d_model, d_ff)
            for _ in range(num_experts)
        ])
        
        # Router
        self.gate = nn.Linear(d_model, num_experts, bias=False)
    
    def forward(self, x: torch.Tensor):
        """
        Args:
            x: [batch, seq_len, d_model]
        
        Returns:
            output: [batch, seq_len, d_model]
            router_aux_loss: auxiliary loss for load balancing
        """
        batch_size, seq_len, d_model = x.shape
        x_flat = x.reshape(-1, d_model)
        
        # Compute routing
        router_logits = self.gate(x_flat)  # [batch*seq, num_experts]
        
        # Top-k selection
        topk_weights, topk_indices = torch.topk(router_logits, self.k, dim=-1)
        
        # Normalize weights with softmax
        routing_weights = F.softmax(topk_weights, dim=-1, dtype=torch.float32)
        
        # Cast back to original dtype
        routing_weights = routing_weights.to(x.dtype)
        
        # Initialize output
        final_output = torch.zeros_like(x_flat)
        
        # Process each expert
        for expert_idx in range(self.num_experts):
            # Get mask for tokens using this expert
            expert_mask = (topk_indices == expert_idx)
            
            # Process for each routing position
            for k_idx in range(self.k):
                k_mask = expert_mask[:, k_idx]
                
                if k_mask.sum() == 0:
                    continue
                
                # Get expert output
                expert_input = x_flat[k_mask]
                expert_output = self.experts[expert_idx](expert_input)
                
                # Weight and accumulate
                final_output[k_mask] += expert_output * \
                                       routing_weights[k_mask, k_idx:k_idx+1]
        
        # Compute auxiliary load balancing loss
        router_aux_loss = self._compute_aux_loss(router_logits)
        
        return final_output.reshape(batch_size, seq_len, d_model), router_aux_loss
    
    def _compute_aux_loss(self, router_logits: torch.Tensor) -> torch.Tensor:
        """
        Compute auxiliary loss for load balancing.
        
        Uses the standard Switch Transformer formulation.
        """
        router_probs = F.softmax(router_logits, dim=-1)
        
        # Get top-k indices
        _, topk_indices = torch.topk(router_logits, self.k, dim=-1)
        
        # Create one-hot encoding
        one_hot = F.one_hot(topk_indices, self.num_experts).float()
        
        # Calculate fraction of tokens per expert
        fraction_of_tokens = router_probs.mean(dim=tuple(range(router_probs.dim()-1)))
        
        # Calculate fraction of capacity per expert
        fraction_of_capacity = one_hot.mean(dim=tuple(range(one_hot.dim()-2))).sum(dim=-2)
        
        # Auxiliary loss
        aux_loss = (fraction_of_tokens * fraction_of_capacity).sum() * self.num_experts
        
        return aux_loss


class SwiGLUFFN(nn.Module):
    """SwiGLU feed-forward network as used in Mixtral."""
    
    def __init__(self, d_model: int, d_ff: int):
        super().__init__()
        self.gate_proj = nn.Linear(d_model, d_ff, bias=False)
        self.up_proj = nn.Linear(d_model, d_ff, bias=False)
        self.down_proj = nn.Linear(d_ff, d_model, bias=False)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """SwiGLU activation: (gate ⊗ up) → down"""
        gate = F.silu(self.gate_proj(x))
        up = self.up_proj(x)
        return self.down_proj(gate * up)
```

---

## 4. Hierarchical MoE

Hierarchical MoE introduces multiple levels of routing for more fine-grained specialization.

### Two-Level Routing Architecture

```python
class HierarchicalMoE(nn.Module):
    """Two-level hierarchical MoE with coarse and fine routing."""
    
    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_groups: int = 4,
        experts_per_group: int = 4,
        top_k_groups: int = 2,
        top_k_experts: int = 2
    ):
        super().__init__()
        self.num_groups = num_groups
        self.experts_per_group = experts_per_group
        self.total_experts = num_groups * experts_per_group
        self.top_k_groups = top_k_groups
        self.top_k_experts = top_k_experts
        
        # Group-level router
        self.group_router = nn.Linear(d_model, num_groups, bias=False)
        
        # Expert-level routers (one per group)
        self.expert_routers = nn.ModuleList([
            nn.Linear(d_model, experts_per_group, bias=False)
            for _ in range(num_groups)
        ])
        
        # Experts organized by groups
        self.experts = nn.ModuleList([
            nn.ModuleList([
                nn.Sequential(
                    nn.Linear(d_model, d_ff),
                    nn.GELU(),
                    nn.Linear(d_ff, d_model)
                )
                for _ in range(experts_per_group)
            ])
            for _ in range(num_groups)
        ])
    
    def forward(self, x: torch.Tensor):
        """
        Two-stage routing:
        1. Route to top-k groups
        2. Within each selected group, route to top-k experts
        """
        batch_size, seq_len, d_model = x.shape
        x_flat = x.reshape(-1, d_model)
        
        # Stage 1: Group routing
        group_logits = self.group_router(x_flat)
        topk_group_weights, topk_group_indices = torch.topk(
            group_logits, self.top_k_groups, dim=-1
        )
        group_weights = F.softmax(topk_group_weights, dim=-1)
        
        # Initialize output
        output = torch.zeros_like(x_flat)
        
        # Stage 2: Expert routing within selected groups
        for group_k_idx in range(self.top_k_groups):
            group_idx = topk_group_indices[:, group_k_idx]
            
            # Process each unique group
            for g in range(self.num_groups):
                group_mask = (group_idx == g)
                if group_mask.sum() == 0:
                    continue
                
                # Get tokens for this group
                group_tokens = x_flat[group_mask]
                
                # Expert routing within group
                expert_logits = self.expert_routers[g](group_tokens)
                topk_expert_weights, topk_expert_indices = torch.topk(
                    expert_logits, self.top_k_experts, dim=-1
                )
                expert_weights = F.softmax(topk_expert_weights, dim=-1)
                
                # Process experts in this group
                group_output = torch.zeros_like(group_tokens)
                
                for expert_k_idx in range(self.top_k_experts):
                    expert_idx = topk_expert_indices[:, expert_k_idx]
                    
                    for e in range(self.experts_per_group):
                        expert_mask = (expert_idx == e)
                        if expert_mask.sum() == 0:
                            continue
                        
                        expert_input = group_tokens[expert_mask]
                        expert_output = self.experts[g][e](expert_input)
                        
                        group_output[expert_mask] += expert_output * \
                                                    expert_weights[expert_mask, expert_k_idx:expert_k_idx+1]
                
                # Accumulate with group weight
                output[group_mask] += group_output * group_weights[group_mask, group_k_idx:group_k_idx+1]
        
        return output.reshape(batch_size, seq_len, d_model)
```

---

## 5. Attention-Based Routing

Instead of a simple linear router, use attention mechanisms for more sophisticated routing decisions.

```python
class AttentionRouter(nn.Module):
    """Attention-based router for context-aware expert selection."""
    
    def __init__(self, d_model: int, num_experts: int, num_heads: int = 4):
        super().__init__()
        self.num_experts = num_experts
        self.attention = nn.MultiheadAttention(
            embed_dim=d_model,
            num_heads=num_heads,
            batch_first=True
        )
        self.router = nn.Linear(d_model, num_experts)
    
    def forward(self, x: torch.Tensor, key_value: torch.Tensor = None):
        """
        Args:
            x: [batch, seq_len, d_model] query
            key_value: optional context for routing
        
        Returns:
            expert_weights: routing weights
            expert_indices: selected experts
        """
        if key_value is None:
            key_value = x
        
        # Self-attention over sequence
        attended, _ = self.attention(x, key_value, key_value)
        
        # Route based on attended representation
        router_logits = self.router(attended)
        topk_weights, topk_indices = torch.topk(router_logits, 2, dim=-1)
        expert_weights = F.softmax(topk_weights, dim=-1)
        
        return expert_weights, topk_indices


class AttentionMoELayer(nn.Module):
    """MoE layer with attention-based routing."""
    
    def __init__(self, d_model: int, d_ff: int, num_experts: int, num_heads: int = 4):
        super().__init__()
        self.experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, d_ff),
                nn.GELU(),
                nn.Linear(d_ff, d_model)
            )
            for _ in range(num_experts)
        ])
        self.router = AttentionRouter(d_model, num_experts, num_heads)
    
    def forward(self, x: torch.Tensor):
        batch_size, seq_len, d_model = x.shape
        x_flat = x.reshape(-1, d_model)
        
        # Get routing from attention router
        routing_weights, expert_indices = self.router(x.unsqueeze(1))
        routing_weights = routing_weights.squeeze(1)
        expert_indices = expert_indices.squeeze(1)
        
        # Process through experts
        output = torch.zeros_like(x_flat)
        
        for expert_idx in range(self.num_experts):
            mask = (expert_indices == expert_idx)
            if mask.sum() == 0:
                continue
            
            for k_idx in range(2):
                k_mask = expert_indices[:, k_idx] == expert_idx
                if k_mask.sum() > 0:
                    expert_out = self.experts[expert_idx](x_flat[k_mask])
                    output[k_mask] += expert_out * routing_weights[k_mask, k_idx:k_idx+1]
        
        return output.reshape(batch_size, seq_len, d_model)
```

---

## Architecture Comparison

| Architecture | Routing | Experts/Layer | Active Params | Best Use Case |
|-------------|---------|---------------|---------------|---------------|
| **Switch Transformer** | Top-1 | 64-256 | ~1/num_experts | Maximum scale, efficiency |
| **GShard** | Top-2 | 8-16 | ~2/num_experts | Distributed training |
| **Mixtral 8x7B** | Top-2 | 8 | 2/8 = 25% | High quality, moderate scale |
| **Hierarchical MoE** | Two-level | 16-64 | Variable | Fine-grained specialization |
| **Attention MoE** | Context-aware | 8-16 | 2/num_experts | Sequence-dependent routing |

---

## Practical Implementation Tips

### 1. Expert Initialization

```python
def initialize_experts(model: nn.Module, init_method: str = 'xavier'):
    """Properly initialize expert networks."""
    
    for expert in model.experts:
        for module in expert.modules():
            if isinstance(module, nn.Linear):
                if init_method == 'xavier':
                    nn.init.xavier_uniform_(module.weight)
                elif init_method == 'orthogonal':
                    nn.init.orthogonal_(module.weight)
                
                if module.bias is not None:
                    nn.init.zeros_(module.bias)
    
    # Initialize router with smaller variance
    if hasattr(model, 'gate') or hasattr(model, 'router'):
        router = getattr(model, 'gate', None) or getattr(model, 'router', None)
        nn.init.xavier_uniform_(router.weight, gain=0.1)
```

### 2. Gradient Checkpointing for Memory Efficiency

```python
from torch.utils.checkpoint import checkpoint

class CheckpointedMoE(nn.Module):
    """MoE with gradient checkpointing for memory efficiency."""
    
    def __init__(self, base_moe: nn.Module):
        super().__init__()
        self.base_moe = base_moe
    
    def forward(self, x):
        # Checkpoint the expensive expert computation
        return checkpoint(self.base_moe.forward, x, use_reentrant=False)
```

### 3. Expert Drop Path

```python
class DropPath(nn.Module):
    """Drop paths (Stochastic Depth) for MoE regularization."""
    
    def __init__(self, drop_prob: float = 0.0):
        super().__init__()
        self.drop_prob = drop_prob
    
    def forward(self, x):
        if self.drop_prob == 0.0 or not self.training:
            return x
        
        keep_prob = 1 - self.drop_prob
        shape = (x.shape[0],) + (1,) * (x.ndim - 1)
        random_tensor = keep_prob + torch.rand(shape, dtype=x.dtype, device=x.device)
        binary_tensor = torch.floor(random_tensor)
        
        return x / keep_prob * binary_tensor


class MoEWithDropPath(nn.Module):
    """MoE with stochastic depth."""
    
    def __init__(self, base_moe: nn.Module, drop_path_rate: float = 0.1):
        super().__init__()
        self.moe = base_moe
        self.drop_path = DropPath(drop_path_rate)
    
    def forward(self, x):
        return x + self.drop_path(self.moe(x))
```

---

## Hands-On Exercises

### Exercise 1: Implement Switch Transformer MoE
Create a complete Switch Transformer block with top-1 routing and train it on a simple language modeling task.

### Exercise 2: Build Hierarchical MoE
Implement the two-level hierarchical MoE and compare its specialization patterns with flat MoE.

### Exercise 3: Experiment with Routing Strategies
Compare top-1, top-2, and attention-based routing on the same task. Measure convergence speed and final performance.

### Exercise 4: Scale to Multiple Devices
Simulate distributed MoE training by partitioning experts across multiple "virtual devices" and implementing all-to-all communication.

---

## Next Steps

In Chapter 3, we'll cover:
- Production deployment strategies for MoE models
- Quantization and compression techniques
- Real-world case studies and performance benchmarks
- Debugging and monitoring MoE systems in production

---

## References

1. Fedus, W., et al. (2021). "Switch Transformers: Scaling to Trillion Parameter Models"
2. Lepikhin, A., et al. (2020). "GShard: Scaling Giant Models with Conditional Computation"
3. Jiang, A.Q., et al. (2024). "Mixtral of Experts"
4. Zhou, Y., et al. (2022). "Mixture-of-Experts meets Instruction Tuning"
5. Clark, A., et al. (2022). "Unified Scaling Laws for Routed Language Models"
