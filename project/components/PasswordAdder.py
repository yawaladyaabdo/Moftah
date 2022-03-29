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


class PasswordAdder:
    def __init__(self):
        """
        Adds the user's password to their database
        """
        self.add()

    def add(self):
        """
        Adds password to database
        """
        i = 0
        n = 10
        while i < n:
            # Variables needed to connect to the database
            USERNAME = getuser()
            CNFPATH = f'/home/{USERNAME}/.config/moftah'
            # Ask the user for the important website details
            WEB = input("Enter the name of this website: ")
            USER = input("Enter your username on the website: ")
            PASSWORD = input("Enter your password: ")

            print(f'''
Is this information correct?
Website: {WEB}
Username: {USER}
Password: {PASSWORD}''')
            QUESTION = input("[" + colors.OKGREEN + "Y" + colors.ENDC + "/" + colors.FAIL + "N" + colors.ENDC + "] ")
            if QUESTION in ("Y", "y", "Yes", "yes"):
                # Creating the website connection and creating the cursor
                con = sqlite3.connect(f'{CNFPATH}/db/passwords.db')
                cur = con.cursor()
                cur.execute('''
                    INSERT INTO passwords(website,user,password) VALUES (?, ?, ?)
                ''', (WEB,USER,PASSWORD,))  # noqa: E231
                # Commit changes
                con.commit()
                con.close()
                exit()
            elif QUESTION in ("N", "n", "No", "n"):
                i = 0
            else:
                i = 0
