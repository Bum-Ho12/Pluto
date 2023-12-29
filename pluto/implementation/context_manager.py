'''
this file contains the code definition for context manager
for the Pluto framework.
'''
import threading
from pluto.theme import Theme
class ContextManager:
    '''
    This class defines the context manager for the Pluto framework.
    It manages the shared state and communication between widgets.
    '''
    _instance_lock = threading.Lock()
    _instance = None

    def __new__(cls):
        with cls._instance_lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.lock = threading.Lock()
                cls._instance.widgets = []  # List to keep track of added widgets
                cls._instance.shared_state = {}  # Shared state among widgets
                cls._instance.theme = Theme()
                cls._instance.margin = (0,0,0,0)
                cls._instance.padding = (0,0,0,0)
        return cls._instance

    def __enter__(self):
        return self

    # pylint: disable=E1101
    def execute_widget(self, widget):
        '''
        Executes the widget by initializing, executing, and adding it to the list.
        '''
        widget.on_create(self)
        widget.execute(self)
        self.widgets.append(widget)

    def remove_widget(self, widget):
        '''
        Removes the widget from the list and calls its on_destroy method.
        '''
        with self.lock:
            if widget in self.widgets:
                self.widgets.remove(widget)
                widget.on_destroy()

    def set_state(self, key, value):
        '''
        Sets a key-value pair in the shared state.
        '''
        with self.lock:
            self.shared_state[key] = value

    def get_state(self, key):
        '''
        Gets the value associated with the given key from the shared state.
        '''
        with self.lock:
            return self.shared_state.get(key)

    def send_message(self, sender, recipient, message):
        '''
        Sends a message from sender to recipient within the context manager.
        '''
        with self.lock:
            recipient.handle_message(sender, message)

class ContextWidget:
    '''
    This class represents a widget in the context.
    It provides methods to interact with the context manager and handle messages.
    '''
    # pylint: disable = E1101
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme = ContextManager().theme
        self.margin = ContextManager().margin
        self.padding = ContextManager().padding

    def on_create(self, context):
        '''
        Called when the widget is created.
        '''


    def on_destroy(self):
        '''
        Called when the widget is destroyed.
        '''


    def execute(self, context):
        '''
        Executes the context, adding the widget to the context manager.
        '''
        context.add_widget(f"Widget ({self.__class__.__name__})")

    def add_child(self, child):
        '''
        Adds a child widget to the context manager.
        '''
        context = ContextManager()
        context.execute_widget(child)

        # Propagate styles to the child
        child.theme = context.theme
        child.margin = context.margin
        child.padding = context.padding

        context.widgets.append(child)

    def set_state(self, key, value):
        '''
        Sets a key-value pair in the shared state using the context manager.
        '''
        ContextManager().set_state(key, value)

    def get_state(self, key):
        '''
        Gets the value associated with the given key from the shared state.
        '''
        return ContextManager().get_state(key)

    def send_message(self, recipient, message):
        '''
        Sends a message to a recipient widget using the context manager.
        '''
        sender = self
        ContextManager().send_message(sender, recipient, message)

    def handle_message(self, sender, message):
        '''
        Handles a message received from a sender widget.
        '''


def context_manager(widget_class):
    '''
    Decorator to integrate the ContextManager with a widget class.
    '''
    class ContextWidgetWrapper(widget_class, ContextWidget):
        '''Wrapper class to integrate the ContextManager'''
        def __init__(self, *args, **kwargs):
            # Check if ContextWidget is in base classes
            if ContextWidget not in self.__class__.__bases__:
                super().__init__(*args, **kwargs)
            else:
                super(ContextWidgetWrapper, self).__init__(*args, **kwargs)
                self.context_manager = ContextManager()
                self.context_manager.execute_widget(self)

        def __exit__(self, exc_type, exc_value, traceback):
            self.context_manager.remove_widget(self)

    return ContextWidgetWrapper
