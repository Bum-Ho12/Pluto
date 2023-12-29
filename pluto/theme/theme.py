'''contains the initial theme styles'''

class Theme:
    '''class that defines the THeme of Pluto'''
    def __init__(self,
                primary_color=(0.2, 0.6, 1, 1),
                secondary_color=(1, 0.4, 0.4, 1),
                background_color=(1, 1, 1, 1),
                text_color=(0, 0, 0, 1),
                title_color=(1, 0.8, 0.8, 1),
                button_normal_color=None,
                button_press_color=(0.8, 0.8, 0.8, 1),
                hover_color=(0.8, 0.8, 0.8, 1),
                hint_color=(0.8, 0.8, 0.8, 1),
                splash_color=(0.8, 0.8, 0.8, 1),
                title_font=('Roboto', 24),
                body_font=('Arial', 14)):
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.background_color = background_color
        self.text_color = text_color
        self.title_color = title_color
        self.button_normal_color = button_normal_color or primary_color
        self.button_press_color = button_press_color
        self.hover_color = hover_color
        self.hint_color = hint_color
        self.splash_color = splash_color

        self.title_font = title_font
        self.body_font = body_font

        self.text_theme = {
            'displayLarge': {'color': text_color, 'font_size': 20, 'bold': True},
            'displayMedium': {'color': text_color, 'font_size': 18, 'bold': True},
            'displaySmall': {'color': text_color, 'font_size': 16, 'bold': False},
            'headlineLarge': {'color': title_color, 'font_size': 16, 'bold': True},
            'headlineMedium': {'color': title_color, 'font_size': 15, 'bold': False},
            'headlineSmall': {'color': title_color, 'font_size': 13, 'bold': False},
            'labelLarge': {'color': text_color, 'font_size': 14, 'bold': False},
            'labelMedium': {'color': text_color, 'font_size': 12, 'bold': False},
            'labelSmall': {'color': text_color, 'font_size': 11, 'bold': False},
        }
    def get_text_theme(self,style):
        '''gets text Theme'''
        return self.text_theme.get(style,{})
