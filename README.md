# Inspect AI Evaluation Project

This project uses [Inspect AI](https://github.com/inspect-dev/inspect) to evaluate AI models on various tasks.

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer and resolver

## Setup

### Create and activate virtual environment

```bash
uv venv
```

### Install dependencies

```bash
uv pip install -e .
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
└── README.md                # This file
```


