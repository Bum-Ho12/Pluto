'''file that defines images'''
from kivy.clock import Clock
from kivy.uix.image import AsyncImage, Image
from pluto_architecture.implementation.context_manager import ContextManager, ContextWidget

class NetworkImage(ContextWidget, AsyncImage):
    '''class defines the NetworkImage class
    required arguments:
    - image_url
    - bounds
    '''
    def __init__(self, image_url, bounds=None, **kwargs):
        super(NetworkImage, self).__init__(**kwargs)
        self.source = image_url
        self.pos = bounds.pos if bounds else (0, 0)
        self.size = bounds.size if bounds else (100, 100)
        self.execute_widget()

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

class AssetImage(ContextWidget, Image):
    '''class that defines the AssetImage class
    required arguments:
    - image_filename
    - bounds
    '''
    def __init__(self, image_filename, bounds=None, **kwargs):
        super(AssetImage, self).__init__(**kwargs)
        self.source = image_filename
        self.pos = bounds.pos if bounds else (0, 0)
        self.size = bounds.size if bounds else (100, 100)
        self.execute_widget()

    def on_create(self, context):
        '''adds the AssetImage widget to context'''
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
                print(f"AssetImage {self} added to context")

    def on_destroy(self):
        '''removes AssetImage widget from context'''
        # You can add any cleanup logic here if needed
        with self._context.lock:
            self._context.widgets.remove(self)

    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        # Handle messages if needed
