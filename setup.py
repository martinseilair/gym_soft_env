import os
from setuptools import setup
from setuptools import find_packages

setup(
    name = "gym_soft_env",
    version = "0.0.1",
    author = "Martin Seiler",
    description = ("Open AI Gym with soft image observations"),
    license = "",
    keywords = "openai gym environment soft image",
    packages=find_packages(),
    install_requires=[
        'gym'
    ],
)