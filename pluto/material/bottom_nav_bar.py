'''this file contains code that defines the behavior bottomNavBar'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BottomNavBar(BoxLayout):
    '''
    this class provides the bottomNavBar
    '''
    def __init__(self, label,**kwargs):
        super(BottomNavBar, self).__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = 50
        self.orientation = 'horizontal'

        # Create buttons for each screen
        home_button = Button(text=label)
        #pylint: disable = E1101:no-member
        home_button.bind(on_release=self.switch_screen)
        self.add_widget(home_button)

        other_button = Button(text=label)
        other_button.bind(on_release=self.switch_screen)
        self.add_widget(other_button)

    def switch_screen(self, instance, app):
        '''
        this method helps switch screens
        '''
        screen_name = instance.text.lower()
        app.get_running_app().root.screen_manager.current = screen_name
