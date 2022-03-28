import getpass
import sqlite3
import time
import json
import os

class Nuke:
    def __init__(self):
        self.BoomBangBop()

    def BoomBangBop(self):
        user = getpass.getuser()
        os.system(f'rm /home/{user}/.config/moftah/db/passwords.db')
        time.sleep(2)
        con = sqlite3.connect(
            f'/home/{user}/.config/moftah/db/passwords.db')
        con.close()
        print("Removed all passwords!")
        with open(f"/home/{user}/.config/moftah/log/log.json", "r+") as config:
            f = json.load(config)

            f['ran'] = 0
            config.seek(0)
            json.dump(f, config)
            config.truncate()
            config.close()
        exit()
