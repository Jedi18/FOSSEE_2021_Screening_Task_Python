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
        BeamModel.column_names = [description[0] for description in c.description]

        res = {}
        for beam_data in result:
            res[beam_data[0]] = BeamModel(beam_data)

        c = c.execute('PRAGMA TABLE_INFO(Beams)')
        BeamModel.column_types = [info[2].split('(')[0].strip() for info in c.fetchall()]

        conn.commit()
        conn.close()
        return res
