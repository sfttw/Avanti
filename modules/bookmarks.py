#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''Bookmarks module'''
import os
import pickle
from datetime import datetime
import urllib.request

__all__ = ['html']
dblocation = '/var/www/bookmarks/bookmarks.db'
global db

def findTitle(url):
	webpage = urllib.request.urlopen(url).read()
	title = str(webpage).split('<title>')[1].split('</title>')[0]
	return title
	
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
	global db
	tags = tags.split(',') #seperate by commas
	tags = [i.strip() for i in tags] #remove spaces
	db[len(db)+1] = {'url':url, 'tags': tags, 'title':findTitle(url), 'date':str(datetime.now())}
	saveDatabase()

def database():
	db = loadDatabase()
	html5 = ''
	
	for k,v in db.items():
		html5 += "\n<span class='title'><a href='{}'>{}</a></span>".format(db[k]['url'], db[k]['title'])
		html5 += "<span class='url'><a href='{}'>{}</a></span>\n".format(db[k]['url'], db[k]['url'])
		html5 += "<span class='tags'>"
		for tag in db[k]['tags']:
			html5 += "<span class='tag'>{}</span> ".format(tag)
		html5 += "</span>\n"
	return html5


	
def html(params=None):
	html5 = ''
	url = False
	tags = False
	try: url = params['url'][0]
	except: pass
	try:
		tags = params['tags'][0]
	except:
		pass
		
	if url: 
		saveLink(url, tags)
		html5 ="<b>{}</b> saved. Thank You! You are being redirected...</b><script>window.location='/';</script> ".format(url)
	else: 
		url = ''	
		html5 = open('/var/www/bookmarks/template.html').read()
		html5 = html5.format(database())
		
	return html5	