from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import exact
from inspect_ai.solver import generate
import argparse
import dotenv
import os
import openai

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="openai/gpt-4o")
    return parser.parse_args()

@task
def hello_world():
    return Task(
        dataset=[
            Sample(
                input="Just reply with Hello World",
                target="Hello World",
            )
        ],
        solver=[generate()],
        scorer=exact(),
    )

if __name__ == "__main__":
    args = arg_parser()
    model = args.model
    result = eval(hello_world(), model=model)
    print(result)
