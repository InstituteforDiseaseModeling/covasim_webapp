'''
Covasim webapp installation. Typical installation is via:

    python setup.py develop

For further information, see the README.
'''

import os
import runpy
from setuptools import setup, find_packages

# Get version
cwd = os.path.abspath(os.path.dirname(__file__))
versionpath = os.path.join(cwd, 'covasim_webapp', 'version.py')
version = runpy.run_path(versionpath)['__version__']

# Get the documentation
with open(os.path.join(cwd, 'README.rst'), "r") as fh:
    long_description = fh.read()

CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: Science/Research",
    "License :: Other/Proprietary License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3.7",
]

setup(
    name="covasim_webapp",
    version=version,
    author="Cliff Kerr, Robyn Stuart, Romesh Abeysuriya, Dina Mistry, Lauren George, and Daniel Klein, on behalf of the IDM COVID-19 Response Team",
    author_email="covasim@idmod.org",
    description="Webapp for Covasim (COVID-19 Agent-based Simulator)",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='http://covasim.org',
    keywords=["Covid-19", "coronavirus", "SARS-CoV-2", "stochastic", "agent-based model", "interventions", "epidemiology", "webapp"],
    platforms=["OS Independent"],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'covasim',
        'scirisweb>=0.17.0',
        'gunicorn',
        'plotly',
        'ipywidgets',
        ]
)

