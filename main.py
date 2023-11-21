'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
# from pluto.material import Container, Text
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class RunApp(App):
    '''
    this is the primary method that encapsulates
    all the widgets of the application.
    '''
    def build(self):
        return Scaffold()


class Scaffold(BoxLayout):
    '''scaffold example'''
    def __init__(self, **kwargs):
        super(Scaffold, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Create a screen manager
        self.screen_manager = ScreenManager()

        # Add screens to the screen manager
        self.screen_manager.add_widget(HomeScreen(name='home'))
        self.screen_manager.add_widget(OtherScreen(name='other'))

        # Add the screen manager to the Scaffold
        self.add_widget(self.screen_manager)

        # Create a bottom navigation bar
        self.bottom_nav = BottomNavBar()
        self.add_widget(self.bottom_nav)

class BottomNavBar(BoxLayout):
    '''BottomNavBar example'''
    def __init__(self, **kwargs):
        super(BottomNavBar, self).__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = 50
        self.orientation = 'horizontal'

        # Create buttons for each screen
        home_button = Button(text='Home')
        home_button.bind(on_release=self.switch_screen)
        self.add_widget(home_button)

        other_button = Button(text='Other')
        other_button.bind(on_release=self.switch_screen)
        self.add_widget(other_button)

    def switch_screen(self, instance):
        '''example'''
        screen_name = instance.text.lower()
        App.get_running_app().root.screen_manager.current = screen_name

class HomeScreen(Screen):
    '''Home Screen example'''
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Welcome, Pluto'))

class OtherScreen(Screen):
    '''Other screen example'''
    def __init__(self, **kwargs):
        super(OtherScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Welcome, to Other screen'))

class OtherScreen2(Screen):
    '''Other screen example'''
    def __init__(self, **kwargs):
        super(OtherScreen2, self).__init__(**kwargs)
        self.add_widget(Label(text='Welcome, to Other screen 2'))
