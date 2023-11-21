'''scaffold widget for the application'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

class Scaffold(BoxLayout):
    '''
    this widget handles the encapsulation of the entire application
    widgets in the application.
    '''
    def __init__(self,child, **kwargs):
        self.orientation = 'vertical'
        super(Scaffold, self).__init__(**kwargs)
        self.child = child
        if child:
            self.add_widget(child)

        # Create a screen manager
        self.screen_manager = ScreenManager()

        # Add the screen manager to the Scaffold
        self.add_widget(self.screen_manager)
