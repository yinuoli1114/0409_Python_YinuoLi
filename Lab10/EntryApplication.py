
import sys
import math
import re

from PySide.QtCore import *
from PySide.QtGui import *


import EntryForm

class SampleWindow(QMainWindow, EntryForm.Ui_MainWindow):


    def __init__(self, parent=None):
        super(SampleWindow, self).__init__(parent)
        self.setupUi(self)

        self.pbSave.setEnabled(False)
        #self.label_Error.clear()

        self.pbClear.clicked.connect(self.clear)

        self.lFirst.textEdited.connect(self.beginEditing)
        self.lLast.textEdited.connect(self.beginEditing)
        self.lAddress.textEdited.connect(self.beginEditing)
        self.lCity.textEdited.connect(self.beginEditing)
        self.lState.textEdited.connect(self.beginEditing)
        self.lZIP.textEdited.connect(self.beginEditing)
        self.lEmail.textEdited.connect(self.beginEditing)

        self.pbSave.clicked.connect(self.checkError)
        self.pbLoad.clicked.connect(self.loadFile)






    def checkError(self):
        if self.lFirst.text() == "":
            self.label_Error.setText("Error: First Name can not be empty")
            return
        if self.lLast.text() == "":
            self.label_Error.setText("Error: Last Name can not be empty")
            return
        if self.lAddress.text() == "":
            self.label_Error.setText("Error: Address can not be empty")
            return
        if self.lCity.text() == "":
            self.label_Error.setText("Error: City can not be empty")
            return
        if self.lState.text() == "":
            self.label_Error.setText("Error: State can not be empty")
            return
        if self.lZIP.text() == "":
            self.label_Error.setText("Error: ZIP can not be empty")
            return
        if self.lEmail.text() == "":
            self.label_Error.setText("Error: Email can not be empty")
            return
        state = self.lState.text()
        if state not in ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO"]:
            self.label_Error.setText("Error: State must be one of the US states")
            return


        zip = self.lZIP.text()
        m = re.match(r"[0-9]{5}",zip)
        if not m:
            self.label_Error.setText("Error: ZIP code must be a 5-digit number")
            return
        email = self.lEmail.text()
        m = re.match(r"([\w.-]+)@([\w.-]+)",email)
        if not m:
            self.label_Error.setText("Error: Email must have a valid email format")
            return

        #self.label_Error.setText("Error")
        outfileName = QFileDialog.getSaveFileName(self,"Save File","../untitled.xml","XML (*.xml)")
        of = open(outfileName[0],'w')
        of.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        of.write("<User>\n")
        of.write("    <FirstName>"+self.lFirst.text()+"</FirstName>\n")
        of.write("    <LastName>"+self.lLast.text()+"</LastName>\n")
        of.write("    <Address>"+self.lAddress.text()+"</Address>\n")
        of.write("    <City>"+self.lCity.text()+"</City>\n")
        of.write("    <State>"+self.lState.text()+"</State>\n")
        of.write("    <ZIP>"+self.lZIP.text()+"</ZIP>\n")
        of.write("    <Email>"+self.lEmail.text()+"</Email>\n")
        of.write("</user>\n")
        of.close()

    def loadFile(self):
        infileName = QFileDialog.getOpenFileName(self,"Load File","../","XML (*.xml)")
        f = open(infileName[0],'r')
        content = f.read()
        dt = re.findall(r">(.*)<",content)
        self.lFirst.setText(dt[0])
        self.lLast.setText(dt[1])
        self.lAddress.setText(dt[2])
        self.lCity.setText(dt[3])
        self.lState.setText(dt[4])
        self.lZIP.setText(dt[5])
        self.lEmail.setText(dt[6])
        f.close()






    def clear(self):
        self.lFirst.setText("")
        self.lLast.setText("")
        self.lAddress.setText("")
        self.lCity.setText("")
        self.lState.setText("")
        self.lZIP.setText("")
        self.lEmail.setText("")
        self.label_Error.setText("")
        self.pbLoad.setEnabled(True)
        self.pbSave.setEnabled(False)
    def beginEditing(self):
        self.pbSave.setEnabled(True)
        self.pbLoad.setEnabled(False)





currentApp = QApplication(sys.argv)
currentForm = SampleWindow()

currentForm.show()
currentApp.exec_()
