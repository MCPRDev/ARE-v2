# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_subject_subwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_subject_sub_window(object):
    def setupUi(self, add_subject_sub_window):
        add_subject_sub_window.setObjectName("add_subject_sub_window")
        add_subject_sub_window.resize(400, 156)
        add_subject_sub_window.setMinimumSize(QtCore.QSize(400, 156))
        add_subject_sub_window.setMaximumSize(QtCore.QSize(400, 156))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../GUI IMAGE/selection_management_window/staff_management_window/add_subjects_icon/open-book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label_2.setGeometry(QtCore.QRect(120, 40, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(add_subject_sub_window)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(add_subject_sub_window)
        self.pushButton.setGeometry(QtCore.QRect(70, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(add_subject_sub_window)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 100, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(add_subject_sub_window)
        QtCore.QMetaObject.connectSlotsByName(add_subject_sub_window)

    def retranslateUi(self, add_subject_sub_window):
        _translate = QtCore.QCoreApplication.translate
        add_subject_sub_window.setWindowTitle(_translate("add_subject_sub_window", "Agregar Nueva Materia"))
        self.label.setText(_translate("add_subject_sub_window", "Agregar Nueva Materia"))
        self.label_2.setText(_translate("add_subject_sub_window", "Ingresa el nombre de la materia:"))
        self.pushButton.setText(_translate("add_subject_sub_window", "Agregar"))
        self.pushButton_2.setText(_translate("add_subject_sub_window", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_subject_sub_window = QtWidgets.QWidget()
    ui = Ui_add_subject_sub_window()
    ui.setupUi(add_subject_sub_window)
    add_subject_sub_window.show()
    sys.exit(app.exec_())
