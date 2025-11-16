import os
from inspect_ai import Task, task, eval
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import (               
  chain_of_thought, generate, self_critique   
)   
import openai
import dotenv
import argparse

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="openai/gpt-4o")
    return parser.parse_args()

@task
def theory_of_mind():
    return Task(
        dataset=example_dataset("theory_of_mind"),
        solver=[
          chain_of_thought(),
          generate(),
          self_critique()
        ],
        scorer=model_graded_fact(),
    )


if __name__ == "__main__":
    args = arg_parser()
    model = args.model
    print(f"Model: {model}")
    result = eval(theory_of_mind(), model=model)
    print(result)
    
