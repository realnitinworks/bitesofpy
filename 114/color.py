import os
import sys
import struct
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.rgb = COLOR_NAMES.get(color.upper())
        self.color = color

    @staticmethod
    def hex2rgb(hex_value):
        return tuple(
            int(hex_value.lstrip('#')[i:i + 2], 16)
            for i in (0, 2, 4)
        )

    @staticmethod
    def rgb2hex(rgb_value):
        if any(int(value) < 0 or int(value) > 255 for value in rgb_value):
            raise ValueError

        try:
            hex_value = "".join(
                hex(value).lstrip('0').lstrip('x') if value != 0 else '00'
                for value in rgb_value
            )
        except TypeError:
            raise ValueError


        return f'#{hex_value}'

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return f"{self.rgb}" if self.rgb else "Unknown"
