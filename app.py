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
        return render_template('login.html')

@app.route('/rauth', methods=["POST"])
def auth_register():
    if request.form["pass"]!=request.form["pass-conf"]:
        return redirect(url_for('disp_register'))
    elif addUser(request.form["username"], request.form["pass"]) == 1:
        return redirect(url_for('disp_homepage'))
    else:
        return redirect(url_for('disp_register'))
    
@app.route('/storylist')
def home():
    if 'username' in session:
        return render_template('story.html', stories=getStories())
    else:
        return redirect(url_for('disp_homepage'))

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('disp_homepage'))


if __name__=="__main__":
    app.debug = True
    app.run()
