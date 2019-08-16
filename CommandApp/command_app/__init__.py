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

import command_app.util

#
# Build arguments
#

def build_args():

    desc = '''
The app parses command lines and dispatches the commands.

Usage 1: python -m command_app README.md

Usage 2: python -m command_app README.md -d images

Usage 3: python -m command_app README.md -d images -o output
'''

    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawTextHelpFormatter,
                description=desc)

    #
    # Standard arguments
    #

    parser.add_argument(
            "--verbose",
            dest="verbose",
            action='store_true',
            help="Print verbose messages")

    parser.add_argument(
            "--debug",
            dest="debug",
            action='store_true',
            help="Show debug messages")

    parser.add_argument(
            '--log',
            dest='log_fn',
            help='A name of a log file.')

    parser.add_argument(
            '--cfg',
            action='store_true',
            help="Import Config.py")

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
            dest='out_dir',
            help='A directory that contains output results')

    parser.add_argument(
            "--start",
            type=int,
            default=4,
            dest="start",
            help="Input start")

    return parser.parse_args()

#
# It reads file content into lines.
#

def read_file_content(fn):

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

def read_base_names(dir):
    bn_list = []
    if not os.path.exists(dir):
            print('Error! The directory is not found.')
            print(dir)
            sys.exit(0)

    for fn in os.listdir(dir):
        path = os.path.join(dir, fn)
        if not os.path.isdir(path):
            bn_list.append(fn)

    return bn_list

#
# It load Config.py
#

def read_config():

    pattern = "\<module\s\\'(\w+\.\w+)\\'"
    text = str(sys.modules[__name__])
    logging.info('text = %s' % text)
    res = re.match(pattern, text)
    name = res.group(1)

    from config import config
    return config[name]

def main():

    #
    # Parse arguments
    #

    args = build_args()

    #
    # Enable debug messages if --debug
    #

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)

    #
    # Enable verbose messages if --verbose
    #

    if args.verbose:
        print('.............verbose..............')

    #
    # Check arguments.
    #

    #
    # Open a log file if --log
    #

    if args.log_fn != None:
        log_f = open(args.log_fn, 'w')

    #
    # If --cfg, read config and override args.
    #

    if args.cfg:
        config = read_config()

        #
        # Override args
        #

        if 'dir' in Config:
            if args.dir is None:
                args.dir = config['dir']
                print('Override dir = %s' % args.dir)
        if 'out_dir' in Config:
            if args.out_dir is None:
                args.out_dir = config['out_dir']
                print('Override outputDir = %s' % args.outputDir)

    #
    # Specify out_dir
    #

    if args.out_dir is None:
        args.out_dir = '%s#CommandApp' % args.dir
        print('Specify out_dir = %s' % args.out_dir)

    #
    # Check outputDir. If it doesn't exist, built it.
    #

    if not os.path.exists(args.out_dir):
        print('Make directory: %s' % args.out_dir)
        os.mkdir(args.out_dir)

    #
    # Read file base names if -d.
    #

    bn_list = []
    if 'dir' in args and args.dir != None:
        bn_list = read_base_names(args.dir)

    #
    # Here is core function.
    #

    #pdb.set_trace()
    util.handle(args.file, args.dir, bn_list, args.out_dir)

    #
    # Close the log file if --log
    #

    if args.log_fn != None:
        logF.close()

main()
