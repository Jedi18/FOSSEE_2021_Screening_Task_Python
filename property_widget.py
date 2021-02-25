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
        self.MODE = 'VIEW'

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

    def setProperties(self, data, column_names, column_types, section_type):
        if section_type == 'beam':
            contentWidget = self.beamContent
        elif section_type == 'angle':
            contentWidget = self.angleContent
        elif section_type == 'channel':
            contentWidget = self.channelContent
        else:
            return

        for i in range(0, len(data)):
            if column_types[i] == 'INTEGER':
                spinBox = contentWidget.findChild(QtWidgets.QSpinBox, column_names[i])
                if data[i] == None:
                    spinBox.setEnabled(False)
                else:
                    spinBox.setValue(int(data[i]))
                    spinBox.setEnabled(True)
            elif column_types[i] == 'VARCHAR':
                lineEdit = contentWidget.findChild(QtWidgets.QLineEdit, column_names[i])
                if data[i] == None:
                    lineEdit.setEnabled(False)
                else:
                    lineEdit.setText(str(data[i]))
                    lineEdit.setEnabled(True)
            elif column_types[i] == 'REAL':
                doubleSpinBox = contentWidget.findChild(QtWidgets.QDoubleSpinBox, column_names[i])
                if data[i] == None:
                    doubleSpinBox.setEnabled(False)
                else:
                    doubleSpinBox.setValue(float(data[i]))
                    doubleSpinBox.setEnabled(True)

    def clearProperties(self, section_type):
        if section_type == 'beam':
            contentWidget = self.beamContent
        elif section_type == 'angle':
            contentWidget = self.angleContent
        elif section_type == 'channel':
            contentWidget = self.channelContent
        else:
            return

        lineEditsList = contentWidget.findChildren(QtWidgets.QLineEdit)
        spinBoxList = contentWidget.findChildren(QtWidgets.QSpinBox)
        doubleSpinBoxList = contentWidget.findChildren(QtWidgets.QDoubleSpinBox)

        for lineEdit in lineEditsList:
            lineEdit.clear()
            lineEdit.setEnabled(True)

        for spinBox in spinBoxList:
            spinBox.setValue(0)
            spinBox.setEnabled(True)

        for doubleSpinBox in doubleSpinBoxList:
            doubleSpinBox.setValue(0)
            doubleSpinBox.setEnabled(True)

        self.changePropertyArea(section_type)

    def generatePropertyUI(self, label, type, section_type):
        horizLayout = QtWidgets.QHBoxLayout()

        lab = QtWidgets.QLabel(self.beamContent)
        lab.setObjectName("label_{}".format(label))
        horizLayout.addWidget(lab)
        lab.setText("{} : ".format(str(label)))

        if section_type == 'beam':
            parentContent = self.beamContent
        elif section_type == 'angle':
            parentContent = self.angleContent
        else:
            parentContent = self.channelContent

        if type == 'INTEGER':
            spinBox = QtWidgets.QSpinBox(parentContent)
            spinBox.setMaximum(1000000)
            spinBox.setObjectName(label)
            horizLayout.addWidget(spinBox)
        elif type == 'VARCHAR':
            lineEdit = QtWidgets.QLineEdit(parentContent)
            lineEdit.setObjectName(label)
            horizLayout.addWidget(lineEdit)
        elif type == 'REAL':
            doubleSpinBox = QtWidgets.QDoubleSpinBox(parentContent)
            doubleSpinBox.setMaximum(1000000)
            doubleSpinBox.setObjectName(label)
            horizLayout.addWidget(doubleSpinBox)

        if section_type == 'beam':
            self.scrollBeamLayout.addLayout(horizLayout)
        elif section_type == 'angle':
            self.scrollAngleLayout.addLayout(horizLayout)
        else:
            self.scrollChannelLayout.addLayout(horizLayout)

    def changePropertyArea(self, type):
        self.scrollContent.setCurrentIndex(self.sectionTypeToIndex[type])

    def setMode(self, mode, section_type = None):
        self.MODE = mode

        if mode == 'ADD':
            self.clearProperties(section_type)
        elif mode == 'VIEW':
            self.changePropertyArea('empty')
