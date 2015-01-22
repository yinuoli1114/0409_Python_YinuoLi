#! /usr/bin/env python3.4
import glob

def main():
    na_dic = getRegistration()
    #print (na_dic)
    getRoster(370)
    getStudentInfoByName("Betty T Torres")
    getStudentInfoByID("41724-49926")
    getBestStudent("370")
    getStudentAverage("Betty T Torres")




def getRegistration():
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]

            #id_dic[nk] = id_dic[na_dic[nk]]
    #print (na_dic)
    return na_dic

def getRoster(classNumber):
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]

    nlist = []

    for nk in na_dic:
        for e in na_dic[nk]:
            print (e)
            print (e[0])
            if classNumber == int(e[0]):
                nlist.append(nk)
    nlist = sorted(nlist)
    print (nlist)
    return nlist

def getStudentInfoByName(studentName):
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]
    cg_dic = {}
    for tu in na_dic[studentName]:

        cg_dic[tu[0]] = tu[1]

    print (cg_dic)
    return cg_dic

def getStudentInfoByID(studentID):
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]
    cg_dic = {}
    for tu in id_dic[studentID]:

        cg_dic[tu[0]] = tu[1]

    print (cg_dic)
    return cg_dic
def getStudentGrade(studentName, classNumber):
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]
    for tu in na_dic[studentName]:
        if tu[0] == classNumber:
            g = tu[1]
    return g

def getBestStudent(classNumber):
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]
    maxg = 0

    for nk in na_dic:
        for tu in na_dic[nk]:
            if tu[0] == classNumber:
                if int(maxg) < int(tu[1]):
                    maxg = tu[1]
                    l = []
                    l.append(nk)
                    l.append(maxg)
    print (l)
    return l

def getWorstStudent(classNumber):
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]
    maxg = 400

    for nk in na_dic:
        for tu in na_dic[nk]:
            if tu[0] == classNumber:
                if int(maxg) > int(tu[1]):
                    maxg = tu[1]
                    l = []
                    l.append(nk)
                    l.append(maxg)
    print (l)
    return l
def getStudentAverage(studentName):
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    na_dic = {}
    id_dic = {}
    #gl = []
    #print (f_s)
    for word in f_s:
        fsw.append(word.split(str("/")))
    #print (fsw)

    for word in fsw:
        fn.append(word[-1])
    #print (fn)

    for file in fn:
        #print (file)
        fname = file.split('.')[0]
        #print(fname)
        if file[0] == "s":
            f = open(file)
            for i,line in enumerate(f):
                if i > 1:
                    na = line.split("|")[0]
                    #print (na)
                    id = line.split("|")[-1].strip()
                    #print (id)
                    na_dic[na.strip()] = id
        print (na_dic)
    for file in fn:
        if file[0] == "E":
            print (file)
            fname = file.split(".")[0]
            print (fname)
            cname = fname.split("S")[-1]
            print (cname)
            if file[0] == "E":
                f = open(file)

                for i,line in enumerate(f):
                    if i > 1:
                        id = line.split()[0].strip()
                        g = line.split()[-1].strip()
                        print (id)
                        if id not in id_dic:
                            tu = [cname, g]
                            tu = tuple(tu)
                            print (tu)
                            gl = set()
                            gl.add(tu)
                            print (gl)

                            id_dic[id] = gl
                        else:
                            tu = [cname, g]
                            tu = tuple(tu)
                            #s = set()
                            s = id_dic[id]
                            s.add(tu)
                            id_dic[id] = s
                #print (id_dic)
    for nk in na_dic:
        na_dic[nk] = id_dic[na_dic[nk]]
    sum = 0
    i = 0
    for tu in na_dic[studentName]:
        sum = int(sum) + int(tu[1])
        i = i+1

    avg = sum / i
    print (avg)
    return avg








































if __name__ == "__main__":
    main()