from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from functions import loggin_gui_action
from selection_panel_window import Ui_selection_management_window

class Ui_login_windows(object):
    def setupUi(self, login_windows):
        login_windows.setObjectName("login_windows")
        login_windows.setEnabled(True)
        login_windows.resize(600, 315)
        login_windows.setMinimumSize(QtCore.QSize(600, 315))
        login_windows.setMaximumSize(QtCore.QSize(600, 315))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI IMAGE/login_windows_images/login_icon_window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_windows.setWindowIcon(icon)
        login_windows.setToolTip("")
        login_windows.setDocumentMode(False)
        self.login_windows = login_windows
        self.centralwidget = QtWidgets.QWidget(login_windows)
        self.centralwidget.setObjectName("centralwidget")
        self.login_icon_user = QtWidgets.QLabel(self.centralwidget)
        self.login_icon_user.setGeometry(QtCore.QRect(250, 40, 71, 71))
        self.login_icon_user.setAutoFillBackground(False)
        self.login_icon_user.setText("")
        self.login_icon_user.setPixmap(QtGui.QPixmap("GUI IMAGE/login_windows_images/login_icon_user.png"))
        self.login_icon_user.setScaledContents(True)
        self.login_icon_user.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.login_icon_user.setObjectName("login_icon_user")
        self.ARE_login_text_top = QtWidgets.QLabel(self.centralwidget)
        self.ARE_login_text_top.setGeometry(QtCore.QRect(225, 0, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ARE_login_text_top.setFont(font)
        self.ARE_login_text_top.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.ARE_login_text_top.setTextFormat(QtCore.Qt.AutoText)
        self.ARE_login_text_top.setScaledContents(False)
        self.ARE_login_text_top.setAlignment(QtCore.Qt.AlignCenter)
        self.ARE_login_text_top.setObjectName("ARE_login_text_top")
        self.username_login_text = QtWidgets.QLabel(self.centralwidget)
        self.username_login_text.setGeometry(QtCore.QRect(130, 150, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.username_login_text.setFont(font)
        self.username_login_text.setObjectName("username_login_text")
        self.password_login_text = QtWidgets.QLabel(self.centralwidget)
        self.password_login_text.setGeometry(QtCore.QRect(130, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria Math")
        font.setPointSize(12)
        self.password_login_text.setFont(font)
        self.password_login_text.setObjectName("password_login_text")
        self.line_input_user = QtWidgets.QLineEdit(self.centralwidget)
        self.line_input_user.setGeometry(QtCore.QRect(210, 150, 181, 20))
        self.line_input_user.setAutoFillBackground(False)
        self.line_input_user.setObjectName("line_input_user")
        self.line_input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.line_input_password.setGeometry(QtCore.QRect(210, 190, 181, 20))
        self.line_input_password.setAutoFillBackground(False)
        self.line_input_password.setObjectName("line_input_password")
        self.Exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.Exit_button.setGeometry(QtCore.QRect(130, 240, 81, 31))
        self.Exit_button.setObjectName("Exit_button")
        self.Login_button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_button.setGeometry(QtCore.QRect(340, 240, 81, 31))
        self.Login_button.setObjectName("Login_button")
        login_windows.setCentralWidget(self.centralwidget)

        self.retranslateUi(login_windows)
        QtCore.QMetaObject.connectSlotsByName(login_windows)

        self.log_actions = loggin_gui_action()

        self.Exit_button.clicked.connect(self.exit_login)
        self.Login_button.clicked.connect(self.login)
    
    def exit_login(self):
        exit()
        return True
    
    def login(self):
        try:

            username = str(self.line_input_user.text()).lower().strip()
            password = str(self.line_input_password.text()).lower().strip()
            
            success, access_type = self.log_actions.log_button_action(username, password)

            if not success:
                self.line_input_user.clear()
                self.line_input_password.clear()
                show_message_box = QMessageBox()
                show_message_box.setWindowTitle("Error")
                show_message_box.setIcon(QMessageBox.Critical)
                show_message_box.setText("Error Invalid username or password")

                x = show_message_box.exec_()
                return False
            
            match access_type: #Here we check what kind of access has the user logging in
                case 0:
                    self.login_windows.close()
                    self.start_selection_panels()

                    login_success = QMessageBox()
                    login_success.setIcon(QMessageBox.Information)
                    login_success.setText("Success Login successful as Administrator (All Permissions granted)")

                    x = login_success.exec_()
                    return False, access_type
                case 1:
                    self.login_windows.close()
                    self.start_selection_panels()

                    login_success = QMessageBox()
                    login_success.setIcon(QMessageBox.Information)
                    login_success.setText("Success Login successful as Administrator")

                    x = login_success.exec_()
                    return False, access_type
                case 2:
                    login_success = QMessageBox()
                    login_success.setIcon(QMessageBox.Information)
                    login_success.setText("Success Login successful as Teacher [In progress]")

                    x = login_success.exec_()
                    return False, access_type
                case 3:
                    login_success = QMessageBox()
                    login_success.setIcon(QMessageBox.Advertisement)
                    login_success.setText("No Login Successfully, no permission granted")

                    x = login_success.exec_()
                    return False, None
                case _:
                    login_success = QMessageBox()
                    login_success.setIcon(QMessageBox.Warning)
                    login_success.setText("No Login Successfully, wrong username or password")
                    
                    x = login_success.exec_()
                    return False, None
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
    
    def start_selection_panels(self):
            self.selection_panels = QtWidgets.QMainWindow()
            self.ui_panels = Ui_selection_management_window() 
            self.ui_panels.setupUi(self.selection_panels)
            self.selection_panels.show()  

        
    def retranslateUi(self, login_windows):
        _translate = QtCore.QCoreApplication.translate
        login_windows.setWindowTitle(_translate("login_windows", "ARE Login"))
        self.ARE_login_text_top.setText(_translate("login_windows", "ARE Login"))
        self.username_login_text.setText(_translate("login_windows", "Username"))
        self.password_login_text.setText(_translate("login_windows", "Password"))
        self.Exit_button.setText(_translate("login_windows", "Exit"))
        self.Login_button.setText(_translate("login_windows", "Login"))