'''file that handles inkwell'''
import skia
#pylint: disable = E0611
from skia import Rect

class InkWell:
    '''class that defines InkWell button'''
    def __init__(self, child=None, bounds=None, opacity=1.0,background_color = 0xFFFFFFF):
        self.child = child
        self.bounds = bounds or Rect(0, 0, 100, 50)  # Default bounds, adjust as needed
        self.opacity = opacity
        self.background_color = background_color

    def on_press(self):
        '''function that handles the press functionality'''
        self.opacity = 0.5

    def on_release(self):
        '''function that handles the release functionality'''
        self.opacity = 1.0
        self.on_click()

    def on_click(self):
        '''defines the click action'''
        # Your custom click action goes here

    def __call__(self, canvas, x, y):
        '''renders'''
        # Drawing background
        background_color = self.background_color  # Replace with your desired color
        #pylint: disable = I1101
        paint = skia.Paint()
        paint.color = background_color
        canvas.drawRect(self.bounds, paint)

        # Render child if present
        if self.child:
            self.child.render(canvas, x, y)
