# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import os
import multiprocessing

from exec import pomodoro

class Ui_Pomodorism_S_TeaM(object):
    def setupUi(self, Pomodorism_S_TeaM):
        Pomodorism_S_TeaM.setObjectName("Pomodorism_S_TeaM")
        Pomodorism_S_TeaM.resize(399, 410)
        Pomodorism_S_TeaM.setAutoFillBackground(False)
        Pomodorism_S_TeaM.setStyleSheet("QDialog{ background-color:rgb(111, 166, 96)}")
        self.buttonBox = QtWidgets.QDialogButtonBox(Pomodorism_S_TeaM)
        self.buttonBox.setGeometry(QtCore.QRect(250, 350, 71, 32))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.rejected.connect(lambda: self.out())
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
        self.valuePomo = QtWidgets.QSpinBox(Pomodorism_S_TeaM)
        self.valuePomo.setGeometry(QtCore.QRect(220, 80, 71, 22))
        self.valuePomo.setMinimumSize(QtCore.QSize(71, 22))
        self.valuePomo.setStyleSheet("QSpinBox{ background-color:#d4b7b7}")
        self.valuePomo.setMaximum(120)
        self.valuePomo.setProperty("value", 25)
        self.valuePomo.setObjectName("valuePomo")
        self.valueshortbreak = QtWidgets.QSpinBox(Pomodorism_S_TeaM)
        self.valueshortbreak.setGeometry(QtCore.QRect(220, 120, 71, 22))
        self.valueshortbreak.setStyleSheet("QSpinBox{ background-color:#d4b7b7}")
        self.valueshortbreak.setMaximum(30)
        self.valueshortbreak.setProperty("value", 5)
        self.valueshortbreak.setObjectName("valueshortbreak")
        self.valuelongbreak = QtWidgets.QSpinBox(Pomodorism_S_TeaM)
        self.valuelongbreak.setGeometry(QtCore.QRect(220, 160, 71, 22))
        self.valuelongbreak.setStyleSheet("QSpinBox{ background-color:#d4b7b7}")
        self.valuelongbreak.setMaximum(60)
        self.valuelongbreak.setProperty("value", 30)
        self.valuelongbreak.setObjectName("valuelongbreak")
        self.valuecounter = QtWidgets.QSpinBox(Pomodorism_S_TeaM)
        self.valuecounter.setGeometry(QtCore.QRect(220, 210, 71, 22))
        self.valuecounter.setAutoFillBackground(False)
        self.valuecounter.setStyleSheet("QSpinBox{ background-color:#d4b7b7}")
        self.valuecounter.setMaximum(8)
        self.valuecounter.setProperty("value", 4)
        self.valuecounter.setObjectName("valuecounter")
        self.notify = QtWidgets.QComboBox(Pomodorism_S_TeaM)
        self.notify.setGeometry(QtCore.QRect(220, 260, 101, 22))
        self.notify.setAutoFillBackground(False)
        self.notify.setStyleSheet("QComboBox{ background-color:#d4b7b7}")
        self.notify.setObjectName("notify")
        self.notify.addItem("")
        self.notify.addItem("")
        self.notify.addItem("")
        self.label = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.label.setGeometry(QtCore.QRect(100, 280, 261, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Pomodorism_S_TeaM)
        self.label_2.setGeometry(QtCore.QRect(30, 291, 71, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Pomodorism_S_TeaM, clicked = lambda: self.on_click_start(Pomodorism_S_TeaM))
        self.pushButton.setGeometry(QtCore.QRect(160, 354, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Pomodorism_S_TeaM, clicked = lambda: self.on_click_reset())
        self.pushButton_2.setGeometry(QtCore.QRect(70, 354, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Pomodorism_S_TeaM)
        self.buttonBox.accepted.connect(Pomodorism_S_TeaM.accept)
        self.buttonBox.rejected.connect(Pomodorism_S_TeaM.reject)
        QtCore.QMetaObject.connectSlotsByName(Pomodorism_S_TeaM)

    def retranslateUi(self, Pomodorism_S_TeaM):
        _translate = QtCore.QCoreApplication.translate
        Pomodorism_S_TeaM.setWindowIcon(QtGui.QIcon('icon.png'))
        Pomodorism_S_TeaM.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        Pomodorism_S_TeaM.setWindowTitle(_translate("Pomodorism_S_TeaM", "Write by l1ghtg3m"))
        self.buttonBox.setToolTip(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><br/></p></body></html>"))
        self.title.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#CA4141;\">-S-Pomodoro</span></p></body></html>"))
        self.setpomo.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#04591A;\">Pomodoro:</span></p></body></html>"))
        self.setshort.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;color:#04591A;\">Short break time:</span></p></body></html>"))
        self.setlong.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;color:#04591A;\">Long break time:</span></p></body></html>"))
        self.counter.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\";  style=\"line-height:50%;color:#04591A;\"><span style=\" font-size:12pt;\">Num of pomodori </span></p><p align=\"right\";  style=\"line-height:50%;color:#04591A;\"><span style=\" font-size:12pt;\">per long break time:</span></p></body></html>"))
        self.alertby.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;color:#04591A;\">Notify by:</span></p></body></html>"))
        self.notify.setItemText(0, _translate("Pomodorism_S_TeaM", "Cover screen 5s"))
        self.notify.setItemText(1, _translate("Pomodorism_S_TeaM", "Ring a bell"))
        self.notify.setItemText(2, _translate("Pomodorism_S_TeaM", "Both"))
        self.label.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p style=\"line-height:50%\" ><span style=\" font-size:10pt; color:#70423d;\">Unit: minute(s)</span></p><p align=\"justify\" style=\"line-height:50%\"><span style=\" font-size:10pt; color:#70423d;\">Ver0.1</span></p></body></html>"))
        self.label_2.setText(_translate("Pomodorism_S_TeaM", "<html><head/><body><p><span style=\" font-size:15pt; color:#70423d;\">*Note:</span></p></body></html>"))
        self.pushButton.setText(_translate("Pomodorism_S_TeaM", "Start"))
        self.pushButton_2.setText(_translate("Pomodorism_S_TeaM", "Reset"))

    def on_click_start(self, Pomodorism_S_TeaM): # Start button return result and show new windows
        result = self.result()
        Pomodorism_S_TeaM.close()
        #pomodoro(result[0], result[1], result[2], result[3]).run()
        with open("setting.txt","w+" ) as setter:
            for var in result:
                setter.write(str(var)+"\n")
    def on_click_reset(self):  # Reset  button
        self.reset()

    def result(self):
        long = self.valuelongbreak.value()
        round = self.valuecounter.value()
        short = self.valueshortbreak.value()
        time = self.valuePomo.value()
        option = self.notify.currentIndex()
        return [time, short, long, round, option]

    def reset(self):
        self.valuelongbreak.setProperty("value", 30)
        self.valuecounter.setProperty("value", 4)
        self.valueshortbreak.setProperty("value", 5)
        self.valuePomo.setProperty("value", 25)
    def out(self):
        exit()

#if __name__ == "__main__":
def run():
    import sys
    try:
        app
    except:
        app = QtWidgets.QApplication(sys.argv)
    Pomodorism_S_TeaM = QtWidgets.QDialog()
    ui = Ui_Pomodorism_S_TeaM()
    ui.setupUi(Pomodorism_S_TeaM)
    Pomodorism_S_TeaM.show()
    app.exec_()
#run()