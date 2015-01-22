#! /usr/local/bin/python3
#
#$Author: ee364e07 $
#$Date: 2014-11-04 17:29:08 -0500 (Tue, 04 Nov 2014) $
#$Revision: 70411 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F14/students/ee364e07/Lab08/vtools.py $
#$Id: vtools.py 70411 2014-11-04 22:29:08Z ee364e07 $

import string
def is_valid_name(identifier):
    for item in identifier:
        if item not in string.ascii_letters and item not in string.digits and item != "_":
            return False
    return True
def parse_pin_assignment(assignment):
    flag = 1
    assignment = assignment.replace(" ","")
    print("llllllll"+assignment)
    assignment = assignment.split("(")
    print("kkkkkkkk"+str(assignment))
    print(assignment[0][0])
    print(type(assignment))
    print(type(assignment[0]))
    if assignment[0][0] != ".":
        flag = 0
    print(assignment)
    flag = is_valid_name(assignment[0][1:]) and flag
    
    flag = is_valid_name(assignment[1][0:-1]) and flag
    if assignment[1][-1] != ")":
        flag = 0
    if(flag == 0):
        raise ValueError("The statement is not valid")
    tup1 = (assignment[0][1:], assignment[1][0:-1])
    return tup1
def parse_net(line):
    flag = 1
    A = []
    j = 0
    while line[j] == " ":
        j+=1
    line = line[j:]
    
    line = line.split("(")
    #print(line)
    line[0] = line[0].split(" ")
    line2 = ""
    i = 1
    while i < len(line):
        line2 += str(line[i]) + "("
        i+=1
    line[1]= line2
    #print(line[1])
    line[1] = line[1].replace(" ","")
    line[1] = line[1].split(",")
    k = 0
    b = []
    while k < len(line[0]):
        if line[0][k] != "":
            #print(line[0][k])
            b.append(line[0][k])
        k+=1
    line[0] = b
    #print(b)
    #print(line[0])
    #print (flag)
    #print(line[0])
    if len(line[0]) != 2:
        flag = 0 
    for item in line[0]:
        try:
            is_valid_name(item)
            A.append(item)
        except ValueError:
            flag = 0
    length = len(line[1])
    if line[1][length-1][-2] != ")":
        flag = 0
    line[1][length-1] = line[1][length-1][0:-2]
    for item in line[1]:
        try:
            b = parse_pin_assignment(item)
            A.append(b)
        except ValueError:
            flag = 0
    if(flag == 0):
        raise ValueError("The line is not valid")
    A = tuple(A)
    return A
if __name__ == "__main__":
    a = is_valid_name("HI_this_is90")
    print(a)
    b = parse_pin_assignment(".D(n30)")
    print(b)
    #c = parse_net("DFFSR present_val_reg  ( .D(n30), .CLK(clk), .R(n33), .S(1), .Q(stop_bit) )")
    #print(c)
