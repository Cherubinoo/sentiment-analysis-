from app import app, db

with app.app_context():
    # Add new rating columns to review table
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE review ADD COLUMN teaching_rating INT NOT NULL DEFAULT 1"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN course_content_rating INT NOT NULL DEFAULT 1"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN examination_rating INT NOT NULL DEFAULT 1"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN lab_support_rating INT NOT NULL DEFAULT 1"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN teaching_method_rating INT NOT NULL DEFAULT 1"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN library_support_rating INT NOT NULL DEFAULT 1"))
        conn.commit()

print("Migration completed: New rating columns added.")
