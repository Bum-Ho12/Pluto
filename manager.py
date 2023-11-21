'''
PlutoVerse handles dependency management in the Pluto Framework
'''
import subprocess
import json

class PlutoVerse:
    '''
    this class is the primary class that handles dependency management
    for the Pluto Framework.
    '''
    def __init__(self):
        self.dependencies = {}

    def add_dependency(self, package_name, version):
        '''
        adds dependency to the Pluto Framework.
        '''
        self.dependencies[package_name] = version

    def install_dependencies(self):
        '''
        this method fetches dependencies from internet and installs them in your
        project.
        '''
        for package, version in self.dependencies.items():
            command = f"pip install {package}=={version}"
            # pylint: disable = W1510:subprocess-run-check
            subprocess.run(command, shell=True)

    def save_to_file(self, filename='dependencies.json'):
        '''
        this method adds dependencies to a json trackable file named dependencies.json
        '''
        # pylint: disable = W1514:unspecified-encoding
        with open(filename, 'w') as file:
            json.dump(self.dependencies, file)

    def load_from_file(self, filename='dependencies.json'):
        '''
        this method loads the dependencies to the project
        from the dependencies.json file.
        '''
        # pylint: disable = W1514:unspecified-encoding
        with open(filename, 'r') as file:
            self.dependencies = json.load(file)

# Example usage:
dependency_manager = PlutoVerse()

# Add dependencies
dependency_manager.add_dependency('kivy', '2.2.1')
dependency_manager.add_dependency('other_dependency', '1.0.0')

# Save dependencies to a file
dependency_manager.save_to_file()

# Load dependencies from a file
dependency_manager.load_from_file()

# Install dependencies
dependency_manager.install_dependencies()
