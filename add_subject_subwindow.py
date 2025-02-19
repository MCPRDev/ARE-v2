from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from functions import subject_gui_action


class Ui_add_subject_sub_window(object):
    def setupUi(self, add_subject_sub_window):
        add_subject_sub_window.setObjectName("add_subject_sub_window")
        add_subject_sub_window.resize(400, 156)
        add_subject_sub_window.setMinimumSize(QtCore.QSize(400, 156))
        add_subject_sub_window.setMaximumSize(QtCore.QSize(400, 156))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI IMAGE/selection_management_window/staff_management_window/add_subjects_icon/open-book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        add_subject_sub_window.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(add_subject_sub_window)
        self.label.setGeometry(QtCore.QRect(140, 20, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(add_subject_sub_window)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 170, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_input_subject = QtWidgets.QLineEdit(add_subject_sub_window)
        self.line_input_subject.setGeometry(QtCore.QRect(120, 60, 161, 20))
        self.line_input_subject.setObjectName("line_input_subject")
        self.button_add_subject = QtWidgets.QPushButton(add_subject_sub_window)
        self.button_add_subject.setGeometry(QtCore.QRect(70, 100, 75, 23))
        self.button_add_subject.setObjectName("button_add_subject")
        self.button_cancel_action = QtWidgets.QPushButton(add_subject_sub_window)
        self.button_cancel_action.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.button_cancel_action.setObjectName("button_cancel_action")

        self.button_add_subject.clicked.connect(self.add_subject_action_button)
        self.button_cancel_action.clicked.connect(add_subject_sub_window.close)

        self.subject_add_action = subject_gui_action()

        self.retranslateUi(add_subject_sub_window)
        QtCore.QMetaObject.connectSlotsByName(add_subject_sub_window)

    def add_subject_action_button(self):
        try:
            subject_name = str(self.line_input_subject.text()).lower().strip()

            if self.subject_add_action.add_subject_button_action(subject_name) == False:
                show_message_box = QMessageBox()
                show_message_box.setWindowTitle("Error")
                show_message_box.setIcon(QMessageBox.Critical)
                show_message_box.setText(f"El nombre de la materia {subject_name.capitalize()} ya existe.")
                x = show_message_box.exec_()
                self.line_input_subject.clear()
                return None
            
            show_message_box = QMessageBox()
            show_message_box.setWindowTitle("Agregada")
            show_message_box.setIcon(QMessageBox.Information)
            show_message_box.setText(f"Materia {subject_name.capitalize()} agregada")
            x = show_message_box.exec_()
            self.line_input_subject.clear()
            return True

        except Exception as e:
            print(f"Error adding subject: {e}")




    def retranslateUi(self, add_subject_sub_window):
        _translate = QtCore.QCoreApplication.translate
        add_subject_sub_window.setWindowTitle(_translate("add_subject_sub_window", "Agregar Nueva Materia"))
        self.label.setText(_translate("add_subject_sub_window", "Agregar Nueva Materia"))
        self.label_2.setText(_translate("add_subject_sub_window", "Ingresa el nombre de la materia:"))
        self.button_add_subject.setText(_translate("add_subject_sub_window", "Agregar"))
        self.button_cancel_action.setText(_translate("add_subject_sub_window", "Cancelar"))