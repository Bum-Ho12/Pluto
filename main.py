'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from pluto.implementation.ptx_wrapper import ptx
from pluto.material import Container, Text

# Define your application structure using the ptx decorator
@ptx
def main_app():
    '''main function definition'''

    font_path = os.path.abspath('E:/Projects/Pluto/fonts/Montserrat-VariableFont_wght.ttf')

    return BoxLayout(
        orientation='vertical',
        children=[
            Text(text="Hello, this is a Kivy app!"),
            Container(
                height=200,
                width=200,
                margin=(20, 20, 0, 0),
                decoration=None,  # Add your decoration if needed
                background_color=(0.5, 0.5, 0.5, 1),
                children=[
                    Text(text="Hello, this is inside the Container!",
                        font_name= font_path,
                        italic= True,
                    )
                ]
            )
        ]
    )

class RunApp(App):
    '''runs the Main application'''
    def build(self):
        # Instantiate the root widget using the MyApp function
        return main_app()

# if __name__ == '__main__':
#     RunApp().run()
