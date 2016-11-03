import sqlite3

uid = 1
sid = 1

u = "data/userdata.db" #not sure if i have to do data/ first
s = "data/stories.db"

udb = sqlite3.connect(u)
sdb = sqlite3.connect(s)
users = udb.cursor()
stories = sdb.cursor()

def addUser(username, password):
    q = "INSERT INTO users VALUES (\"%s\", %s, %s)" % (username, password, uid)
    udb.execute(q)
    global uid = uid + 1

def addStory(input,title):
    #timestamp = stuff
    q = "INSERT INTO " + title + " VALUES (\"%s\", %s, %s)" % (timestamp, sid, input)
    sdb.execute(q)
    global sid = sid + 1

#def showStuff
