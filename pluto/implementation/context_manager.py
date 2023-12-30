'''
this file contains the code definition for context manager
for the Pluto framework.
'''
import threading
from pluto.theme import Theme

class ContextManager:
    '''context manager'''
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
                cls._instance.margin = (0, 0, 0, 0)
                cls._instance.padding = (0, 0, 0, 0)
        return cls._instance

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Add any cleanup logic here if needed
        pass

    # pylint: disable = E1101
    def execute_widget(self, widget):
        """
        Executes the given widget by initializing, executing,
        and adding it to the list of widgets in the context.

        Parameters:
        - widget: The widget to be executed within the context.
        """
        print("Start: ")
        print(f"Current widgets in context: {self.widgets}")
        widget.on_create(self)
        # widget.execute(self)
        self.widgets.append(widget)
        print(f"Widget executed successfully: {widget}")

    def remove_widget(self, widget):
        """
        Removes the specified widget from the list and calls its on_destroy method.

        Parameters:
        - widget: The widget to be removed from the context.
        """
        with self.lock:
            if widget in self.widgets:
                self.widgets.remove(widget)
                widget.on_destroy()

    def set_state(self, key, value):
        """
        Sets a key-value pair in the shared state.

        Parameters:
        - key: The key for the shared state.
        - value: The value associated with the key.
        """
        with self.lock:
            self.shared_state[key] = value

    def get_state(self, key):
        """
        Gets the value associated with the given key from the shared state.

        Parameters:
        - key: The key for retrieving the value from the shared state.

        Returns:
        - The value associated with the key.
        """
        with self.lock:
            return self.shared_state.get(key)

    def send_message(self, sender, recipient, message):
        """
        Sends a message from sender to recipient within the context manager.

        Parameters:
        - sender: The widget sending the message.
        - recipient: The widget receiving the message.
        - message: The message to be sent.
        """
        with self.lock:
            recipient.handle_message(sender, message)

class ContextWidget:
    '''context widget'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._context = None

    def set_context(self, context):
        """
        Sets the context for the widget.

        Parameters:
        - context: The context in which the widget exists.
        """
        self._context = context

    def get_theme(self):
        """
        Gets the theme from the associated context.

        Returns:
        - The theme of the widget's context.
        """
        return self._context.theme

    def get_margin(self):
        """
        Gets the margin from the associated context.

        Returns:
        - The margin of the widget's context.
        """
        return self._context.margin

    def get_padding(self):
        """
        Gets the padding from the associated context.

        Returns:
        - The padding of the widget's context.
        """
        return self._context.padding

    def on_create(self, context):
        """
        Called when the widget is created.

        Parameters:
        - context: The context in which the widget is created.
        """
        print(f"Executing widget: {self} in context: {context}")
        context.execute_widget(self)


    def on_destroy(self):
        """
        Called when the widget is destroyed.
        """


    def execute(self, context):
        """
        Executes the context, adding the widget to the context manager.

        Parameters:
        - context: The context in which the widget is executed.
        """
        print(f"Start execute on widget: {self}")
        print(f"Current widgets in context: {context.widgets}")
        print(f"Executing widget: {self}")
        context.execute_widget(self)
        print(f"Widget executed successfully: {self}")

    def set_state(self, key, value):
        """
        Sets a key-value pair in the shared state using the context manager.

        Parameters:
        - key: The key for the shared state.
        - value: The value associated with the key.
        """
        self._context.set_state(key, value)

    def get_state(self, key):
        """
        Gets the value associated with the given key from the shared state.

        Parameters:
        - key: The key for retrieving the value from the shared state.

        Returns:
        - The value associated with the key.
        """
        return self._context.get_state(key)

    def send_message(self, recipient, message):
        """
        Sends a message to a recipient widget using the context manager.

        Parameters:
        - recipient: The widget to receive the message.
        - message: The message to be sent.
        """
        sender = self
        self._context.send_message(sender, recipient, message)

    def handle_message(self, sender, message):
        """
        Handles a message received from a sender widget.

        Parameters:
        - sender: The widget sending the message.
        - message: The message received.
        """


def context_manager(widget_class):
    '''context manager decorator'''
    class ContextWidgetWrapper(widget_class):
        '''context manager wrapper'''
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._initialize_context_manager()

        def _initialize_context_manager(self):
            """
            Initializes the context manager for the widget.
            """
            self._context_manager = ContextManager()
            self._context_manager.execute_widget(self)

        def __exit__(self, exc_type, exc_value, traceback):
            """
            Handles the exit of the widget from the context.
            """
            self._context_manager.remove_widget(self)

    return ContextWidgetWrapper
