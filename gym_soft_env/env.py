from gym_soft_env.renderer import SoftRenderer
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import numpy as np


class PendulumRenderer(SoftRenderer):
    def __init__(self, width, height, radius):
        super(PendulumRenderer, self).__init__(width, height, radius)

        self.create_ellipse("pendulum", 0.4, 0.1)

    def draw(self, observation):

        # 0: cos(theta)
        # 1: sin(theta)
        # 2: theta dot

        angle = np.arctan2(observation[0], observation[1])
        self.draw_ellipse("pendulum", 1.0, (0.5, 0.5), -angle)


class CartPoleRenderer(SoftRenderer):
    def __init__(self, width, height, radius):
        super(CartPoleRenderer, self).__init__(width, height, radius)

        self.create_ellipse("pole", 0.20, 0.06)

    def draw(self, observation):

        # 0: cart position
        # 1: cart velocity
        # 2: pole angle
        # 3: pole velocity at tip

        self.draw_ellipse("pole", 1.0, (observation[0]/4.8 + 0.5, 0.5), -observation[2] - np.pi/2)


class MountainCarRenderer(SoftRenderer):
    def __init__(self, width, height, radius):
        super(MountainCarRenderer, self).__init__(width, height, radius)

        self.create_ellipse("car", 0.2, 0.2)

    def draw(self, observation):
        # 0: position
        # 1: velocity

        # terrain
        y = -np.sin(3 * observation[0])*0.3+0.5
        x = (observation[0] - (-1.7))/ (1.1 - (-1.7))

        self.draw_ellipse("car", 1.0, (x, y), 0)


class AcrobotRenderer(SoftRenderer):
    def __init__(self, width, height, radius):
        super(AcrobotRenderer, self).__init__(width, height, radius)

        self.create_ellipse("beam1", 0.2, 0.07)
        self.create_ellipse("beam2", 0.2, 0.07)

    def draw(self, observation):
        # 0: sin(theta1)
        # 1: cos(theta2)
        # 2: sin(theta2)
        # 3: thetaDot1
        # 4: thetaDot2

        theta1 = np.arctan2(observation[0], observation[1])
        theta2 = np.arctan2(observation[1], observation[2])

        pos = self.draw_ellipse("beam1", 1.0, (0.5, 0.5), -theta1+np.pi, getpos=-1.2)
        self.draw_ellipse("beam2", 1.0, pos, -theta1 - theta2+np.pi)





