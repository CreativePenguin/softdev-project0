#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv
import os
import subprocess
from os.path import join, dirname, abspath
DB_FILE = join(dirname(dirname(abspath(__file__))), 'data/databases.db')

def saltPassword(username, password):
    """uses username and password to create a salt to encrypt passwords"""
    return subprocess.run(['lesspass', '206.189.68.125', username, password],
                          stdout=subprocess.PIPE).stdout

def checkLogin(username, password):
    """returns userid of the username, password pair and returns -1 if it doesn't exist """

    password = saltPassword(usernma,e password)
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT user_id, username FROM users WHERE username = \"{}\" AND password = \"{}\";".format(username, password) #looks for the username,password combination in the users db
    c.execute('SELECT user_id, username FROM users where username = ? AND password = ?',
              [username, password])
    q = c.fetchall()
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    if len(q) == 0:
        return -1 #return -1 if it doesn't exist
    if q[0][0] == "" or q[0][1] == "": #doesn't allow for username or password to be empty
        return -1
    else:
        return q[0][0] #return ID of user if exists
