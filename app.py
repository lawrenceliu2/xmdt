# Xtreme Meme Dream Team
import os
from flask import Flask, request, render_template, redirect, url_for, session
from utils.db_manager import *

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def disp_homepage():
    if 'username' in session:
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/register', methods=["GET"])
def disp_register():
    return render_template('register.html')

@app.route('/auth', methods=["POST"])
def authenticate():
    if userAuth(request.form["username"], request.form["pass"]):
        session["username"] = request.form["username"]
        return redirect(url_for('home'))
    else:
        return render_template('login.html', message="Username and password do not match, please try again.")

@app.route('/rauth', methods=["POST"])
def auth_register():
    if request.form["pass"]!=request.form["pass-conf"]:
        return render_template('register.html', message="Passwords do not match! Try again.")
    elif addUser(request.form["username"], request.form["pass"]) == 1:
        return render_template('login.html', message= "Account successfully created, please log in.")
    else:
        return render_template('register.html', message="Username already in use, please choose a different one.")
    
@app.route('/storylist', methods=["GET"])
def home():
    if 'username' in session:
        return render_template('stories.html', stories=getStories())
    else:
        return redirect(url_for('disp_homepage'))

@app.route('/story/<storyname>', methods=["GET"])
def disp_story(storyname):
    if 'username' in session:
        return render_template('story.html',story=getStories()[storyname])
    else:
        return redirect(url_for('disp_homepage'))

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/logout', methods=["GET"])
def logout():
    if 'username' in session:
        session.pop('username')
    #return render_template('login.html', message="Successfully logged out.")
    return redirect(url_for("disp_homepage"))


if (__name__ == "__main__"):
    app.debug = True
    app.run()
