#/usr/bin/env python
import os
import hashlib

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
		
def index(notes, html5):
	blacklist = ['irc', 'src', '.template', 'template', 'links.py']
	links = ''
	for i in getfiles('/var/www/blog/posts'): 
		if i not in blacklist:
			links += '''<li><a href="/posts/%s">%s</a><br /></li>''' % (i,i[:-5])
	html5 = html5 % links
	return html5

def notes(html5='', view=' '):
	path = '/var/www/blog/posts/'
	notes = os.listdir(path)
	note = ''

	
	if view in notes:  # make sure nobody tries to do ?view=/etc/passwd. 
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
		return index(filtered_notes_list, html5)

def html(params):
	html5  = init()
	
	try: 
		view = params['view'][0]
	except: view = ''
	return notes(html5, view)
