#
# FILENAME.
#       Debug.py - SecureCore Tiano(TM) build Utility Debug Instrumentation Macros.
#
#       $PATH:
#
# FUNCTIONAL DESCRIPTION.
#       This include file defines the definitions used by debugging instrumentation
#       in this driver.
# 
#       This file contains definitions for DPRINTF_class, DEBUG_class,
#       and ASSERT_class macros, in order to standardize instrumentation.
#
# MODIFICATION HISTORY.
#
# NOTICE.
#       Copyright (C) 2013 Phoenix Technologies Ltd. All Rights Reserved.
#

from Meta import *

STATUS_SUCCESS = 0
STATUS_UNSUPPORTED = 1
STATUS_INVALID_PARAMETER = 2
STATUS_ABORTED = 3

_Logger = logging.getLogger("sct_debug")
_Formatter = logging.Formatter('%(filename)-20s(%(lineno)04d): %(funcName)-16s: %(message)s')
_Logger.setLevel(logging.INFO)
_Channel = logging.StreamHandler(sys.stdout)
_Channel.setFormatter(_Formatter)
_Logger.addHandler(_Channel)
DPRINTF = _Logger.info
_Logger.disabled = True
    
def Debug (Flag):
    _Logger.disabled = not Flag    
    
def DebugEnabled ():
    return not _Logger.disabled
        
def ReportError (ErrorCode):
    print ("- Failed - (%s, %d)" % (UTILITY_NAME, ErrorCode)) # Don't update this displaying text because other pipe programs read it and report error.
    sys.exit (ErrorCode)        
        
def ReportError2 (ErrorCode):
    print ("- Failed - (%s, %d)" % (UTILITY_NAME, ErrorCode)) # Don't update this displaying text because other pipe programs read it and report error.
    File = open ("SctErrorCode.txt", "w+")
    File.write ("%d\n" % ErrorCode)
    File.close ()
    sys.exit (ErrorCode)    


