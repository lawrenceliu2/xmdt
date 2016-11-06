# Xtreme Meme Dream Team
import os
from flask import Flask, request, render_template, redirect, url_for, session
from utils.db_manager import *

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def disp_homepage():
    # =================================
    print '\n\n\n'
    print '=== DIAGNOSTICS === this Flask object'
    print app
    print '=== DIAGNOSTICS === request object'
    print request
    print '=== DIAGNOSTICS === request.headers'
    print request.headers
    # =================================
    return render_template('login.html')

@app.route('/register', methods=["GET"])
def disp_register():
    return render_template('register.html')

@app.route('/auth', methods=["POST"])
def authenticate():
    if userAuth(request.form["username"], request.form["pass"]):
        session["username"] = request.form["username"]
        return render_template("home.html", message="youre in my dude")
    else:
        return render_template("home.html", message="you dun gofed my dude")

@app.route('/rauth', methods=["POST"])
def auth_register():
    if addUser(request.form["username"], request.form["pass"]) == 1:
        return redirect(url_for('home'))
    else:
        return render_template("register.html")
@app.route('/home')
def home():
    return render_template('profile.html', storylist=getStories())

if __name__=="__main__":
    app.debug = True
    app.run()
