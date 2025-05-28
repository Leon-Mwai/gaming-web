from lib.db.connection import get_connection
import os

def run_schema():
    conn = get_connection()
    cursor = conn.cursor()
    schema_path = os.path.join(os.path.dirname(__file__), "../lib/db/schema.sql")

    with open(schema_path, "r") as file:
        cursor.executescript(file.read())

    conn.commit()
    conn.close()
    print("Database schema created.")

if __name__ == "__main__":
    run_schema()

  
    from lib.db.seed import seed_data
    seed_data()
