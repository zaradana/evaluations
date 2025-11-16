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

Activate the virtual environment manually:

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
inspect eval tasks/hello_world.py --model openai/gpt-4o
```

Or run it directly with Python:

```bash
python tasks/hello_world.py --model openai/gpt-4o
```

To run a task on a partial dataset, use the `--limit` flag:

```bash
inspect eval tasks/math.py --model openai/gpt-4o --limit 10
```
or to run on a specific range of examples:

```bash
inspect eval ./tasks/math.py --limit 100-200 -T shuffle=false --model openai/gpt-4o
```

## Development

### Linting and Formatting

This project uses [ruff](https://github.com/astral-sh/ruff) for linting and formatting. Pre-commit hooks are configured to run automatically on commit.

To manually run linting:

```bash
ruff check .
ruff format .
```

Or run pre-commit on all files:

```bash
pre-commit run --all-files
```


