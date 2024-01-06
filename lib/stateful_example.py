'''example implementation of stateful widget'''
from kivy.uix.floatlayout import FloatLayout
from pluto_architecture.implementation.state_widgets import State, StatefulWidget
from pluto_architecture.material.button import CustomButton
from pluto_architecture.material.text import Text

# pylint:disable = E1101
class CounterWidgetState(State):
    '''
    an example class to showcase how to use
    StatefulWidget and State
    '''
    def __init__(self, widget, initial_count=0):
        super().__init__(widget)
        self._count = initial_count
        self.button = CustomButton(text='Click me',
                on_click=self.increment,
                context=self.widget._context)

        # Schedule the text update using context manager's clock
        self.widget._context.schedule_clock_event(self.update_text, 1)

    def increment(self):
        '''method that increases the counter'''
        self._count += 1
        self.widget.request_build()

    # pylint: disable = W0212,W0613
    def update_text(self, dt):
        '''updates state'''
        # Update the shared state, triggering the on_text event in Text widget
        self.widget._context.set_state('text', str(self._count))

    def build(self):
        return Text(text=str(self._count), context=self.widget._context)

class CounterWidget(FloatLayout, StatefulWidget):
    '''final widget to integrate into main.py'''
    def create_state(self):
        return CounterWidgetState(self)

    def request_build(self):
        '''builds'''
        self.build()

    # pylint:disable = W0221
    def add_widget(self, widget, **kwargs):
        '''
        Override add_widget to ensure compatibility with Kivy's widget structure
        '''
        return super(CounterWidget, self).add_widget(widget, **kwargs)
