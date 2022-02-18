## About Avanti!

Avanti! is a small custom CMS built on python + nginx + uwsgi. 


## Prerequisites and assumptions
You must have the following installed:

- nginx
- uwsgi

## Running

This tutorial assumes you're running OpenSUSE. 

Clone Avanti! to `/var/www` or your systems equivalent 
```
$ git clone https://github.com/sfttw/avanti.git
```

Install uWSGI:
```
$ zypper in -y uwsgi uwsgi-python3
```

Setup `avanti.service` - be sure to edit it first.
```
$ cp avanti.service /etc/systemd/system
```

Enable Avanti! and uWSGI to start at boot:
```
$ systemctl enable avanti
$ systemctl start avanti
$ systemctl enable uwsgi
$ systemctl start uwsgi
```


Edit your `nginx.conf`:
```
	server { 
		server_name example.com;
		root /var/www/example.com/;
	...
		location = / {            
			include uwsgi_params;
			uwsgi_pass 127.0.0.1:9292;
		}
```
