## About Rosie

Rosie is a small custom CMS built on python + nginx + uwsgi. 


## Prerequisites and assumptions
You must have the following installed:

- nginx
- uwsgi

## Running

Your nginx.conf will look something like this:
```
	server { 
		server_name chords.guitar.ro;
		root /var/www/chords.guitar.ro/;
	...
		location = / {            
			include uwsgi_params;
			uwsgi_pass 127.0.0.1:9090;
        }
```

Launch uwsgi:
```
uwsgi --socket 127.0.0.1:9090 --wsgi-file /var/www/index.py --master --processes 4 --threads 2 --stats :9191 
--stats-http --pidfile /tmp/uwsgi.pid 
```
