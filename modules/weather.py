#!/usr/bin/env python
# -*- coding: utf-8 -*-




def buildlist(count):
	x = 0
	ul = ''''''
	while x < count:
		ul += "<li class='ui-state-default' id='weather%s'></li>" % x
		x += 1

	return ul

def buildjavascript(): 
	cities = open('/var/www/weather/cities.txt').readlines()
	cities = [x.strip() for x in cities]
	count = 0
	javascript = ''' '''
	preset = '''

   $.simpleWeather({
		zipcode: '',
		woeid: '',
		location: '%s',
		unit: 'f',
		success: function (weather) {

			html = '<h2>' + weather.temp + '&deg;' + weather.units.temp + ' <span class="low">(' + weather.low + ')</span></h2>';


			html += '<a href="https://www.google.com/maps/place/' + weather.city + ', ' + weather.region + '">' + '<img alt="'+ weather.currently + '" src="' + weather.image + '"> </a>';

			html += '<a href="https://www.google.com/maps/place/' + weather.city + ', ' + weather.region + '">%s</a>';

			html += '<br /><span class="winds"><b>' + weather.wind.direction + '</b> <font color="#999">Winds @</font><b>' + weather.wind.speed + weather.units.speed + '</b> <font color="skyblue">Chill</font>: ' + weather.wind.chill + '</span>';
			html += '<br /><b>Humidity: </b>' + weather.humidity + ' <b>Pressure: </b>' + weather.pressure + '<br /> <b>Sunrise: </b>' + weather.sunrise + ' <b>Sunset: </b>' + weather.sunset + '<br><b>Visibility</b>: ' + weather.visibility; 

			$('#weather%s').html(html);
			
		},
		error: function (error) {
			$('#weather%s').html('<p>' + error + '</p>');
		}
	});

	 '''

	for city in cities:
		javascript += preset % (city, city, str(count), str(count))
		count += 1


	buildlist(count)    
	return (javascript, buildlist(count)) 



def html():
	count = 0
	html5 = """



 <!DOCTYPE html>
 <html >
   <head>
	 <meta charset="UTF-8"> 
	 <title>Weather Reports</title>
	 <script src="//code.jquery.com/jquery-1.10.2.js"></script>
	  <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
	   <link href='http://fonts.googleapis.com/css?family=Open+Sans:400,300' rel='stylesheet' type='text/css'>
	 <script src='/src/jquery.simpleWeather.min.js'></script>
<style>
	* { margin: 0; padding: 0; }
	body { background-color: #fff; }
	 #sortable { list-style: none; width: 90%%;  height: 100%%; }
	li { display: block; float: left; margin: 1em;   width: 15%%;} 
	img { margin: 0 auto; }
	a:link, a, a:visited { color: blue; text-decoration: none; font-size: 1.4em;}
	.ui-state-default { background: #f5f5f5; margin: 2em; min-width: 100px; padding: 1em; border-radius: 5px; border: 1px solid #f5f5f5; }
	.low { color: #fff; }
	.wind { letter-spacing: .2em; }
	.humidity { color: skyblue; }
 </style>

	 <script>$(document).ready(function () { %s });</script>

	<body>
		<center>
	<ul id="sortable">
	  %s


	</ul>
	</center>
	</body>
 </html>



""" % buildjavascript()


	return html5

if __name__ == "__main__":
	print(html())


