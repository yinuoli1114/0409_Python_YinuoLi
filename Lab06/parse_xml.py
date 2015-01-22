
import re
import sys, getopt
import os.path

def main():
    convertToAttrib()
    getGenres()
    a = getAuthorOf("MSXML3: A Comprehensive Guide")
    print (a)
    a = getBookInfo("bk112")
    print (a)
    a = getBooksBy("Corets, Eva")
    print (a)
    a= getBooksBelow(7.88)
    print (a)


def getBooksBelow(bookPrice):
    file = "books.xml"
    f = open(file)
    lis = f.read()
    na_dic = {}
    pa = re.findall(r"<price>([\w\s\.]*)</price>",lis)
    print (pa)
    ba = re.findall(r"<title>([\w\'\s\,\.\:]*)</title>",lis)
    print (ba)
    l = []
    for i in range(len(ba)):
        if float(pa[i])< bookPrice:
            l.append(ba[i])
    #print (l)
    return (l)






def getBooksBy(authorName):
    file = "books.xml"
    f = open(file)
    lis = f.read()
    na_dic = {}
    ba = re.findall(r"<title>([\w\'\s\,\.\:]*)</title>",lis)
    #print (ba)
    print (len(ba))
    aa = re.findall(r"<author>([\w\,\s\.\']*)</author>",lis)
    print (len(aa))

    for i in range(len(ba)):
        if ba[i] not in na_dic.values():
            if aa[i] not in na_dic:
                l = []
                l.append(ba[i])
                na_dic[aa[i]] = l
            else:
                na_dic[aa[i]].append(ba[i])

    #print (na_dic)
    return (na_dic[authorName])


def getBookInfo(bookID):
    file = "books.xml"
    f = open(file)
    lis = f.read()
    id_dic = {}
    ida = re.findall(r"<book id=\"([\w]*)\">",lis)
    #print (ida)
    #print (len(ba))
    ba = re.findall(r"<title>([\w\'\s\,\.\:]*)</title>",lis)
    #print (ba)
    #print (len(ba))
    aa = re.findall(r"<author>([\w\,\s\.\']*)</author>",lis)
    #print (aa)
    #print (len(aa))

    for i in range(len(ida)):
        l = []
        l.append(ba[i])
        l.append(aa[i])
        id_dic[ida[i]] = l
        l = tuple(l)
    #print (id_dic)
    return (id_dic[bookID])




def convertToAttrib():
    defp = r"def( )*(?P<fname>[a-zA-Z]{1}[\w\-\_]*)\((?P<argm>[\w\s\=\-\_\,]*)\)\:"
    file = "points.xml"
    f = open(file)
    lis = f.read()
    #print (lis)
    #all = re.findall(r"-?[0-9]+",str)
    ida = re.findall(r"<ID>([\w]*)</ID>",lis)
    #print (ida)
    xa = re.findall(r"<X>([\+\-\w\.]*)</X>",lis)
    #print (xa)
    ya = re.findall(r"<Y>([\+\-\w\.]*)</Y>",lis)
    #print (ya)
    outfile = "points_out.xml"
    fo = open(outfile,'w')
    fo.write("<?xml version=\"1.0\"?>\n")
    fo.write("<coordinates>\n")
    for e in range(len(ida)):
        fo.write("   <point ID=\""+ida[e]+"\" X=\""+xa[e]+"\" Y=\""+ya[e]+"\" />\n")
    fo.write("</coordinates>\n")

def getGenres():
    file = "books.xml"
    f = open(file)
    lis = f.read()
    ga = re.findall(r"<genre>([\w]*)</genre>",lis)
    ga = sorted(ga)
    gas = set()
    for e in range(len(ga)):
        gas.add(ga[e])
    gas = sorted(gas)
    #print (gas)
    return (gas)

def getAuthorOf(bookName):
    file = "books.xml"
    f = open(file)
    lis = f.read()
    na_dic = {}
    ba = re.findall(r"<title>([\w\'\s\,\.\:]*)</title>",lis)
    #print (ba)
    #print (len(ba))
    aa = re.findall(r"<author>([\w\,\s\.\']*)</author>",lis)
    #print (aa)
    #print (len(aa))
    for i in range(len(ba)):
        if ba[i] not in na_dic:
            na_dic[ba[i]] = aa[i]
    #print (na_dic)
    return (na_dic[bookName])








if __name__=="__main__":
    main()