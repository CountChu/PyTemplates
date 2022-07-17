#
# FILENAME.
#       log.py - Log Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module provides app with log functions.
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

import inspect
import traceback
import logging

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
    
def build_simple_logger(tag, level_str, log_fn):

    log = logging.getLogger(tag)
    log.propagate  = False
    
    level = get_level(level_str)
    log.setLevel(level)

    #
    # Create FileHandler and add it.
    #

    if log_fn != None:
        fh = logging.FileHandler(log_fn)
        fh.setLevel(level)
        log.addHandler(fh)
    
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
