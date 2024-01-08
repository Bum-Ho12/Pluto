'''file that contains logic for reload capabilities'''
import os
import sys
import importlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from lib.main import RunApp

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
        self.reload_components()

    def reload_components(self):
        '''tracker for which components to reload'''
        for module in list(sys.modules.keys()):
            if module.startswith('your_project_name.'):  # Adjust based on your project's structure
                importlib.reload(sys.modules[module])
                print(f"Reloaded: {module}")

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
        framework.observer.stop()

    framework.observer.join()
