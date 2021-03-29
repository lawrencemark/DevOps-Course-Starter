from flask import Flask, render_template, request, url_for, redirect
from todo_app.data.session_items import *
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods = ['POST'])
def postRequest():
    if request.method == 'POST':
        itemAdded = request.form['addTo']
        add_item(itemAdded)
        return redirect(url_for('index'))
    else:
        return "Something went wrong!"

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', lstToDo = get_items()) 


if __name__ == '__main__':
    app.run()