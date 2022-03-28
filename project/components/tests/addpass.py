import sqlite3


class AddPass:
    def __init__(self):
        self.AddPassFunction()

    def AddPassFunction(self):
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

                cur.execute((query), (webs, usern, passw,))
                con.commit()
                print("Updated your passwords!")
                con.close()
                exit()
            else:
                que = input("Repeat? [Y/N] ")
                if que.casefold() == "N":
                    return
                else:
                    print("Goodbye!")
                    con.close()
                    exit()
