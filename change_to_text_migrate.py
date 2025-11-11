from app import app, db

with app.app_context():
    # Change rating columns to TEXT
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE review MODIFY COLUMN teaching TEXT NULL"))
        conn.execute(db.text("ALTER TABLE review MODIFY COLUMN course_content TEXT NULL"))
        conn.execute(db.text("ALTER TABLE review MODIFY COLUMN examination TEXT NULL"))
        conn.execute(db.text("ALTER TABLE review MODIFY COLUMN lab_support TEXT NULL"))
        conn.execute(db.text("ALTER TABLE review MODIFY COLUMN teaching_method TEXT NULL"))
        conn.execute(db.text("ALTER TABLE review MODIFY COLUMN library_support TEXT NULL"))
        conn.commit()

print("Migration completed: Changed rating columns to TEXT.")
