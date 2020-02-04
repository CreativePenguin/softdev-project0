#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv
import os

DB_FILE ="../data/databases.db"

def checkUser(username):

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT user_id, username FROM users WHERE username = \"{}\";".format(username)
    c.execute(command)
    q = c.fetchall()
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    else:
        return q[0][0] #return ID of user if exists
