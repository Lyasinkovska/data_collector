import sqlite3

def create():
    conn = sqlite3.connect('first_db.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS employees(name TEXT, year INTEGER, phone TEXT)')
    conn.commit()
    conn.close()

def insert(name, year, phone):
    conn = sqlite3.connect('first_db.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO employees VALUES (?,?,?)",(name, year, phone))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('first_db.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(name):
    conn = sqlite3.connect('first_db.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE name = ?", (name, ))
    conn.commit()
    conn.close()

def update(phone, name):
    conn = sqlite3.connect('first_db.db')
    cur = conn.cursor()
    cur.execute("UPDATE employees SET phone=? WHERE name = ?", (phone, name))
    conn.commit()
    conn.close()

#create()
insert("Liudmyla", 1991, "+380986144586")
#delete("Liudmyla")
update("+380979455231", "Yuriy")
print(view())
