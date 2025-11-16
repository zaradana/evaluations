from inspect_ai import Task, eval, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import match
from inspect_ai.solver import generate, use_tools
from inspect_ai.tool import tool

from utils.arg_parser import arg_parser


@tool
def add():
    async def execute(x: int, y: int):
        """
        Add two numbers.

        Args:
            x: First number to add.
            y: Second number to add.

        Returns:
            The sum of the two numbers.
        """
        return x + y

    return execute


@task
def addition_problem():
    return Task(
        dataset=[Sample(input="What is 1 + 1?", target=["2", "2.0"])],
        solver=[use_tools(add()), generate()],
        scorer=match(numeric=True),
    )


if __name__ == "__main__":
    args = arg_parser()
    result = eval(addition_problem(), model=args.model)
    print(result)
