import sqlite3

with sqlite3.connect("baseData.db") as db:
    cursor=db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS posts(
postID INTEGER PRIMARY KEY,
title VARCHAR(20) NOT NULL,
imagePath VARCHAR(20) NOT NULL,
text VARCHAR(1000) NOT NULL,
user VARCHAR(30) NOT NULL,
link VARCHAR(30) NOT NULL);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
password VARCHAR(100) NOT NULL);
''')


cursor.execute("SELECT * FROM users")
print(cursor.fetchall())