import sqlite3
from tkinter import *

root = Tk()
root.geometry("400x400")

# def submit():



# connect to database
conn = sqlite3.connect('users.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE IF NOT EXISTS users(
    user_ID integer primary key autoincrement not null,
    username text not null,
    password text not null
)""")

# user input
for i in range(1):
    username = input("Username: ").capitalize()
    password = input("Password: ").capitalize()

# inserting data into table
conn.execute("INSERT INTO users VALUES ('{}','{}')".format(username,password))

# commit command
conn.commit()

# close connection
conn.close()

root.mainloop()
