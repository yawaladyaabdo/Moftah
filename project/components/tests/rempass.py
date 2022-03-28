import getpass
import sqlite3


class RemPass:
    def __init__(self):
        self.RemPassFunction()

    def RemPassFunction(self):
        user = getpass.getuser()
        con = sqlite3.connect(
                f'/home/{user}/.config/moftah/db/passwords.db')
        cur = con.cursor()
        print("Please enter the credentials correctly!")
        webs = input("Website: ")
        usern = input("User: ")
        query = """DELETE FROM passwords WHERE website = ? AND user = ?"""
        cur.execute(query, (webs, usern,))
        con.commit()
        print("Updated passwords")
        con.close()