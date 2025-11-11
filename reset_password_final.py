"""
Final password reset with verification
"""

from app import app, db, User
from werkzeug.security import generate_password_hash, check_password_hash

def reset_and_verify():
    """Reset password and verify it works"""
    with app.app_context():
        staff_id = "2000"
        password = "123"
        
        # Find user
        user = User.query.filter_by(reg_no=staff_id, role='admin').first()
        
        if user:
            print(f"Found user: {user.full_name}")
            
            # Generate and set new password
            new_hash = generate_password_hash(password)
            print(f"New hash generated: {new_hash[:50]}...")
            
            user.password_hash = new_hash
            db.session.commit()
            
            # Verify immediately
            verification = check_password_hash(user.password_hash, password)
            print(f"Immediate verification: {verification}")
            
            # Fetch user again from database to double-check
            user_check = User.query.filter_by(reg_no=staff_id, role='admin').first()
            verification2 = check_password_hash(user_check.password_hash, password)
            print(f"Database verification: {verification2}")
            
            if verification2:
                print("✅ Password reset successful! You can now login.")
            else:
                print("❌ Password reset failed!")
                
        else:
            print("User not found!")

if __name__ == '__main__':
    reset_and_verify()
