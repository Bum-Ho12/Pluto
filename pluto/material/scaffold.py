'''scaffold widget for the application'''

import skia
#pylint: disable = E0611
from skia import Rect, Surface

class Scaffold:
    '''
    this widget handles the encapsulation of the entire application
    widgets in the application.
    '''
    def __init__(self, child, bounds=None):
        self.child = child
        self.bounds = bounds or Rect(0, 0, 100, 100)  # Default bounds, adjust as needed
        self.surface = Surface(self.bounds.width(), self.bounds.height())
    def add_widget(self, widget):
        '''adds widget'''
        # Add the widget to the surface or handle it based on your Skia implementation

    def __call__(self, canvas, x, y):
        # Rendering the Scaffold using Skia
        # Draw the background or handle it based on your Skia implementation
        # pylint: disable = I1101
        paint = skia.Paint()
        paint.color = skia.Color(0, 0, 0, 255)  # Replace with your desired background color
        canvas.drawRect(self.bounds, paint)

        # Render the child widget
        if self.child:
            self.child(canvas, x, y)
