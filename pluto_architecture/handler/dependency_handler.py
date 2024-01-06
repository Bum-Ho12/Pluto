'''
this file contains script that enable installation and handling of dependencies
necessary in the Pluto Project.
'''
import sys
import subprocess

def install_dependencies(dependencies):
    '''
    this method fetches dependencies from internet and installs them in your
    project.
    '''
    # pylint: disable = W1510:subprocess-run-check
    # subprocess.run([sys.executable,'-m','pip', 'install','--upgrade'], dependencies)
    for dependency in dependencies:
        # pylint: disable = W1510:subprocess-run-check
        subprocess.run([sys.executable,'-m','pip', 'install','--upgrade',dependency])

def main():
    '''the main function that handles dependency installation'''
    # installing PyYAML
    # pylint: disable = W1510:subprocess-run-check
    subprocess.run([sys.executable,'-m','pip', 'install', 'PyYAML'])

    # pylint: disable = W1514:unspecified-encoding
    with open('dep.yaml', 'r') as file:
        # pylint: disable = C0415:import-outside-toplevel
        import yaml
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
