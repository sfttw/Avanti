#!/usr/bin/env python
''' Rosie by Radiacl Ed. (c) 2017 '''
from os import listdir
from cgi import parse_qs, escape

import os, sys, inspect
 # realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

 # use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
if cmd_subfolder not in sys.path:
	sys.path.insert(0, cmd_subfolder)

#modules
import modules.chordie as chordie
import modules.blog as blog
import modules.weather as weather
__version__ = '1.2'



def application(env, start_response):
	start_response('200 OK', [('Content-Type','text/html')])
	parameters = parse_qs(env.get('QUERY_STRING', ''))
	hostname = env.get('HTTP_HOST')

	if hostname == '77n.win' : return [bytes('what', 'utf-8')]
	if hostname == 'blog.sailingfasterthanthewind.com' : return [bytes(blog.html(parameters), 'utf-8')]
	if hostname == 'st.gabriel.st' : return [bytes(blog.html(parameters), 'utf-8')]
	if hostname == 'bookmarks.77n.win' : return [bytes(bookmarks.html(parameters), 'utf-8')]


	if hostname == 'chords.sailingfasterthanthewind.com':
		if 'key' in parameters:
			keyOf = escape(parameters['key'][0])
			return [bytes(chordie.html(keyOf), 'utf-8')]
		else:
			return [bytes(chordie.html(), 'utf-8')]

	if hostname == 'weather.77n.win':
		if parameters:
			return [bytes(weather.html(parameters), 'utf-8')]
		else:
			return [bytes(weather.html(), 'utf-8')]
