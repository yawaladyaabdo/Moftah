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


class PasswordRemover:
    def __init__(self):
        """
        Removes the user's password from their database
        """
        self.rem()

    def rem(self):
        """
        Removes password from database
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
                        SELECT * FROM passwords''')
            data = cur.fetchall()
            con.close()
            if len(data) == 0:
                print(colors.FAIL + "[1] You have no passwords!" + colors.ENDC)
                con.close()
                exit()
            else:
                # Creating the website connection and creating the cursor
                con = sqlite3.connect(f'{CNFPATH}/db/passwords.db')
                cur = con.cursor()
                WEB = input('Enter the website name: ')
                USER = input('Enter the username associated with that website: ')
                cur.execute(
                    '''SELECT * FROM passwords WHERE website = ? AND user = ?''',
                    (WEB,USER,))  # noqa: E231
                details = cur.fetchone()
                if details is None:
                    print(colors.FAIL + "[1] Those details do not exist" + colors.ENDC)
                    i = 0
                    con.close()
                else:
                    cur.execute(
                        '''DELETE FROM passwords WHERE website = ? AND user = ?''',(WEB,USER,))  # noqa: E231
                    print(colors.OKGREEN + "[0] Deleted password from database!" + colors.ENDC)
                    i = 11
                    con.commit()
                    con.close()
                    exit()
