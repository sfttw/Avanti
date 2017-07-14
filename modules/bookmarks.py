#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''Bookmarks module'''
import os
import pickle
__all__ = ['html']
dblocation = '/var/www/bookmarks/bookmarks.db'
global db
def loadDatabase():
	global db
	try:
		with open(dblocation, 'rb') as f:
			db = pickle.load(f)
	except:
		print('error loading bookmarks.db')
	return db
		
def saveDatabase():
	with open(dblocation, 'wb') as f:
		pickle.dump(db, f)

def saveLink(url, tags):
	tags = tags.split(',') #seperate by commas
	tags = [i.strip() for i in tags] #remove spaces
	db[url] = {'tags': tags}
	saveDatabase()

def database():
	db = loadDatabase()
	html5 = ''
	
	for k,v in db.items():
		html5 += "\n<span class='url'><a href='{}'>{}</a></span>\n".format(k, k)
		html5 += "<span class='tags'>"
		for tag in v['tags']:
			html5 += "<span class='tag'>{}</span> ".format(tag)
		html5 += "</span>\n"
	return html5
	
def html(params=None):
	html5 = ''
	try: 
		url = params['url'][0]
		tags = params['tags'][0]
		saveLink(url, tags)
		html5 ='<b><h1>{} saved. Thank You!</h1></b>'.format(url)
	except: 
		url = ''	
		html5 = '<b><h1>{}</h1></b>'.format(database())
	return html5