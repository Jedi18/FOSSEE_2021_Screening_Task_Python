# Author : Jedi18
#
# Database manager for handling fetching data from database

import sqlite3
from beam_model import BeamModel

class DatabaseManager:
    def __init__(self, database_path):
        self.database_path = database_path

    def fetchBeams(self):
        conn = sqlite3.connect(self.database_path)
        c = conn.cursor()
        c.execute("SELECT * FROM Beams")
        result = c.fetchall()

        res = {}
        for beam_data in result:
            res[beam_data[0]] = BeamModel(beam_data)

        conn.commit()
        conn.close()
        return res
