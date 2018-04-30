from setuptools import setup, find_packages

setup(
    name='supproperty',

    version='0.0.1.dev1',

    description='Superior property',

    long_description='Copy from README file',

    url='http://ccs.chem.ucl.ac.uk',

    author='Kristof Farkas-Pall',

    requires=['numpy'],

    packages=find_packages(),

    include_package_data=True,
)

