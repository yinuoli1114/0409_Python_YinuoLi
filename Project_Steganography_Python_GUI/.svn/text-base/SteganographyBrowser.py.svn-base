
import sys
import math
import re
import glob

from PySide.QtCore import *
from PySide.QtGui import *


import SteganographyGUI
from NewSteganography import *

class SampleWindow(QMainWindow, SteganographyGUI.Ui_MainWindow):


    def __init__(self, parent=None):
        super(SampleWindow, self).__init__(parent)
        self.setupUi(self)
        self.begin()

        #directory = QFileDialog.getExistingDirectory(self,"Please Select a Folder","/Home/ee364e02")
        #print (directory)
        #self.getPictures(directory)
        #self.btnExtract.setEnabled(False)
        #self.btnWipeMedium.setEnabled(False)
        self.grpMedium.setEnabled(False)
        self.grpMessage.setEnabled(False)
        self.btnWipeMedium.clicked.connect(self.boxQuestion)
        self.btnExtract.clicked.connect(lambda: self.extractImage(self.target,self.type))
        #self.fileTreeWidget.itemClicked.connect(self.displayMedium)
    def begin(self):
        directory = QFileDialog.getExistingDirectory(self,"Please Select a Folder","/Home/ee364e02")
        print (directory)
        self.getPictures(directory)
        self.fileTreeWidget.itemClicked.connect(self.displayMedium)


    def displayMedium(self):
        self.grpMedium.setEnabled(True)
        #self.grpMessage.setEnabled(False)
        self.btnWipeMedium.setEnabled(False)
        self.btnExtract.setEnabled(False)
        print ("displayMdium")

        it = self.fileTreeWidget.currentItem()
        self.item = it
        #self.it = it
        file_name = it.text(0)
        self.file_path = self.first_path+"/"+file_name
        print (file_name)
        scene = QGraphicsScene()
        self.viewMedium.setScene(scene)
        pix_map = QPixmap(self.file_path)
        pix_it = QGraphicsPixmapItem(pix_map)
        scene.addItem(pix_it)
        #scene.setSceneRect(0,0,250,250)
        self.viewMedium.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)
        self.viewMedium.show()
        self.txtMessage.setPlainText("")

        sc = QGraphicsScene()
        self.viewMessage.setScene(sc)


        medium = NewSteganography(self.file_path,"horizontal")
        #self.medium = medium
        medium2 = NewSteganography(self.file_path,"vertical")
        #self.medium2 = medium2
        o = medium.checkIfMessageExists()
        o2 = medium2.checkIfMessageExists()
        print ("o"+str(o[0]))
        print ("o2[0]"+str(o2[0]))
        if o[0] == True or o2[0] == True:
            self.btnWipeMedium.setEnabled(True)
            self.btnExtract.setEnabled(True)
            self.grpMessage.setEnabled(True)
            if o[1] == "GrayImage" or o[1] == "ColorImage":
                print ("case1start")

                self.stackMessage.setCurrentWidget(self.pgImage)
                message = medium.extractMessageFromMedium()
                target = "extract.png"
                self.target = target
                self.type = "Image"
                message.saveToTarget(target)
                #self.btnExtract.clicked.connect(lambda: self.extractImage(target))
                self.medium = medium
                #self.btnWipeMedium.clicked.connect(self.boxQuestion)
                print ("case1end")
                #self.btnWipeMedium.clicked.connect(lambda: self.wipe(self.file_path))
            elif o2[1] == "GrayImage" or o2[1] == "ColorImage":
                print ("case2start")
                #self.grpMessage.setEnabled(True)
                self.stackMessage.setCurrentWidget(self.pgImage)
                message2 = medium2.extractMessageFromMedium()
                target = "extract.png"
                self.target = target
                self.type = "Image"
                message2.saveToTarget(target)
                #self.btnExtract.clicked.connect(lambda: self.extractImage(target))
                self.medium = medium2
                #self.btnWipeMedium.clicked.connect(self.boxQuestion)
                print ("case2end")
                #self.btnWipeMedium.clicked.connect(lambda: self.wipe(self.file_path))
            elif o[1] == "Text":
                print ("case3start")
                self.stackMessage.setCurrentWidget(self.pgText)
                message = medium.extractMessageFromMedium()
                target = "extract.txt"
                self.target = target
                self.type = "Text"
                message.saveToTarget(target)
                #self.btnExtract.clicked.connect(lambda: self.extractText(target))
                self.medium = medium
                #self.btnWipeMedium.clicked.connect(self.boxQuestion)
                print ("case3end")
            else:
                print ("case4tart")
                self.stackMessage.setCurrentWidget(self.pgText)
                message2 = medium2.extractMessageFromMedium()
                target = "extract.txt"
                self.target = target
                self.type = "Text"
                message2.saveToTarget(target)
                #self.btnExtract.clicked.connect(lambda: self.extractText(target))
                self.medium = medium2
                #self.btnWipeMedium.clicked.connect(self.boxQuestion)
                print ("case4end")

        else:
            print ("caseNonestart")
            self.btnWipeMedium.setEnabled(False)
            self.btnExtract.setEnabled(False)
            self.grpMessage.setEnabled(False)
            print ("caseNoneend")


            #self.btnExtract.setEnabled(False)
    def boxQuestion(self):
        print ("box1")
        answer = QMessageBox.question(self,"Test","Are you sure?",QMessageBox.Yes, QMessageBox.No)
        print ("box2")
        if answer == QMessageBox.Yes:
            print ("box3")
            self.wipe(self.file_path)
        #else:
        #return


    def wipe(self,path):
        print ("wipe")
        self.medium.wipeMedium()

        self.item.setForeground(0,QBrush(QColor(0,0,255)))
        child = self.item.child(0)
        self.item.removeChild(child)
        self.txtMessage.setPlainText("")
        sc = QGraphicsScene()
        self.viewMessage.setScene(sc)
        self.grpMessage.setEnabled(False)
        self.btnWipeMedium.setEnabled(False)
        self.btnExtract.setEnabled(False)




    '''
    def extractText(self,target):
        f = open(target)
        content = f.read()
        self.txtMessage.setPlainText(content)
    '''

    def extractImage(self,target,type):
        if type == "Image":
            print ("extractImage")
            scene = QGraphicsScene()
            self.viewMessage.setScene(scene)
            pix_map = QPixmap(target)
            pix_it = QGraphicsPixmapItem(pix_map)
            scene.addItem(pix_it)
            #scene.setSceneRect(0,0,250,250)
            self.viewMessage.fitInView(scene.sceneRect(),Qt.KeepAspectRatio)
            #self.viewMessage.fitInView(pix_it)
            self.viewMessage.show()
        elif type == "Text":
            f = open(target)
            content = f.read()
            self.txtMessage.setPlainText(content)
        self.btnExtract.setEnabled(False)

    def getPictures(self,path):
        fileList = glob.glob(path+"/*.png")
        #print (fileList[0])

        for file in fileList:
            #print (file)
            file_name = file.split("/")[-1]
            #print (file_name)
            folder_name = file.split("/")[:-1]
            #print (folder_name)
            #folder_name =
            st = ""
            for s in folder_name:
                st += "/"
                st += s
            st = st.strip("/")
            st = "/"+st
            #print ("llll="+st)



            file_path = st + "/" +file_name
            self.first_path = st
            #print (file_path)
            medium = NewSteganography(file_path,"horizontal")
            o = medium.checkIfMessageExists()
            medium2 = NewSteganography(file_path,"vertical")
            o2 = medium2.checkIfMessageExists()
            #print (o)
            if o[0] == False and o2[0] == False:
                item = QTreeWidgetItem()

                item.setText(0,file_name)

                self.fileTreeWidget.addTopLevelItem(item)
                item.setForeground(0,QBrush(QColor(0,0,255)))

            elif o[0] == True:
                #print (o)
                item = QTreeWidgetItem()

                item.setText(0,file_name)
                self.fileTreeWidget.addTopLevelItem(item)
                item.setForeground(0,QBrush(QColor(255,0,0)))
                child = QTreeWidgetItem()
                child.setText(0,o[1])
                child.setForeground(0,QBrush(QColor(0,255,0)))
                item.addChild(child)
            else:
                item = QTreeWidgetItem()

                item.setText(0,file_name)
                self.fileTreeWidget.addTopLevelItem(item)
                item.setForeground(0,QBrush(QColor(255,0,0)))
                #item.QFont.setBold(True)
                child = QTreeWidgetItem()
                child.setText(0,o2[1])
                child.setForeground(0,QBrush(QColor(0,255,0)))
                item.addChild(child)












currentApp = QApplication(sys.argv)
currentForm = SampleWindow()

currentForm.show()
currentApp.exec_()
