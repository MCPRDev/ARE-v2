from PyQt5 import QtWidgets
from gui_login_window import Ui_login_windows
from selection_panel_window import Ui_selection_management_window
#Controller is in charge of open, close and get signals for the windows, specially to logout in selection panel
class Controller:
    def __init__(self):
        self.login_window = None
        self.selection_panel = None

    def show_login(self):
        if self.selection_panel:
            self.selection_panel.close()
            self.selection_panel = None

        self.login_window = QtWidgets.QMainWindow()
        self.ui = Ui_login_windows(self) #here we recieve Controller self to get the signals in the corresponding module
        self.ui.setupUi(self.login_window)
        self.login_window.show()

    def show_panel_selection(self):
        if self.login_window:
            self.login_window.close()
            self.login_window = None

        self.selection_panel_window = QtWidgets.QMainWindow()
        self.ui = Ui_selection_management_window(self) #here we recieve Controller self to get the signals in the corresponding module
        self.ui.setupUi(self.selection_panel_window)
        self.selection_panel_window.show()