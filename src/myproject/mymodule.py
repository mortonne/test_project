"""Test module with simple functions."""

import click


def print_message(message="Hello, world"):
    """Print a message given as a string."""
    print(message)


@click.command()
def hello_world():
    print_message()
