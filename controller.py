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
        self.beams = self.database_manager.fetchBeams()
        self.ui.populateList(self.beams, 'beam')

    def getBeamData(self, beamId):
        return self.beams[beamId]
