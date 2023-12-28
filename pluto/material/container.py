'''file that defines the Container class widget'''
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color

class Container(FloatLayout):
    '''class that defines the Container widget'''
    def __init__(self, height=100, width=100,
        child = None,
        padding=(0, 0, 0, 0),
        margin=(0, 0, 0, 0), decoration=None,
        background_color=(0, 0, 0, 0), **kwargs):
        super(Container, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (width, height)
        self.padding = padding
        self.margin = margin
        self.decoration = decoration
        self.background_color = background_color

        # Render decoration if available
        if self.decoration:
            self.decoration(self.canvas)

        # Add the child widget if provided
        if child:
            self.add_widget(child)

        # Create a background rectangle
        with self.canvas.before:
            Color(*background_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

    # pylint: disable = W0613
    def on_size(self, instance, value):
        '''Update the position of the background rectangle when size changes'''
        self.rect.pos = self.pos
        self.rect.size = value

    def on_pos(self, instance, value):
        '''Update the position of the background rectangle when position changes'''
        self.rect.pos = value

    # pylint: disable = W0221
    def add_widget(self, widget, **kwargs):
        '''Add a widget to the Container'''
        # Adjust child widget's position based on margin
        widget.pos_hint = {'x': self.margin[0], 'y': self.margin[1]}
        return super(Container, self).add_widget(widget, **kwargs)
