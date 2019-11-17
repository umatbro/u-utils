"""
Get `um` package version from file 'pyproject.toml'
"""
import os
import sys
import toml

with open(os.path.join(os.path.dirname(__file__), 'pyproject.toml')) as f:
    config = toml.load(f)

sys.stdout.write(config['tool']['poetry']['version'])
