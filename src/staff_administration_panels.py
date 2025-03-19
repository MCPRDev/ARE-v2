from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QWidget, QListWidget, QMessageBox, QMenu
from PyQt5.QtCore import QDate, Qt
from add_subject_subwindow import Ui_add_subject_sub_window
from query import *
from outfuctions import *
from functions import *
from datetime import date, time
import sys
import traceback

class Ui_staff_management_window(object):
    def setupUi(self, staff_management_window):
        staff_management_window.setObjectName("staff_management_window")
        staff_management_window.resize(1215, 690)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(staff_management_window.sizePolicy().hasHeightForWidth())
        staff_management_window.setSizePolicy(sizePolicy)
        staff_management_window.setMinimumSize(QtCore.QSize(1215, 690))
        staff_management_window.setMaximumSize(QtCore.QSize(1215, 690))
        staff_management_window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/gui/GUI IMAGE/selection_management_window/staff_management_window/staff_management_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        staff_management_window.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(staff_management_window)
        self.centralwidget.setObjectName("centralwidget")
        self.main_central_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.main_central_widget.setGeometry(QtCore.QRect(0, 0, 1215, 690))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_central_widget.sizePolicy().hasHeightForWidth())
        self.main_central_widget.setSizePolicy(sizePolicy)
        self.main_central_widget.setMinimumSize(QtCore.QSize(1215, 690))
        self.main_central_widget.setMaximumSize(QtCore.QSize(1215, 690))
        self.main_central_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_central_widget.setDocumentMode(False)
        self.main_central_widget.setTabsClosable(False)
        self.main_central_widget.setMovable(False)
        self.main_central_widget.setTabBarAutoHide(False)
        self.main_central_widget.setObjectName("main_central_widget")
        self.Materias = QtWidgets.QWidget()
        self.Materias.setObjectName("Materias")
        self.frame_subject = QtWidgets.QFrame(self.Materias)
        self.frame_subject.setGeometry(QtCore.QRect(0, 0, 1201, 661))
        self.frame_subject.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_subject.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_subject.setObjectName("frame_subject")
        self.tablew_subject_show = QtWidgets.QTableWidget(self.frame_subject)
        self.tablew_subject_show.setGeometry(QtCore.QRect(440, 90, 321, 421))
        self.tablew_subject_show.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tablew_subject_show.setAutoFillBackground(False)
        self.tablew_subject_show.setShowGrid(True)
        self.tablew_subject_show.setGridStyle(QtCore.Qt.NoPen)
        self.tablew_subject_show.setWordWrap(True)
        self.tablew_subject_show.setCornerButtonEnabled(True)
        self.tablew_subject_show.setObjectName("tablew_subject_show")
        self.tablew_subject_show.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tablew_subject_show.setColumnCount(2)
        self.tablew_subject_show.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tablew_subject_show.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tablew_subject_show.setHorizontalHeaderItem(1, item)
        self.tablew_subject_show.horizontalHeader().setVisible(True)
        self.tablew_subject_show.horizontalHeader().setCascadingSectionResizes(False)
        self.tablew_subject_show.horizontalHeader().setHighlightSections(True)
        self.tablew_subject_show.verticalHeader().setVisible(False)
        self.tablew_subject_show.verticalHeader().setHighlightSections(True)
        self.tablew_subject_show.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tablew_subject_show.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablew_subject_show.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label_subject_search = QtWidgets.QLabel(self.frame_subject)
        self.label_subject_search.setGeometry(QtCore.QRect(550, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_subject_search.setFont(font)
        self.label_subject_search.setObjectName("label_subject_search")
        self.lineedit_search_subject_id = QtWidgets.QLineEdit(self.frame_subject)
        self.lineedit_search_subject_id.setGeometry(QtCore.QRect(700, 60, 61, 20))
        self.lineedit_search_subject_id.setText("")
        self.lineedit_search_subject_id.setFrame(True)
        self.lineedit_search_subject_id.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineedit_search_subject_id.setClearButtonEnabled(False)
        self.lineedit_search_subject_id.setObjectName("lineedit_search_subject_id")
        self.frame_buttons_subjects = QtWidgets.QFrame(self.frame_subject)
        self.frame_buttons_subjects.setGeometry(QtCore.QRect(420, 520, 366, 43))
        self.frame_buttons_subjects.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons_subjects.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons_subjects.setObjectName("frame_buttons_subjects")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_buttons_subjects)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_delete_subject = QtWidgets.QPushButton(self.frame_buttons_subjects)
        self.button_delete_subject.setObjectName("button_delete_subject")
        self.button_delete_subject.setEnabled(False)
        self.horizontalLayout.addWidget(self.button_delete_subject)
        self.button_edit_subject = QtWidgets.QPushButton(self.frame_buttons_subjects)
        self.button_edit_subject.setObjectName("button_edit_subject")
        self.horizontalLayout.addWidget(self.button_edit_subject)
        self.button_edit_subject.setEnabled(False)
        self.button_add_subject = QtWidgets.QPushButton(self.frame_buttons_subjects)
        self.button_add_subject.setObjectName("button_add_subject")
        self.horizontalLayout.addWidget(self.button_add_subject)
        self.lineedit_search_subject_name = QtWidgets.QLineEdit(self.frame_subject)
        self.lineedit_search_subject_name.setGeometry(QtCore.QRect(440, 60, 151, 20))
        self.lineedit_search_subject_name.setText("")
        self.lineedit_search_subject_name.setFrame(True)
        self.lineedit_search_subject_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineedit_search_subject_name.setClearButtonEnabled(False)
        self.lineedit_search_subject_name.setObjectName("lineedit_search_subject_name")
        self.label_subject_search_name = QtWidgets.QLabel(self.frame_subject)
        self.label_subject_search_name.setGeometry(QtCore.QRect(470, 40, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_subject_search_name.setFont(font)
        self.label_subject_search_name.setObjectName("label_subject_search_name")
        self.label_subject_search_name_2 = QtWidgets.QLabel(self.frame_subject)
        self.label_subject_search_name_2.setGeometry(QtCore.QRect(700, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_subject_search_name_2.setFont(font)
        self.label_subject_search_name_2.setObjectName("label_subject_search_name_2")
        self.main_central_widget.addTab(self.Materias, "")
        self.add_staff_widget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_staff_widget.sizePolicy().hasHeightForWidth())
        self.add_staff_widget.setSizePolicy(sizePolicy)
        self.add_staff_widget.setObjectName("add_staff_widget")
        self.frame_entry_data_add_staff = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_entry_data_add_staff.setGeometry(QtCore.QRect(0, 0, 671, 161))
        self.frame_entry_data_add_staff.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_entry_data_add_staff.setObjectName("frame_entry_data_add_staff")
        self.label_fname = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_fname.setGeometry(QtCore.QRect(10, 20, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fname.setFont(font)
        self.label_fname.setObjectName("label_fname")
        self.label_sname = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_sname.setGeometry(QtCore.QRect(10, 50, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_sname.setFont(font)
        self.label_sname.setObjectName("label_sname")
        self.line_input_fname = QtWidgets.QLineEdit(self.frame_entry_data_add_staff)
        self.line_input_fname.setGeometry(QtCore.QRect(140, 20, 181, 20))
        self.line_input_fname.setObjectName("line_input_fname")
        self.line_input_sname = QtWidgets.QLineEdit(self.frame_entry_data_add_staff)
        self.line_input_sname.setGeometry(QtCore.QRect(140, 50, 181, 20))
        self.line_input_sname.setObjectName("line_input_sname")
        self.label_fsurname = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_fsurname.setGeometry(QtCore.QRect(10, 80, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_fsurname.setFont(font)
        self.label_fsurname.setObjectName("label_fsurname")
        self.label_ssurname = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_ssurname.setGeometry(QtCore.QRect(10, 110, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_ssurname.setFont(font)
        self.label_ssurname.setObjectName("label_ssurname")
        self.line_input_fsurname = QtWidgets.QLineEdit(self.frame_entry_data_add_staff)
        self.line_input_fsurname.setGeometry(QtCore.QRect(140, 80, 181, 20))
        self.line_input_fsurname.setObjectName("line_input_fsurname")
        self.line_input_ssurname = QtWidgets.QLineEdit(self.frame_entry_data_add_staff)
        self.line_input_ssurname.setGeometry(QtCore.QRect(140, 110, 181, 20))
        self.line_input_ssurname.setObjectName("line_input_ssurname")
        self.label_document_id = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_document_id.setGeometry(QtCore.QRect(340, 20, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_document_id.setFont(font)
        self.label_document_id.setObjectName("label_document_id")
        self.line_input_document_id = QtWidgets.QLineEdit(self.frame_entry_data_add_staff)
        self.line_input_document_id.setGeometry(QtCore.QRect(480, 20, 181, 20))
        self.line_input_document_id.setObjectName("line_input_document_id")
        self.label_address = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_address.setGeometry(QtCore.QRect(340, 50, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_address.setFont(font)
        self.label_address.setObjectName("label_address")
        self.line_input_phone_number = QtWidgets.QLineEdit(self.frame_entry_data_add_staff)
        self.line_input_phone_number.setGeometry(QtCore.QRect(480, 80, 181, 20))
        self.line_input_phone_number.setObjectName("line_input_phone_number")
        self.label_phone = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_phone.setGeometry(QtCore.QRect(340, 80, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.line_input_address = QtWidgets.QLineEdit(self.frame_entry_data_add_staff)
        self.line_input_address.setGeometry(QtCore.QRect(480, 50, 181, 20))
        self.line_input_address.setObjectName("line_input_address")
        self.label_birthdate = QtWidgets.QLabel(self.frame_entry_data_add_staff)
        self.label_birthdate.setGeometry(QtCore.QRect(340, 110, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_birthdate.setFont(font)
        self.label_birthdate.setObjectName("label_birthdate")
        self.birthdate_input_get = QtWidgets.QDateEdit(self.frame_entry_data_add_staff)
        self.birthdate_input_get.setGeometry(QtCore.QRect(480, 110, 110, 22))
        self.birthdate_input_get.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.birthdate_input_get.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Nicaragua))
        self.birthdate_input_get.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.birthdate_input_get.setCalendarPopup(True)
        self.birthdate_input_get.setObjectName("birthdate_input_get")
        self.line_input_ssurname.raise_()
        self.birthdate_input_get.raise_()
        self.birthdate_input_get.setDate(QDate.currentDate())
        self.label_ssurname.raise_()
        self.line_input_document_id.raise_()
        self.label_fname.raise_()
        self.line_input_fname.raise_()
        self.line_input_phone_number.raise_()
        self.label_document_id.raise_()
        self.line_input_address.raise_()
        self.label_phone.raise_()
        self.label_sname.raise_()
        self.label_birthdate.raise_()
        self.line_input_fsurname.raise_()
        self.label_fsurname.raise_()
        self.line_input_sname.raise_()
        self.label_address.raise_()
        self.frame_selection_data_add_staff = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_selection_data_add_staff.setGeometry(QtCore.QRect(670, 0, 251, 161))
        self.frame_selection_data_add_staff.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_selection_data_add_staff.setObjectName("frame_selection_data_add_staff")
        self.combox_job_id_selection = QtWidgets.QComboBox(self.frame_selection_data_add_staff)
        self.combox_job_id_selection.setGeometry(QtCore.QRect(10, 40, 131, 22))
        self.combox_job_id_selection.setObjectName("combox_job_id_selection")
        self.combox_job_id_selection.addItem("")
        self.combox_job_id_selection.addItem("")
        self.combox_job_id_selection.addItem("")
        self.combox_job_id_selection.addItem("")
        self.label_job_selection = QtWidgets.QLabel(self.frame_selection_data_add_staff)
        self.label_job_selection.setGeometry(QtCore.QRect(10, 20, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_job_selection.setFont(font)
        self.label_job_selection.setObjectName("label_job_selection")
        self.frame_teacher_selection = QtWidgets.QFrame(self.frame_selection_data_add_staff)
        self.frame_teacher_selection.setGeometry(QtCore.QRect(0, 60, 251, 101))
        self.frame_teacher_selection.setObjectName("frame_teacher_selection")
        self.cb_highschool_teacher = QtWidgets.QCheckBox(self.frame_teacher_selection)
        self.cb_highschool_teacher.setGeometry(QtCore.QRect(10, 10, 131, 17))
        self.cb_highschool_teacher.setObjectName("cb_highschool_teacher")
        self.cb_assign_grade = QtWidgets.QCheckBox(self.frame_teacher_selection)
        self.cb_assign_grade.setGeometry(QtCore.QRect(10, 70, 91, 17))
        self.cb_assign_grade.setObjectName("cb_assign_grade")
        self.cb_assign_subject = QtWidgets.QCheckBox(self.frame_teacher_selection)
        self.cb_assign_subject.setGeometry(QtCore.QRect(10, 40, 141, 17))
        self.cb_assign_subject.setObjectName("cb_assign_subject")
        self.frame_assign_grade = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_assign_grade.setGeometry(QtCore.QRect(0, 160, 201, 331))
        self.frame_assign_grade.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_assign_grade.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_assign_grade.setObjectName("frame_assign_grade")
        self.qlistw_grade_assign = QtWidgets.QListWidget(self.frame_assign_grade)
        self.qlistw_grade_assign.setGeometry(QtCore.QRect(10, 30, 181, 291))
        self.qlistw_grade_assign.setObjectName("qlistw_grade_assign")
        self.info_grade_assign = QtWidgets.QLabel(self.frame_assign_grade)
        self.info_grade_assign.setGeometry(QtCore.QRect(10, 10, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.info_grade_assign.setFont(font)
        self.info_grade_assign.setObjectName("info_grade_assign")
        self.frame_assign_subject = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_assign_subject.setGeometry(QtCore.QRect(201, 161, 211, 331))
        self.frame_assign_subject.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_assign_subject.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_assign_subject.setObjectName("frame_assign_subject")
        self.info_grade_subject = QtWidgets.QLabel(self.frame_assign_subject)
        self.info_grade_subject.setGeometry(QtCore.QRect(20, 10, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.info_grade_subject.setFont(font)
        self.info_grade_subject.setObjectName("info_grade_subject")
        self.qlistw_subject_assign = QtWidgets.QListWidget(self.frame_assign_subject)
        self.qlistw_subject_assign.setGeometry(QtCore.QRect(10, 30, 191, 291))
        self.qlistw_subject_assign.setObjectName("qlistw_subject_assign")
        self.frame_multi_selection_subjects = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_multi_selection_subjects.setGeometry(QtCore.QRect(411, 161, 221, 331))
        self.frame_multi_selection_subjects.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_multi_selection_subjects.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_multi_selection_subjects.setObjectName("frame_multi_selection_subjects")
        self.qlistw_subject_selection = QtWidgets.QListWidget(self.frame_multi_selection_subjects)
        self.qlistw_subject_selection.setGeometry(QtCore.QRect(20, 30, 191, 291))
        self.qlistw_subject_selection.setObjectName("qlistw_subject_selection")
        self.qlistw_subject_selection.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.info_subjects_selection = QtWidgets.QLabel(self.frame_multi_selection_subjects)
        self.info_subjects_selection.setGeometry(QtCore.QRect(50, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.info_subjects_selection.setFont(font)
        self.info_subjects_selection.setObjectName("info_subjects_selection")
        self.frame_grades_assigned = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_grades_assigned.setGeometry(QtCore.QRect(630, 160, 211, 331))
        self.frame_grades_assigned.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_grades_assigned.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_grades_assigned.setObjectName("frame_grades_assigned")
        self.qlistw_grades_impart_selection = QtWidgets.QListWidget(self.frame_grades_assigned)
        self.qlistw_grades_impart_selection.setGeometry(QtCore.QRect(10, 30, 191, 291))
        self.qlistw_grades_impart_selection.setObjectName("qlistw_grades_impart_selection")
        self.qlistw_grades_impart_selection.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.info_grades_multiselections = QtWidgets.QLabel(self.frame_grades_assigned)
        self.info_grades_multiselections.setGeometry(QtCore.QRect(30, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.info_grades_multiselections.setFont(font)
        self.info_grades_multiselections.setObjectName("info_grades_multiselections")
        self.frame_buttons = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_buttons.setGeometry(QtCore.QRect(920, 0, 291, 161))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_buttons.setObjectName("frame_buttons")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_buttons)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_clean_information = QtWidgets.QPushButton(self.frame_buttons)
        self.button_clean_information.setObjectName("button_clean_information")
        self.verticalLayout.addWidget(self.button_clean_information)
        self.button_save_information_add_staff = QtWidgets.QPushButton(self.frame_buttons)
        self.button_save_information_add_staff.setObjectName("button_save_information_add_staff")
        self.verticalLayout.addWidget(self.button_save_information_add_staff)
        self.button_gback = QtWidgets.QPushButton(self.frame_buttons)
        self.button_gback.setObjectName("button_gback")
        self.verticalLayout.addWidget(self.button_gback)
        self.frame_output_information_will_save = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_output_information_will_save.setGeometry(QtCore.QRect(-1, 489, 1211, 171))
        self.frame_output_information_will_save.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_output_information_will_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_output_information_will_save.setObjectName("frame_output_information_will_save")
        self.output_information_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.output_information_info.setGeometry(QtCore.QRect(10, 10, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.output_information_info.setFont(font)
        self.output_information_info.setObjectName("output_information_info")
        self.name_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.name_output_info.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name_output_info.setFont(font)
        self.name_output_info.setObjectName("name_output_info")
        self.surname_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.surname_output_info.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.surname_output_info.setFont(font)
        self.surname_output_info.setObjectName("surname_output_info")
        self.document_id_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.document_id_output_info.setGeometry(QtCore.QRect(10, 130, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.document_id_output_info.setFont(font)
        self.document_id_output_info.setObjectName("document_id_output_info")
        self.address_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.address_output_info.setGeometry(QtCore.QRect(10, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.address_output_info.setFont(font)
        self.address_output_info.setObjectName("address_output_info")
        self.phone_number_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.phone_number_output_info.setGeometry(QtCore.QRect(390, 40, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.phone_number_output_info.setFont(font)
        self.phone_number_output_info.setObjectName("phone_number_output_info")
        self.birthdate_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.birthdate_output_info.setGeometry(QtCore.QRect(390, 70, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.birthdate_output_info.setFont(font)
        self.birthdate_output_info.setObjectName("birthdate_output_info")
        self.edad_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.edad_output_info.setGeometry(QtCore.QRect(390, 100, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edad_output_info.setFont(font)
        self.edad_output_info.setObjectName("edad_output_info")
        self.grade_assign_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.grade_assign_output_info.setGeometry(QtCore.QRect(710, 70, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.grade_assign_output_info.setFont(font)
        self.grade_assign_output_info.setObjectName("grade_assign_output_info")
        self.subject_assign_output_info = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.subject_assign_output_info.setGeometry(QtCore.QRect(710, 40, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subject_assign_output_info.setFont(font)
        self.subject_assign_output_info.setObjectName("subject_assign_output_info")
        self.label_name_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_name_output.setGeometry(QtCore.QRect(80, 40, 301, 16))
        self.label_name_output.setText("")
        self.label_name_output.setObjectName("label_name_output")
        self.label_surname_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_surname_output.setGeometry(QtCore.QRect(80, 70, 301, 16))
        self.label_surname_output.setText("")
        self.label_surname_output.setObjectName("label_surname_output")
        self.label_address_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_address_output.setGeometry(QtCore.QRect(80, 100, 301, 16))
        self.label_address_output.setText("")
        self.label_address_output.setObjectName("label_address_output")
        self.label_document_id_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_document_id_output.setGeometry(QtCore.QRect(80, 130, 191, 16))
        self.label_document_id_output.setText("")
        self.label_document_id_output.setObjectName("label_document_id_output")
        self.label_phone_number_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_phone_number_output.setGeometry(QtCore.QRect(540, 40, 161, 16))
        self.label_phone_number_output.setText("")
        self.label_phone_number_output.setObjectName("label_phone_number_output")
        self.label_birthdate_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_birthdate_output.setGeometry(QtCore.QRect(540, 70, 161, 16))
        self.label_birthdate_output.setText("")
        self.label_birthdate_output.setObjectName("label_birthdate_output")
        self.label_age_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_age_output.setGeometry(QtCore.QRect(440, 100, 91, 16))
        self.label_age_output.setText("")
        self.label_age_output.setObjectName("label_age_output")
        self.label_subject_assign_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_subject_assign_output.setGeometry(QtCore.QRect(830, 40, 151, 16))
        self.label_subject_assign_output.setText("")
        self.label_subject_assign_output.setObjectName("label_subject_assign_output")
        self.label_grade_assign_output = QtWidgets.QLabel(self.frame_output_information_will_save)
        self.label_grade_assign_output.setGeometry(QtCore.QRect(830, 70, 111, 16))
        self.label_grade_assign_output.setText("")
        self.label_grade_assign_output.setObjectName("label_grade_assign_output")
        self.frame_confirmation_buttons = QtWidgets.QFrame(self.frame_output_information_will_save)
        self.frame_confirmation_buttons.setGeometry(QtCore.QRect(1029, -1, 171, 171))
        self.frame_confirmation_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_confirmation_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_confirmation_buttons.setObjectName("frame_confirmation_buttons")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_confirmation_buttons)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_confirm_information_add_staff = QtWidgets.QPushButton(self.frame_confirmation_buttons)
        self.button_confirm_information_add_staff.setObjectName("button_confirm_information_add_staff")
        self.verticalLayout_2.addWidget(self.button_confirm_information_add_staff)
        self.button_cancelar_information_add_staff = QtWidgets.QPushButton(self.frame_confirmation_buttons)
        self.button_cancelar_information_add_staff.setObjectName("button_cancelar_information_add_staff")
        self.verticalLayout_2.addWidget(self.button_cancelar_information_add_staff)
        self.frame_output_information_grade_subject = QtWidgets.QFrame(self.add_staff_widget)
        self.frame_output_information_grade_subject.setGeometry(QtCore.QRect(839, 159, 361, 331))
        self.frame_output_information_grade_subject.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_output_information_grade_subject.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_output_information_grade_subject.setObjectName("frame_output_information_grade_subject")
        self.qlistw_selected_subjects = QtWidgets.QListWidget(self.frame_output_information_grade_subject)
        self.qlistw_selected_subjects.setGeometry(QtCore.QRect(30, 31, 131, 291))
        self.qlistw_selected_subjects.setObjectName("qlistw_selected_subjects")
        self.label_output_subjects = QtWidgets.QLabel(self.frame_output_information_grade_subject)
        self.label_output_subjects.setGeometry(QtCore.QRect(40, 10, 111, 20))
        self.label_output_subjects.setObjectName("label_output_subjects")
        self.qlistw_selected_grade = QtWidgets.QListWidget(self.frame_output_information_grade_subject)
        self.qlistw_selected_grade.setGeometry(QtCore.QRect(210, 30, 131, 291))
        self.qlistw_selected_grade.setObjectName("qlistw_selected_grade")
        self.label_output_grades = QtWidgets.QLabel(self.frame_output_information_grade_subject)
        self.label_output_grades.setGeometry(QtCore.QRect(220, 10, 111, 20))
        self.label_output_grades.setObjectName("label_output_grades")
        self.main_central_widget.addTab(self.add_staff_widget, "")
        self.edit_staff_widget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_staff_widget.sizePolicy().hasHeightForWidth())
        self.edit_staff_widget.setSizePolicy(sizePolicy)
        self.edit_staff_widget.setMinimumSize(QtCore.QSize(1215, 0))
        self.edit_staff_widget.setMaximumSize(QtCore.QSize(1215, 16777215))
        self.edit_staff_widget.setObjectName("edit_staff_widget")
        self.edit_staff_search_frame = QtWidgets.QFrame(self.edit_staff_widget)
        self.edit_staff_search_frame.setGeometry(QtCore.QRect(0, -10, 491, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.edit_staff_search_frame.setFont(font)
        self.edit_staff_search_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.edit_staff_search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_staff_search_frame.setObjectName("edit_staff_search_frame")
        self.label_search_id_edit = QtWidgets.QLabel(self.edit_staff_search_frame)
        self.label_search_id_edit.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label_search_id_edit.setObjectName("label_search_id_edit")
        self.label_search_document_id_edit = QtWidgets.QLabel(self.edit_staff_search_frame)
        self.label_search_document_id_edit.setGeometry(QtCore.QRect(230, 30, 121, 16))
        self.label_search_document_id_edit.setObjectName("label_search_document_id_edit")
        self.line_input_edit_staff_search_id = QtWidgets.QLineEdit(self.edit_staff_search_frame)
        self.line_input_edit_staff_search_id.setGeometry(QtCore.QRect(110, 30, 91, 20))
        self.line_input_edit_staff_search_id.setObjectName("line_input_edit_staff_search_id")
        self.line_input_edit_staff_search_document_id = QtWidgets.QLineEdit(self.edit_staff_search_frame)
        self.line_input_edit_staff_search_document_id.setGeometry(QtCore.QRect(360, 30, 113, 20))
        self.line_input_edit_staff_search_document_id.setObjectName("line_input_edit_staff_search_document_id")
        self.button_search_edit_staff = QtWidgets.QPushButton(self.edit_staff_search_frame)
        self.button_search_edit_staff.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.button_search_edit_staff.setObjectName("button_search_edit_staff")
        self.frame_edit_staff = QtWidgets.QFrame(self.edit_staff_widget)
        self.frame_edit_staff.setGeometry(QtCore.QRect(-1, 99, 491, 231))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame_edit_staff.setFont(font)
        self.frame_edit_staff.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_edit_staff.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edit_staff.setObjectName("frame_edit_staff")
        self.label_full_name_static_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_full_name_static_edit.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_full_name_static_edit.setObjectName("label_full_name_static_edit")
        self.label_document_id_static_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_document_id_static_edit.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.label_document_id_static_edit.setObjectName("label_document_id_static_edit")
        self.label_phone_number_static_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_phone_number_static_edit.setGeometry(QtCore.QRect(10, 120, 131, 16))
        self.label_phone_number_static_edit.setObjectName("label_phone_number_static_edit")
        self.label_job_id_static_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_job_id_static_edit.setGeometry(QtCore.QRect(10, 150, 51, 16))
        self.label_job_id_static_edit.setObjectName("label_job_id_static_edit")
        self.label_address_static_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_address_static_edit.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_address_static_edit.setObjectName("label_address_static_edit")
        self.label_birthdate_static_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_birthdate_static_edit.setGeometry(QtCore.QRect(10, 180, 131, 16))
        self.label_birthdate_static_edit.setObjectName("label_birthdate_static_edit")
        self.label_agre_static_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_agre_static_edit.setGeometry(QtCore.QRect(10, 210, 47, 13))
        self.label_agre_static_edit.setObjectName("label_agre_static_edit")
        self.label_full_name_dynamic_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_full_name_dynamic_edit.setGeometry(QtCore.QRect(130, 20, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_full_name_dynamic_edit.setFont(font)
        self.label_full_name_dynamic_edit.setText("")
        self.label_full_name_dynamic_edit.setObjectName("label_full_name_dynamic_edit")
        self.label_document_id_dynamic_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_document_id_dynamic_edit.setEnabled(True)
        self.label_document_id_dynamic_edit.setGeometry(QtCore.QRect(60, 60, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_document_id_dynamic_edit.setFont(font)
        self.label_document_id_dynamic_edit.setText("")
        self.label_document_id_dynamic_edit.setObjectName("label_document_id_dynamic_edit")
        self.label_address_dynamic_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_address_dynamic_edit.setEnabled(True)
        self.label_address_dynamic_edit.setGeometry(QtCore.QRect(80, 90, 401, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_address_dynamic_edit.setFont(font)
        self.label_address_dynamic_edit.setText("")
        self.label_address_dynamic_edit.setObjectName("label_address_dynamic_edit")
        self.label_phone_number_dynamic_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_phone_number_dynamic_edit.setEnabled(True)
        self.label_phone_number_dynamic_edit.setGeometry(QtCore.QRect(140, 120, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_phone_number_dynamic_edit.setFont(font)
        self.label_phone_number_dynamic_edit.setText("")
        self.label_phone_number_dynamic_edit.setObjectName("label_phone_number_dynamic_edit")
        self.label_job_id_dynamic_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_job_id_dynamic_edit.setEnabled(True)
        self.label_job_id_dynamic_edit.setGeometry(QtCore.QRect(70, 150, 411, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_job_id_dynamic_edit.setFont(font)
        self.label_job_id_dynamic_edit.setText("")
        self.label_job_id_dynamic_edit.setObjectName("label_job_id_dynamic_edit")
        self.label_birthdate_dynamic_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_birthdate_dynamic_edit.setEnabled(True)
        self.label_birthdate_dynamic_edit.setGeometry(QtCore.QRect(150, 180, 331, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_birthdate_dynamic_edit.setFont(font)
        self.label_birthdate_dynamic_edit.setText("")
        self.label_birthdate_dynamic_edit.setObjectName("label_birthdate_dynamic_edit")
        self.label_age_dynamic_edit = QtWidgets.QLabel(self.frame_edit_staff)
        self.label_age_dynamic_edit.setEnabled(True)
        self.label_age_dynamic_edit.setGeometry(QtCore.QRect(50, 205, 168, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_age_dynamic_edit.setFont(font)
        self.label_age_dynamic_edit.setText("")
        self.label_age_dynamic_edit.setObjectName("label_age_dynamic_edit")
        self.frame_if_teacher = QtWidgets.QFrame(self.edit_staff_widget)
        self.frame_if_teacher.setGeometry(QtCore.QRect(-1, 329, 491, 341))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.frame_if_teacher.setFont(font)
        self.frame_if_teacher.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_if_teacher.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_if_teacher.setObjectName("frame_if_teacher")
        self.label_if_teacher_main_subject_static = QtWidgets.QLabel(self.frame_if_teacher)
        self.label_if_teacher_main_subject_static.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.label_if_teacher_main_subject_static.setObjectName("label_if_teacher_main_subject_static")
        self.label_if_teacher_assigned_grade_static = QtWidgets.QLabel(self.frame_if_teacher)
        self.label_if_teacher_assigned_grade_static.setGeometry(QtCore.QRect(290, 30, 91, 16))
        self.label_if_teacher_assigned_grade_static.setObjectName("label_if_teacher_assigned_grade_static")
        self.label_if_teacher_assigned_grade_dynamic = QtWidgets.QLabel(self.frame_if_teacher)
        self.label_if_teacher_assigned_grade_dynamic.setGeometry(QtCore.QRect(390, 30, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_if_teacher_assigned_grade_dynamic.setFont(font)
        self.label_if_teacher_assigned_grade_dynamic.setText("")
        self.label_if_teacher_assigned_grade_dynamic.setObjectName("label_if_teacher_assigned_grade_dynamic")
        self.label_if_teacher_main_subject_dynamic = QtWidgets.QLabel(self.frame_if_teacher)
        self.label_if_teacher_main_subject_dynamic.setGeometry(QtCore.QRect(120, 30, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_if_teacher_main_subject_dynamic.setFont(font)
        self.label_if_teacher_main_subject_dynamic.setText("")
        self.label_if_teacher_main_subject_dynamic.setObjectName("label_if_teacher_main_subject_dynamic")
        self.label_if_teacher_assigned_subjects_static = QtWidgets.QLabel(self.frame_if_teacher)
        self.label_if_teacher_assigned_subjects_static.setGeometry(QtCore.QRect(40, 60, 131, 20))
        self.label_if_teacher_assigned_subjects_static.setObjectName("label_if_teacher_assigned_subjects_static")
        self.label_if_teacher_grades_assigned_subject_static = QtWidgets.QLabel(self.frame_if_teacher)
        self.label_if_teacher_grades_assigned_subject_static.setGeometry(QtCore.QRect(310, 60, 121, 20))
        self.label_if_teacher_grades_assigned_subject_static.setObjectName("label_if_teacher_grades_assigned_subject_static")
        self.qlist_if_teacher_grades_assigned = QtWidgets.QListWidget(self.frame_if_teacher)
        self.qlist_if_teacher_grades_assigned.setGeometry(QtCore.QRect(305, 80, 151, 192))
        self.qlist_if_teacher_grades_assigned.setObjectName("qlist_if_teacher_grades_assigned")
        self.qlist_if_teacher_subjects_assigned = QtWidgets.QListWidget(self.frame_if_teacher)
        self.qlist_if_teacher_subjects_assigned.setGeometry(QtCore.QRect(40, 80, 151, 192))
        self.qlist_if_teacher_subjects_assigned.setObjectName("qlist_if_teacher_subjects_assigned")
        self.frame_edit_info = QtWidgets.QFrame(self.edit_staff_widget)
        self.frame_edit_info.setGeometry(QtCore.QRect(489, -1, 731, 181))
        self.frame_edit_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_edit_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edit_info.setObjectName("frame_edit_info")
        self.line_input_first_name_edit = QtWidgets.QLineEdit(self.frame_edit_info)
        self.line_input_first_name_edit.setGeometry(QtCore.QRect(70, 30, 113, 20))
        self.line_input_first_name_edit.setObjectName("line_input_first_name_edit")
        self.line_input_second_name_edit = QtWidgets.QLineEdit(self.frame_edit_info)
        self.line_input_second_name_edit.setGeometry(QtCore.QRect(250, 30, 113, 20))
        self.line_input_second_name_edit.setObjectName("line_input_second_name_edit")
        self.line_input_first_surname_edit = QtWidgets.QLineEdit(self.frame_edit_info)
        self.line_input_first_surname_edit.setGeometry(QtCore.QRect(420, 30, 113, 20))
        self.line_input_first_surname_edit.setObjectName("line_input_first_surname_edit")
        self.line_input_second_surname_edit = QtWidgets.QLineEdit(self.frame_edit_info)
        self.line_input_second_surname_edit.setGeometry(QtCore.QRect(580, 30, 113, 20))
        self.line_input_second_surname_edit.setObjectName("line_input_second_surname_edit")
        self.line_input_document_id_edit = QtWidgets.QLineEdit(self.frame_edit_info)
        self.line_input_document_id_edit.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.line_input_document_id_edit.setReadOnly(False)
        self.line_input_document_id_edit.setObjectName("line_input_document_id_edit")
        self.line_input_phone_number_edit = QtWidgets.QLineEdit(self.frame_edit_info)
        self.line_input_phone_number_edit.setGeometry(QtCore.QRect(250, 100, 113, 20))
        self.line_input_phone_number_edit.setObjectName("line_input_phone_number_edit")
        self.label_first_name_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_first_name_edit.setGeometry(QtCore.QRect(70, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_first_name_edit.setFont(font)
        self.label_first_name_edit.setObjectName("label_first_name_edit")
        self.label_second_name_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_second_name_edit.setGeometry(QtCore.QRect(250, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_second_name_edit.setFont(font)
        self.label_second_name_edit.setObjectName("label_second_name_edit")
        self.label_second_surname_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_second_surname_edit.setGeometry(QtCore.QRect(580, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_second_surname_edit.setFont(font)
        self.label_second_surname_edit.setObjectName("label_second_surname_edit")
        self.label_first_surname_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_first_surname_edit.setGeometry(QtCore.QRect(420, 10, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_first_surname_edit.setFont(font)
        self.label_first_surname_edit.setObjectName("label_first_surname_edit")
        self.combobox_job_id_edit = QtWidgets.QComboBox(self.frame_edit_info)
        self.combobox_job_id_edit.setGeometry(QtCore.QRect(430, 100, 101, 22))
        self.combobox_job_id_edit.setObjectName("combobox_job_id_edit")
        self.combobox_job_id_edit.addItem("")
        self.combobox_job_id_edit.addItem("")
        self.combobox_job_id_edit.addItem("")
        self.combobox_job_id_edit.addItem("")
        self.label_document_id_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_document_id_edit.setGeometry(QtCore.QRect(70, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_document_id_edit.setFont(font)
        self.label_document_id_edit.setObjectName("label_document_id_edit")
        self.label_phone_number_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_phone_number_edit.setGeometry(QtCore.QRect(250, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_phone_number_edit.setFont(font)
        self.label_phone_number_edit.setObjectName("label_phone_number_edit")
        self.label_job_id_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_job_id_edit.setGeometry(QtCore.QRect(430, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_job_id_edit.setFont(font)
        self.label_job_id_edit.setObjectName("label_job_id_edit")
        self.date_edit_staff = QtWidgets.QDateEdit(self.frame_edit_info)
        self.date_edit_staff.setGeometry(QtCore.QRect(590, 100, 110, 22))
        self.date_edit_staff.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.date_edit_staff.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Nicaragua))
        self.date_edit_staff.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.date_edit_staff.setCalendarPopup(True)
        self.date_edit_staff.setObjectName("date_edit_staff")
        self.label_birthdate_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_birthdate_edit.setGeometry(QtCore.QRect(590, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_birthdate_edit.setFont(font)
        self.label_birthdate_edit.setObjectName("label_birthdate_edit")
        self.checkbox_if_teacher_edit_subjects_assigned = QtWidgets.QCheckBox(self.frame_edit_info)
        self.checkbox_if_teacher_edit_subjects_assigned.setGeometry(QtCore.QRect(150, 150, 141, 17))
        self.checkbox_if_teacher_edit_subjects_assigned.setObjectName("checkbox_if_teacher_edit_subjects_assigned")
        self.checkbox_if_teacher_edit_grades_assigned = QtWidgets.QCheckBox(self.frame_edit_info)
        self.checkbox_if_teacher_edit_grades_assigned.setGeometry(QtCore.QRect(500, 150, 141, 17))
        self.checkbox_if_teacher_edit_grades_assigned.setObjectName("checkbox_if_teacher_edit_grades_assigned")
        self.checkbox_if_high_school_teacher_edit_staff = QtWidgets.QCheckBox(self.frame_edit_info)
        self.checkbox_if_high_school_teacher_edit_staff.setGeometry(QtCore.QRect(10, 150, 121, 17))
        self.checkbox_if_high_school_teacher_edit_staff.setObjectName("checkbox_if_high_school_teacher_edit_staff")
        self.label_address_edit = QtWidgets.QLabel(self.frame_edit_info)
        self.label_address_edit.setGeometry(QtCore.QRect(360, 130, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_address_edit.setFont(font)
        self.label_address_edit.setObjectName("label_address_edit")
        self.line_input_address_edit = QtWidgets.QLineEdit(self.frame_edit_info)
        self.line_input_address_edit.setGeometry(QtCore.QRect(330, 150, 113, 20))
        self.line_input_address_edit.setObjectName("line_input_address_edit")
        self.frame_if_edit_subject_or_grades = QtWidgets.QFrame(self.edit_staff_widget)
        self.frame_if_edit_subject_or_grades.setGeometry(QtCore.QRect(489, 179, 721, 341))
        self.frame_if_edit_subject_or_grades.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_if_edit_subject_or_grades.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_if_edit_subject_or_grades.setObjectName("frame_if_edit_subject_or_grades")
        self.listw_input_subjects_edit = QtWidgets.QListWidget(self.frame_if_edit_subject_or_grades)
        self.listw_input_subjects_edit.setGeometry(QtCore.QRect(120, 41, 161, 231))
        self.listw_input_subjects_edit.setObjectName("listw_input_subjects_edit")
        self.listw_input_subjects_edit.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.label_selection_subjects_edit = QtWidgets.QLabel(self.frame_if_edit_subject_or_grades)
        self.label_selection_subjects_edit.setGeometry(QtCore.QRect(130, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_selection_subjects_edit.setFont(font)
        self.label_selection_subjects_edit.setObjectName("label_selection_subjects_edit")
        self.label_selections_grades_edit = QtWidgets.QLabel(self.frame_if_edit_subject_or_grades)
        self.label_selections_grades_edit.setGeometry(QtCore.QRect(460, 10, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_selections_grades_edit.setFont(font)
        self.label_selections_grades_edit.setObjectName("label_selections_grades_edit")
        self.listw_input_grades_edit = QtWidgets.QListWidget(self.frame_if_edit_subject_or_grades)
        self.listw_input_grades_edit.setGeometry(QtCore.QRect(470, 41, 161, 231))
        self.listw_input_grades_edit.setObjectName("listw_input_grades_edit")
        self.listw_input_grades_edit.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.label_selection_main_subject_edit = QtWidgets.QLabel(self.frame_if_edit_subject_or_grades)
        self.label_selection_main_subject_edit.setGeometry(QtCore.QRect(10, 300, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_selection_main_subject_edit.setFont(font)
        self.label_selection_main_subject_edit.setObjectName("label_selection_main_subject_edit")
        self.label_selection_guide_grade_edit = QtWidgets.QLabel(self.frame_if_edit_subject_or_grades)
        self.label_selection_guide_grade_edit.setGeometry(QtCore.QRect(400, 300, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_selection_guide_grade_edit.setFont(font)
        self.label_selection_guide_grade_edit.setObjectName("label_selection_guide_grade_edit")
        self.combobox_main_subject_edit = QtWidgets.QComboBox(self.frame_if_edit_subject_or_grades)
        self.combobox_main_subject_edit.setGeometry(QtCore.QRect(200, 300, 151, 22))
        self.combobox_main_subject_edit.setObjectName("combobox_main_subject_edit")
        self.combobox_guide_grade_edit = QtWidgets.QComboBox(self.frame_if_edit_subject_or_grades)
        self.combobox_guide_grade_edit.setGeometry(QtCore.QRect(560, 300, 121, 22))
        self.combobox_guide_grade_edit.setObjectName("combobox_guide_grade_edit")
        self.frame_buttons_edit = QtWidgets.QFrame(self.edit_staff_widget)
        self.frame_buttons_edit.setGeometry(QtCore.QRect(489, 519, 711, 141))
        self.frame_buttons_edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons_edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons_edit.setObjectName("frame_buttons_edit")
        self.button_save_edit_staff = QtWidgets.QPushButton(self.frame_buttons_edit)
        self.button_save_edit_staff.setGeometry(QtCore.QRect(140, 70, 111, 41))
        self.button_save_edit_staff.setObjectName("button_save_edit_staff")
        self.button_clean_information_2 = QtWidgets.QPushButton(self.frame_buttons_edit)
        self.button_clean_information_2.setGeometry(QtCore.QRect(500, 70, 111, 41))
        self.button_clean_information_2.setObjectName("button_clean_information_2")
        self.main_central_widget.addTab(self.edit_staff_widget, "")
        self.change_status_staff_widget = QtWidgets.QWidget()
        self.change_status_staff_widget.setObjectName("change_status_staff_widget")
        self.frame_change_status_staff = QtWidgets.QFrame(self.change_status_staff_widget)
        self.frame_change_status_staff.setGeometry(QtCore.QRect(0, -10, 1211, 111))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame_change_status_staff.setFont(font)
        self.frame_change_status_staff.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_change_status_staff.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_change_status_staff.setObjectName("frame_change_status_staff")
        self.label_search_id_change_status = QtWidgets.QLabel(self.frame_change_status_staff)
        self.label_search_id_change_status.setGeometry(QtCore.QRect(390, 30, 91, 16))
        self.label_search_id_change_status.setObjectName("label_search_id_change_status")
        self.label_search_document_id_change_status = QtWidgets.QLabel(self.frame_change_status_staff)
        self.label_search_document_id_change_status.setGeometry(QtCore.QRect(600, 30, 121, 16))
        self.label_search_document_id_change_status.setObjectName("label_search_document_id_change_status")
        self.line_input_change_status_staff_search_id = QtWidgets.QLineEdit(self.frame_change_status_staff)
        self.line_input_change_status_staff_search_id.setGeometry(QtCore.QRect(480, 30, 91, 20))
        self.line_input_change_status_staff_search_id.setObjectName("line_input_change_status_staff_search_id")
        self.line_input_change_status_staff_search_document_id = QtWidgets.QLineEdit(self.frame_change_status_staff)
        self.line_input_change_status_staff_search_document_id.setGeometry(QtCore.QRect(730, 30, 113, 20))
        self.line_input_change_status_staff_search_document_id.setObjectName("line_input_change_status_staff_search_document_id")
        self.button_search_change_status_staff = QtWidgets.QPushButton(self.frame_change_status_staff)
        self.button_search_change_status_staff.setGeometry(QtCore.QRect(560, 70, 75, 23))
        self.button_search_change_status_staff.setObjectName("button_search_change_status_staff")
        self.frame_change_status_staff_outputinfo = QtWidgets.QFrame(self.change_status_staff_widget)
        self.frame_change_status_staff_outputinfo.setGeometry(QtCore.QRect(0, 100, 1211, 131))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame_change_status_staff_outputinfo.setFont(font)
        self.frame_change_status_staff_outputinfo.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_change_status_staff_outputinfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_change_status_staff_outputinfo.setObjectName("frame_change_status_staff_outputinfo")
        self.label_full_name_static_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_full_name_static_change_status.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_full_name_static_change_status.setObjectName("label_full_name_static_change_status")
        self.label_document_id_static_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_document_id_static_change_status.setGeometry(QtCore.QRect(500, 20, 47, 13))
        self.label_document_id_static_change_status.setObjectName("label_document_id_static_change_status")
        self.label_phone_number_static_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_phone_number_static_change_status.setGeometry(QtCore.QRect(500, 50, 131, 16))
        self.label_phone_number_static_change_status.setObjectName("label_phone_number_static_change_status")
        self.label_job_id_static_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_job_id_static_change_status.setGeometry(QtCore.QRect(10, 80, 51, 16))
        self.label_job_id_static_change_status.setObjectName("label_job_id_static_change_status")
        self.label_address_static_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_address_static_change_status.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_address_static_change_status.setObjectName("label_address_static_change_status")
        self.label_birthdate_static_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_birthdate_static_change_status.setGeometry(QtCore.QRect(500, 80, 131, 16))
        self.label_birthdate_static_change_status.setObjectName("label_birthdate_static_change_status")
        self.label_agre_static_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_agre_static_change_status.setGeometry(QtCore.QRect(970, 25, 47, 13))
        self.label_agre_static_change_status.setObjectName("label_agre_static_change_status")
        self.label_full_name_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_full_name_dynamic_change_status.setGeometry(QtCore.QRect(130, 20, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_full_name_dynamic_change_status.setFont(font)
        self.label_full_name_dynamic_change_status.setText("")
        self.label_full_name_dynamic_change_status.setObjectName("label_full_name_dynamic_change_status")
        self.label_document_id_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_document_id_dynamic_change_status.setEnabled(True)
        self.label_document_id_dynamic_change_status.setGeometry(QtCore.QRect(550, 20, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_document_id_dynamic_change_status.setFont(font)
        self.label_document_id_dynamic_change_status.setText("")
        self.label_document_id_dynamic_change_status.setObjectName("label_document_id_dynamic_change_status")
        self.label_address_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_address_dynamic_change_status.setEnabled(True)
        self.label_address_dynamic_change_status.setGeometry(QtCore.QRect(80, 50, 401, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_address_dynamic_change_status.setFont(font)
        self.label_address_dynamic_change_status.setText("")
        self.label_address_dynamic_change_status.setObjectName("label_address_dynamic_change_status")
        self.label_phone_number_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_phone_number_dynamic_change_status.setEnabled(True)
        self.label_phone_number_dynamic_change_status.setGeometry(QtCore.QRect(630, 50, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_phone_number_dynamic_change_status.setFont(font)
        self.label_phone_number_dynamic_change_status.setText("")
        self.label_phone_number_dynamic_change_status.setObjectName("label_phone_number_dynamic_change_status")
        self.label_job_id_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_job_id_dynamic_change_status.setEnabled(True)
        self.label_job_id_dynamic_change_status.setGeometry(QtCore.QRect(70, 80, 411, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_job_id_dynamic_change_status.setFont(font)
        self.label_job_id_dynamic_change_status.setText("")
        self.label_job_id_dynamic_change_status.setObjectName("label_job_id_dynamic_change_status")
        self.label_birthdate_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_birthdate_dynamic_change_status.setEnabled(True)
        self.label_birthdate_dynamic_change_status.setGeometry(QtCore.QRect(640, 80, 331, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_birthdate_dynamic_change_status.setFont(font)
        self.label_birthdate_dynamic_change_status.setText("")
        self.label_birthdate_dynamic_change_status.setObjectName("label_birthdate_dynamic_change_status")
        self.label_age_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_age_dynamic_change_status.setEnabled(True)
        self.label_age_dynamic_change_status.setGeometry(QtCore.QRect(1010, 20, 168, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_age_dynamic_change_status.setFont(font)
        self.label_age_dynamic_change_status.setText("")
        self.label_age_dynamic_change_status.setObjectName("label_age_dynamic_change_status")
        self.label_status_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_status_change_status.setGeometry(QtCore.QRect(970, 50, 51, 16))
        self.label_status_change_status.setObjectName("label_status_change_status")
        self.label_status_dynamic_change_status = QtWidgets.QLabel(self.frame_change_status_staff_outputinfo)
        self.label_status_dynamic_change_status.setGeometry(QtCore.QRect(1020, 50, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_status_dynamic_change_status.setFont(font)
        self.label_status_dynamic_change_status.setText("")
        self.label_status_dynamic_change_status.setObjectName("label_status_dynamic_change_status")
        self.frame_buttons_change_status = QtWidgets.QFrame(self.change_status_staff_widget)
        self.frame_buttons_change_status.setGeometry(QtCore.QRect(340, 229, 501, 43))
        self.frame_buttons_change_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons_change_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons_change_status.setObjectName("frame_buttons_change_status")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_buttons_change_status)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_chhange_status_restore = QtWidgets.QPushButton(self.frame_buttons_change_status)
        self.button_chhange_status_restore.setObjectName("button_chhange_status_restore")
        self.horizontalLayout_2.addWidget(self.button_chhange_status_restore)
        self.button_change_status_delete = QtWidgets.QPushButton(self.frame_buttons_change_status)
        self.button_change_status_delete.setObjectName("button_change_status_delete")
        self.horizontalLayout_2.addWidget(self.button_change_status_delete)
        self.button_clean_information_change_status = QtWidgets.QPushButton(self.frame_buttons_change_status)
        self.button_clean_information_change_status.setObjectName("button_clean_information_change_status")
        self.horizontalLayout_2.addWidget(self.button_clean_information_change_status)
        self.frame_if_teacher_change_status_staff = QtWidgets.QFrame(self.change_status_staff_widget)
        self.frame_if_teacher_change_status_staff.setGeometry(QtCore.QRect(-1, 339, 1211, 321))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.frame_if_teacher_change_status_staff.setFont(font)
        self.frame_if_teacher_change_status_staff.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_if_teacher_change_status_staff.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_if_teacher_change_status_staff.setObjectName("frame_if_teacher_change_status_staff")
        self.label_change_status_note_if_teacher = QtWidgets.QLabel(self.frame_if_teacher_change_status_staff)
        self.label_change_status_note_if_teacher.setGeometry(QtCore.QRect(40, 40, 461, 16))
        self.label_change_status_note_if_teacher.setObjectName("label_change_status_note_if_teacher")
        self.label_grade_guide_change_status_if_teacher = QtWidgets.QLabel(self.frame_if_teacher_change_status_staff)
        self.label_grade_guide_change_status_if_teacher.setGeometry(QtCore.QRect(40, 80, 131, 16))
        self.label_grade_guide_change_status_if_teacher.setObjectName("label_grade_guide_change_status_if_teacher")
        self.label_grades_assigned_change_status_if_teacher = QtWidgets.QLabel(self.frame_if_teacher_change_status_staff)
        self.label_grades_assigned_change_status_if_teacher.setGeometry(QtCore.QRect(220, 80, 121, 16))
        self.label_grades_assigned_change_status_if_teacher.setObjectName("label_grades_assigned_change_status_if_teacher")
        self.label_grade_guide_if_teacher_change_status_dynamic = QtWidgets.QLabel(self.frame_if_teacher_change_status_staff)
        self.label_grade_guide_if_teacher_change_status_dynamic.setGeometry(QtCore.QRect(40, 110, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_grade_guide_if_teacher_change_status_dynamic.setFont(font)
        self.label_grade_guide_if_teacher_change_status_dynamic.setText("")
        self.label_grade_guide_if_teacher_change_status_dynamic.setObjectName("label_grade_guide_if_teacher_change_status_dynamic")
        self.tablew_change_status_if_teacher_grades_assigned = QtWidgets.QTableWidget(self.frame_if_teacher_change_status_staff)
        self.tablew_change_status_if_teacher_grades_assigned.setGeometry(QtCore.QRect(220, 110, 411, 192))
        self.tablew_change_status_if_teacher_grades_assigned.setObjectName("tablew_change_status_if_teacher_grades_assigned")
        self.tablew_change_status_if_teacher_grades_assigned.setColumnCount(4)
        self.tablew_change_status_if_teacher_grades_assigned.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_change_status_if_teacher_grades_assigned.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_change_status_if_teacher_grades_assigned.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_change_status_if_teacher_grades_assigned.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_change_status_if_teacher_grades_assigned.setHorizontalHeaderItem(3, item)
        self.frame_buttons_confirm = QtWidgets.QFrame(self.frame_if_teacher_change_status_staff)
        self.frame_buttons_confirm.setGeometry(QtCore.QRect(649, 109, 100, 76))
        self.frame_buttons_confirm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons_confirm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons_confirm.setObjectName("frame_buttons_confirm")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_buttons_confirm)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.buttons_change_status_confirm_if_teacher = QtWidgets.QPushButton(self.frame_buttons_confirm)
        self.buttons_change_status_confirm_if_teacher.setObjectName("buttons_change_status_confirm_if_teacher")
        self.verticalLayout_3.addWidget(self.buttons_change_status_confirm_if_teacher)
        self.button_change_status_cancel_if_teacher = QtWidgets.QPushButton(self.frame_buttons_confirm)
        self.button_change_status_cancel_if_teacher.setObjectName("button_change_status_cancel_if_teacher")
        self.verticalLayout_3.addWidget(self.button_change_status_cancel_if_teacher)
        self.frame_buttons_confirm_change_status = QtWidgets.QFrame(self.change_status_staff_widget)
        self.frame_buttons_confirm_change_status.setGeometry(QtCore.QRect(470, 280, 251, 51))
        self.frame_buttons_confirm_change_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons_confirm_change_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons_confirm_change_status.setObjectName("frame_buttons_confirm_change_status")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_buttons_confirm_change_status)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_confirm_change_status = QtWidgets.QPushButton(self.frame_buttons_confirm_change_status)
        self.button_confirm_change_status.setObjectName("button_confirm_change_status")
        self.horizontalLayout_3.addWidget(self.button_confirm_change_status)
        self.button_cancel_change_status = QtWidgets.QPushButton(self.frame_buttons_confirm_change_status)
        self.button_cancel_change_status.setObjectName("button_cancel_change_status")
        self.horizontalLayout_3.addWidget(self.button_cancel_change_status)
        self.main_central_widget.addTab(self.change_status_staff_widget, "")
        self.search_staff_widget = QtWidgets.QWidget()
        self.search_staff_widget.setObjectName("search_staff_widget")
        self.frame_search_staff = QtWidgets.QFrame(self.search_staff_widget)
        self.frame_search_staff.setGeometry(QtCore.QRect(-1, -1, 1211, 661))
        self.frame_search_staff.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_search_staff.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_search_staff.setObjectName("frame_search_staff")
        self.tablew_show_staff_registered_search_staff = QtWidgets.QTableWidget(self.frame_search_staff)
        self.tablew_show_staff_registered_search_staff.setEnabled(True)
        self.tablew_show_staff_registered_search_staff.setGeometry(QtCore.QRect(10, 160, 1201, 461))
        self.tablew_show_staff_registered_search_staff.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tablew_show_staff_registered_search_staff.setAlternatingRowColors(False)
        self.tablew_show_staff_registered_search_staff.setObjectName("tablew_show_staff_registered_search_staff")
        self.tablew_show_staff_registered_search_staff.setColumnCount(9)
        self.tablew_show_staff_registered_search_staff.setRowCount(0)
        self.tablew_show_staff_registered_search_staff.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_show_staff_registered_search_staff.setHorizontalHeaderItem(8, item)
        self.tablew_show_staff_registered_search_staff.verticalHeader().setSortIndicatorShown(False)
        self.tablew_show_staff_registered_search_staff.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.frame_details_search_staff = QtWidgets.QFrame(self.frame_search_staff)
        self.frame_details_search_staff.setGeometry(QtCore.QRect(9, -1, 911, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.frame_details_search_staff.setFont(font)
        self.frame_details_search_staff.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_details_search_staff.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_details_search_staff.setObjectName("frame_details_search_staff")
        self.label_full_name_search_staff = QtWidgets.QLabel(self.frame_details_search_staff)
        self.label_full_name_search_staff.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_full_name_search_staff.setObjectName("label_full_name_search_staff")
        self.label_document_id_search_staff = QtWidgets.QLabel(self.frame_details_search_staff)
        self.label_document_id_search_staff.setGeometry(QtCore.QRect(640, 10, 51, 16))
        self.label_document_id_search_staff.setObjectName("label_document_id_search_staff")
        self.label_phone_number_search_staff = QtWidgets.QLabel(self.frame_details_search_staff)
        self.label_phone_number_search_staff.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_phone_number_search_staff.setObjectName("label_phone_number_search_staff")
        self.line_input_full_name_search_staff = QtWidgets.QLineEdit(self.frame_details_search_staff)
        self.line_input_full_name_search_staff.setGeometry(QtCore.QRect(140, 10, 451, 20))
        self.line_input_full_name_search_staff.setObjectName("line_input_full_name_search_staff")
        self.line_input_document_id_search_staff = QtWidgets.QLineEdit(self.frame_details_search_staff)
        self.line_input_document_id_search_staff.setGeometry(QtCore.QRect(690, 10, 191, 20))
        self.line_input_document_id_search_staff.setObjectName("line_input_document_id_search_staff")
        self.line_input_phone_number_search_staff = QtWidgets.QLineEdit(self.frame_details_search_staff)
        self.line_input_phone_number_search_staff.setGeometry(QtCore.QRect(140, 50, 91, 20))
        self.line_input_phone_number_search_staff.setText("")
        self.line_input_phone_number_search_staff.setObjectName("line_input_phone_number_search_staff")
        self.frame_buttons_actions_search_staff = QtWidgets.QFrame(self.frame_search_staff)
        self.frame_buttons_actions_search_staff.setGeometry(QtCore.QRect(919, -1, 291, 161))
        self.frame_buttons_actions_search_staff.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons_actions_search_staff.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons_actions_search_staff.setObjectName("frame_buttons_actions_search_staff")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_buttons_actions_search_staff)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_show_details_qtable_selected_search_staff = QtWidgets.QPushButton(self.frame_buttons_actions_search_staff)
        self.button_show_details_qtable_selected_search_staff.setObjectName("button_show_details_qtable_selected_search_staff")
        self.verticalLayout_4.addWidget(self.button_show_details_qtable_selected_search_staff)
        self.button_edit_selected_staff_search_staff = QtWidgets.QPushButton(self.frame_buttons_actions_search_staff)
        self.button_edit_selected_staff_search_staff.setObjectName("button_edit_selected_staff_search_staff")
        self.verticalLayout_4.addWidget(self.button_edit_selected_staff_search_staff)
        self.button_clear_information_search_staff = QtWidgets.QPushButton(self.frame_buttons_actions_search_staff)
        self.button_clear_information_search_staff.setObjectName("button_clear_information_search_staff")
        self.verticalLayout_4.addWidget(self.button_clear_information_search_staff)
        self.main_central_widget.addTab(self.search_staff_widget, "")
        self.impart_teacher_time = QtWidgets.QWidget()
        self.impart_teacher_time.setObjectName("impart_teacher_time")
        self.frame_impart_teacher_time = QtWidgets.QFrame(self.impart_teacher_time)
        self.frame_impart_teacher_time.setGeometry(QtCore.QRect(-1, -1, 1211, 671))
        self.frame_impart_teacher_time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_impart_teacher_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_impart_teacher_time.setObjectName("frame_impart_teacher_time")
        self.label_select_teacher_static_impart_tt = QtWidgets.QLabel(self.frame_impart_teacher_time)
        self.label_select_teacher_static_impart_tt.setGeometry(QtCore.QRect(10, 10, 661, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_select_teacher_static_impart_tt.setFont(font)
        self.label_select_teacher_static_impart_tt.setObjectName("label_select_teacher_static_impart_tt")
        self.tablew_select_teacher_impart_tt = QtWidgets.QTableWidget(self.frame_impart_teacher_time)
        self.tablew_select_teacher_impart_tt.setGeometry(QtCore.QRect(10, 30, 1191, 411))
        self.tablew_select_teacher_impart_tt.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.tablew_select_teacher_impart_tt.setObjectName("tablew_select_teacher_impart_tt")
        self.tablew_select_teacher_impart_tt.setColumnCount(8)
        self.tablew_select_teacher_impart_tt.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_select_teacher_impart_tt.setHorizontalHeaderItem(7, item)
        self.tablew_select_teacher_impart_tt.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tablew_select_teacher_impart_tt.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablew_select_teacher_impart_tt.setSortingEnabled(False)
        self.tablew_select_teacher_impart_tt.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablew_select_teacher_impart_tt.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listw_select_grade_impart_tt = QtWidgets.QListWidget(self.frame_impart_teacher_time)
        self.listw_select_grade_impart_tt.setGeometry(QtCore.QRect(10, 470, 141, 192))
        self.listw_select_grade_impart_tt.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listw_select_grade_impart_tt.setViewMode(QtWidgets.QListView.ListMode)
        self.listw_select_grade_impart_tt.setObjectName("listw_select_grade_impart_tt")
        self.label_select_grade_static_impart_tt = QtWidgets.QLabel(self.frame_impart_teacher_time)
        self.label_select_grade_static_impart_tt.setGeometry(QtCore.QRect(10, 450, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_select_grade_static_impart_tt.setFont(font)
        self.label_select_grade_static_impart_tt.setObjectName("label_select_grade_static_impart_tt")
        self.label_select_subject_static_impart_tt = QtWidgets.QLabel(self.frame_impart_teacher_time)
        self.label_select_subject_static_impart_tt.setGeometry(QtCore.QRect(350, 450, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_select_subject_static_impart_tt.setFont(font)
        self.label_select_subject_static_impart_tt.setObjectName("label_select_subject_static_impart_tt")
        self.listw_select_subject_impart_tt = QtWidgets.QListWidget(self.frame_impart_teacher_time)
        self.listw_select_subject_impart_tt.setGeometry(QtCore.QRect(350, 470, 141, 192))
        self.listw_select_subject_impart_tt.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listw_select_subject_impart_tt.setViewMode(QtWidgets.QListView.ListMode)
        self.listw_select_subject_impart_tt.setObjectName("listw_select_subject_impart_tt")
        self.label_select_start_time_subject_static_impart_tt = QtWidgets.QLabel(self.frame_impart_teacher_time)
        self.label_select_start_time_subject_static_impart_tt.setGeometry(QtCore.QRect(170, 470, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_select_start_time_subject_static_impart_tt.setFont(font)
        self.label_select_start_time_subject_static_impart_tt.setObjectName("label_select_start_time_subject_static_impart_tt")
        self.timeedit_select_impart_start_time_impart_tt = QtWidgets.QTimeEdit(self.frame_impart_teacher_time)
        self.timeedit_select_impart_start_time_impart_tt.setGeometry(QtCore.QRect(170, 500, 118, 22))
        self.timeedit_select_impart_start_time_impart_tt.setTime(QtCore.QTime(6, 0, 0))
        self.timeedit_select_impart_start_time_impart_tt.setObjectName("timeedit_select_impart_start_time_impart_tt")
        self.label_select_end_time_static_static_impart_tt = QtWidgets.QLabel(self.frame_impart_teacher_time)
        self.label_select_end_time_static_static_impart_tt.setGeometry(QtCore.QRect(170, 560, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_select_end_time_static_static_impart_tt.setFont(font)
        self.label_select_end_time_static_static_impart_tt.setObjectName("label_select_end_time_static_static_impart_tt")
        self.timeedit_select_impart_end_time_impart_tt = QtWidgets.QTimeEdit(self.frame_impart_teacher_time)
        self.timeedit_select_impart_end_time_impart_tt.setGeometry(QtCore.QRect(170, 590, 118, 22))
        self.timeedit_select_impart_end_time_impart_tt.setTime(QtCore.QTime(8, 0, 0))
        self.timeedit_select_impart_end_time_impart_tt.setObjectName("timeedit_select_impart_end_time_impart_tt")
        self.frame_buttons_impart_teacher_time = QtWidgets.QFrame(self.frame_impart_teacher_time)
        self.frame_buttons_impart_teacher_time.setGeometry(QtCore.QRect(990, 470, 221, 191))
        self.frame_buttons_impart_teacher_time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons_impart_teacher_time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons_impart_teacher_time.setObjectName("frame_buttons_impart_teacher_time")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_buttons_impart_teacher_time)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.button_clean_information_selected_impart_tt = QtWidgets.QPushButton(self.frame_buttons_impart_teacher_time)
        self.button_clean_information_selected_impart_tt.setObjectName("button_clean_information_selected_impart_tt")
        self.verticalLayout_5.addWidget(self.button_clean_information_selected_impart_tt)
        self.button_unassign_time_selected_impart_tt = QtWidgets.QPushButton(self.frame_buttons_impart_teacher_time)
        self.button_unassign_time_selected_impart_tt.setObjectName("button_unassign_time_selected_impart_tt")
        self.verticalLayout_5.addWidget(self.button_unassign_time_selected_impart_tt)
        self.button_save_information_selected_impart_tt = QtWidgets.QPushButton(self.frame_buttons_impart_teacher_time)
        self.button_save_information_selected_impart_tt.setObjectName("button_save_information_selected_impart_tt")
        self.verticalLayout_5.addWidget(self.button_save_information_selected_impart_tt)
        self.frame_details_selected_data_impart_tt = QtWidgets.QFrame(self.frame_impart_teacher_time)
        self.frame_details_selected_data_impart_tt.setGeometry(QtCore.QRect(510, 468, 481, 191))
        self.frame_details_selected_data_impart_tt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_details_selected_data_impart_tt.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_details_selected_data_impart_tt.setObjectName("frame_details_selected_data_impart_tt")
        self.label_details_selected_data_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_details_selected_data_impart_tt.setGeometry(QtCore.QRect(10, 0, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_details_selected_data_impart_tt.setFont(font)
        self.label_details_selected_data_impart_tt.setObjectName("label_details_selected_data_impart_tt")
        self.label_time_selected_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_time_selected_impart_tt.setGeometry(QtCore.QRect(10, 160, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_time_selected_impart_tt.setFont(font)
        self.label_time_selected_impart_tt.setObjectName("label_time_selected_impart_tt")
        self.label_grade_selected_data_dynamic_impart_tt_ = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_grade_selected_data_dynamic_impart_tt_.setGeometry(QtCore.QRect(57, 80, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_grade_selected_data_dynamic_impart_tt_.setFont(font)
        self.label_grade_selected_data_dynamic_impart_tt_.setText("")
        self.label_grade_selected_data_dynamic_impart_tt_.setObjectName("label_grade_selected_data_dynamic_impart_tt_")
        self.label_subject_selected_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_subject_selected_impart_tt.setGeometry(QtCore.QRect(10, 120, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_subject_selected_impart_tt.setFont(font)
        self.label_subject_selected_impart_tt.setObjectName("label_subject_selected_impart_tt")
        self.label_grade_selected_data_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_grade_selected_data_impart_tt.setGeometry(QtCore.QRect(10, 80, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_grade_selected_data_impart_tt.setFont(font)
        self.label_grade_selected_data_impart_tt.setObjectName("label_grade_selected_data_impart_tt")
        self.label_teacher_selected_dynamic_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_teacher_selected_dynamic_impart_tt.setGeometry(QtCore.QRect(70, 40, 301, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_teacher_selected_dynamic_impart_tt.setFont(font)
        self.label_teacher_selected_dynamic_impart_tt.setText("")
        self.label_teacher_selected_dynamic_impart_tt.setObjectName("label_teacher_selected_dynamic_impart_tt")
        self.label_subject_selected_data_dynamic_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_subject_selected_data_dynamic_impart_tt.setGeometry(QtCore.QRect(66, 120, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_subject_selected_data_dynamic_impart_tt.setFont(font)
        self.label_subject_selected_data_dynamic_impart_tt.setText("")
        self.label_subject_selected_data_dynamic_impart_tt.setObjectName("label_subject_selected_data_dynamic_impart_tt")
        self.label_teacher_selected_data_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_teacher_selected_data_impart_tt.setGeometry(QtCore.QRect(10, 40, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_teacher_selected_data_impart_tt.setFont(font)
        self.label_teacher_selected_data_impart_tt.setObjectName("label_teacher_selected_data_impart_tt")
        self.label_time_selected_data_dynamic_impart_tt = QtWidgets.QLabel(self.frame_details_selected_data_impart_tt)
        self.label_time_selected_data_dynamic_impart_tt.setGeometry(QtCore.QRect(125, 160, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_time_selected_data_dynamic_impart_tt.setFont(font)
        self.label_time_selected_data_dynamic_impart_tt.setText("")
        self.label_time_selected_data_dynamic_impart_tt.setObjectName("label_time_selected_data_dynamic_impart_tt")
        self.combox_filter_tablew_select_teacher_impart_tt = QtWidgets.QComboBox(self.frame_impart_teacher_time)
        self.combox_filter_tablew_select_teacher_impart_tt.setGeometry(QtCore.QRect(1079, 4, 121, 22))
        self.combox_filter_tablew_select_teacher_impart_tt.setObjectName("combox_filter_tablew_select_teacher_impart_tt")
        self.combox_filter_tablew_select_teacher_impart_tt.addItem("")
        self.combox_filter_tablew_select_teacher_impart_tt.addItem("")
        self.combox_filter_tablew_select_teacher_impart_tt.addItem("")
        self.combox_filter_tablew_select_teacher_impart_tt.addItem("")
        self.combox_filter_tablew_select_teacher_impart_tt.addItem("")
        self.combox_filter_tablew_select_teacher_impart_tt.addItem("")
        self.label_name_search_impart_tt = QtWidgets.QLabel(self.frame_impart_teacher_time)
        self.label_name_search_impart_tt.setGeometry(QtCore.QRect(680, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name_search_impart_tt.setFont(font)
        self.label_name_search_impart_tt.setObjectName("label_name_search_impart_tt")
        self.line_input_search_name_teacher_impart_tt = QtWidgets.QLineEdit(self.frame_impart_teacher_time)
        self.line_input_search_name_teacher_impart_tt.setGeometry(QtCore.QRect(738, 8, 201, 20))
        self.line_input_search_name_teacher_impart_tt.setObjectName("line_input_search_name_teacher_impart_tt")
        self.label_id_search_impart_tt = QtWidgets.QLabel(self.frame_impart_teacher_time)
        self.label_id_search_impart_tt.setGeometry(QtCore.QRect(941, 10, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_search_impart_tt.setFont(font)
        self.label_id_search_impart_tt.setObjectName("label_id_search_impart_tt")
        self.line_input_search_id_teacher_impart_tt = QtWidgets.QLineEdit(self.frame_impart_teacher_time)
        self.line_input_search_id_teacher_impart_tt.setGeometry(QtCore.QRect(960, 8, 81, 20))
        self.line_input_search_id_teacher_impart_tt.setObjectName("line_input_search_id_teacher_impart_tt")
        self.main_central_widget.addTab(self.impart_teacher_time, "")
        self.new_login = QtWidgets.QWidget()
        self.new_login.setObjectName("new_login")
        self.tablew_software_access_show = QtWidgets.QTableWidget(self.new_login)
        self.tablew_software_access_show.setGeometry(QtCore.QRect(0, 0, 1201, 461))
        self.tablew_software_access_show.setObjectName("tablew_software_access_show")
        self.tablew_software_access_show.setColumnCount(6)
        self.tablew_software_access_show.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_software_access_show.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_software_access_show.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_software_access_show.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_software_access_show.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_software_access_show.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablew_software_access_show.setHorizontalHeaderItem(5, item)
        self.tablew_software_access_show.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) 
        self.tablew_software_access_show.setSortingEnabled(False)
        self.tablew_software_access_show.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.label_search_id_software_access = QtWidgets.QLabel(self.new_login)
        self.label_search_id_software_access.setGeometry(QtCore.QRect(10, 489, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_search_id_software_access.setFont(font)
        self.label_search_id_software_access.setObjectName("label_search_id_software_access")
        self.line_input_search_by_register_id_staff_software_access = QtWidgets.QLineEdit(self.new_login)
        self.line_input_search_by_register_id_staff_software_access.setGeometry(QtCore.QRect(100, 489, 61, 20))
        self.line_input_search_by_register_id_staff_software_access.setText("")
        self.line_input_search_by_register_id_staff_software_access.setObjectName("line_input_search_by_register_id_staff_software_access")
        self.label_add_access_software_access = QtWidgets.QLabel(self.new_login)
        self.label_add_access_software_access.setGeometry(QtCore.QRect(140, 540, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_add_access_software_access.setFont(font)
        self.label_add_access_software_access.setObjectName("label_add_access_software_access")
        self.line_software_access_8 = QtWidgets.QFrame(self.new_login)
        self.line_software_access_8.setGeometry(QtCore.QRect(1, 540, 131, 16))
        self.line_software_access_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access_8.setLineWidth(2)
        self.line_software_access_8.setMidLineWidth(0)
        self.line_software_access_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_software_access_8.setObjectName("line_software_access_8")
        self.line_software_access = QtWidgets.QFrame(self.new_login)
        self.line_software_access.setGeometry(QtCore.QRect(240, 540, 241, 20))
        self.line_software_access.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access.setLineWidth(2)
        self.line_software_access.setMidLineWidth(0)
        self.line_software_access.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_software_access.setObjectName("line_software_access")
        self.label_search_and_add_by_register_id_staff_software_access = QtWidgets.QLabel(self.new_login)
        self.label_search_and_add_by_register_id_staff_software_access.setGeometry(QtCore.QRect(10, 560, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_search_and_add_by_register_id_staff_software_access.setFont(font)
        self.label_search_and_add_by_register_id_staff_software_access.setObjectName("label_search_and_add_by_register_id_staff_software_access")
        self.label_new_user_software_access = QtWidgets.QLabel(self.new_login)
        self.label_new_user_software_access.setGeometry(QtCore.QRect(10, 590, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_new_user_software_access.setFont(font)
        self.label_new_user_software_access.setObjectName("label_new_user_software_access")
        self.label_new_password_software_access = QtWidgets.QLabel(self.new_login)
        self.label_new_password_software_access.setGeometry(QtCore.QRect(10, 620, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_new_password_software_access.setFont(font)
        self.label_new_password_software_access.setObjectName("label_new_password_software_access")
        self.label_search_by_user_software_access = QtWidgets.QLabel(self.new_login)
        self.label_search_by_user_software_access.setGeometry(QtCore.QRect(420, 491, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_search_by_user_software_access.setFont(font)
        self.label_search_by_user_software_access.setObjectName("label_search_by_user_software_access")
        self.line_input_search_by_user_software_access = QtWidgets.QLineEdit(self.new_login)
        self.line_input_search_by_user_software_access.setGeometry(QtCore.QRect(550, 490, 201, 20))
        self.line_input_search_by_user_software_access.setText("")
        self.line_input_search_by_user_software_access.setObjectName("line_input_search_by_user_software_access")
        self.line_input_add_access_by_staff_id_software_access = QtWidgets.QLineEdit(self.new_login)
        self.line_input_add_access_by_staff_id_software_access.setGeometry(QtCore.QRect(100, 560, 61, 20))
        self.line_input_add_access_by_staff_id_software_access.setObjectName("line_input_add_access_by_staff_id_software_access")
        self.line_input_new_user_add_software_access = QtWidgets.QLineEdit(self.new_login)
        self.line_input_new_user_add_software_access.setGeometry(QtCore.QRect(110, 590, 191, 20))
        self.line_input_new_user_add_software_access.setObjectName("line_input_new_user_add_software_access")
        self.line_input_new_password_software_access = QtWidgets.QLineEdit(self.new_login)
        self.line_input_new_password_software_access.setGeometry(QtCore.QRect(130, 620, 211, 20))
        self.line_input_new_password_software_access.setObjectName("line_input_new_password_software_access")
        self.line_software_access_2 = QtWidgets.QFrame(self.new_login)
        self.line_software_access_2.setGeometry(QtCore.QRect(360, 543, 20, 131))
        self.line_software_access_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access_2.setLineWidth(2)
        self.line_software_access_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_software_access_2.setObjectName("line_software_access_2")
        self.button_clean_information_software_access = QtWidgets.QPushButton(self.new_login)
        self.button_clean_information_software_access.setGeometry(QtCore.QRect(510, 552, 271, 101))
        self.button_clean_information_software_access.setObjectName("button_clean_information_software_access")
        self.button_add_access_software_access = QtWidgets.QPushButton(self.new_login)
        self.button_add_access_software_access.setGeometry(QtCore.QRect(388, 570, 75, 81))
        self.button_add_access_software_access.setObjectName("button_add_access_software_access")
        self.line_software_access_3 = QtWidgets.QFrame(self.new_login)
        self.line_software_access_3.setGeometry(QtCore.QRect(470, 549, 20, 131))
        self.line_software_access_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access_3.setLineWidth(2)
        self.line_software_access_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_software_access_3.setObjectName("line_software_access_3")
        self.label_remove_access_by_register_id_staff_software_access = QtWidgets.QLabel(self.new_login)
        self.label_remove_access_by_register_id_staff_software_access.setGeometry(QtCore.QRect(830, 570, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_remove_access_by_register_id_staff_software_access.setFont(font)
        self.label_remove_access_by_register_id_staff_software_access.setObjectName("label_remove_access_by_register_id_staff_software_access")
        self.line_input_remove_access_by_staff_id_software_access = QtWidgets.QLineEdit(self.new_login)
        self.line_input_remove_access_by_staff_id_software_access.setGeometry(QtCore.QRect(920, 570, 61, 20))
        self.line_input_remove_access_by_staff_id_software_access.setObjectName("line_input_remove_access_by_staff_id_software_access")
        self.label_remove_access_software_access = QtWidgets.QLabel(self.new_login)
        self.label_remove_access_software_access.setGeometry(QtCore.QRect(870, 540, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_remove_access_software_access.setFont(font)
        self.label_remove_access_software_access.setObjectName("label_remove_access_software_access")
        self.line_software_access_4 = QtWidgets.QFrame(self.new_login)
        self.line_software_access_4.setGeometry(QtCore.QRect(810, 540, 51, 20))
        self.line_software_access_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access_4.setLineWidth(2)
        self.line_software_access_4.setMidLineWidth(0)
        self.line_software_access_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_software_access_4.setObjectName("line_software_access_4")
        self.line_software_access_5 = QtWidgets.QFrame(self.new_login)
        self.line_software_access_5.setGeometry(QtCore.QRect(800, 550, 20, 131))
        self.line_software_access_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access_5.setLineWidth(2)
        self.line_software_access_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_software_access_5.setObjectName("line_software_access_5")
        self.line_software_access_6 = QtWidgets.QFrame(self.new_login)
        self.line_software_access_6.setGeometry(QtCore.QRect(970, 540, 251, 20))
        self.line_software_access_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access_6.setLineWidth(2)
        self.line_software_access_6.setMidLineWidth(0)
        self.line_software_access_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_software_access_6.setObjectName("line_software_access_6")
        self.line_input_remove_access_by_document_id_software_access = QtWidgets.QLineEdit(self.new_login)
        self.line_input_remove_access_by_document_id_software_access.setGeometry(QtCore.QRect(880, 620, 101, 20))
        self.line_input_remove_access_by_document_id_software_access.setText("")
        self.line_input_remove_access_by_document_id_software_access.setObjectName("line_input_remove_access_by_document_id_software_access")
        self.label_remove_access_by_document_id_software_access = QtWidgets.QLabel(self.new_login)
        self.label_remove_access_by_document_id_software_access.setGeometry(QtCore.QRect(830, 620, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_remove_access_by_document_id_software_access.setFont(font)
        self.label_remove_access_by_document_id_software_access.setObjectName("label_remove_access_by_document_id_software_access")
        self.button_remove_access_software_access = QtWidgets.QPushButton(self.new_login)
        self.button_remove_access_software_access.setGeometry(QtCore.QRect(1024, 570, 171, 81))
        self.button_remove_access_software_access.setObjectName("button_remove_access_software_access")
        self.line_software_access_7 = QtWidgets.QFrame(self.new_login)
        self.line_software_access_7.setGeometry(QtCore.QRect(990, 550, 20, 131))
        self.line_software_access_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_software_access_7.setLineWidth(2)
        self.line_software_access_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_software_access_7.setObjectName("line_software_access_7")
        self.main_central_widget.addTab(self.new_login, "")
        staff_management_window.setCentralWidget(self.centralwidget)
        self.actionLimpiar_Datos = QtWidgets.QAction(staff_management_window)
        self.actionLimpiar_Datos.setObjectName("actionLimpiar_Datos")
        #############################################################################
        ##########################LOAD QWIDGETS##################################
        self.main_central_widget.currentChanged.connect(self.widgets_current_on)
        #############################Query##########################################
        self.query = Postgresqueries()
        ###############################################################################
        #################################Subjects Widget#############################
        ########################Subwindows############################################
        self.add_subject_window = None
        self.load_subject_widget()
        #################################################################################
        ######################Buttons subjects############################################
        self.button_add_subject.clicked.connect(self.add_subject_window_emergent)

        self.button_save_edit_staff.clicked.connect(self.get_data_update_edit_staff)
        ##################search qlines subjects################################
        self.lineedit_search_subject_name.textChanged.connect(self.filter_table_subject_name)
        self.lineedit_search_subject_id.textChanged.connect(self.filter_table_subject_id)
        

        ######Load data from database to show in qtablewidget subject############
        
        self.tablew_subject_show.cellClicked.connect(self.qtablew_row_clicked)

        ########################################################################

        ########################################################################
        #############################ADD STAFF WIDGET###########################
        #####################################################################
        self.combox_job_id_selection.currentIndexChanged.connect(self.show_widgets_add_staff)
        self.combox_job_id_selection.model().item(0).setEnabled(False)
        #########Frames hide###########
        self.frame_assign_grade.hide()
        self.frame_assign_subject.hide()
        self.frame_multi_selection_subjects.hide()
        self.frame_grades_assigned.hide()
        self.frame_output_information_grade_subject.hide()
        self.frame_output_information_will_save.hide()
        self.frame_teacher_selection.hide()
        ############################################################
        self.button_save_information_add_staff.clicked.connect(self.save_button_add_staff)

        self.button_clean_information.clicked.connect(self.clear_information_add_staff)
        ############################################################
        self.cb_highschool_teacher.stateChanged.connect(self.show_widgets_add_staff)
        self.cb_assign_subject.stateChanged.connect(self.show_widgets_add_staff)
        self.cb_assign_grade.stateChanged.connect(self.show_widgets_add_staff)





        ########################################################################
        ########################################################################
        ###################Edit staff widget####################################
        self.hide_edit_staff_widget()
        self.connect_signals()

        self.combobox_job_id_edit.model().item(0).setEnabled(False)

        #self.initial_date = self.date_edit_staff.date()
        ##################BUTTONS###########################
        self.button_search_edit_staff.clicked.connect(self.search_staff_button_edit_staff)

        ########Checkbox###############
        self.checkbox_if_teacher_edit_subjects_assigned.stateChanged.connect(self.show_data_subjects_teacher_editable)
        self.checkbox_if_teacher_edit_grades_assigned.stateChanged.connect(self.show_data_grades_teacher_editable)
        self.checkbox_if_high_school_teacher_edit_staff.stateChanged.connect(self.show_data_grades_teacher_editable)
        ########################################################################
        ########################################################################
        ########################################################################
        ########################################################################


        ########################################################################
        ###################LOGICAL DELETE STAFF#################################
        ########################################################################
        self.hide_frames_logical_delete_staff()
        
        ##################BUTTONS###############################################
        self.button_search_change_status_staff.clicked.connect(self.search_staff_button_logical_delete)
        self.button_change_status_delete.clicked.connect(self.logical_delete_button)
        self.button_chhange_status_restore.clicked.connect(self.logical_restore_button)
        self.button_clean_information_change_status.clicked.connect(self.clear_button_logical_delete)
        ########################################################################################
        ########################################################################################
        ################################Search Staff Table######################################
        ########################################################################################


        #####SIGNALS####
        self.line_input_full_name_search_staff.textChanged.connect(self.filter_search_staff)
        self.line_input_document_id_search_staff.textChanged.connect(self.filter_search_staff)
        self.line_input_phone_number_search_staff.textChanged.connect(self.filter_search_staff)

        #####Buttons####
        self.button_edit_selected_staff_search_staff.clicked.connect(self.edit_selected_staff)
        self.button_clear_information_search_staff.clicked.connect(self.clean_inputs_search_staff)
        self.button_show_details_qtable_selected_search_staff.clicked.connect(self.details_button_search_staff)

    ########################################################################################
    ########################################################################################
    ################################Impart Time assign######################################
    ########################################################################################

        ####Table context menu
        self.tablew_select_teacher_impart_tt.setContextMenuPolicy(3)  # 3 = Qt.CustomContextMenu
        self.tablew_select_teacher_impart_tt.customContextMenuRequested.connect(self.show_context_menu)

        ###combobox order/filter
        self.combox_filter_tablew_select_teacher_impart_tt.currentIndexChanged.connect(self.combox_filter_tablew_select_teacher_impart_tt_changed)

        ####Table signals
        self.tablew_select_teacher_impart_tt.cellClicked.connect(self.load_subject_selected_teacher)
        self.tablew_select_teacher_impart_tt.cellClicked.connect(self.load_grades_selected_teacher)
        self.tablew_select_teacher_impart_tt.cellClicked.connect(self.dynamic_label_details_impart_time)
        self.tablew_select_teacher_impart_tt.itemSelectionChanged.connect(self.enable_assign_save_button)

        ###Dynamic Labels
        self.timeedit_select_impart_start_time_impart_tt.timeChanged.connect(self.dynamic_label_details_impart_time)
        self.timeedit_select_impart_end_time_impart_tt.timeChanged.connect(self.dynamic_label_details_impart_time)

        ##Buttons signals
        self.button_save_information_selected_impart_tt.clicked.connect(self.assign_impart_time)
        self.button_save_information_selected_impart_tt.setEnabled(False)
        self.button_clean_information_selected_impart_tt.clicked.connect(self.clear_data_impart_time)
        self.button_unassign_time_selected_impart_tt.clicked.connect(self.unassign_all_subject_grades_impart_time)

        ###Listwidget signals
        self.listw_select_grade_impart_tt.itemSelectionChanged.connect(self.dynamic_label_details_impart_time)
        self.listw_select_subject_impart_tt.itemSelectionChanged.connect(self.dynamic_label_details_impart_time)

        ###Search qlines signals
        self.line_input_search_name_teacher_impart_tt.textChanged.connect(self.filter_search_impart_time)
        self.line_input_search_id_teacher_impart_tt.textChanged.connect(self.filter_search_impart_time)

        ############################################################################################
        ############################################################################################
        #################################ADD ACCESS WIDGET#########################################
        ############################################################################################

        self.line_input_search_by_register_id_staff_software_access.textChanged.connect(self.filter_search_access_staff)
        self.line_input_search_by_user_software_access.textChanged.connect(self.filter_search_access_staff)

        self.button_clean_information_software_access.clicked.connect(self.clear_inputs_add_staff_access)
        
        self.line_input_remove_access_by_staff_id_software_access.textChanged.connect(self.block_input_lines_add_access_staff)
        self.line_input_remove_access_by_document_id_software_access.textChanged.connect(self.block_input_lines_add_access_staff)

        self.button_add_access_software_access.clicked.connect(self.add_access_staff)
        self.button_remove_access_software_access.clicked.connect(self.remove_access_staff)
        self.retranslateUi(staff_management_window)
        self.main_central_widget.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(staff_management_window)
    
    ################################
    #####Subject widget actions#####
    ################################
    def filter_table_subject_name(self):
        search_text = self.lineedit_search_subject_name.text().strip().lower()
        for row in range(self.tablew_subject_show.rowCount()):
            item = self.tablew_subject_show.item(row, 1)
            if item and search_text in item.text().lower():
                self.tablew_subject_show.setRowHidden(row, False)
            else:
                self.tablew_subject_show.setRowHidden(row, True)

    def filter_table_subject_id(self):
        search_text = self.lineedit_search_subject_id.text().strip().lower()
        for row in range(self.tablew_subject_show.rowCount()):
            item = self.tablew_subject_show.item(row, 0)
            if item and search_text in item.text().lower():
                self.tablew_subject_show.setRowHidden(row, False)
            else:
                self.tablew_subject_show.setRowHidden(row, True)

    def load_data_subjects_main_central_widget(self):
        subject_rows = self.query.show_data_subjects()
        self.tablew_subject_show.setRowCount(0)

        for row_index, row in enumerate(subject_rows):
            self.tablew_subject_show.insertRow(row_index)
            self.tablew_subject_show.setItem(row_index, 0, QtWidgets.QTableWidgetItem(str(row[0]).capitalize()))
            self.tablew_subject_show.setItem(row_index, 1, QtWidgets.QTableWidgetItem(str(row[1]).capitalize()))
        
    def add_subject_window_emergent(self):
        if self.add_subject_window is None:
            self.add_subject_window = QtWidgets.QWidget()
            self.ui_add_subject = Ui_add_subject_sub_window()
            self.ui_add_subject.setupUi(self.add_subject_window)
        self.add_subject_window.show()

    def qtablew_row_clicked(self, row: int, column: int):
        id_item = self.tablew_subject_show.item(row, 0)

        if id_item and id_item.text().strip():
            self.button_delete_subject.setEnabled(True)
            self.button_edit_subject.setEnabled(True)
            try:
                self.id_value = int(id_item.text())
                try:
                    self.button_delete_subject.clicked.disconnect()
                except TypeError:
                    pass


                self.button_delete_subject.clicked.connect(lambda: self.delete_subject_action_button(self.id_value))
                self.button_edit_subject.clicked.connect(lambda: self.edit_subject_action_button(self.id_value))
            except ValueError:
                self.button_edit_subject.setEnabled(False)
                self.button_delete_subject.setEnabled(False)
        else:
            self.button_edit_subject.setEnabled(False)
            self.button_delete_subject.setEnabled(False)

    def delete_subject_action_button(self, id_value):
        try:
            if id_value:
                table = 'subjects'
                self.query.delete_data_from_table(table, id_value)
                self.query.show_data_subjects()
                self.tablew_subject_show.clearSelection()
                self.id_value = None
                self.button_delete_subject.setEnabled(False)
                self.button_edit_subject.setEnabled(False)
            
            else:
                return None
        except Exception as e:
            print(f"Error al intentar eliminar la materia: {e}")
    
    def edit_subject_action_button(self, id_value):
        if hasattr(self, "_edit_dialog_open") and self._edit_dialog_open:
            return
    
        row = self.find_row_by_id(id_value)
        if row is None:
            return
        
        current_item = self.tablew_subject_show.item(row, 1)
        if not current_item:
            return
        current_name = current_item.text()
        
        self._edit_dialog_open = True
        
        new_name, ok = QtWidgets.QInputDialog.getText(
            self.tablew_subject_show,
            "Editar Materia",
            "Nuevo nombre de la materia:",
            QtWidgets.QLineEdit.Normal,
            current_name
        )
        
        self._edit_dialog_open = False
        if ok and new_name.strip() and new_name != current_name:
            if not self.query.edit_subject_name(id_value, new_name.strip().lower()):
                id_subject_existing = self.query.get_subject_id_already_exists(new_name.strip().lower())
                QtWidgets.QMessageBox.information(
                    self.tablew_subject_show,
                    "Error al editar",
                    f"No se pudo editar la materia con id {id_subject_existing}. La materia ya existe con el mismo nombre."
                )
                self.id_value = None
                self.tablew_subject_show.clearSelection()
                self.button_edit_subject.setEnabled(False)
                self.button_delete_subject.setEnabled(False)
            else:
                self.load_data_subjects_main_central_widget()
                self.id_value = None
                self.tablew_subject_show.clearSelection()
                self.button_edit_subject.setEnabled(False)
                self.button_delete_subject.setEnabled(False)
    
    def find_row_by_id(self, id_value):
        for row in range(self.tablew_subject_show.rowCount()):
            item = self.tablew_subject_show.item(row, 0)
            if item and int(item.text()) == id_value:
                return row
        return None
    ########################################################################################

    ################################
    ####ADD Staff widget actions####
    ################################
    def calculate_age(self, birthdate):
        today = QDate.currentDate()
        age = today.year() - birthdate.year()
        if today.month() < birthdate.month() or (today.month() == birthdate.month() and today.day() < birthdate.day()):
            age -= 1
        
        return age
    
    def save_button_add_staff(self):
        first_name = str(self.line_input_fname.text()).strip().capitalize()
        second_name = str(self.line_input_sname.text()).strip().capitalize()
        first_surname = str(self.line_input_fsurname.text()).strip().capitalize()
        second_surname = str(self.line_input_ssurname.text()).strip().capitalize()
        self.document_id = str(self.line_input_document_id.text()).strip()
        address = str(self.line_input_address.text()).strip().capitalize()
        job_id = int(self.combox_job_id_selection.currentIndex())
        phone_number = str(self.line_input_phone_number.text()).strip()
        birthdate = self.birthdate_input_get.date()
        age = self.calculate_age(birthdate)

        second_name = second_name if second_name else None
        second_surname = second_name if second_name else None
        data_entry = [first_name, second_name, first_surname, second_surname]
        wrong_data = ("Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido")
        for i in range(len(data_entry)):
            if not string_input_data_validator(data_entry[i]):
                QtWidgets.QMessageBox.information(None, "Error", f"En este campo solo se admiten letras (Sin simbolos, espacios, caracteres especiales o numeros): {wrong_data[i]}")
                return
        
        second_name = second_name if second_name else ""
        second_surname = second_name if second_name else ""

        if not age_validator(age):
            QtWidgets.QMessageBox.information(None, "Error", "Edad invalida, debe ser mayor a 18 años")
            return


        if self.combox_job_id_selection.currentIndex() == 0:
            QtWidgets.QMessageBox.information(None, "Error", "Debe seleccionar un puesto de trabajo")
            return
        
        if not document_id_validation(self.document_id):
            new_document_id = rewrite_document_id(self.document_id)
            self.document_id = new_document_id 
            if not document_id_validation(self.document_id):
                QtWidgets.QMessageBox.information(None, "Error al agregar la cedula", "Formato de cedula erroneo, utiliza el siguiente formato XXX-XXXXXX-XXXXA o 1234567891234A")
                return

        saa = staff_add_action()
        if not saa.validate_document_id_repeated(self.document_id):
            QtWidgets.QMessageBox.information(None, "Error al agregar la cedula", "La cedula ya se encuentra registrada en la base de datos")
            return
        

        if not self.validate_data_input(first_name, first_surname, self.document_id, address, phone_number):
            return
        
        if not phone_number_validation(phone_number):
            QtWidgets.QMessageBox.information(None, "Error al agregar el numero de telefono", "Formato de numero de telefono erroneo, utiliza el siguiente formato 12345678")
            return

        if not self.validate_input_birthdate(birthdate):
            return
        
        birthdate = birthdate.toString("yyyy-MM-dd")

        self.frame_output_information_will_save.show()
        phone_number = rewrite_phone_number(phone_number)
        self.label_name_output.setText(first_name + " " + second_name)
        self.label_surname_output.setText(first_surname + " " + second_surname)
        self.label_address_output.setText(address)
        self.label_document_id_output.setText(self.document_id)
        self.label_phone_number_output.setText(phone_number)
        self.label_birthdate_output.setText(birthdate)
        self.label_age_output.setText(str(age))


        self.subject_assign_output_info.hide()
        self.grade_assign_output_info.hide()

        if job_id == 2:
            self.subject_assign_output_info.show()
            self.grade_assign_output_info.show()
            self.frame_output_information_grade_subject.show()

            grade_guide = self.qlistw_grade_assign.selectedItems()[0].text() if self.qlistw_grade_assign.selectedItems() else None
            grades_assigned = [item.text() for item in self.qlistw_grades_impart_selection.selectedItems()] if self.qlistw_grades_impart_selection.selectedItems() else None
            subjects_selected = [item.text() for item in self.qlistw_subject_selection.selectedItems()] if self.qlistw_subject_selection.selectedItems() else None
            main_subject_assigned = self.qlistw_subject_assign.selectedItems()[0].text() if self.qlistw_subject_assign.selectedItems() else None

            self.label_subject_assign_output.setText(main_subject_assigned)
            self.label_grade_assign_output.setText(grade_guide)
            if subjects_selected is not None:
                for i in range(len(subjects_selected)):
                    self.qlistw_selected_subjects.addItem(subjects_selected[i])
            
            if grades_assigned is not None:
                for i in range(len(grades_assigned)):
                    self.qlistw_selected_grade.addItem(grades_assigned[i])
        
        self.frame_confirmation_buttons.show()

        self.frame_buttons.setEnabled(False)
        self.frame_selection_data_add_staff.setEnabled(False)
        self.frame_entry_data_add_staff.setEnabled(False)
        self.frame_assign_grade.setEnabled(False)
        self.frame_assign_subject.setEnabled(False)
        self.frame_multi_selection_subjects.setEnabled(False)
        self.frame_grades_assigned.setEnabled(False)

        self.button_confirm_information_add_staff.clicked.connect(self.add_staff_button_save_action)
        self.button_cancelar_information_add_staff.clicked.connect(self.cancel_button_add_staff)

    def cancel_button_add_staff(self):
        self.frame_output_information_will_save.hide()
        self.frame_output_information_grade_subject.hide()
        self.frame_buttons.setEnabled(True)
        self.frame_selection_data_add_staff.setEnabled(True)
        self.frame_entry_data_add_staff.setEnabled(True)
        self.frame_assign_grade.setEnabled(True)
        self.frame_assign_subject.setEnabled(True)
        self.frame_multi_selection_subjects.setEnabled(True)
        self.frame_grades_assigned.setEnabled(True)

    def clear_information_add_staff(self):
        self.line_input_fname.clear()
        self.line_input_sname.clear()
        self.line_input_fsurname.clear()
        self.line_input_ssurname.clear()
        self.line_input_document_id.clear()
        self.line_input_address.clear()
        self.combox_job_id_selection.setCurrentIndex(0)
        self.line_input_phone_number.clear()
        self.birthdate_input_get.setDate(QDate.currentDate())

        self.cb_assign_grade.setChecked(False)
        self.cb_assign_subject.setChecked(False)
        self.cb_highschool_teacher.setChecked(False)

        self.frame_assign_grade.hide()
        self.frame_assign_subject.hide()
        self.frame_multi_selection_subjects.hide()
        self.frame_grades_assigned.hide()

        self.qlistw_grade_assign.clear()
        self.qlistw_subject_assign.clear()
        self.qlistw_subject_selection.clear()
        self.qlistw_grades_impart_selection.clear()

        self.qlistw_grade_assign.clearSelection()
        self.qlistw_subject_assign.clearSelection()
        self.qlistw_subject_selection.clearSelection()
        self.qlistw_grades_impart_selection.clearSelection()

        self.frame_output_information_will_save.hide()
        self.frame_teacher_selection.hide()

    def add_staff_button_save_action(self):
        first_name = str(self.line_input_fname.text()).strip().lower()
        second_name = str(self.line_input_sname.text()).strip().lower()
        first_surname = str(self.line_input_fsurname.text()).strip().lower()
        second_surname = str(self.line_input_ssurname.text()).strip().lower()
        document_id = self.document_id
        address = str(self.line_input_address.text()).strip().lower()
        job_id = int(self.combox_job_id_selection.currentIndex())
        phone_number = str(self.line_input_phone_number.text()).strip()
        birthdate = self.birthdate_input_get.date()
        

        birthdate = birthdate.toString("yyyy-MM-dd")
        if job_id == 2:

            grade_guide = self.qlistw_grade_assign.selectedItems()[0].text() if self.qlistw_grade_assign.selectedItems() else None
            grades_assigned = [item.text() for item in self.qlistw_grades_impart_selection.selectedItems()] if self.qlistw_grades_impart_selection.selectedItems() else None
            subjects_selected = [item.text() for item in self.qlistw_subject_selection.selectedItems()] if self.qlistw_subject_selection.selectedItems() else None
            main_subject_assigned = self.qlistw_subject_assign.selectedItems()[0].text() if self.qlistw_subject_assign.selectedItems() else None
            
            self.add_staff_query_if_teacher(first_name, second_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthdate, grade_guide, grades_assigned, subjects_selected, main_subject_assigned)
            QtWidgets.QMessageBox.information(None, "Profesor agregado", "El profesor fue agregado a la base de datos con exito")
        else:
            
            self.add_staff_query(first_name, second_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthdate)
            QtWidgets.QMessageBox.information(None, "Personal agregado", "El personal fue agregado a la base de datos con exito")  

    def add_staff_query(self, first_name, second_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthdate):
        try:
            if self.query.insert_staff(first_name, second_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthdate):
                self.line_input_fname.clear()
                self.line_input_sname.clear()
                self.line_input_fsurname.clear()
                self.line_input_ssurname.clear()
                self.line_input_document_id.clear()
                self.line_input_address.clear()
                self.line_input_phone_number.clear()

                self.combox_job_id_selection.setCurrentIndex(0)

                self.cancel_button_add_staff()
                return True

        except Exception as e:
            print(f"Error al intentar agregar al personal: {e}")
            return False
        
    def add_staff_query_if_teacher(self, first_name, second_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthdate ,guide_grade, grades_selected ,subjects_selected, main_subject_assigned): #Specific fuctions and query for insert staff if is teahcer
        try:
            if self.query.insert_staff_if_teacher(first_name, second_name, first_surname, second_surname, document_id, address, job_id, phone_number, birthdate ,guide_grade, grades_selected, subjects_selected, main_subject_assigned):
                self.line_input_fname.clear()
                self.line_input_sname.clear()
                self.line_input_fsurname.clear()
                self.line_input_ssurname.clear()
                self.line_input_document_id.clear()
                self.line_input_address.clear()
                self.line_input_phone_number.clear()

                self.combox_job_id_selection.setCurrentIndex(0)

                self.frame_teacher_selection.hide()
                self.cb_assign_grade.setChecked(False)
                self.cb_assign_subject.setChecked(False)
                self.cb_highschool_teacher.setChecked(False)

                self.frame_assign_grade.hide()
                self.qlistw_grade_assign.clear()
                self.qlistw_grade_assign.clearSelection()

                self.frame_assign_subject.hide()
                self.qlistw_subject_assign.clear()
                self.qlistw_subject_assign.clearSelection()

                self.frame_multi_selection_subjects.hide()
                self.qlistw_subject_selection.clear()
                self.qlistw_subject_selection.clearSelection()

                self.frame_grades_assigned.hide()
                self.qlistw_grades_impart_selection.clear()
                self.qlistw_grades_impart_selection.clearSelection()

                self.cancel_button_add_staff()
                return True

        except Exception as e:
            print(f"Error al intentar agregar al personal como profesor: {e}")
            return False
  
    def validate_data_input(self, first_name, first_surname, document_id, address, phone_number):
        if not self.validate_data_input_required(first_name, first_surname, document_id, address, phone_number):
            return False


        if not phone_number.isdigit():
            QtWidgets.QMessageBox.warning(None, "Formato incorrecto", "El teléfono debe contener solo números.")
            return False

        return True
    
    def validate_data_input_required(self, first_name, first_surname, document_id, address, phone_number):

        campos = [
            ("Primer Nombre", first_name),
            ("Primer Apellido", first_surname),
            ("Cedula", document_id),
            ("Direccion", address),
            ("Numero de telefono", phone_number)
        ]
        

        campos_faltantes = [nombre for nombre, valor in campos if not valor]
        

        if campos_faltantes:
            mensaje = "Los siguientes campos son obligatorios:\n\n" + "\n".join(campos_faltantes)
            QtWidgets.QMessageBox.warning(None, "Datos incompletos", mensaje)
            return False
        
        return True
    
    def validate_input_birthdate(self, birthdate_date):
        selected_date = birthdate_date
        if birthdate_date.year() < 1900:
            QtWidgets.QMessageBox.warning(None, "Fecha invalida", "Debe seleccionar una fecha válida.")
            return False
        
        if selected_date >= QDate.currentDate():
            QtWidgets.QMessageBox.warning(None, "Fecha invalida", "No puede seleccionar la fecha actual.")
            return False
        return True

    def show_widgets_add_staff(self):
        self.combo_box_job_id = self.combox_job_id_selection.currentIndex()
        match self.combo_box_job_id:
            case 1:
                self.hide_all_frames_add_staff()


            case 2:
                self.handle_teacher_selection()
                

            case 3:
                self.hide_all_frames_add_staff()

    def handle_teacher_selection(self):
        self.frame_teacher_selection.show()

        if self.cb_highschool_teacher.isChecked():
            self.frame_multi_selection_subjects.show()
            self.frame_grades_assigned.show()
            if not self.grades_loaded:
                high_school_teacher = True
                self.load_grades(high_school_teacher)
                self.load_subject_assign_add_staff()
                self.grades_loaded = True
        else:
            self.frame_multi_selection_subjects.hide()
            self.frame_grades_assigned.hide()
            self.qlistw_grades_impart_selection.clearSelection()
            self.qlistw_grades_impart_selection.clear()
            self.grades_loaded = False
            self.qlistw_subject_selection.clearSelection()
            self.qlistw_subject_selection.clear()

        if self.cb_assign_subject.isChecked():
            if not self.load_main_subject_teacher:
                self.frame_assign_subject.show()
                self.load_subject_main_assign_add_staff()
                self.load_main_subject_teacher = True


        else:
            self.frame_assign_subject.hide()
            self.qlistw_subject_assign.clear()
            self.qlistw_subject_assign.clearSelection()
            self.load_main_subject_teacher = False

        if self.cb_assign_grade.isChecked():
            self.frame_assign_grade.show()

            if self.cb_highschool_teacher.isChecked():
                if not self.grades_guide_loaded:
                    self.qlistw_grade_assign.clearSelection()
                    self.qlistw_grade_assign.clear()
                    high_school_teacher = True
                    self.load_grades_guide(high_school_teacher)
                    self.grades_guide_loaded = True

                elif self.cb_highschool_teacher.isChecked() and self.grades_guide_loaded:
                    self.grades_guide_loaded = False
                    self.qlistw_grade_assign.clear()
                    self.qlistw_grade_assign.clearSelection()
                    high_school_teacher = True
                    self.load_grades_guide(high_school_teacher)
                    self.grades_guide_loaded = True
                
            elif not self.cb_highschool_teacher.isChecked() and self.grades_guide_loaded:
                self.grades_guide_loaded = False
                self.qlistw_grade_assign.clear()
                self.qlistw_grade_assign.clearSelection()
                high_school_teacher = False
                self.load_grades_guide(high_school_teacher)
                self.grades_guide_loaded = True


            else:
                if not self.grades_guide_loaded:
                    self.qlistw_grade_assign.clearSelection()
                    self.qlistw_grade_assign.clear()
                    high_school_teacher = False
                    self.load_grades_guide(high_school_teacher)
                    self.grades_guide_loaded = True
        else:
            self.frame_assign_grade.hide()
            self.qlistw_grade_assign.clearSelection()
            self.qlistw_grade_assign.clear()
            self.grades_guide_loaded = False

    def hide_all_frames_add_staff(self):
        self.frame_assign_grade.hide()
        self.frame_assign_subject.hide()
        self.frame_multi_selection_subjects.hide()
        self.frame_grades_assigned.hide()
        self.frame_output_information_grade_subject.hide()
        self.frame_output_information_will_save.hide()
        self.frame_teacher_selection.hide()
        self.frame_confirmation_buttons.hide()

    def load_grades_guide(self, high_school_teacher):
        if self.grades_guide_loaded:
            return
        
        rows = self.query.show_data_grades_guide(high_school_teacher)
        for row in rows:
            self.qlistw_grade_assign.addItem(row[0])
    
    def load_grades(self, high_school_teacher):
        if self.grades_loaded:
            return
        rows = self.query.show_data_grades_all(high_school_teacher)
        for row in rows:
            self.qlistw_grades_impart_selection.addItem(row[0])
    
    def load_subject_main_assign_add_staff(self):
        if self.load_main_subject_teacher:
            return
        rows = self.query.show_data_subjects()
        for row in rows:
            self.qlistw_subject_assign.addItem(row[1])
    
    def load_subject_assign_add_staff(self):
        rows = self.query.show_data_subjects()
        for row in rows:
            self.qlistw_subject_selection.addItem(row[1])

    ###############################################
    #######Edit_staff_widget actions###############
    ###############################################
    def search_staff_button_edit_staff(self):
        try:
            id_search = int(self.line_input_edit_staff_search_id.text()) if self.line_input_edit_staff_search_id.text() else None
            document_id_search = str(self.line_input_edit_staff_search_document_id.text()) if self.line_input_edit_staff_search_document_id.text() else None

            if document_id_search is not None:
                if not document_id_validation(document_id_search):
                    document_id_search = rewrite_document_id(document_id_search)
                    if not document_id_validation(document_id_search):
                        QtWidgets.QMessageBox.information(None, "Error Cedula", "Formato de cedula ingresado es erroneo, utiliza el siguiente formato XXX-XXXXXX-XXXXA o 1234567891234A")
                        self.clear_label_output_edit()
                        self.frame_edit_info.hide()
                        return
                    
            self.sega = staff_edit_gui_action()
            self.results = self.sega.entry_data_search_query(id_search, document_id_search)

            if not self.results:
                QtWidgets.QMessageBox.information(None, "Error", "No se encontraron resultados para la busqueda")
                self.clear_label_output_edit()
                self.frame_edit_info.hide()
                return
            

            

            self.clear_label_output_edit()
            self.staff_id_edit_staff = self.results[0]
            first_name = self.results[1]
            second_name = self.results[2]
            first_surname = self.results[3]
            second_surname = self.results[4]

            split_name = [first_name, second_name, first_surname, second_surname]
            split_name = [name.capitalize() for name in split_name if name is not None]
            full_name = " ".join(split_name)

            staff_id_registered = self.results[0]
            document_id = self.results[5]
            address = self.results[6]

            phone_number = self.results[9]
            phone_number = rewrite_phone_number(phone_number)

            birthdate = self.results[10]
            show_birthdate = birthdate.strftime('%d-%m-%Y')

            self.initial_date = birthdate
            self.date_edit_staff.setDate(birthdate)

            job_id = self.results[7]

            job_position = self.sega.job_position_get(staff_id_registered)

            age = str(self.calculate_age_edit_staff(birthdate))

            self.label_full_name_dynamic_edit.setText(full_name)
            self.label_document_id_dynamic_edit.setText(document_id)
            self.label_address_dynamic_edit.setText(address)
            self.label_phone_number_dynamic_edit.setText(phone_number)
            self.label_job_id_dynamic_edit.setText(job_position)
            self.label_birthdate_dynamic_edit.setText(show_birthdate)
            self.label_age_dynamic_edit.setText(age)
            self.combobox_job_id_edit.setCurrentIndex(job_id)
            if job_id == 2:
                self.frame_if_teacher.show()
                self.checkbox_if_teacher_edit_grades_assigned.show()
                self.checkbox_if_teacher_edit_subjects_assigned.show()
                self.checkbox_if_high_school_teacher_edit_staff.show()
                self.show_data_subjects_teacher_editable()
                self.show_data_grades_teacher_editable()


                main_subject, main_grade = self.sega.main_teacher_has(staff_id_registered)

                self.label_if_teacher_main_subject_dynamic.setText(main_subject)
                self.label_if_teacher_assigned_grade_dynamic.setText(main_grade)

                subjects_assigned = self.sega.impart_subjects(staff_id_registered)
                grades_assigned = self.sega.grades_assigned(staff_id_registered)

                subject_count = self.qlist_if_teacher_subjects_assigned.count()
                grade_count = self.qlist_if_teacher_grades_assigned.count()
                
                if subject_count > 0:
                    self.qlist_if_teacher_subjects_assigned.clear()

                for subject in subjects_assigned:
                    self.qlist_if_teacher_subjects_assigned.addItem(subject)
                
                if grade_count > 0:
                    self.qlist_if_teacher_grades_assigned.clear()

                for grade in grades_assigned:
                    self.qlist_if_teacher_grades_assigned.addItem(grade)
                
                self.teacher_data_grades_and_subjects_edit = [main_subject, main_grade, subjects_assigned, grades_assigned]

                high_school_teacher_state_edit_staff = self.sega.get_bool_primary_teacher(self.results[0])
                self.checkbox_if_high_school_teacher_edit_staff.setChecked(high_school_teacher_state_edit_staff)



            else:
                self.frame_if_teacher.hide()
                self.checkbox_if_teacher_edit_grades_assigned.hide()
                self.checkbox_if_teacher_edit_subjects_assigned.hide()
                self.checkbox_if_high_school_teacher_edit_staff.hide()

                self.label_if_teacher_main_subject_dynamic.clear()
                self.label_if_teacher_assigned_grade_dynamic.clear()
                self.qlist_if_teacher_subjects_assigned.clear()
                self.qlist_if_teacher_grades_assigned.clear()
            
            self.old_data_edit = {
            'first_name' : first_name, 
            'middle_name' : second_name, 
            'first_surname' : first_surname, 
            'second_surname' : second_surname, 
            'document_id' : document_id, 
            'address' : address, 
            'job_id' : job_position, 
            'phone_number' : phone_number, 
            'birthday' : show_birthdate
            }

            self.frame_edit_info.show()
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")
        
    def clear_label_output_edit(self):
        self.label_full_name_dynamic_edit.clear()
        self.label_document_id_dynamic_edit.clear()
        self.label_address_dynamic_edit.clear()
        self.label_phone_number_dynamic_edit.clear()
        self.label_job_id_dynamic_edit.clear()
        self.label_birthdate_dynamic_edit.clear()
        self.label_age_dynamic_edit.clear()
        
        self.frame_if_teacher.hide()

        self.label_if_teacher_main_subject_dynamic.clear()
        self.label_if_teacher_assigned_grade_dynamic.clear()
        self.qlist_if_teacher_subjects_assigned.clear()
        self.qlist_if_teacher_grades_assigned.clear()

        self.clean_information_edit_staff()

    def calculate_age_edit_staff(self, birthdate):
        today = date.today()
        age = today.year - birthdate.year

        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age
    
    def hide_edit_staff_widget(self):
        self.frame_if_teacher.hide()
        self.frame_edit_info.hide()
        self.frame_if_edit_subject_or_grades.hide()
        self.frame_buttons_edit.hide()
        self.checkbox_if_teacher_edit_subjects_assigned.hide()
        self.checkbox_if_teacher_edit_grades_assigned.hide()
        self.label_selections_grades_edit.hide()
        self.listw_input_grades_edit.hide()
        self.listw_input_subjects_edit.hide()
        self.label_selection_subjects_edit.hide()
        self.label_selection_main_subject_edit.hide()
        self.combobox_main_subject_edit.hide()
        self.label_selection_guide_grade_edit.hide()
        self.combobox_guide_grade_edit.hide()

    def show_data_subjects_teacher_editable(self):
        if self.checkbox_if_teacher_edit_subjects_assigned.isChecked():
            QtWidgets.QMessageBox.information(None, "Advertencia", "Al marcar esta casilla las materias asignadas al profesor seleccionado, se le removeran, puede seleccionar nuevas o mismas materias, o dejar la casilla marcada")
            self.frame_if_edit_subject_or_grades.show()
            self.label_selection_subjects_edit.show()
            self.listw_input_subjects_edit.show()
            self.label_selection_main_subject_edit.show()
            self.combobox_main_subject_edit.show()
            if not self.load_subjects_options_flag:
                self.load_all_subjects_options_edit_staff()
                self.load_subjects_options_flag = True
        else:
            self.listw_input_subjects_edit.clear()
            self.listw_input_subjects_edit.clearSelection()
            self.combobox_main_subject_edit.clear()
            self.label_selection_subjects_edit.hide()
            self.listw_input_subjects_edit.hide()
            self.label_selection_main_subject_edit.hide()
            self.combobox_main_subject_edit.hide()
            self.load_subjects_options_flag = False

    def show_data_grades_teacher_editable(self):
        if self.checkbox_if_teacher_edit_grades_assigned.isChecked():
            QtWidgets.QMessageBox.information(None, "Adventencia", "Al marcar esta casilla, los grados asignados y grado guiado se removeran del profesor seleccionado, y si selecciona los grados asignados y el grado guiado, estos se les agregara al profesor")
            self.frame_if_edit_subject_or_grades.show()
            self.label_selections_grades_edit.show()
            self.listw_input_grades_edit.show()
            self.label_selection_guide_grade_edit.show()
            self.combobox_guide_grade_edit.show()
            
            if self.checkbox_if_high_school_teacher_edit_staff.isChecked():
                high_school_teacher = True
                if not self.load_grades_options_flag:
                    self.clear_grades_and_combobox_edit_staff()
                    self.load_all_grades_options_edit_staff(high_school_teacher)
                    self.load_grades_options_flag = True
                
                elif self.load_grades_options_flag:
                    self.load_grades_options_flag = False
                    self.clear_grades_and_combobox_edit_staff()
                    self.load_all_grades_options_edit_staff(high_school_teacher)
                    self.load_grades_options_flag = True
            
            elif not self.checkbox_if_high_school_teacher_edit_staff.isChecked() and self.load_grades_options_flag:
                self.load_grades_options_flag = False
                self.clear_grades_and_combobox_edit_staff()
                high_school_teacher = False
                self.load_all_grades_options_edit_staff(high_school_teacher)
                self.load_grades_options_flag = True
            
            else:
                if not self.load_grades_options_flag:
                    high_school_teacher = False
                    self.clear_grades_and_combobox_edit_staff()
                    self.load_all_grades_options_edit_staff(high_school_teacher)
                    self.load_grades_options_flag = True

        else:
            self.listw_input_grades_edit.clear()
            self.listw_input_grades_edit.clearSelection()
            self.combobox_guide_grade_edit.clear()
            self.label_selections_grades_edit.hide()
            self.listw_input_grades_edit.hide()
            self.label_selection_guide_grade_edit.hide()
            self.combobox_guide_grade_edit.hide()
            self.load_grades_options_flag = False
    
    def enable_buttons_edit(self):
        fields_changed = [
            self.line_input_first_name_edit.text(),
            self.line_input_second_name_edit.text(),
            self.line_input_first_surname_edit.text(),
            self.line_input_second_surname_edit.text(),
            self.line_input_document_id_edit.text(),
            self.line_input_phone_number_edit.text(),
            self.line_input_address_edit.text()
        ]

        date_changed = self.date_edit_staff.date() != self.initial_date
        index_changed = self.combobox_job_id_edit.currentIndex() != self.results[7] if self.results else 0

        if any(fields_changed) or index_changed or date_changed or self.checkbox_if_teacher_edit_grades_assigned.isChecked() or self.checkbox_if_teacher_edit_subjects_assigned.isChecked():
            self.frame_buttons_edit.show()
        else:
            self.frame_buttons_edit.hide()
        
    def connect_signals(self):
        self.line_input_first_name_edit.textChanged.connect(self.enable_buttons_edit)
        self.line_input_second_name_edit.textChanged.connect(self.enable_buttons_edit)
        self.line_input_first_surname_edit.textChanged.connect(self.enable_buttons_edit)
        self.line_input_second_surname_edit.textChanged.connect(self.enable_buttons_edit)
        self.line_input_document_id_edit.textChanged.connect(self.enable_buttons_edit)
        self.line_input_phone_number_edit.textChanged.connect(self.enable_buttons_edit)
        self.line_input_address_edit.textChanged.connect(self.enable_buttons_edit)

        self.checkbox_if_teacher_edit_grades_assigned.stateChanged.connect(self.enable_buttons_edit)
        self.checkbox_if_teacher_edit_subjects_assigned.stateChanged.connect(self.enable_buttons_edit)
        self.checkbox_if_high_school_teacher_edit_staff.stateChanged.connect(self.enable_buttons_edit)

        self.combobox_job_id_edit.currentIndexChanged.connect(self.enable_buttons_edit)

        self.date_edit_staff.dateChanged.connect(self.enable_buttons_edit)

    def load_all_grades_options_edit_staff(self, high_school_bool):
        try:
            if self.load_grades_options_flag:
                return
            self.load_grades_edit_staff(high_school_bool)
            self.load_combobox_options_grade_guide(high_school_bool)
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")

    def load_grades_edit_staff(self, high_school_teacher):
        try:
            results = self.query.show_data_grades_all(high_school_teacher)

            if results and results[0] is not None:
                for result in results:
                    self.listw_input_grades_edit.addItems([result[0]])
            else:
                self.listw_input_grades_edit.addItems(["Sin Resultados"])
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")
    
    def clear_grades_and_combobox_edit_staff(self):
        self.listw_input_grades_edit.clear()
        self.listw_input_grades_edit.clearSelection()

        self.combobox_guide_grade_edit.clear()
        self.combobox_guide_grade_edit.setCurrentIndex(0)

    def load_subjects_edit_staff(self):
        try:
            results = self.query.show_data_subjects()

            if results and results[1] is not None:
                for result in results:
                    self.listw_input_subjects_edit.addItem(result[1])
            else:
                self.listw_input_subjects_edit.addItems(["Sin Resultados"])
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")

    def load_all_subjects_options_edit_staff(self):
        try:
            if self.load_subjects_options_flag:
                return
            self.load_subjects_edit_staff()
            self.load_combobox_options_main_subject()
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")

    def load_combobox_options_grade_guide(self, high_school_teacher):
        try:
            results = self.query.show_data_grades_guide(high_school_teacher)

            if results and results[0] is not None:
                self.combobox_guide_grade_edit.addItem("")
                for result in results:
                    self.combobox_guide_grade_edit.addItem(result[0])

            else:
                self.combobox_guide_grade_edit.addItem("Sin Resultados")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")

    def load_combobox_options_main_subject(self):
        try:
            results = self.query.show_data_subjects()
            if results and results[1] is not None:
                self.combobox_main_subject_edit.addItem("")
                for result in results:
                    self.combobox_main_subject_edit.addItem(result[1])
            else:
                self.combobox_main_subject_edit.addItem("Sin Resultados")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")
    
    def clean_information_edit_staff(self):
        self.line_input_first_name_edit.clear()
        self.line_input_second_name_edit.clear()
        self.line_input_first_surname_edit.clear()
        self.line_input_second_surname_edit.clear()
        self.line_input_document_id_edit.clear()
        self.line_input_phone_number_edit.clear()
        self.line_input_address_edit.clear()
        self.combobox_job_id_edit.setCurrentIndex(0)

        self.checkbox_if_teacher_edit_subjects_assigned.setChecked(False)
        self.checkbox_if_teacher_edit_grades_assigned.setChecked(False)
        self.frame_buttons_edit.hide()

    def get_data_update_edit_staff(self):
        first_name = str(self.line_input_first_name_edit.text()) if self.line_input_first_name_edit.text().strip() else None
        second_name = str(self.line_input_second_name_edit.text()) if self.line_input_second_name_edit.text().strip() else None
        first_surname = str(self.line_input_first_surname_edit.text()) if self.line_input_first_surname_edit.text().strip() else None
        second_surname = str(self.line_input_second_surname_edit.text()) if self.line_input_second_surname_edit.text().strip() else None
        address = str(self.line_input_address_edit.text()) if self.line_input_address_edit.text().strip() else None

        data_entry_update = [first_name, second_name, first_surname, second_surname]
        wrong_data = ("Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido")
        for i in range(len(data_entry_update)):
            if not string_input_data_validator(data_entry_update[i]):
                QtWidgets.QMessageBox.information(None, "Error", f"En este campo solo se admiten letras (Sin simbolos, espacios, caracteres especiales o numeros): {wrong_data[i]}")
                return

        document_id = str(self.line_input_document_id_edit.text()) if self.line_input_document_id_edit.text() else None
        if document_id is not None:
            if not document_id_validation(document_id):
                new_document_id = rewrite_document_id(document_id)
                document_id = new_document_id 
                if not document_id_validation(document_id):
                    QtWidgets.QMessageBox.information(None, "Error al guardar la cedula", "Formato de cedula erroneo, utiliza el siguiente formato XXX-XXXXXX-XXXXA o 1234567891234A")
                    return
            
            saa = staff_add_action()
            if not saa.validate_document_id_repeated(document_id):
                QtWidgets.QMessageBox.information(None, "Error al guardar", "La cedula ya se encuentra registrada en la base de datos")
                return
        
        phone_number = str(self.line_input_phone_number_edit.text()) if self.line_input_phone_number_edit.text() else None
        if phone_number is not None:
            if not phone_number_validation(phone_number):
                QtWidgets.QMessageBox.information(None, "Error al guardar el numero de telefono", "Formato de numero de telefono erroneo, utiliza el siguiente formato 12345678")
                return

        new_job_position = self.combobox_job_id_edit.currentIndex() if self.results[7] != self.combobox_job_id_edit.currentIndex() else self.results[7]

        new_birthdate = self.date_edit_staff.date() if self.date_edit_staff.date() != self.initial_date else self.initial_date
        if isinstance (new_birthdate, QDate):
            if not self.validate_input_birthdate(new_birthdate): #Fuction in line #1937
                return
            new_birthdate = new_birthdate.toString('yyyy-MM-dd')
        

        age = calculate_age_edited(new_birthdate)


        if age < 18:
            QtWidgets.QMessageBox.information(None, "Edad Invalida", "Debe ser mayor de 18")
            return
        
        if new_job_position == 2:
            if self.checkbox_if_teacher_edit_subjects_assigned.isChecked():
                new_subjects_assigned = [item.text() for item in self.listw_input_subjects_edit.selectedItems()] if self.listw_input_subjects_edit.selectedItems() else None
                new_subject_main_assigned = self.combobox_main_subject_edit.currentText() if self.combobox_main_subject_edit.currentText() else None
            else:
                if hasattr(self, 'teacher_data_grades_and_subjects_edit') and self.teacher_data_grades_and_subjects_edit:
                    new_subjects_assigned = self.teacher_data_grades_and_subjects_edit[2]
                    new_subject_main_assigned = self.teacher_data_grades_and_subjects_edit[0]
                else:
                    new_subjects_assigned = None
                    new_subject_main_assigned = None
            
            if self.checkbox_if_teacher_edit_grades_assigned.isChecked():
                new_grades_assigned = [item.text() for item in self.listw_input_grades_edit.selectedItems()] if self.listw_input_grades_edit.selectedItems() else None
                new_grade_guide_assigned = self.combobox_guide_grade_edit.currentText() if self.combobox_guide_grade_edit.currentText() else None
            else:
                if hasattr(self, 'teacher_data_grades_and_subjects_edit') and self.teacher_data_grades_and_subjects_edit:
                    new_grades_assigned =  self.teacher_data_grades_and_subjects_edit[3]
                    new_grade_guide_assigned = self.teacher_data_grades_and_subjects_edit[1]
                else:
                    new_grades_assigned = None
                    new_grade_guide_assigned = None
            

        new_values = {
            'first_name' : first_name, 
            'middle_name' : second_name, 
            'first_surname' : first_surname, 
            'second_surname' : second_surname, 
            'document_id' : document_id, 
            'address' : address, 
            'job_id' : new_job_position, 
            'phone_number' : phone_number, 
            'birthday' : new_birthdate
        }

        if new_job_position == 2:
            dialog_show_subjects_and_grades_saved = TeacherAssignmentDialogEditStaff(new_subject_main_assigned, new_grade_guide_assigned, new_subjects_assigned, new_grades_assigned, None)
            dialog_show_subjects_and_grades_saved.exec_()
        
        dialog_show_data_saved = EditDialogEditStaff(self.old_data_edit,new_values , None)
        
        result = dialog_show_data_saved.exec_()
        if result == QDialog.Accepted:
            try:
                new_values_cleaned = {}
                for key, value in new_values.items():
                    if value is not None:
                        new_values_cleaned[key] = value

                        if value == self.results[7]:
                            new_values_cleaned.pop('job_id')
                        
                        if value == self.results[10]:
                            new_values_cleaned.pop('birthday')
                        
                if new_job_position == 2:
                    staff_id = self.results[0]
                    if self.checkbox_if_teacher_edit_subjects_assigned.isChecked():

                        self.query.edit_subjects_teacher_assigned(new_subject_main_assigned, new_subjects_assigned, staff_id)
                    
                    if self.checkbox_if_teacher_edit_grades_assigned.isChecked():

                        self.query.edit_grades_teacher_assigned(new_grade_guide_assigned, new_grades_assigned, staff_id)
                    
                    if self.checkbox_if_high_school_teacher_edit_staff.isChecked():
                        high_school_teacher = False
                        self.sega.verify_and_change_primary_teacher_bool(high_school_teacher, self.results[0])
                    else:
                        high_school_teacher = True
                        self.sega.verify_and_change_primary_teacher_bool(high_school_teacher, self.results[0])

                        
                self.query.search_query('staff', self.results[0], None, None)
                self.query.edit_multiple_columns(new_values_cleaned)
                QtWidgets.QMessageBox.information(None, "Datos actualizados", "Los datos han sido actualizados")
                self.clear_label_output_edit()
                self.search_staff_button_edit_staff()
            except Exception as e:
                print(f'Error: {e}')
        else:
            print("Cambios cancelados")

    ########################################################################################
    ########################################################################################
    ################################LOGICAL DELETE STAFF####################################
    ########################################################################################
    def search_staff_button_logical_delete(self):
        try:
            id_search = int(self.line_input_change_status_staff_search_id.text()) if self.line_input_change_status_staff_search_id.text() else None
            document_id_search = str(self.line_input_change_status_staff_search_document_id.text()) if self.line_input_change_status_staff_search_document_id.text() else None

            if document_id_search is not None:
                if not document_id_validation(document_id_search):
                    document_id_search = rewrite_document_id(document_id_search)
                    if not document_id_validation(document_id_search):
                        QtWidgets.QMessageBox.information(None, "Error Cedula", "Formato de cedula ingresado es erroneo, utiliza el siguiente formato XXX-XXXXXX-XXXXA o 1234567891234A")
                        return
                    
            self.lds = logical_delete_staff()
            results = self.lds.entry_data_search_query_lds(id_search, document_id_search)

            if not results:
                QtWidgets.QMessageBox.information(None, "Error", "No se encontraron resultados para la busqueda")
                return
            

            
            self.lds_staff_id = results[0]
            first_name = results[1]
            second_name = results[2]
            first_surname = results[3]
            second_surname = results[4]

            split_name = [first_name, second_name, first_surname, second_surname]
            split_name = [name.capitalize() for name in split_name if name is not None]
            full_name = " ".join(split_name)

            staff_id_registered = results[0]
            document_id = results[5]
            address = results[6]

            phone_number = results[9]
            phone_number = rewrite_phone_number(phone_number)

            birthdate = results[10]
            show_birthdate = birthdate.strftime('%d-%m-%Y')

            job_id = results[7]

            job_position = self.lds.job_position_get_lds(staff_id_registered)

            age = str(self.calculate_age_edit_staff(birthdate))

            self.label_full_name_dynamic_change_status.setText(full_name)
            self.label_document_id_dynamic_change_status.setText(document_id)
            self.label_address_dynamic_change_status.setText(address)
            self.label_phone_number_dynamic_change_status.setText(phone_number)
            self.label_job_id_dynamic_change_status.setText(job_position)
            self.label_birthdate_dynamic_change_status.setText(show_birthdate)
            self.label_age_dynamic_change_status.setText(age)

            status_lds = self.lds.get_status(self.lds_staff_id)
            self.label_status_dynamic_change_status.setText(status_lds)
            
            self.frame_change_status_staff_outputinfo.show()

            if job_id == 2:
                self.frame_if_teacher_change_status_staff.show()

                guide_grade = self.lds.get_grade_guide(self.lds_staff_id)

                impart_time_teacher = self.lds.get_info_impart_time_teacher(self.lds_staff_id)

                self.tablew_change_status_if_teacher_grades_assigned.setRowCount(len(impart_time_teacher))

                for row_index, row_data in enumerate(impart_time_teacher):
                    for col_index, cell_data in enumerate(row_data):

                        if isinstance(cell_data, time):
                            cell_data = cell_data.strftime("%H:%M")
                        elif cell_data is None:
                            cell_data = "N/A"

                        item = QtWidgets.QTableWidgetItem(str(cell_data))
                        self.tablew_change_status_if_teacher_grades_assigned.setItem(row_index, col_index, item)
                self.tablew_change_status_if_teacher_grades_assigned.resizeColumnsToContents()
                self.label_grade_guide_if_teacher_change_status_dynamic.setText(guide_grade)




            else:
                self.frame_if_teacher_change_status_staff.hide()
                self.tablew_change_status_if_teacher_grades_assigned.clear()
                self.tablew_change_status_if_teacher_grades_assigned.clearSelection()

            self.frame_buttons_change_status.show()

            self.enable_disable_buttons_logical_delete(self.lds_staff_id)
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            QtWidgets.QMessageBox.information(None, "Error", "Error al cargar los datos")
    
    def hide_frames_logical_delete_staff(self):
        self.frame_change_status_staff_outputinfo.hide()
        self.frame_if_teacher_change_status_staff.hide()
        self.frame_buttons_change_status.hide()
        self.frame_buttons_confirm_change_status.hide()
        self.buttons_change_status_confirm_if_teacher.hide()
        self.button_change_status_cancel_if_teacher.hide()

    def logical_delete_button(self):
        delete_message = "¿Estás seguro de que deseas eliminar este registro?"

        reply = QMessageBox.question(
            None,
            "Confirmar Acción",
            delete_message,
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            activate_bool = False
            self.lds.logical_delete_staff_action(self.lds_staff_id, activate_bool)
            QtWidgets.QMessageBox.information(None, "Cambios Realizados", "El empleado seleccionado ha sido eliminado y desasignado de los demas registros, puede volver a restaurarlo \npero tendra que reasignarle las demas tareas.")
            self.search_staff_button_logical_delete()
        else:
            QtWidgets.QMessageBox.information(None, "Se ha cancelado", "No se ha eliminado el registro del empleado")

    def logical_restore_button(self):
        delete_message = "¿Estás seguro de que deseas restaurar este registro?"

        reply = QMessageBox.question(
            None,
            "Confirmar Acción",
            delete_message,
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            activate_bool = True
            self.lds.logical_delete_staff_action(self.lds_staff_id, activate_bool)
            QtWidgets.QMessageBox.information(None, "Cambios Realizados", "El empleado seleccionado ha sido restaurado, en caso de tener grados o materias asignadas, debes volver a asignarlos")
            self.search_staff_button_logical_delete()
        else:
            QtWidgets.QMessageBox.information(None, "Se ha cancelado", "No se ha restaurado el registro del empleado")

    def enable_disable_buttons_logical_delete(self, staff_id):
        status = self.lds.get_status(staff_id)
        match status:

            case "Activo":
                self.button_chhange_status_restore.setEnabled(False)
                self.button_change_status_delete.setEnabled(True)

            case "Inactivo":
                self.button_chhange_status_restore.setEnabled(True)
                self.button_change_status_delete.setEnabled(False)

            case _:
                self.button_chhange_status_restore.setEnabled(False)
                self.button_change_status_delete.setEnabled(False)

    def clear_button_logical_delete(self):
        self.line_input_change_status_staff_search_id.clear()
        
        self.frame_if_teacher_change_status_staff.hide()
        self.frame_change_status_staff_outputinfo.hide()
        self.frame_buttons_change_status.hide()
    ########################################################################################
    ########################################################################################
    ################################Search Staff Table######################################
    ########################################################################################

    def load_staff_data_search_staff(self):
        self.ssw = search_staff_widget()
        rows_staff = self.ssw.load_staff_table()
        self.tablew_show_staff_registered_search_staff.setRowCount(0)
        if rows_staff is not None:
            header = self.tablew_show_staff_registered_search_staff.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            header.setStretchLastSection(True)

            for row_index, row in enumerate(rows_staff):
                self.tablew_show_staff_registered_search_staff.insertRow(row_index)

                for col_index, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    item.setToolTip(str(value))
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    self.tablew_show_staff_registered_search_staff.setItem(row_index, col_index, item)

            self.tablew_show_staff_registered_search_staff.resizeRowsToContents()
        else:
            pass

    def filter_search_staff(self):
        search_full_name = self.line_input_full_name_search_staff.text().strip().lower()

        search_document_id = self.line_input_document_id_search_staff.text().strip().lower()
        search_number_phone = self.line_input_phone_number_search_staff.text().strip().lower()

        for row in range(self.tablew_show_staff_registered_search_staff.rowCount()):
            full_name = self.tablew_show_staff_registered_search_staff.item(row, 1).text().lower() if self.tablew_show_staff_registered_search_staff.item(row, 1) else " "
            document_id = self.tablew_show_staff_registered_search_staff.item(row, 2).text().lower() if self.tablew_show_staff_registered_search_staff.item(row, 1) else " "
            phone_number = self.tablew_show_staff_registered_search_staff.item(row, 4).text().lower() if self.tablew_show_staff_registered_search_staff.item(row, 1) else " "
        
            match_first_name = search_full_name in full_name
            match_document_id = search_document_id in document_id
            match_phone = search_number_phone in phone_number

            if (match_first_name and match_phone and match_document_id):
                self.tablew_show_staff_registered_search_staff.setRowHidden(row, False)
            else:
                self.tablew_show_staff_registered_search_staff.setRowHidden(row, True)

    def edit_selected_staff(self):
        selected_row = self.tablew_show_staff_registered_search_staff.currentRow()

        if selected_row >= 0:
            id_item = self.tablew_show_staff_registered_search_staff.item(selected_row, 0)
            if id_item:
                selected_id = id_item.text()

                self.main_central_widget.setCurrentWidget(self.edit_staff_widget)

                self.line_input_edit_staff_search_id.setText(selected_id)

                self.button_search_edit_staff.click()
        else:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "No hay ninguna fila seleccionada.")

    def clean_inputs_search_staff(self):
        self.line_input_full_name_search_staff.clear()
        self.line_input_phone_number_search_staff.clear()
        self.line_input_document_id_search_staff.clear()

    def details_button_search_staff(self):
        selected_row = self.tablew_show_staff_registered_search_staff.currentRow()

        if selected_row >= 0:
            staff_id = self.tablew_show_staff_registered_search_staff.item(selected_row, 0)

            if staff_id:
                selected_id = staff_id.text()
                selected_id = int(selected_id)

                status =  self.ssw.get_status(selected_id)

                match status:
                    case "Activo":
                        job_id = self.ssw.get_job_id(selected_id)
                        if job_id == 2:
                            
                            guide_grade, main_subject = self.ssw.get_main_subject_guide_grade(selected_id)
                            grades_assigned = self.ssw.get_grades_assigned(selected_id)
                            subjects_assigned = self.ssw.get_subjects_assigned(selected_id)

                            registered_date, updated_date = self.ssw.get_date_registered_and_last_update(selected_id)
                            schedule = self.ssw.get_schedule_impart_time(selected_id)

                            print(selected_id)
                            print(schedule)

                            sidg = StaffInfoDialog(job_id, guide_grade, main_subject, grades_assigned, subjects_assigned, schedule, registered_date, updated_date, None)
                            sidg.exec_()
                        
                        else:
                            guide_grade = None
                            main_subject = None
                            grades_assigned = None
                            subjects_assigned = None
                            registered_date, updated_date = self.ssw.get_date_registered_and_last_update(selected_id)
                            schedule = None

                            sidg = StaffInfoDialog(job_id, guide_grade, main_subject, grades_assigned, subjects_assigned, schedule, registered_date, updated_date, None)
                            sidg.exec_()

                    case "Inactivo":
                        QtWidgets.QMessageBox.information(None, "Empleado Inactivo", "El empleado actualmente esta inactivo/borrado de la base de datos, no hay detalles a mostrar")
        else:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "No hay ninguna fila seleccionada.")

    ########################################################################################
    ########################################################################################
    ################################Impart Time assign######################################
    ########################################################################################

    def load_impart_time_teachers(self):
        self.aitt = assign_impart_time_teacher()
        self.tablew_select_teacher_impart_tt_order = self.combox_filter_tablew_select_teacher_impart_tt.currentIndex()


        impart_time_results = self.aitt.load_impart_time_table(self.tablew_select_teacher_impart_tt_order)
        self.tablew_select_teacher_impart_tt.setRowCount(0)

        if impart_time_results is not None:
            header = self.tablew_select_teacher_impart_tt.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            header.setStretchLastSection(True)

            for row_index, row in enumerate(impart_time_results):
                self.tablew_select_teacher_impart_tt.insertRow(row_index)

                for col_index, value in enumerate(row):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    item.setToolTip(str(value))
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    self.tablew_select_teacher_impart_tt.setItem(row_index, col_index, item)

            self.tablew_select_teacher_impart_tt.resizeRowsToContents()
        else:
            pass
    
    def combox_filter_tablew_select_teacher_impart_tt_changed(self):
        if self.tablew_select_teacher_impart_tt_order != self.combox_filter_tablew_select_teacher_impart_tt.currentIndex():
            self.load_impart_time_teachers()
    
    def show_context_menu(self, position):
        selected_row = self.tablew_select_teacher_impart_tt.currentRow()
        if selected_row == -1:
            return

        context_menu = QMenu(None)

        edit_action = context_menu.addAction("Editar")
        delete_action = context_menu.addAction("Desasignar")

        edit_action.triggered.connect(self.edit_selected_staff_itt)
        delete_action.triggered.connect(self.unassign_impart_tiem)

        context_menu.exec_(self.tablew_select_teacher_impart_tt.viewport().mapToGlobal(position))

    def edit_selected_staff_itt(self):
        selected_row = self.tablew_select_teacher_impart_tt.currentRow()

        if selected_row >= 0:
            id_item = self.tablew_select_teacher_impart_tt.item(selected_row, 0)
            if id_item:
                selected_id = id_item.text()
                staff_id = self.aitt.get_staff_id_w_teacher_id(selected_id)

                self.main_central_widget.setCurrentWidget(self.edit_staff_widget)

                self.line_input_edit_staff_search_id.setText(str(staff_id))

                self.button_search_edit_staff.click()
        else:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "No hay ninguna fila seleccionada.")

    def unassign_impart_tiem(self):
        selected_row = self.tablew_select_teacher_impart_tt.currentRow()

        if selected_row >= 0:
            id_item = self.tablew_select_teacher_impart_tt.item(selected_row, 0)
            grade_assigned_item = self.tablew_select_teacher_impart_tt.item(selected_row, 4)
            subject_assined_item = self.tablew_select_teacher_impart_tt.item(selected_row, 5)
            time_start_item = self.tablew_select_teacher_impart_tt.item(selected_row, 6)
            time_end_item = self.tablew_select_teacher_impart_tt.item(selected_row, 7)

            if id_item:
                selected_id = id_item.text()
                selected_grade = grade_assigned_item.text()
                selected_subject = subject_assined_item.text()
                selected_time_start = time_start_item.text()
                selected_time_end = time_end_item.text()

                if selected_time_start == "None" and selected_time_end == "None":
                    return 
                
                try:
                    self.aitt.unassign_impart_time_action(str(selected_id), str(selected_grade), str(selected_subject), str(selected_time_start), str(selected_time_end))
                    QtWidgets.QMessageBox.information(None, "Exito", "Se ha desasignado la hora")
                    self.load_impart_time_teachers()
                except Exception as e:
                    QtWidgets.QMessageBox.warning(None, "Error", "No se ha podido eliminar la hora asignada")
                    print(e)

        else:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "No hay ninguna fila seleccionada.")

    def load_subject_selected_teacher(self):
        selected_row = self.tablew_select_teacher_impart_tt.currentRow()

        if selected_row >= 0:
            teacher_id_selected = self.tablew_select_teacher_impart_tt.item(selected_row, 0)
            if teacher_id_selected:
                old_teacher_id_selected = teacher_id_selected
                teacher_id_selected = teacher_id_selected.text()

                self.teacher_id_selected_impart = teacher_id_selected

                if old_teacher_id_selected != teacher_id_selected or old_teacher_id_selected == teacher_id_selected:
                    self.listw_select_subject_impart_tt.clear()
                    self.listw_select_subject_impart_tt.clearSelection()

                subjects_assigned = self.aitt.load_subjects(teacher_id_selected)
                for subject in subjects_assigned:
                    self.listw_select_subject_impart_tt.addItem(subject[0])
                
                subject_selected = self.tablew_select_teacher_impart_tt.item(selected_row, 5)
                subject_selected = subject_selected.text()

                self.current_subject_to_assign_qtable = subject_selected

                matching_items = self.listw_select_subject_impart_tt.findItems(subject_selected, QtCore.Qt.MatchExactly)
                if matching_items:
                    self.listw_select_subject_impart_tt.setCurrentItem(matching_items[0])
                else:
                    QtWidgets.QMessageBox.warning(None, "Advertencia", "No se encontró un elemento coincidente en la lista.")

        else:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "No hay ninguna fila seleccionada.")

    def load_grades_selected_teacher(self):
        selected_row = self.tablew_select_teacher_impart_tt.currentRow()

        if selected_row >= 0:
            teacher_id_selected = self.tablew_select_teacher_impart_tt.item(selected_row, 0)
            if teacher_id_selected:
                old_teacher_id_selected = teacher_id_selected
                teacher_id_selected = teacher_id_selected.text()

                if old_teacher_id_selected != teacher_id_selected or old_teacher_id_selected == teacher_id_selected:
                    self.listw_select_grade_impart_tt.clear()
                    self.listw_select_grade_impart_tt.clearSelection()

                subjects_assigned = self.aitt.load_grades(teacher_id_selected)
                for subject in subjects_assigned:
                    self.listw_select_grade_impart_tt.addItem(subject[0])
                
                grade_selected = self.tablew_select_teacher_impart_tt.item(selected_row, 4)
                grade_selected = grade_selected.text()
                
                self.current_grade_to_assign_qtable = grade_selected

                matching_items = self.listw_select_grade_impart_tt.findItems(grade_selected, QtCore.Qt.MatchExactly)
                if matching_items:
                    self.listw_select_grade_impart_tt.setCurrentItem(matching_items[0])
                else:
                    QtWidgets.QMessageBox.warning(None, "Advertencia", "No se encontró un elemento coincidente en la lista.")

        else:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "No hay ninguna fila seleccionada.")
    
    def enable_assign_save_button(self):
        if self.tablew_select_teacher_impart_tt.selectedItems:
            self.button_save_information_selected_impart_tt.setEnabled(True)
        else:
            self.button_save_information_selected_impart_tt.setEnabled(False)

    def clear_events_impart_time(self):
        self.listw_select_grade_impart_tt.clear()
        self.listw_select_subject_impart_tt.clear()
        self.listw_select_grade_impart_tt.clearSelection()
        self.listw_select_subject_impart_tt.clearSelection()

        self.button_save_information_selected_impart_tt.setEnabled(False)

    def assign_impart_time(self):

        current_selected_grade = self.listw_select_grade_impart_tt.selectedItems()
        current_selected_subject = self.listw_select_subject_impart_tt.selectedItems()

        compare_grade = current_selected_grade[0].text()
        compare_subject = current_selected_subject[0].text()

        current_teacher_id = self.tablew_select_teacher_impart_tt.item(self.tablew_select_teacher_impart_tt.currentRow(), 0)
        current_teacher_id = current_teacher_id.text()

        if not current_selected_grade or not current_selected_subject:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "No se ha seleccionado un grado o una materia")
            return

        if compare_grade != self.current_grade_to_assign_qtable or compare_subject != self.current_subject_to_assign_qtable and current_teacher_id == self.teacher_id_selected_impart:
            
            grade_text = current_selected_grade[0].text()
            subject_text = current_selected_subject[0].text()

            time_starts = self.timeedit_select_impart_start_time_impart_tt.time().toString("HH:mm:ss")
            time_ends = self.timeedit_select_impart_end_time_impart_tt.time().toString("HH:mm:ss")

            if not self.aitt.verify_teacher_time_assign(current_teacher_id, grade_text, subject_text ,time_starts, time_ends):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "El profesor ya tiene una hora asignada en ese rango de tiempo o el grado ya tiene asignada esa hora")
                return

            if not verify_start_time(time_starts):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "La hora de inicio no puede ser menor a las 6:00")
                return 
            
            if not verify_end_time(time_ends):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "La hora de finalizacion no puede ser mayor a las 18:00")
                return
            
            if not verify_start_end_tiem(time_starts, time_ends):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "La hora de finalizacion no puede ser menor a la hora de inicio")
                return
            
            found_match = False

            for row in range(self.tablew_select_teacher_impart_tt.rowCount()):
                grade_item = self.tablew_select_teacher_impart_tt.item(row, 4)
                subject_item = self.tablew_select_teacher_impart_tt.item(row, 5)
                if grade_item and subject_item:
                    if grade_item.text() == grade_text and subject_item.text() == subject_text:
                        self.tablew_select_teacher_impart_tt.selectRow(row)
                        action = "UPDATE"
                        found_match = True
                        
                        try:
                            self.aitt.assign_impart_time_action(current_teacher_id, grade_text, subject_text, time_starts, time_ends, action)
                            QtWidgets.QMessageBox.information(None, "Exito", "Se ha asignado la hora")
                            self.tablew_select_teacher_impart_tt.clearSelection()
                            self.clear_events_impart_time()
                            self.load_impart_time_teachers()
                            return
                        except Exception as e:
                            QtWidgets.QMessageBox.warning(None, "Error", "No se ha podido asignar la hora")
                            self.tablew_select_teacher_impart_tt.clearSelection()
                            self.clear_events_impart_time()
                            print(e)
                            return
            if not found_match:
                action = "INSERT"
                
                try:
                    self.aitt.assign_impart_time_action(current_teacher_id ,grade_text, subject_text, time_starts, time_ends, action)
                    QtWidgets.QMessageBox.information(None, "Exito", "Se ha asignado la hora")
                    self.load_impart_time_teachers()
                    self.tablew_select_teacher_impart_tt.clearSelection()
                    self.clear_events_impart_time()
                    return
                except Exception as e:
                    QtWidgets.QMessageBox.warning(None, "Error", "No se ha podido asignar la hora")
                    self.tablew_select_teacher_impart_tt.clearSelection()
                    self.clear_events_impart_time()
                    print(e)
                    return
        else:
            grade_text = current_selected_grade[0].text()
            subject_text = current_selected_subject[0].text()

            time_starts = self.timeedit_select_impart_start_time_impart_tt.time().toString("HH:mm:ss")
            time_ends = self.timeedit_select_impart_end_time_impart_tt.time().toString("HH:mm:ss")

            if not self.aitt.verify_teacher_time_assign(current_teacher_id, grade_text, subject_text ,time_starts, time_ends):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "El profesor ya tiene una hora asignada en ese rango de tiempo")
                return

            if not verify_start_time(time_starts):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "La hora de inicio no puede ser menor a las 6:00")
                return 
            
            if not verify_end_time(time_ends):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "La hora de finalizacion no puede ser mayor a las 18:00")
                return
            
            if not verify_start_end_tiem(time_starts, time_ends):
                QtWidgets.QMessageBox.warning(None, "Advertencia", "La hora de finalizacion no puede ser menor a la hora de inicio")
                return
            
            action = "UPDATE"
            try:
                self.aitt.assign_impart_time_action(current_teacher_id, grade_text, subject_text, time_starts, time_ends, action)
                QtWidgets.QMessageBox.information(None, "Exito", "Se ha asignado la hora")
                self.tablew_select_teacher_impart_tt.clearSelection()
                self.clear_events_impart_time()
                self.load_impart_time_teachers()
                return
            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", "No se ha podido asignar la hora")
                self.tablew_select_teacher_impart_tt.clearSelection()
                self.clear_events_impart_time()
                print(e)
                return

    def filter_search_impart_time(self):
        search_all_name_table = self.line_input_search_name_teacher_impart_tt.text().strip().lower()
        search_id = self.line_input_search_id_teacher_impart_tt.text().strip().lower()


        for row in range(self.tablew_select_teacher_impart_tt.rowCount()):
            id_teacher = self.tablew_select_teacher_impart_tt.item(row, 0).text().lower() if self.tablew_select_teacher_impart_tt.item(row, 0) else " "
            full_name = self.tablew_select_teacher_impart_tt.item(row, 1).text().lower() if self.tablew_select_teacher_impart_tt.item(row, 1) else " "
            grade = self.tablew_select_teacher_impart_tt.item(row, 4).text().lower() if self.tablew_select_teacher_impart_tt.item(row, 4) else " "
            subject = self.tablew_select_teacher_impart_tt.item(row, 5).text().lower() if self.tablew_select_teacher_impart_tt.item(row, 5) else " "

            match_id = search_id in id_teacher
            match_full_name = search_all_name_table in full_name
            match_grade = search_all_name_table in grade
            match_subject = search_all_name_table in subject


            if (match_id and match_full_name or match_grade or match_subject):
                self.tablew_select_teacher_impart_tt.setRowHidden(row, False)
            else:
                self.tablew_select_teacher_impart_tt.setRowHidden(row, True)
    
    def dynamic_label_details_impart_time(self):
        selected_row = self.tablew_select_teacher_impart_tt.currentRow()
        if selected_row >= 0:
            teacher_name = self.tablew_select_teacher_impart_tt.item(selected_row, 1).text()
            grade = self.tablew_select_teacher_impart_tt.item(selected_row, 4).text()
            subject = self.tablew_select_teacher_impart_tt.item(selected_row, 5).text()
            start_time = self.timeedit_select_impart_start_time_impart_tt.time().toString("HH:mm:ss")
            end_time = self.timeedit_select_impart_end_time_impart_tt.time().toString("HH:mm:ss")

            compare_grade = self.listw_select_grade_impart_tt.currentItem().text() if self.listw_select_grade_impart_tt.currentItem() else grade
            compare_subject = self.listw_select_subject_impart_tt.currentItem().text() if self.listw_select_subject_impart_tt.currentItem() else subject

            if grade != compare_grade:
                grade = self.listw_select_grade_impart_tt.currentItem().text()

            if subject != compare_subject:
                subject = self.listw_select_subject_impart_tt.currentItem().text()

        else:
            teacher_name = None
            grade = None
            subject = None
            start_time = None
            end_time = None

        self.label_teacher_selected_dynamic_impart_tt.setText(teacher_name) if teacher_name else self.label_teacher_selected_dynamic_impart_tt.setText(" ")
        self.label_grade_selected_data_dynamic_impart_tt_.setText(grade) if grade else self.label_grade_selected_data_dynamic_impart_tt_.setText(" ")
        self.label_subject_selected_data_dynamic_impart_tt.setText(subject) if subject else self.label_subject_selected_data_dynamic_impart_tt.setText(" ")
        full_time = f"{start_time} - {end_time}" if start_time and end_time else " "
        self.label_time_selected_data_dynamic_impart_tt.setText(full_time) if start_time and end_time else self.label_time_selected_data_dynamic_impart_tt.setText(" ")

    def clear_data_impart_time(self):
        self.listw_select_grade_impart_tt.clear()
        self.listw_select_subject_impart_tt.clear()
        self.listw_select_grade_impart_tt.clearSelection()
        self.listw_select_subject_impart_tt.clearSelection()
        self.timeedit_select_impart_start_time_impart_tt.setTime(QtCore.QTime(7, 0, 0))
        self.timeedit_select_impart_end_time_impart_tt.setTime(QtCore.QTime(8, 0, 0))
        self.tablew_select_teacher_impart_tt.clearSelection()
        self.button_save_information_selected_impart_tt.setEnabled(False)
        self.line_input_search_name_teacher_impart_tt.clear()
        self.line_input_search_id_teacher_impart_tt.clear()
        self.label_teacher_selected_dynamic_impart_tt.clear()
        self.label_grade_selected_data_dynamic_impart_tt_.clear()
        self.label_subject_selected_data_dynamic_impart_tt.clear()
        self.label_time_selected_data_dynamic_impart_tt.clear()

    def unassign_all_subject_grades_impart_time(self):
        message = "Esta accion desasignara todas las horas de inicio y final asignadas a los profesores \n¿Estás seguro de que deseas desasignar a todos los maestros?"

        reply = QMessageBox.question(
            None,
            "Confirmar Acción",
            message,
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.aitt.unassing_all_impart_time()
            QtWidgets.QMessageBox.information(None, "Cambios Realizados", "Los maestros han sido desasignados de las horas de inicio y final de los grados y materias asignadas")
            self.load_impart_time_teachers()
        else:
            QtWidgets.QMessageBox.information(None, "Cancelado", "No se ha desasignado ningun maestro a su horario")

    ########################################################################################
    ########################################################################################
    ################################Add Access Staff#######################################
    ########################################################################################

    def load_data_access_staff(self):
        self.als = access_login_software()

        login_info_rows = self.als.get_data_table()
        self.tablew_software_access_show.setRowCount(0)

        if login_info_rows is not None:
            header = self.tablew_software_access_show.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            header.setStretchLastSection(True)

            for row_index, row in enumerate(login_info_rows):
                self.tablew_software_access_show.insertRow(row_index)

                for col_index, value in enumerate(row):
                    if isinstance(value, datetime):
                        value = value.strftime('%d-%m-%Y %H:%M:%S')
                    elif value is None:
                        value = "N/A"
                    item = QtWidgets.QTableWidgetItem(str(value))
                    item.setToolTip(str(value))
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                    item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                    self.tablew_software_access_show.setItem(row_index, col_index, item)

            self.tablew_software_access_show.resizeRowsToContents()
        else:
            pass
    
    def filter_search_access_staff(self):
        search_id = self.line_input_search_by_register_id_staff_software_access.text().strip().lower()

        search_user = self.line_input_search_by_user_software_access.text().strip().lower()

        for row in range(self.tablew_software_access_show.rowCount()):
            id_registered = self.tablew_software_access_show.item(row, 0).text().lower() if self.tablew_software_access_show.item(row, 1) else " "
            user_registered = self.tablew_software_access_show.item(row, 2).text().lower() if self.tablew_software_access_show.item(row, 1) else " "
        
            match_id = search_id in id_registered
            match_user = search_user in user_registered

            if (match_id and match_user):
                self.tablew_software_access_show.setRowHidden(row, False)
            else:
                self.tablew_software_access_show.setRowHidden(row, True)
            
    def add_access_staff(self):
        staff_id = self.line_input_add_access_by_staff_id_software_access.text().strip()
        user = self.line_input_new_user_add_software_access.text().strip()
        password = self.line_input_new_password_software_access.text().strip()

        if not staff_id:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El campo de ID de empleado no puede estar vacio")
            return

        if not user:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El campo de usuario no puede estar vacio")
            return

        if not password:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El campo de contraseña no puede estar vacio")
            return

        if not self.als.verify_if_staff_exists(staff_id):
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El ID de empleado no existe")
            return
        
        if len(user) < 12 and not is_valid_username(user):
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El usuario debe tener al menos 12 caracteres y solo puede contener letras, numeros y guiones bajos")
            return
        
        if not is_valid_password(password):
            QtWidgets.QMessageBox.warning(None, "Advertencia", "La contraseña debe tener al menos 12 caracteres")
            return
        
        

        try:
            self.als.add_login_access(staff_id, user, password)
            QtWidgets.QMessageBox.information(None, "Exito", "Se ha añadido el usuario")
            self.load_data_access_staff()
            self.clear_inputs_add_staff_access()
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", "No se ha podido añadir el usuario")
            print(e)

    def remove_access_staff(self):
        staff_id = self.line_input_remove_access_by_staff_id_software_access.text().strip() if self.line_input_remove_access_by_staff_id_software_access.text().strip() else None
        document_id = self.line_input_remove_access_by_document_id_software_access.text().strip() if self.line_input_remove_access_by_document_id_software_access.text().strip() else None

        if not staff_id and not document_id:
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El campo de ID de empleado o cedula no puede estar vacio")
            return
        if not self.als.verify_id_or_document_id(staff_id, document_id):
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El ID de empleado o cedula no existe")
            return
        
        if not self.als.verify_if_login_access_exists(staff_id, document_id):
            QtWidgets.QMessageBox.warning(None, "Advertencia", "El empleado esta registrado al sistema de acceso")
            return

        message = "Esta accion desasignara el acceso al sistema de acceso del empleado \n¿Estás seguro de que deseas desasignar el acceso?"
        reply = QMessageBox.question(
            None, "Confirmar Acción", message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                self.als.deactivate_login_access(staff_id, document_id)
                QtWidgets.QMessageBox.information(None, "Cambios Realizados", "Se ha desasignado el acceso al sistema de acceso")
                self.load_data_access_staff()
                self.clear_inputs_add_staff_access()
            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", "No se ha podido desasignar el acceso al sistema de acceso")
                print(e)
        else:
            QtWidgets.QMessageBox.information(None, "Cancelado", "No se ha recovado el acceso al sistema de acceso")

    def clear_inputs_add_staff_access(self):
        self.line_input_add_access_by_staff_id_software_access.clear()
        self.line_input_new_user_add_software_access.clear()
        self.line_input_new_password_software_access.clear()
        self.line_input_search_by_register_id_staff_software_access.clear()
        self.line_input_search_by_user_software_access.clear()
        self.line_input_remove_access_by_staff_id_software_access.clear()
        self.line_input_remove_access_by_document_id_software_access.clear()

    def block_input_lines_add_access_staff(self):
        staff_id_text = self.line_input_remove_access_by_staff_id_software_access.text().strip()
        document_id_text = self.line_input_remove_access_by_document_id_software_access.text().strip()

        if staff_id_text:
            self.line_input_remove_access_by_document_id_software_access.setEnabled(False)
        elif document_id_text:
            self.line_input_remove_access_by_staff_id_software_access.setEnabled(False)
        else: 
            self.line_input_remove_access_by_staff_id_software_access.setEnabled(True)
            self.line_input_remove_access_by_document_id_software_access.setEnabled(True)


    ########################################################################################
    ########################################################################################
    ################################Load Widget Fuctions#####################################
    ########################################################################################
    def load_subject_widget(self):
        self.db_listener = Postgresqueries(self.load_data_subjects_main_central_widget)
        self.load_data_subjects_main_central_widget()

    def load_staff_add_widget(self):
        self.clear_information_add_staff()
    
    def load_staff_edit_widget(self):
        self.clear_label_output_edit()
        self.frame_edit_info.hide()
    
    def load_staff_remove_widget(self):
        self.clear_button_logical_delete()

    def load_search_staff_wdiget(self):
        self.clean_inputs_search_staff()
        self.load_staff_data_search_staff()
    
    def load_impart_time_teacher_widget(self):
        self.clear_data_impart_time()
        self.load_impart_time_teachers()
    
    def load_add_access_staff_widget(self):
        self.clear_inputs_add_staff_access()
        self.load_data_access_staff()

    def widgets_current_on(self, index):
        match index:
            case 0:
                self.load_subject_widget()
            case 1:
                self.load_staff_add_widget()
            case 2:
                self.load_staff_edit_widget()
            case 3:
                self.load_staff_remove_widget()
            case 4:
                self.load_search_staff_wdiget()
            case 5:
                self.load_impart_time_teacher_widget()
            case 6:
                self.load_add_access_staff_widget()
                

    def retranslateUi(self, staff_management_window):
        _translate = QtCore.QCoreApplication.translate
        staff_management_window.setWindowTitle(_translate("staff_management_window", "Administracion de personal"))
        self.tablew_subject_show.setSortingEnabled(False)
        item = self.tablew_subject_show.horizontalHeaderItem(0)
        item.setText(_translate("staff_management_window", "ID Materia"))
        item = self.tablew_subject_show.horizontalHeaderItem(1)
        item.setText(_translate("staff_management_window", "Materia"))
        self.label_subject_search.setText(_translate("staff_management_window", "Buscar Materia"))
        self.button_delete_subject.setText(_translate("staff_management_window", "Eliminar Materia"))
        #self.button_refresh_subjects_list.setText(_translate("staff_management_window", "Refrescar Tabla"))
        self.button_edit_subject.setText(_translate("staff_management_window", "Editar Materia"))
        self.button_add_subject.setText(_translate("staff_management_window", "Agregar Materia"))
        self.label_subject_search_name.setText(_translate("staff_management_window", "Buscar Materia"))
        self.label_subject_search_name_2.setText(_translate("staff_management_window", "Buscar ID"))
        self.main_central_widget.setTabText(self.main_central_widget.indexOf(self.Materias), _translate("staff_management_window", "Materias"))
        self.label_fname.setText(_translate("staff_management_window", "Primer Nombre"))
        self.label_sname.setText(_translate("staff_management_window", "Segundo Nombre"))
        self.label_fsurname.setText(_translate("staff_management_window", "Primer Apellido"))
        self.label_ssurname.setText(_translate("staff_management_window", "Segundo Apellido"))
        self.label_document_id.setText(_translate("staff_management_window", "Cedula"))
        self.label_address.setText(_translate("staff_management_window", "Direccion"))
        self.label_phone.setText(_translate("staff_management_window", "Numero Telefonico"))
        self.label_birthdate.setText(_translate("staff_management_window", "Fecha de Nacimeinto"))
        self.birthdate_input_get.setDisplayFormat(_translate("staff_management_window", "yyyy-MM-dd"))
        self.combox_job_id_selection.setItemText(1, _translate("staff_management_window", "Administrativo"))
        self.combox_job_id_selection.setItemText(2, _translate("staff_management_window", "Profesor"))
        self.combox_job_id_selection.setItemText(3, _translate("staff_management_window", "Tecnico en mantenimiento"))
        self.label_address_edit.setText(_translate("staff_management_window", "Direccion"))
        self.label_job_selection.setText(_translate("staff_management_window", "Seleccionar Trabajo"))
        self.cb_highschool_teacher.setToolTip(_translate("staff_management_window", "<html><head/><body><p>Marque la casilla si el profesor es de primaria</p></body></html>"))
        self.cb_highschool_teacher.setText(_translate("staff_management_window", "Profesor de Secundaria"))
        self.cb_assign_grade.setToolTip(_translate("staff_management_window", "<html><head/><body><p>Asignarle un grado guiado</p></body></html>"))
        self.cb_assign_grade.setText(_translate("staff_management_window", "Asignar grado"))
        self.cb_assign_subject.setText(_translate("staff_management_window", "Asignar Materia Principal"))
        self.info_grade_assign.setText(_translate("staff_management_window", "Seleccione el grado guiado"))
        self.info_grade_subject.setText(_translate("staff_management_window", "Seleccione la materia principal"))
        self.info_subjects_selection.setText(_translate("staff_management_window", "Materias que impartira"))
        self.info_grades_multiselections.setText(_translate("staff_management_window", "Grados que impartira clases"))
        self.button_clean_information.setToolTip(_translate("staff_management_window", "<html><head/><body><p>Limpiar los campos</p></body></html>"))
        self.button_clean_information.setText(_translate("staff_management_window", "Limpiar"))
        self.button_save_information_add_staff.setToolTip(_translate("staff_management_window", "<html><head/><body><p>Guardar los datos en la base de datos</p></body></html>"))
        self.button_save_information_add_staff.setText(_translate("staff_management_window", "Guardar"))
        self.button_gback.setToolTip(_translate("staff_management_window", "<html><head/><body><p>Regresar a la pagina de inicio</p></body></html>"))
        self.button_gback.setText(_translate("staff_management_window", "Regresar"))
        self.output_information_info.setText(_translate("staff_management_window", "La siguiente informacion sera guardada"))
        self.name_output_info.setText(_translate("staff_management_window", "Nombres:"))
        self.surname_output_info.setText(_translate("staff_management_window", "Apellidos:"))
        self.document_id_output_info.setText(_translate("staff_management_window", "Cedula:"))
        self.address_output_info.setText(_translate("staff_management_window", "Direccion:"))
        self.phone_number_output_info.setText(_translate("staff_management_window", "Numero de telefono:"))
        self.birthdate_output_info.setText(_translate("staff_management_window", "Fecha de nacimiento:"))
        self.edad_output_info.setText(_translate("staff_management_window", "Edad:"))
        self.grade_assign_output_info.setText(_translate("staff_management_window", "Grado asignado:"))
        self.subject_assign_output_info.setText(_translate("staff_management_window", "Materia Principal:"))
        self.button_confirm_information_add_staff.setText(_translate("staff_management_window", "Confirmar"))
        self.button_cancelar_information_add_staff.setText(_translate("staff_management_window", "Cancelar"))
        self.label_output_subjects.setText(_translate("staff_management_window", "Materias Seleccionadas"))
        self.label_output_grades.setText(_translate("staff_management_window", "Grados Seleccionados"))
        self.main_central_widget.setTabText(self.main_central_widget.indexOf(self.add_staff_widget), _translate("staff_management_window", "Agregar Personal"))
        self.label_search_id_edit.setText(_translate("staff_management_window", "Buscar por ID:"))
        self.label_search_document_id_edit.setText(_translate("staff_management_window", "Buscar por Cedula:"))
        self.button_search_edit_staff.setText(_translate("staff_management_window", "Buscar"))
        self.label_full_name_static_edit.setText(_translate("staff_management_window", "Nombre completo:"))
        self.label_document_id_static_edit.setText(_translate("staff_management_window", "Cedula:"))
        self.label_phone_number_static_edit.setText(_translate("staff_management_window", "Numero de telefono:"))
        self.label_job_id_static_edit.setText(_translate("staff_management_window", "Puesto:"))
        self.label_address_static_edit.setText(_translate("staff_management_window", "Direccion:"))
        self.label_birthdate_static_edit.setText(_translate("staff_management_window", "Fecha de nacimeinto:"))
        self.label_agre_static_edit.setText(_translate("staff_management_window", "Edad:"))
        self.label_if_teacher_main_subject_static.setText(_translate("staff_management_window", "Materia prinpical:"))
        self.label_if_teacher_assigned_grade_static.setText(_translate("staff_management_window", "Grado Guiado:"))
        self.label_if_teacher_assigned_subjects_static.setText(_translate("staff_management_window", "Materias Asignadas:"))
        self.label_if_teacher_grades_assigned_subject_static.setText(_translate("staff_management_window", "Grados Asignados:"))
        self.label_first_name_edit.setText(_translate("staff_management_window", "Primer Nombre"))
        self.label_second_name_edit.setText(_translate("staff_management_window", "Segundo Nombre"))
        self.label_second_surname_edit.setText(_translate("staff_management_window", "Segundo Apellido"))
        self.label_first_surname_edit.setText(_translate("staff_management_window", "Primer Apellido"))
        self.combobox_job_id_edit.setItemText(1, _translate("staff_management_window", "Administrativo"))
        self.combobox_job_id_edit.setItemText(2, _translate("staff_management_window", "Profesor"))
        self.combobox_job_id_edit.setItemText(3, _translate("staff_management_window", "Tecnico en mantenimiento"))
        self.checkbox_if_high_school_teacher_edit_staff.setText(_translate("staff_management_window", "Profesor Secundaria"))
        self.label_document_id_edit.setText(_translate("staff_management_window", "Cedula"))
        self.label_phone_number_edit.setText(_translate("staff_management_window", "Numero de telefono"))
        self.label_job_id_edit.setText(_translate("staff_management_window", "Puesto"))
        self.date_edit_staff.setDisplayFormat(_translate("staff_management_window", "yyyy-MM-dd"))
        self.label_birthdate_edit.setText(_translate("staff_management_window", "birthdate"))
        self.checkbox_if_teacher_edit_subjects_assigned.setText(_translate("staff_management_window", "Editar materias asignadas"))
        self.checkbox_if_teacher_edit_grades_assigned.setText(_translate("staff_management_window", "Editar grados asignados"))
        self.label_selection_subjects_edit.setText(_translate("staff_management_window", "Selecciona las materias:"))
        self.label_selections_grades_edit.setText(_translate("staff_management_window", "Selecciona los nuevos grados:"))
        self.label_selection_main_subject_edit.setText(_translate("staff_management_window", "Seleciona la materia principal:"))
        self.label_selection_guide_grade_edit.setText(_translate("staff_management_window", "Selecciona el grado guia:"))
        self.button_save_edit_staff.setText(_translate("staff_management_window", "Guardar"))
        self.button_clean_information_2.setText(_translate("staff_management_window", "Limpiar"))
        self.main_central_widget.setTabText(self.main_central_widget.indexOf(self.edit_staff_widget), _translate("staff_management_window", "Modificar Personal"))
        self.label_search_id_change_status.setText(_translate("staff_management_window", "Buscar por ID:"))
        self.label_search_document_id_change_status.setText(_translate("staff_management_window", "Buscar por Cedula:"))
        self.button_search_change_status_staff.setText(_translate("staff_management_window", "Buscar"))
        self.label_full_name_static_change_status.setText(_translate("staff_management_window", "Nombre completo:"))
        self.label_document_id_static_change_status.setText(_translate("staff_management_window", "Cedula:"))
        self.label_phone_number_static_change_status.setText(_translate("staff_management_window", "Numero de telefono:"))
        self.label_job_id_static_change_status.setText(_translate("staff_management_window", "Puesto:"))
        self.label_address_static_change_status.setText(_translate("staff_management_window", "Direccion:"))
        self.label_birthdate_static_change_status.setText(_translate("staff_management_window", "Fecha de nacimeinto:"))
        self.label_agre_static_change_status.setText(_translate("staff_management_window", "Edad:"))
        self.label_status_change_status.setToolTip(_translate("staff_management_window", "<html><head/><body><p>El estado determina si esta eliminado</p><p>Activo: No Eliminado</p><p>Inactivo: Eliminado</p></body></html>"))
        self.label_status_change_status.setText(_translate("staff_management_window", "Estado:"))
        self.button_chhange_status_restore.setText(_translate("staff_management_window", "Resturar"))
        self.button_change_status_delete.setText(_translate("staff_management_window", "Eliminar"))
        self.button_clean_information_change_status.setText(_translate("staff_management_window", "Limpiar"))
        self.label_change_status_note_if_teacher.setText(_translate("staff_management_window", "Nota: Al ser profesor y ser eliminado, se desasignaras los siguientes grados"))
        self.label_grade_guide_change_status_if_teacher.setText(_translate("staff_management_window", "Grado Guiado libre:"))
        self.label_grades_assigned_change_status_if_teacher.setText(_translate("staff_management_window", "Grados asignados:"))
        item = self.tablew_change_status_if_teacher_grades_assigned.horizontalHeaderItem(0)
        item.setText(_translate("staff_management_window", "Grado"))
        item = self.tablew_change_status_if_teacher_grades_assigned.horizontalHeaderItem(1)
        item.setText(_translate("staff_management_window", "Materia"))
        item = self.tablew_change_status_if_teacher_grades_assigned.horizontalHeaderItem(2)
        item.setText(_translate("staff_management_window", "Hora Inicio"))
        item = self.tablew_change_status_if_teacher_grades_assigned.horizontalHeaderItem(3)
        item.setText(_translate("staff_management_window", "Hora Final"))
        self.buttons_change_status_confirm_if_teacher.setText(_translate("staff_management_window", "Confirmar"))
        self.button_change_status_cancel_if_teacher.setText(_translate("staff_management_window", "Cancelar"))
        self.button_confirm_change_status.setText(_translate("staff_management_window", "Confirmar"))
        self.button_cancel_change_status.setText(_translate("staff_management_window", "Cancelar"))
        self.main_central_widget.setTabText(self.main_central_widget.indexOf(self.change_status_staff_widget), _translate("staff_management_window", "Eliminar Personal"))
        self.tablew_show_staff_registered_search_staff.setSortingEnabled(False)
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(0)
        item.setText(_translate("staff_management_window", "ID Registrado"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(1)
        item.setText(_translate("staff_management_window", "Nombre Completo"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(2)
        item.setText(_translate("staff_management_window", "Cedula"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(3)
        item.setText(_translate("staff_management_window", "Direccion"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(4)
        item.setText(_translate("staff_management_window", "Numero de Telefono"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(5)
        item.setText(_translate("staff_management_window", "Fecha de Nacimiento"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(6)
        item.setText(_translate("staff_management_window", "Edad"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(7)
        item.setText(_translate("staff_management_window", "Puesto"))
        item = self.tablew_show_staff_registered_search_staff.horizontalHeaderItem(8)
        item.setText(_translate("staff_management_window", "Estado"))
        self.label_full_name_search_staff.setText(_translate("staff_management_window", "Nombre Completo:"))
        self.label_document_id_search_staff.setText(_translate("staff_management_window", "Cedula:"))
        self.label_phone_number_search_staff.setText(_translate("staff_management_window", "Numero de Telefono:"))
        self.button_show_details_qtable_selected_search_staff.setText(_translate("staff_management_window", "Detalles"))
        self.button_edit_selected_staff_search_staff.setText(_translate("staff_management_window", "Editar"))
        self.main_central_widget.setTabText(self.main_central_widget.indexOf(self.search_staff_widget), _translate("staff_management_window", "Buscar Personal"))
        self.button_clear_information_search_staff.setText(_translate("staff_management_window", "Limpiar"))
        self.label_select_teacher_static_impart_tt.setText(_translate("staff_management_window", "Selecciona un profesor (Click Izquierdo para asignar horas de clase | Click derecho para desasignar o editar):"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(0)
        item.setText(_translate("staff_management_window", "ID Profesor"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(1)
        item.setText(_translate("staff_management_window", "Nombre Completo"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(2)
        item.setText(_translate("staff_management_window", "Grado Guiado"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(3)
        item.setText(_translate("staff_management_window", "Materia Principal"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(4)
        item.setText(_translate("staff_management_window", "Grado Asignado"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(5)
        item.setText(_translate("staff_management_window", "Materia Asignada"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(6)
        item.setText(_translate("staff_management_window", "Hora de inicio"))
        item = self.tablew_select_teacher_impart_tt.horizontalHeaderItem(7)
        item.setText(_translate("staff_management_window", "Hora que termina"))
        self.label_select_grade_static_impart_tt.setText(_translate("staff_management_window", "Selecciona un grado:"))
        self.label_select_subject_static_impart_tt.setText(_translate("staff_management_window", "Selecciona la materia:"))
        self.label_select_start_time_subject_static_impart_tt.setText(_translate("staff_management_window", "Selecciona la hora inicial:"))
        self.timeedit_select_impart_start_time_impart_tt.setDisplayFormat(_translate("staff_management_window", "hh:mm a"))
        self.label_select_end_time_static_static_impart_tt.setText(_translate("staff_management_window", "Selecciona la hora final:"))
        self.timeedit_select_impart_end_time_impart_tt.setDisplayFormat(_translate("staff_management_window", "hh:mm a"))
        self.button_clean_information_selected_impart_tt.setText(_translate("staff_management_window", "Limpiar"))
        self.button_unassign_time_selected_impart_tt.setText(_translate("staff_management_window", "Desasignar Horas"))
        self.button_save_information_selected_impart_tt.setText(_translate("staff_management_window", "Guardar"))
        self.label_details_selected_data_impart_tt.setText(_translate("staff_management_window", "DETALLES"))
        self.label_time_selected_impart_tt.setText(_translate("staff_management_window", "Tiempo asignado:"))
        self.label_subject_selected_impart_tt.setText(_translate("staff_management_window", "Materia:"))
        self.label_grade_selected_data_impart_tt.setText(_translate("staff_management_window", "Grado:"))
        self.label_teacher_selected_data_impart_tt.setText(_translate("staff_management_window", "Profesor:"))
        self.combox_filter_tablew_select_teacher_impart_tt.setItemText(0, _translate("staff_management_window", "Id profesor"))
        self.combox_filter_tablew_select_teacher_impart_tt.setItemText(1, _translate("staff_management_window", "Grado asignado"))
        self.combox_filter_tablew_select_teacher_impart_tt.setItemText(2, _translate("staff_management_window", "Hora inicial"))
        self.combox_filter_tablew_select_teacher_impart_tt.setItemText(3, _translate("staff_management_window", "Hora final"))
        self.combox_filter_tablew_select_teacher_impart_tt.setItemText(4, _translate("staff_management_window", "Hora inicial sin asignar"))
        self.combox_filter_tablew_select_teacher_impart_tt.setItemText(5, _translate("staff_management_window", "Hora final sin asignar"))
        self.label_name_search_impart_tt.setText(_translate("staff_management_window", "Nombre:"))
        self.label_id_search_impart_tt.setText(_translate("staff_management_window", "ID:"))
        self.main_central_widget.setTabText(self.main_central_widget.indexOf(self.impart_teacher_time), _translate("staff_management_window", "Tiempo de clases"))
        item = self.tablew_software_access_show.horizontalHeaderItem(0)
        item.setText(_translate("staff_management_window", "ID Empleado"))
        item = self.tablew_software_access_show.horizontalHeaderItem(1)
        item.setText(_translate("staff_management_window", "Nombre Completo"))
        item = self.tablew_software_access_show.horizontalHeaderItem(2)
        item.setText(_translate("staff_management_window", "Usuario"))
        item = self.tablew_software_access_show.horizontalHeaderItem(3)
        item.setText(_translate("staff_management_window", "Contraseña Ultima Vez Actualizada"))
        item = self.tablew_software_access_show.horizontalHeaderItem(4)
        item.setText(_translate("staff_management_window", "Tipo de Acceso"))
        item = self.tablew_software_access_show.horizontalHeaderItem(5)
        item.setText(_translate("staff_management_window", "Estado"))
        self.label_search_id_software_access.setText(_translate("staff_management_window", "Buscar por ID:"))
        self.label_add_access_software_access.setText(_translate("staff_management_window", "Agregar Acceso"))
        self.label_search_and_add_by_register_id_staff_software_access.setText(_translate("staff_management_window", "ID Empleado:"))
        self.label_new_user_software_access.setText(_translate("staff_management_window", "Nuevo Usuario:"))
        self.label_new_password_software_access.setText(_translate("staff_management_window", "Nueva contraseña:"))
        self.label_search_by_user_software_access.setText(_translate("staff_management_window", "Buscar por Usuario:"))
        self.button_clean_information_software_access.setText(_translate("staff_management_window", "Limpiar"))
        self.button_add_access_software_access.setText(_translate("staff_management_window", "Agregar"))
        self.label_remove_access_by_register_id_staff_software_access.setText(_translate("staff_management_window", "ID Empleado"))
        self.label_remove_access_software_access.setText(_translate("staff_management_window", "Quitar Acceso"))
        self.label_remove_access_by_document_id_software_access.setText(_translate("staff_management_window", "Cedula:"))
        self.button_remove_access_software_access.setText(_translate("staff_management_window", "Quitar Acceso"))
        self.main_central_widget.setTabText(self.main_central_widget.indexOf(self.new_login), _translate("staff_management_window", "Acceso al software"))
        self.actionLimpiar_Datos.setText(_translate("staff_management_window", "Limpiar Datos"))
    

class EditDialogEditStaff(QDialog):
    def __init__(self, old_data, new_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmar Cambios")
        self.setModal(True)
        self.resize(400, 300)
        
        layout = QVBoxLayout()

        field_mapping = {
            "Primer Nombre": "first_name",
            "Segundo Nombre": "middle_name",
            "Primer Apellido": "first_surname",
            "Segundo Apellido": "second_surname",
            "Cedula": "document_id",
            "Direccion": "address",
            "Puesto": "job_id",
            "Numero de telefono": "phone_number",
            "Fecha de nacimiento": "birthday"
        }

        fields = [
            "Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido",
            "Cedula", "Direccion", "Puesto", "Numero de telefono", "Fecha de nacimiento"
        ]
        
        for field in fields:
            key = field_mapping.get(field, field)

            old_value = old_data.get(key)
            new_value = new_data.get(key)
            
            old_value = "Sin Registrar" if old_value is None else old_value
            new_value = "Sin Cambios" if new_value is None else new_value
            
            if isinstance(new_value, int):
                match new_value:
                    case 1:
                        new_value = "Administrativo"
                    case 2:
                        new_value = "Profesor"
                    case 3:
                        new_value = "Tecnico en mantenimiento"
                    case _:
                        new_value = "Puesto no reconocido"

            label_text = f"{field}: {old_value} ➜ {new_value}"
            label = QLabel(label_text)
            layout.addWidget(label)

        button_layout = QHBoxLayout()
        self.save_button = QPushButton("Guardar")
        self.cancel_button = QPushButton("Cancelar")

        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.setLayout(layout)

class TeacherAssignmentDialogEditStaff(QDialog):
    def __init__(self, main_subject, guided_grade, subjects_list, grades_list, parent=None):
        super().__init__(parent) 
        self.main_subject = main_subject if main_subject is not None else "No asignado"
        self.guided_grade = guided_grade if guided_grade is not None else "No asignado"
        self.subjects_list = subjects_list if subjects_list is not None else ["No asignados", "Se desasignaran los grados relacionados con este profesor despues de guardar"]
        self.grades_list = grades_list if grades_list is not None else ["No asignados", "Se desasignaran los grados relacionados con este profesor despues de guardar"]
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Asignación del Maestro")
        self.resize(400, 300)

        layout = QVBoxLayout()

        main_subject_label = QLabel(f"Materia Principal: {self.main_subject}")
        layout.addWidget(main_subject_label)


        guided_grade_label = QLabel(f"Grado Guiado: {self.guided_grade}")
        layout.addWidget(guided_grade_label)

        subjects_label = QLabel("Materias Asignadas:")
        layout.addWidget(subjects_label)

        self.subjects_list_widget = QListWidget()
        for subject in self.subjects_list:
            self.subjects_list_widget.addItem(subject)
        layout.addWidget(self.subjects_list_widget)

        grades_label = QLabel("Grados Asignados:")
        layout.addWidget(grades_label)

        self.grades_list_widget = QListWidget()
        for grade in self.grades_list:
            self.grades_list_widget.addItem(grade)
        layout.addWidget(self.grades_list_widget)

        self.close_button = QPushButton("Cerrar")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)


class StaffInfoDialog(QtWidgets.QDialog):
    def __init__(self, job_id, guide_grade, main_subject, assigned_grades, assigned_subjects, schedule, registration_date, last_update, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detalles del empleado")
        self.setMinimumSize(600, 400 if job_id == 2 else 150)
        
        main_layout = QtWidgets.QVBoxLayout(self)
        
        if job_id == 2: 
            self.setup_teacher_ui(main_layout, guide_grade, main_subject, 
                                assigned_grades, assigned_subjects, 
                                schedule, registration_date, last_update)
        else:  
            self.setup_non_teacher_ui(main_layout, registration_date, last_update)

    def setup_teacher_ui(self, layout, guide_grade, main_subject, 
                       assigned_grades, assigned_subjects, 
                       schedule, reg_date, update_date):

        self.schedule_table = QtWidgets.QTableWidget()
        self.schedule_table.setColumnCount(4)
        self.schedule_table.setHorizontalHeaderLabels(
            ["Grado", "Materia", "Inicia", "Termina"])
        self.schedule_table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.schedule_table.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        
        self.guide_grade_lbl = QtWidgets.QLabel(f"Grado Guia: {guide_grade}")
        self.main_subject_lbl = QtWidgets.QLabel(f"Materia Principal: {main_subject}")
        
        self.assigned_list = QtWidgets.QListWidget()
        self.assigned_list.addItem("Grados asignados & Materias asignadas:")
        for grade, subject in zip(assigned_grades, assigned_subjects):
            self.assigned_list.addItem(f"{grade} - {subject}")
        
        self.reg_date_lbl = QtWidgets.QLabel(
            f"Registrado: {reg_date.strftime('%Y-%m-%d %H:%M:%S')}")
        self.update_date_lbl = QtWidgets.QLabel(
            f"Ultima actualizacion: {update_date.strftime('%Y-%m-%d %H:%M:%S')}")

        layout.addWidget(self.schedule_table)
        layout.addWidget(self.guide_grade_lbl)
        layout.addWidget(self.main_subject_lbl)
        layout.addWidget(self.assigned_list)
        layout.addWidget(self.reg_date_lbl)
        layout.addWidget(self.update_date_lbl)
        

        self.populate_schedule(schedule)

    def setup_non_teacher_ui(self, layout, reg_date, update_date):

        self.reg_date_lbl = QtWidgets.QLabel(
            f"Registrado: {reg_date.strftime('%Y-%m-%d %H:%M:%S')}")
        self.update_date_lbl = QtWidgets.QLabel(
            f"Ultima actualizacion: {update_date.strftime('%Y-%m-%d %H:%M:%S')}")

        layout.addWidget(self.reg_date_lbl)
        layout.addWidget(self.update_date_lbl)

    def populate_schedule(self, schedule):
        self.schedule_table.setRowCount(len(schedule))
        for row, (grade, subject, start, end) in enumerate(schedule):
            self.schedule_table.setItem(row, 0, QtWidgets.QTableWidgetItem(grade))
            self.schedule_table.setItem(row, 1, QtWidgets.QTableWidgetItem(subject))
            
            if isinstance(start, time):
                start = start.strftime("%H:%M")
            elif start is None:
                start = "N/A"
            
            if isinstance(end, time):
                end = end.strftime("%H:%M")
            elif end is None:
                end = "N/A"

            self.schedule_table.setItem(row, 2, QtWidgets.QTableWidgetItem(start))
            self.schedule_table.setItem(row, 3, QtWidgets.QTableWidgetItem(end))
