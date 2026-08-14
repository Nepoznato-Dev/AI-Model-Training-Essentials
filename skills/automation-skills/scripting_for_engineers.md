---
# Metadata
title: "Scripting for Engineers"
description: "Write robust, maintainable automation scripts with proper error handling, argument parsing, logging, and testing for engineering workflows."
category: "Automation Skills"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2026-08-10"
reviewed_by: "Automation Skills Team"
next_review: "2027-02-10"

# Classification
tags: [scripting, python, bash, error-handling, automation, maintainability]
difficulty_level: "beginner"
prerequisites:
  - "Basic Python or Bash knowledge"
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Scripting for Engineers

Write scripts that are reliable, readable, and maintainable — the foundation of all automation.

## Overview

Every engineer writes scripts. The difference between a throwaway prototype and a production automation is a handful of practices: argument parsing, error handling, logging, and basic testing. These practices add maybe 15 minutes to development time but save hours of debugging and prevent silent failures.

This skill covers the patterns that elevate scripts from "it works on my machine" to "it works reliably in production." It focuses on Python (the most common scripting language in engineering) with patterns applicable to any language.

The core principle: **write scripts for the person who will debug them at 3 AM — that person might be future-you.**

## Quick-Start Checklist

Every script you write should have these five things:

```python
#!/usr/bin/env python3
"""One-line description of what this script does."""

import argparse
import logging
import sys

# 1. Argument parsing — make the script configurable
# 2. Logging — replace print() with structured logging
# 3. Error handling — catch specific exceptions, not bare except
# 4. Exit codes — return meaningful status codes
# 5. Main guard — if __name__ == "__main__" for importability
```

## Core Competencies

- **Argument Parsing**: Make scripts flexible without editing source code — use `argparse` for flags, options, and help text
- **Error Handling**: Catch specific exceptions with meaningful messages instead of bare `except:` that hides bugs
- **Logging**: Replace `print()` with structured logging that includes timestamps, severity levels, and context
- **Exit Codes**: Return meaningful status codes so calling scripts and CI systems can detect success vs failure
- **File Handling**: Use context managers (`with` statements) and handle missing files, permissions, and encoding issues

## When to Use

- Writing any script longer than 20 lines
- Automating file processing, data transformation, or system tasks
- Building tools that other team members will use
- Creating scripts that will run in production or CI/CD pipelines
- Replacing manual multi-step processes with a single command

## Framework/Methodology

### The Five Pillars of Robust Scripts

#### 1. Argument Parsing

```python
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Process experiment results and generate summary report.",
        epilog="Example: python process_results.py --input data/ --output reports/ --format pdf"
    )
    parser.add_argument("--input", "-i", required=True, help="Input directory containing experiment data")
    parser.add_argument("--output", "-o", default="./reports", help="Output directory for reports (default: ./reports)")
    parser.add_argument("--format", "-f", choices=["pdf", "html", "csv"], default="pdf", help="Output format (default: pdf)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without executing")
    return parser.parse_args()
```

**Why this matters**: Scripts without argument parsing require editing source code to change behavior. This leads to accidental commits of personal paths, broken scripts for other users, and no self-documentation.

#### 2. Structured Logging

```python
import logging

def setup_logging(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)-8s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

# Usage
logging.info("Processing started")           # Normal operation messages
logging.debug("Loaded 1,234 records")        # Detailed info for debugging
logging.warning("Config file not found, using defaults")  # Something unexpected
logging.error("Failed to connect to database: {e}")       # Something broke
```

**Replace print() because**:
- Logs include timestamps automatically
- Severity levels let you filter output
- Logs can be directed to files without changing code
- Other tools can parse structured logs

#### 3. Specific Error Handling

```python
# BAD — catches everything, hides bugs
try:
    process_data()
except:
    print("Error")

# BAD — too broad
try:
    process_data()
except Exception as e:
    print(f"Error: {e}")

# GOOD — specific, informative, actionable
try:
    process_data(input_path)
except FileNotFoundError as e:
    logging.error(f"Input file not found: {input_path}. Check the --input argument.")
    sys.exit(1)
except PermissionError as e:
    logging.error(f"Permission denied accessing: {e.filename}. Check file permissions.")
    sys.exit(1)
except json.JSONDecodeError as e:
    logging.error(f"Invalid JSON in input file at line {e.lineno}, column {e.colno}.")
    sys.exit(1)
```

#### 4. Meaningful Exit Codes

