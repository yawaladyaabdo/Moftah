from getpass import getuser
import sqlite3
import json


class colors:
    # Important colors
    OKGREEN = '\033[92m'  # noqa: F841
    WARNING = '\033[93m'  # noqa: F841
    FAIL = '\033[91m'  # noqa: F841
    ENDC = '\033[0m'  # noqa: F841
    BOLD = '\033[1m'  # noqa: F841
    FAIL = '\033[91m'  # noqa: F841


class Main():
    def __init__(self):
        self.checkFirstRun()

    def InputManager(self):
        """
        Gives user choices
        """
        USERNAME = getuser()
        CNFPATH = f'/home/{USERNAME}/.config/moftah'
        con = sqlite3.connect(f'{CNFPATH}/db/passwords.db')
        cur = con.cursor()

        cur.execute("""
                SELECT password FROM userpass
                """)
        PASSWORD = cur.fetchone()
        PASSWORD = ''.join(PASSWORD)
        CHECK = input("Please enter your password: ")
        try:
            if CHECK == PASSWORD:
                try:
                    print(f"""
Welcome back, {USERNAME}.
Please pick an option.
1. Add a password
2. Remove a password
3. View all my passwords
4. REMOVE EVERYTHING
                    """)
                    con.close()
                    OPTION = input("Which option will you pick: ")
                    i = 0
                    n = 10
                    while i < n:
                        if OPTION == "1":
                            from components.PasswordAdder import PasswordAdder
                            PasswordAdder()
                            i = 11
                        elif OPTION == "2":
                            from components.PasswordRemover import PasswordRemover
                            PasswordRemover()
                            i = 11
                        elif OPTION == "3":
                            from components.PasswordViewer import PasswordViewer
                            PasswordViewer()
                            i = 11
                        elif OPTION == "4":
                            from components.PasswordNuker import PasswordNuker
                            PasswordNuker()
                            i = 11
                        else:
                            i = 0
                except Exception as e:
                    print(colors.FAIL + f"[1] {e}" + colors.ENDC)
            else:
                print(colors.FAIL + "[1] Wrong password" + colors.ENDC)
                exit()
        except Exception as e:
            print(colors.FAIL + f"[1] {e}" + colors.ENDC)

    def setup(self):
        """
        Sets up the user details
        """
        USERNAME = getuser()
        CNFPATH = f'/home/{USERNAME}/.config/moftah'
        con = sqlite3.connect(f'{CNFPATH}/db/passwords.db')
        cur = con.cursor()
        print(
            f"""
            Hi there, {USERNAME}.
            Since it is your first time running Moftah we will
            go through the setup process. You need a password
            to protect your stuff so how about we start with that
            """)
        PASSWORD = input("Please enter a password: ")
        cur.execute("""
CREATE TABLE "passwords" (
    "website"	TEXT,
    "user"	TEXT,
    "password"	TEXT
);""")
        cur.execute("""
CREATE TABLE "userpass" (
    "password"	TEXT
);""")
        con.commit()
        cur.execute(
            """INSERT INTO userpass VALUES (?)""", (PASSWORD,))
        con.commit()
        con.close()

    def checkFirstRun(self):
        try:
            # Variables needed to connect to the database
            USERNAME = getuser()
            CNFPATH = f'/home/{USERNAME}/.config/moftah'
            with open(f'{CNFPATH}/log/log.json', 'r+') as config:
                f = json.load(config)
                if f['ran'] == "0":
                    self.setup()

                else:
                    self.InputManager()
        except Exception as e:
            print(f"[1] {e}")


if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
