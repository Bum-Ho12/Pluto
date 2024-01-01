'''file that defines the Container class widget'''
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from pluto.implementation.context_manager import ContextWidget

class Container(ContextWidget, FloatLayout):
    '''class that defines the Container widget'''

    def __init__(self, height=100, width=100,
                child=None,
                padding=(0, 0, 0, 0),
                margin=(0, 0, 0, 0),
                decoration=None,
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
            Color(*background_color)  # Set a default color, it will be overridden by Rectangle
            self.rect = Rectangle(pos=self.pos, size=self.size)

    # pylint: disable = W0613
    def on_size(self, instance, value):
        '''Update the position of the background rectangle when size changes'''
        if hasattr(self, 'rect'):
            self.rect.pos = (self.x + self.margin[0], self.y + self.margin[1])
            self.rect.size = (self.width - (self.margin[0] + self.margin[2]),
                self.height - (self.margin[1] + self.margin[3]))

    def on_pos(self, instance, value):
        '''Update the position of the background rectangle when position changes'''
        if hasattr(self, 'rect'):
            self.rect.pos = (self.x + self.margin[0], self.y + self.margin[1])

    # pylint: disable = W0221
    def add_widget(self, widget, **kwargs):
        '''Add a widget to the Container'''
        # Adjust child widget's position based on margin
        widget.pos = (self.margin[0], self.margin[1])
        return super(Container, self).add_widget(widget, **kwargs)

    def on_create(self, context):
        '''adds the Container widget to context'''
        print(f"Container {self} added to context with child: {self.children}")


    def on_destroy(self):
        '''removes Container widget from context'''
        # You can add any cleanup logic here if needed


    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        # Handle messages if needed
