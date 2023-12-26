'''this file contains code that defines the behavior bottomNavBar'''
import skia
# pylint: disable = E0611
from skia import Rect

class BottomNavBar:
    '''
    this class provides the bottomNavBar
    '''
    def __init__(self, labels,app,
            button_color=(0.7, 0.7, 0.7, 1),
            text_color=(0, 0, 0, 1),
            text_size=20
            ):
        self.label = labels
        self.app = app
        self.button_color = button_color
        self.text_color = text_color
        self.text_size = text_size
        self.buttons = []

        # Create buttons for each screen
        for label in labels:
            button = SkiaButton(label=label, on_click=self.switch_screen,
                                button_color=button_color, text_color=text_color,
                                text_size = text_size
            )
            self.add_button(button)

    def add_button(self, button):
        '''adds button to the navigation bar'''
        self.buttons.append(button)

    def switch_screen(self, instance):
        '''
        this method helps switch screens
        '''
        screen_name = instance.label.lower()
        self.app.get_running_app().root.screen_manager.current = screen_name

class SkiaButton:
    '''button that provides interface to navigation bar'''
    def __init__(self, label, on_click=None,
                button_color=(0.7, 0.7, 0.7, 1), text_color=(0, 0, 0, 1),
                text_size=20
                ):
        self.label = label
        self.on_click = on_click
        self.button_color = button_color
        self.text_color = text_color
        self.text_size = text_size

    def _call__(self, canvas, x, y, width, height):
        # Render the button using Skia drawing operations
        # pylint: disable = I1101
        paint = skia.Paint()
        paint.color = skia.Color(*[int(c * 255) for c in self.button_color])

        rect = Rect.MakeLTRB(x, y, x + width, y + height)
        canvas.drawRect(rect, paint)

        # Render the label
        text_paint = skia.Paint()
        text_paint.color = skia.Color(*[int(c * 255) for c in self.text_color])
        text_paint.text_size = self.text_size

        text_rect = Rect()
        text_paint.measureText(self.label, text_rect)

        text_x = x + (width - text_rect.width()) / 2
        text_y = y + (height + text_rect.height()) / 2

        canvas.drawText(self.label, text_x, text_y, text_paint)

    def handle_click(self):
        '''handles onclick functionality'''
        if self.on_click:
            self.on_click(self)
