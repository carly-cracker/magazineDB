import sqlite3

def seed_db(db_path="lib/db/database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    
    cursor.execute("DELETE FROM articles;")
    cursor.execute("DELETE FROM authors;")
    cursor.execute("DELETE FROM magazines;")

   
    cursor.executemany(
        "INSERT INTO authors (name, email, location, category) VALUES (?, ?, ?, ?);",
        [
            ("korir", "korir123@gmail.com", "Nairobi", "Tech"),
            ("kipkoech", "kip223@gmail.com", "Nakuru", "Health"),
            ("Carlos", "carl226@gmail.com", "Bomet", "politics"),
        ]
    )

    cursor.executemany(
        "INSERT INTO magazines (name, category) VALUES (?, ?);",
        [
            ('Technopolis', 'Tech'),
            ('Fiction Today', 'Fiction'),
            ('The Nation', 'Politics'),
        ]
    )

    cursor.executemany(
        "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?);",
        [
            ('AI Trends in 2025', 'Exploring the future of AI technology...', 1, 1),
            ('Benefits of Yoga', 'How yoga improves your health and well-being...', 2, 2),
            ('New Finance Bill', 'Kenyans angered by the court ruling of finance bill...', 3, 3),
            ('Deputy president impeached', 'Deputy Gachagua has been impeached following a court ruling...', 3, 3),
            ('Digital Detox', 'Tech-free weekends', 1, 2),
            ('AI Trends in 2025', 'Developers worry about AI taking over...', 1, 1),
        ]
    )

    conn.commit()
    conn.close()
    print("Database seeded successfully from seed.py.")