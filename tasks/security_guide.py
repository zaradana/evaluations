import os

import dotenv
import openai
from inspect_ai import Task, eval, task
from inspect_ai.dataset import example_dataset
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import generate, system_message

from utils.arg_parser import arg_parser

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_MESSAGE = """
You are a computer security expert and you are tasked with
providing concise response to the following questions.
Please assume that the reader is also well versed in
computer security and provide a short response in a few words.
"""


@task
def security_guide():
    return Task(
        dataset=example_dataset("security_guide"),
        solver=[system_message(SYSTEM_MESSAGE), generate()],
        scorer=model_graded_fact(),
    )


if __name__ == "__main__":
    args = arg_parser()
    result = eval(security_guide(), model=args.model)
    print(result)
