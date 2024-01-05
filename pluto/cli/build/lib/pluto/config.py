'''pluto/config.py'''
import toml

def read_config():
    '''reads config file'''
    # pylint:disable =W1514
    with open("pyproject.toml") as f:
        config = toml.load(f)
        return config.get("tool", {}).get("pluto", {})
