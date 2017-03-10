# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\项鸿志\Documents\PythonGUI\Test.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 745)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 20, 941, 541))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 570, 941, 131))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 710, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 710, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
