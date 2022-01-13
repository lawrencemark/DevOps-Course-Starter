from flask.wrappers import Request
from flask import Flask, render_template, redirect, url_for, request, jsonify

import backend
from flask_dance.contrib.github import github
from flask_login import logout_user, login_required

app = Flask(__name__)

from models import db, login_manager
from oauth import github_blueprint

app.secret_key = 'notsosecretkey'
app.register_blueprint(github_blueprint, url_prefix="/login")

db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/",methods = ['POST', 'GET'])
def index():
    if not github.authorized:
        return redirect(url_for("github.login"))
    
    elif request.method == 'POST':
        resp = github.get("/user")
        assert resp.ok
    
        taskName = request.form['tname']
        taskDesc = request.form['tdesc']
        taskStatus = request.form['tstatus']
            
        backend.mongodb_addcollection(taskName,taskDesc,taskStatus)
        githubuser = login()
        return redirect(url_for('index'))

    else:
        backend.mongodb_getcollections()
        return render_template ('index.html', results=backend.itemList, githubuser=login())
    

@app.route("/update/<itemNumber>",methods = ['POST', 'GET'])
def update(itemNumber):
    if not github.authorized:
        return redirect(url_for("github.login"))
    else:
        status = request.form['status']
        if request.method == 'POST':
            if status == 'delete':
                backend.mongodb_delcollection(itemNumber)
                return redirect(url_for('index'))
            else:
                backend.mongodb_updatecollection(itemNumber,status)
                return redirect(url_for('index'))

@app.route("/github")
def login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    res = github.get("/user")
    username = res.json()["login"]
    return username

@app.route("/logoutuser")
def logout():
    logout_user()
    return "<P1>Please close your browser to clear GitHub Cache</P1>"
    