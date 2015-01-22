import math
import sys
import re

def main():
    file = "bad_sensors.xml"
    f = open(file)
    outfile = "good.xml"
    fo = open(outfile,'w')
    content = f.read()
    print (content)
    lis = re.findall(r"<[\w]+>[\n\s]*.*[\n\s]*</[\w]+>",content)
    for line in lis:
        line = line.replace("\n","").replace(" ","")
        values = re.findall(r"\+?\-?[0-9]+\.[0-9]+",line)
        values = [float(x) for x in values]
        avg = sum(values)/len(values)
        avg = round(avg,2)
        print (avg)
        print (values)
        fo.write("{}\n".format(line))
    print (lis)




if __name__=="__main__":
    main()