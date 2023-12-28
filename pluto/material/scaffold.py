'''scaffold widget for the application'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color

class Scaffold(BoxLayout):
    '''
    this widget handles the encapsulation of the entire application
    widgets in the application.
    '''
    def __init__(self, child, bounds=None, padding=(10, 10), margin=(10, 10), **kwargs):
        super(Scaffold, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = padding
        self.margin = margin

        # Define properties for the Scaffold
        self.child = child
        self.bounds = bounds or (0, 0, 100, 100)  # Default bounds, adjust as needed
        self.background_color = (0, 0, 0, 1)  # Replace with your desired background color

        # Create and add child widget
        self.child_widget = Widget()
        self.add_widget(self.child_widget)

    def add_widget_to_child(self, widget):
        '''Add a widget to the child widget'''
        self.child_widget.add_widget(widget)

    def on_background_color(self, instance, value):
        '''Update the background color when the background_color property changes'''
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*value)
            Rectangle(pos=self.pos, size=self.size)

    def on_size(self, instance, value):
        '''Update the child widget size when the size of the Scaffold changes'''
        self.child_widget.size = value

    def on_pos(self, instance, value):
        '''Update the child widget position when the position of the Scaffold changes'''
        self.child_widget.pos = value
