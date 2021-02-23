# Author : Jedi18
#
# Manages the view (GUI) part of the application

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 383, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(10, 20, 139, 49))
        self.widget.setObjectName("widget")
        self.propertyLayout = QtWidgets.QVBoxLayout(self.widget)
        self.propertyLayout.setContentsMargins(0, 0, 0, 0)
        self.propertyLayout.setObjectName("propertyLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.propertyLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.propertyLayout.addWidget(self.lineEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionLoad_Database.setText(_translate("MainWindow", "Load Database"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))

    def setupConnections(self):
        self.beamList.itemSelectionChanged.connect(self.beamItemSelected)

    def populateList(self, sectionList, type):
        if type == "beam":
            for section_id in sectionList:
                section = sectionList[section_id]
                sectionItem = QtWidgets.QListWidgetItem(section.designation)
                sectionItem.setData(QtCore.Qt.UserRole, section.id)
                self.beamList.addItem(sectionItem)

    def beamItemSelected(self):
        beamItemId = self.beamList.selectedItems()[0].data(QtCore.Qt.UserRole)
        beamItem = self.controller.getBeamData(beamItemId)
        self.populateSteelSectionProperties(beamItem, "beam")

    def populateSteelSectionProperties(self, steelSection, type):
        pass
