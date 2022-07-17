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
#       Updated on 2020/5/9
#

#
#-------------------------------------------------------------------------------
# Include standard packages.
#-------------------------------------------------------------------------------
#

import os
import sys
import re
import logging
import json
import pdb
import shutil
from distutils.dir_util import copy_tree

#
#-------------------------------------------------------------------------------
# Include private packages.
#-------------------------------------------------------------------------------
#
       
#
#-------------------------------------------------------------------------------
# Other functions.
#-------------------------------------------------------------------------------
#    

#
# get a string of a timestamp with milliseconds.
# E.g., '2019-09-05 17:18:08.339'
#

def get_now():
    return str(datetime.datetime.now())[:-3]    

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
# Read json from a file
#

def read_json(fn):
    f = open(fn)
    dict = json.load(f)
    f.close()
    return dict

#
# Write json into a file
#

def write_json(dict, fn):
    json_str = json.dumps(dict, indent=2)

    f = open(fn, 'w', encoding='utf-8')
    f.write(json_str)
    f.close()

#
# Ask if remove a directory and build the directory.
#

def ask_remove_and_build_dir(dir):

    if os.path.exists(dir):
        print('The directory exists. %s' % dir)
        key = input('Do you want to delete it? [y/n]')
        if key == 'y':
            print('Remove it.')
            shutil.rmtree(dir)

    if not os.path.exists(dir):
        print('Build the directory %s' % dir)
        os.mkdir(dir)

#
# Override args.name.
#

def override_arg(config, args, arg, name):
    if arg in config:
        if vars(args)[name] is not None:
            vars(args)[name] = config[arg]
            print('Override %s = %s' % (name, vars(args)[name]))
            config[name] = config[arg]

#
# set config.
#

cfg = {}
def set_config(config):
    global cfg
    cfg = config
    print('cfg = %s' % cfg)
