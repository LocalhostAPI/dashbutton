"""dashbutton - API Service

The main api for the buttons
"""

from setuptools import setup, find_packages
from dash import __name__, __version__
doc = __doc__.splitlines()

setup(
    name=__name__,
    version=__version__,
    description=doc[0],
    long_description='\n'.join(doc[2:]),
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        dash=dash.tasks.cli:cli
    ''',
)
