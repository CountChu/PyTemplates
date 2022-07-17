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
#       Updated on 2020/5/9
#

#
# Include standard packages.
#

import pdb
import logging

#
# Include private packages.
#

import common.log
from common.log import lno, idt

#
# Init the log of the module.
#

log = None
def init_log(level_str, log_fn=None):
    global log

    tag = 'CR'
    log = common.log.build_logger(tag, level_str, log_fn)
    
    #
    # Init logs of modules in the low-level packages.
    #
    
    #p1.init_log(level_str, log_fn)
    #p2.init_log(level_str, log_fn)

#
# It handles them.
#

def handle(fn, dir, bn_list, out_dir):
    log.info('%s<handle>' % idt())
    log.info('fn = %s' % fn)
    log.info('dir = %s' % dir)
    log.info('bn_list = %s' % bn_list)
    log.info('out_dir = %s' % out_dir)
    log.info('cfg = %s' % common.util.cfg)
    log.info('%s</handle> #%d' % (idt(), lno()))
    #pdb.set_trace()
