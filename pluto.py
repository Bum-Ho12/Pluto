'''
this file contains script that manages the command line commands passed
to execute different instructions
'''
import sys
from runner import main as pluto_main
from pluto.core import pluto_verse_main

def main():
    '''
    checks type of instruction and handles passed as arguments
    and assigns correct scripts.
    '''
    if len(sys.argv) < 2:
        print("Usage: python pluto.py <command>")
        return

    command = sys.argv[1]

    if command == "run":
        pluto_main()
    elif command == "setup":
        pluto_verse_main()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
