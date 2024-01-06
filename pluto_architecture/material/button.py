'''file defines a button for the UI component framework'''
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from pluto_architecture.implementation import ContextWidget
from pluto_architecture.implementation.context_manager import ContextManager


class CustomButton(ContextWidget,ButtonBehavior, Label):
    '''class that defines the Button component'''
    def __init__(self, text='', on_click=None,
                 style=None, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.text = text
        self.on_click = on_click
        self.style = style or {}
        theme = self._context.theme
        print(f"Button Theme {theme['background_color']}")

        # Set button properties
        self.background_color = self.style.get('background', (1, 1, 1, 1))
        self.text_color = self.style.get('text_color', (1, 1, 1, 1))
        self.text_size = self.style.get('text_size', 16)
        self.padding = (self.style.get('padding', 0), 0)

        # Bind click event
        # pylint:disable = E1101
        if self.on_click:
            self.bind(on_press=self.on_click)

    def on_press(self):
        # Handle button press event
        print(f'Button "{self.text}" pressed')

    def on_create(self, context):
        '''adds the CustomButton widget to context'''
        with context.lock:
            # Create a new context for the widget
            widget_context = ContextManager()
            widget_context.parent_context = context  # Store a reference to the parent context
            self.set_context(widget_context)

            # Set the parent for the widget
            if context.widgets:
                parent = context.widgets[-1]  # Assuming the last added widget is the parent
                self.set_parent(parent)
                parent.add_child(self)

                # Schedule on_create to be called in the main thread
                Clock.schedule_once(lambda dt: self.on_create(widget_context))

                context.widgets.append(self)
                print(f"CustomButton {self} added to context")

    def on_destroy(self):
        '''removes CustomButton widget from context'''
        # You can add any cleanup logic here if needed
        with self._context.lock:
            self._context.widgets.remove(self)

    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        # Handle messages if needed
