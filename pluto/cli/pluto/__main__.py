'''main file for CMD commands for Pluto'''
import click
from .commands import check_cmd

@click.group()
def cli():
    '''example'''


@cli.command()
def check():
    '''example'''
    check_cmd()

if __name__ == "__main__":
    cli()
