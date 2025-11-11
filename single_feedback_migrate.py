from app import app, db

with app.app_context():
    # Alter to single feedback column
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE review DROP COLUMN teaching_feedback, DROP COLUMN course_content_feedback, DROP COLUMN examination_feedback, DROP COLUMN lab_support_feedback, DROP COLUMN teaching_method_feedback, DROP COLUMN library_support_feedback"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN feedback TEXT NOT NULL"))
        conn.commit()

print("Migration completed: Combined feedback into single TEXT field.")
