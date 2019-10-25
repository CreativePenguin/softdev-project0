#Jackson Zou
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3
import csv

def displayBlogs(userid):
    """Returns all blogs of a user specified by their userid. The return value of this method is going to a list of blogs. The overall list will be organized by
    [blog1, blog2, blog3, ...] and each blog will be a list so blog1 = [blog_id, blog_name, entry1, entry2, ...]"""
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================

    command = "SELECT blogs.user_id, blogs.blog_id, blog_name, entry_num, entry_text FROM blogs INNER JOIN entries ON blogs.user_id = entries.user_id AND blogs.blog_id = entries.blog_id WHERE blogs.user_id = {};".format(userid)
    c.execute(command)
    q = c.fetchall()
    final = []
    for entry in q:
        index = entry[1] - 1
        if len(final) == index:
            final.append([])
            final[index].append(entry[1])
            final[index].append(entry[2])
            final[index].append(entry[4])
        else:
            final[index].append(entry[4])
    #==========================================================

    db.commit() #save changes
    db.close()  #close database

    return final

def displayEntries(userid, blogid):
    """Returns all entries for the specified user_id, blog_id combination. Return value will be a list formatted as [blog_id, blog_name, entry1, entry2,...]"""
    DB_FILE="data/databases.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #==========================================================

    command = "SELECT blog_name, entry_num, entry_text FROM blogs INNER JOIN entries ON blogs.user_id = entries.user_id AND blogs.blog_id = entries.blog_id WHERE blogs.user_id = {} AND blogs.blog_id = {};".format(userid, blogid)
    c.execute(command)
    q = c.fetchall()
    final = []
    final.append(q[0][0])
    final.append(q[0][1])
    for entry in q:
        final.append(entry[2])

    #==========================================================
    db.commit() #save changes
    db.close()  #close database

    return final