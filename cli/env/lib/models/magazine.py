from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("""
                UPDATE magazines SET name = ?, category = ? WHERE id = ?
            """, (self.name, self.category, self.id))
        else:
            cursor.execute("""
                INSERT INTO magazines (name, category) VALUES (?, ?)
            """, (self.name, self.category))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(**row) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(**row) if row else None

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title FROM articles WHERE magazine_id = ?
        """, (self.id,))
        results = cursor.fetchall()
        conn.close()
        return [row["title"] for row in results]

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.name FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return rows  # list of dicts with 'name'

    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.name, COUNT(ar.id) as article_count FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
            GROUP BY a.id
            HAVING article_count > 2
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def __repr__(self):
        return f"<Magazine #{self.id} - {self.name}>"
