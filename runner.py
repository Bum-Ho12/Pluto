'''
this file runs the project application
defined in main.py
'''
import os
import sys
import subprocess
from pathlib import Path
from watchgod import watch
from main import RunApp


def reload():
    """
    Restarts the Python interpreter. This function is needed to apply changes to Python files.
    """
    print("Reloading...")
    python = sys.executable
    os.execl(python, python, *sys.argv)


def watch_for_changes():
    """
    Watch for changes in the project directory and trigger a reload when changes are detected.
    """
    project_dir = Path(__file__).parent.resolve()
    watched_dirs = [project_dir]

    for changes in watch(watched_dirs):
        print("Changes detected:")
        for change_type, change_path in changes:
            print(f"  {change_type.name}: {change_path}")
        reload()


def main():
    '''
    this method execute the application
    by taking advantage  of the kivy package.
    '''
    app = RunApp()

    app.run()

if __name__ == '__main__':
    # Start a separate thread to watch for changes in the project directory
    subprocess.Popen([sys.executable, __file__, 'watch_for_changes'])
    main()
