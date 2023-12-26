'''file that defines the Container class widget'''
import skia

class Container:
    '''class that contains the container properties'''
    # pylint: disable = W0102
    def __init__(self, height=100, width=100, padding=[0, 0, 0, 0],
                margin=[0, 0, 0, 0], decoration=None, background_color=(0, 0, 0, 0)):
        # Custom properties
        self.height = height
        self.width = width
        self.padding = padding
        self.margin = margin
        self.decoration = decoration
        self.background_color = background_color
        self.children = []

    def add_widget(self, widget):
        '''adds widget to the container'''
        self.children.append(widget)

    def __call__(self, canvas, x, y):
        # Render the container background
        # pylint: disable = I1101
        paint = skia.Paint()
        paint.color = skia.Color(*[int(c * 255) for c in self.background_color])
        bounds = skia.Rect(x, y, x + self.width, y + self.height)
        canvas.drawRect(bounds, paint)

        # Render decoration if available
        if self.decoration:
            self.decoration(canvas)

        # Render child widgets
        for child in self.children:
            # use margin to adjust child position
            child.render(canvas, x + self.margin[3], y + self.margin[2])
