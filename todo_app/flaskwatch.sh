#!/bin/bash

#start web dev server  and place into the background and log output accordingly to few from host
#followed by the execution of the watchdog process to log test status and file systen changes, which are available 
#and viewable from the host platform

nohup flask run -h 0.0.0.0 > /srv/www/logs/flask.log  &  \
watchmedo shell-command \
    --patterns="*.py;*.txt" \
    --recursive \
    --command='pytest /srv/www/tests/test_pytest.py' \
    > /srv/www/logs/watchmedo.log