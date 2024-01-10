'''file that contains logic for reload capabilities'''
import os
import sys
import importlib
from kivy.app import App
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from lib.main import RunApp
from lib.pluto_app import MainLogic


LIB_PATH = os.getcwd()

class HotReloadHandler(FileSystemEventHandler):
    '''hot reload class mechanism'''
    # pylint: disable = W0246
    def __init__(self):
        super().__init__()

    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith('.py'):
            return

        print(f"Changes detected in {event.src_path}")
        if "pluto_app.py" in event.src_path:
            self.reload_main()

    def reload_main(self):
        '''reload the main module'''
        try:
            # Reload the main module
            importlib.reload(sys.modules['pluto_app'])
            self.restart_kivy_app()
            print("Reloaded: pluto_app.py")
        # pylint: disable = W0718
        except Exception as e:
            print(f"Error during reload: {e}")

    def restart_kivy_app(self):
        '''invokes new instance of the root widget'''
        App.get_running_app().root_window.remove_widget(App.get_running_app().root)
        new_main_widget = MainLogic.run_app()
        App.get_running_app().root = new_main_widget
        App.get_running_app().root_window.add_widget(new_main_widget)

class ProjectEntryPoint:
    '''my Pluto entry point'''
    def __init__(self):
        self.setup_file_watcher()

    def setup_file_watcher(self):
        '''sets up a watcher for the files in the framework'''
        self.observer = Observer()
        self.observer.schedule(HotReloadHandler(), path=LIB_PATH, recursive=True)
        self.observer.start()

def reload_runner():
    '''entry method to enable reload to work efficiently'''
    framework = ProjectEntryPoint()

    try:
        # Your Kivy entry point or runner code
        RunApp().run()
    except KeyboardInterrupt:
        pass
    # ensures kivy app is stopped properly
    App.get_running_app().stop()
    # this stops the watcher after the kivy stops running app
    framework.observer.stop()
    framework.observer.join()
