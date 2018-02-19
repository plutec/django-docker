#!/usr/bin/env python
import pip
import os
from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

REQUIREMENTS_FILE = 'requirements.txt'

setup(name='django-docker',
      packages=find_packages(),
      package_data={'docker.templates':['*']},
      version='0.1',
      description='Module to create django docker based on your project',
      author='Antonio Sanchez',
      author_email='asanchez@plutec.net',
      license='Apache Version 2',
      url='',
      download_url='',
      keywords=['docker', 'docker-ce', 'django', 'apache2', 'wsgi', 'gunicorn', 'nginx'],
      install_requires=[]
      )

      

