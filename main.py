# Author : Jedi18
#
# Main file for the OSDAG Screening Task

from PyQt5 import QtCore, QtGui, QtWidgets
from view import Ui_MainWindow
from controller import Controller

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    controller = Controller(ui)

    sys.exit(app.exec_())
