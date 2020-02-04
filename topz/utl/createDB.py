#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv
import os
DB_FILE = os.path.dirname("data/databases.db")

def createTable():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, password TEXT);"
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS blogs (user_id INTEGER, blog_id INTEGER, blog_name TEXT);"
    c.execute(command)
    command = "CREATE TABLE IF NOT EXISTS entries (user_id INTEGER, blog_id INTEGER, entry_num INTEGER, entry_text TEXT);"
    c.execute(command)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database
