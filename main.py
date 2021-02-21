# Author : Jedi18
#
# Main file for the OSDAG Screening Task

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from view import MainWindow
from controller import Controller

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()

    controller = Controller(ui)

    sys.exit(app.exec_())
