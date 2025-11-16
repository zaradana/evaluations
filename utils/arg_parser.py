import argparse
import os

import dotenv
import openai

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="openai/gpt-4o")
    return parser.parse_args()
