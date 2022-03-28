from .manager import Manager
import getpass
import sqlite3
import json


class SetupManager:
    def __init__(self):
        self.SetupManagerFunction()

    def SetupManagerFunction(self):
        try:
            # Create database connection
            user = getpass.getuser()
            con = sqlite3.connect(
                f'/home/{user}/.config/moftah/db/passwords.db')
            cur = con.cursor()

            with open(f"/home/{user}/.config/moftah/log/log.json", "r+") as config:
                f = json.load(config)

                if f['ran'] == 0:
                    cur.execute("""
CREATE TABLE "passwords" (
	"website"	TEXT,
	"user"	TEXT,
	"password"	TEXT
);
CREATE TABLE "userpass" (
	"password"	TEXT
);
                    """)
                    con.commit()
                    print(f"""
It seems that you are running Moftah for the first time, {user}.\n
We'll have to update the password now so please enter a new password!
                      """)

                    # Ask for a master password
                    newpass = getpass.getpass(prompt="New password: ")

                    # Insert password
                    insertQuery = """INSERT INTO userpass VALUES (?)"""
                    cur.execute(insertQuery, (newpass,))
                    con.commit()

                    # Rewrite the number in json
                    f['ran'] = 1
                    config.seek(0)
                    json.dump(f, config)
                    config.truncate()
                    config.close()
                    return True
                    Manager()
            con.close()
        except Exception as e:
            print(f"[1] {e}")
