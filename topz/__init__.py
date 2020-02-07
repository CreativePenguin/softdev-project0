# Jackson Zou
# SoftDev1 PD 9
# p00


from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from utl import createDB
from utl import checkLogin
from utl import checkUser
from utl import newuser
from utl import readDB
from utl import addDB

import sqlite3
import os
os.path.dirname(__file__)
DIR = os.path.dirname(__file__)
DIR += '/'

DB_FILE ="{}databases.db".format(DIR)

DIR += DB_FILE

app = Flask(__name__)
app.secret_key = os.urandom(32) #generates a secret key for session to start
createDB.createTable() #always create tables when first run, just in case tables don't exist

@app.route("/")
def firstLogin():
    if ('username' in session and 'password' in session):
        redirect(url_for("home"))
    return render_template('login.html',errorMessage = "")

@app.route("/login", methods=["POST"])
def login():
    #print(request.form)
    if(request.form['sub1'] == 'Register'):
        return render_template('register.html', errorMessage = "")
    else:
        session['username'] = request.form["username"]          # assign username key in session to inputted username
        session['password'] = request.form["password"]          # assign password key in session to inputted password
        if (session):
            username = session['username']
            password = session['password']
            validLogin = checkLogin.checkLogin(username, password) #temp for testing
            if (validLogin == -1):
                return render_template('login.html', errorMessage = "Invalid Credentials")
            return redirect(url_for("home"))
        else:
            return render_template('login.html',errorMessage = "")


@app.route("/register", methods=["POST"])
def register():
    if(request.form['sub1'] == 'Log In'):
        return redirect(url_for("firstLogin"))
    else:
        session['username'] = request.form["username"]          # assign username key in session to inputted username
        session['password'] = request.form["password1"]          # assign password key in session to inputted password1
        session['password2'] = request.form["password2"]          # assign password key in session to inputted password2
        if (session):
            username = session['username']
            password1 = session['password']
            password2 = session['password2']
            if password1 == '' or password2 == '':
                return render_template('register.html', errorMessage = 'Password cannot be blank')
            if (password1 == password2):
                if (newuser.addUser(username, password1) != -1):
                    return redirect(url_for("home"))
                return render_template('register.html',
                    errorMessage = "Username already taken")
            return render_template('register.html',
                errorMessage = "Passwords do not match. Please try again.")
        return render_template('register.html', errorMessage = "")

    #add user checks if account exists (returns false). If DNE, enters into database, returns true

@app.route("/logout", methods=["GET"])
def logout():      # route logs out the user by getting rid of username and password in session
    if ('username' in session and 'password' in session):
        session.pop('username')
        session.pop('password')
        if 'password2' in session:
            session.pop('password2')
        return redirect(url_for("firstLogin"))                # redirect to beginning
    return redirect(url_for("firstLogin"))                # redirect to beginning


@app.route("/home", methods = ["GET", "POST"])
def home():
    #print(request.form)

    if ('username' in session and 'password' in session):
        if('profileRedirect' in request.form):
            return redirect("/user/" + session['username'])
        user = session['username']
        #VARIABLES TO PASS
        entries = readDB.getAllBlogs()
        return render_template("home.html",
            username = user,
            recentEntries = entries)
    return redirect(url_for("firstLogin"))


@app.route("/user/<user>")
def userPage(user):
    #username = session[username] return specific template
    # if user DNE: return error template

    if ('username' in session and 'password' in session):
        if (user == session["username"]):
            return render_template("user.html",
                user = user,
                myBlogs = readDB.displayBlogs(user))
        return render_template("otherUser.html",
            user = user,
            theirBlogs=readDB.displayBlogs(user))
    return redirect(url_for("firstLogin"))


@app.route("/user/<user>/blog/<blogid>")
def blogPage(user,blogid):
    if ('username' in session and 'password' in session):
        userid = readDB.getUserID(user)
        entries = readDB.displayOnlyEntries(user, blogid)
        print(session)
        #print(entries)
        if (user == session["username"]):
            return render_template("blog.html",
                user = user,
                blogid = blogid,
                blogname = readDB.getBlogName(userid,blogid),
                myEntries = entries)
        return render_template("otherBlog.html",
            user = user,
            blogid = blogid,
            blogname = readDB.getBlogName(userid,blogid),
            theirEntries=entries)
    return redirect(url_for("firstLogin"))

@app.route("/search", methods = ['POST'])
def search():
    if ('username' in session and 'password' in session):
        if('search1' in request.form and 'keywords' in request.form):
            session['search'] = request.form['keywords']
            input = str(session['search'])
            results = readDB.searchUp(input)
            return render_template('searchresults.html', searchresults = results, keyword = input)
    return redirect(url_for("firstLogin"))

@app.route("/addBlog", methods=['POST'])
def addBlog():
    if ('username' in session and 'password' in session):
        user = session['username']
        userid = readDB.getUserID(session['username'])
        #print(request.form)
        if('title' in request.form and request.form['title'] != ""):
            addDB.createBlog(int(readDB.getUserID(session['username'])), str(request.form['title']))
            return redirect("/user/" + session['username'])
        return render_template('addBlog.html', user = user, userid = userid)
    return redirect(url_for("firstLogin"))

@app.route("/addEntry/<blogid>", methods=['POST'])
def addEntry(blogid):
    if ('username' in session and 'password' in session):
        user = session['username']
        userid = readDB.getUserID(session['username'])
        print(request.form)
        if('entry' in request.form and request.form['entry'] != ""):
            addDB.addEntry(int(readDB.getUserID(session['username'])), blogid, str(request.form['entry']))
            return redirect("/user/" + session['username'] + "/blog/" + blogid)
        return render_template('addEntry.html', user = user, userid = userid, blogid = blogid)
    return redirect(url_for("firstLogin"))

@app.route("/editEntry/blog/<blogid>/entry/<entrynum>", methods=['POST'])
def editBlog(blogid, entrynum):
    if ('username' in session and 'password' in session):
        user = session['username']
        userid = readDB.getUserID(session['username'])
        #print(request.form)
        if('entry' in request.form and request.form['entry'] != ""):
            addDB.editEntry(int(readDB.getUserID(session['username'])), blogid, entrynum, str(request.form['entry']))
            return redirect("/user/" + session['username'] + "/blog/" + blogid)
        return render_template('editEntry.html', user = user, userid = userid, blogid = blogid, entrynum = entrynum, oldentry = readDB.getEntry(userid,blogid,entrynum))
    return redirect(url_for("firstLogin"))

if __name__ == "__main__":
    app.debug = False
    app.run()
