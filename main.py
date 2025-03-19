import sys
from PyQt5 import QtWidgets
from gui_login_window import Ui_login_windows

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_windows = QtWidgets.QMainWindow()
    ui = Ui_login_windows()
    ui.setupUi(login_windows)
    login_windows.show()
    sys.exit(app.exec_())