# Author : Jedi18
#
# Manages the view (GUI) part of the application

from PyQt5 import QtCore, QtGui, QtWidgets
from beam_model import BeamModel
from angle_model import AngleModel
from channel_model import ChannelModel
from property_widget import PropertyWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()

    def setController(self, controller):
        self.controller = controller

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.beamTab = QtWidgets.QWidget()
        self.beamTab.setObjectName("beamTab")
        self.beamList = QtWidgets.QListWidget(self.beamTab)
        self.beamList.setObjectName("beamList")
        self.tabWidget.addTab(self.beamTab, "")

        self.channelTab = QtWidgets.QWidget()
        self.channelTab.setObjectName("channelTab")
        self.channelList = QtWidgets.QListWidget(self.channelTab)
        self.channelList.setObjectName("channelList")
        self.tabWidget.addTab(self.channelTab, "")

        self.angleTab = QtWidgets.QWidget()
        self.angleTab.setObjectName("angleTab")
        self.angleList = QtWidgets.QListWidget(self.angleTab)
        self.angleList.setObjectName("angleList")
        self.tabWidget.addTab(self.angleTab, "")

        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addPushButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setObjectName("editPushButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
##
        self.rightWidget = QtWidgets.QWidget()
        self.rightVerticalLayout = QtWidgets.QVBoxLayout()
        self.rightWidget.setLayout(self.rightVerticalLayout)

        self.propertyWidget = PropertyWidget(self.centralwidget)
        self.sectionTypeComboBox = QtWidgets.QComboBox(self.rightWidget)

        self.finishButton = QtWidgets.QPushButton(self.rightWidget)
        self.finishButton.setObjectName("finishButton")
        self.finishButton.setVisible(False)
        self.finishButton.setText("Finish")

        self.cancelButton = QtWidgets.QPushButton(self.rightWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.setVisible(False)
        self.cancelButton.setText("Cancel")

        self.button2Layout = QtWidgets.QHBoxLayout()
        self.button2Layout.addWidget(self.finishButton)
        self.button2Layout.addWidget(self.cancelButton)

        self.sectionTypeComboBox.setVisible(False)
        self.sectionTypeComboBox.addItem("Beam")
        self.sectionTypeComboBox.addItem("Angle")
        self.sectionTypeComboBox.addItem("Channel")
        self.rightVerticalLayout.addWidget(self.sectionTypeComboBox)
        self.rightVerticalLayout.addWidget(self.propertyWidget)
        self.rightVerticalLayout.addLayout(self.button2Layout)
        self.horizontalLayout_2.addWidget(self.rightWidget)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionLoad_Database = QtWidgets.QAction(self)
        self.actionLoad_Database.setObjectName("actionLoad_Database")
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd = QtWidgets.QAction(self)
        self.actionAdd.setObjectName("actionAdd")
        self.menuFile.addAction(self.actionAdd)
        self.menuFile.addAction(self.actionLoad_Database)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.setupConnections()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.beamTab), _translate("MainWindow", "Beam"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.channelTab), _translate("MainWindow", "Channel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.angleTab), _translate("MainWindow", "Angle"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.editButton.setText(_translate("MainWindow", "Edit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoad_Database.setText(_translate("MainWindow", "Load Database"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))

    def setupConnections(self):
        self.beamList.itemSelectionChanged.connect(self.beamItemSelected)
        self.angleList.itemSelectionChanged.connect(self.angleItemSelected)
        self.channelList.itemSelectionChanged.connect(self.channelItemSelected)
        self.addButton.clicked.connect(self.addSectionItem)
        self.actionAdd.triggered.connect(self.addSectionItem)
        self.finishButton.clicked.connect(self.finishSelected)
        self.cancelButton.clicked.connect(self.cancelSelected)
        self.sectionTypeComboBox.activated.connect(self.sectionTypeComboBoxChanged)

    def populateList(self, sectionList, type):
        if type == "beam":
            for section_id in sectionList:
                section = sectionList[section_id]
                sectionItem = QtWidgets.QListWidgetItem(section.designation)
                sectionItem.setData(QtCore.Qt.UserRole, section.id)
                self.beamList.addItem(sectionItem)

            self.propertyWidget.setupBeamProperties(BeamModel.column_names, BeamModel.column_types)
        elif type == "angle":
            for section_id in sectionList:
                section = sectionList[section_id]
                sectionItem = QtWidgets.QListWidgetItem(section.designation)
                sectionItem.setData(QtCore.Qt.UserRole, section.id)
                self.angleList.addItem(sectionItem)

            self.propertyWidget.setupAngleProperties(AngleModel.column_names, AngleModel.column_types)
        elif type ==  "channel":
            for section_id in sectionList:
                section = sectionList[section_id]
                sectionItem = QtWidgets.QListWidgetItem(section.designation)
                sectionItem.setData(QtCore.Qt.UserRole, section.id)
                self.channelList.addItem(sectionItem)

            self.propertyWidget.setupChannelProperties(ChannelModel.column_names, ChannelModel.column_types)

    def beamItemSelected(self):
        self.propertyWidget.changePropertyArea('beam')

        beamItemId = self.beamList.selectedItems()[0].data(QtCore.Qt.UserRole)
        beamItem = self.controller.getBeamData(beamItemId)
        self.propertyWidget.setProperties(beamItem.data, BeamModel.column_names, BeamModel.column_types, 'beam')

    def angleItemSelected(self):
        self.propertyWidget.changePropertyArea('angle')

        angleItemId = self.angleList.selectedItems()[0].data(QtCore.Qt.UserRole)
        angleItem = self.controller.getAngleData(angleItemId)
        self.propertyWidget.setProperties(angleItem.data, AngleModel.column_names, AngleModel.column_types, 'angle')

    def channelItemSelected(self):
        self.propertyWidget.changePropertyArea('channel')

        channelItemId = self.channelList.selectedItems()[0].data(QtCore.Qt.UserRole)
        channelItem = self.controller.getChannelData(channelItemId)
        self.propertyWidget.setProperties(channelItem.data, ChannelModel.column_names, ChannelModel.column_types, 'channel')

    def addSectionItem(self):
        self.sectionTypeComboBox.setVisible(True)
        self.finishButton.setVisible(True)
        self.cancelButton.setVisible(True)
        self.tabWidget.setEnabled(False)
        self.editButton.setEnabled(False)
        self.addButton.setEnabled(False)
        self.propertyWidget.setMode('ADD', self.sectionTypeComboBox.currentText().lower())

    def cancelSelected(self):
        self.sectionTypeComboBox.setVisible(False)
        self.finishButton.setVisible(False)
        self.cancelButton.setVisible(False)
        self.tabWidget.setEnabled(True)
        self.editButton.setEnabled(True)
        self.addButton.setEnabled(True)
        self.propertyWidget.setMode('VIEW')

    def finishSelected(self):
        self.sectionTypeComboBox.setVisible(False)
        self.finishButton.setVisible(False)
        self.cancelButton.setVisible(False)
        self.tabWidget.setEnabled(True)
        self.editButton.setEnabled(True)
        self.addButton.setEnabled(True)
        self.propertyWidget.setMode('VIEW')

    def sectionTypeComboBoxChanged(self):
        self.propertyWidget.setMode('ADD', self.sectionTypeComboBox.currentText().lower())
