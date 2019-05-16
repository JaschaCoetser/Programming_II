"""
Dynamic Name
By Jascha
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicNameApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Jeff John", "Fred Brown", "John Sheer"}

    def build(self):
        self.title = "Dynamic Names"
        self.root = Builder.load_file('dynamic_names.kv')
        self.display_name()
        return self.root

    def display_name(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicNameApp().run()
