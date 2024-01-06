'''file that handles the decoration'''
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, RoundedRectangle
from pluto_architecture.implementation import ContextWidget
from pluto_architecture.implementation.context_manager import ContextManager


class Decoration(ContextWidget,Widget):
    '''class that defines the Decoration class'''
    def __init__(self, color=(1, 1, 1, 1), border_radius=0,
                bounds=None, **kwargs):
        super(Decoration, self).__init__(**kwargs)
        self.color = color
        self.border_radius = border_radius
        self.bounds = bounds or (0, 0, 100, 100)

        self.draw()

    def draw(self):
        '''method that draws decoration definitions'''
        self.canvas.clear()
        with self.canvas:
            Color(*self.color)
            if self.border_radius > 0:
                RoundedRectangle(pos=self.pos, size=self.size, radius=[self.border_radius])
            else:
                Rectangle(pos=self.pos, size=self.size)

    def on_create(self, context):
        '''adds the Decoration widget to context'''
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
                print(f"Decoration {self} added to context")

    def on_destroy(self):
        '''removes Decoration widget from context'''
        # You can add any cleanup logic here if needed
        with self._context.lock:
            self._context.widgets.remove(self)

    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        # Handle messages if needed
