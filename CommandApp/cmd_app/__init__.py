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
import sys
import re
import datetime

#
# Include specific packages.
#

import cmd_app.util as util
import cmd_app.core as core

#
# Build arguments
#

def build_args():

    desc = '''
The app parses command lines and dispatches the commands.

Usage 1: python -m cmd_app README.md

Usage 2: python -m cmd_app README.md -d images

Usage 3: python -m cmd_app README.md -d images -o output
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
            dest='log',
            action='store_true',
            help='Enable to save log in a file.')

    parser.add_argument(
            '--cfg',
            action='store_true',
            help="Import config.py")

    parser.add_argument(
            "--check",
            dest="check",
            action='store_true',
            help="Enable check.")

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
# It load Config.py
#

def read_config():

    pattern = "\<module\s\\'(.+)\\'\sfrom"
    text = str(sys.modules[__name__])
    logging.debug('text = %s' % text)
    res = re.match(pattern, text)
    #pdb.set_trace()
    name = res.group(1)

    from config import config

    if name not in config:
        return None

    return config[name]

def main():

    #
    # Parse arguments
    #

    args = build_args()
    #pdb.set_trace()

    #
    # Specify loggin level. If --debug, the level is DEBUG.
    #

    level = logging.INFO
    if args.debug:
        level = logging.DEBUG

    #
    # Create a handler of logging of which the default is console.
    #

    handlers = []
    handlers += [logging.StreamHandler()]

    #
    # If --log, enable to save log in a file.
    #

    if args.log:
        tag = 'CmdApp'
        log_fn = datetime.datetime.now().strftime(tag+"-%Y%m%d-%H%M%S.log")
        print('Create a log file: %s' % log_fn)
        handlers += [logging.FileHandler(log_fn)]

    logging.basicConfig(
        level=level,
        format='%(asctime)s.%(msecs)03d |%(levelname)-8s |%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=handlers)

    logging.debug(args)
    logging.info('The level is info.')

    #
    # Enable verbose messages if --verbose
    #

    if args.verbose:
        print('.............verbose..............')

    #
    # Check arguments.
    #

    #
    # If --cfg, specify default values if args don't exist.
    #

    if args.cfg:
        config = read_config()

        #
        # Override args
        #

        util.set_default_arg(config, args, '-d', 'dir')
        util.set_default_arg(config, args, '-o', 'out_dir')

        util.set_config(config)
        from cmd_app.util import cfg
        logging.debug('cfg = %s' % cfg)

    #
    # Specify out_dir
    #

    #pdb.set_trace()
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
        bn_list = util.read_base_names(args.dir)
        #pdb.set_trace()

    #
    # Here is core function.
    #

    #pdb.set_trace()
    core.handle(args.file, args.dir, bn_list, args.out_dir)

main()
