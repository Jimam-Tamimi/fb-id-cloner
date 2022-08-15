import platform
import os 
from cryptography.fernet import Fernet
from sys import exit

fernet = Fernet("QtL_rD8NiJvtEgknC8KMbS0l75sowlINBV-V3q3mwqA=".encode())

if os.path.exists("f3220fcc-62ec-4744-bd0e-52aacff1539d.txt"):
    with open("f3220fcc-62ec-4744-bd0e-52aacff1539d.txt", "r") as f:
        print()
        name = fernet.decrypt(f.read().encode())
        if(name.decode() != platform.node()):
            raise(Exception("This version of the software will not run on your computer. Please contact the seller."))
            
else:
    raise(Exception("Some files ar deleted. Please contact the seller for fix."))


from PyQt6 import QtCore, QtGui, QtWidgets

from main import quitAllWindow, run

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.allDrivers = []
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 130, 381, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.firstNum = QtWidgets.QLineEdit(self.widget)
        self.firstNum.setObjectName("firstNum")
        self.verticalLayout.addWidget(self.firstNum)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.secondNum = QtWidgets.QLineEdit(self.widget)
        self.secondNum.setObjectName("secondNum")
        self.verticalLayout_2.addWidget(self.secondNum)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.totalTabs = QtWidgets.QLineEdit(self.widget)
        self.totalTabs.setObjectName("totalTabs")
        self.verticalLayout_3.addWidget(self.totalTabs)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.totalAcccount = QtWidgets.QLineEdit(self.widget)
        self.totalAcccount.setObjectName("totalAcccount")
        self.verticalLayout_4.addWidget(self.totalAcccount)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.prefix = QtWidgets.QLineEdit(self.widget)
        self.prefix.setObjectName("prefix")
        self.verticalLayout_5.addWidget(self.prefix)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.newPass = QtWidgets.QLineEdit(self.widget)
        self.newPass.setObjectName("newPass")
        self.verticalLayout_6.addWidget(self.newPass)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.customPass = QtWidgets.QLineEdit(self.widget)
        self.customPass.setObjectName("customPass")
        self.verticalLayout_7.addWidget(self.customPass)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.passwordIndex = QtWidgets.QLineEdit(self.widget)
        self.passwordIndex.setText("0")
        self.passwordIndex.setObjectName("passwordIndex")
        self.verticalLayout_8.addWidget(self.passwordIndex)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        
        self.runBtn = QtWidgets.QPushButton(self.widget)
        self.runBtn.setObjectName("runBtn")

        self.runBtn.clicked.connect(self.runBtnClick)

        self.stopBtn = QtWidgets.QPushButton(self.widget)
        self.stopBtn.setObjectName("stopBtn")
        self.stopBtn.clicked.connect(lambda : quitAllWindow(self.allDrivers))
        
        
        self.verticalLayout_9.addWidget(self.runBtn)
        self.verticalLayout_9.addWidget(self.stopBtn)
        
        
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(200, 410, 351, 81))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setStyleSheet("background-color: #233DFF;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.totalAtempts = QtWidgets.QLabel(self.widget1)
        self.totalAtempts.setStyleSheet("color: rgb(35, 61, 255);\n"
"font-size: 14px;\n"
"font-weight: 600;")
        self.totalAtempts.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.totalAtempts.setObjectName("totalAtempts")
        self.verticalLayout_11.addWidget(self.totalAtempts)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setStyleSheet("background-color: #233DFF;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_12.addWidget(self.label_11)
        self.sccessFulAtmps = QtWidgets.QLabel(self.widget1)
        self.sccessFulAtmps.setStyleSheet("color: rgb(35, 61, 255);\n"
"font-size: 14px;\n"
"font-weight: 600;")
        self.sccessFulAtmps.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sccessFulAtmps.setObjectName("sccessFulAtmps")
        self.verticalLayout_12.addWidget(self.sccessFulAtmps)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        
    def runBtnClick(self):
        self.totalAtempts.setText("0")
        self.sccessFulAtmps.setText("0")

        self.allDrivers = run(int(self.firstNum.text()), int(self.secondNum.text()), int(self.totalTabs.text()), int(self.totalAcccount.text()), self.prefix.text(), self.newPass.text(), self.customPass.text(), int(self.passwordIndex.text()), self.changeAtmps, self.changeSuccessAtmps)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "First Number"))
        self.label_2.setText(_translate("MainWindow", "Second Number"))
        self.label_3.setText(_translate("MainWindow", "Total Tabs"))
        self.label_4.setText(_translate("MainWindow", "Total Acccount"))
        self.label_5.setText(_translate("MainWindow", "Prefix"))
        self.label_6.setText(_translate("MainWindow", "New Password"))
        self.label_7.setText(_translate("MainWindow", "Custom Password"))
        self.label_8.setText(_translate("MainWindow", "Password Index"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))

        self.label_9.setText(_translate("MainWindow", "Total Attempts"))
        self.totalAtempts.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Successful Attempts"))
        self.sccessFulAtmps.setText(_translate("MainWindow", "0"))
    
    def changeAtmps(self, count):
        self.totalAtempts.setText(str(int(self.totalAtempts.text()) + count))
    def changeSuccessAtmps(self, count):
        self.sccessFulAtmps.setText(str(int(self.sccessFulAtmps.text()) + count))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setMaximumHeight(650)
    MainWindow.setMaximumWidth(785)
    MainWindow.setMinimumHeight(600)
    MainWindow.setMinimumWidth(785)
    MainWindow.setWindowTitle("Majumder clone bot")
    MainWindow.setWindowIcon(QtGui.QIcon('C:/Users/Jimam Tamimi/Downloads/Majumder-Logo.ico'))
    MainWindow.show()
    sys.exit(app.exec())
