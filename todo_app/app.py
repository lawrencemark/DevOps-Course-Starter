from flask import Flask, render_template, request
from todo_app.data.session_items import *
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        itemAdded = request.form['addTo']
        add_item(itemAdded)
        return render_template('index.html', lstToDo = get_items())
    else:
        return render_template('index.html', lstToDo = get_items()) 


if __name__ == '__main__':
    app.run()
