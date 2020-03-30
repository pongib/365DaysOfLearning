from setuptools import setup, find_packages

setup(
    name='words',  # Required    
    version='1.0.0',  # Required
    package_dir={'': 'src'},
    packages=find_packages(where='src'), 
    python_requires='>=3.6, <4'
)
