from gym_soft_env.env import *

# factory environment renderer
# if no renderer was found the a blank renderer is returned
def make(env, width, height, radius):
    if env.env.spec.id == "Pendulum-v0":
        return PendulumRenderer(width, height, radius)
    if env.env.spec.id == "CartPole-v1":
        return CartPoleRenderer(width, height, radius)
    if env.env.spec.id == "MountainCar-v0":
        return MountainCarRenderer(width, height, radius)
    if env.env.spec.id == "MountainCarContinuous-v0":
        return MountainCarRenderer(width, height, radius)
    if env.env.spec.id == "Acrobot-v1":
        return AcrobotRenderer(width, height, radius)

    print("No renderer for ", env.env.spec.id," found!")
    return SoftRenderer(width, height, radius)