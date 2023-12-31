'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
from kivy.app import App
from kivy.config import Config
from lib.stateful_example import CounterWidget
# from lib.stateless_example import GreetingWidget
from pluto_architecture.implementation.ptx_wrapper import ptx
from pluto_architecture.material.container import Container
from pluto_architecture.material.text import Text

Config.set('graphics', 'multisamples', '0')

# Define your application structure using the ptx decorator
# @ptx
# def main_app():
#     '''main function definition'''

#     with ContextManager() as context:
#         # Create the Text widget using the new ContextWidget definition
#         # Create the Text widget using the new ContextWidget definition
#         title_text = Text(
#             text='My First Demo',
#             style='labelMedium',  # Specify the style for the Text widget
#             context=context
#         )
#         context.execute_widget(title_text)

#         # Create the AppBar widget with a separate Text widget for the Container
#         app_bar_text = Text(
#             text='My AppBar Title',
#             style='labelMedium',
#             context=context
#         )

#         # Create the AppBar widget with the Text widget
#         app_bar_widget = AppBar(
#             title=app_bar_text,
#         )
#         context.execute_widget(app_bar_widget)

#         # Create the Scaffold widget
#         scaffold_widget = Scaffold(
#             app_bar=app_bar_widget,
#             body=Container(
#                 child=title_text,
#                 background_color=[0, 0, 0, 0],
#                 width=100,
#                 height=50,
#                 padding=(5, 5, 5, 5),
#                 margin=(2, 2, 2, 2)
#             )
#         )
#         context.execute_widget(scaffold_widget)

#     return scaffold_widget

@ptx
def main_app():
    '''main function definition for StatefulWidget'''
    # counter_widget = CounterWidget()
    return Container(
        # child=counter_widget,  # Add the widget to the UI
        child= Text(
            text='Test Reactivity',
        ),
        background_color=[0, 0, 0, 0],
        width=100,
        height=50,
        padding=(5, 5, 5, 5),
        margin=(2, 2, 2, 2)
    )

        # Additional code to display the UI window
    # context.execute_widget(container)

# @ptx
# def main_app():
#     '''main function definition for StatelessWidget'''
#     with ContextManager() as context:
#         context.set_state('name', 'John')
#         greeting_widget = GreetingWidget()
#         context.execute_widget(greeting_widget)


class RunApp(App):
    '''runs the Main application'''

    def build(self):
        # Instantiate the root widget using the main_app function
        main_widget = main_app()
        return main_widget
