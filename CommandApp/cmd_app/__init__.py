#
# FILENAME.
#       __init__.py - COMPANY_NAME(TM) Initialize Package.
#
# FUNCTIONAL DESCRIPTION.
#       The module initializes the cmd_app package.
#
# NOTICE.
#       COMPANY_NAME Confidential
#       COPYRIGHT COMPANY_NAME 2019 All RIGHTS RESERVED
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/4/24
#       Updated on 2020/5/9
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
# Include private packages.
#

import common.util as util
import common.log as mylog
import cmd_app.core as core

#
# Global variables.
#

config = None
log_01 = None
log_02 = None

#
# Main function.
#

def main():

    #
    # Parse arguments
    #

    args = build_args()
    
    #
    # If --log, enable to save logs in files.
    #  

    tag = 'CA'
    log_fn = None                       # For a general log
    log_01_fn = None                    # For a specific log 01
    log_02_fn = None                    # For a specific log 02    

    if args.log:
    
        #
        # Build the directory to save log files.
        #
        
        if not os.path.exists('log'):
            print('Build the log directory')
            os.mkdir('log')    

        date_str = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    
        #
        # Build log_fn.
        #      

        log_fn = "%s-%s.log" % (tag, date_str)
        log_fn = os.path.join('log', log_fn)
        print('Create a log file: %s' % log_fn) 

        #
        # Build log_01_fn
        #

        log_01_fn = "%s-%s-01.log" % (tag, date_str)
        log_01_fn = os.path.join('log', log_01_fn)
        print('Create a log file: %s' % log_01_fn)

        #
        # Build log_02_fn
        #

        log_02_fn = "%s-%s-02.log" % (tag, date_str)
        log_02_fn = os.path.join('log', log_02_fn)
        print('Create a log file: %s' % log_02_fn)

    #
    # set logging.
    #

    mylog.set_logging(args.level, log_fn)
    log_01 = mylog.build_simple_logger(tag+'-01', args.level, log_01_fn)
    log_02 = mylog.build_logger(tag+'-02', args.level, log_02_fn)
    
    #
    # Test a general log with level.
    #

    logging.debug(args) 
    logging.debug('It is debug level.')
    logging.info('It is info level.')
    logging.warning('It is warning level.')
    logging.error('It is error level.')
    logging.critical('It is critical level.')
    
    #
    # Test specific logs.
    #
        
    log_01.info('log_01: --------')    
    log_02.info('log_02: --------')    

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
        from common.util import cfg
        logging.debug('cfg = %s' % cfg)

    #
    # Init logs of modules.
    #

    core.init_log(args.level, log_fn)

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
    logging.info('Call core.handle()')
    core.handle(args.file, args.dir, bn_list, args.out_dir)

#
# Build arguments
#

def build_args():

    desc = '''
The app parses command lines and dispatches the commands.

Mode 1: Run the script.
    python cmd_app.py README.md
    python cmd_app.py README.md -d images
    python cmd_app.py README.md -d images -o output

Mode 2: Run library module as a script.
    python -m cmd_app README.md
    python -m cmd_app README.md -d images
    python -m cmd_app README.md -d images -o output
'''

    #
    # Build an ArgumentParser object to parse arguments.
    #

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
            '--log',
            dest='log',
            action='store_true',
            help='Enable to save log in a file.')

    parser.add_argument(
            '--level',
            dest='level',
            default='critical',
            help='Level of logging. debug < info < warning < error < critical')

    parser.add_argument(
            '--cfg',
            action='store_true',
            help="Import config.py")

    parser.add_argument(
            "--try",
            dest="try_it",
            action='store_true',
            help="Try if the command is expected.")

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

    parser.add_argument(
            '-e',
            dest='emulate',
            action='store_true',
            help='Emulate real environment.')

    return parser.parse_args()

#
# It load config.py
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

#
# Run it.
#

main()
