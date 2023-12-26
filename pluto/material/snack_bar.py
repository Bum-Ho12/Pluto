'''file that handles snack bar'''
# import skia
# pylint: disable = E0611
from skia import Rect

class Snackbar:
    '''class that defines snackbar'''
    def __init__(self, text, duration=3, bounds=None):
        self.text = text
        self.duration = duration
        self.bounds = bounds or Rect(0, 0, 300, 50)  # Default bounds, adjust as needed
        self.opacity = 1.0

    def update_pos(self, x, y):
        '''method that updates state of snackbar'''
        self.bounds.offsetTo(x, y)

    def dismiss(self):
        '''method that collapses the snack bar'''
