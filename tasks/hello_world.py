from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import exact
from inspect_ai.solver import generate

from utils.arg_parser import arg_parser


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
    result = eval(hello_world(), model=args.model)
    print(result)
