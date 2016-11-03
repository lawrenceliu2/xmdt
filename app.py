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
    return render_template('login.html')

@app.route('/register', methods=["POST"])
def disp_register():
    return render_template('register.html')


@app.route('/auth', methods=["POST"])
def authenticate():
    if request.form["username"]=="" and request.form["pass"]=="":#gotta get users info from database, FORTUNES JOB
        session["username"] = request.form["username"]
        return render_template("home.html", message="youre in my dude")
    else:
        if request.form["username"]=="":#gotta get users info from database, FORTUNES JOB
            return render_template("login.html", message="wrong password my dude, try again")
        elif request.form["pass"]=="":#gotta get users info from database, FORTUNES JOB
            return render_template("login.html", message="wrong username my dude, try again")
        else:
            return render_template("login.html", message="no account with those credentials my dude, try again")

        
@app.route('/registration', methods=["POST"])
def registration():
    if request.form["username"]=="":#find the user in the users.db, FORTUNES JOB
        return render_template("register.html", message="that username is taken my dude, try again")
    elif request.form["pass"] != request.form["pass-conf"]:
        return render_template("register.html", message="passwords dont match my dude, try again")
    else:
        return render_template("login.html", message="account successfully created my dude, login now")
            

                
@app.route('/home')
def disp_stories():
    return render_template('home.html')



if __name__=="__main__":
    app.debug = True
    app.run()
