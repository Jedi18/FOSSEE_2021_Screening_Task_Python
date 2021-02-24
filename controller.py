# Author : Jedi18
#
# Controller

from database_manager import DatabaseManager

class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.ui.setController(self)

        self.database_manager = DatabaseManager('steel_sections.sqlite')
        self.populateSteelSectionLists()

    def populateSteelSectionLists(self):
        self.beams = self.database_manager.fetchSection('beam')
        self.angles = self.database_manager.fetchSection('angle')
        self.channels = self.database_manager.fetchSection('channel')
        self.ui.populateList(self.beams, 'beam')
        self.ui.populateList(self.angles, 'angle')
        self.ui.populateList(self.channels, 'channel')

    def getBeamData(self, beamId):
        return self.beams[beamId]

    def getAngleData(self, angleId):
        return self.angles[angleId]

    def getChannelData(self, channelId):
        return self.channels[channelId]
