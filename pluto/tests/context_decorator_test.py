from pluto.material import Text, Scaffold, Container
from pluto.material.app_bar import AppBar
from pluto.implementation import context_manager
import unittest

# Apply the @context decorator to all widgets
@context_manager
class TextWithContext(Text):
    pass

@context_manager
class ContainerWithContext(Container):
    pass

@context_manager
class AppBarWithContext(AppBar):
    pass

@context_manager
class ScaffoldWithContext(Scaffold):
    pass

class TestContext(unittest.TestCase):
    def test_context_manager(self):
        # Create instances of the widgets
        text_widget = TextWithContext()
        container_widget = ContainerWithContext()
        app_bar_widget = AppBarWithContext()
        scaffold_widget = ScaffoldWithContext()

        # Access the context manager instance
        context_manager = text_widget.context_manager

        # Check if the widgets are added to the context manager
        self.assertIn("Widget (TextWithContext)", context_manager.widgets)
        self.assertIn("Widget (ContainerWithContext)", context_manager.widgets)
        self.assertIn("Widget (AppBarWithContext)", context_manager.widgets)
        self.assertIn("Widget (ScaffoldWithContext)", context_manager.widgets)

        # Remove the widgets from the context manager
        text_widget.__exit__(None, None, None)
        container_widget.__exit__(None, None, None)
        app_bar_widget.__exit__(None, None, None)
        scaffold_widget.__exit__(None, None, None)

        # Check if the widgets are removed from the context manager
        self.assertNotIn("Widget (TextWithContext)", context_manager.widgets)
        self.assertNotIn("Widget (ContainerWithContext)", context_manager.widgets)
        self.assertNotIn("Widget (AppBarWithContext)", context_manager.widgets)
        self.assertNotIn("Widget (ScaffoldWithContext)", context_manager.widgets)

def context_decorator_test():
    # Create an instance of TestContext
    test_instance = TestContext()

    # Call the test method
    test_instance.test_context_manager()