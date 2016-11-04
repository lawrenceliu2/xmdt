# Xtreme Meme Dream Team
import os, util.db_manager
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
    return render_template('login.html')

@app.route('/register', methods=["POST"])
def disp_register():
    return render_template('register.html')


@app.route('/auth', methods=["POST"])
def authenticate():
    if db_manager.userAuth(request.form["username"], request.form["pass"]):
        session["username"] = request.form["username"]
        return render_template("home.html", message="youre in my dude")
    else:
        return render_template("home.html", message="you dun gofed my dude")

@app.route('/rauthgister', methods=["POST"])
def auth_register():
    if db_manager.addUser(request.form["username"], request.form["pass"]) == 1:
        return render_template("home.html")
    else:
        return render_template("register.html")
    
@app.route('/home')
def disp_stories():
    return render_template('home.html')



if __name__=="__main__":
    app.debug = True
    app.run()
