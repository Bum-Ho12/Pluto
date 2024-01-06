'''
this file defines the AppBar widget that can be used to
define the top bar in pluto framework
'''
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from pluto_architecture.implementation.context_manager import ContextManager, ContextWidget

class AppBar(ContextWidget, BoxLayout):
    '''
    This class defines a custom AppBar widget.
    It can contain a title, and you can customize its appearance.
    '''

    def __init__(
        self, title=None, background_color=(0, 0, 0, 1),
        height=56, orientation='horizontal', **kwargs
    ):
        super(AppBar, self).__init__(**kwargs)
        self.orientation = orientation
        self.size_hint_y = None
        self.height = height

        # Create and add a title Text widget
        if title:
            self.add_widget(title)

        # Customize the background color
        with self.canvas.before:
            Color(*background_color)
            Rectangle(pos=self.pos, size=self.size)

    def set_title(self, title):
        '''Set the title widget of the AppBar'''
        if self.children:
            # If there are existing children (e.g., a previous title), remove them
            self.clear_widgets()

        self.add_widget(title)

    def on_create(self, context):
        '''adds the AppBar widget to context'''
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
                print(f"AppBar {self} added to context with title: {self.children}")

    def on_destroy(self):
        '''removes AppBar widget from context'''
        with self._context.lock:
            self._context.widgets.remove(self)

    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        # Handle messages if needed
