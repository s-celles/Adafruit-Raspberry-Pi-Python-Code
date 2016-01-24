from setuptools import setup, find_packages
NAME = 'Adafruit_Libraries'

setup(
    name=NAME,
    version='0.x.y',
    author='Adafruit',
    packages=find_packages(),
    url='http://www.adafruit.com/',
    license='LICENSE.txt',
    description='Libraries for using Adafruit Hardware on a Raspberry Pi or BeagleBone Black',
    long_description=open('README.md').read(),
)