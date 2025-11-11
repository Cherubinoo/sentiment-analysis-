"""
Create a new admin user with proper password hashing
"""

from app import app, db, User
from werkzeug.security import generate_password_hash

def create_admin_user():
    """Create a new admin user with proper password hashing"""
    with app.app_context():
        # Check if admin already exists
        existing_admin = User.query.filter_by(email='admin@ramco.edu').first()
        if existing_admin:
            print("Admin user already exists!")
            return
        
        # Create new admin user
        admin_email = 'admin@ramco.edu'
        admin_password = 'admin123'  # You can change this
        admin_name = 'System Administrator'
        admin_staff_id = 'ADMIN001'
        
        hashed_password = generate_password_hash(admin_password)
        
        new_admin = User(
            email=admin_email,
            password_hash=hashed_password,
            full_name=admin_name,
            reg_no=admin_staff_id,
            role='admin'
        )
        
        db.session.add(new_admin)
        db.session.commit()
        
        print(f"Admin user created successfully!")
        print(f"Email: {admin_email}")
        print(f"Staff ID: {admin_staff_id}")
        print(f"Password: {admin_password}")
        print("\nYou can now login using these credentials.")

if __name__ == '__main__':
    create_admin_user()
