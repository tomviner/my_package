from setuptools import setup, find_packages


setup(
    name='my-package',
    version='0.1.1.dev0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
