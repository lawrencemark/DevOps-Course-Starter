#set script variables
approotdir=/srv/www/DevOps-Course-Starter
appdir="/srv/www/DevOps-Course-Starter/todo_app"
appfile="applaunch.sh" 

#install packages outside of the dockerfile to reduce layers
apk add python3
apk add curl
apk add git

#create shortcut and install pip
ln /usr/bin/python3 /usr/bin/python
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

#download poetry package management
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

#create file structure environment; download my to-do application 
#from github and execute poetry, adding gunicorn in the process
mkdir -p /srv/www/
git -C /srv/www clone https://github.com/lawrencemark/DevOps-Course-Starter

cd "$approotdir" && ~/.poetry/bin/poetry install 
~/.poetry/bin/poetry add gunicorn

#create launch script for entrypoint
echo "cd /srv/www/DevOps-Course-Starter/todo_app" >>$appdir/$appfile
echo "source /srv/www/DevOps-Course-Starter/.venv/bin/activate" >> $appdir/$appfile
echo "gunicorn --bind 0.0.0.0:5000 app:app" >> $appdir/$appfile
chmod +x $appdir/$appfile
