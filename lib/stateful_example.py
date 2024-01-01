'''example implementation of stateful widget'''

from pluto.implementation.state_widgets import State, StatefulWidget
from pluto.material.button import CustomButton
from pluto.material.text import Text

class CounterWidgetState(State):
    '''
    an example class to showcase how to use
    StatefulWidget and State
    '''
    # pylint: disable = E1101
    def __init__(self, widget, initial_count=0):
        super().__init__(widget)
        self._count = initial_count
        self.button = CustomButton(text='Click me',
                on_click=self.increment,
                context=self.widget._context)

    def increment(self):
        '''method that increases the counter'''
        self._count += 1
        self.widget.request_build()

    # pylint: disable = W0212
    def build(self):
        return Text(text=str(self._count), context=self.widget._context)

# pylint: disable = E1101
class CounterWidget(StatefulWidget):
    '''final widget to integrate into main.py'''
    def create_state(self):
        return CounterWidgetState(self)

    def request_build(self):
        '''builds'''
        self.build()

    def add_widget(self, widget, **kwargs):
        '''
        Override add_widget to ensure compatibility with Kivy's widget structure
        '''
        return super(CounterWidget, self).add_widget(widget, **kwargs)
