# Author : Jedi18
#
# Database manager for handling and fetching data from database

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

    def addSection(self, newData, type):
        conn = sqlite3.connect(self.database_path)
        c = conn.cursor()

        # fetch max id for new id for the newly added section
        if type == 'beam':
            c = c.execute('SELECT max(id) from Beams')
        elif type == 'angle':
            c = c.execute('SELECT max(id) from Angles')
        else:
            c = c.execute('SELECT max(id) from Channels')
        newid = c.fetchone()[0] + 1

        sql = "INSERT INTO "

        is_varchar = []
        if type == 'beam':
            sql += "Beams("
            for col in range(0,len(BeamModel.column_names)):
                if BeamModel.column_types[col] == 'VARCHAR':
                    is_varchar.append(True)
                else:
                    is_varchar.append(False)

                sql += BeamModel.column_names[col]
                if col != len(BeamModel.column_names)-1:
                    sql += ","
            sql += ")"
        elif type == 'angle':
            sql += "Angles("
            for col in range(0,len(AngleModel.column_names)):
                if AngleModel.column_types[col] == 'VARCHAR':
                    is_varchar.append(True)
                else:
                    is_varchar.append(False)

                sql += '"' + AngleModel.column_names[col] + '"'
                if col != len(AngleModel.column_names)-1:
                    sql += ","
            sql += ")"
        else:
            sql += "Channels("
            for col in range(0,len(ChannelModel.column_names)):
                if ChannelModel.column_types[col] == 'VARCHAR':
                    is_varchar.append(True)
                else:
                    is_varchar.append(False)

                sql += ChannelModel.column_names[col]
                if col != len(ChannelModel.column_names)-1:
                    sql += ","
            sql += ")"

        sql += " values(" + str(newid) + ","
        for i in range(0,len(newData)):
            if is_varchar[i+1]:
                sql += '"'
                sql += str(newData[i])
                sql += '"'
            else:
                sql += str(newData[i])
            if i != len(newData)-1:
                sql += ","
        sql += ")"

        c.execute(sql)
        conn.commit()
        conn.close()
