# Author : Jedi18
#
# Database manager for handling fetching data from database

import sqlite3

class DatabaseManager:
    def __init__(self, database_path):
        self.database_path = database_path

    def fetchBeams(self):
        return [{"name" : "boop"}]
