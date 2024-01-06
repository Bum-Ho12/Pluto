#!/usr/bin/env python
'''
this file contains script that manages the command line commands passed
to execute different instructions
'''

# import sys
import click
from pluto_architecture.core import pluto_verse_env

@click.command()
@click.argument('command', default='run', required=False)
def main(command):
    '''
    checks type of instruction and handles passed as arguments
    and assigns correct scripts.
    '''

    # pylint: disable = C0415:import-outside-toplevel
    if command == "run":
        from runner import main as pluto_main
        pluto_main()
    elif command == "setup":
        pluto_verse_env()
    elif command == 'context':
        from pluto_architecture.tests import test_context_manager
        test_context_manager()
    elif command == 'decorator-main':
        from pluto_architecture.tests import context_decorator_test
        context_decorator_test()
    elif command =="fetch":
        from pluto_architecture.handler import pluto_verse_main
        pluto_verse_main()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    # pylint:disable = E1120
    main()
