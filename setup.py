from setuptools import setup, find_packages

setup(
    name='sql_generator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'spacy>=3.0.0',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple SQL generator from natural language descriptions.',
)