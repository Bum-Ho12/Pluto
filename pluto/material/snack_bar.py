'''file that handles snack bar'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from ..implementation import context


@context
class Snackbar(BoxLayout):
    '''class that defines snackbar'''
    def __init__(self, text, duration=3, **kwargs):
        super(Snackbar, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 50
        self.padding = (10, 10)
        self.spacing = 10

        self.label = Label(text=text, color=(1, 1, 1, 1))
        self.add_widget(self.label)

        # pylint: disable = E1101:no-member
        self.bind(size=self.update_pos)

        # Schedule the Snackbar to fade out after the specified duration
        Clock.schedule_once(self.dismiss, duration)

    # pylint: disable = W0613:unused-argument
    def update_pos(self, instance, value):
        '''method that updates state of snackbar'''
        self.pos = (self.parent.width / 2 - self.width / 2, 0)

    def dismiss(self, dt):
        '''method that collapses the snack bar'''
        self.parent.remove_widget(self)
