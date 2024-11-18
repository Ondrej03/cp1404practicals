"""
CP1404/CP5632 Practical
Kivy GUI program to demonstrate dynamic widgets
Created by : Ondrej Kalny
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')

        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

        return self.root


DynamicLabelsApp().run()
