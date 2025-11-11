"""
Fix password for specific user
"""

from app import app, db, User
from werkzeug.security import generate_password_hash

def fix_user_password():
    """Fix password for staff ID 2000"""
    with app.app_context():
        staff_id = "2000"
        new_password = "123"
        
        # Find user
        user = User.query.filter_by(reg_no=staff_id, role='admin').first()
        
        if user:
            print(f"Found user: {user.full_name} ({user.email})")
            
            # Generate new password hash
            new_hash = generate_password_hash(new_password)
            user.password_hash = new_hash
            
            db.session.commit()
            
            print(f"Password updated successfully!")
            print(f"Staff ID: {staff_id}")
            print(f"Password: {new_password}")
            print("You can now login with these credentials.")
        else:
            print(f"User with staff ID {staff_id} not found!")

if __name__ == '__main__':
    fix_user_password()
