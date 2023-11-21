'''file that manages the framework's context'''
import threading

class ContextManager:
    '''this class defines the context of the framework'''
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
        '''method that execute the widget inside '''
        widget.execute(self)

    def add_widget(self, widget_name):
        '''method that add widgets to the context'''
        # pylint: disable=no-member
        with self.lock:
            self.widgets.append(widget_name)

    def remove_widget(self, widget_name):
        '''Method that removes widgets from the context'''
        # pylint: disable=no-member
        with self.lock:
            if widget_name in self.widgets:
                self.widgets.remove(widget_name)
                print(f"Removed widget: {widget_name}")

    def __exit__(self, exc_type, exc_value, traceback):
        pass
# pylint: disable=redefined-outer-name


def context(cls):
    '''
    it is a decorator that adds widgets to context
    '''
    class ContextWidget(cls):
        '''this class adds widgets to the context'''
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.execute(ContextManager()._instance)

        def execute(self, context):
            '''this method performs the add_widget action from ContextManager class'''
            context.add_widget(f"Widget ({self.__class__.__name__})")

        def __del__(self):
            # Remove the widget from the context when it is deleted
            ContextManager()._instance.remove_widget(self)
    return ContextWidget
