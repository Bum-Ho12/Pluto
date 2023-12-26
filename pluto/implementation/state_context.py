'''this file handles state management in the framework'''

class StateContext:
    '''this class defines the state context of the framework'''
    def __init__(self):
        '''method that execute the widget inside '''
        self.state = {}

    def get_state(self, key):
        '''method that execute the widget inside '''
        return self.state.get(key)

    def set_state(self, key, value):
        '''method that execute the widget inside '''
        self.state[key] = value
