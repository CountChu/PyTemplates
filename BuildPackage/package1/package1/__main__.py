import sys
import os.path
import package1

def main():

    print('main() in package1')
    print('argv = ', sys.argv)

    package1.method1()

if __name__ == '__main__':
    main()
