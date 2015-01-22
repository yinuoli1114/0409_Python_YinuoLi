import math
import sys
import re
import string

def main():
    o = is_valid_name("Uaadaa_5.")
    #print (o)
    o = parse_pin_assignment(".CLK$(clk)")
    print (o)
    #o = parse_net("DFFSR present_val_reg (.D(n30), .CLK(clk), .R(n33))")
    #print (o)

    #valid("_Uaa5&UU&&&&")


def valid(id):
    '''
    m = re.match(r"[\w]+$",id)
    if m:
        print (m.group())
    else:
        print ("not match")
    '''
    expr = r"[a-zA-Z0-9_]+"
    match = re.match(r"[a-zA-Z0-9_]+$", id)
    if match:
        print (match.group())
    else:
        print ("not match")



def is_valid_name(identifier):
    #expr = r"[a-zA-Z0-9_]+"
    #match = re.match(r"[a-zA-Z0-9_]+", identifier)
    t = True
    for c in identifier:
        if c in string.ascii_letters or c in string.digits or c == "_":
            t = t and True
        else:
            t = t and False
    return t

def parse_pin_assignment(assignment):
    match = re.match(r"\.(?P<por>[a-zA-Z0-9_]+)\$\((?P<pin>[a-zA-Z0-9_]+)\)$", assignment)
    if match:
        return (match.group(1),match.group(2))
    else:
        print ("not m")
        #raise ValueError(assignment)
def parse(assignment):
    match = re.match(r"\.(?P<por>[a-zA-Z0-9_]+)\((?P<pin>[a-zA-Z0-9_]+)\)$", assignment)
    if match:
        return True
    else:
        raise ValueError(assignment)

def parse_net(line):
    el = line.split("(",1)
    #print (el)
    to = True
    names = el[0].split()
    print (names)

    if len(names) != 2:
        raise ValueError(el[0])


    for name in names:
        #print (name)
        to = to and is_valid_name(name);
    if to == False:
        raise ValueError(el[0])


    #print (el)
    es = el[1][0:len(el[1])-1]
    ps = el[1].split(" )")
    #print (es)
    pn = es.split(",")
    #print (pn)
    t = True
    lis = []
    for pi in pn:
        pi = pi.split()
        #print (pi)
        t = t and parse(pi[0])
        lis.append(parse_pin_assignment(pi[0]))
        #print (lis)
        #print (t)

    if t == True:
        #print (t)
        es = "(("+es + ")"
        lis = tuple(lis)
        return (names[0],names[1],lis)

    #ps = ps[:ps.length-1]
    #print (ps)


if __name__=="__main__":
    main()