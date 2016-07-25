__author__ = 'naveenkumar'
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mdc-logging',
    version='0.1',
    packages=['mdc_logging'],
    include_package_data=True,
    description='MDC logging utility in python.',
    long_description=README,
    author='Naveen Kumar',
    author_email='naveen.nitk2009@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'setuptools',
        'django>=1.6.5'
    ],
    package_dir={
        'mdc_logging': 'mdc_logging'
    }
)