# gym_soft_env

gym_soft_env is a small python module that allows rendering environments in a inference network friendly way.
## Installation

```shell
$ git clone https://github.com/martinseilair/gym_soft_env/
$ cd gym_soft_env
$ pip install .
```

Tested with Python 3.5.2 and Ubuntu 16.04.

## Quick start

```python
import gym
import gym_soft_env

# create gym environment
env = gym.make("Pendulum-v0")

# initialize render class
ren = gym_soft_env.make(env, 28, 28, 2) # environment, width, height, blur radius

env.reset()

for t in range(10000):
    observation, reward, done, info = env.step(env.action_space.sample()) # take a random action
    # render the environment and return output image
    im = ren.render(observation)
    # optional: view the rendered image
    ren.show()

```

Rendering routines for Classic Control environments available. Build custom rendering routines by using SoftRenderer as superclass.