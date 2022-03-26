import sqlite3
import getpass
import base64
import json

user = getpass.getuser()

class Main():
    def __init__(self):
        self.checkFirstRun()
        
    def checkFirstRun(self):
        with open('../config.json', 'r+') as config:
            f = json.load(config)
            if f['password'] == "firstrun":
                print(f"""
It seems that you are running Moftah for the first time, {user}.\n
We'll have to update the password now so please enter a new password!
                      """)
                newpass = getpass.getpass(prompt="New password: ")
            else:
                print('bing')
        
        
    def writePassword(self, password):
        """Writes the new password to a json file.

        Args:
            password (string)
        """
        with open('../config.json', 'r+') as config:
            f = json.load(config)
            f['password'] = password
            config.seek(0)
            json.dump(f, config)
            config.truncate()
        
    def requirePassword(self):
        try:
            x = getpass.getpass(f"Welcome to Moftah, {user}. Please enter your password: ")
        except Exception as e:
            print("Wrong password")
        
if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        