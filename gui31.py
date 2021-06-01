# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\layer2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from playsound import playsound

class Ui_Pomodorism_S_TeaM(object):
    def getValue(self):
        with open("setting.txt", "r+") as setter:
            getset = setter.readlines()
            valuer=[]
            for line in getset:
                valuer.insert(len(valuer), line.rstrip("\n"))
        return valuer
    def setupUi(self, Pomodorism_S_TeaM):
        numLCD = self.getValue()
        Pomodorism_S_TeaM.setObjectName("Pomodorism_S_TeaM")
        Pomodorism_S_TeaM.resize(399, 410)
        Pomodorism_S_TeaM.setAutoFillBackground(False)
        Pomodorism_S_TeaM.setStyleSheet("QDialog{ background-color:rgb(111, 166, 96)}")
        self.buttonBox = QtWidgets.QDialogButtonBox(Pomodorism_S_TeaM)
        self.buttonBox.setGeometry(QtCore.QRect(210, 350, 71, 32))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.title = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.title.setGeometry(QtCore.QRect(50, 10, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        self.title.setFont(font)
        self.title.setStyleSheet("")
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setOpenExternalLinks(False)
        self.title.setObjectName("title")
        self.setpomo = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.setpomo.setGeometry(QtCore.QRect(90, 80, 111, 21))
        self.setpomo.setObjectName("setpomo")
        self.setshort = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.setshort.setGeometry(QtCore.QRect(80, 120, 121, 20))
        self.setshort.setObjectName("setshort")
        self.setlong = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.setlong.setGeometry(QtCore.QRect(80, 160, 121, 20))
        self.setlong.setObjectName("setlong")
        self.counter = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.counter.setGeometry(QtCore.QRect(30, 190, 171, 51))
        self.counter.setAlignment(QtCore.Qt.AlignCenter)
        self.counter.setWordWrap(True)
        self.counter.setObjectName("counter")
        self.alertby = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.alertby.setGeometry(QtCore.QRect(50, 260, 151, 20))
        self.alertby.setObjectName("alertby")
        self.label = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.label.setGeometry(QtCore.QRect(80, 282, 311, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.label_2.setGeometry(QtCore.QRect(10, 291, 71, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Pomodorism_S_TeaM, clicked = lambda: self.replay())
        self.pushButton.setGeometry(QtCore.QRect(120, 354, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(Pomodorism_S_TeaM)
        self.lcdNumber.setGeometry(QtCore.QRect(210, 80, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setProperty("value", numLCD[0])
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Pomodorism_S_TeaM)
        self.lcdNumber_2.setGeometry(QtCore.QRect(210, 120, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setProperty("value", numLCD[1])
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Pomodorism_S_TeaM)
        self.lcdNumber_3.setGeometry(QtCore.QRect(210, 160, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_3.setProperty("value", numLCD[2])
        self.lcdNumber_4 = QtWidgets.QLCDNumber(Pomodorism_S_TeaM)
        self.lcdNumber_4.setGeometry(QtCore.QRect(210, 210, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_4.setProperty("value", numLCD[3])
        self.label_3 = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.label_3.setGeometry(QtCore.QRect(210, 260, 161, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Pomodorism_S_TeaM)
        self.buttonBox.accepted.connect(Pomodorism_S_TeaM.accept)
        self.buttonBox.rejected.connect(Pomodorism_S_TeaM.reject)
        QtCore.QMetaObject.connectSlotsByName(Pomodorism_S_TeaM)
        Pomodorism_S_TeaM.showMinimized()

    def retranslateUi(self, Pomodorism_S_TeaM):
        _translate = QtCore.QCoreApplication.translate
        Pomodorism_S_TeaM.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        Pomodorism_S_TeaM.setWindowTitle(_translate("Pomodorism_S_TeaM", "Write by l1ghtg3m"))
        self.buttonBox.setToolTip(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><br/></p></body></html>"))
        self.title.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#CA4141;\">-S-Pomodoro</span></p></body></html>"))
        self.setpomo.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#04591A;\">Pomodoro:</span></p></body></html>"))
        self.setshort.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;color:#04591A;\">Short break time:</span></p></body></html>"))
        self.setlong.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;color:#04591A;\">Long break time:</span></p></body></html>"))
        self.counter.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\";  style=\"line-height:50%;color:#04591A;\"><span style=\" font-size:12pt;\">Num of pomodori </span></p><p align=\"right\";  style=\"line-height:50%;color:#04591A;\"><span style=\" font-size:12pt;\">per long break time:</span></p></body></html>"))
        self.alertby.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;color:#04591A;\">Notify by:</span></p></body></html>"))
        self.label.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><span style=\" font-size:12pt; color:#70423d;\">Running...... (Replay: For fun!)</span></p></body></html>"))
        self.label_2.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><span style=\" font-size:15pt; color:#70423d;\">*Note:</span></p></body></html>"))
        self.pushButton.setText(_translate("Pomodorism_S_TeaM", "Replay"))
        options = self.getValue()
        option = int(options[4])
        if option == 0:
            textOptions = "Cover screen 5s"
        elif option == 1:
            textOptions = "Ring a bell"
        elif option == 2:
            textOptions = "Both"
        self.label_3.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><span style=\" font-size:12pt;color:#04591A;\">"+textOptions +"</span></p></body></html>"))

    def replay(self):
        playsound("ohno01.wav")
#if __name__ == "__main__":
def run1():
    import sys
    try:
        app
    except:
        app = QtWidgets.QApplication(sys.argv)
    Pomodorism_S_TeaM = QtWidgets.QDialog()
    ui = Ui_Pomodorism_S_TeaM()
    ui.setupUi(Pomodorism_S_TeaM)
    Pomodorism_S_TeaM.show()
    sys.exit(app.exec_())
