'''
file that defines the View UI basic component
'''
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color

class View(FloatLayout):
    '''this class defines the View component'''
    def __init__(self, children=None, style=None, **kwargs):
        super(View, self).__init__(**kwargs)
        self.children = children or []
        self.style = style or {}

        # Set background color
        background_color = self.style.get('background_color', (1, 1, 1, 1))
        with self.canvas.before:
            Color(*background_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
    # pylint: disable = W0221
    def add_widget(self, widget, index=0, canvas=None):
        # Adjust child widget's position based on padding and margin
        margin = self.style.get('margin', 0)
        widget.pos_hint = {'x': margin, 'y': margin}
        return super(View, self).add_widget(widget, index=index, canvas=canvas)
