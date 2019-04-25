import psycopg2

def create():
    conn = psycopg2.connect("dbname ='db2' user ='postgres' password = 'postgres123' host  = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS employees(name TEXT, year INTEGER, phone TEXT)')
    conn.commit()
    conn.close()

def insert(name, year, phone):
    conn = psycopg2.connect("dbname ='db2' user ='postgres' password = 'postgres123' host  = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO employees VALUES (%s,%s,%s)",(name, year, phone))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname ='db2' user ='postgres' password = 'postgres123' host  = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(name):
    conn = psycopg2.connect("dbname ='db2' user ='postgres' password = 'postgres123' host  = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE name = %s", (name, ))
    conn.commit()
    conn.close()

def update(phone, name):
    conn = psycopg2.connect("dbname ='db2' user ='postgres' password = 'postgres123' host  = 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE employees SET phone=%s WHERE name = %s", (phone, name))
    conn.commit()
    conn.close()

#create()
#insert("Liudmyla", 1983, "+380979455231")
#delete("Liudmyla")
update("+380986144586", "Liudmyla")
print(view())
