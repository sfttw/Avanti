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
	
def index(notes, html5):
	blacklist = ['irc', 'src', '.template', 'template']
	links = ''
	for i in notes: 
		if i not in blacklist:
			links += '''<li><a href="/posts/%s">%s</a><br /></li>''' % (i,i[:-5])
	html5 = html5 % links
	return html5

def notes(html5='', views=' '):
	path = '/var/www/blog/posts/'
	notes = os.listdir(path)
	note = ''

	
	if views in notes: 
		fullpath = path + views
		note = open(fullpath).read()
		html5 = html5 % note #populate html5 content
		return html5
		
	else: #index
		return index(notes, html5)

def html(params):
	html5  = init()
	
	try: 
		views = params['view'][0]
	except: views = ''
	return notes(html5, views)
