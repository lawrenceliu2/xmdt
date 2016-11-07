# Xtreme Meme Dream Team
import os
from flask import Flask, flash, request, render_template, redirect, url_for, session
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
        flash("Username and password do not match, please try again.")
        return redirect(url_for('home'))

    
@app.route('/rauth', methods=["POST"])
def auth_register():
    if len(request.form["username"])<4:
        flash("Username too short! Please choose a longer one.")
        return redirect(url_for('disp_register'))
    if len(request.form["username"])>16:
        flash("Username too long! Please choose a shorter one.")
        return redirect(url_for('disp_register'))
    
    if len(request.form["pass"])<4:
        flash("Password too short! Please choose a longer one.")
        return redirect(url_for('disp_register'))
    if len(request.form["pass"])>16:
        flash("Password too long! Please choose a shorter one.")
        return redirect(url_for('disp_register'))
    
    if request.form["pass"]!=request.form["pass-conf"]:
        flash("Passwords do not match! Try again.")
        return redirect(url_for('disp_register'))
    elif addUser(request.form["username"], request.form["pass"]) == 1:
        flash("Account successfully created, please log in.")
        return redirect(url_for('home'))
    else:
        flash("Username already in use, please choose a different one.")
        return redirect(url_for('disp_register'))

    
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

@app.route('/cauth', methods=["POST"])
def auth_create():
<<<<<<< HEAD
    addStory(request.form['title'], "meme 'o clock", \
             request.form['content'], request.form['userid'])

    
=======
    addStory(request.form['title'], "meme 'o clock", request.form['init'], getID(session["username"]))
    redirect(url_for('disp_story('+sanitize(request.form['title'])+')'))
    
             
>>>>>>> 16690925d1cfbe1d50265f1cbe7cec968057f710
@app.route('/logout', methods=["GET"])
def logout():
    if 'username' in session:
        session.pop('username')
    #return render_template('login.html', message="Successfully logged out.")
    flash("Successfully logged out.")
    return redirect(url_for("disp_homepage"))


if (__name__ == "__main__"):
    app.debug = True
    app.run()
