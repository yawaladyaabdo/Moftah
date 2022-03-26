import sqlite3
import getpass
import json
import time
import os

user = getpass.getuser()


class Main():
    def __init__(self):
        self.checkFirstRun()


    def checkFirstRun(self):
        try:
            # Create database connection
            con = sqlite3.connect(f'/home/{user}/.config/moftah/db/passwords.db')
            cur = con.cursor()
 

            with open(f"/home/{user}/.config/moftah/log/log.json", "r+") as config:
                f = json.load(config)

                if f['ran'] == 0:
                    cur.execute("""
CREATE TABLE "passwords" (
	"website"	TEXT,
	"user"	TEXT,
	"password"	TEXT
);

                    """)
                    con.commit()
                    cur.execute("""
CREATE TABLE "userpass" (
	"password"	TEXT
);
            """)
                    con.commit()
                    print(f"""
It seems that you are running Moftah for the first time, {user}.\n
We'll have to update the password now so please enter a new password!
                      """)

                    # Ask for a master password
                    newpass = getpass.getpass(prompt="New password: ")

                    # Insert password
                    insertQuery = """INSERT INTO userpass VALUES (?)"""
                    cur.execute(insertQuery, (newpass,))
                    con.commit()

                    # Rewrite the number in json
                    f['ran'] = 1
                    config.seek(0)
                    json.dump(f, config)
                    config.truncate()
                    config.close()
                    print("Please rerun this!")
                else:
                    try:
                        con = sqlite3.connect('db/passwords.db')
                        cur = con.cursor()
                        insertQuery = """SELECT password FROM userpass"""
                        cur.execute(insertQuery)
                        x = cur.fetchone()
                        x = ''.join(x)
                        y = input(
                            f"Welcome back {user}, please enter your master password: ")
                        if x == y:
                            print("Please type the number next to the text")
                            print("(1) new info: ")
                            print("(2) View all passwords")
                            print("(3) RESET FULLY (DANGEROUS): ")
                            pick = input("Pick a number: ")
                            if pick == "1":
                                while 420 > 69:
                                    webs = input("Website name: ")
                                    if webs == None:
                                        print("You didn't enter a website name!")
                                        return
                                    else:
                                        pass
                                    usern = input("Username: ")
                                    if usern == None:
                                        print("You didn't enter a username")
                                        return
                                    else:
                                        pass
                                    passw = input("Password: ")
                                    if passw == None:
                                        print("You didn't enter a password!")
                                        return
                                    else:
                                        pass
                                    print(f"Username: {usern}, Password: {passw}, Website: {webs}")
                                    que = input("Correct? [Y/N]: ")
                                    
                                    if que.casefold() == "y":
                                        query = """
                                        INSERT INTO passwords(website,user,password) VALUES (?,?,?);
                                        """
                                        
                                        cur.execute((query), (webs,usern,passw,))
                                        con.commit()
                                        print("Updated your passwords!")
                                        con.close()
                                        exit()
                                    else:
                                        que = input("Repeat? [Y/N] ")
                                        if que.casefold():
                                            return
                                        else:
                                            print("Goodbye!")
                                            con.close()
                                            exit()
                            elif pick == "2":
                                cur.execute("SELECT * FROM passwords")
                                entries = cur.fetchall()
                                for row in entries:
                                    print("==================")
                                    print("Website:", row[0])
                                    print("Username: ", row[1])
                                    print("Passsword: ", row[2])
                            elif pick == "3":
                                os.system('rm db/passwords.db')
                                time.sleep(2)
                                con = sqlite3.connect('db/passwords.db')
                                con.close()
                                print("Removed all passwords!")
                                with open("log/log.json", "r+") as config:
                                    f = json.load(config)
                                    
                                    f['ran'] = 0
                                    config.seek(0)
                                    json.dump(f, config)
                                    config.truncate()
                                    config.close()
                                exit()
                        else:
                            print('[1] Wrong password!')
                    except Exception as e:
                        print(f"[1] Wrong password!")
        except Exception as e:
            print(f"[1] {e}")

    def requirePassword(self):
        try:
            x = getpass.getpass(
                f"Welcome to Moftah, {user}. Please enter your password: ")
        except Exception as e:
            print("Wrong password")
    
    


if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
