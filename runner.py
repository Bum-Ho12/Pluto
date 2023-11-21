'''
this file runs the project application
defined in main.py
'''
from kivy.base import runTouchApp
from main import runApp  # Replace with the actual name of your App class

def main():
    '''
    this method execute the application
    by taking advantage  of the kivy package.
    '''
    app = runApp()
    runTouchApp(app)

if __name__ == '__main__':
    main()
