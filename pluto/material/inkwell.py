'''file that handles inkwell'''
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from pluto.implementation.context_manager import ContextManager, ContextWidget

class InkWell(ContextWidget, ButtonBehavior, Label):
    '''class that defines the InkWell component'''
    def __init__(self, child=None, bounds=None, **kwargs):
        super(InkWell, self).__init__(**kwargs)
        theme = self._context.theme
        self.child = child
        self.bounds = bounds or (0, 0, 100, 50)  # Default bounds, adjust as needed
        self.background_color = theme.button_normal_color
        self.opacity = 1.0
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

    def on_create(self, context):
        '''adds the NetworkImage widget to context'''
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
                print(f"NetworkImage {self} added to context")

    def on_destroy(self):
        '''removes NetworkImage widget from context'''
        # You can add any cleanup logic here if needed
        with self._context.lock:
            self._context.widgets.remove(self)

    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        # Handle messages if needed
