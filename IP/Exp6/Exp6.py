# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp6.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 430)
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(224, 355, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(462, 355, 56, 17))
        self.label_5.setObjectName("label_5")
        self.lowerbound = QtWidgets.QSpinBox(self.centralwidget)
        self.lowerbound.setGeometry(QtCore.QRect(354, 350, 101, 30))
        self.lowerbound.setMaximum(254)
        self.lowerbound.setObjectName("lowerbound")
        self.upperbound = QtWidgets.QSpinBox(self.centralwidget)
        self.upperbound.setGeometry(QtCore.QRect(480, 350, 101, 30))
        self.upperbound.setMaximum(255)
        self.upperbound.setValue(255)
        self.upperbound.setObjectName("upperbound")
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
        self.output.clicked.connect(self.contrast_stretching)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contrast Stretching"))
        self.import_image.setText(_translate("MainWindow", "Import"))
        self.output.setText(_translate("MainWindow", "Apply Contrast Stretching"))
        self.label.setText(_translate("MainWindow", "Imported Image"))
        self.label_2.setText(_translate("MainWindow", "Converted Image"))
        self.label_4.setText(_translate("MainWindow", "Rmin - Rmax Range: "))
        self.label_5.setText(_translate("MainWindow", "-"))
    
    def show_image(self):
        file_filter = 'Image File (*.jpg *.png)'
        fname = QtWidgets.QFileDialog.getOpenFileName(parent=self.centralwidget,
        caption='Select an Image',
        directory="/run/media/deeprajb/HDD/Important Photos/Wallpapers",
        filter=file_filter)
        self.img = cv2.imread(fname[0], cv2.IMREAD_GRAYSCALE)
        self.img1 = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_Grayscale8)
        self.imageinput.setPixmap(QtGui.QPixmap.fromImage(self.img1))
    
    def contrast_stretching(self):
        (row, col) = self.img.shape[0:2]
        min_range = self.lowerbound.value()
        max_range = self.upperbound.value()
        cso = self.img.copy()
        smin=0
        smax=255
        for i in range(0,row-1):
            for j in range(0,col-1):
                if self.img[i,j] <= min_range:
                    cso[i,j] = smin
                elif self.img[i,j] >= max_range:
                    cso[i,j] = smax
                else:
                    cso[i,j] = smin + (((smax-smin)*(self.img[i,j]-min_range))/(max_range-min_range))
        cv2.imwrite('cs_output.jpg',cso)
        self.imageoutput.setPixmap(QtGui.QPixmap("cs_output.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
