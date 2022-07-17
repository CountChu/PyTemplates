from setuptools import setup
from setuptools import find_packages

def get_desc():

    #
    # Read README.md
    #

    f = open('package2/README.md', 'r')
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
    name='package2',
    version='0.1',
    description=get_desc(),
    url='http://github.com/countchu',
    author='CountChu',
    author_email='visualge@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False)
