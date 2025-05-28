import sqlite3

def print_table(cursor, table_name):
    print(f"\n--- {table_name.upper()} ---")
    try:
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("(No rows found)")
    except sqlite3.Error as e:
        print(f"Error reading {table_name}: {e}")

def main(db_path="lib/db/magazine.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for table in ["authors", "magazines", "articles"]:
        print_table(cursor, table)

    conn.close()

if __name__ == "__main__":
    main()