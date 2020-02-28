## About Avanti!

Avanti! is a small custom CMS built on python + nginx + uwsgi. 


## Prerequisites and assumptions
You must have the following installed:

- nginx
- uwsgi

## Running

Your nginx.conf will look something like this:
```
	server { 
		server_name example.com;
		root /var/www/example.com/;
	...
		location = / {            
			include uwsgi_params;
			uwsgi_pass 127.0.0.1:9090;
        }
```

Install uWSGI:
```
$ dnf install -y uwsgi uwsgi-plugin-python3
```

Launch uWSGI:
```
uwsgi --plugin python3 --socket 127.0.0.1:9292 --wsgi-file /path/to/avanti.py --master --processes 4 --threads 2 --stats :9191 --stats-http --pidfile /tmp/uwsgi.pid
```

Made by iw
