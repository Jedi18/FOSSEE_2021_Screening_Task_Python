# Author : Jedi18
#
# Database manager for handling fetching data from database

import sqlite3
from beam_model import BeamModel
from angle_model import AngleModel
from channel_model import ChannelModel

class DatabaseManager:
    def __init__(self, database_path):
        self.database_path = database_path

    def fetchSection(self, type):
        conn = sqlite3.connect(self.database_path)
        c = conn.cursor()

        if type == 'beam':
            c.execute("SELECT * FROM Beams")
        elif type == 'angle':
            c.execute("SELECT * FROM Angles")
        elif type == 'channel':
            c.execute("SELECT * FROM Channels")
        else:
            conn.close()
            return

        result = c.fetchall()
        column_names = [description[0] for description in c.description]

        res = {}
        for beam_data in result:
            if type == 'beam':
                res[beam_data[0]] = BeamModel(beam_data)
            elif type == 'angle':
                res[beam_data[0]] = AngleModel(beam_data)
            else:
                res[beam_data[0]] = ChannelModel(beam_data)

        if type == 'beam':
            c = c.execute('PRAGMA TABLE_INFO(Beams)')
        elif type == 'angle':
            c = c.execute('PRAGMA TABLE_INFO(Angles)')
        else:
            c = c.execute('PRAGMA TABLE_INFO(Channels)')

        column_types = [info[2].split('(')[0].strip() for info in c.fetchall()]

        if type == 'beam':
            BeamModel.column_names = column_names
            BeamModel.column_types = column_types
        elif type == 'angle':
            AngleModel.column_names = column_names
            AngleModel.column_types = column_types
        else:
            ChannelModel.column_names = column_names
            ChannelModel.column_types = column_types

        conn.commit()
        conn.close()
        return res
