from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class PropertyWidget(QtWidgets.QWidget):
    """
    Property widget to display properties of the selected steel section
    """

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)

        self.listBox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.listBox)

        self.scroll = QtWidgets.QScrollArea(self)
        self.listBox.addWidget(self.scroll)
        self.scroll.setWidgetResizable(True)
        self.scrollContent = QtWidgets.QWidget(self.scroll)

        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollContent)
        self.scrollContent.setLayout(self.scrollLayout)
        self.scroll.setWidget(self.scrollContent)

    def setupBeamProperties(self, column_names, column_types):
        for i in range(0, len(column_names)):
            self.generatePropertyUI(column_names[i], column_types[i])

    def generatePropertyUI(self, label, type):
        horizLayout = QtWidgets.QHBoxLayout()

        lab = QtWidgets.QLabel(self.scrollContent)
        lab.setObjectName("label_{}".format(label))
        horizLayout.addWidget(lab)
        lab.setText("{} : ".format(str(label)))

        if type == 'INTEGER':
            spinBox = QtWidgets.QSpinBox(self.scrollContent)
            spinBox.setObjectName("spinBox_{}".format(label))
            horizLayout.addWidget(spinBox)
        elif type == 'VARCHAR':
            lineEdit = QtWidgets.QLineEdit(self.scrollContent)
            lineEdit.setObjectName("lineEdit_{}".format(label))
            horizLayout.addWidget(lineEdit)
        elif type == 'REAL':
            doubleSpinBox = QtWidgets.QDoubleSpinBox(self.scrollContent)
            doubleSpinBox.setObjectName("doubleSpinBox_{}".format(label))
            horizLayout.addWidget(doubleSpinBox)

        self.scrollLayout.addLayout(horizLayout)
