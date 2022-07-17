from setuptools import setup
from setuptools import find_packages
import pdb
import unittest

def get_desc():

    #
    # Read README.md
    #

    f = open('README.md', 'r')
    lines = f.readlines()
    f.close()
    desc = ''

    #
    # Extract desc from README.md.
    #

    s = 'init'
    for line in lines:
        if s == 'init' and line[0] == '#':
            s = 'start'
        elif s == 'start' and line[0] != '#':
            s = 'text'
        elif s == 'text' and line[0] == '#':
            s = 'end'
        else:
            s = 'error'

        if s == 'text':
            desc += line.strip()

    #
    # Return it.
    #

    #pdb.set_trace()
    return desc

def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name='cmd_app',
    version='0.1',
    description=get_desc(),
    url='https://github.com/CountChu/PyTemplates/tree/master/CommandApp',
    author='CountChu',
    author_email='visualge@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False,
    test_suite='setup.my_test_suite')
