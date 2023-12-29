'''file that handles snack bar'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.clock import Clock
from pluto.implementation import context_manager

@context_manager
# pylint: disable = E1101
class Snackbar(BoxLayout):
    '''this class defines a snackbar banner'''
    def __init__(self, text, duration=3, bounds=None, width=300, height=50,opacity=1.0, **kwargs):
        super(Snackbar, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, None)
        self.width = width
        self.height = height
        self.opacity = opacity

        self.pos_hint = {'top': 1.0}
        self.bind(pos=self.update_pos)

        # Create label for displaying text
        self.label = Label(text=text, size_hint_y=None, height=self.height)
        self.add_widget(self.label)

        # Set initial position
        self.pos = bounds.pos if bounds else (0, 0)

        # Set duration for the snackbar to be displayed
        self.duration = duration

        # Schedule the dismissal of the snackbar after the specified duration
        Clock.schedule_once(self.dismiss, duration)

    # pylint: disable = W0613
    def update_pos(self, instance, value):
        '''Update the position of the snackbar'''
        self.label.pos = value

    def dismiss(self, *args):
        '''Animate the snackbar's opacity and remove it from the parent layout'''
        animation = Animation(opacity=0, duration=0.5)
        animation.start(self)
        Clock.schedule_once(self.remove_from_parent, animation.duration)

    def remove_from_parent(self, *args):
        '''Remove the snackbar from its parent layout'''
        parent_layout = self.parent
        if parent_layout:
            parent_layout.remove_widget(self)
