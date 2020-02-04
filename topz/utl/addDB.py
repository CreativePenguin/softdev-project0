#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv
import os
DB_FILE = os.path.dirname("data/databases.db")
def addEntry(userid, blogid, entrytext):
    """adds an entry into the blog taking in the userid, blogid, and the blog text. This method returns nothing"""
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================

    command = "SELECT entry_num FROM entries WHERE user_id = {} AND blog_id = {};".format(userid, blogid) #gets all entry numbers for that current blog
    c.execute(command)
    q = c.fetchall();
    newentry_id = q[len(q)-1][0]+1
    command = "INSERT INTO entries VALUES({},{},{},\"{}\");".format(userid, blogid, newentry_id, entrytext) #adds the entry into the database with a new entry num
    c.execute(command)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

def editEntry(userid, blogid, entrynum, entrytext):
    """edits an entry in the database based on the userid, blogid, entrynum, and the updated entrytext"""
        db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "UPDATE entries SET entry_text = \"{}\" WHERE user_id = {} AND blog_id = {} AND entry_num = {};".format(entrytext, userid, blogid, entrynum)
    #updates the previous entry based on the blog parameters with the new entry text
    c.execute(command)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

def createBlog(userid, blogtitle):
    """creates a new blog for a user with a blogname, and will add it to the blogs db. When the blog is created, it will be initialized by a pilot entry """
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================
    command = "SELECT blog_id FROM blogs WHERE user_id = {};".format(userid) #gets all blogids for a user and looks for the next available id
    c.execute(command)
    q = c.fetchall()
    if len(q) == 0:
        blogid = 1 #sets id equal to 1 if they don't have any previous blogs
    else:
        blogid = q[len(q)-1][0] + 1 #otherwise gives next available number

    command = "INSERT INTO blogs VALUES({},{},\"{}\")".format(userid, blogid, blogtitle) #adds blog title into blogs db
    c.execute(command)
    command = "INSERT INTO entries VALUES({},{},{},\"{}\")".format(userid, blogid, 0, "Pilot Entry") #adds a pilot entry into the entries db
    c.execute(command)
    #==========================================================

    db.commit() #save changes
    db.close()  #close database
