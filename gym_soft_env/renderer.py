from PIL import Image, ImageDraw, ImageFilter, ImageOps
import gym_soft_env.viewer as viewer
import numpy as np


class SoftRenderer:
    def __init__(self, width, height, radius):
        self.viewer = []
        self.width = width
        self.height = height
        self.radius = radius
        self.layers = {}

    def render(self, observation):
        # clear screen
        self.pixel = Image.new('L', (self.width, self.height), color='white')

        # drawing routine of the individual environment
        self.draw(observation)

        # apply gaussian blur
        self.pixel = np.asarray(self.pixel.filter(ImageFilter.GaussianBlur(radius=self.radius)))

        # return generated image
        return self.pixel

    def show(self):
        if not self.viewer:
            self.viewer = viewer.SoftViewer(self.width, self.height)

        if self.viewer:
            self.viewer.update(self.pixel)

    def close(self):
        if self.viewer:
            self.viewer.close()

    def draw(self, observation):
        pass

    def create_ellipse(self, key, width_pc, height_pc):
        # create image
        self.layers[key] = Image.new('L', (round(width_pc*self.width), round(height_pc*self.width)), color="black")
        draw = ImageDraw.Draw(self.layers[key])
        # draw ellipse on image
        draw.ellipse((0, 0, round(width_pc*self.width), round(height_pc*self.height)), 255)

    def draw_ellipse(self, name, p, position, angle, getpos=0.0):

        # p defines the position of rotation axis on the ellipses longest chord.
        #   p =  0.0: middle of the ellipse
        #   p =  1.0: border on the right
        #   p = -1.0: border on the left

        # rotate
        rotated = self.layers[name].rotate(angle/np.pi*180.0, expand=True)

        # get image sizes of ellipse prototype and rotated version
        pw, ph = self.layers[name].size
        rw, rh = rotated.size

        # calculate position where rotated image should be placed
        px = int(round(position[0]*self.width - (rw / 2.0 + p * pw / 2.0 * np.cos(angle))))
        py = int(round(position[1]*self.height - (rh / 2.0 - p * pw / 2.0 * np.sin(angle))))
        self.pixel.paste(ImageOps.invert(rotated), (px, py), rotated)

        getposx = px + (p-getpos) * pw / 2.0 * np.cos(angle)
        getposy = py + (p-getpos) * pw / 2.0 * np.sin(angle)

        getposx = position[0] + ((getpos - p) * pw / 2.0 * np.cos(angle))/self.width
        getposy = position[1] - ((getpos - p) * pw / 2.0 * np.sin(angle))/self.width

        return (getposx, getposy)

