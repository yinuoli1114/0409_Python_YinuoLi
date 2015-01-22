from dataFile import *

def main():
    o = findMultiplesUnder(10)
    print o
    s = 3.14
    l = [0,1,2,3]
    scaleVector(s,l)
    print l
    A = [[7,3,-2],[5,3,0],[8,0,4]]
    idx = 1
    o = getColumnAverage(A,idx)
    print o
    su = [0,-3,2,8,1,4]
    sb = [2,-3]
    o = isSubsetOf(su,sb)
    print o
    x1 = [0,2,1,0]
    x2 = [1,2,3,4]
    o = dotProduct(x1,x2)
    print o
    l = getLongestWord(sentence)
    print l
    l = decodeNumbers(coded)
    print l
    o = getStudentAverage(2)
    print o
    o = getSubjectAverage(1)
    print o

    #print students[0]

def getSubjectAverage(subjectIndex):

        avg = 0
        for i in range(len(students)):
            students[i] = students[i].split(str("|"))
            print students[i][subjectIndex+1]
            avg = avg + float(students[i][subjectIndex+1])
        avg = avg / (i+1)
        return avg


def getStudentAverage(studentIndex):
        stt = students[studentIndex]
        #print students[2]
        stt = stt.split(str("|"))
        print stt
        avg = 0
        for i in range(len(stt)):
            if i > 0:
                avg = avg + float(stt[i])

        avg = avg / i
        return avg



def decodeNumbers(numList):

        strr = ""
        for i in range(len(numList)):
            strr = strr + chr(numList[i])

        return strr


def getLongestWord(sentence):

        str = sentence.split(" ")
        print str
        lenth = 0
        lenmax = 0
        strmax = ""
        for streak in str:
            if lenmax < len(streak):
                lenmax = len(streak)
                strmax = streak
        return  strmax




def dotProduct(x, y):
        sum = 0
        for i in range(len(x)):
            sum = sum + x[i] * y[i]

        return sum



def isSubsetOf(superList, subList):
    uu = 0
    for i in range(len(subList)):
        for j in range(len(superList)):
            if subList[i] == superList[j]:
                uu = uu + 1
    if uu == (i+1):
        return True
    else:
        return False


def getColumnAverage(A, idx):
        sum = 0
        for i in range(len(A)):
            for j in range(len(A[i])):
                if j == idx:
                    sum = sum + A[i][j]
        avg = sum / (i+1)

        return avg





def scaleVector(s, vList):
    if type(s) is not float:
        return None
    if type(vList) is not list:
        return None
    else:
        for i in range(len(vList)):
            vList[i] = "%0.2f" % (vList[i] * s)
        #print vList[1]
        return vList




def findMultiplesUnder(maxValue):
    if maxValue > 0:

        sum = 0
        mul = 3
        n = 1
        while mul < maxValue:
            sum = sum + mul
            n = n + 1
            mul = 3 * n

        mul = 5
        n = 1
        while mul < maxValue:
            sum = sum + mul
            n = n + 1
            mul = 5 * n
        return sum
    else:
        return None













if __name__ == "__main__":
    main()