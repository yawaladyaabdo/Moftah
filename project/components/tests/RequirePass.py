import getpass
import sqlite3

class RequirePass:
    def __init__(self):
        self.RequirePassFunction()
    
    def RequirePassFunction(self):
        try:
            user = getpass.getuser()
            con = sqlite3.connect(
                f'/home/{user}/.config/moftah/db/passwords.db')
            cur = con.cursor()
            insertQuery = """SELECT password FROM userpass"""
            cur.execute(insertQuery)
            password = cur.fetchone()
            x = getpass.getpass(
                f"Welcome to Moftah, {user}. Please enter your password: ")
            if x == password:
                return True
            con.close()
        except Exception as e:
            print(f"[1] {e}")