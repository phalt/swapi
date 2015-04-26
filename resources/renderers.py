from __future__ import unicode_literals
from rest_framework import renderers


class WookieeRenderer(renderers.JSONRenderer):
    media_type = "application/json"
    charset = 'utf-8'
    format = "wookiee"
    lookup = {
        "a": "ra",
        "b": "rh",
        "c": "oa",
        "d": "wa",
        "e": "wo",
        "f": "ww",
        "g": "rr",
        "h": "ac",
        "i": "ah",
        "j": "sh",
        "k": "or",
        "l": "an",
        "m": "sc",
        "n": "wh",
        "o": "oo",
        "p": "ak",
        "q": "rq",
        "r": "rc",
        "s": "c",
        "t": "ao",
        "u": "hu",
        "v": "ho",
        "w": "oh",
        "x": "k",
        "y": "ro",
        "z": "uf",
    }

    def render(self, data, media_type=None, renderer_context=None):
        encoded_data = super(WookieeRenderer, self).render(
            data, media_type, renderer_context
        )
        return bytes(self.translate_to_wookie(encoded_data))

    def translate_to_wookie(self, data):
        translated_data = ""
        for char in data:
            if char in self.lookup:
                translated_data += self.lookup[char]
            else:
                translated_data += char
        return translated_data
