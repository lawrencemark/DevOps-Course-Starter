#set script variables
appdir="/srv/www/todo-app"
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

echo "echo poetry package manager application dependencies" >> /tmp/firstrun.sh 
echo "cd /srv/www/todo-app" >> /tmp/firstrun.sh
echo "~/.poetry/bin/poetry install" >> /tmp/firstrun.sh
