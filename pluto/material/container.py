'''file that defines the Container class widget'''
from kivy.uix.boxlayout import BoxLayout
import kivy.properties as kivyProp
from ..implementation import context

@context
class Container(BoxLayout):
    '''class that contains the container properties'''
    # Custom properties
    # pylint: disable = I1101:c-extension-no-member
    height = kivyProp.NumericProperty(100)  # Default height
    width = kivyProp.NumericProperty(100)   # Default width
    padding = kivyProp.ListProperty([0, 0, 0, 0])  # Default padding: [top, right, bottom, left]
    margin = kivyProp.ListProperty([0, 0, 0, 0])   # Default margin: [top, right, bottom, left]
    decoration = kivyProp.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.orientation = 'vertical'
        # Apply custom properties
        self.size_hint = None, None
        self.size = (self.width, self.height)
        self.padding = self.padding
        self.margin = self.margin

    def child(self, widget, **kwargs):
        '''adds child widget to the Container'''
        # Adjust child widget's position based on margin
        widget.pos_hint = {'top': 1 - self.margin[0] / self.height,
                            'right': 1 - self.margin[1] / self.width,
                            'bottom': self.margin[2] / self.height,
                            'left': self.margin[3] / self.width
                        }
        # Apply decoration properties
        if self.decoration:
            widget.background_color = self.decoration.color
            widget.border_radius = [self.decoration.border_radius]

        super(Container, self).add_widget(widget,**kwargs)
