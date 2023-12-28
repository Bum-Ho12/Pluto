'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
from kivy.app import App
from kivy.config import Config
from pluto.material import Container, Text, Scaffold
from pluto.material.app_bar import AppBar
from pluto.implementation.ptx_wrapper import ptx

Config.set('graphics', 'multisamples', '0')

# Define your application structure using the ptx decorator
@ptx
def main_app():
    '''main function definition'''

    font_name = 'E:/Projects/Pluto/pluto/fonts/Montserrat-VariableFont_wght.ttf'

    scaffold = Scaffold(
        orientation='vertical',
        app_bar=AppBar(
            title=Text(
                text='My First Demo',
                font_name=font_name,
                italic=False,
                text_color=[1, 1, 1, 1],
                font_size=20,
            )
        ),
        body=Container(
            height=200,
            width=200,
            margin=(20, 20),  # Adjusted margin
            decoration=None,
            background_color=(1, 0.5, 0.5, 1),
            children=[
                Text(
                    text="Hello, this is inside the Container!",
                    font_name=font_name,
                    italic=True,
                    text_color=[1, 1, 1, 1]
                )
            ]
        ),
    )
    print(f"Scaffold size: {scaffold.size}")
    print(f"AppBar size: {scaffold.app_bar.size}")
    print(f"Body size: {scaffold.body.size}")
    return scaffold

class RunApp(App):
    '''runs the Main application'''
    def build(self):
        # Instantiate the root widget using the MyApp function
        return main_app()
