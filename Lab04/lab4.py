
import re
import sys, getopt
import os.path
import glob

def main():
    filelist = glob.glob(r"E*.txt")
    print (filelist)
    id_dic = {}
    for file in filelist:
        f = open(file)

        for i,line in enumerate(f):
            if i > 1:
                print (line)
                id = line.split()[0]
                print (id)
                score = int(line.split()[1])
                if score >= 90:
                    grade = 'A'
                elif score >= 80:
                    grade = 'B'
                elif score >= 70:
                    grade = 'C'
                elif score >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                print (grade)

                coursename = file.split(".")[0]
                ct = (coursename,grade)
                print (ct)
                if id not in id_dic:
                    lis = [ct]
                    id_dic[id] = lis
                else:
                    id_dic[id].append(ct)
        f.close()
    print (id_dic)
    stu_dic = {}
    f = open("students.txt")
    for i,line in enumerate(f):
        if i > 1:
            print (line)
            name = line.split("|")[0].strip()
            print (name)
            idd = line.split("|")[1].strip()
            print (idd)
            if name not in stu_dic:
                stu_dic[name] = idd
    print (stu_dic)
    for k in stu_dic:
        stu_dic[k] = id_dic[stu_dic[k]]
    print (stu_dic)
    outfile = "report.txt"
    fo = open(outfile,"w")
    for k in stu_dic:
        fo.write("{}\n".format(k))
        for course in stu_dic[k]:
            cname = course[0]
            grade = course[1]
            fo.write("{} {}\n".format(cname,grade))












if __name__ == "__main__":
    main()