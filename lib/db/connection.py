import sqlite3

CONNECTION = sqlite3.connect('lib/db/magazine.db')

CONNECTION.execute("PRAGMA foreign_keys = ON;")