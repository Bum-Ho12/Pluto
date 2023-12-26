'''file that defines images'''
import skia

class NetworkImage:
    '''class that defines Network image'''
    def __init__(self, image_url, bounds=None):
        self.image_url = image_url
        #pylint: disable = I1101
        self.bounds = bounds or skia.Rect(0, 0, 100, 100)  # Default bounds, adjust as needed

    def load(self):
        '''loads '''
        # Implement the logic to load the image from the network

    def __call__(self, canvas, x, y):
        # Load the image (you need to implement the actual image loading logic)
        self.load()

        # Rendering the image using Skia
        if self.image_url:
            # Assuming you have loaded the image into a Skia Bitmap object
            #pylint: disable = I1101
            bitmap = skia.Bitmap()
            # Implement the logic to load the image into the bitmap

            # Draw the image
            canvas.drawImageRect(bitmap, self.bounds, skia.Paint())

class AssetImage:
    '''class that defines asset image'''
    def __init__(self, image_filename, bounds=None):
        self.image_filename = image_filename
        #pylint: disable = I1101
        self.bounds = bounds or skia.Rect(0, 0, 100, 100)  # Default bounds, adjust as needed

    def load(self):
        '''loads'''
        # Implement the logic to load the image from the assets


    def __call__(self, canvas, x, y):
        # Load the image (you need to implement the actual image loading logic)
        self.load()

        # Rendering the image using Skia
        if self.image_filename:
            # Assuming you have loaded the image into a Skia Bitmap object
            # pylint: disable = I1101
            bitmap = skia.Bitmap()
            # Implement the logic to load the image into the bitmap

            # Draw the image
            canvas.drawImageRect(bitmap, self.bounds, skia.Paint())
