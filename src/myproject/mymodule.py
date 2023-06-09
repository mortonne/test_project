"""Test module with simple functions."""

import click


@click.command()
def hello_world():
    print("Hello, world.")
