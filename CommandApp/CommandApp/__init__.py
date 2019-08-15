#
# FILENAME.
#       __init__.py - COMPANY_NAME(TM) Initialize Package.
#
# FUNCTIONAL DESCRIPTION.
#       The module initializes the CommandApp package.
#
# NOTICE.
#       COMPANY_NAME Confidential
#       COPYRIGHT COMPANY_NAME 2019 All RIGHTS RESERVED
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/4/24
#

#
# Include standard packages.
#

import argparse
import logging
import pdb
import os
import json
import sys

#
# Include specific packages.
#

import CommandApp.Util

#
# Build argument parser and return it.
#

def buildArgParser():

    desc = '''
The app parses command lines and dispatches the commands.

Usage 1: python CommandApp.py README.md

Usage 2: python CommandApp.py -d images

Usage 3: python CommandApp.py -d images -o output
'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Standard arguments
    #

    parser.add_argument(
            "-v",
            dest="verbose",
            action='store_true',
            help="Verbose log")

    parser.add_argument(
            '--log',
            dest='logFn',
            help='A name of a log file.')

    parser.add_argument(
            '--cfg',
            action='store_true',
            help="Read Config.py")

    #
    # Anonymous arguments.
    #

    parser.add_argument(
            'file',
            help='A file')

    #
    # Specific arguments
    #

    parser.add_argument(
            '-d',
            dest='dir',
            #required=True,
            help='A directory that contains files')

    parser.add_argument(
            '-o',
            dest='outputDir',
            help='A directory that contains output results')

    parser.add_argument(
            "--start",
            type=int,
            default=4,
            dest="start",
            help="Input start")

    return parser

#
# It reads file content into lines.
#

def readFileContent(fn):

    if not os.path.exists(fn):
        print('Error! The file is not found.')
        print(fn)
        sys.exit(0)

    f = open(fn, 'r')
    lines = f.readlines()
    f.close()

    return lines

#
# It reads base names in the dir directory.
#

def readBaseNames(dir):
    baseNameList = []
    if not os.path.exists(dir):
            print('Error! The directory is not found.')
            print(dir)
            sys.exit(0)

    for fn in os.listdir(dir):
        path = os.path.join(dir, fn)
        if not os.path.isdir(path):
            baseNameList.append(fn)

    return baseNameList

def main():

    #
    # Parse arguments
    #

    args = buildArgParser().parse_args()

    #
    # Enable log if -v
    #

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)

    #
    # Check arguments.
    #

    #
    # Open a log file if --log
    #

    if args.logFn != None:
        logF = open(args.logFn, 'w')

    #
    # If --cfg, read Config and override args.
    #

    if args.cfg:
        from CommandApp.Config import Config
        logging.info('Config = %s' % Config)

        #
        # Override args
        #

        if 'dir' in Config:
            if args.dir is None:
                args.dir = Config['dir']
                print('Override dir = %s' % args.dir)
        if 'outputDir' in Config:
            if args.outputDir is None:
                args.outputDir = Config['outputDir']
                print('Override outputDir = %s' % args.outputDir)

    #
    # Specify outputDir
    #

    if args.outputDir is None:
        args.outputDir = '%s#CommandApp' % args.dir
        print('Specify outputDir = %s' % args.outputDir)

    #
    # Check outputDir. If it doesn't exist, built it.
    #

    if not os.path.exists(args.outputDir):
        print('Make directory: %s' % args.outputDir)
        os.mkdir(args.outputDir)

    #
    # Read file base names if -d.
    #

    baseNameList = []
    if 'dir' in args and args.dir != None:
        baseNameList = readBaseNames(args.dir)

    #
    # Here is core function.
    #

    #pdb.set_trace()
    Util.handle(args.file, args.dir, baseNameList, args.outputDir)

    #
    # Close the log file if --log
    #

    if args.logFn != None:
        logF.close()

main()
