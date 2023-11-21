'''
this file contains script that enable installation and handling of dependencies
necessary in the Pluto Project.
'''
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

def main():
    '''the main function that handles dependency installation'''
    # pylint: disable = W1514:unspecified-encoding
    with open('dep.yaml', 'r') as file:
        data = yaml.safe_load(file)
        dependencies = data.get('dependencies', [])

    if dependencies:
        print("<<<< installing dependencies from dep.yaml >>>>")
        install_dependencies(dependencies)
        print("<<<<<<<<< Dependencies installed successfully. >>>>>>>>>>>>")
    else:
        print("<<<<<<<<< No dependencies found in dependencies.yaml. >>>>>>>>>>>>")

if __name__ == "__main__":
    main()
