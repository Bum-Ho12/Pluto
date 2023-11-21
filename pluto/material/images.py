'''file that defines images'''
from kivy.uix.image import AsyncImage,Image
from pluto.implementation import Context

class NetworkImage(AsyncImage, Context):
    '''class that defines Network image'''
    def __init__(self, image_url,**kwargs):
        super(NetworkImage,self).__init__(source = image_url,**kwargs)

class AssetImage(Image):
    '''class that defines asset image'''
    def __init__(self, image_filename, **kwargs):
        super(AssetImage, self).__init__(source=image_filename, **kwargs)
