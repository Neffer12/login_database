import sqlite3
from tkinter import *

root = Tk()
root.geometry("400x400")


def database():
    # connect to database
    conn = sqlite3.connect('users.db')
    # create a cursor
    c = conn.cursor()

    # create a table
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        username text not null,
        password text not null,
        first_name text,
        last_name text
    )""")

    # inserting Admin if not in table
    conn.execute("INSERT OR IGNORE INTO users (username, password, first_name) VALUES"
                 " ('Admin', 'admin', 'Administration')")


def login(conn):
    # getting data for login
    user = username.get()
    pwd = password.get()

    # if empty values
    if user == '' or pwd == '':
        print("fill all the fields")
    else:
        # select query
        cursor = conn.execute('SELECT * from users where username = "%s" and password = "%s"' % (user, pwd))

    # commit command
    conn.commit()

    # close connection
    conn.close()

root.mainloop()
