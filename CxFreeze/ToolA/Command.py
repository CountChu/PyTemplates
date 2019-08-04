#
# FILENAME.
#       Command.py - SecureCore Tiano(TM) Command Module.
#
#       $PATH:
#
# FUNCTIONAL DESCRIPTION.
#       Parse the command line arguments of PhMake.
#
# MODIFICATION HISTORY.
#
# NOTICE.
#       Copyright (C) 2014 Phoenix Technologies Ltd. All Rights Reserved.
#

from Meta import *


#
# FUNCTION NAME.
#      Parse
#
# FUNCTIONAL DESCRIPTION.
#      Parse the command line and create the symbol:value table. (Such as Param[symbol]=value).
#
# INPUT.
#      sys.argv[1:] & parameters from the optional command file.
#
# OUTPUT.
#      [0]      - The symbol:value-pair table.
#      [1]      - The remaining unprocessed arguments.
#      [2]      - Macros defined from command-line.
#      [3]      - DEF #define constants
#

def Parse (Argv):

    Params = {}
    NewArgvs = []
    PrevArg = None
    ArgvConsumed = False
    Macros = {}
    DefParams = OrderedDict()

    for Param in Argv:
        Param = Param.strip()
        p = Param.upper()
        if p[0] in "-/":
            p1 = p[1:]
            if p1 in ["?", "H", "HELP", "-HELP"]:       # display the help message.
                Params["HELP"] = True
                ArgvConsumed = False
            elif p1 in ["F", "MAKEFILE"]:               # /f makefile - assign the makefile.
                PrevArg = "MAKEFILE"
                Params["MAKEFILE"] = False
                ArgvConsumed = False
            elif p1 in ["QUIET", "NOLOGO"]:             # /quiet - no copyright and logo messages.
                Params["QUIET"] = True
                ArgvConsumed = True
            elif p1 in ["D", "DEFINE"]:                 # "/d foo" or "/d foo=bar" - define macro.
                PrevArg = "DEFINE"
                ArgvConsumed = True
            elif p1 == "MAKETOOL":                      # /maketool toolname - define the external make tool.
                PrevArg = "MAKETOOL"
                ArgvConsumed = True
            elif p1 in ["DEF"]:                         # "/def foo" or "/def foo=bar" - define DEF constant.
                PrevArg = "DEF"
                ArgvConsumed = True
        else:
            if PrevArg:
                if PrevArg == "MAKEFILE":               # /f makefile - assign the makefile.
                    Params["MAKEFILE"] = Param
                    ArgvConsumed = True
                elif PrevArg == "MAKETOOL":             # /maketool toolname - define the external make tool.
                    Params["MAKETOOL"] = Param
                    ArgvConsumed = True
                elif PrevArg == "DEFINE":               # "/d foo" or "/d foo=bar" - define macro.
                    DefPair = Param.split('=', 1)
                    if len(DefPair) == 2:
                        Params[DefPair[0].upper()] = DefPair[1].upper()
                        Macros[DefPair[0].upper()] = DefPair[1]
                    else:
                        Macros[DefPair[0].upper()] = None
                    ArgvConsumed = False
                elif PrevArg == "DEF":                  # "/def foo" or "/def foo=bar" - define DEF constant.
                    DefPair = Param.split('=', 1)
                    if len(DefPair) == 2:
                        DefParams[DefPair[0]] = DefPair[1]
                    else:
                        DefParams[DefPair[0]] = ""
                    ArgvConsumed = True
            else:
                if p == "?":                            # display the help message.
                    Params["HELP"] = True
                    ArgvConsumed = False
                elif p == "DEL":                        # PhMake del.
                    Params[p] = True
                    ArgvConsumed = False                # "del" will also be passed as a build target to the make tool.
                else:
                    if '=' in p:                        # parse a bare equation in the argument list.
                        MacroPair=p.split("=", 1)
                        Params[MacroPair[0].upper()]=MacroPair[1].upper()
                        Macros[MacroPair[0]] = MacroPair[1]
                        ArgvConsumed = False
            PrevArg == None
        if not ArgvConsumed:
            NewArgvs.append(Param)
        ArgvConsumed = False

    #NEWREL: check on error: when an argument is specified but its required parameter is missing.

    return Params, NewArgvs, Macros, DefParams