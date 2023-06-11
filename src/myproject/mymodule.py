"""Test module with simple functions."""

import click


def print_message(message="Hello, world"):
    """Print a message given as a string."""
    print(message)


@click.command(description="Print hello world message to standard output.")
def hello_world():
    print_message()
