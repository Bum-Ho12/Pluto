'''file that handles the decoration'''
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, RoundedRectangle
from pluto.implementation import ContextWidget


class Decoration(ContextWidget,Widget):
    '''class that defines the Decoration class'''
    def __init__(self, color=(1, 1, 1, 1), border_radius=0, bounds=None, **kwargs):
        super(Decoration, self).__init__(**kwargs)
        self.color = color
        self.border_radius = border_radius
        self.bounds = bounds or (0, 0, 100, 100)  # Default bounds, adjust as needed

        self.draw()

    def draw(self):
        '''method that draws decoration definitions'''
        self.canvas.clear()
        with self.canvas:
            Color(*self.color)
            if self.border_radius > 0:
                RoundedRectangle(pos=self.pos, size=self.size, radius=[self.border_radius])
            else:
                Rectangle(pos=self.pos, size=self.size)
