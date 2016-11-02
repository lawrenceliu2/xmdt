import sqlite3

u = "userdata.db" #not sure if i have to do data/ first
s = "stories.db"

udb = sqlite3.connect(u)
sdb = sqlite3.connect(s)
users = udb.cursor()
stories = sdb.cursor()

def addUser(username, password, id):
    q = "INSERT INTO users VALUES (\"%s\", %s, %s)" % (username, password, id)
    udb.execute(q)

def addStory(id,input,title):
    #timestamp = stuff
    q = "INSERT INTO " + title + " VALUES (\"%s\", %s, %s)" % (timestamp, id, input)
    sdb.execute(q)

#def showStuff
