'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
from kivy.app import App
from kivy.config import Config
from pluto_architecture.implementation.ptx_wrapper import ptx
from  .pluto_app import MainLogic

Config.set('graphics', 'multisamples', '0')

@ptx
def main_app():
    '''main function definition for StatefulWidget'''
    return MainLogic.main_widget()

class RunApp(App):
    '''runs the Main application'''
    def build(self):
        return main_app()
