'''file that contains the text widget'''
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from pluto.implementation import context_manager

@context_manager
class Text(Label):
    '''class that defines a custom text'''
    # pylint: disable = W0102
    def __init__(self, text='',
                style = 'labelMedium',
                # text_color=[1, 1, 1, 1],
                # background_color = [1,1,1,1],
                # font_size=15, font_name='Arial',
                # bold=False, italic=False,
                 **kwargs):
        super(Text, self).__init__(**kwargs)
        # pylint: disable = E1101
        context = self.context_manager

        theme = context.theme
        text_theme = theme.get_text_theme(style)

        self.text = text
        self.text_color = text_theme.get('text_color',[1,1,1,1])
        self.font_size = text_theme.get('font_size',15)
        self.font_name = text_theme.get('font_name','Arial')
        self.bold = text_theme.get('bold',False)
        self.italic = text_theme.get('italic',False)
        self.background_color = text_theme.get('background_color',[1,1,1,1])

        self.update_properties()
        self.draw_text()

    def update_properties(self):
        '''updates properties of the text'''
        self.color = self.text_color
        self.font_size = self.font_size
        self.bold = 'bold' if self.bold else ''
        self.italic = int(self.italic)
        self.size = self.texture_size  # Set size based on the text content
        self.font_name = self.font_name

    def draw_text(self):
        '''draws the text on the canvas'''
        with self.canvas.before:
            Color(*self.background_color)
            Rectangle(pos=self.pos, size=self.size)

        with self.canvas:
            Color(*self.text_color)

            # Draw the text
            Rectangle(pos=self.pos, size=self.size)

    # pylint: disable=W0613
    def on_size(self, instance, value):
        '''Update the size of the text when size changes'''
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.background_color)
            Rectangle(pos=self.pos, size=value)

    def on_create(self, context):
        '''adds the Text widget to context'''
        context.set_state('text', self.text)

    def on_destroy(self):
        '''removes Text widget from context'''
        # You can add cleanup logic here if needed

    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        if message == 'update_text':
            self.text = sender.get_state('text')
            self.update_properties()
            self.draw_text()
