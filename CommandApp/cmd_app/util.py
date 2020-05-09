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
import inspect
import traceback
from distutils.dir_util import copy_tree

#
#-------------------------------------------------------------------------------
# Include private packages.
#-------------------------------------------------------------------------------
#

#
#-------------------------------------------------------------------------------
# Log Setting functions.
#-------------------------------------------------------------------------------
#    

g_format = '%(asctime)s.%(msecs)03d |%(levelname)-5s |%(name)-4s |%(message)s'
g_datefmt = '%Y-%m-%d %H:%M:%S'

def set_logging(level_str, log_fn):
    global g_format
    global g_datefmt

    handlers = []
    
    #
    # Create a handler of logging of which the default is console.
    #

    handlers += [logging.StreamHandler()]

    #
    # Create a file handler if has log_fn.
    #
    
    if log_fn != None:
        handlers += [logging.FileHandler(log_fn)]
        
    #
    # Set logging.
    #
    
    level = get_level(level_str)
    logging.basicConfig(
        level=level,
        format=g_format,
        datefmt=g_datefmt,
        handlers=handlers)

def build_logger(tag, level_str, log_fn):
    global g_format
    global g_datefmt

    log = logging.getLogger(tag)
    log.propagate  = False
    
    level = get_level(level_str)
    log.setLevel(level)

    #
    # Create Formatter.
    #

    formatter = logging.Formatter(g_format, g_datefmt)

    #
    # Create FileHandler and add it.
    #

    if log_fn != None:
        fh = logging.FileHandler(log_fn)
        fh.setLevel(level)
        fh.setFormatter(formatter)
        log.addHandler(fh)
    
    #
    # Create StreamHandler and add it.
    #

    sh = logging.StreamHandler()
    sh.setLevel(level)    
    sh.setFormatter(formatter)
    log.addHandler(sh)
    
    return log
    
def get_level(level_str):

    #
    # Specify loggin level.
    #

    level_dict = {
        'debug':        logging.DEBUG,
        'info':         logging.INFO,
        'warning':      logging.WARNING,
        'error':        logging.ERROR,
        'critical':     logging.CRITICAL
        }
        
    level = level_dict[level_str]
    return level
    
#
#-------------------------------------------------------------------------------
# Log Displaying functions.
#-------------------------------------------------------------------------------
#     

#
# Get indent in the code.
#

def idt(indent_str = '..'):
    return indent_str * (len(traceback.extract_stack()) - 1)
    
#
# Get line number in the code.
#

def lno():
    return inspect.currentframe().f_back.f_lineno     
    
#
# get a string of a timestamp with milliseconds.
# E.g., '2019-09-05 17:18:08.339'
#

def get_now():
    return str(datetime.datetime.now())[:-3]    
    
#
#-------------------------------------------------------------------------------
# Other functions.
#-------------------------------------------------------------------------------
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
