import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.seed import seed_db 
db_path = 'lib/db/magazine.db'


connection = sqlite3.connect('lib/db/magazine.db')

connection.execute("PRAGMA foreign_keys = ON;")

cursor = connection.cursor()

with open("lib/db/schema.sql") as schema_file:
    schema_sql = schema_file.read()
    cursor.executescript(schema_sql)
    print("schema.sql has been successfully executed.")

seed_db(db_path) 


connection.commit()
connection.close()
print("Magazine.db has been setup successfully.")