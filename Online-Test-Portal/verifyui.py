# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verify.ui'
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
        self.loginbutton = QtWidgets.QPushButton(Dialog)
        self.loginbutton.setGeometry(QtCore.QRect(270, 270, 121, 51))
        self.loginbutton.setAutoFillBackground(False)
        self.loginbutton.setStyleSheet("color:Black;\n"
                                       "font: 9pt \"Nemesis Grant\";\n"
                                       "\n"
                                       "background:#9FE2BF;\n"
                                       "font-size:22;\n"
                                       "\n"
                                       "")
        self.loginbutton.setDefault(False)
        self.loginbutton.setFlat(False)
        self.loginbutton.setObjectName("loginbutton")
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 170, 81, 21))
        self.label_2.setStyleSheet("color:#9FE2BF;;\n"
                                   "\n"
                                   "font: 63 8pt \"Bahnschrift SemiBold\";\n"
                                   "background-color:\n"
                                   "\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 210, 81, 16))
        self.label_3.setStyleSheet("color:#9FE2BF;;\n"
                                   "font: 63 8pt \"Bahnschrift SemiBold\";\n"
                                   "\n"
                                   "\n"
                                   "")
        self.label_3.setObjectName("label_3")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(240, 170, 181, 22))
        self.email.setStyleSheet("color:#9FE2BF;;")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(240, 210, 181, 22))
        self.password.setStyleSheet("color:white;\n"
                                    "")
        self.password.setObjectName("password")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(270, 330, 121, 31))
        self.back.setAutoFillBackground(False)
        self.back.setStyleSheet("color:Black;\n"
                                "font: 9pt \"Nemesis Grant\";\n"
                                "\n"
                                "background:#9FE2BF;\n"
                                "font-size:22;\n"
                                "\n"
                                "")
        self.back.setDefault(False)
        self.back.setFlat(False)
        self.back.setObjectName("back")
        self.invalid = QtWidgets.QLabel(Dialog)
        self.invalid.setGeometry(QtCore.QRect(280, 250, 121, 16))
        self.invalid.setStyleSheet("color:#e5383b;\n"
                                   "")
        self.invalid.setObjectName("invalid")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Exam portal", "Exam portal"))
        self.loginbutton.setText(_translate("Dialog", "LOGIN"))
        self.label.setText(_translate("Dialog", "SARANATHAN COLLEGE OF ENGINEERING\n"
                                                "EXAM PORTAL"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.back.setText(_translate("Dialog", "Back"))
        self.invalid.setText(_translate("Dialog", "invalid credentials"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
