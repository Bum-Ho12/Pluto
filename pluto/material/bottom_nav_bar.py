'''this file contains code that defines the behavior bottomNavBar'''
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from pluto.implementation import ContextWidget
from pluto.implementation.context_manager import ContextManager


class BottomNavBar(ContextWidget,BoxLayout):
    '''class that defines the Navigation bar class'''
    def __init__(self, labels, screen_manager,**kwargs):
        super(BottomNavBar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.screen_manager = screen_manager

        # Create buttons for each screen
        for label in labels:
            button = NavButton(
                label=label,
                on_click=self.switch_screen,
                # context = self._context
            )
            self.add_widget(button)

    def switch_screen(self, instance):
        '''switches screen'''
        screen_name = instance.label.lower()
        self.screen_manager.current = screen_name

    def on_create(self, context):
        '''adds the BottomNavBar widget to context'''
        with context.lock:
            # Create a new context for the widget
            widget_context = ContextManager()
            widget_context.parent_context = context  # Store a reference to the parent context
            self.set_context(widget_context)

            # Set the parent for the widget
            if context.widgets:
                parent = context.widgets[-1]  # Assuming the last added widget is the parent
                self.set_parent(parent)
                parent.add_child(self)

                # Schedule on_create to be called in the main thread
                Clock.schedule_once(lambda dt: self.on_create(widget_context))

                context.widgets.append(self)
                print(f"BottomNavBar {self} added to context with buttons: {self.children}")

    def on_destroy(self):
        '''removes BottomNavBar widget from context'''
        # You can add any cleanup logic here if needed
        with self._context.lock:
            self._context.widgets.remove(self)

class NavButton(Button):
    '''defines a navbar button'''
    def __init__(self, label, on_click=None, **kwargs):
        super(NavButton, self).__init__(**kwargs)
        self.text = label
        self.on_click = on_click
        # self.set_context(context)

    def on_release(self):
        if self.on_click:
            self.on_click(self)
