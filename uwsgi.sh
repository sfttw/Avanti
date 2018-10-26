#!/bin/bash

PID=""

function get_pid {
   PID=`cat /tmp/uwsgi.pid`
}


function stop {
   get_pid
   if [ -z $PID ]; then
	  echo "server is not running."
	  exit 1
   else
	  echo -n "Stopping server.."
	  sudo kill -9 $PID
	  echo "" > /tmp/uwsgi.pid
	  sleep 1
	  echo ".. Done."
   fi
}


function start {
   get_pid
   if [ -z $PID ]; then
	  echo  "Starting server.."
	  uwsgi --plugin python3 --socket 127.0.0.1:9292 --wsgi-file /var/www/avanti/avanti.py --master --processes 4 --threads 2 --stats :9191 --stats-http --pidfile /tmp/uwsgi.pid &
	  get_pid
	  echo "Done. PID=$PID"
   else
	  echo "server is already running, PID=$PID"
   fi
}

function restart {
   echo  "Restarting server.."
   get_pid
   if [ -z $PID ]; then
	  start
   else
	  stop
	  sleep 5
	  start
   fi
}


function status {
   get_pid
   if [ -z  $PID ]; then
	  echo "Server is not running."
	  exit 1
   else
	  echo "Server is running, PID=$PID"
   fi
}

case "$1" in
   start)
	  start
   ;;
   stop)
	  stop
   ;;
   restart)
	  restart
   ;;
   status)
	  status
   ;;
   *)
	  echo "Usage: $0 {start|stop|restart|status}"
esac
