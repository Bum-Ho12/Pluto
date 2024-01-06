'''this file provides the window size of a device'''
import win32api

def screen_size():
    '''gets the current screen size'''
    # pylint: disable = I1101
    width = win32api.GetSystemMetrics(0)
    height = win32api.GetSystemMetrics(1)
    return width, height
