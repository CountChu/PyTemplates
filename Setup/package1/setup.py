from setuptools import setup
from setuptools import find_packages

def getDescription():

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

setup(
    name='package1',
    version='0.1',
    description=getDescription(),
    url='http://github.com/countchu',
    author='Chu',
    author_email='visualge@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False)
