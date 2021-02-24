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
        self.scrollContent = QtWidgets.QStackedWidget(self.scroll)

        self.sectionTypeToIndex = {
            'empty' : 0,
            'beam' : 1,
            'angle' : 2,
            'channel' : 3
        }

        self.emptyContent = QtWidgets.QWidget(self.scrollContent)
        self.scrollContent.addWidget(self.emptyContent)

        self.beamContent = QtWidgets.QWidget(self.scrollContent)
        self.scrollBeamLayout = QtWidgets.QVBoxLayout(self.beamContent)
        self.beamContent.setLayout(self.scrollBeamLayout)
        self.scrollContent.addWidget(self.beamContent)

        self.angleContent = QtWidgets.QWidget(self.scrollContent)
        self.scrollAngleLayout = QtWidgets.QVBoxLayout(self.angleContent)
        self.angleContent.setLayout(self.scrollAngleLayout)
        self.scrollContent.addWidget(self.angleContent)

        self.channelContent = QtWidgets.QWidget(self.scrollContent)
        self.scrollChannelLayout = QtWidgets.QVBoxLayout(self.channelContent)
        self.channelContent.setLayout(self.scrollChannelLayout)
        self.scrollContent.addWidget(self.channelContent)

        self.scroll.setWidget(self.scrollContent)
        self.scrollContent.setCurrentIndex(self.sectionTypeToIndex['empty'])

    def setupBeamProperties(self, column_names, column_types):
        for i in range(0, len(column_names)):
            self.generatePropertyUI(column_names[i], column_types[i], "beam")

    def setupAngleProperties(self, column_names, column_types):
        for i in range(0, len(column_names)):
            self.generatePropertyUI(column_names[i], column_types[i], "angle")

    def setupChannelProperties(self, column_names, column_types):
        for i in range(0, len(column_names)):
            self.generatePropertyUI(column_names[i], column_types[i], "channel")

    def generatePropertyUI(self, label, type, section_type):
        horizLayout = QtWidgets.QHBoxLayout()

        lab = QtWidgets.QLabel(self.beamContent)
        lab.setObjectName("label_{}".format(label))
        horizLayout.addWidget(lab)
        lab.setText("{} : ".format(str(label)))

        if type == 'INTEGER':
            spinBox = QtWidgets.QSpinBox(self.beamContent)
            spinBox.setObjectName("spinBox_{}".format(label))
            horizLayout.addWidget(spinBox)
        elif type == 'VARCHAR':
            lineEdit = QtWidgets.QLineEdit(self.beamContent)
            lineEdit.setObjectName("lineEdit_{}".format(label))
            horizLayout.addWidget(lineEdit)
        elif type == 'REAL':
            doubleSpinBox = QtWidgets.QDoubleSpinBox(self.beamContent)
            doubleSpinBox.setObjectName("doubleSpinBox_{}".format(label))
            horizLayout.addWidget(doubleSpinBox)

        if section_type == 'beam':
            self.scrollBeamLayout.addLayout(horizLayout)
        elif section_type == 'angle':
            self.scrollAngleLayout.addLayout(horizLayout)
        else:
            self.scrollChannelLayout.addLayout(horizLayout)

    def changePropertyArea(self, type):
        self.scrollContent.setCurrentIndex(self.sectionTypeToIndex[type])
