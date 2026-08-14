# Simple Agent with Memory
# Build a conversational agent with short-term and long-term memory
# Lines of code: ~300 (including comments)

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================================

import json
import os
import ast
import time
from datetime import datetime
from collections import deque

print("=" * 70)
print("SIMPLE AGENT WITH MEMORY - Build Your Own AI Agent")
print("=" * 70)
print()

# ============================================================================
# STEP 2: UNDERSTAND WHAT MAKES AN AGENT
# ============================================================================
#
# A regular chatbot:  User says something -> Bot gives a response (done)
#
# An AGENT:          User says something -> Agent:
#                       1. Perceives the input
#                       2. Thinks about what to do (reasoning)
#                       3. Decides on an action (tool use, memory lookup)
#                       4. Observes the result
#                       5. Updates its memory
#                       6. Responds
#
# Key difference: Agents have a LOOP (perceive -> think -> act -> observe)
# and they can use TOOLS and MEMORY to accomplish goals.
#
# In this project, we'll build an agent with:
#   - Short-term memory: Recent conversation context (like working memory)
#   - Long-term memory: Persistent facts the agent remembers across sessions
#   - Tools: Calculator, time lookup, and note-taking
#   - A simple reasoning loop to decide what to do
#
# ============================================================================

# ============================================================================
# STEP 3: BUILD THE MEMORY SYSTEMS
# ============================================================================

