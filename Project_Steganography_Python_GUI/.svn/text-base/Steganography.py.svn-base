import math
import sys
import re
import string
import base64
import os
from PIL import Image
from pprint import pprint as pp

def main():
    '''
    m4 = Message(XmlString="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<message type=\"Text\" size=\"52\" encrypted=\"False\">\nVG9kYXkgaXMgdGhlIGJlZ2lubmluZyBvZiBhIG5ldyB3ZWVrLg==\n</message>")
    #m1 = Message(filePath="lab11/a.txt",messageType="Text")
    m3 = Message(XmlString="<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<message type=\"GrayImage\" size=\"4,4\" encrypted=\"False\">\nBwwBDgINCAsQAwoFCQYPBA==\n</message>\"")
    m3.saveToImage("test.png")
    m4.saveToTextFile("test.txt")
    m5 = Message(filePath = "test.txt", messageType="Text")
    #m5.getXmlString()
    s1 = Steganography("dog.png","horizontal")
    s1.embedMessageInMedium(m5,"i2.png")
    s1.extractMessageFromMedium()
    message = s1.extractMessageFromMedium()
    #print (message.XmlString)

    m7 = Message(filePath="test1.png",messageType="GrayImage")
    st = m7.getXmlString()
    '''
    #message = Message(filePath=)
    '''
    message0 = Message(filePath="files/small.txt",messageType="Text")
    print (message0.XmlString)
    medium0 = Steganography("files/mona.png")
    medium0.embedMessageInMedium(message0,targetImagePath="my_mona_small_h.png")
    message0.checkEqual(expectedPath="files/mona_small_h.png",myPath="my_mona_small_h.png",d="horizontal")
    '''

    #message1 = Message(filePath="test.png",messageType="GrayImage")
    #message1.getXmlString()

    #message2 = Message(filePath="lion.png",messageType="ColorImage")
    #message2.getXmlString()
    medium3 = Steganography("files/nature_sunflower_h.png")
    message3 = medium3.extractMessageFromMedium()
    message3.saveToTarget("my_sunflower.png")
    message3.checkEqual(expectedPath="files/dog.png",myPath="my_dog.png",d="horizontal")
    #print (message3.XmlString)
    '''
    message = Message(filePath="files/full.txt", messageType="Text")
    medium = Steganography("files/lena.png")
    medium.embedMessageInMedium(message, "aa1.png")
    mm = medium.extractMessageFromMedium()
    #print (mm.XmlString)
    mm.saveToTextFile("aa1.txt")
    '''
    #mm.checkEqual()


    #m6 = Message(filePath = "mmm", messageType="Test")

