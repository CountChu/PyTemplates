from setuptools import setup
from setuptools import find_packages

def get_desc():

    #
    # Read README.md
    #

    f = open('package1/README.md', 'r')
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

    return desc

setup(
    name='package1',
    version='0.1',
    description=get_desc(),
    url='http://github.com/countchu',
    author='Chu',
    author_email='visualge@gmail.com',
    license='MIT',
    packages=['package1'],
    package_dir={'package1': 'package1'},
    package_data={
        'package1': ['README.md']
    },
    include_package_data=True,
    zip_safe=False)
