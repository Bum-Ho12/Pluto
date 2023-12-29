'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
from kivy.app import App
from kivy.config import Config
from pluto.material import Text, Scaffold,Container
from pluto.material.app_bar import AppBar
from pluto.implementation.ptx_wrapper import ptx

Config.set('graphics', 'multisamples', '0')

# Define your application structure using the ptx decorator
@ptx
def main_app():
    '''main function definition'''

    font_name = 'E:/Projects/Pluto/pluto/fonts/Montserrat-VariableFont_wght.ttf'

    # Create the Text widget
    title_text = Text(
        text='My First Demo',
        font_name=font_name,
        italic=False,
        text_color=[1, 1, 1, 1],
        font_size=20,
        background_color=[0,0,0,0],
    )

    # Create the AppBar widget with the Text widget
    app_bar_widget = AppBar(
        title=title_text,
    )

    # Create the Scaffold widget
    scaffold_widget = Scaffold(
        app_bar=app_bar_widget,
        body=Container(
            child=Text(
                text='My First Body',
                font_name=font_name,
                italic=False,
                text_color=[1, 1, 1, 1],
                font_size=20,
                background_color=[1,1,0.5,0.5],
            ),
            background_color=[1,0.5,0.5,1],
            width=100,
            height=50,
            padding=(5,5,5,5),
            margin=(2,2,2,2)
        )
    )

    return scaffold_widget

class RunApp(App):
    '''runs the Main application'''
    def build(self):
        # Instantiate the root widget using the MyApp function
        return main_app()
