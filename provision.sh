#!/bin/bash

directory='/home/vagrant/webapps'

#pull pyenv from github 
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

#environment function to set the correct python version and pull todo from github and configure poetry
function envfuct {
echo 'Setting default Python environment to 3.9.5'
	source ~/.profile
	sh -c '~/.pyenv/bin/pyenv global 3.9.5'
	mkdir $directory
	git clone https://github.com/lawrencemark/DevOps-Course-Starter $directory
	sh -c 'cd /home/vagrant/webapps && ~/.poetry/bin/poetry install'
	chmod +x /home/vagrant/webapps/todo_app/startapp.sh
return
}

#parse environment settings to Vagrant user profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init --path)"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.bashrc 

~/.pyenv/bin/pyenv install 3.9.5



#download Poertry package manager and append path values and set python version via envfunct

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
export PATH=$PATH:$HOME/.poetry/bin

envfuct




