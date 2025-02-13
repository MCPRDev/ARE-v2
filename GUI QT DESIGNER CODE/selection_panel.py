from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_selection_management_window(object):
    def setupUi(self, selection_management_window):
        selection_management_window.setObjectName("selection_management_window")
        selection_management_window.resize(728, 168)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../GUI IMAGE/selection_management_window/icon_window_selection_panel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selection_management_window.setWindowIcon(icon)
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

        self.retranslateUi(selection_management_window)
        QtCore.QMetaObject.connectSlotsByName(selection_management_window)

    def retranslateUi(self, selection_management_window):
        _translate = QtCore.QCoreApplication.translate
        selection_management_window.setWindowTitle(_translate("selection_management_window", "Panel de seleccion"))
        self.staff_management_button.setToolTip(_translate("selection_management_window", "<html><head/><body><p><span style=\" font-size:9pt;\">Administracion de personal permite realizar las siguientes acciones:<br/></span></p><p><span style=\" font-size:9pt;\">- Agregar Personal</span></p><p><span style=\" font-size:9pt;\">- Modificar Personal</span></p><p><span style=\" font-size:9pt;\">- Eliminar Personal</span></p><p><span style=\" font-size:9pt;\">- Mostrar Personal</span></p><p><span style=\" font-size:9pt;\">- Asignar Profesores</span></p><p><span style=\" font-size:9pt;\">- Asignar Grados Guiados a Profesores</span></p><p><span style=\" font-size:9pt; font-weight:600; text-decoration: underline;\">- Administracion de accesos al software</span></p></body></html>"))
        self.staff_management_button.setText(_translate("selection_management_window", "Administracion de Personal"))
        self.score_grade_management_button.setText(_translate("selection_management_window", "Administracion de notas"))
        self.student_management_button.setText(_translate("selection_management_window", "Administracion de estudiantes"))
        self.logout_button.setText(_translate("selection_management_window", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selection_management_window = QtWidgets.QMainWindow()
    ui = Ui_selection_management_window()
    ui.setupUi(selection_management_window)
    selection_management_window.show()
    sys.exit(app.exec_())
