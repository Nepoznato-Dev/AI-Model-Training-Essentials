# Simple Agent with Memory

A basic conversational agent with short-term and long-term memory, tools (calculator, time lookup), and a perceive-think-act-observe loop.

## What This Project Does

This project demonstrates how to build an AI agent that:
- Maintains **short-term memory** (recent conversation history) and **long-term memory** (persistent facts across sessions)
- Uses **tools** — a calculator, time lookup, and knowledge search — to take actions
- Follows a structured **perceive → think → act → observe** loop
- Recognizes user patterns (greetings, name introductions, math expressions, memory commands)

## Concepts Covered

- Agent architecture (perceive-think-act-observe loop)
- Short-term memory with bounded deque
- Long-term memory with JSON persistence
- Tool use and pattern-matching reasoning
- Case-insensitive input handling

## Prerequisites

- Basic Python programming
- No external dependencies required (stdlib only)

## Quick Start

```bash
# Navigate to this project directory
cd guides/Agentic_Systems/projects/simple_agent_memory

# Install dependencies (none required — stdlib only)
pip install -r requirements.txt

# Run the demo
python main.py

# Run interactively
python main.py --interactive
```

## Files in This Project

| File | Description |
|------|-------------|
| `main.py` | Full agent implementation (~300 lines, heavily commented) |
| `requirements.txt` | No external dependencies (stdlib only) |
| `README.md` | This documentation file |

## How It Works

### Memory Systems

- **ShortTermMemory** — A `deque(maxlen=20)` that stores the most recent conversation messages with timestamps.
- **LongTermMemory** — A JSON-backed dictionary that persists facts (topic → fact mappings) across sessions. Supports store, recall, search, and forget operations.

### Tools

| Tool | Description |
|------|-------------|
| `calculator` | Safely evaluates math expressions using Python's `ast` module |
| `get_time` | Returns the current date and time |
| `search_knowledge` | Searches long-term memory for relevant facts |

### Agent Loop

1. **Perceive** — Receive user input and store it in short-term memory.
2. **Think** — Pattern-match the input to decide which action to take.
3. **Act** — Execute the chosen tool or generate a conversational response.
4. **Observe** — Store the agent's response in short-term memory.

## Example Interaction

```
User: My name is Sarah
Atlas: Nice to meet you, Sarah! I'll remember your name.

User: Remember favorite_color | blue
Atlas: Got it! I'll remember that favorite_color is blue.

User: What is 42 * 7 + 15?
Atlas: The answer is: 42 * 7 + 15 = 309

User: Recall favorite_color
Atlas: I remember: favorite_color: blue
```

## Exercises

1. Add a new tool (e.g., a unit converter or weather lookup stub)
2. Increase the short-term memory capacity and observe the behavior
3. Add a "forget all" command that clears only long-term memory
4. Implement fuzzy matching for the recall command

## Next Steps

- Read the full [Agentic Systems Guide](../../) for deeper theory
- Explore multi-agent patterns (planned for future projects in this directory)
- Check [Common Errors](../../../errors/) if you get stuck

## Project Stats

| Metric | Value |
|--------|-------|
| Lines of Code | ~300 |
| Time to Complete | 15-20 minutes |
| GPU Required | No |
| Difficulty | ⭐☆☆ Beginner |
| Prerequisites | Basic Python |
