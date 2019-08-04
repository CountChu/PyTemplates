#
# FILENAME.
#       Test.py - Lenovo(TM) Test Application.
#
# FUNCTIONAL DESCRIPTION.
#       The module parses command line and dispatches the command. 
#
# NOTICE.
#       Lenovo Confidential
#       COPYRIGHT LENOVO 2019 All RIGHTS RESERVED
#

#
# Include standard packages.
#

import argparse
import logging

import os

#
# Build argument parser and return it.
#
    
def buildArgParser():

    parser = argparse.ArgumentParser(
                description='Build ...')
                
    #
    # Standard arguments
    #
                
    parser.add_argument(
            "-v", 
            dest="verbose", 
            action='store_true',    
            help="Verbose log") 
            
    #
    # Anonymous arguments.
    #
                            
    #
    # Specific arguments
    #     
                
    parser.add_argument(
            "-d", 
            dest="directory",    
            help="Directory where image files are")   

    parser.add_argument(
            "-f", 
            dest="file",    
            help="File name of an image.")    

    parser.add_argument(
            "--low",
            default=200,
            type=int,
            dest="low",  
            help="Low of the threashold")     

    return parser

def test(fn, low):
    print(fn)
    
def main():    

    #
    # Parse arguments
    #
    
    args = buildArgParser().parse_args()
    
    #
    # Enable log if -v
    #
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.info(args)

    #
    # call test()
    #

    if args.file is not None:
        test(args.file, args.low)

    if args.directory is not None:
        for fn in os.listdir(args.directory):
            if fn[-4:] != '.png':
                continue

            logging.info('fn = %s' % fn)
            fn = args.directory + '/' + fn
            test(fn, args.low)    

if __name__ == '__main__':

    main()