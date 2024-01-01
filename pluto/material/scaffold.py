'''scaffold widget for the application'''
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
# pylint:disable = E0611,W0613
from kivy.properties import ObjectProperty
from pluto.implementation.context_manager import ContextWidget

class Scaffold(ContextWidget, BoxLayout):
    '''scaffold class'''
    app_bar = ObjectProperty(None, force_dispatch=True)
    body = ObjectProperty(None, force_dispatch=True)

    def __init__(
        self, app_bar=None, body=None,
        orientation='vertical',context= None,
        padding=(10, 10), margin=(10, 10),
        **kwargs
    ):
        super(Scaffold, self).__init__(**kwargs)
        self.orientation = orientation
        self.padding = padding
        self.margin = margin
        self.set_context(context)
        self.execute_widget()

        self.app_bar = app_bar
        self.body = body

        # Create and add app_bar if provided
        if app_bar:
            anchor_layout_app_bar = AnchorLayout(anchor_x='center', anchor_y='top')
            anchor_layout_app_bar.add_widget(app_bar)
            self.add_widget(anchor_layout_app_bar)

        # Create and add body widget if provided
        if body:
            anchor_layout_body = AnchorLayout(anchor_x='center', anchor_y='center')
            anchor_layout_body.add_widget(body)
            self.add_widget(anchor_layout_body)

    def on_background_color(self, instance, value):
        '''on_background_color call'''
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*value)
            Rectangle(pos=self.pos, size=self.size)

    def on_size(self, instance, value):
        '''on_size call'''
        if self.body:
            self.body.size = (value[0], value[1] - self.app_bar.height)

    def on_pos(self, instance, value):
        '''sets position'''
        if self.body:
            self.body.pos = value[0], value[1] + self.app_bar.height

    def on_create(self, context):
        '''adds the Scaffold widget to context'''
        # You can add any additional setup logic here if needed


    def on_destroy(self):
        '''removes Scaffold widget from context'''
        # You can add any cleanup logic here if needed


    def handle_message(self, sender, message):
        '''passes messages in the context widgets'''
        # Handle messages if needed
