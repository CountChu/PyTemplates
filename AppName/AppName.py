#
# FILENAME.
#       AppName.py - SecureCore Tiano(TM) AppName Console Application Module.
#
#       $PATH:
#
# FUNCTIONAL DESCRIPTION.
#       The module implements the entry point of this console application.
#
# MODIFICATION HISTORY.
#
# NOTICE.
#       Copyright (C) 2013 Phoenix Technologies Ltd. All Rights Reserved.
#

from Meta import *
#Debug (True)

def PrintUtilityInfo ():
    print ""
    print "SecureCore Technology(TM) %s Utility."" Version %i.%i" % \
          (UTILITY_NAME, UTILITY_MAJOR_VERSION, UTILITY_MINOR_VERSION)
    print "Copyright (C) 2013 Phoenix Technologies Ltd. All Rights Reserved"
    print ""

def main ():

    #
    # Print utility information.
    #

    PrintUtilityInfo ()
    
    #
    # Create Params
    #
    
    Params = {}

    #
    # Parse the command.
    #

    Status = Command.Parse (sys.argv, Params)
    if Status != STATUS_SUCCESS:
        DPRINTF ("Calling Parse() failed, status = %d", Status)
        CommandHelp (Params)
        return Status
    DPRINTF ("Params: %s" % Params)
    
    #
    # Set default command parameters.
    #

    Status = Command.SetDefault (Params)
    if Status != STATUS_SUCCESS:
        DPRINTF ("Calling SetDefault() failed, status = %d", Status)
        print ("  Failed!")
        return Status    
    
    #
    # Dispatch commands.
    #
    
    Status = Command.Dispatch (Params)
    if Status == STATUS_UNSUPPORTED:
        print ("  This command has not been supported yet!");
        return Status
    if Status != STATUS_SUCCESS:
        print ("  Failed!")
        return Status

if __name__ == "__main__":
    main()

