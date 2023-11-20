'''file that contains the text widget'''
from kivy.uix.label import Label
import kivy.properties as kvProps

class Text(Label):
    '''Class that defines a custom Text widget'''
    # pylint: disable = I1101:c-extension-no-member
    text_color = kvProps.ListProperty([1, 1, 1, 1])  # Default text color (white)
    font_size = kvProps.NumericProperty(15)  # Default font size
    # Default font name (None means use the default font)
    font_name = kvProps.StringProperty(None, allow_none=True)
    bold = kvProps.NumericProperty(0)  # 0 for not bold, 1 for bold
    italic = kvProps.NumericProperty(0)  # 0 for not italic, 1 for italic

    def __init__(self, **kwargs):
        super(Text, self).__init__(**kwargs)

        # Apply custom text properties
        self.color = self.text_color
        self.font_size = self.font_size
        self.font_name = self.font_name
        self.bold = self.bold
        self.italic = self.italic
