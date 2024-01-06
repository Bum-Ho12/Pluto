'''example that shows how to use StatelessWidget'''
from pluto_architecture.implementation.state_widgets import StatelessWidget
from pluto_architecture.material.text import Text


class GreetingWidget(StatelessWidget):
    '''
    class example of how to extend
    StatelessWidget and utilize it
    '''
    def build(self):
        return Text(text=f"Hello, {self._context.get_state('name')}!", context=self._context)