```python
# Standard exit codes
sys.exit(0)  # Success
sys.exit(1)  # General error
sys.exit(2)  # Misuse of command (bad arguments)

# Custom exit codes for workflows
EXIT_SUCCESS = 0
EXIT_CONFIG_ERROR = 10
EXIT_DATA_ERROR = 20
EXIT_NETWORK_ERROR = 30

# Usage in calling scripts (bash)
# if ! python process.py --input data/; then
#     echo "Processing failed"
#     exit 1
# fi
```

#### 5. Safe File Handling

```python
from pathlib import Path

# GOOD — uses context manager, handles encoding
def read_config(config_path: str) -> dict:
    path = Path(config_path)
    if not path.exists():
        logging.error(f"Config file not found: {config_path}")
        sys.exit(1)
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# GOOD — atomic write (prevents partial files on crash)
def write_output(data: str, output_path: str):
    path = Path(output_path)
    temp_path = path.with_suffix(".tmp")
    
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(data)
    
    temp_path.rename(path)  # Atomic on most filesystems
    logging.info(f"Written output to {output_path}")
```

### Script Template

```python
#!/usr/bin/env python3
"""
[Script Name] — [One-line description]

Usage:
    python script_name.py --input <path> [--output <path>] [--verbose]

Examples:
    python script_name.py --input data/raw/
    python script_name.py --input data/raw/ --output reports/ --verbose
"""

import argparse
import logging
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", "-i", required=True, help="Input path")
    parser.add_argument("--output", "-o", default="./output", help="Output path (default: ./output)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def process(input_path: Path, output_path: Path) -> None:
    """Main processing logic."""
    # Your logic here
    pass


def main():
    args = parse_args()
    
    # Setup
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)-8s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    # Validate inputs
    if not input_path.exists():
        logging.error(f"Input path does not exist: {input_path}")
        sys.exit(1)
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Execute
    try:
        logging.info(f"Processing: {input_path} → {output_path}")
        process(input_path, output_path)
        logging.info("Completed successfully")
    except Exception as e:
        logging.error(f"Processing failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Bare `except:` clauses | Hides bugs, makes debugging impossible | Always catch specific exception types |
| Using `print()` instead of logging | No timestamps, no severity levels, can't redirect to file | Use `logging` module from the start |
| Hardcoded paths | Script breaks on different machines or users | Use arguments, config files, or environment variables |
| No `if __name__ == "__main__"` guard | Importing the script executes it | Always use the main guard pattern |
| Not checking if files exist before reading | Cryptic errors instead of clear messages | Validate inputs at the start with clear error messages |
| Writing output directly (non-atomic) | Partial files on crash corrupt downstream processes | Write to temp file, then rename |
| No exit codes | Calling scripts can't detect success vs failure | Always `sys.exit(0)` on success, `sys.exit(1)` on failure |

## Best Practices

1. **Start with the template.** Copy the script template above for every new script. The 30 seconds of setup saves hours later.

2. **Validate inputs early.** Check that files exist, directories are writable, and required arguments are provided — before doing any real work. Fail fast with clear messages.

3. **Use `pathlib` over `os.path`.** It's more readable, cross-platform, and handles edge cases better:
```python
# BAD
output = os.path.join(os.path.dirname(input_file), "output", filename)

# GOOD
output = Path(input_file).parent / "output" / filename
```

4. **Handle encoding explicitly.** Always specify `encoding="utf-8"` when opening text files. The default varies by OS and locale.

5. **Make scripts importable.** The `if __name__ == "__main__"` guard lets other scripts import your functions for reuse.

6. **Add a `--dry-run` flag.** For any script that modifies files or state, a dry-run mode that shows what would happen (without doing it) is invaluable for testing.

## Tools & Resources

- **[argparse](https://docs.python.org/3/library/argparse.html)** - Built-in argument parsing (no install needed)
- **[click](https://click.palletsprojects.com/)** - Higher-level CLI creation with decorators
- **[rich](https://rich.readthedocs.io/)** - Beautiful terminal output with progress bars and tables
- **[pathlib](https://docs.python.org/3/library/pathlib.html)** - Object-oriented filesystem paths
- **[shutil](https://docs.python.org/3/library/shutil.html)** - High-level file operations

## Success Indicators

You've mastered scripting when:

- Every script you write has argument parsing, logging, and error handling by default
- Other people can use your scripts without reading the source code (help text is sufficient)
- Your scripts fail with clear, actionable error messages
- Scripts are safely re-runnable and don't corrupt data on partial failure
- You instinctively use context managers and pathlib for file operations

## Related Skills

- [Workflow Automation](workflow_automation.md) - Composing scripts into automated workflows
- [Programming Fundamentals](../technical-skills/programming_fundamentals.md) - Core programming concepts
- [Debugging](../behavior-skills/debugging.md) - Investigating script failures systematically
