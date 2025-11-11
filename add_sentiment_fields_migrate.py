from app import app, db

with app.app_context():
    # Add new rating columns for sentiment analysis
    with db.engine.connect() as conn:
        conn.execute(db.text("ALTER TABLE review ADD COLUMN teaching INT NULL"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN course_content INT NULL"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN examination INT NULL"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN lab_support INT NULL"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN teaching_method INT NULL"))
        conn.execute(db.text("ALTER TABLE review ADD COLUMN library_support INT NULL"))
        conn.commit()

print("Migration completed: Added new rating columns to review table.")
