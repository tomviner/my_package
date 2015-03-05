from setuptools import setup, find_packages


setup(
    name='my-package',
    version='0.1.0.dev0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
