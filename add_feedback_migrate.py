from app import app, db

with app.app_context():
    # Alter rating columns to TEXT
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE review DROP COLUMN rating"))
        conn.execute(db.text("ALTER TABLE review CHANGE COLUMN teaching_rating teaching_feedback TEXT NOT NULL"))
        conn.execute(db.text("ALTER TABLE review CHANGE COLUMN course_content_rating course_content_feedback TEXT NOT NULL"))
        conn.execute(db.text("ALTER TABLE review CHANGE COLUMN examination_rating examination_feedback TEXT NOT NULL"))
        conn.execute(db.text("ALTER TABLE review CHANGE COLUMN lab_support_rating lab_support_feedback TEXT NOT NULL"))
        conn.execute(db.text("ALTER TABLE review CHANGE COLUMN teaching_method_rating teaching_method_feedback TEXT NOT NULL"))
        conn.execute(db.text("ALTER TABLE review CHANGE COLUMN library_support_rating library_support_feedback TEXT NOT NULL"))
        conn.commit()

print("Migration completed: Rating columns changed to feedback TEXT fields.")
