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

#
# Include specific packages.
#

import cmd_app.util as util

#
# It handles them.
#

def handle(fn, dir, bn_list, out_dir):
    print('handle()')
    print('fn = %s' % fn)
    print('dir = %s' % dir)
    print('bn_list = %s' % bn_list)
    print('out_dir = %s' % out_dir)
    print('CFG = %s' % util.CFG)
    #pdb.set_trace()
