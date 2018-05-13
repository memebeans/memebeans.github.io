from random import randint
import os,string,sqlite3
from flask import *
from random import randint,choice

def isNoneType(variable):
    if variable is not None:
        return variable
    else:
        return 'You are not logged in.'

def posts():
    with sqlite3.connect("application/baseData.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM posts")
    listi=cursor.fetchall()
    listi=listi[::-1]
    return listi

def id_gen(size):
    chars = string.ascii_letters + string.digits
    thin = ''.join(choice(chars) for x in range(size))
    return thin

def download(path):
    target = os.path.join(APP_ROOT, path)

    if not os.path.isdir(target):
        os.mkdir(target)

    titill=request.form["title"]
    for file in request.files.getlist("file"):
        filename = file.filename
        file_extension = filename.split(".")[-1]
        filename = id_gen(10) + "." +file_extension
        link = filename.split(".")[0]
        destination = "/".join([target, filename])
        file.save(destination)
        with sqlite3.connect("application/baseData.db") as db:
            cursor = db.cursor()
        cursor.execute('''
        INSERT INTO posts(title,imagePath,text,user,link)
        VALUES(?,?,?,?,?)
        ''',(titill,filename,"texti",isNoneType(session.get('notendanafn')),link,))
        db.commit()

def checkUser(user, password):
    with sqlite3.connect("application/baseData.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    list = cursor.fetchall()
    for x in list:
        if x[1] == user:
            if x[2] == password:
                session['notendanafn'] = x[1]
            else:
                 return redirect('/login')

def signUser(user, password):
    with sqlite3.connect("application/baseData.db") as db:
        cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    list = cursor.fetchall()
    users = []
    for x in list:
        users.append(x[1])

    if user not in users:
        cursor.execute('''
                INSERT INTO users(username, password)
                VALUES(?,?)
                ''', (user, password,))
        db.commit()
    else:
        return redirect('/signup')


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
