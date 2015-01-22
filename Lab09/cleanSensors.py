
import math
import sys
import re
import string
import re


def main():
    createOutputFile()


def createOutputFile():
    file = "bad_sensors.xml"
    outfile = "sensors.xml"
    f = open(file)
    fo = open(outfile,'w')
    content = f.read()
    f.close()
    lis = re.findall(r"<[\w]+>[\n\s]*.*[\n\s]*</[\w]+>",content)
    #print (lis)
    fo.write("<?xml version=\"1.0\"?>\n")
    fo.write("<sensors>\n")
    for line in lis:
        line = line.replace("\n","").replace(" ","")
        #print (line)
        values = re.findall(r"\+?\-?[0-9]+\.[0-9]+",line)
        #print (values)
        v = [float(x) for x in values]
        avg = sum(v) / len(v)
        avg = round(avg,2)
        #print (avg)
        m0 = re.search(r"<([\w]+)>",line)
        if m0:
            id0 = m0.group(1)
            #print (id0)
        m1 = re.search(r"</([\w]+)>",line)
        if m1:
            id1 = m1.group(1)
            #print (id1)
        if id0 == id1:
            fo.write("    <sensor id=\"{}\" average=\"{}\">\n".format(id0,avg))
            for value in values:
                fo.write("        <value>{}</value>\n".format(value))
            fo.write("    </sensor>\n")
    fo.write("</sensors>\n")





if __name__=="__main__":
    main()