class Steganography:
    def __init__(self, imagePath, direction='horizontal'):
        if os.path.exists(imagePath) == False:
            raise ValueError("this file does not exist")
        self.imagePath = imagePath
        self.direction = direction
        self.img = Image.open(imagePath)
        '''
        if len(self.img.shape) == 3:
            raise TypeError("medium can not be ColorImage")
        '''


        self.w,self.h = Image.open(imagePath).size
        #print (self.w,self.h)
        self.size = int(self.w)*int(self.h)
        im = Image.open(imagePath).convert("RGB")
        we,he = im.size
        for w in range(we):
            for h in range(he):
                r,g,b = im.getpixel((w,h))
                if r != g != b:
                    raise TypeError("can not be ColorImage")

        #print (self.size)
    def embedMessageInMedium(self, message, targetImagePath):
        self.targetImagePath = targetImagePath
        m_size = message.getMessageSize()
        if m_size > self.size:
            raise ValueError("size of the given message is larger than what this medium can hold")
        pix = self.img.load()
        new_img = Image.new('L',(self.w,self.h))
        new_pix = new_img.load()
        #print (pix)
        pix_lis = []
        if self.direction == "horizontal":
            for h in range(self.h):
                for w in range(self.w):
                    pix_lis.append(pix[w,h])
        if self.direction == "vertical":
            for w in range(self.w):
                for h in range(self.h):
                    pix_lis.append(pix[w,h])

        #print ("pix="+str(pix_lis[0:20]))
        xml = message.XmlString
        #print (xml[0:10],xml[2])
        askLis = []
        for letter in xml:
            askLis.append(ord(letter))
        #print (askLis)
        askLis = [bin(e)[2:].rjust(8,"0") for e in askLis]
        #print (askLis)
        #print (type(askLis[0]))
        i = 0
        il = 0

        while(i < 8*len(askLis)):
            for k in range(0,8):
                stri = askLis[il]
                #print (stri[k])
                if stri[k] == "0":
                    if pix_lis[i]%2 != 0:
                        pix_lis[i] = pix_lis[i]-1
                else:
                    if pix_lis[i]%2 == 0:
                        pix_lis[i] = pix_lis[i]+1
                i = i+1
            il = il+1
        i = 0
        #print("nix="+str(pix_lis[0:20]))
        if self.direction == "horizontal":
            for h in range(self.h):
                for w in range(self.w):
                    new_pix[w,h] = pix_lis[i]
                    i = i+1
        if self.direction == "vertical":
            for w in range(self.w):
                for h in range(self.h):
                    new_pix[w,h] = pix_lis[i]
                    i = i+1
        new_img.save(targetImagePath)
    def extractMessageFromMedium(self):
        img = Image.open(self.imagePath)
        pix = img.load()
        [self.ew,self.eh] = img.size
        pix_lis = []
        if self.direction == "horizontal":
            for h in range(self.eh):
                for w in range(self.ew):
                    pix_lis.append(pix[w,h])
        if self.direction == "vertical":
            for w in range(self.ew):
                for h in range(self.eh):
                    pix_lis.append(pix[w,h])
        #print (pix_lis[0:20])
        askLis = []
        #for num in pix_lis:
        i = 0

        while(i+8 < len(pix_lis)):
            stri = ""
            for k in range(0,8):
                if pix_lis[i]%2 == 0:
                    stri += "0"
                else:
                    stri += "1"
                i = i+1
            #print (stri)
            askLis.append(stri)

        '''
        ia = 2
        askLis = [2,2,2]
        while(askLis[ia-2] != "e" and askLis[ia-1] != ">"):
            stri = ""
            for k in range(0,8):
                if pix_lis[i]%2 == 0:
                    stri += "0"
                else:
                    stri += "1"
                i = i+1
            #print (stri)
            ia = ia+1
            askLis.append(stri)
        '''
        #print (askLis)
        mes = ""
        ia = 0
        sp = ""
        while(ia+2 < len(askLis) and sp != "age>"):
            a = chr((int(askLis[ia],2)))
            mes += a
            ia = ia+1
            if len(mes) > 10:
                sp = mes[-4:]
        '''
        for stri in askLis:
            a = chr((int(stri,2)))
            mes += a
        '''
        #a = chr(int(askLis[0],2))

        #print (mes)
        '''
        with open('TestByAlex.txt', 'w') as xml:
            xml.write(mes)
        '''
        fo = open("yinuo.xml",'w')
        fo.write(mes)
        ma = re.search(r"</message>",mes)
        #if ma:
            #print (ma.group())

        #m = re.search(r"<\?xml[\\\/\+\w\n\<\?\=\"\-\>\.\s]*</message>",mes)
        m = re.search(r"<\?.*e>",mes)
        #print (m)
        if mes[0] != "<":
            mes = None


        '''
        if m:
            message = m.group()
            print (message)
        else:
            message = None
            print ("not find")

        if message == None:
            return None
        else:
            return Message(XmlString=message)
        '''
        if mes == None:
            return None
        else:
            return Message(XmlString=mes)





