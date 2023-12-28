'''scaffold widget for the application'''
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from pluto.material.app_bar import AppBar
from pluto.material.container import Container

class Scaffold(BoxLayout):
    '''
    This widget handles the encapsulation of the entire application
    widgets in the application.
    '''
    def __init__(
        self, app_bar=None, body=None,
        orientation='vertical',
        padding=(10, 10), margin=(10, 10),
        **kwargs
    ):
        super(Scaffold, self).__init__(**kwargs)
        self.orientation = orientation
        self.padding = padding
        self.margin = margin

        # Define properties for the Scaffold
        self.app_bar = AppBar() if app_bar is None else app_bar
        self.body = Container() if body is None else body
        self.bounds = (0, 0, 100, 100)  # Default bounds, adjust as needed
        self.background_color = (0, 0, 0, 1)  # Replace with your desired background color

        # Add app_bar and body to the Scaffold
        self.add_widget(self.app_bar)
        self.add_widget(self.body)

    def on_background_color(self, instance, value):
        '''Update the background color when the background_color property changes'''
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*value)
            Rectangle(pos=self.pos, size=self.size)

    def on_size(self, instance, value):
        '''Update the body widget size when the size of the Scaffold changes'''
        self.body.size = value

    def on_pos(self, instance, value):
        '''Update the body widget position when the position of the Scaffold changes'''
        self.body.pos = value