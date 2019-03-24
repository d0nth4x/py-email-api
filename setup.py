# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='EmailAPI',
    version="1.0",
    packages=find_packages(),
    include_package_data=False,
    install_requires=["configparser","flask","html"],
)
