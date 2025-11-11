"""
Create a new staff account with known credentials
"""

from app import app, db, User
from werkzeug.security import generate_password_hash

def create_new_staff():
    """Create a new staff account"""
    with app.app_context():
        # Delete existing user with staff ID 2000 if exists
        existing_user = User.query.filter_by(reg_no="2000").first()
        if existing_user:
            db.session.delete(existing_user)
            print("Deleted existing user with staff ID 2000")
        
        # Create new user
        staff_email = 'yashwanth@ramco.edu'
        staff_password = '123'
        staff_name = 'Yashwanth'
        staff_id = '2000'
        
        hashed_password = generate_password_hash(staff_password)
        
        new_staff = User(
            email=staff_email,
            password_hash=hashed_password,
            full_name=staff_name,
            reg_no=staff_id,
            role='admin'
        )
        
        db.session.add(new_staff)
        db.session.commit()
        
        print(f"New staff account created!")
        print(f"Staff ID: {staff_id}")
        print(f"Password: {staff_password}")
        print(f"Email: {staff_email}")
        
        # Verify the password works
        from werkzeug.security import check_password_hash
        verification = check_password_hash(new_staff.password_hash, staff_password)
        print(f"Password verification: {verification}")

if __name__ == '__main__':
    create_new_staff()
