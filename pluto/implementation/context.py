import threading

class FlutterContextManager:
    _instance_lock = threading.Lock()
    _instance = None

    def __new__(cls):
        with cls._instance_lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.lock = threading.Lock()
                cls._instance.widgets = []
        return cls._instance

    def __enter__(self):
        print("Entering Flutter context")
        return self

    def execute_widget(self, widget):
        widget.execute(self)

    def add_widget(self, widget_name):
        with self.lock:
            self.widgets.append(widget_name)
            print(f"Added widget: {widget_name}")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Flutter context")

class WidgetMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        FlutterContextManager()._instance.widgets.append(cls)

class WidgetBase(metaclass=WidgetMeta):
    def __init__(self, name):
        self.name = name

    def execute(self, context):
        pass

class Widget1(WidgetBase):
    def execute(self, context):
        print(f"Inside Widget 1 ({self.name})")
        context.add_widget(f"Widget 1 ({self.name})")

class Widget2(WidgetBase):
    def execute(self, context):
        print(f"Inside Widget 2 ({self.name})")
        context.add_widget(f"Widget 2 ({self.name})")

# Simulate widget interactions
with FlutterContextManager() as context:
    widget1_instance = Widget1("Instance 1")
    widget2_instance = Widget2("Instance 2")

# Access the widgets outside the context
print("Outside Flutter context")
print("All widgets:", FlutterContextManager().widgets)
