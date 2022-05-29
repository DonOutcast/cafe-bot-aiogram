import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect("cafe.db")
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute("")
    base.commit()