'''file that defines the Container class widget'''
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color

class Container(FloatLayout):
    '''class that defines the Container widget'''
    def __init__(self, height=100, width=100, padding=(0, 0, 0, 0),
                 margin=(0, 0, 0, 0), decoration=None, background_color=(0, 0, 0, 0), **kwargs):
        super(Container, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (width, height)
        self.padding = padding
        self.margin = margin
        self.decoration = decoration
        self.background_color = background_color

        # Create a background rectangle
        with self.canvas.before:
            Color(*background_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Render decoration if available
        if self.decoration:
            self.decoration(self.canvas)
    # pylint: disable = W0221
    def add_widget(self, widget, **kwargs):
        # Adjust child widget's position based on margin
        widget.pos_hint = {'x': self.margin[0], 'y': self.margin[1]}
        return super(Container, self).add_widget(widget, **kwargs)
