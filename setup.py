from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wetai',
    version='0.0.1',
    description='wetAI Python utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/braingeneers/wetai',
    author='Braingeneers',
    keywords=['machine-learning', 'jupyter', 'neuroscience', 'wetai', 'braingeneers'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=()),
    install_requires=['numpy', 'scipy', 'requests'],
    include_package_data=True)
