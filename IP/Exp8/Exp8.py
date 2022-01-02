# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp8.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 638)
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
        self.label.setGeometry(QtCore.QRect(150, 0, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 0, 71, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 340, 121, 17))
        self.label_3.setObjectName("label_3")
        self.imageoutput_2 = QtWidgets.QLabel(self.centralwidget)
        self.imageoutput_2.setGeometry(QtCore.QRect(0, 360, 400, 225))
        self.imageoutput_2.setText("")
        self.imageoutput_2.setPixmap(QtGui.QPixmap(""))
        self.imageoutput_2.setScaledContents(True)
        self.imageoutput_2.setObjectName("imageoutput_2")
        self.imageoutput_3 = QtWidgets.QLabel(self.centralwidget)
        self.imageoutput_3.setGeometry(QtCore.QRect(401, 360, 400, 225))
        self.imageoutput_3.setText("")
        self.imageoutput_3.setPixmap(QtGui.QPixmap(""))
        self.imageoutput_3.setScaledContents(True)
        self.imageoutput_3.setObjectName("imageoutput_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(510, 340, 171, 17))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 22))
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
        self.output.clicked.connect(self.smoothening)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smoothening Techniques"))
        self.import_image.setText(_translate("MainWindow", "Import"))
        self.output.setText(_translate("MainWindow", "Apply Smoothening"))
        self.label.setText(_translate("MainWindow", "Imported Image"))
        self.label_2.setText(_translate("MainWindow", "Box Filter"))
        self.label_3.setText(_translate("MainWindow", "Median Filter"))
        self.label_4.setText(_translate("MainWindow", "Weighted Average Filter"))
    
    def show_image(self):
        file_filter = 'Image File (*.jpg *.png)'
        fname = QtWidgets.QFileDialog.getOpenFileName(parent=self.centralwidget,
        caption='Select an Image',
        directory="/run/media/deeprajb/HDD/Important Photos/Wallpapers",
        filter=file_filter)
        self.img = cv2.imread(fname[0])
        self.img1 = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imageinput.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        
    def smoothening(self):
        img_b_blur_50 = cv2.boxFilter(self.img, -1, (50,50))
        img_median = cv2.medianBlur(self.img, 35)
        img_blur_50 = cv2.blur(self.img, (50,50))
        cv2.imwrite('bf_output.jpg',img_b_blur_50)
        cv2.imwrite('mf_output.jpg',img_median)
        cv2.imwrite('wa_output.jpg',img_blur_50)
        self.imageoutput.setPixmap(QtGui.QPixmap("bf_output.jpg"))
        self.imageoutput_2.setPixmap(QtGui.QPixmap("mf_output.jpg"))
        self.imageoutput_3.setPixmap(QtGui.QPixmap("wa_output.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
