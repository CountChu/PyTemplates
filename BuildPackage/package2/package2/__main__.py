import os.path
import pdb

def get_usage(fn):

    #
    # Read README.md
    #

    f = open(fn, 'r')
    lines = f.readlines()
    f.close()
    usage = ''

    #
    # Extract desc from README.md.
    #

    s = 'init'
    for line in lines:
        if s == 'init' and '## Usage' in line:
            s = 'start'
        elif s == 'start' and line[0] != '#':
            s = 'text'
        elif s == 'text' and line[0] == '#':
            s = 'end'
        elif s == 'init':
            s = 'init'
        elif s == 'text':
            s = 'text'
        else:
            s = 'error'

        #print('%s | %s' % (s, line))

        if s == 'text':
            usage += line

    usage = usage.strip()
    if usage[:3] == '```' and usage[-3:]  == '```':
        usage = usage[3:-3]
    usage = usage.strip()

    #
    # Return it.
    #

    return usage

def main():
    fn = os.path.join(__file__, '..', '..', 'README.md')
    usage = get_usage(fn)
    print(usage)

if __name__ == '__main__':
    main()
