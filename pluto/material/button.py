'''file defines a button for the UI component framework'''
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from pluto.implementation import ContextWidget


class CustomButton(ContextWidget,ButtonBehavior, Label):
    '''class that defines the Button component'''
    def __init__(self, text='', on_click=None,
                context = None,
                 style=None, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.text = text
        self.on_click = on_click
        self.style = style or {}
        self.set_context(context)
        self.execute_widget()
        theme = context.theme
        print(f"Button Theme {theme['background_color']}")

        # Set button properties
        self.background_color = self.style.get('background', (1, 1, 1, 1))
        self.text_color = self.style.get('text_color', (1, 1, 1, 1))
        self.text_size = self.style.get('text_size', 16)
        self.padding = (self.style.get('padding', 0), 0)

        # Bind click event
        if self.on_click:
            self.bind(on_press=self.on_click)

    def on_press(self):
        # Handle button press event
        print(f'Button "{self.text}" pressed')
