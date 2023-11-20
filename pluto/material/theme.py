'''contains the initial theme styles'''

class Theme:
    '''class that defines theme of the package'''
    def __init__(self):
        # Colors
        self.primary_color = (0.2, 0.6,1,1)
        self.secondary_color = (1, 0.4,0.4,1)
        self.background_color = (1,1,1,1)
        self.text_color = (0,0,0,0)
        self.title_color = (1,0.8,0.8,1)

        # fonts
        self.title_font = ('Roboto',24)
        self.body_font = ('Arial',14)

        # button Styles
        self.button_normal_color = self.primary_color
        self.button_press_color = (0.8,0.8,0.8,1)

        # hover effects
        self.hover_color = (0.8,0.8,0.8,1)
        self.hint_color = (0.8,0.8,0.8,1)
        self.splash_color = (0.8,0.8,0.8,1)
        self.text_theme = {
            'displayLarge':{
                'color': self.text_color,
                'font_size': 20,
                'bold':True
            },
            'displayMedium':{
                'color': self.text_color,
                'font_size': 18,
                'bold':True
            },
            'displaySmall':{
                'color': self.text_color,
                'font_size': 16,
                'bold':False
            },
            'headlineLarge':{
                'color':self.title_color,
                'font_size': 16,
                'bold': True,
            },
            'headlineMedium':{
                'color':self.title_color,
                'font_size': 15,
                'bold': False,
            },
            'headlineSmall':{
                'color':self.title_color,
                'font_size': 13,
                'bold': False,
            },
            'labelLarge':{
                'color':self.text_color,
                'font_size': 14,
                'bold': False,
            },
            'labelMedium':{
                'color':self.text_color,
                'font_size': 12,
                'bold': False,
            },
            'labelSmall':{
                'color':self.text_color,
                'font_size': 11,
                'bold': False,
            },
        }
