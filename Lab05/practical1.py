import glob

def main():
    o = getListProduct([])
    #print (o)
    o = partition([1,2,3,4,5,6],4)
    #print (o)
    o = getLargestPartition([2,1,4,3],2)
    print (o)
    getLargestProduct()
    o = getDirectory()
    print (o)
    o = getPhoneByPartialName("Lee")
    print (o)
    o = reverseLookup("843")
    print (o)

def getListProduct(numList):
    if numList == []:
        return 0
    else:
        prod = 1
        for e in numList:
            prod = prod * e
        print (prod)
        return prod

def partition(numList, n):
    p = []
    for a in range(len(numList)):
        #print (a)
        s = []

        s = numList[a:a+n]
        #print (s)
        if a+n-1 < len(numList):
            p.append(s)
            #print (p)
    return p

def getLargestPartition(numList, n):
    maxprod = 1
    maxlist = []
    numList = partition(numList, n)
    #print (numList)
    for list in numList:
        prod = 1
        for e in list:
            e = int(e)
            prod = prod * e
        if prod > maxprod:
            maxprod = prod
            maxlist = list
    #print (maxprod)
    tu = (maxlist, maxprod)
    tu = tuple(tu)
    #print (tu)
    return tu

def getLargestProduct():
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    maxlist = []
    maxprod = 1
    for word in f_s:
        fsw.append(word.split(str("/")))
    for word in fsw:
        fn.append(word[-1])
    for file in fn:
        print (file)
        if file[0]=="N":
            f = open(file)
            for i,line in enumerate(f):
                list = []
                list = line.split()
                    #list.append(word)
                #print (list)
                for i in list:
                    i = int(i)
                #print "kkkkkkkkkkkkkkk"
                #print (list)
                tu = getLargestPartition(list, 4)
                #print "lllllllllllllll"
                #print (tu)
                #print (prod)

    return tu

def getDirectory():
    f_s = glob.glob('./*')
    fsw = []
    fn = []
    name_dic = {}

    for word in f_s:
        fsw.append(word.split(str("/")))
    for word in fsw:
        fn.append(word[-1])
    for file in fn:
        #print (file)
        if file[0]=="P":
            f = open(file)
            for i,line in enumerate(f):
                list = []
                fnamef = line.split()[0].strip()
                list.append(fnamef)
                fnamem = line.split()[1].strip()
                list.append(fnamem)
                fnamel = line.split()[2].strip()
                list.append(fnamel)
                print (list)
                num = line.split('   ')[-1].strip()
                print (num)
                tu = tuple(list)
                if tu not in name_dic:
                    name_dic[tu] = num
            print (name_dic)
    return name_dic

def getPhoneByPartialName(partialName):
    name_dic = getDirectory()
    pl = []
    for fullname in name_dic:
        for e in fullname:
            if partialName==e:
                pl.append(name_dic[fullname])
    return pl

def reverseLookup(areaCode):
    name_dic = getDirectory()
    nl = []
    b = "("+areaCode+")"
    print (b)
    for fullname in name_dic:
        a = name_dic[fullname].split()[0]
        if a==b:
            c = " ".join(fullname)
            nl.append(c)
    print ("lllllllllllllll")
    print (nl)
    return nl













if __name__=="__main__":
    main()