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


class PasswordViewer:
    def __init__(self):
        """
        View the user's passwords
        """
        self.see()

    def see(self):
        """
        View's all the user's passwords
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
                    SELECT * FROM passwords
                    ''')
            data = cur.fetchall()
            if len(data) == 0:
                print(colors.FAIL + "[1] You have no passwords" + colors.ENDC)
                exit()
            else:
                print(f"[0] You have {len(data)} passwords")
                for row in data:
                    print("==================")
                    print("Website:", row[0])
                    print("Username: ", row[1])
                    print("Passsword: ", row[2])
                con.close()
                i = 11
                exit()
