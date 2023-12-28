'''file defines the ptx "jsx format for python" for Pluto framework'''

# Custom decorator for JSX-like syntax
def ptx(component_func):
    '''wrapper that defines the ptx format for Pluto'''
    def wrapper(*args, **kwargs):
        # Instantiate the component class or return the function result
        return component_func(*args, **kwargs)
    return wrapper
