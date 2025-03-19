from PyQt5 import QtCore, QtGui, QtWidgets
from staff_administration_panels import Ui_staff_management_window

class Ui_selection_management_window(object):
    def __init__(self, controller):
        self.Controller = controller

    def setupUi(self, selection_management_window):
        selection_management_window.setObjectName("selection_management_window")
        selection_management_window.resize(693, 168)
        selection_management_window.setMinimumSize(QtCore.QSize(693, 168))
        selection_management_window.setMaximumSize(QtCore.QSize(693, 168))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/gui/GUI IMAGE/selection_management_window/icon_window_selection_panel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selection_management_window.setWindowIcon(icon)
        self.selection_management_window = selection_management_window
        self.centralwidget = QtWidgets.QWidget(selection_management_window)
        self.centralwidget.setObjectName("centralwidget")
        self.staff_management_button = QtWidgets.QPushButton(self.centralwidget)
        self.staff_management_button.setGeometry(QtCore.QRect(20, 50, 211, 41))
        self.staff_management_button.setObjectName("staff_management_button")
        self.score_grade_management_button = QtWidgets.QPushButton(self.centralwidget)
        self.score_grade_management_button.setGeometry(QtCore.QRect(460, 50, 211, 41))
        self.score_grade_management_button.setObjectName("score_grade_management_button")
        self.student_management_button = QtWidgets.QPushButton(self.centralwidget)
        self.student_management_button.setGeometry(QtCore.QRect(240, 50, 211, 41))
        self.student_management_button.setObjectName("student_management_button")
        self.logout_button = QtWidgets.QPushButton(self.centralwidget)
        self.logout_button.setGeometry(QtCore.QRect(310, 120, 75, 23))
        self.logout_button.setObjectName("logout_button")
        selection_management_window.setCentralWidget(self.centralwidget)

        self.staff_administration_window = None

        self.staff_management_button.clicked.connect(self.staff_administration_window_open)
        self.logout_button.clicked.connect(self.handle_logout)
        
        self.retranslateUi(selection_management_window)
        QtCore.QMetaObject.connectSlotsByName(selection_management_window)

    def handle_logout(self):
        if self.Controller:
            self.Controller.show_login()
            self.selection_management_window.close()
            if self.staff_administration_window:
                self.staff_administration_window.close()

    
    def staff_administration_window_open(self):
        try:
            if self.staff_administration_window is None:
                self.staff_administration_window = QtWidgets.QMainWindow()
                self.ui_staff = Ui_staff_management_window() 
                self.ui_staff.setupUi(self.staff_administration_window)
            self.staff_administration_window.show()  
        except Exception as e:
            print(f"Error al abrir ventana de administracion de personal: {str(e)}")


    def retranslateUi(self, selection_management_window):
        _translate = QtCore.QCoreApplication.translate
        selection_management_window.setWindowTitle(_translate("selection_management_window", "Panel de seleccion"))
        self.staff_management_button.setToolTip(_translate("selection_management_window", "<html><head/><body><p><span style=\" font-size:9pt;\">Administracion de personal permite realizar las siguientes acciones:<br/></span></p><p><span style=\" font-size:9pt;\">- Agregar Personal</span></p><p><span style=\" font-size:9pt;\">- Modificar Personal</span></p><p><span style=\" font-size:9pt;\">- Eliminar Personal</span></p><p><span style=\" font-size:9pt;\">- Buscar Personal</span></p><p><span style=\" font-size:9pt;\">- Asignar Profesores</span></p><p><span style=\" font-size:9pt;\">- Asignar Grados Guiados a Profesores</span></p><p><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">- Administracion de accesos al software</span></p></body></html>"))
        self.staff_management_button.setText(_translate("selection_management_window", "Administracion de Personal"))
        self.score_grade_management_button.setText(_translate("selection_management_window", "Administracion de notas"))
        self.student_management_button.setText(_translate("selection_management_window", "Administracion de estudiantes"))
        self.logout_button.setText(_translate("selection_management_window", "Logout"))
