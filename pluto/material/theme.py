'''contains the initial theme styles'''

import skia

class Theme:
    '''class that defines theme of the package'''
    def __init__(self,
                primary_color=(0.2, 0.6, 1, 1),
                secondary_color=(1, 0.4, 0.4, 1),
                background_color=(1, 1, 1, 1),
                text_color=(0, 0, 0, 0),
                title_color=(1, 0.8, 0.8, 1),
                button_normal_color=None,
                button_press_color=(0.8, 0.8, 0.8, 1),
                hover_color=(0.8, 0.8, 0.8, 1),
                hint_color=(0.8, 0.8, 0.8, 1),
                splash_color=(0.8, 0.8, 0.8, 1),
                title_font=('Roboto', 24),
                body_font=('Arial', 14)):
        # Colors
        # pylint: disable = I1101
        self.primary_color = skia.Color(*[int(c * 255) for c in primary_color])
        self.secondary_color = skia.Color(*[int(c * 255) for c in secondary_color])
        self.background_color = skia.Color(*[int(c * 255) for c in background_color])
        self.text_color = skia.Color(*[int(c * 255) for c in text_color])
        self.title_color = skia.Color(*[int(c * 255) for c in title_color])
        self.button_normal_color = skia.Color(*[int(c * 255) for c in button_normal_color]) if button_normal_color else self.primary_color
        self.button_press_color = skia.Color(*[int(c * 255) for c in button_press_color])
        self.hover_color = skia.Color(*[int(c * 255) for c in hover_color])
        self.hint_color = skia.Color(*[int(c * 255) for c in hint_color])
        self.splash_color = skia.Color(*[int(c * 255) for c in splash_color])

        # Fonts
        self.title_font = skia.Typeface(title_font[0], title_font[1])
        self.body_font = skia.Typeface(body_font[0], body_font[1])

        self.text_theme = {
            'displayLarge': {
                'color': self.text_color,
                'font_size': 20,
                'bold': True
            },
            'displayMedium': {
                'color': self.text_color,
                'font_size': 18,
                'bold': True
            },
            'displaySmall': {
                'color': self.text_color,
                'font_size': 16,
                'bold': False
            },
            'headlineLarge': {
                'color': self.title_color,
                'font_size': 16,
                'bold': True,
            },
            'headlineMedium': {
                'color': self.title_color,
                'font_size': 15,
                'bold': False,
            },
            'headlineSmall': {
                'color': self.title_color,
                'font_size': 13,
                'bold': False,
            },
            'labelLarge': {
                'color': self.text_color,
                'font_size': 14,
                'bold': False,
            },
            'labelMedium': {
                'color': self.text_color,
                'font_size': 12,
                'bold': False,
            },
            'labelSmall': {
                'color': self.text_color,
                'font_size': 11,
                'bold': False,
            },
        }
