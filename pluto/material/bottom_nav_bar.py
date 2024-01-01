'''this file contains code that defines the behavior bottomNavBar'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from pluto.implementation import ContextWidget


class BottomNavBar(ContextWidget,BoxLayout):
    '''class that defines the Navigation bar class'''
    def __init__(self, labels, screen_manager, **kwargs):
        super(BottomNavBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.screen_manager = screen_manager

        # Create buttons for each screen
        for label in labels:
            button = NavButton(
                label=label,
                on_click=self.switch_screen,
            )
            self.add_widget(button)

    def switch_screen(self, instance):
        '''switches screen'''
        screen_name = instance.label.lower()
        self.screen_manager.current = screen_name

class NavButton(Button):
    '''defines a navbar button'''
    def __init__(self, label, on_click=None, **kwargs):
        super(NavButton, self).__init__(**kwargs)
        self.text = label
        self.on_click = on_click

    def on_release(self):
        if self.on_click:
            self.on_click(self)
