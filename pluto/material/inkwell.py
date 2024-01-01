'''file that handles inkwell'''
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from pluto.implementation import ContextWidget


class InkWell(ContextWidget,ButtonBehavior, Label):
    '''class that defines the InkWell component'''
    def __init__(self, child=None,
                bounds=None,
                context=None,
                **kwargs):
        super(InkWell, self).__init__(**kwargs)
        theme = context.theme
        self.child = child
        self.bounds = bounds or (0, 0, 100, 50)  # Default bounds, adjust as needed
        self.background_color = theme.button_normal_color
        self.opacity = 1.0
        self.set_context(context)
        self.execute_widget()

        # rectangle definition
        with self.canvas.before:
            Color(*self.background_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)

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
        print("Button clicked")

    def render(self, canvas, x, y):
        '''renders the child component'''
        # Drawing background
        background_color = self.background_color
        with self.canvas.before:
            Color(*background_color)

        # Render child if present
        if self.child:
            self.child.render(canvas, x, y)
