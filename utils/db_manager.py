import sqlite3

#need to retrive previous id instead

def userAuth(username, password):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()
     
     if not nameAvail(username):
          q = "SELECT * FROM users WHERE username = %s;" % (username)
          users.execute(q)
          info = users.fetchall()
          if (info[0][1] == password):
               return True
     return False

def nameAvail(username):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()

     q = "SELECT * FROM users WHERE username = \"%s\";" % (username)
     users.execute(q)
     info = users.fetchall()
     if (len(info) > 0): return False
     else: return True

def addUser(username, password):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()
     
     if nameAvail(username):
          q = "SELECT userid FROM users WHERE userid=(SELECT MAX(userid) FROM users);"
          users.execute(q)
          x = users.fetchall()
          q = "INSERT INTO users VALUES(\"%s\", \"%s\", %s)" % (username, password, x[0][0] + 1)
          users.execute(q)
          return 1;
     else:
          return 0;
    
def addStory(title, content, userid):
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()
     
     q = "INSERT INTO " + title + " VALUES (\"%s\", %s, %s)" % (title, content, userid)
     stories.execute(q)

def getStories():
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()

     q = "SELECT name FROM sqlite_master WHERE type = 'table';"
     stories.execute(q)
     x = stories.fetchall()
     return x
     

