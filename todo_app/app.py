from flask import Flask, redirect, render_template, request, session, abort, url_for
from markupsafe import escape
import json, requests
from werkzeug import utils
from .utils.classfunct import *

app = Flask(__name__)

taskclassrunner = card_tasks

@app.route("/")
def index():
    taskclassrunner.get_cardsonlist(TODO_LISTID)
    return render_template('index.html',title='To Do List', myobjects=cardslist)

@app.route("/completed/<cardid>")
def completed(cardid):
    if (taskclassrunner.update_card(cardid, DONE_LISTID)) == "200":
        return redirect(url_for('index'))
    else:
        return 'Ouch - something went wrong'
    
@app.route('/addtask', methods = ['POST'])
def postRequest():
    if request.method == 'POST':
        itemAdded = request.form['addTo']
        taskdescription = request.form['description']
        taskclassrunner.addcard_todo(itemAdded,taskdescription)
        return redirect(url_for('index'))
    else:
        return "Something went wrong!"


if __name__ == "__main__":
    app.run()