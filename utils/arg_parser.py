import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="openai/gpt-4o")
    return parser.parse_args()
