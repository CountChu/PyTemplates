#
# FILENAME.
#       Command.py - SecureCore Tiano(TM) Command Module.
#
#       $PATH:      
#
# FUNCTIONAL DESCRIPTION.
#      The module parses command line and dispatches the command. 
#
# NOTICE.
#       Copyright (C) 2014 Phoenix Technologies Ltd. All Rights Reserved.
#

#
# Include standard header files.
#

from Meta import *

#
# Usage 1. AppName -help
# Usage 2. AppName -status
#

def Parse (Argv, Params):

    #
    # Init Params.
    #

    Params ["Help"] = False
    Params ["Status"] = False

    #
    # Commands
    #

    STATE_INIT = 1
    STATE_HELP = 2                          # for -help
    STATE_STATUS = 3                        # for -status

    #
    # Parameters.
    #

    #
    # Error.
    #

    STATE_ERROR = 0

    #
    # Build Params.
    # 
    
    s = STATE_INIT
    for Param in Argv [1:]:
        
        #
        # -help
        #
        
        if s == STATE_INIT and Param == "-help":
            s = STATE_HELP
        
        #
        # -status
        #
            
        elif s == STATE_INIT and Param == "-status":
            s = STATE_STATUS
            
        #
        # Parsing parameters is failed.
        #
        
        else:
            s = STATE_ERROR
            break;
            
        DPRINTF ("%03d | %s", s, Param)
        
        #
        # Build Parameters
        #
        
        if s == STATE_HELP:
            Params ["Help"] = True
            
        elif s == STATE_STATUS:    
            Params ["Status"] = True
            
    if s == STATE_INIT:
        return STATUS_INVALID_PARAMETER
    elif s == STATE_ERROR:
        return STATUS_INVALID_PARAMETER
        
    DPRINTF ("Params:")
    DPRINTF ("  Help   = %d", Params ["Help"])
    DPRINTF ("  Status = %d", Params ["Status"])
    
    return STATUS_SUCCESS
    
def SetDefault (Params):    
    return STATUS_SUCCESS

def Dispatch (Params):
    Status = STATUS_SUCCESS
    
    if Params ["Help"]:
        Status = CommandHelp (Params)
        if Status != STATUS_SUCCESS:
            DPRINTF ("Calling CommandHelp() failed, status = %d", Status)
        
    elif Params ["Status"]:
        Status = CommandStatus (Params)
        if Status != STATUS_SUCCESS:
            DPRINTF ("Calling CommandStatus() failed, status = %d", Status)
        
    return Status
        
