from getpass import getuser
import sqlite3


class colors:
    # Important colors
    OKGREEN = '\033[92m'  # noqa: F841
    WARNING = '\033[93m'  # noqa: F841
    FAIL = '\033[91m'  # noqa: F841
    ENDC = '\033[0m'  # noqa: F841
    BOLD = '\033[1m'  # noqa: F841
    FAIL = '\033[91m'  # noqa: F841


class PasswordNuker:
    def __init__(self):
        """
        Removes ALL the user's passwords
        """
        self.nuke()

    def nuke(self):
        """
        Removes ALL the user's passwords
        """
        i = 0
        n = 10
        while i < n:
            # Variables needed to connect to the database
            USERNAME = getuser()
            CNFPATH = f'/home/{USERNAME}/.config/moftah'

            # Creating the website connection and creating the cursor
            con = sqlite3.connect(f'{CNFPATH}/db/passwords.db')
            cur = con.cursor()
            cur.execute('''
                        DELETE FROM passwords
                    ''')
            con.commit()
            print(colors.OKGREEN + f"[0] Deleted {cur.rowcount} passwords" + colors.ENDC)
            con.close()
            exit()
