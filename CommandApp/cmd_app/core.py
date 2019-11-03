#
# FILENAME.
#       core.py - Core Module.
#
# FUNCTIONAL DESCRIPTION.
#       The module provides app with core API.
#
# NOTICE.
#       Author: visualge@gmail.com (CountChu)
#       Created on 2019/11/1
#

#
# Include standard packages.
#

import pdb
import logging

#
# Include specific packages.
#

import cmd_app.util as util

#
# It handles them.
#

def handle(fn, dir, bn_list, out_dir):
    logging.debug('handle()')
    logging.debug('fn = %s' % fn)
    logging.debug('dir = %s' % dir)
    logging.debug('bn_list = %s' % bn_list)
    logging.debug('out_dir = %s' % out_dir)
    logging.debug('CFG = %s' % util.CFG)
    #pdb.set_trace()
