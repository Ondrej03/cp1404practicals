"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to km
Created by : Ondrej Kalny
"""

from kivy.app import App
from kivy.graphics.vertex_instructions import StripMesh
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

CONVERSION_RATE_MILES_TO_KM = 1.609344


class ConvertKmToMilesApp(App):
    """ ConvertKmToMilesApp is a Kivy App for squaring a number """

    output_conversion = StringProperty()


    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Km to miles Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """

        try:
            self.output_conversion = f"{float(value) * CONVERSION_RATE_MILES_TO_KM:.4f}"
        except ValueError:
            self.output_conversion = "0.0"

    def handle_increment(self, step):
        """handle incrementation of input value"""
        try:
            self.root.ids.input_number.text = str(float(self.root.ids.input_number.text) + step)
        except ValueError:
            self.root.ids.input_number.text = "1" if step == 1 else "-1"

ConvertKmToMilesApp().run()