class ShortTermMemory:
    """
    Short-term memory: stores the recent conversation history.
    
    Like your working memory, it has limited capacity and forgets
    older information when it gets full.
    """
    
    def __init__(self, max_messages=20):
        """
        Args:
            max_messages: Maximum number of messages to remember
        """
        self.memory = deque(maxlen=max_messages)
    
    def add(self, role, content):
        """Add a message to short-term memory."""
        self.memory.append({
            "role": role,       # "user" or "agent"
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
    
    def get_recent(self, n=5):
        """Get the n most recent messages."""
        return list(self.memory)[-n:]
    
    def get_all(self):
        """Get all messages in memory."""
        return list(self.memory)
    
    def clear(self):
        """Clear all short-term memories."""
        self.memory.clear()
    
    def __len__(self):
        return len(self.memory)


class LongTermMemory:
    """
    Long-term memory: persistent storage of important facts.
    
    Unlike short-term memory, this persists across conversations.
    The agent can store facts, recall them later, and even forget
    things it hasn't used in a while.
    """
    
    def __init__(self, filepath="agent_memory.json"):
        self.filepath = filepath
        self.memories = {}  # key: topic, value: {fact, timestamp, access_count}
        self._load()
    
    def store(self, topic, fact):
        """
        Store a fact in long-term memory.
        
        Args:
            topic: What the fact is about (e.g., "user_name", "favorite_color")
            fact: The actual information to remember
        """
        self.memories[topic] = {
            "fact": fact,
            "stored_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "access_count": 0
        }
        self._save()
        print(f"  [Memory] Stored: '{topic}' -> '{fact}'")
    
    def recall(self, topic):
        """
        Recall a fact from long-term memory.
        
        Args:
            topic: What to look up
        
        Returns:
            The stored fact, or None if not found
        """
        if topic in self.memories:
            self.memories[topic]["access_count"] += 1
            self._save()
            return self.memories[topic]["fact"]
        return None
    
    def search(self, query):
        """Search for facts related to a query."""
        results = []
        query_lower = query.lower()
        for topic, data in self.memories.items():
            if query_lower in topic.lower() or query_lower in data["fact"].lower():
                results.append((topic, data["fact"]))
        return results
    
    def forget(self, topic):
        """Remove a memory (if it's wrong or no longer relevant)."""
        if topic in self.memories:
            del self.memories[topic]
            self._save()
            print(f"  [Memory] Forgot: '{topic}'")
    
    def get_all_memories(self):
        """List all stored memories."""
        return {topic: data["fact"] for topic, data in self.memories.items()}
    
    def _save(self):
        """Persist memories to disk."""
        with open(self.filepath, 'w') as f:
            json.dump(self.memories, f, indent=2)
    
    def _load(self):
        """Load memories from disk."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    self.memories = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.memories = {}

# ============================================================================
# STEP 4: BUILD THE TOOLS
# ============================================================================

class AgentTools:
    """
    Tools that the agent can use to accomplish tasks.
    
    Tools are what make an agent more than just a chatbot.
    They allow the agent to take ACTIONS in the world.
    """
    
    @staticmethod
    def calculator(expression):
        """
        Evaluate a mathematical expression safely.
        
        Uses Python's ast module to parse and evaluate only math
        operations (no code execution risk).
        
        Args:
            expression: Math expression string (e.g., "2 + 3 * 4")
        
        Returns:
            Result as string
        """
        def _safe_eval(node):
            """Recursively evaluate an AST node, allowing only math ops."""
            if isinstance(node, ast.Expression):
                return _safe_eval(node.body)
            elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                return node.value
            elif isinstance(node, ast.BinOp):
                left = _safe_eval(node.left)
                right = _safe_eval(node.right)
                ops = {
                    ast.Add: lambda a, b: a + b,
                    ast.Sub: lambda a, b: a - b,
                    ast.Mult: lambda a, b: a * b,
                    ast.Div: lambda a, b: a / b if b != 0 else (_ for _ in ()).throw(ZeroDivisionError("Division by zero")),
                    ast.Pow: lambda a, b: a ** b,
                    ast.Mod: lambda a, b: a % b if b != 0 else (_ for _ in ()).throw(ZeroDivisionError("Modulo by zero")),
                    ast.FloorDiv: lambda a, b: a // b if b != 0 else (_ for _ in ()).throw(ZeroDivisionError("Division by zero")),
                }
                op_type = type(node.op)
                if op_type in ops:
                    return ops[op_type](left, right)
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            elif isinstance(node, ast.UnaryOp):
                operand = _safe_eval(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                elif isinstance(node.op, ast.UAdd):
                    return +operand
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            else:
                raise ValueError(f"Unsupported expression element: {type(node).__name__}")
        
        try:
            tree = ast.parse(expression, mode='eval')
            result = _safe_eval(tree)
            return str(result)
        except Exception as e:
            return f"Error: {str(e)}"
    
    @staticmethod
    def get_time():
        """Get the current time."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def search_knowledge(query, long_term_memory):
        """
        Search the agent's long-term memory for relevant facts.
        
        Args:
            query: What to search for
            long_term_memory: Reference to the agent's long-term memory
        
        Returns:
            Matching facts as a formatted string
        """
        results = long_term_memory.search(query)
        if results:
            facts = [f"  - {topic}: {fact}" for topic, fact in results]
            return "Found relevant memories:\n" + "\n".join(facts)
        return "No relevant memories found."
    
    @staticmethod
    def get_available_tools():
        """List all tools the agent can use."""
        return {
            "calculator": "Evaluate a math expression. Input: math expression string",
            "get_time": "Get the current date and time",
            "remember": "Store a fact in long-term memory. Input: 'topic | fact'",
            "recall": "Search memories. Input: search query",
            "forget": "Remove a memory. Input: topic to forget",
        }

# ============================================================================
# STEP 5: BUILD THE AGENT
# ============================================================================

class SimpleAgent:
    """
    A simple rule-based agent with memory and tools.
    
    TODO: Consider renaming to RuleBasedAgent or PatternMatchingAgent
    to more clearly convey the reasoning approach, especially if an
    LLM-backed agent class is added later.
    
    The agent follows a perceive -> think -> act -> observe loop:
    
    1. PERCEIVE: Receive user input
    2. THINK: Decide what action to take (using simple pattern matching)
    3. ACT: Execute the chosen tool or generate a response
    4. OBSERVE: Process the result and update memory
    """
    
    def __init__(self, name="Atlas"):
        self.name = name
        self.short_term = ShortTermMemory(max_messages=20)
        self.long_term = LongTermMemory(filepath="agent_memory.json")
        self.tools = AgentTools()
        self.conversation_count = 0
        
        print(f"Agent '{self.name}' initialized!")
        print(f"  Short-term memory: 20 messages")
        print(f"  Long-term memory: {len(self.long_term.get_all_memories())} stored facts")
        print(f"  Available tools: {', '.join(self.tools.get_available_tools().keys())}")
        print()
    
    def perceive(self, user_input):
        """Step 1: Receive and store the user's message."""
        self.short_term.add("user", user_input)
        self.conversation_count += 1
    
    def think(self, user_input):
        """
        Step 2: Decide what to do.
        
        This is a simple rule-based reasoning system.
        In a real agent, this would be an LLM making decisions.
        """
        user_lower = user_input.lower()
        
        # Check for memory-related commands
        if user_lower.startswith("remember ") or user_lower.startswith("remember:"):
            return "remember"
        
        if user_lower.startswith("recall ") or user_lower.startswith("recall:") or "what do you know about" in user_lower:
            return "recall"
        
        if user_lower.startswith("forget ") or user_lower.startswith("forget:"):
            return "forget"
        
        # Check for tool usage
        if any(op in user_input for op in ["+", "-", "*", "/"]) and any(c.isdigit() for c in user_input):
            return "calculator"
        
        if "what time" in user_lower or "what day" in user_lower or "current time" in user_lower:
            return "get_time"
        
        if "show memories" in user_lower or "list memories" in user_lower or "what do you remember" in user_lower:
            return "show_memories"
        
        if "clear memory" in user_lower:
            return "clear_memory"
        
        if "help" in user_lower or "what can you do" in user_lower:
            return "help"
        
        # Default: conversational response
        return "respond"
    
    def act(self, action, user_input):
        """Step 3: Execute the chosen action."""
        user_lower = user_input.lower()
        
        if action == "remember":
            # Parse: "remember topic | fact"
            content = user_input.split("remember", 1)[1].strip().lstrip(":").strip()
            if "|" in content:
                topic, fact = content.split("|", 1)
                self.long_term.store(topic.strip(), fact.strip())
                return f"Got it! I'll remember that {topic.strip()} is {fact.strip()}."
            else:
                # Auto-detect topic from user input
                self.long_term.store("user_fact", content)
                return f"Got it! I'll remember: '{content}'"
        
        elif action == "recall":
            query = user_input.replace("recall", "").replace(":", "").strip()
            if "what do you know about" in user_lower:
                query = user_lower.replace("what do you know about", "").strip().rstrip("?")
            results = self.long_term.search(query)
            if results:
                facts = "; ".join([f"{t}: {f}" for t, f in results])
                return f"I remember: {facts}"
            return f"I don't have any memories about '{query}'."
        
        elif action == "forget":
            topic = user_input.split("forget", 1)[1].strip().lstrip(":").strip()
            self.long_term.forget(topic)
            return f"I've forgotten about '{topic}'."
        
        elif action == "calculator":
            # Extract the math expression
            expr = "".join(c for c in user_input if c in "0123456789+-*/.() ")
            result = self.tools.calculator(expr)
            return f"The answer is: {expr} = {result}"
        
        elif action == "get_time":
            current_time = self.tools.get_time()
            return f"The current time is: {current_time}"
        
        elif action == "show_memories":
            memories = self.long_term.get_all_memories()
            if memories:
                items = [f"  - {k}: {v}" for k, v in memories.items()]
                return "Here's everything I remember:\n" + "\n".join(items)
            return "I don't have any long-term memories yet. Tell me something to remember!"
        
        elif action == "clear_memory":
            self.long_term.memories.clear()
            self.long_term._save()
            self.short_term.clear()
            return "All memories cleared. Fresh start!"
        
        elif action == "help":
            return self._get_help_message()
        
        else:
            return self._generate_response(user_input)
    
    def observe(self, response):
        """Step 4: Store the agent's response in short-term memory."""
        self.short_term.add("agent", response)
    
    def chat(self, user_input):
        """
        Full agent loop: perceive -> think -> act -> observe
        
        Args:
            user_input: The user's message
        
        Returns:
            Agent's response
        """
        # Step 1: Perceive
        self.perceive(user_input)
        
        # Step 2: Think (decide what action to take)
        action = self.think(user_input)
        
        # Step 3: Act (execute the action)
        response = self.act(action, user_input)
        
        # Step 4: Observe (store the response)
        self.observe(response)
        
        return response
    
    def _generate_response(self, user_input):
        """Generate a conversational response using context."""
        user_lower = user_input.lower()
        
        # Check if user previously told us their name
        stored_name = self.long_term.recall("user_name")
        
        # Simple pattern matching responses
        if stored_name and stored_name in user_input:
            return f"Yes, I remember! Your name is {stored_name}."
        
        if "my name is" in user_lower:
            name = user_input.split("my name is", 1)[1].strip().rstrip(".")
            self.long_term.store("user_name", name)
            return f"Nice to meet you, {name}! I'll remember your name."
        
        if "hello" in user_lower or "hi" in user_lower or "hey" in user_lower:
            greeting = f"Hello! I'm {self.name}"
            if stored_name:
                greeting += f", {stored_name}"
            greeting += "! How can I help you?"
            return greeting
        
        if "bye" in user_lower or "goodbye" in user_lower:
            return f"Goodbye! It was great chatting with you. I've had {self.conversation_count} messages in this conversation."
        
        # Default: acknowledge and offer help
        return (f"That's interesting! I'm a simple agent that can:\n"
                f"  - Remember things you tell me\n"
                f"  - Do math calculations\n"
                f"  - Tell you the time\n"
                f"  - Search my memories\n"
                f"Type 'help' to see everything I can do!")
    
    def _get_help_message(self):
        """Return the help message."""
        return f"""
I'm {self.name}, an AI agent with memory! Here's what I can do:

  MEMORY:
    - "Remember user_name | Alice"  -> Store a fact
    - "Recall user_name"            -> Look up a fact
    - "Forget user_name"            -> Remove a memory
    - "Show memories"               -> List all memories
    - "Clear memory"                -> Reset everything
    - "My name is Bob"              -> I'll remember your name!

  TOOLS:
    - "What is 25 * 4 + 10?"       -> Calculator
    - "What time is it?"            -> Current time

  GENERAL:
    - "Hello" / "Hi"                -> Greeting
    - "Help"                        -> This message
    - "Goodbye"                     -> End conversation

Try it! Tell me something to remember, ask me to calculate something, or just chat.
"""

# ============================================================================
# STEP 6: RUN THE AGENT
# ============================================================================

def run_demo():
    """Run a demonstration of the agent's capabilities."""
    
    agent = SimpleAgent(name="Atlas")
    
    # Demo conversation showing all features
    demo_messages = [
        "Hello!",
        "My name is Sarah",
        "Remember favorite_color | blue",
        "Remember hobby | playing guitar",
        "What is 42 * 7 + 15?",
        "What time is it?",
        "What do you know about Sarah?",
        "Show memories",
        "Recall favorite_color",
        "Goodbye!",
    ]
    
    print("=" * 70)
    print("DEMO CONVERSATION")
    print("=" * 70)
    print()
    
    for msg in demo_messages:
        print(f"User: {msg}")
        response = agent.chat(msg)
        print(f"{agent.name}: {response}")
        print()
        time.sleep(0.3)  # Small pause for readability
    
    print("=" * 70)
    print("END OF DEMO")
    print("=" * 70)

# ============================================================================
# STEP 7: INTERACTIVE MODE (OPTIONAL)
# ============================================================================

def run_interactive():
    """Run the agent in interactive mode."""
    
    agent = SimpleAgent(name="Atlas")
    
    print("=" * 70)
    print("INTERACTIVE MODE - Chat with the agent!")
    print("Type 'help' to see commands, 'quit' to exit.")
    print("=" * 70)
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"{agent.name}: Goodbye! It was great chatting!")
                break
            
            if not user_input:
                continue
            
            response = agent.chat(user_input)
            print(f"{agent.name}: {response}")
            print()
            
        except KeyboardInterrupt:
            print(f"\n{agent.name}: Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print()

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        run_interactive()
    else:
        run_demo()
        print()
        print("To chat interactively, run: python main.py --interactive")
