'''scaffold widget for the application'''
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
# pylint: disable = E0611
from kivy.properties import ObjectProperty
from pluto_architecture.implementation.context_manager import ContextManager, ContextWidget

class Scaffold(ContextWidget, BoxLayout):
    '''scaffold class'''
    app_bar = ObjectProperty(None, force_dispatch=True)
    body = ObjectProperty(None, force_dispatch=True)

    def __init__(
        self, app_bar=None, body=None,
        orientation='vertical', padding=(10, 10), margin=(10, 10),
        **kwargs
    ):
        super(Scaffold, self).__init__(**kwargs)
        self.orientation = orientation
        self.padding = padding
        self.margin = margin
        self.execute_widget()

        self.app_bar = app_bar
        self.body = body

        # Create and add app_bar if provided
        if app_bar:
            anchor_layout_app_bar = AnchorLayout(anchor_x='center', anchor_y='top')
            anchor_layout_app_bar.add_widget(app_bar)
            self.add_widget(anchor_layout_app_bar)

        # Create and add body widget if provided
        if body:
            anchor_layout_body = AnchorLayout(anchor_x='center', anchor_y='center')
            anchor_layout_body.add_widget(body)
            self.add_widget(anchor_layout_body)

    # pylint:disable = W0613
    def on_background_color(self, instance, value):
        '''on_background_color call'''
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*value)
            Rectangle(pos=self.pos, size=self.size)

    def on_size(self, instance, value):
        '''on_size call'''
        if self.body:
            self.body.size = (value[0], value[1] - self.app_bar.height)

    def on_pos(self, instance, value):
        '''sets position'''
        if self.body:
            self.body.pos = value[0], value[1] + self.app_bar.height

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
