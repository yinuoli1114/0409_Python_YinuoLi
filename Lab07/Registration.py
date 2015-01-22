import math
import sys

def main():
    c1 = Course("ECE337",30,60,90)
    print (c1)
    letter1 = c1.getLetterGrade(99)
    print (c1.letter)

    #loadData("students.txt")




class Course:
    def __init__(self, courseID, fst, snd, final):
        self.courseID = courseID
        self.fst = fst
        self.snd = snd
        self.final = final
        self.total = 0.25*self.fst + 0.25*self.snd + 0.5*self.final
        if self.total >= 90:
            self.letter = 'A'
        elif self.total >= 80:
            self.letter = 'B'
        elif self.total >= 70:
            self.letter = 'C'
        elif self.total >= 60:
            self.letter = 'D'
        else:
            self.letter = 'F'


    def __str__(self):
        stri = "{}: ({},{},{}) = ({},{})".format(self.courseID,self.fst,self.snd,self.final,self.total,self.letter)
        return stri
    def getLetterGrade(self, totalGrade):
        if totalGrade >= 90:
            self.letter = 'A'
        elif totalGrade >= 80:
            self.letter = 'B'
        elif totalGrade >= 70:
            self.letter = 'C'
        elif totalGrade >= 60:
            self.letter = 'D'
        else:
            self.letter = 'F'
        return self.letter

class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}
    def addCourse(self, course):
        if course.courseID not in self.courses:
            self.courses[course.courseID] = course
    def __str__(self):
        #courses = self.courses.sort()
        lis = []
        for key in self.courses:
            #e = [key, self.courses[key]]
            lis.append(key)
        lis = sorted(lis)
        tl = []
        for id in lis:
            e = [id,self.courses[id].letter]
        os = ""
        os += "{}\n".format(self.name)
        for id in tl:
            os += "{}: {}\n".format(id[0], id[1])
        return os
    def generateTranscript(self):
        lis = []
        for key in self.courses:
            #e = [key, self.courses[key]]
            lis.append(key)
        lis = sorted(lis)
        tl = []
        for id in lis:
            e = [id,self.courses[id].fst,self.courses[id].snd,self.courses[id].final,self.courses[id].total,self.courses[id].letter]
            tl.append(e)
        os = ""
        os += "{}\n".format(self.name)
        for id in tl:
            os += "{}: ({},{},{}) = ({},{})\n".format(id[0],id[1],id[2],id[3],id[4],id[5])
        return os

class School:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def __str__(self):
        lis = []
        for key in self.studnets:
            lis.append(key)
        lis = sorted(lis)
        num = len(lis)
        os = ""
        os += "{}: {} Students\n".format(self.name,num)
        for name in lis:
            os += "{}\n".format(name)
        return os

    def loadData(self,filename):
        f = open(filename)
        lis = f.read()
        print (lis)
        lis = lis.split("\n\n")
        print (lis)
        for es in lis:
            e = es.split("\n")
            for i in range(len(e)):
                if e[i] != "\n" or e[i] != "":
                #print (i)
                    if i==0:
                        print (e[i])
                        stu = Student(e[0])
                    elif i>1:

                        cr = e[i].split(":")
                        print (cr)
                        if len(cr) > 2:
                            cname = cr[0].strip()
                            sc = cr[1].split(",")

                            #print (sc)

                            #print (cname)
                            course = Course(cname,float(sc[0].strip()),float(sc[1].lstrip()),float(sc[2].strip()))
                            print (course)













if __name__=="__main__":
    main()