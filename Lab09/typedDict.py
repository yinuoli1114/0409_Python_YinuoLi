
import math
import sys
import re
import string
import re


def main():
    d0 = Entry(42,"Answer to Life, the Universe, and Everything")
    print (d0)
    l0 = Lookup("l0Entry")
    print (l0)
    d1 = Entry(39, "bblllllaaa")
    d2 = Entry(39, "bbl333rrrrrrrrrllllaaa")
    d3 = Entry(38, "rrrrrrrrrraa")
    l0.addEntry(d1)
    l0.addEntry(d0)
    #l0.addEntry(d2)
    l0.updateEntry(d2)
    #l0.updateEntry(d3)
    print (l0)
    l0.saveToFile("fout.txt")
    k = l0.getKeys()
    print (k)
    v = l0.getValues()
    print (v)



class Entry:
    def __init__(self, k=0, v=''):
        if type(k) != int:
            raise TypeError("input key is not an integer")
        if type(v) != str:
            raise TypeError("input value is not an string")
        self.key = k
        self.value = v

        '''
        if len(names) != 2:
            raise ValueError(el[0])
        '''
    def __str__(self):
        stri = "({}: \"{}\")".format(self.key,self.value)
        return stri
    def __hash__(self):
        t = (self.key, self.value)
        return hash(t)

class Lookup:
    def __init__(self, name):
        if name == "":
            raise ValueError(name)
        self._name = name
        self._entrySet = set()
    def __str__(self):
        n = len(self._entrySet)
        stri = "[\"{}\": {} Entries]".format(self._name, n)
        return stri
    def addEntry(self, entry):
        for e in self._entrySet:
            if e.key == entry.key:
                raise ValueError("there exists an entry with the same key in the backing store")
        self._entrySet.add(entry)
    def updateEntry(self, entry):
        exist = 0
        for e in self._entrySet:
            if e.key == entry.key:
                exist += 1
                e.value = entry.value
        if exist == 0:
            raise KeyError("entry with the same key does not exist")
    def addOrUpdateEntry(self, entry):
        exist = 0
        for e in self._entrySet:
            if e.key == entry.key:
                self.updateEntry(entry)
                exist += 1
        if exist == 0:
            self.addEntry(entry)
    def removeEntry(self, entry):
        i = -1
        geti = -1
        for e in self._entrySet:
            i += 1
            if e.key == entry.key:
                geti = i
        self._entrySet.remove(geti)
    def addOrUpdateFromDictionary(self, someDict):
        for key in someDict:
            entry = Entry(key, someDict[key])
            self.addOrUpdateEntry(entry)
    def getAsDictionary(self):
        dic = {}
        for entry in self._entrySet:
            dic[entry.key] = entry.value
        return dic
    def getKeys(self):
        lk = []
        for entry in self._entrySet:
            lk.append(entry.key)
        lk = sorted(lk)
        return lk
    def getValues(self):
        lv = []
        for entry in self._entrySet:
            lv.append(entry.value)
        lv = sorted(lv)
        return lv
    def getElementCount(self):
        n = len(self._entrySet)
        return n
    def saveToFile(self, fileName):
        fo = open(fileName,'w')
        fo.write("\"{}\"\n\n".format(self._name))
        dic = self.getAsDictionary()
        for k in dic:
            fo.write("({}: \"{}\")\n".format(k,dic[k]))



















if __name__=="__main__":
    main()