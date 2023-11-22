'''
this file contains script that enable installation and handling of dependencies
necessary in the Pluto Project.
'''
import os
import sys
import subprocess


def create_virtual_environment():
    '''Create a Python virtual environment'''
    # pylint: disable = W1510:subprocess-run-check
    subprocess.run([sys.executable, '-m', 'venv', 'pluto_env'])

def activate_virtual_environment():
    '''Activate the Python virtual environment'''
    venv_path = os.path.join(os.getcwd(), 'pluto_env')

    # Determine the platform-specific activation script
    activate_script = 'activate' if sys.platform == 'win32' else 'activate'

    if sys.platform == 'win32':
        activate_script_path = os.path.join(venv_path,'Scripts',activate_script)
        os.environ['VIRTUAL_ENV'] = venv_path
        os.environ['PATH'] = f"{venv_path}/Scripts;{os.environ['PATH']}"
    else:
        activate_script_path = os.path.join(venv_path, 'bin', activate_script)
        os.environ['VIRTUAL_ENV'] = venv_path
        os.environ['PATH'] = f"{venv_path}/bin:{os.environ['PATH']}"
    # activate_script_path = os.path.join(venv_path, 'Scripts'
    #                     if sys.platform == 'win32' else 'bin', activate_script)

    # Set the appropriate command based on the platform
    if sys.platform == 'win32':
        activate_cmd = f'cmd /k "{activate_script_path}"'
    else:
        activate_cmd = f'source "{activate_script_path}"'

    # pylint: disable = W1510:subprocess-run-check
    subprocess.run(activate_cmd, shell=True)

def main():
    '''the main function that handles dependency installation'''
        # Check if a virtual environment is present
    venv_path = os.path.join(os.getcwd(), 'pluto_env')
    if not os.path.exists(venv_path):
        print("<<<< Creating virtual environment 'pluto_env' >>>>")
        create_virtual_environment()
        print("<<<< Virtual environment created successfully 'pluto_env' >>>>")

    # Activate the virtual environment
    activate_virtual_environment()


if __name__ == "__main__":
    main()
