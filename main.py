'''
this file contains the main code to be ran
for the entire project to execute in python for
the Pluto framework
'''
import skia
from pluto.material import Container, Text

class RunApp:
    '''
    this is the primary method that encapsulates
    all the widgets of the application.
    '''
    def run(self):
        '''execute application'''
        # Create a Skia canvas (replace with your desired setup)
        # pylint: disable = I1101
        surface = skia.ImageSurface.MakeRasterN32Premul(400, 300)
        canvas = skia.SurfaceCanvas(surface)

        # Create widgets using Skia-based classes
        container = Container(height=100, width=200, padding=[10, 10, 10, 10], margin=[5, 5, 5, 5])
        text = Text(text="Hello, Skia!", text_color=[1, 1, 1, 1], font_size=20)
        container.add_widget(text)

        # Render the widgets
        container(canvas, 0, 0)

        # Save or display the result (replace with your desired output)
        surface.saveToFile("output.png")

# Run the Skia app
if __name__ == "__main__":
    app = RunApp()
    app.run()
