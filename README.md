# ChatGPT Introduction

This project introduces the use of ChatGPT and AI-assisted programming for debugging and problem-solving.

## Learning Objectives

- How to use ChatGPT for debugging code
- How to formulate effective questions for AI assistants
- How to interpret and implement AI-suggested solutions
- Understanding the limitations of AI-assisted programming
- Best practices for using AI tools in software development
- How to verify and test AI-generated code solutions

## Requirements

- Python 3.12.x
- GCC compiler for C programs
- Code follows PEP8 style guide (Python)
- Code follows Betty style guide (C)
- All files end with a new line
- First line of Python files: `#!/usr/bin/python3`

## Project Structure

### Debugging Tasks

The `debugging/` directory contains various debugging exercises:

| File | Description |
|------|-------------|
| `factorial.py` | Debug factorial calculation implementation |
| `factorial_recursive.py` | Debug recursive factorial function |
| `checkbook.py` | Debug a checkbook management program |
| `print_arguments.py` | Debug argument printing in Python |
| `print_arguments.c` | Debug argument printing in C |
| `tic.py` | Debug tic-tac-toe game implementation |
| `mines.py` | Debug minesweeper game logic |
| `change_background.html` | Debug HTML/CSS background functionality |

## Usage

### Python Scripts

```bash
cd debugging
./factorial.py
./factorial_recursive.py
./checkbook.py
./print_arguments.py arg1 arg2
```

### C Programs

```bash
cd debugging
gcc -Wall -Werror -Wextra -pedantic print_arguments.c -o print_arguments
./print_arguments arg1 arg2
```

### HTML Files

Open the HTML files in a web browser:

```bash
cd debugging
firefox change_background.html
# or
google-chrome change_background.html
```

## Debugging Process

1. **Identify the Problem**: Run the code and observe the error or unexpected behavior
2. **Ask ChatGPT**: Formulate a clear question describing the issue
3. **Analyze the Response**: Review ChatGPT's suggested solution
4. **Implement the Fix**: Apply the suggested changes
5. **Test**: Verify that the fix resolves the issue
6. **Document**: Keep track of what was learned

## Best Practices

- Always verify AI-suggested solutions before implementing them
- Test thoroughly after making changes
- Understand the solution, don't just copy-paste
- Use AI as a learning tool, not a replacement for understanding
- Cross-reference multiple sources when unsure

## Authors

- Alison Amblard
- Damien Rossi
- Yanis Leroy
- Valentin Planchon

Holberton School Project
