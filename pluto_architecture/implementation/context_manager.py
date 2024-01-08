'''
this file contains the code definition for context manager
for the Pluto framework.
'''
import threading
from kivy.clock import Clock
from pluto_architecture.theme import Theme

class ContextManager:
    '''
    context manager class
    methods:
        - __enter__
        - __exit__
        - execute_widget
        - remove_widget
        - set_widget
        - get_state
        - send_message
        - schedule_clock_event
        - unschedule_clock_events
        - start_reactivity_monitoring
        - stop_reactivity_monitoring
        - is_reactivity_monitoring_enabled
    '''
    def __init__(self):
        self.lock = threading.Lock()
        self.widgets = []  # List to keep track of added widgets
        self.shared_state = {}  # Shared state among widgets
        self.clock_scheduled_events = [] # tracks properties updates in kivy
        self.theme = Theme()
        self.margin = (0, 0, 0, 0)
        self.padding = (0, 0, 0, 0)
        self.initialized = False # boolean to track if context is initialized
        self.parent_context = None # parent context
        self.reactivity_monitoring = False # tracks reactivity for reactive programming purpose

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Add any cleanup logic here if needed
        pass

    def execute_widget(self, widget):
        """
        Executes the given widget by initializing, executing,
        and adding it to the list of widgets in the context.

        Parameters:
        - widget: The widget to be executed within the context.
        """
        with self.lock:
                # Set the parent for the widget
            if self.widgets:
                parent = self.widgets[-1]  # Assuming the last added widget is the parent
                widget.set_parent(parent)
                parent.add_child(widget)

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
            # Remove the parent-child relationship
            widget.set_parent(None)

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
            # Propagate the message to children
            for child in recipient.get_children():
                self.send_message(sender, child, message)

    def schedule_clock_event(self, callback, interval):
        """
        Schedules a clock event with the specified callback and interval.

        Parameters:
        - callback: The function to be called.
        - interval: The time interval between calls.
        """
        with self.lock:
            event = Clock.schedule_interval(callback, interval)
            self.clock_scheduled_events.append(event)

    def unschedule_clock_events(self):
        """Unschedule all clock events."""
        with self.lock:
            for event in self.clock_scheduled_events:
                event.cancel()
            self.clock_scheduled_events.clear()

    # pylint:disable = W0201
    def start_reactivity_monitoring(self):
        """Starts reactivity monitoring."""
        with self.lock:
            self.reactivity_monitoring = True

    def stop_reactivity_monitoring(self):
        """Stops reactivity monitoring."""
        with self.lock:
            self.reactivity_monitoring = False

    def is_reactivity_monitoring_enabled(self):
        """Checks if reactivity monitoring is enabled."""
        with self.lock:
            return self.reactivity_monitoring

class ContextWidget:
    '''
    context widget class
    methods:
    - set_context
    - set_parent
    - get_parent
    - get_children
    - add_child
    - get_theme
    - get_margin
    - get_padding
    - on_create
    - on_destroy
    - set_state
    - get_state
    - send_message
    - handle_message
    '''
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        context_manager = ContextManager()
        self._context = None
        self._parent = None
        self._children = []
        self._parent_context = None
        context_manager.execute_widget(self)
        self.set_context(context_manager)

    def set_context(self, context)->None:
        """
        Sets the context for the widget.

        Parameters:
        - context: The context in which the widget exists.
        """
        self._context = context
        if hasattr(self._context, 'parent_context') and self._context.parent_context:
            self._parent_context = self._context.parent_context

    def set_parent(self, parent)->None:
        """
        Sets the parent widget for the widget.

        Parameters:
        - parent: The parent widget of the current widget.
        """
        self._parent = parent

    def get_parent(self):
        """
        Gets the parent widget for the widget.
        """
        return self._parent

    def get_children(self):
        """
        Gets the list of children widgets.

        Returns:
        - List of children widgets.
        """
        return self._children

    def add_child(self, child):
        """
        adds children widget for the widget.

        Parameters:
        - child: The child widget of the current widget.
        """
        self._children.append(child)
        child.set_parent(self)

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

    def get_context(self):
        '''provides the context value'''
        return self._context

    def get_padding(self):
        """
        Gets the padding from the associated context.

        Returns:
        - The padding of the widget's context.
        """
        return self._context.padding

    def on_create(self):
        """
        Called when the widget is created.

        Parameters:
        - context: The context in which the widget is created.
        """
        print(f"Executing widget: {self} in context: {self._context}")


    def on_destroy(self):
        """
        Called when the widget is destroyed.
        """

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
