'''file that defines state and stateful widget states'''
from pluto.implementation import ContextWidget


class StatefulWidget(ContextWidget):
    '''class that handles mutable widget state'''
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
    def build(self):
        '''builds the mutable state of widget'''
        raise NotImplementedError
