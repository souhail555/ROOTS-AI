import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
print(cur.execute("select name from sqlite_master where type='table' and name='core_car'").fetchone())
print(cur.execute("select app, name from django_migrations where app='core' order by id").fetchall())
conn.close()
