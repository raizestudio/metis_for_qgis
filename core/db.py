import sqlite3
import os

class MetisDb():

    def __init__(self, plugindir):
        self.con = sqlite3.connect(os.path.join(plugindir, 'metisdb.db'))