'''file that contains the text widget'''
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class Text(Label):
    '''class that defines a custom text'''
    # pylint: disable = W0102
    def __init__(self, text='', text_color=[1, 1, 1, 1],
                font_size=15, font_name='Arial',
                bold=False, italic=False, bounds=None, **kwargs):
        super(Text, self).__init__(**kwargs)
        self.text = text
        self.text_color = text_color
        self.font_size = font_size
        self.font_name = font_name
        self.bold = bold
        self.italic = italic
        self.bounds = bounds or (0, 0, 100, 30)

        self.update_properties()
        self.draw_text()

    def update_properties(self):
        '''updates properties of the text'''
        self.color = self.text_color
        self.font_size = self.font_size
        self.bold = 'bold' if self.bold else ''
        self.italic = int(self.italic)
        self.size = (self.bounds[2] - self.bounds[0], self.bounds[3] - self.bounds[1])
        print("Font Name:", self.font_name)
        self.font_name = self.font_name

    def draw_text(self):
        '''draws the text on the canvas'''
        with self.canvas:
            Color(*self.text_color)
            Rectangle(pos=self.pos, size=self.size)

            # Draw the text
            self.text_size = self.size
            self.text = self.text
