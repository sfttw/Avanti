#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''Bookmarks module'''
import os
import pickle
import datetime
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
	tags = tags.split(',') #seperate by commas
	tags = [i.strip() for i in tags] #remove spaces
	db[url] = {'tags': tags, 'title':findTitle(url), 'date':str(datetime.now())}
	saveDatabase()

def database():
	db = loadDatabase()
	html5 = ''
	
	for k,v in db.items():
		html5 += "\n<span class='title'><a href='{}'>{}</a></span>".format(k, v['title'])
		html5 += "<span class='url'><a href='{}'>{}</a></span>\n".format(k, k)
		html5 += "<span class='tags'>"
		for tag in v['tags']:
			html5 += "<span class='tag'>{}</span> ".format(tag)
		html5 += "</span>\n"
	return html5


	
def html(params=None):
	html5 = ''
	''''
	{}
	</body>'''.format(database())
	try: 
		url = params['url'][0]
		tags = params['tags'][0]
		saveLink(url, tags)
		html5 ="<b>{}</b> saved. Thank You! You are being redirected...</b><script>window.location='/';</script> ".format(url)
	except: 
		url = ''	
		html5 = open('/var/www/bookmarks/template.html').read()
		html5 = html5.format(database())
	return html5