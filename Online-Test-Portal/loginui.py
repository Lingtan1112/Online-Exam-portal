# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("Background:      #2c3e50 ")
        self.mainloginbutton = QtWidgets.QPushButton(Dialog)
        self.mainloginbutton.setGeometry(QtCore.QRect(270, 220, 121, 51))
        self.mainloginbutton.setAutoFillBackground(False)
        self.mainloginbutton.setStyleSheet("color:Black;\n"
"font: 9pt \"Nemesis Grant\";\n"
"\n"
"background:#9FE2BF;\n"
"font-size:22;\n"
"\n"
"")
        self.mainloginbutton.setDefault(False)
        self.mainloginbutton.setFlat(False)
        self.mainloginbutton.setObjectName("mainloginbutton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 571, 71))
        self.label.setStyleSheet("background:#9FE2BF;\n"
"font: 57 12pt \"OldSansBlack\";\n"
"margin: auto;\n"
"  width: 50%;\n"
"  border: 40px solid #9FE2BF;\n"
"  padding: 10px;\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.mainloginbutton.setText(_translate("Dialog", "LOGIN"))
        self.label.setText(_translate("Dialog", "SARANATHAN COLLEGE OF ENGINEERING\n"
"EXAM PORTAL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