class Message:
    def __init__(self, **kwargs):

        #to initialize everything
        self.filePath = ""
        self.messageType = ""
        self.XmlString = ""
        #if the length of kwargs is 2, it is the first case
        if len(kwargs) == 2:
            if "filePath" not in kwargs:
                raise ValueError("Missing argument of filePath")
            elif kwargs["filePath"] == "":
                raise ValueError("filePath can not be Null")
            elif "messageType" not in kwargs:
                raise ValueError("Missing argument of messageType")
            elif kwargs["messageType"] not in ["Text","GrayImage","ColorImage"]:
                raise ValueError("messageType is wrong")
            else:
                self.filePath = kwargs["filePath"]
                self.messageType = kwargs["messageType"]
                self.getXmlString()
                #print (self.XmlString)
        #if the length of kwargs is 1, it is the second case
        elif len(kwargs) == 1:
            if "XmlString" not in kwargs:
                raise ValueError("Missing argument of XmlString")
            elif kwargs["XmlString"] == "":
                raise ValueError("XmlString is Null")
            else:
                self.XmlString = kwargs["XmlString"]

        else:
            raise ValueError("argument number is wrong")


    def getMessageSize(self):
        #raise Exception if no data in XmlString, else return the length of XmlString
        if self.XmlString == "":
            raise Exception("No data in XmlString")
        else:
            return len(self.XmlString)
    def saveToImage(self, targetImagePath):
        #raise Exception if no data in XmlString
        if self.XmlString == "":
            raise Exception("no data in XmlString")

        #get the messageType
        m = re.search(r"message type=\"(.*)\"\s*size=",self.XmlString)
        if m:
            self.messageType = m.group(1)
        #print ("save"+self.messageType)
        #raise TypeError if messageType is not GrayImage or ColorImage
        if self.messageType != "GrayImage" and self.messageType != "ColorImage":
            raise TypeError("messageType is not Image")
        #get the size
        m = re.search(r"size=\"(.*)\"\s*encrypted=",self.XmlString)
        if m:
            self.size = m.group(1)
        #print (self.size)
        self.width = int(self.size.split(",")[0])
        #print (self.width)
        #print (type(self.row))
        self.height = int(self.size.split(",")[1])
        #print (self.col)
        #print (type(self.col))
        m = re.search(r"encrypted=(.*)>\n(.*)\n",self.XmlString)
        if m:
            self.codeStr = m.group(2)
        #print (self.codeStr)
        #n = list(base64.b64decode(self.codeStr))
        #print (n)
        numberLis = list(base64.b64decode(self.codeStr))
        numberLis = [ord(e) for e in numberLis]
        #print ("numL="+str(numberLis))



        if self.messageType == "ColorImage":
            #print ("l="+str(len(numberLis)))
            chunk = len(numberLis) / 3
            #print (chunk)
            tulis = []
            for i in range(chunk):
                tulis.append((numberLis[i],numberLis[i+chunk],numberLis[i+2*chunk]))
            #print (tulis)
            img2 = Image.new('RGB',(self.width,self.height))
        #elif self.messageType == "ColorImage":
            #img = Image.new('L',(self.row,self.col))
            pix2 = img2.load()
            i = 0
            for h in range(img2.size[1]):
                for w in range(img2.size[0]):
                    pix2[w,h] = tulis[i]
                    i = i+1
        #print (pix)
            img2.save(targetImagePath)


        if self.messageType == "GrayImage":
            img2 = Image.new('L',(self.width,self.height))
        #elif self.messageType == "ColorImage":
            #img = Image.new('L',(self.row,self.col))
            pix2 = img2.load()
            i = 0
            for h in range(img2.size[1]):
                for w in range(img2.size[0]):
                    pix2[w,h] = numberLis[i]
                    i = i+1
        #print (pix)
            img2.save(targetImagePath)
    def saveToTextFile(self, targetTextFilePath):
        if self.XmlString == "":
            raise Exception("no data in XmlString")
        #if self.messageType != "Text":
            #raise TypeError("messageType is not Text")
        m = re.search(r"message type=\"(.*)\"\s*size=",self.XmlString)
        if m:
            self.messageType = m.group(1)
        if self.messageType != "Text":
            raise TypeError("messageType is not Text")
        #print (self.messageType)
        m = re.search(r"size=\"(.*)\"\s*encrypted=",self.XmlString)
        if m:
            self.size = m.group(1)
        #print (self.size)
        m = re.search(r"encrypted=(.*)>\n(.*)\n",self.XmlString)
        if m:
            self.codeStr = m.group(2)
        #print (self.codeStr)
        letterStr = base64.b64decode(self.codeStr)
        f = open(targetTextFilePath,'w')
        f.write(str(letterStr))
    def saveToTarget(self, targetPath):
        m = re.search(r"message type=\"(.*)\"\s*size=",self.XmlString)
        if m:
            self.messageType = m.group(1)
        #print (self.messageType)
        if self.messageType == "GrayImage" or self.messageType == "ColorImage":
            self.saveToImage(targetPath)
        if self.messageType == "Text":
            self.saveToTextFile(targetPath)
    def getXmlString(self):
        if self.filePath == "":
            raise Exception("no data in XmlString")
        if self.messageType == "Text":
            f = open(self.filePath)
            content = f.read()
            #print (content)
            xml = base64.b64encode(content)
            self.code = xml
            #xml += "TG9yZ=="
            size = len(content)


            self.XmlString = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<message type=\""+self.messageType+"\" size=\""+str(size)+"\" encrypted=\"False\">\n"+xml+"\n</message>"



        if self.messageType == "GrayImage":
            img = Image.open(self.filePath)
            width,height = img.size
            pix = img.load()
            pix_lis = []
            for h in range(height):
                for w in range(width):
                    pix_lis.append(pix[w,h])
            #print (pix_lis)

            pix_byte = bytearray(pix_lis)
            #print (pix_byte)

            xml = base64.b64encode(str(pix_byte))
            self.code = xml
            #print (xml)
            size = str(width)+","+str(height)
            #print (size)
            self.XmlString = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<message type=\""+self.messageType+"\" size=\""+str(size)+"\" encrypted=\"False\">\n"+xml+"\n</message>"

            #print (self.XmlString)
        if self.messageType == "ColorImage":
            img = Image.open(self.filePath)
            width,height = img.size
            pix = img.getdata()
            all_lis = list(pix)
            #print (all_lis[0:5])
            pix_lis = []
            for tu in all_lis:
                pix_lis.append(tu[0])
            for tu in all_lis:
                pix_lis.append(tu[1])
            for tu in all_lis:
                pix_lis.append(tu[2])
            #print (pix_lis[0:20])
            pix_byte = bytearray(pix_lis)
            #print (pix_byte)

            xml = base64.b64encode(str(pix_byte))
            size = str(width)+","+str(height)
            #print (size)
            self.XmlString = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<message type=\""+self.messageType+"\" size=\""+str(size)+"\" encrypted=\"False\">\n"+xml+"\n</message>"



        return self.XmlString

    def checkEqual(self,expectedPath,myPath,d):
        igiven = Image.open(expectedPath)
        pgiven = igiven.load()
        wi,hi = igiven.size
        pix_given =[]
        inew = Image.open(myPath)
        pnew = inew.load()
        #win,hin = inew.size
        pix_new=[]
        io = Image.open("files/mona.png")
        po = io.load()
        #wio,hio = io.size
        pix_o =[]
        if d == "vertical":
            for w in range(wi):
                for h in range(hi):
                    pix_given.append(pgiven[w,h])
            print (pix_given[20:60])

            for w in range(wi):
                for h in range(hi):
                    pix_new.append(pnew[w,h])
            print (pix_new[20:60])

            '''
            for w in range(wi):
                for h in range(hi):
                    pix_o.append(po[w,h])
            print (pix_o[0:20])
            '''
        if d == "horizontal":
            for h in range(hi):
                for w in range(wi):
                    pix_given.append(pgiven[w,h])
            print ("expec"+str(pix_given[9000:9020]))

            for h in range(hi):
                for w in range(wi):
                    pix_new.append(pnew[w,h])
            print ("mypix"+str(pix_new[9000:9020]))

            '''
            for h in range(hi):
                for w in range(wi):
                    pix_o.append(po[w,h])
            print ("orign"+str(pix_o[9000:9020]))
            '''
        #print (len(pix_given))
        #print (len(pix_new))
        '''
        for i in range(len(pix_given)):
            if pix_given[i] == pix_new[i]:
                print (i),
                #print (i)
        '''















if __name__=="__main__":
    main()