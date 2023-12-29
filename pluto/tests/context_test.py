'''context test file'''
import time
from pluto.implementation import ContextManager

class Widget:
    '''widget generator'''
    def __init__(self, name):
        self.name = name

    # pylint: disable = W0613
    def execute(self, context):
        '''widget executor'''
        print(f"Widget {self.name} executed in context")

def test_context_manager():
    '''tests context manager method'''
    # Create an instance of the ContextManager
    context_manager = ContextManager()

    # Create some sample widgets
    widget1 = Widget("Widget1")
    widget2 = Widget("Widget2")
    widget3 = Widget("Widget3")

    # Verify that the context is initially empty
    # pylint: disable = E1101
    assert not context_manager.widgets

    # Add widgets to the context
    with context_manager as context:
        context.add_widget(widget1.name)
        context.add_widget(widget2.name)
        context.add_widget(widget3.name)

    # Verify that widgets have been added to the context
    assert context_manager.widgets == [widget1.name, widget2.name, widget3.name]

    # Execute widgets within the context
    with context_manager as context:
        for widget_name in context_manager.widgets:
            widget = Widget(widget_name)
            context.execute_widget(widget)

    # Wait for a moment to see the print statements
    time.sleep(1)

    # Remove a widget from the context
    with context_manager as context:
        context.remove_widget(widget2.name)

    # Verify that the removed widget is no longer in the context
    assert widget2.name not in context_manager.widgets
