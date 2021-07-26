#!/bin/bash

echo "Please select 1 for the production image or 2 for development"
echo "============================================================="
read response

if [[ $response = 1 ]]
then
    docker build . -t todo-app:prod --target=production 
    echo "To lauch the container please use the following command:"
    echo "docker run -d -p 5000:5000 --env-file .env todo-app:prod"
elif [[ $response = 2 ]]
then
    git clone https://github.com/lawrencemark/DevOps-Course-Starter
    docker build . -t todo-app:dev --target=development
    echo "To lauch the container please use the following command:"
    echo "docker run -it -p 5000:5000 --env-file .env --mount "
    echo "type=bind,source=\"$(pwd)\DevOps-Course-Starter/www,target=/srv/www/todo-app"
    echo "todo-app:dev"
else
    echo "exiting - incorrect value"
fi
