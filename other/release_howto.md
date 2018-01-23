# Releasing next version

## pypirc
create `.pypirc` file with account configuration

```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository=https://pypi.python.org/pypi
username=<username>
password=<password_here>

[pypitest]
repository=https://testpypi.python.org/pypi
username=<username>
password=<password>

```


## setup.py

Example `setup.py` file

```python
from setuptools import setup, find_packages
from os import path
from codecs import open


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='um',
    version='1.3.0',  # development release
    description='Package with utilities',
    long_description=long_description,  # read this form README.rst
    url='https://github.com/umatbro/u-utils',
    author='umat',
    author_email='umatbroo@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
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
```

Before release remember to update `version`.

`install_requires` - dependencies needed to run the project

## Packaging the project

### wheel

Before you can build wheels for your project, you’ll need to install the `wheel` package:

```
pip install wheel
```

To build the wheel:

```
python setup.py bdist_wheel
```

## Uploading project to PyPi

When package distribution is created in `dist/` directory it is time to upload files.


```
twine upload dist/*
```

## Other

Remember to also keep track with your releases with git tags. To add git tag:

```
git tag 1.4.0
```

To push tag to remote:

```
git push origin <tag_name>
```

Command to push **all** tags (not recommended)

```
git push --tags
```
