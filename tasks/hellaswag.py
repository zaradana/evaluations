from inspect_ai import Task, eval, task
from inspect_ai.dataset import Sample, hf_dataset
from inspect_ai.scorer import choice
from inspect_ai.solver import multiple_choice, system_message

from utils.arg_parser import arg_parser

SYSTEM_MESSAGE = """
Choose the most plausible continuation for the story.
"""


def record_to_sample(record):
    return Sample(
        input=record["ctx"],
        target=chr(ord("A") + int(record["label"])),
        choices=record["endings"],
        metadata={"source_id": record["source_id"]},
    )


@task
def hellaswag():
    # dataset
    dataset = hf_dataset(
        path="hellaswag", split="validation", sample_fields=record_to_sample, trust=True
    )

    # define task
    return Task(
        dataset=dataset,
        solver=[system_message(SYSTEM_MESSAGE), multiple_choice()],
        scorer=choice(),
    )


if __name__ == "__main__":
    args = arg_parser()
    result = eval(hellaswag(), model=args.model)
    print(result)
