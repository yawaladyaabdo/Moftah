from .RequirePass import RequirePass
from .addpass import AddPass
from .rempass import RemPass
from .seepass import SeePass
from .nuke import Nuke
import sqlite3


class Manager:
    def __init__(self):
        self.ManagePasswords()

    def ManagePasswords(self):
        try:
            PasswordAsker = RequirePass()
            if PasswordAsker == True:
                print("Please type the number next to the text")
                print("(1) new info: ")
                print("(2) View all passwords")
                print("(3) Remove a password")
                print("(4) RESET FULLY (DANGEROUS): ")
                pick = input("Pick a number: ")
                if pick == "1":
                    AddPass()
                elif pick == "2":
                    SeePass()
                elif pick == "3":
                    RemPass()
                elif pick == "4":
                    Nuke()
            else:
                print('[1] Wrong password!')
        except Exception as e:
            print(f"[1] {e}")
