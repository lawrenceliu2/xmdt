import sqlite3, re

#need to retrive previous id instead

def userAuth(username, password):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()
     
     if not nameAvail(username):
          q = "SELECT * FROM users WHERE username = \"%s\";" % (username)
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
          q = "SELECT MAX(userid) FROM users;"
          users.execute(q)
          x = users.fetchall()
          q = '''INSERT INTO users(username, pass, userid)
 VALUES("%s", "%s", %s)''' % (username, password, x[0][0] + 1,)
          users.execute(q)
          udb.commit()
          return 1
     else:
          return 0
    
def addStory(title, timestamp, content, userid):
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()
     
     q = "CREATE TABLE " + title + " (timestamp text, content text, userid integer);"
     stories.execute(q)
     addToStory(title, timestamp, content, userid)
     sdb.commit()
     
def addToStory(title, timestamp, content, userid):
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()
     
     q = "INSERT INTO " + title + " VALUES (\"%s\", \"%s\", %s)" % (timestamp, content, userid)
     stories.execute(q)
     sdb.commit()
     
def fullStory(title):
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()
     
     q = "SELECT content FROM " + title + ";"
     stories.execute(q)
     contents = stories.fetchall()
#     story = ""
#     for part in contents:
#          story = story + part
     return contents

#def lastContent(title):
#     sdb = sqlite3.connect("data/stories.db")
#     stories = sdb.cursor()
#     
#     q = "SELECT LAST(content) FROM " + title + ";"
#     stories.execute(q)
#     return stories.fetchall()
     
def getStories():
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()

     q = "SELECT name FROM sqlite_master WHERE type = 'table';"
     stories.execute(q)
     x = stories.fetchall()
     stor = dict()
     for y in x:
          b = y[0]
#          print b
          stor[sanitize(b)] = {b : fullStory(b)}
     return stor

def getID(username):
     udb = sqlite3.connect("data/userdata.db")
     users = udb.cursor()
     
     q = "SELECT userid FROM users WHERE username=\"%s\";" % (username)
     users.execute(q)
     x = users.fetchall()
     return x[0][0]

def hasContributed(title, username):
     x = getID(username)
     sdb = sqlite3.connect("data/stories.db")
     stories = sdb.cursor()

     q = "SELECT * FROM " + title + " WHERE userid=%s;" % (x)
     stories.execute(q)
     info = stories.fetchall()
     if (len(info) > 0): return True
     else: return False

def sanitize(title):
     rx = re.compile('\W+')
     res = rx.sub(' ', title).strip()
     res = res.replace(' ', '-').lower()
     return res
