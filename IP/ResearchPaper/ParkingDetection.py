# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParkingDetection.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
import numpy as np
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageinput = QtWidgets.QLabel(self.centralwidget)
        self.imageinput.setGeometry(QtCore.QRect(0, 80, 400, 323))
        self.imageinput.setText("")
        self.imageinput.setPixmap(QtGui.QPixmap(""))
        self.imageinput.setScaledContents(True)
        self.imageinput.setObjectName("imageinput")
        self.import_image = QtWidgets.QPushButton(self.centralwidget)
        self.import_image.setGeometry(QtCore.QRect(200, 420, 400, 81))
        self.import_image.setObjectName("import_image")
        self.imageoutput = QtWidgets.QLabel(self.centralwidget)
        self.imageoutput.setGeometry(QtCore.QRect(401, 80, 400, 323))
        self.imageoutput.setText("")
        self.imageoutput.setPixmap(QtGui.QPixmap(""))
        self.imageoutput.setScaledContents(True)
        self.imageoutput.setObjectName("imageoutput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 60, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 60, 111, 17))
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(360, 10, 91, 51))
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 0, 81, 17))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.count = -1

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Importing Image
        self.import_image.clicked.connect(self.show_image)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_image.setText(_translate("MainWindow", "Next Frame"))
        self.label.setText(_translate("MainWindow", "Live Frame"))
        self.label_2.setText(_translate("MainWindow", "Parking Detection"))
        self.label_3.setText(_translate("MainWindow", "Parking Left"))

    def show_image(self):
        self.count+=1
        self.image_link = ['Images/Parking_Empty.jpg','Images/Parking_1.jpg','Images/Parking_3.jpg','Images/Parking_Full.jpg','Images/Parking_5.jpg']
        self.img = cv2.imread(self.image_link[self.count])
        self.output = self.img.copy()
        self.img1 = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0],QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imageinput.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        self.detect_circles()
        
    def detect_circles(self):
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img = cv2.GaussianBlur(self.img, (21,21), cv2.BORDER_DEFAULT)
        
        # Find circles
        circles = cv2.HoughCircles(self.img, cv2.HOUGH_GRADIENT,0.9,120,param1 =50, param2 = 30 , minRadius= 60, maxRadius=100)
        # If some circle is found
        if circles is not None:
            # Get the (x, y, r) as integers
            circles = np.round(circles[0, :]).astype("int")
            self.lcdNumber.display(circles.shape[0])
            # loop over the circles
            for (x, y, r) in circles:
                cv2.circle(self.output, (x, y), r, (0, 255, 0), 2)
        else:
            self.lcdNumber.display(0)
        cv2.imwrite('circles_output.jpg',self.output)
        self.imageoutput.setPixmap(QtGui.QPixmap("circles_output.jpg"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
                  