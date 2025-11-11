"""
Migration script to fix password hashes from sha256 to pbkdf2:sha256
Run this once to update existing user passwords
"""

from app import app, db, User
from werkzeug.security import generate_password_hash

def fix_password_hashes():
    """Update all users with sha256 hashes to use the new default method"""
    with app.app_context():
        # Find all users with old sha256 hashes
        users = User.query.all()
        
        updated_count = 0
        for user in users:
            if user.password_hash and user.password_hash.startswith('sha256$'):
                print(f"Found user with old hash format: {user.email}")
                # For existing users, we'll set a default password that they need to change
                # Or you can prompt for each user's password
                
                # Option 1: Set default password (they'll need to change it)
                new_hash = generate_password_hash('temppassword123')
                user.password_hash = new_hash
                updated_count += 1
                print(f"Updated password hash for {user.email} - they need to use 'temppassword123' to login")
        
        if updated_count > 0:
            db.session.commit()
            print(f"\nUpdated {updated_count} user password hashes.")
            print("Users with updated passwords should change their passwords after logging in.")
        else:
            print("No users with old password hashes found.")

if __name__ == '__main__':
    fix_password_hashes()
