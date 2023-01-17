"""
A simple python script to ask gpt-3 for a response. 
It defaults to asking for bash commands

It uses the openai api to ask for a response.
It uses argparse to parse the optional command line arguments.
"""

import argparse
import os
import openai

# Parse the command line arguments
def main():
    parser = argparse.ArgumentParser()
    # make a default parameter where if arguments are given but no flag is given it will use the default
    parser.add_argument("prompt", type=str)
    # parser.add_argument("--temperature", type=float, default=0.9)
    parser.add_argument("--max_tokens", type=int, default=100)
    parser.add_argument("--top_p", type=float, default=1)
    # parser.add_argument("--frequency_penalty", type=float, default=0)
    # parser.add_argument("--presence_penalty", type=float, default=0)
    # parser.add_argument("--stop", type=str, default="STOP")
    # engine default to instruct
    parser.add_argument("--engine", type=str, default="davinci-instruct-beta")
    args = parser.parse_args()

    # Set the openai from the environment variable
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Ask for a response
    response = openai.Completion.create(
        engine=args.engine,
        prompt="Convert this text to a bash command:\nlist files in the parent dir \nls -l\n" + args.prompt,
        # temperature=args.temperature,
        max_tokens=args.max_tokens,
        top_p=args.top_p,
        # frequency_penalty=args.frequency_penalty,
        # presence_penalty=args.presence_penalty,
        # stop=args.stop,
    )
    print(response.choices[0].text)


if __name__ == "__main__":
    main()

