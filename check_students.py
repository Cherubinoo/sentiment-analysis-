"""
Check student accounts and their password hashes
"""

from app import app, db, User

def check_students():
    """Check all student accounts"""
    with app.app_context():
        # Get all student users
        students = User.query.filter_by(role='student').all()
        
        print(f"Found {len(students)} student accounts:")
        for student in students:
            print(f"  ID: {student.id}")
            print(f"  Email: {student.email}")
            print(f"  Name: {student.full_name}")
            print(f"  Reg No: {student.reg_no}")
            print(f"  Password Hash: {student.password_hash[:50]}...")
            print("  ---")

if __name__ == '__main__':
    check_students()
