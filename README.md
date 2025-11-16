# Inspect AI Evaluation Project

This project uses [Inspect AI](https://github.com/inspect-dev/inspect) to evaluate AI models on various tasks.

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Setup

### Install dependencies and set up environment

Simply run:

```bash
uv sync
```

This will:
- Create a virtual environment (if it doesn't exist)
- Install all dependencies from `pyproject.toml`
- Create/update `uv.lock` for reproducible builds

The virtual environment will be automatically activated in your shell. If you need to activate it manually:

```bash
source .venv/bin/activate
```

### Configure environment variables

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running a task

Run the theory of mind evaluation task:

```bash
inspect eval tasks/theory_of_mind.py --model openai/gpt-4o
```

Or run it directly with Python:

```bash
python tasks/theory_of_mind.py --model openai/gpt-4o
```

## Project Structure

```
inspect/
├── tasks/
│   └── theory_of_mind.py    # Theory of mind evaluation task
├── data/                    # Dataset files
├── logs/                    # Evaluation logs
├── pyproject.toml           # Project configuration and dependencies
├── uv.lock                  # Lock file for reproducible builds (auto-generated)
└── README.md                # This file
```


