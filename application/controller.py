from flask import Flask, render_template, request, redirect, session, url_for
from application import app,model
import os,string,sqlite3
from random import randint,choice

@app.route('/')
def index():
    return render_template('index.html', imag=model.posts(), ses=model.isNoneType(session.get('notendanafn')))


@app.route('/<more>')
def more(more):
    with sqlite3.connect("application/baseData.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    if len(posts) > 0:
        for x in posts:
            if x[5] == more:
                post = x
                break
    else:
        post = ""
    return render_template('more.html', post=post)

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def done():
    model.download('static/view/')
    with sqlite3.connect("application/baseData.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM posts")
    print(cursor.fetchall())
    return render_template("complete.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        form = request.form.to_dict()
        model.checkUser(form['username'], form['password'])
        return redirect('/')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form = request.form.to_dict()
        model.signUser(form['username'], form['password'])
        redirect('/')
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')