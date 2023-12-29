'''
this file defines the AppBar widget that can be used to
define the top bar in pluto framework
'''

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from pluto.implementation import context_manager

@context_manager
class AppBar(BoxLayout):
    '''
    This class defines a custom AppBar widget.
    It can contain a title, and you can customize its appearance.
    '''
    def __init__(
        self, title=None, background_color=(0, 0, 0, 1),
        height=56, orientation='horizontal', **kwargs
    ):
        super(AppBar, self).__init__(**kwargs)
        self.orientation = orientation
        self.size_hint_y = None
        self.height = height

        # Create and add a title Text widget
        if title:
            self.add_widget(title)

        # Customize the background color
        with self.canvas.before:
            Color(*background_color)
            Rectangle(pos=self.pos, size=self.size)

    def set_title(self, title):
        '''Set the title widget of the AppBar'''
        if self.children:
            # If there are existing children (e.g., a previous title), remove them
            self.clear_widgets()

        self.add_widget(title)
