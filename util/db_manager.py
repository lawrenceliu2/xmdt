import sqlite3

#need to retrive previous id instead

u = "data/userdata.db"
s = "data/stories.db"

udb = sqlite3.connect(u)
sdb = sqlite3.connect(s)
users = udb.cursor()
stories = sdb.cursor()

def nameAvail(username):
     q = "SELECT * FROM users WHERE username = %s;" % (username)
     udb.execute(q)
     info = udb.fetchall()
     if (len(info) > 0): return False
     else: return True

def addUser(username, password):
    q = "INSERT INTO users VALUES (\"%s\", %s, %s)" % (username, password, 1)
    udb.execute(q)
    
def addStory(ipt, title):
    #timestamp = stuff
    q = "INSERT INTO " + title + " VALUES (\"%s\", %s, %s)" % (timestamp, 1, ipt)
    sdb.execute(q)

#def showStuff
