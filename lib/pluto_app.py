'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
from pluto_architecture.implementation.ptx_wrapper import ptx
from pluto_architecture.material import Container,Text


class MainLogic:
    '''Main logic class for application'''
    @staticmethod
    @ptx
    def main_widget():
        '''main function definition for StatefulWidget'''
        return Container(
            child= Text(
                text='Test Demo',
                style='labelLarge',
            ),
            background_color=[0, 0, 0, 0],
            width=100,
            height=50,
            padding=(5, 5, 5, 5),
            margin=(2, 2, 2, 2)
        )

    @staticmethod
    def run_app():
        '''runs the application'''
        main_app_widget = MainLogic.main_widget()
        return main_app_widget
