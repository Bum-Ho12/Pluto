'''file that handles the decoration'''

import skia

class Decoration:
    '''class that defines the decoration properties'''
    # pylint: disable = W0102
    def __init__(self, color=[1, 1, 1, 1], border_radius=0, bounds=None):
        self.color = color
        self.border_radius = border_radius
        # pylint: disable = I1101
        self.bounds = bounds or skia.Rect(0, 0, 100, 100)  # Default bounds, adjust as needed

    def __call__(self, canvas):
        # Drawing decoration using Skia
        # pylint: disable = I1101
        paint = skia.Paint()
        paint.color = skia.Color(*[int(c * 255) for c in self.color])
        paint.isAntiAlias = True

        if self.border_radius > 0:
            # Draw a rounded rectangle
            canvas.drawRoundRect(self.bounds, self.border_radius, self.border_radius, paint)
        else:
            # Draw a regular rectangle
            canvas.drawRect(self.bounds, paint)
