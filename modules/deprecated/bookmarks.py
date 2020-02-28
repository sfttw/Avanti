#!/usr/bin/env python3
# -*- coding: utf8 -*-
'''Bookmarks module'''
import os
import pickle
from datetime import datetime
import urllib.request

__all__ = ['html']
dblocation = '/var/www/bookmarks/bookmarks.db'
db = False
def findTitle(url):
	request = urllib.request.Request(url)
	request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0)')
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

def saveLink(url, tags, title):
	global db
	if not db: loadDatabase()
	tags = tags.split() # tags are seperated by a blank space
	tags = [i.strip() for i in tags] #remove spaces
	db[url] = {'url':url, 'tags': tags, 'title':title, 'date':str(datetime.now())}
	saveDatabase()

def database():
	db = loadDatabase()
	html5 = ''
	
	for k,v in db.items():
		prettytitle = db[k]['title']
		if len(db[k]['title']) > 70:
			prettytitle = db[k]['title'][:70]+'...'
		html5 += "\n<span class='title'><a href='{}'>{}</a></span>".format(db[k]['url'], prettytitle)
		prettyurl = db[k]['url']
		if len(db[k]['url']) > 15:
			prettyurl = db[k]['url'][:40]+'...'
		
		html5 += "<span class='url'><a href='{}'>{}</a></span>\n".format(db[k]['url'], prettyurl)
		html5 += "<span class='tags'>"
		for tag in db[k]['tags']:
			html5 += "<span class='tag'><a href='/?tags={}'>{}</a></span> ".format(tag, tag)
		html5 += "</span>\n"
	return html5


	
def html(params=None):
	html5 = ''
	url = False
	tags = False
	title=False
	global db
	try: url = params['url'][0]
	except: pass
	try:
		tags = params['tags'][0]
		title = params['title'][0]
	except:
		pass
	
	if tags and not url:
		db = loadDatabase()
		html5 = open('/var/www/bookmarks/template.html').read()
		html6 =''
		for k,v in db.items():
			if tags in db[k]['tags']:
				html6 += "\n<span class='title'><a href='{}'>{}</a></span>".format(db[k]['url'], db[k]['title'])
				html6 += "<span class='url'><a href='{}'>{}</a></span>\n".format(db[k]['url'], db[k]['url'])
				html6 += "<span class='tags'>"
				for tag in db[k]['tags']:
					html6 += "<span class='tag'><a href='/?tags={}'>{}</a></span> ".format(tag, tag)
				html6 += "</span>\n"	
		html5 = html5.format(html6)	
	elif url and tags: #addlink
		saveLink(url, tags, title)
		html5 ="<b>{}</b> saved. Thank You! You are being redirected...</b><script>window.location='/';</script> ".format(url)
	else: 
		url = ''	
		html5 = open('/var/www/bookmarks/template.html').read()
		html5 = html5.format(database())
		
	return html5	