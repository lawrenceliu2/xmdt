# Xtreme Meme Dream Team
import os
from flask import Flask, request, render_template, redirect, url_for, session

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
    return render_template('index.html')


'''
@app.route('/login')
def disp_login():
    #session["username"] = request.form["username"]
    return render_template('login.html')

@app.route('/register')
def disp_register():
    return render_template('register.html') 

@app.route('/home')
def disp_stories():
return render_template('home.html')'''

