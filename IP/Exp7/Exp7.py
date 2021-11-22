# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp7.ui'
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
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imageinput = QtWidgets.QLabel(self.centralwidget)
        self.imageinput.setGeometry(QtCore.QRect(0, 20, 400, 225))
        self.imageinput.setText("")
        self.imageinput.setPixmap(QtGui.QPixmap(""))
        self.imageinput.setScaledContents(True)
        self.imageinput.setObjectName("imageinput")
        self.import_image = QtWidgets.QPushButton(self.centralwidget)
        self.import_image.setGeometry(QtCore.QRect(0, 260, 400, 81))
        self.import_image.setObjectName("import_image")
        self.output = QtWidgets.QPushButton(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(400, 260, 400, 81))
        self.output.setObjectName("output")
        self.imageoutput = QtWidgets.QLabel(self.centralwidget)
        self.imageoutput.setGeometry(QtCore.QRect(401, 20, 400, 225))
        self.imageoutput.setText("")
        self.imageoutput.setPixmap(QtGui.QPixmap(""))
        self.imageoutput.setScaledContents(True)
        self.imageoutput.setObjectName("imageoutput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 0, 101, 17))
        self.label_2.setObjectName("label_2")
        self.imageoutput_2 = QtWidgets.QLabel(self.centralwidget)
        self.imageoutput_2.setGeometry(QtCore.QRect(401, 370, 400, 225))
        self.imageoutput_2.setText("")
        self.imageoutput_2.setPixmap(QtGui.QPixmap(""))
        self.imageoutput_2.setScaledContents(True)
        self.imageoutput_2.setObjectName("imageoutput_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 350, 121, 17))
        self.label_3.setObjectName("label_3")
        self.imageinput_2 = QtWidgets.QLabel(self.centralwidget)
        self.imageinput_2.setGeometry(QtCore.QRect(0, 370, 400, 225))
        self.imageinput_2.setText("")
        self.imageinput_2.setPixmap(QtGui.QPixmap(""))
        self.imageinput_2.setScaledContents(True)
        self.imageinput_2.setObjectName("imageinput_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 350, 111, 17))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Importing Image
        self.import_image.clicked.connect(self.show_image)

        #Checking Output Image
        self.output.clicked.connect(self.histogram_equalisation)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_image.setText(_translate("MainWindow", "Import"))
        self.output.setText(_translate("MainWindow", "Apply Histogram Equalisation"))
        self.label.setText(_translate("MainWindow", "Imported Image"))
        self.label_2.setText(_translate("MainWindow", "Converted Image"))
        self.label_3.setText(_translate("MainWindow", "Equalised Histogram"))
        self.label_4.setText(_translate("MainWindow", "Original Histogram"))
    
    def show_image(self):
        file_filter = 'Image File (*.jpg *.png)'
        fname = QtWidgets.QFileDialog.getOpenFileName(parent=self.centralwidget,
        caption='Select an Image',
        directory="/home/deeprajb/Downloads/",
        filter=file_filter)
        self.img = cv2.imread(fname[0], cv2.IMREAD_GRAYSCALE)
        self.img1 = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_Grayscale8)
        self.hist = cv2.calcHist([self.img], [0], None, [256], [0, 256])
        self.imageinput.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        plt.figure()
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.plot(self.hist)
        plt.xlim([0, 256])
        plt.savefig('Original_Histogram.png')
        # plt.show()
        self.imageinput_2.setPixmap(QtGui.QPixmap("Original_Histogram.png"))
    
    def getCounts(self,width,height,px):
        counts=[0]*255 
        for i in range(width):
            for j in range(height):
                counts[px[i,j]]+=1
        return counts

    def histogram_equalisation(self):
        (row, col) = self.img.shape[0:2]
        # final = self.hist.copy()
        # ejo = self.hist.copy()
        preture = self.img.copy()
        counts=self.getCounts(row,col,preture)
        # ehi /= row*col
        pS=0
        for i in range(len(counts)):
            pS+=255*(counts[i]/row*col)
            counts[i]=pS
        for i in range(row):
            for j in range(col):
                preture[i,j]=int(counts[preture[i,j]])
        eq_hist = cv2.calcHist([preture], [0], None, [256], [0, 256])
        cv2.imwrite('eh_output.jpg',preture)
        self.imageoutput.setPixmap(QtGui.QPixmap("eh_output.jpg"))
        plt.figure()
        plt.xlabel("Bins")
        plt.ylabel("# of Pixels")
        plt.plot(eq_hist)
        plt.xlim([0, 256])
        plt.savefig('Equalised_Histogram.png')
        self.imageoutput_2.setPixmap(QtGui.QPixmap("Equalised_Histogram.png"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
