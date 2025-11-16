import os

import dotenv
import openai
from inspect_ai import Task, eval, task
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import chain_of_thought, generate, self_critique

from utils.arg_parser import arg_parser

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


@task
def theory_of_mind():
    return Task(
        dataset=example_dataset("theory_of_mind"),
        solver=[chain_of_thought(), generate(), self_critique()],
        scorer=model_graded_fact(),
    )


if __name__ == "__main__":
    args = arg_parser()
    result = eval(theory_of_mind(), model=args.model)
    print(result)
