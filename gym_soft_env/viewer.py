import pyglet
import numpy as np


class SoftViewer:
    def __init__(self, width, height):
        self.window = pyglet.window.Window(width=width, height=height, display=None)
        self.width = width
        self.height = height

        self.format = 'L'
        self.pitch = self.width * -1

    def update(self, pixel):
        self.window.clear()
        self.window.switch_to()
        self.window.dispatch_events()
        pyglet.image.ImageData(self.width, self.height, self.format, pixel.tobytes(), pitch=self.pitch).blit(0, 0)
        self.window.flip()

    def close(self):
        self.window.close()