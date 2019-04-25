import sqlite3
from sqlite3.dbapi2 import Cursor


def create():
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, '
                'isbn INTEGER)')
    conn.commit()
    conn.close()


def add(title, author, year, isbn):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM books WHERE title=? OR author = ? OR year = ? OR isbn = ?', (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def update(id, title, author, year, isbn):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author = ?, year = ?, isbn = ? WHERE id = ?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect('bookstore.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()


create()
# delete(4)
# add("The sun", "Alice", 1989, 73675553684)
# update(1, "Harry Potter", "Joanne Rowling", 1992, 643765736583)
print(view())
print(search(year='1992'))
