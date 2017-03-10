# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import socket, sys;
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_Login import Ui_Dialog

from PyQt5 import QtWidgets

from Test import MainWindow


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()  # 登录，发送用户名密码至服务器验证，成功则进入聊天界面
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        username = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        print(username)
        if username.strip() == '' or passwd.strip()== '':
            QMessageBox.warning(self, "警告", "用户名或密码不能为空！", QMessageBox.Yes)
            return
        # 连接服务器
        addr = (socket.gethostname(), 8888)
        s = socket.socket()
        s.connect(addr)
        # 发送用户名和密码
        str1 = username + "&" + passwd
        print(str1)
        s.send(str1.encode())
        # 接收服务器反馈
        info = s.recv(1024).decode()
        if info=="2":
            QMessageBox.warning(self, "警告", "该用户已登录！", QMessageBox.Yes)
            return
        if info == "4":
            QMessageBox.warning(self, "警告", "用户名或密码错误！", QMessageBox.Yes)
            return
        if info=="1":
            self.another = MainWindow(username,s)
            self.another.show()
            Dialog.close(self)
        else:
            QMessageBox.warning(self, "警告", "服务器错误！", QMessageBox.Yes)



    @pyqtSlot()  # 退出，close()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        Dialog.close(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Dialog()
    mainWindow.show()
    sys.exit(app.exec_())