# Mixture of Experts (MoE) - Chapter 1: Fundamentals

## Introduction

Mixture of Experts (MoE) is a neural network architecture that combines multiple specialized sub-networks ("experts") with a gating mechanism that dynamically routes inputs to the most appropriate experts. This approach enables models to scale to billions or even trillions of parameters while maintaining computational efficiency during inference.

### Why MoE Matters

Traditional dense models activate all parameters for every input, leading to:
- **Computational bottlenecks** at large scales
- **Memory constraints** limiting model size
- **Inefficient specialization** where all parameters must handle all tasks

MoE addresses these challenges by:
- **Conditional computation**: Only activating a subset of parameters per input
- **Specialization**: Different experts learn different aspects of the data
- **Scalability**: Enabling trillion-parameter models with manageable compute costs

### Real-World Impact

MoE architectures power many state-of-the-art models:
- **Switch Transformer** (Google): 1.6 trillion parameters
- **GShard** (Google): Efficient multilingual translation
- **Mixtral 8x7B** (Mistral AI): High-performance open-weight model
- **GLaM** (Google): 1.2 trillion parameter language model

---

## Core Concepts

### 1. Expert Networks

Experts are independent neural networks (typically feed-forward networks) that specialize in different aspects of the input space.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class Expert(nn.Module):
    """A single expert network (typically an FFN)."""
    
    def __init__(self, d_model: int, d_ff: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model)
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class SparseMoELayer(nn.Module):
    """Sparse Mixture of Experts layer with top-k routing."""
    
    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_experts: int,
        k: int = 2,
        capacity_factor: float = 1.0
    ):
        super().__init__()
        self.num_experts = num_experts
        self.k = k
        self.capacity_factor = capacity_factor
        
        # Create experts
        self.experts = nn.ModuleList([
            Expert(d_model, d_ff) for _ in range(num_experts)
        ])
        
        # Gating network (router)
        self.gate = nn.Linear(d_model, num_experts)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: Input tensor of shape [batch_size, seq_len, d_model]
        
        Returns:
            Output tensor of shape [batch_size, seq_len, d_model]
        """
        batch_size, seq_len, d_model = x.shape
        
        # Flatten for processing
        x_flat = x.reshape(-1, d_model)  # [batch*seq, d_model]
        
        # Compute router logits
        router_logits = self.gate(x_flat)  # [batch*seq, num_experts]
        
        # Get top-k experts and their weights
        topk_weights, topk_indices = torch.topk(
            router_logits, self.k, dim=-1
        )  # [batch*seq, k]
        
        # Normalize weights
        topk_weights = F.softmax(topk_weights, dim=-1)
        
        # Initialize output
        output = torch.zeros_like(x_flat)
        
        # Process each expert
        for expert_idx in range(self.num_experts):
            # Find tokens routed to this expert
            expert_mask = (topk_indices == expert_idx)
            
            if expert_mask.sum() == 0:
                continue
            
            # Get positions and routing indices
            token_positions = expert_mask.any(dim=-1)
            
            # Process through expert
            expert_input = x_flat[token_positions]
            expert_output = self.experts[expert_idx](expert_input)
            
            # Weight and accumulate
            for k_idx in range(self.k):
                k_mask = expert_mask[:, k_idx]
                if k_mask.sum() > 0:
                    weighted_output = expert_output[k_mask.any(dim=-1, keepdim=True).expand_as(k_mask)] * \
                                     topk_weights[k_mask, k_idx:k_idx+1]
                    output[token_positions] += weighted_output
        
        # Reshape back
        output = output.reshape(batch_size, seq_len, d_model)
        
        return output
```

### 2. Gating Mechanism

The gating network determines which experts should process each input token.

#### Top-K Routing

The most common approach selects the top-k experts for each token:

```python
class TopKRouter(nn.Module):
    """Top-k routing with load balancing loss."""
    
    def __init__(self, d_model: int, num_experts: int, k: int = 2):
        super().__init__()
        self.num_experts = num_experts
        self.k = k
        self.gate = nn.Linear(d_model, num_experts, bias=False)
    
    def forward(self, x: torch.Tensor):
        """
        Returns:
            gate_output: Router logits
            selected_experts: Top-k expert indices
            routing_weights: Normalized weights for selected experts
            load_balance_loss: Auxiliary loss for load balancing
        """
        # Compute router logits
        gate_logits = self.gate(x)  # [..., num_experts]
        
        # Get top-k
        topk_weights, topk_indices = torch.topk(gate_logits, self.k, dim=-1)
        
        # Normalize weights
        routing_weights = F.softmax(topk_weights, dim=-1)
        
        # Compute load balancing loss
        load_balance_loss = self._compute_load_balance_loss(gate_logits)
        
        return gate_logits, topk_indices, routing_weights, load_balance_loss
    
    def _compute_load_balance_loss(self, gate_logits: torch.Tensor) -> torch.Tensor:
        """
        Compute auxiliary loss to encourage balanced expert usage.
        
        Based on Switch Transformer paper.
        """
        # Compute fraction of tokens routed to each expert
        router_probs = F.softmax(gate_logits, dim=-1)
        fraction_of_tokens = router_probs.mean(dim=tuple(range(router_probs.dim()-1)))
        
        # Compute fraction of capacity allocated to each expert
        _, topk_indices = torch.topk(gate_logits, self.k, dim=-1)
        one_hot = F.one_hot(topk_indices, self.num_experts).float()
        fraction_of_capacity = one_hot.mean(dim=tuple(range(one_hot.dim()-2)))
        fraction_of_capacity = fraction_of_capacity.sum(dim=-2)  # Sum over k
        
        # Load balance loss
        load_balance_loss = (fraction_of_tokens * fraction_of_capacity).sum() * self.num_experts
        
        return load_balance_loss
```

### 3. Sparse vs Dense MoE

| Aspect | Sparse MoE | Dense MoE |
|--------|-----------|-----------|
| **Experts Activated** | Subset (e.g., 2 of 8) | All experts |
| **Compute Cost** | Constant (independent of num_experts) | Linear in num_experts |
| **Parameter Count** | Very high (billions+) | Moderate |
| **Specialization** | High (experts develop distinct skills) | Lower (all experts see all data) |
| **Training Complexity** | Higher (routing, load balancing) | Lower |
| **Use Cases** | LLMs, large-scale models | Multi-task learning, ensembles |

### 4. Capacity Factor and Token Dropping

When using sparse MoE, we need to manage how many tokens each expert can process:

```python
class MoEWithCapacity(nn.Module):
    """MoE layer with capacity factor and token dropping."""
    
    def __init__(
        self,
        d_model: int,
        d_ff: int,
        num_experts: int,
        k: int = 2,
        capacity_factor: float = 1.25
    ):
        super().__init__()
        self.num_experts = num_experts
        self.k = k
        self.capacity_factor = capacity_factor
        
        self.experts = nn.ModuleList([
            Expert(d_model, d_ff) for _ in range(num_experts)
        ])
        self.gate = nn.Linear(d_model, num_experts, bias=False)
    
    def forward(self, x: torch.Tensor):
        batch_size, seq_len, d_model = x.shape
        total_tokens = batch_size * seq_len
        
        # Calculate capacity per expert
        tokens_per_expert = int(
            self.capacity_factor * total_tokens / self.num_experts
        )
        
        # Route tokens
        router_logits = self.gate(x.reshape(-1, d_model))
        topk_weights, topk_indices = torch.topk(router_logits, self.k, dim=-1)
        routing_weights = F.softmax(topk_weights, dim=-1)
        
        # Track dropped tokens
        tokens_dropped = 0
        
        # Process experts with capacity constraints
        output = torch.zeros_like(x.reshape(-1, d_model))
        
        for expert_idx in range(self.num_experts):
            # Find tokens assigned to this expert
            expert_mask = (topk_indices == expert_idx)
            
            # Count tokens per position in top-k
            expert_counts = expert_mask.sum(dim=0)  # [k]
            
            # Process each routing position
            for k_idx in range(self.k):
                k_mask = expert_mask[:, k_idx]
                num_tokens = k_mask.sum()
                
                if num_tokens == 0:
                    continue
                
                # Check capacity
                if num_tokens > tokens_per_expert:
                    # Drop excess tokens
                    tokens_dropped += num_tokens - tokens_per_expert
                    # Select first tokens_per_expert tokens
                    selected_indices = k_mask.nonzero(as_tuple=True)[0][:tokens_per_expert]
                    k_mask_selected = torch.zeros_like(k_mask)
                    k_mask_selected[selected_indices] = True
                else:
                    k_mask_selected = k_mask
                
                # Process through expert
                expert_input = x.reshape(-1, d_model)[k_mask_selected]
                expert_output = self.experts[expert_idx](expert_input)
                
                # Accumulate weighted output
                output[k_mask_selected] += expert_output * routing_weights[k_mask_selected, k_idx:k_idx+1]
        
        output = output.reshape(batch_size, seq_len, d_model)
        
        return output, tokens_dropped
```

---

## Mathematical Foundations

### MoE Output Computation

For an input token $x$, the MoE layer output is:

$$y = \sum_{i=1}^{n} g(x)_i \cdot E_i(x)$$

Where:
- $g(x)_i$ is the gating weight for expert $i$
- $E_i(x)$ is the output of expert $i$
- $n$ is the number of experts

In sparse MoE with top-k routing:

$$y = \sum_{i \in \text{TopK}(g(x))} \frac{\exp(g(x)_i)}{\sum_{j \in \text{TopK}(g(x))} \exp(g(x)_j)} \cdot E_i(x)$$

### Load Balancing Loss

To prevent expert collapse (where some experts are rarely used), Switch Transformer introduces:

$$\mathcal{L}_{aux} = n \cdot \sum_{i=1}^{n} f_i \cdot P_i$$

Where:
- $f_i$ is the fraction of tokens routed to expert $i$
- $P_i$ is the fraction of capacity allocated to expert $i$
- $n$ is the number of experts

---

## Basic Implementation Example

Here's a complete minimal MoE implementation:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F


class MinimalMoE(nn.Module):
    """Minimal working MoE implementation."""
    
    def __init__(self, d_model=512, d_ff=2048, num_experts=8, k=2):
        super().__init__()
        self.num_experts = num_experts
        self.k = k
        
        # Experts
        self.experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, d_ff),
                nn.GELU(),
                nn.Linear(d_ff, d_model)
            )
            for _ in range(num_experts)
        ])
        
        # Router
        self.router = nn.Linear(d_model, num_experts, bias=False)
    
    def forward(self, x):
        """
        Args:
            x: [batch, seq_len, d_model]
        """
        batch, seq_len, d_model = x.shape
        x_flat = x.reshape(-1, d_model)
        
        # Route
        router_logits = self.router(x_flat)
        topk_weights, topk_indices = torch.topk(router_logits, self.k, dim=-1)
        weights = F.softmax(topk_weights, dim=-1)
        
        # Compute output
        output = torch.zeros_like(x_flat)
        
        for i, expert in enumerate(self.experts):
            mask = (topk_indices == i)
            if mask.sum() == 0:
                continue
            
            for k_idx in range(self.k):
                k_mask = mask[:, k_idx]
                if k_mask.sum() > 0:
                    expert_out = expert(x_flat[k_mask])
                    output[k_mask] += expert_out * weights[k_mask, k_idx:k_idx+1]
        
        return output.reshape(batch, seq_len, d_model)


# Test the implementation
if __name__ == "__main__":
    # Create model
    model = MinimalMoE(d_model=512, d_ff=2048, num_experts=8, k=2)
    
    # Create sample input
    x = torch.randn(4, 32, 512)  # batch=4, seq=32, d_model=512
    
    # Forward pass
    output = model(x)
    
    print(f"Input shape: {x.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Number of experts: {model.num_experts}")
    print(f"Top-k: {model.k}")
```

---

## Training Considerations

### 1. Learning Rate Scheduling

MoE models often benefit from:
- Warmup period for stable routing
- Lower learning rates for router compared to experts
- Careful monitoring of load balance

```python
def create_moe_optimizer(model, base_lr=1e-4, router_lr_multiplier=0.1):
    """Create optimizer with different learning rates for router and experts."""
    
    router_params = []
    expert_params = []
    
    for name, param in model.named_parameters():
        if 'gate' in name or 'router' in name:
            router_params.append(param)
        else:
            expert_params.append(param)
    
    optimizer = torch.optim.AdamW([
        {'params': router_params, 'lr': base_lr * router_lr_multiplier},
        {'params': expert_params, 'lr': base_lr}
    ])
    
    return optimizer
```

### 2. Monitoring Expert Usage

```python
def monitor_expert_usage(router_logits, num_experts):
    """Monitor how evenly experts are being used."""
    
    # Get routing decisions
    _, topk_indices = torch.topk(router_logits, 2, dim=-1)
    
    # Count expert usage
    expert_counts = torch.zeros(num_experts, device=router_logits.device)
    for k_idx in range(2):
        unique, counts = torch.unique(topk_indices[:, k_idx], return_counts=True)
        expert_counts[unique] += counts.float()
    
    # Calculate statistics
    usage_ratio = expert_counts.max() / (expert_counts.mean() + 1e-8)
    
    return {
        'expert_counts': expert_counts.cpu().numpy(),
        'max_min_ratio': usage_ratio.item(),
        'std_dev': expert_counts.std().item()
    }
```

---

## Comparison with Other Architectures

| Architecture | Parameters | Active Params/Token | Specialization | Best For |
|-------------|------------|---------------------|----------------|----------|
| **Dense Transformer** | 1B | 1B | None | General purpose, smaller scale |
| **MoE (8 experts)** | 8B | ~2B | High | Large-scale language modeling |
| **MoE (64 experts)** | 64B | ~4B | Very High | Massive multi-task learning |
| **Mixture of Attention** | Variable | Variable | Medium | Multi-domain understanding |

---

## Practical Tips

### Do's ✅
- Start with 4-8 experts for experimentation
- Use capacity factor between 1.0-1.25
- Monitor load balance loss during training
- Apply dropout to router for regularization
- Use gradient clipping to stabilize training

### Don'ts ❌
- Don't use too many experts initially (>16)
- Don't ignore load balancing metrics
- Don't set capacity factor too low (<1.0)
- Don't train without warmup
- Don't expect immediate convergence (MoE takes longer)

---

## Hands-On Exercises

### Exercise 1: Implement Basic MoE
Create a simple MoE layer with 4 experts and top-2 routing. Test it with random input and verify output shapes.

### Exercise 2: Add Load Balancing
Extend your MoE implementation to include load balancing loss. Train a small model and monitor expert usage distribution.

### Exercise 3: Compare Sparse vs Dense
Implement both sparse (top-2) and dense (all experts) versions. Compare their performance and compute requirements on a simple task.

### Exercise 4: Experiment with Capacity Factor
Test different capacity factors (0.5, 1.0, 1.5, 2.0) and measure their impact on token dropping and model performance.

---

## Next Steps

In Chapter 2, we'll explore advanced MoE architectures including:
- Switch Transformer's single-expert routing
- GShard's distributed MoE training
- Mixtral's fine-grained MoE design
- Hierarchical MoE structures

In Chapter 3, we'll cover production deployment strategies, optimization techniques, and real-world case studies.

---

## References

1. Shazeer, N., et al. (2017). "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
2. Fedus, W., et al. (2021). "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
3. Lepikhin, A., et al. (2020). "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding"
4. Jiang, A.Q., et al. (2026). "Mixtral of Experts"
