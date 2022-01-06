from flask.wrappers import Request
from flask import Flask, render_template, redirect, url_for, request
import backend


app = Flask(__name__)

@app.route("/",methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        taskName = request.form['tname']
        taskDesc = request.form['tdesc']
        taskStatus = request.form['tstatus']
        
        backend.mongodb_addcollection(taskName,taskDesc,taskStatus)
        return redirect(url_for('index'))

    else:
        backend.mongodb_getcollections()
        return render_template ('index.html', results=backend.itemList)


@app.route("/update/<itemNumber>",methods = ['POST', 'GET'])
def update(itemNumber):
    status = request.form['status']
    if request.method == 'POST':
        if status == 'delete':
            backend.mongodb_delcollection(itemNumber)
            return redirect(url_for('index'))
        else:
            backend.mongodb_updatecollection(itemNumber,status)
            return redirect(url_for('index'))

     