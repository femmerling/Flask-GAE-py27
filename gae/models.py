# coding: UTF-8
from google.appengine.ext import db

# to use NDB datastore uncomment the line below
#from google.appengine.ext import ndb

class User(db.Model):
    name = db.StringProperty()

# for NDB models uncomment and follow the following model pattern
#class User(ndb.Model):
#    name = ndb.StringProperty()

