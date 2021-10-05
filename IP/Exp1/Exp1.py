# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(0, 0, 801, 451))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(""))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.import_image = QtWidgets.QPushButton(self.centralwidget)
        self.import_image.setGeometry(QtCore.QRect(0, 450, 261, 81))
        self.import_image.setObjectName("import_image")
        self.output = QtWidgets.QPushButton(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(260, 450, 281, 81))
        self.output.setObjectName("output")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(540, 450, 261, 81))
        self.clear.setObjectName("clear")
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
        self.output.clicked.connect(self.show_output)

        #Clearing Image
        self.clear.clicked.connect(self.clear_image)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_image.setText(_translate("MainWindow", "Import"))
        self.output.setText(_translate("MainWindow", "Output"))
        self.clear.setText(_translate("MainWindow", "Clear"))

    def show_image(self):
        self.img = cv2.imread('killer.jpg')
        self.img1 = QtGui.QImage(self.img.data, self.img.shape[1], self.img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image.setPixmap(QtGui.QPixmap.fromImage(self.img1))
    
    def show_output(self):
        cv2.imwrite('output.jpg',self.img)
        self.image.setPixmap(QtGui.QPixmap("output.jpg"))
    
    def clear_image(self):
        self.image.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
