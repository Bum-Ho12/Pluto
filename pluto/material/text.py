'''file that contains the text widget'''
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from pluto.implementation.context_manager import ContextManager, ContextWidget


class Text(ContextWidget, Label):
    '''class that defines a custom text'''

    def __init__(self, text='', style='labelMedium',**kwargs):

        super(Text, self).__init__(**kwargs)
        # Access theme from the context
        theme = self._context.theme
        text_theme = theme.get_text_theme(style)
        # Initialize properties directly
        self.text = text
        self.text_color = text_theme.get('text_color', [1, 1, 1, 1])
        self.font_size = text_theme.get('font_size', 15)
        self.font_name = text_theme.get('font_name', 'Arial')
        self.bold = text_theme.get('bold', False)
        self.italic = text_theme.get('italic', False)
        self.background_color = text_theme.get('background_color', [1, 1, 1, 1])

        # Apply properties
        self.color = self.text_color
        self.font_size = self.font_size
        self.bold = 'bold' if self.bold else ''
        self.italic = int(self.italic)
        self.size = self.texture_size
        self.font_name = self.font_name
        # Draw the text
        self.draw_text()
        print(f"Theme:{text_theme.get('primary_color')}")

    def draw_text(self):
        '''draws the text on the canvas'''
        with self.canvas.before:
            Color(*self.background_color)
            Rectangle(pos=self.pos, size=self.size)

        with self.canvas:
            Color(*self.text_color)

            # Draw the text
            Rectangle(pos=self.pos, size=self.size)

    # pylint:disable = W0613
    def on_size(self, instance, value):
        '''Update the size of the text when size changes'''
        self.canvas.before.clear()
        with self.canvas.before:
            # Color(*self.background_color)
            Rectangle(pos=self.pos, size=value)

    def on_create(self, context):
        '''adds the Text widget to context'''
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

                if not getattr(self, '_created', False):
                    # Schedule on_create to be called in the main thread
                    Clock.schedule_once(lambda dt: self.on_create(widget_context))

                    context.widgets.append(self)
                    print(f"NetworkImage {self} added to context")
                    # Mark that on_create has been scheduled
                    self._created = True

    def on_destroy(self):
        '''removes Text widget from context'''
        with self._context.lock:
            self._context.widgets.remove(self)

    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        if message == 'update_text':
            self.text = sender.get_state('text')

            self.draw_text()

    # pylint: disable = E0203,W0201
    def on_text(self, instance, value):
        '''Ensure reactivity monitoring to prevent unwanted recursions'''
        if not self._reacting_to_text_update and self._context.is_reactivity_monitoring_enabled():
            self._reacting_to_text_update = True
            self.text = value
            self.draw_text()
            self._reacting_to_text_update = False
