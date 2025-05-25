from lib.db.connection import CONNECTION
cursor = CONNECTION.cursor()

with open("lib/schema.sql") as schema_file:
    cursor.executescript(schema_file.read())
    print("schema.sql has been successfully executed.")

with open("lib/db/seed.sql") as seed_file:
    cursor.executescript(seed_file.read())
    print("seed.sql has been executed succsessfully.")

CONNECTION.commit()
CONNECTION.close()
print("Magazine.db has been setup successfully.")