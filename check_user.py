"""
Check user credentials and debug login issues
"""

from app import app, db, User
from werkzeug.security import check_password_hash

def check_user_credentials():
    """Check if user exists and verify password"""
    with app.app_context():
        staff_id = "2000"
        password = "123"
        
        # Find user by staff ID
        user = User.query.filter_by(reg_no=staff_id, role='admin').first()
        
        if user:
            print(f"User found:")
            print(f"  ID: {user.id}")
            print(f"  Email: {user.email}")
            print(f"  Full Name: {user.full_name}")
            print(f"  Staff ID (reg_no): {user.reg_no}")
            print(f"  Role: {user.role}")
            print(f"  Password Hash: {user.password_hash[:50]}...")
            
            # Try to verify password
            try:
                is_valid = check_password_hash(user.password_hash, password)
                print(f"  Password verification: {is_valid}")
            except Exception as e:
                print(f"  Password verification error: {e}")
                
                # Try manual verification for legacy hashes
                if user.password_hash.startswith('sha256$'):
                    import hashlib
                    expected_hash = 'sha256$' + hashlib.sha256(password.encode()).hexdigest()
                    is_valid_legacy = user.password_hash == expected_hash
                    print(f"  Legacy password verification: {is_valid_legacy}")
        else:
            print(f"No user found with staff ID: {staff_id} and role: admin")
            
            # Check if user exists with different role
            user_any_role = User.query.filter_by(reg_no=staff_id).first()
            if user_any_role:
                print(f"Found user with staff ID {staff_id} but role is: {user_any_role.role}")
            
            # List all admin users
            print("\nAll admin users:")
            admin_users = User.query.filter_by(role='admin').all()
            for admin in admin_users:
                print(f"  Staff ID: {admin.reg_no}, Email: {admin.email}, Name: {admin.full_name}")

if __name__ == '__main__':
    check_user_credentials()
