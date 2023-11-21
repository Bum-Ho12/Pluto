'''file that handles the decoration'''
from kivy.uix.widget import Widget
import kivy.properties as kvProps
from ..implementation import context

@context
class Decoration(Widget):
    '''class that defines the decoration properties'''
    # pylint: disable = I1101:c-extension-no-member
    color = kvProps.ColorProperty([1,1,1,1]) #default color(white)
    border_radius = kvProps.NumericProperty(0) # default border radius
