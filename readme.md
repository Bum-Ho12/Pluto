This project aims to create a standard framework that can be used to create applications with python and Kivy.
Ensure Python is installed in your computer.

To complete setup, please:
1. run on cmd "python pluto.py setup"
2. run on cmd "python pluto.py fetch"

To run the application, run script on cmd
"python pluto.py run"

definition
# Stylesheet module
class Styles:
    button = {
        'background_color': 'blue',
        'text_color': 'white',
        'padding': 10,
        # Add other styles as needed
    }

    view = {
        'background_color': 'lightgray',
        'margin': 20,
        # Add other styles as needed
    }

# Button component
class Button:
    def __init__(self, text, on_click=None, style=None):
        self.text = text
        self.on_click = on_click
        self.style = style or {}

    def render(self):
        # Apply styles here
        print(f"Rendering Button with style: {self.style}")

# View component
class View:
    def __init__(self, children=None, style=None):
        self.children = children or []
        self.style = style or {}

    def render(self):
        # Apply styles here
        print(f"Rendering View with style: {self.style}")

# Example usage
button_style = Styles.button
view_style = Styles.view

button_component = Button(text="Click me", style=button_style)
view_component = View(children=[button_component], style=view_style)

# Render the components
button_component.render()
view_component.render()
