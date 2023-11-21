'''
this file contains script that enable installation and handling of dependencies
necessary in the Pluto Project.
'''
import os
import sys
import subprocess
import yaml

def install_dependencies(dependencies):
    '''
    this method fetches dependencies from internet and installs them in your
    project.
    '''
    for dependency in dependencies:
        # pylint: disable = W1510:subprocess-run-check
        subprocess.run(['pip', 'install', dependency])



def create_virtual_environment():
    '''Create a Python virtual environment'''
    # pylint: disable = W1510:subprocess-run-check
    subprocess.run(['python', '-m', 'venv', 'pluto_env'])

def activate_virtual_environment():
    '''Activate the Python virtual environment'''
    venv_path = os.path.join(os.getcwd(), 'venv')
    activate_script = os.path.join(venv_path, 'Scripts'
                        if sys.platform == 'win32' else 'bin', 'activate')
    activate_cmd = f'"{activate_script}"'
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

    # pylint: disable = W1514:unspecified-encoding
    with open('dep.yaml', 'r') as file:
        data = yaml.safe_load(file)
        dependencies = data.get('dependencies', [])

    if dependencies:
        print("<<<< installing dependencies from dep.yaml >>>>")
        install_dependencies(dependencies)
        print("<<<<<<<<< Dependencies installed successfully. >>>>>>>>>>>>")
    else:
        print("<<<<<<<<< No dependencies found in dep.yaml. >>>>>>>>>>>>")

if __name__ == "__main__":
    main()
