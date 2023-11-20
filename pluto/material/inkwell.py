'''file that handles inkwell'''
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label

class InkWell(ButtonBehavior, Label):
    '''class that define InkWell button'''
    def __init__(self, child = None,**kwargs):
        super(InkWell, self).__init__(**kwargs)
        self.child = child
        if child:
            self.add_widget(child)
        # pylint: disable= E1101:no-member
        self.bind(on_press=self.on_press)
        self.bind(on_release=self.on_release)

    # pylint: disable = W0613:unused-argument
    # pylint: disable = W0221:arguments-differ
    def on_press(self, instance):
        self.opacity = 0.5

    def on_release(self, instance):
        self.opacity = 1.0
        # pylint: disable = E1101:no-member
        self.dispatch('on_click')

    def on_click(self):
        '''defines the click action'''
