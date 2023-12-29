'''file that defines images'''
from kivy.uix.image import Image, AsyncImage
from pluto.implementation import context_manager

@context_manager
class NetworkImage(AsyncImage):
    '''class defines the networkImage class
    required arguments:
    - sourcefile
    - bounds
    '''
    def __init__(self, image_url, bounds=None, **kwargs):
        super(NetworkImage, self).__init__(**kwargs)
        self.source = image_url
        self.pos = bounds.pos if bounds else (0, 0)
        self.size = bounds.size if bounds else (100, 100)

@context_manager
class AssetImage(Image):
    '''class that defines the assetImage class
    required arguments:
    - sourcefile
    - bounds
    '''
    def __init__(self, image_filename, bounds=None, **kwargs):
        super(AssetImage, self).__init__(**kwargs)
        self.source = image_filename
        self.pos = bounds.pos if bounds else (0, 0)
        self.size = bounds.size if bounds else (100, 100)
