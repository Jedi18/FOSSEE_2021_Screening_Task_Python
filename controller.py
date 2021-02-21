# Author : Jedi18
#
# Controller

from database_manager import DatabaseManager

class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.database_manager = DatabaseManager("")
        print(self.database_manager.fetchBeams())

    def populateSteelSectionLists(self):
        pass
