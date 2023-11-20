'''this file contains tests for ContextManager widget'''
from pluto.implementation.context import WidgetBase, ContextManager

class Widget1(WidgetBase):
    '''practice test'''
    # pylint: disable=redefined-outer-name
    def execute(self, context):
        print(f"Inside Widget 1 ({self.name})")

class Widget2(WidgetBase):
    '''practice test'''
    # pylint: disable=redefined-outer-name
    def execute(self, context):
        print(f"Inside Widget 2 ({self.name})")

# Simulate widget interactions
with ContextManager() as context:
    widget1_instance = Widget1("Instance 1")
    widget2_instance = Widget2("Instance 2")

# Access the widgets outside the context
# pylint: disable=no-member
print("Outside Flutter context")
print("All widgets:", ContextManager().widgets)
