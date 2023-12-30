'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
from kivy.app import App
from kivy.config import Config
from pluto.material import Scaffold, Container,Text
from pluto.material.app_bar import AppBar
from pluto.implementation.context_manager import ContextManager
from pluto.implementation.ptx_wrapper import ptx

Config.set('graphics', 'multisamples', '0')

# Define your application structure using the ptx decorator
@ptx
def main_app():
    '''main function definition'''

    with ContextManager() as context:
        # Create the Text widget using the new ContextWidget definition
        # Create the Text widget using the new ContextWidget definition
        title_text = Text(
            text='My First Demo',
            style='labelMedium',  # Specify the style for the Text widget
        )
        context.execute_widget(title_text)

        # Create the AppBar widget with a separate Text widget for the Container
        app_bar_text = Text(
            text='My AppBar Title',
            style='labelMedium',
        )

        # Create the AppBar widget with the Text widget
        app_bar_widget = AppBar(
            title=app_bar_text,
        )
        context.execute_widget(app_bar_widget)

        # Create the Scaffold widget
        scaffold_widget = Scaffold(
            app_bar=app_bar_widget,
            body=Container(
                child=title_text,
                background_color=[0, 0, 0, 0],
                width=100,
                height=50,
                padding=(5, 5, 5, 5),
                margin=(2, 2, 2, 2)
            )
        )
        context.execute_widget(scaffold_widget)

    return scaffold_widget

class RunApp(App):
    '''runs the Main application'''

    def build(self):
        # Instantiate the root widget using the main_app function
        main_widget = main_app()
        return main_widget
