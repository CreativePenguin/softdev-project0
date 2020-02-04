#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv
import os

DB_FILE = os.path.dirname("/data/databases.db")
def addUser(username, password):
    """method for registering a new user"""

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT user_id, username FROM users WHERE username = \"{}\";".format(username) #checks whether username has already been used
    c.execute(command)
    new = c.fetchall()
    if len(new) == 0: #runs if username is open
        command = "SELECT user_id FROM users;"
        c.execute(command)
        q = c.fetchall()
        new_id = q[len(q)-1][0]+1
        command = "INSERT INTO users VALUES({}, \"{}\", \"{}\");".format(q[len(q)-1][0]+1,username,password) #stores username, password into the users db and gives it next available user id
        c.execute(command)
        db.commit() #save changes
        db.close()  #close database
        #print(new_id)
        return new_id #returns the new id of the user
    else:
        db.commit() #save changes
        db.close()  #close database
        return -1 #returns -1 if username already exists as bad value
    #==========================================================
