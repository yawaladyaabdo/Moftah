import getpass
import sqlite3


class SeePass:
    def __init__(self):
        self.SeePassFunction()

    def SeePassFunction(self):
        try:
            user = getpass.getuser()
            con = sqlite3.connect(
                f'/home/{user}/.config/moftah/db/passwords.db')
            cur = con.cursor()
            cur.execute("SELECT * FROM passwords")
            entries = cur.fetchall()
            if len(entries) == 0:
                print("You have no saved paswords!")
            else:
                for row in entries:
                    print("==================")
                    print("Website:", row[0])
                    print("Username: ", row[1])
                    print("Passsword: ", row[2])
            con.close()
        except Exception as e:
            print(f"[1] {e}")
