#/usr/bin/env python
import os
import hashlib
from datetime import datetime

__all__ = ['html']

def init():
	html5 = open('/var/www/blog/src/template.html').read()
	indexhash = open('/var/www/blog/src/.template-hash').read()
	xx = hashlib.md5(open('/var/www/blog/src/template.html', 'rb').read()).hexdigest() #whaaat???
	
	if indexhash != xx:
		html5  = open('/var/www/blog/src/template.html').read()
	else:
		pass
	return html5

def getfiles(dirpath):
	#sort <posts directory> by date
	a = [s for s in os.listdir(dirpath)
		 if os.path.isfile(os.path.join(dirpath, s))]
	a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
	a.reverse()
	
	return a
	
def getdate(filepath):
	created= os.stat(filepath).st_ctime
	filedate = f"{datetime.fromtimestamp(created):%m-%d-%Y}"
	
	return filedate
	
def index(notes, html5, view):
	blacklist = ['irc', 'src', '.template', 'template', 'links.py', 'About.html']
	links = ''
	archivespath = '/var/www/blog/archives/'
	postspath = '/var/www/blog/posts/'
	if view == 'archives':
		for i in getfiles(archivespath): 
			filedate = getdate(archivespath+i)
			if i not in blacklist:
				links += '''<li><a href="/archives/%s">%s</a> - <span class="postdate">%s</span><br /></li>''' % (i,i[:-5], filedate)
	else:
		for i in getfiles(postspath):
			filedate = getdate(postspath+i)	
			if i not in blacklist:
				links += '''<li><a href="/posts/%s">%s</a> - <span class="postdate">%s</span><br /></li>''' % (i,i[:-5], filedate)
	html5 = html5 % links
	return html5

def notes(html5='', view=' '):
	path = '/var/www/blog/posts/'
	archivespath = '/var/www/blog/archives/'
	notes = os.listdir(path)
	archives = os.listdir('/var/www/blog/archives')
	fullpath = ''
	note = ''

	
	if view in notes or view in archives:  # make sure nobody tries to do ?view=/etc/passwd. 
		if view in archives:
			fullpath = archivespath + view
		else:
			fullpath = path + view # e,g, '/var/www/blog/posts/some file.html'
		note = open(fullpath).read()
		html5 = html5 % note #display posts contents
		return html5
		
	else: # list all posts
		blacklist = ['About.html', 'links.py']
		filtered_notes_list = []
		for i in notes:
			if i not in blacklist:
				filtered_notes_list.append(i)
		return index(filtered_notes_list, html5, view)

def html(params):
	html5  = init()
	
	try: 
		view = params['view'][0]
	except: view = ''
	return notes(html5, view)
