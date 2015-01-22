#! /usr/local/bin/python3
#
#$Author: ee364e07 $
#$Date: 2014-11-04 17:29:08 -0500 (Tue, 04 Nov 2014) $
#$Revision: 70411 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F14/students/ee364e07/Lab08/verilog2vhdl.py $
#$Id: verilog2vhdl.py 70411 2014-11-04 22:29:08Z ee364e07 $

from vtools import *
import sys
if __name__ == "__main__":
    if(len(sys.argv) > 3):
        print("Usage: verilog2vhdl.py [infile] [outfile]")
        sys.exit(1)
    try:
        f = open(sys.argv[1],"r")
    except IOError as e:
        print("Error" + str(e))
        sys.exit(1)
    if (len(sys.argv) == 3):
        try:
            f1 = open(sys.argv[2],"w")
        except IOError as e:
            print("Error" + str(e))
            sys.exit(2)
    data = f.readlines()
    c = []
    for item in data:
        try:
            a = parse_net(item[0:-1])
            print (a)
            print (a[0])
            print (a[2][2])

            outstring = a[1] + ": " + a[0] + "PORT MAP("
            d = 2
            while d < len(a)-1:
                outstring += str(a[d][0]) + "->" + str(a[d][1]) + ", "
                d += 1
            outstring += str(a[d][0]) + "->" + str(a[d][1])
            outstring += ");"
            if (len(sys.argv) == 3):
                outstring += "\n"
                f1.write(outstring)
            else:
                print(outstring)
        except IOError:
            print("Error input file is not a valid verilog port map!")
            


