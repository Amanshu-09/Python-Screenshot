from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from SS import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pyscreenshot
from PIL.ImageQt import ImageQt

class cls_SS(QtWidgets.QMainWindow):
    def __init__(self):
        super(cls_SS, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer(self)

        #Events
        self.ui.btncapture.clicked.connect(self.capture)
        self.ui.btnsave.clicked.connect(self.save)
        self.ui.btnclear.clicked.connect(self.clear)
        self.timer.timeout.connect(self.after_sec)

    def capture(self):
        self.timer.start(1000)
        self.tp = 0
        self.st = self.ui.cmb_timer.currentText()
        self.tt = self.st.split(" ")
        if self.st == "Off":
            self.img = pyscreenshot.grab()
            qim = ImageQt(self.img).copy()
            pix = QPixmap.fromImage(qim)
            self.ui.lblSSPreview.setPixmap(pix)
            self.ui.lblSSPreview.setScaledContents(True)
            self.timer.stop()
        else:
            self.hide()

    def after_sec(self):
        try:
            self.tp = self.tp + 1
            if self.tp == int(self.tt[0])-1:
                self.img = pyscreenshot.grab()
                qim = ImageQt(self.img).copy()
                pix = QPixmap.fromImage(qim)
                self.ui.lblSSPreview.setPixmap(pix)
                self.ui.lblSSPreview.setScaledContents(True)
                self.show()
        except:
            pass

    def save(self):
        try:
            ispath = self.ui.txtSSFullPath.text()
            isname = self.ui.txtSSName.text()
            self.img.save(ispath+"\\"+isname+".png")
        except:
            self.ui.lblSSPreview.setText("Error : Please Enter Path and Name For Screenshot !!!\n"
                                         "And Do Not Forget to Capture Screenshot !!!")

    def clear(self):
        try:
            self.ui.txtSSName.setText("")
            self.ui.txtSSFullPath.setText("")
            self.ui.cmb_timer.setCurrentText("Off")
            self.ui.lblSSPreview.clear()
        except:
            pass