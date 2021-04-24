import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QDesktopWidget
from PyQt5.uic import loadUi
import pyrebase

firebaseConfig = {'apiKey': "AIzaSyBQybhg3tUjctlSKEO7qpayI2pqwuOuZ9A",
                  'authDomain': "collegecredentials-94bff.firebaseapp.com",
                  'databaseURL': "https://collegecredentials-94bff-default-rtdb.firebaseio.com",
                  'projectId': "collegecredentials-94bff",
                  'storageBucket': "collegecredentials-94bff.appspot.com",
                  'messagingSenderId': "1054406150324",
                  'appId': "1:1054406150324:web:d209cac50c9055981cafe1",
                  'measurementId': "G-8KTKNHDP32"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class MainLogin(QDialog):

    def __init__(self):
        super(MainLogin, self).__init__()
        loadUi("login.ui", self)
        self.mainloginbutton.clicked.connect(self.enterLogin)

    def enterLogin(self):
        enter = Login()
        widget.addWidget(enter)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("verify.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.back.clicked.connect(self.backtologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in with email", email, "and password", password)
            self.invalid.setVisible(False)
            self.openportal()

        except:
            print("invalid credentials")
            self.invalid.setVisible(True)

    def openportal(self):
        exam = ExamPortal()
        widget.addWidget(exam)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def backtologin(self):
        back = MainLogin()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class ExamPortal(QDialog):
    def __init__(self):
        super(ExamPortal, self).__init__()
        loadUi("afterlogin.ui", self)
        self.launchexambtn.clicked.connect(self.questionpage)
        self.backtologin.clicked.connect(self.dontlaunch)

    def questionpage(self):
        ques = Questions()
        widget.addWidget(ques)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def dontlaunch(self):
        dont = MainLogin()
        widget.addWidget(dont)
        widget.setCurrentIndex(widget.currentIndex() + 1)

a=[]
b=[]
class Questions(QDialog):
    def __init__(self):
        super(Questions, self).__init__()
        loadUi("question1.ui", self)
        self.next2.clicked.connect(self.page2)
        self.next2.clicked.connect(self.go)
        self.a1.clicked.connect(self.checka)
        self.b1.clicked.connect(self.checkb)
        self.c1.clicked.connect(self.checkc)
        self.d1.clicked.connect(self.checkd)


    def checka(self):
        a.append(0)
    def checkb(self):
        a.append(2)
    def checkc(self):
        a.append(0)
    def checkd(self):
        a.append(0)
    def go(self):
        tet= Marks()
        tet.mark()


    def page2(self):
        page2 = Question2()
        widget.addWidget(page2)
        widget.setCurrentIndex(widget.currentIndex() + 1)





class Question2(QDialog):
    def __init__(self):
        super(Question2, self).__init__()
        loadUi("question2.ui", self)
        self.next3.clicked.connect(self.page3)
        self.next3.clicked.connect(self.go)
        self.a2.clicked.connect(self.checka)
        self.b2.clicked.connect(self.checkb)
        self.c2.clicked.connect(self.checkc)
        self.d2.clicked.connect(self.checkd)

    def checka(self):
        a.append(2)
    def checkb(self):
        a.append(0)
    def checkc(self):
        a.append(0)
    def checkd(self):
        a.append(0)
    def go(self):
        tet = Marks()
        tet.mark()
    def page3(self):
        page3 = Question3()
        widget.addWidget(page3)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Question3(QDialog):
    def __init__(self):
        super(Question3, self).__init__()
        loadUi("question3.ui", self)
        self.submitbutton.clicked.connect(self.thanks)
        self.submitbutton.clicked.connect(self.go)
        self.submitbutton.clicked.connect(self.results)
        self.a3.clicked.connect(self.checka)
        self.b3.clicked.connect(self.checkb)
        self.c3.clicked.connect(self.checkc)
        self.d3.clicked.connect(self.checkd)

    def checka(self):
        a.append(2)

    def checkb(self):
        a.append(0)

    def checkc(self):
        a.append(0)

    def checkd(self):
        a.append(0)

    def go(self):
        tet = Marks()
        tet.mark()

    def results(self):
        add= Marks()
        add.addmarks()

    def thanks(self):
        thanks = Thankyoupage()
        widget.addWidget(thanks)
        widget.setCurrentIndex(widget.currentIndex() + 1)






class Marks(object):
    def mark(self):
        length=len(a)
        marks=a[length-1]
        b.append(marks)
    def addmarks(self):
        Sum=sum(b)
        print("The mark is ", Sum)
        return Sum




class Thankyoupage(QDialog):
    def __init__(self):
        super(Thankyoupage, self).__init__()
        loadUi("thanks.ui", self)
        self.exit.clicked.connect(self.exitout)
        self.exit.clicked.connect(self.erase)
        self.result.clicked.connect(self.showmarks)

    def showmarks(self):
        add = Marks()
        c=add.addmarks()
        d=str(c)
        self.display.setText("Your Mark is  "+ d)


    def exitout(self):
        exitout = MainLogin()
        widget.addWidget(exitout)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def erase(self):
        b.clear()



app = QApplication(sys.argv)
window = MainLogin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(window)
widget.setFixedHeight(480)
widget.setFixedWidth(640)
widget.show()
app.exec_()
