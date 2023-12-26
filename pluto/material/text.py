'''file that contains the text widget'''
import skia

class Text:
    '''Class that defines a custom Text widget'''
    # pylint: disable = W0102
    def __init__(self,text = '', text_color=[1, 1, 1, 1],
                font_size=15, font_name=None, bold=0, italic=0, bounds=None):
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font_name = font_name
        self.bold = bold
        self.italic = italic
        # pylint: disable = I1101
        self.bounds = bounds or skia.Rect(0, 0, 100, 30)  # Default bounds, adjust as needed

    def __call__(self, canvas, x, y):
        # Rendering the text using Skia
        # pylint: disable = I1101
        paint = skia.Paint()
        paint.color = skia.Color(*[int(c * 255) for c in self.text_color])
        paint.textSize = self.font_size

        if self.font_name:
            paint.typeface = skia.Typeface(self.font_name)

        if self.bold:
            paint.isFakeBoldText = True

        if self.italic:
            paint.textSkewX = -0.25

        # Draw the text
        # pylint: disable = E1101
        canvas.drawText(self.text, x, y, paint)
