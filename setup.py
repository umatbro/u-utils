from setuptools import setup, find_packages
from os import path
from codecs import open


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='um_utils',
    version='1.2.0.dev1',  # development release
    description='Package with utilities',
    long_description='',  # read this form README.rst
    url='https://github.com/umatbro/u-utils',
    author='umat',
    author_email='umatbroo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        'Programming Language :: JavaScript',
        'Topic :: Utilities',
    ],
    keywords='utils',
    packages=find_packages(exclude=['docs']),
    install_requires=[],
    python_requires='>=3',
    entry_points={
        'console_scripts': []
    }
)
