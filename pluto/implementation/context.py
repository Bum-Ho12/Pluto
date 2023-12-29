'''
this file contains the code definition for context manager
for the Pluto framework.
'''
import threading

class ContextManager:
    '''context manager class'''
    _instance_lock = threading.Lock()
    _instance = None

    def __new__(cls):
        with cls._instance_lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.lock = threading.Lock()
                cls._instance.widgets = []
        return cls._instance

    def __enter__(self):
        return self

    def execute_widget(self, widget):
        '''executes the widgets'''
        widget.execute(self)

    # pylint:disable = E1101
    def add_widget(self, widget_name):
        '''adds widget to context'''
        with self.lock:
            self.widgets.append(widget_name)

    def remove_widget(self, widget_name):
        '''removes widget from the context'''
        with self.lock:
            if widget_name in self.widgets:
                self.widgets.remove(widget_name)
                print(f"Removed widget: {widget_name}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def context(cls):
    '''context handler method'''
    class ContextWidget(cls):
        '''context widget'''
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.context_manager = ContextManager()
            self.context_manager.execute_widget(self)

        # pylint: disable = W0621
        def execute(self, context):
            '''executes the context'''
            context.add_widget(f"Widget ({self.__class__.__name__})")

        def __exit__(self, exc_type, exc_value, traceback):
            self.context_manager.remove_widget(f"Widget ({self.__class__.__name__})")

    return ContextWidget
