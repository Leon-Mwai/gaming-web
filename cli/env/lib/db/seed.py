from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

   
    cursor.executemany(
        "INSERT INTO authors (name) VALUES (?)",
        [("Leon",), ("Saitama",), ("Uzumaki",)]
    )

    cursor.executemany(
        "INSERT INTO magazines (name, category) VALUES (?, ?)",
        [("Tech Weekly", "Technology"), ("Manga Digest", "Entertainment"), ("AI Monthly", "Science")]
    )

    cursor.executemany(
        "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
        [
            ("The Rise of AI", 1, 3),
            ("Python vs JS", 1, 1),
            ("Shadow Realm Chronicles", 2, 2),
            ("Battle of The Gods", 3, 2),
            ("Ninja Code Tips", 3, 1)
        ]
    )

    conn.commit()
    conn.close()
    print("Seeded database successfully.")
