'''file that defines state and stateful widget states'''
from pluto_architecture.implementation import ContextWidget


class StatefulWidget(ContextWidget):
    '''class that handles mutable widget state'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.execute_widget()

    def create_state(self):
        '''handles the mutable creation of state'''
        raise NotImplementedError


class StatelessWidget(ContextWidget):
    '''class that handles immutable widget state'''
    def build(self):
        '''builds the mutable state of widget'''
        raise NotImplementedError

class State(ContextWidget):
    '''Manages mutable state'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        '''builds the mutable state of widget'''
        raise NotImplementedError
