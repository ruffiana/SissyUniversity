# -*- coding: utf-8 -*-

# Learn more: https://github.com/ruffiana/SissyUniversity/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sissy_university',
    version='0.1.0',
    description='Python interface and Discord bot for sissy-university',
    long_description=readme,
    author='ruffiana',
    author_email='ruffiana.plays@gmail.com',
    url='https://github.com/ruffiana/SissyUniversity',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

