#Connor Oh
#SoftDev
#search :: Searching
#Oct 2019
from utl import readDB

def searchUp(search):
    """From the search input it will check through the blogs list on the homepage to
    see which blogs have usernames, blog numbers, blog names, and entries that contain
    the key word"""
    allBlogs = readDB.getAllBlogs()
    results = []
    for blog in allBlogs:
        if search in str(blog[0]):
            results.append(blog)
        elif search in str(blog[1]):
            results.append(blog)
        elif search in str(blog[2]):
            results.append(blog)
        elif search in str(blog[3]):
            results.append(blog)
    return results

#print(search("Jacob's"))
