#!/usr/bin/env python
from os import listdir
#from cgi import parse_qs, escape
chordkeys = {
	'A': ['A', 'Bm', 'Csharpm', 'D', 'E', 'Fsharpm', 'Gsharpdim'],
	'Ab': ['Ab', 'Bbm', 'Cm', 'Db', 'Eb', 'Fm', 'Gdim'],
	'B': ['B', 'Csharpm', 'Dsharpm', 'E', 'Fsharp', 'Gsharpm', 'Asharpdim'],
	'Bb': ['Bb', 'Cm', 'Dm', 'Eb', 'F', 'Gm', 'Adim'],
	'C': ['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim'],
	'D' : ['D', 'Em', 'Fsharpm', 'G', 'A', 'Bm', 'Csharpdim'],
	'Db' : ['Db', 'Ebm', 'Fm', 'Gb', 'Ab', 'Bbm', 'Cdim'],
	'E' : ['E', 'Fsharpm', 'Gsharpm', 'A', 'B', 'Csharpm', 'Dsharpdim'],
	'Eb' : ['Eb', 'Fm', 'Gm', 'Ab', 'Bb', 'Cm', 'Ddim'],
	'F' : ['F', 'Gm', 'Am', 'Bb', 'C', 'Dm', 'Edim'],
	'G' : ['G', 'Am', 'Bm', 'C', 'D', 'Em', 'Fsharpdim'],
	}



def builder(scale="A"):
	html = "<div id='%s' class='chords'><h1>%s</h1>\n" % (scale, scale)
	html = html.replace('sharp', '#')
	imglist = []
	for i in listdir('/var/www/chordie/img/'+scale):
		imglist.append(i)
	imglist.sort()
	for i in imglist:
		html += "<img src='/img/%s/%s' />\n" % (scale,i)
	html += "</div>\n\n"
	return html
	
def html(keyOf="C"):
	body = ' '
	for i in chordkeys[keyOf]:
		body += builder(i)
	html5 = ''' 
	<html>
	<body>
	
		  <button type="button" onclick="window.location = '/?key=Ab';" title="Chords in the Key of Ab/G#">Ab</button>		  
		  <button type="button" onclick="window.location = '/?key=A';" title="Chords in the Key of A">A</button>
		  <button type="button" onclick="window.location = '/?key=Bb';" title="Chords in the Key of A#/Bb">Bb</button>
		  <button type="button" onclick="window.location = '/?key=B';" title="Chords in the key of B">B</button>
		  <button type="button" onclick="window.location = '/?key=C';" title="Chords in the Key of C">C</button> 
		  <button type="button" onclick="window.location = '/?key=Db';" title="Chords in the Key of C#/Db">Db</button>		  
		  <button type="button" onclick="window.location = '/?key=D';" title="Chords in the Key of D">D</button>
		  <button type="button" onclick="window.location = '/?key=Eb';" title="Chords in the Key of Eb/D#">Eb</button>
		  <button type="button" onclick="window.location = '/?key=E';" title="Chords in the Key of E">E</button>
		  <button type="button" onclick="window.location = '/?key=F';" title="Chords in the Key of F">F</button>
		  <button type="button" onclick="window.location = '/?key=Fsharp';" title="Chords in the Key of F#">F#</button>
		  <button type="button" onclick="window.location = '/?key=G';" title="Chords in the Key of G">G</button>
		  
	%s
	</body>
	</html>
	''' % body
	return html5
		
