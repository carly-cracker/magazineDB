
import sqlite3

connection = sqlite3.connect('lib/db/magazine.db')

connection.execute("PRAGMA foreign_keys = ON;")

cursor = connection.cursor()

with open("lib/db/schema.sql") as schema_file:
    schema_sql = schema_file.read()
    cursor.executescript(schema_sql)
    print("schema.sql has been successfully executed.")

with open("lib/db/seed.sql") as seed_file:
    seed_sql = seed_file.read()
    cursor.executescript(seed_sql)
    print("seed.sql has been executed succsessfully.")

connection.commit()
connection.close()
print("Magazine.db has been setup successfully.")