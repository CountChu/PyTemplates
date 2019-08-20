#
# FILENAME.
#       util.py - Utility Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module provides app with common utility functions.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/4/24
#

#
# Include standard packages.
#

import os
import sys
import re
import logging
import pdb

#
# Include specific packages.
#

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
# Specify a default value for args.name if it doesn't exist.
#

def set_default_arg(config, args, arg, name):
    if arg in config:
        if vars(args)[name] is None:
            vars(args)[name] = config[arg]
            print('Override %s = %s' % (name, vars(args)[name]))
            config[name] = config[arg]

#
# set config.
#

CFG = {}
def set_config(config):
    global CFG
    CFG = config
    logging.info('CFG = %s' % CFG)
