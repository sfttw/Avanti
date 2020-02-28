#!/usr/bin/env python3
import pickle
dblocation = '/var/www/bookmarks/bookmarks.db'
db = False

def load():
	global db
	try:
		with open(dblocation, 'rb') as f:
			db = pickle.load(f)
	except:
		print('error loading bookmarks.db')
	return db

def save():
	with open(dblocation, 'wb') as f:
		pickle.dump(db, f)
