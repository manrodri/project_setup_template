from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='MyTemplate',
    version='0.1.0',
    description='a basic Document class to be used in a text editor',
    long_description=readme,
    author='Manuel Rodriguez',
    author_email='manuel@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)

