import sys

def main():
    print('main() in module2')
    print('argv = ', sys.argv)

def method1():
    print('It is method1() of package2.module2()')

if __name__ == '__main__':
    main()
elif __name__ == 'package2.module2':
    print('The package2.module2 is imported.')
