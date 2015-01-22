import math
import sys
import re
import string

def main():
    if (len(sys.argv) != 3):
        print ("Usage: verilog2vhdl.py [inputfile] [outputfile]")
        exit (1)

    if (os.path.exists(sys.argv[1])==False):
        print ("Could not read "+sys.argv[1])
        exit(1)



if __name__=="__main__":
    main()