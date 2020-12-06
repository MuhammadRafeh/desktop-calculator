# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
class Ui_MainWindow(QMainWindow):    #object by default
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 398)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Calculator = QtWidgets.QLabel(self.centralwidget)
        self.Calculator.setGeometry(QtCore.QRect(170, 0, 141, 31))
        self.Calculator.setTextFormat(QtCore.Qt.RichText)
        self.Calculator.setObjectName("Calculator")
        self.Credit = QtWidgets.QLabel(self.centralwidget)
        self.Credit.setGeometry(QtCore.QRect(10, 0, 111, 20))
        self.Credit.setObjectName("Credit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(132, 190, 51, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(252, 230, 51, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(132, 230, 51, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(192, 230, 51, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(132, 150, 51, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(252, 190, 51, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(252, 150, 51, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(192, 150, 51, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(192, 270, 51, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(192, 190, 51, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 0, 121, 17))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 44, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(132, 270, 51, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(252, 270, 51, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(312, 230, 51, 71))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(312, 190, 51, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(312, 150, 51, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(312, 110, 51, 25))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(252, 110, 51, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(192, 110, 51, 25))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(130, 110, 51, 25))
        self.pushButton_19.setObjectName("pushButton_19")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 80, 231, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, -10, 501, 431))
        self.label_2.setStyleSheet("image: url(:/newPrefix/black-calculator-near-ballpoint-pen-on-white-printed-paper-53621 (1).jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.Calculator.raise_()
        self.Credit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.lineEdit_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.lineEdit_2.setEnabled(False)
        MainWindow.setFixedSize(485,415)
    

        #Buttons
        self.pushButton_9.clicked.connect(self.B0)
        self.pushButton_3.clicked.connect(self.B1)
        self.pushButton_4.clicked.connect(self.B2)
        self.pushButton_2.clicked.connect(self.B3)
        self.pushButton.clicked.connect(self.B4)
        self.pushButton_10.clicked.connect(self.B5)
        self.pushButton_6.clicked.connect(self.B6)
        self.pushButton_5.clicked.connect(self.B7)
        self.pushButton_8.clicked.connect(self.B8)
        self.pushButton_7.clicked.connect(self.B9)
        #Operations

        self.pushButton_12.clicked.connect(self.Bdot)
        self.pushButton_11.clicked.connect(self.Bper)
        self.pushButton_13.clicked.connect(self.Bequal)
        self.pushButton_14.clicked.connect(self.Bplus)
        self.pushButton_15.clicked.connect(self.Bminus)
        self.pushButton_17.clicked.connect(self.Bmultiply)
        self.pushButton_18.clicked.connect(self.Bdivide)
        self.pushButton_19.clicked.connect(self.Bra)
        self.pushButton_16.clicked.connect(self.Br)


        self.lineEdit.setText(None)

        #Operations
        self.operation = ['+','-','x','/','−','÷']

        #Values
        self.txt = ''
        self.cp = 0

        #Flags
        self.flag = False
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False

        self.lineEdit.keyPressEvent = self.keyPressEvent

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Calculator.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CALCULATOR</span></p></body></html>"))
        self.Credit.setText(_translate("MainWindow", "Credit: M. Rafeh"))
        self.pushButton.setText(_translate("MainWindow", "4"))
        self.pushButton_2.setText(_translate("MainWindow", "3"))
        self.pushButton_3.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "2"))
        self.pushButton_5.setText(_translate("MainWindow", "7"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "9"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "0"))
        self.pushButton_10.setText(_translate("MainWindow", "5"))
        self.label.setText(_translate("MainWindow", "Shikari\'s Product"))
        self.lineEdit.setText(_translate("MainWindow", "asdasd"))
        self.pushButton_11.setText(_translate("MainWindow", "%"))
        self.pushButton_12.setText(_translate("MainWindow", "."))
        self.pushButton_13.setText(_translate("MainWindow", "="))
        self.pushButton_14.setText(_translate("MainWindow", "+"))
        self.pushButton_15.setText(_translate("MainWindow", "−"))
        self.pushButton_16.setText(_translate("MainWindow", "<"))
        self.pushButton_17.setText(_translate("MainWindow", "x"))
        self.pushButton_18.setText(_translate("MainWindow", "÷"))
        self.pushButton_19.setText(_translate("MainWindow", "C"))

    def B0(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'0'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B1(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'1'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B2(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'2'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B3(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'3'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B4(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'4'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B5(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'5'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B6(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'6'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B7(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'7'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def B8(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.lineEdit.setText(self.txt[0:self.cp]+'8'+self.txt[self.cp::])
        #print(self.lineEdit.cursorPositionChanged())
        self.lineEdit.setCursorPosition(self.cp+1)

    def B9(self):

        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        print(self.cp)
        self.lineEdit.setText(self.txt[0:self.cp]+'9'+self.txt[self.cp::])
        self.lineEdit.setCursorPosition(self.cp+1)

    def Bdot(self):
        self.lineEdit.insert('.')

    def Bper(self):
        self.lineEdit.setText(self.lineEdit.text()+'%')

    def Bequal(self):
	    pass
        # self.txt = self.lineEdit.text()
        # self.cp = self.lineEdit.cursorPosition()
        # _1st = ''
        #print(self.txt.find('x'))
        #print(self.txt.split('+',2))
        # if self.txt.find('x') < self.txt.find('x') and 
        # _2nd = ''
        # oper = ''
        # new = 0
        #a = 1
        #local = 0
        #flag9 = True
    """for i in self.txt:
            if i in self.operation:
                oper = i
                flag9 = False
                local+=1
            if flag9:
                if (local%2 == 0 or local == 0) and (a == 1):
                    _1st = _1st + i
                else:
                    _2nd = _2nd + i
                    a = 2
            else:
                #_1st = ''
                if _2nd != '':
                    if oper == '+':
                        new = (float(_1st)  + float(_2nd))
                        _1st = str(new)
                    elif oper == '−':
                        new = (float(_1st)  - float(_2nd))
                        _1st = str(new)
                    elif oper == 'x':
                        new = (float(_1st)  * float(_2nd))
                        _1st = str(new)
                    elif oper == '÷':
                        new = (float(_1st)  / float(_2nd))
                        _1st = str(new)

            
                _2nd = ''
                flag9 = True
            print('1st',_1st,'2nd',_2nd)
            
        print(_1st,_2nd,'Your result id: ',new)"""


    def Bplus(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()

        self.flag = False
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False

        try:
            if self.cp-1>=0:
                if self.txt[self.cp-1] in self.operation:
                    self.txt = self.txt[0:self.cp-1]+'+'+self.txt[self.cp::]
                    self.lineEdit.setText(self.txt)
                    self.lineEdit.setCursorPosition(self.cp)
            
                else:
                    self.flag2 = True
            elif self.cp-1==-1 and self.txt[self.cp] not in self.operation:
                #self.txt = self.txt[0:self.cp-1]+'+'+self.txt[self.cp::]
                self.lineEdit.insert('+')
                self.lineEdit.setCursorPosition(self.cp)



            self.flag = True
        except Exception as e:
            pass
        try:
            if self.txt[self.cp] in self.operation:     #Error occur when On Right side is nothing its mean cursur is at end
                self.txt = self.txt[0:self.cp]+'+'+self.txt[self.cp+1::]
                self.lineEdit.setText(self.txt)
                self.lineEdit.setCursorPosition(self.cp)
        
            else:
                self.flag3 = True
                
        except Exception as e:
            self.flag1 = True

        if self.flag and self.flag1 and self.txt[self.cp-1] not in self.operation:
            self.lineEdit.setText(self.txt+'+')
        
        if self.flag2 and self.flag3:
            self.lineEdit.setText(self.txt[0:self.cp]+'+'+self.txt[self.cp::])
            self.lineEdit.setCursorPosition(self.cp)
    

    def Bminus(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()

        self.flag = False
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False

        try:
            if self.cp-1>=0:
                if self.txt[self.cp-1] in self.operation:
                    self.txt = self.txt[0:self.cp-1]+'−'+self.txt[self.cp::]
                    self.lineEdit.setText(self.txt)
                    self.lineEdit.setCursorPosition(self.cp)
            
                else:
                    self.flag2 = True
            elif self.cp-1==-1 and self.txt[self.cp] not in self.operation:
                #self.txt = self.txt[0:self.cp-1]+'+'+self.txt[self.cp::]
                self.lineEdit.insert('−')
                self.lineEdit.setCursorPosition(self.cp)



            self.flag = True
        except Exception as e:
            pass
        try:
            if self.txt[self.cp] in self.operation:     #Error occur when On Right side is nothing its mean cursur is at end
                self.txt = self.txt[0:self.cp]+'−'+self.txt[self.cp+1::]
                self.lineEdit.setText(self.txt)
                self.lineEdit.setCursorPosition(self.cp)
        
            else:
                self.flag3 = True
                
        except Exception as e:
            self.flag1 = True

        if self.flag and self.flag1 and self.txt[self.cp-1] not in self.operation:
            self.lineEdit.setText(self.txt+'−')
        
        if self.flag2 and self.flag3:
            self.lineEdit.setText(self.txt[0:self.cp]+'−'+self.txt[self.cp::])
            self.lineEdit.setCursorPosition(self.cp)
        if self.txt == '':
            self.lineEdit.insert('−')

    def Bmultiply(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()

        self.flag = False
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False

        try:
            if self.cp-1>=0:
                if self.txt[self.cp-1] in self.operation:
                    self.txt = self.txt[0:self.cp-1]+'x'+self.txt[self.cp::]
                    self.lineEdit.setText(self.txt)
                    self.lineEdit.setCursorPosition(self.cp)
            
                else:
                    self.flag2 = True
            elif self.cp-1==-1 and self.txt[self.cp] not in self.operation:
                #self.txt = self.txt[0:self.cp-1]+'+'+self.txt[self.cp::]
                self.lineEdit.insert('x')
                self.lineEdit.setCursorPosition(self.cp)



            self.flag = True
        except Exception as e:
            pass
        try:
            if self.txt[self.cp] in self.operation:     #Error occur when On Right side is nothing its mean cursur is at end
                self.txt = self.txt[0:self.cp]+'x'+self.txt[self.cp+1::]
                self.lineEdit.setText(self.txt)
                self.lineEdit.setCursorPosition(self.cp)
        
            else:
                self.flag3 = True
                
        except Exception as e:
            self.flag1 = True

        if self.flag and self.flag1 and self.txt[self.cp-1] not in self.operation:
            self.lineEdit.setText(self.txt+'x')
        
        if self.flag2 and self.flag3:
            self.lineEdit.setText(self.txt[0:self.cp]+'x'+self.txt[self.cp::])
            self.lineEdit.setCursorPosition(self.cp)

    def Bdivide(self):
        #'÷'
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()

        self.flag = False
        self.flag1 = False
        self.flag2 = False
        self.flag3 = False

        try:
            if self.cp-1>=0:
                if self.txt[self.cp-1] in self.operation:
                    self.txt = self.txt[0:self.cp-1]+'÷'+self.txt[self.cp::]
                    self.lineEdit.setText(self.txt)
                    self.lineEdit.setCursorPosition(self.cp)
            
                else:
                    self.flag2 = True
            elif self.cp-1==-1 and self.txt[self.cp] not in self.operation:
                #self.txt = self.txt[0:self.cp-1]+'+'+self.txt[self.cp::]
                self.lineEdit.insert('÷')
                self.lineEdit.setCursorPosition(self.cp)



            self.flag = True
        except Exception as e:
            pass
        try:
            if self.txt[self.cp] in self.operation:     #Error occur when On Right side is nothing its mean cursur is at end
                self.txt = self.txt[0:self.cp]+'÷'+self.txt[self.cp+1::]
                self.lineEdit.setText(self.txt)
                self.lineEdit.setCursorPosition(self.cp)
        
            else:
                self.flag3 = True
                
        except Exception as e:
            self.flag1 = True

        if self.flag and self.flag1 and self.txt[self.cp-1] not in self.operation:
            self.lineEdit.setText(self.txt+'÷')
        
        if self.flag2 and self.flag3:
            self.lineEdit.setText(self.txt[0:self.cp]+'÷'+self.txt[self.cp::])
            self.lineEdit.setCursorPosition(self.cp)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_0:
            self.B0()
        elif e.key() == Qt.Key_1:
            self.B1()
        elif e.key() == Qt.Key_2:
            self.B2()
        elif e.key() == Qt.Key_3:
            self.B3()
        elif e.key() == Qt.Key_4:
            self.B4()
        elif e.key() == Qt.Key_5:
            self.B5()
        elif e.key() == Qt.Key_6:
            self.B6()
        elif e.key() == Qt.Key_7:
            self.B7()
        elif e.key() == Qt.Key_8:
            self.B8()
        elif e.key() == Qt.Key_9:
            self.B9()
        #Operations
        elif e.key() == Qt.Key_Asterisk:
            self.Bmultiply()
        elif e.key() == Qt.Key_Slash:
            self.Bdivide()
        elif e.key() == Qt.Key_Plus:
            self.Bplus()
        elif e.key() == Qt.Key_Minus:
            self.Bminus()
        #Backspace
        elif e.key() == Qt.Key_Backspace:
            self.Br()
        elif e.key() == Qt.Key_Percent:
            self.Bper()
        elif e.key() == Qt.Key_Enter:
            self.Bequal()
        else:
            if e.key() != Qt.Key_Shift:
                QMessageBox.about(self, 'Warning', "Invalid Input will not accept here")

    def Br(self):
        self.txt = self.lineEdit.text()
        self.cp = self.lineEdit.cursorPosition()
        self.txt = self.txt[0:self.cp-1]+self.txt[self.cp::]
        self.lineEdit.setText(self.txt)
        if self.cp-1>=0:
            self.lineEdit.setCursorPosition(self.cp-1)

    def Bra(self):
        self.lineEdit.setText(None)
        self.lineEdit_2.setText(None)

import source

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
