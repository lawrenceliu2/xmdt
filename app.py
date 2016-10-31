# Xtreme Meme Dream Team
import os
from flask import Flask, request, render_template, direct, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def disp_homepage():
    return render_template('inhex.html')

@app.route('/login')
def disp_login():
    return render_template('auth.html')

@app.route('/register')
def disp_register():
    return render_template('auth.html')

@app.route('/home')
def disp_stories():
