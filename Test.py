# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_Test import Ui_MainWindow

from PyQt5 import QtWidgets

import time

import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__( self,username,s, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.s = s
        self.username=username
        self.flag=False
        self.recvThread()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # 格式化当前的时间
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #获取消息内容
        str=self.username+"  "+theTime+"   ""说：\n    "+self.textEdit_2.toPlainText()+"\n"
        #清除消息
        self.textEdit_2.setText("")
        #发送内容
        self.s.send(str.encode())


    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.s.send("/exitmeplease".encode())
        self.flag = True
        if self.s.recv(1024).decode()=="exit":
            self.s.close()

        MainWindow.close(self)

    @pyqtSlot()
    def on_MainWindow_destroyed(self):
        """
        Slot documentation goes here.
        """
        print("3")


    #接收消息函数
    def receive(self):
        while True:
            if self.flag:
                break
            str=self.s.recv(1024).decode()
            self.textEdit.append(str)


    #线程
    def recvThread(self):
        print("5")
        t = threading.Thread(target=self.receive, args=())
        t.start()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


