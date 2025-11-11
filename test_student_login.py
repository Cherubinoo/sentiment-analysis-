"""
Test student login with legacy password hash
"""

from app import app, db, User, safe_check_password_hash

def test_student_login():
    """Test student login functionality"""
    with app.app_context():
        # Get the first student
        student = User.query.filter_by(role='student').first()
        
        if student:
            print(f"Testing student: {student.full_name}")
            print(f"Reg No: {student.reg_no}")
            print(f"Password Hash: {student.password_hash}")
            
            # Since we don't know the original password, let's create a test
            # Let's assume the password might be the same as reg_no or something simple
            test_passwords = [
                student.reg_no,  # Registration number
                "123456",        # Common password
                "password",      # Common password
                "123",           # Simple password
                student.reg_no[-6:],  # Last 6 digits of reg no
            ]
            
            for test_pwd in test_passwords:
                try:
                    result = safe_check_password_hash(student.password_hash, test_pwd)
                    print(f"Password '{test_pwd}': {result}")
                    if result:
                        print(f"✅ Found working password: {test_pwd}")
                        break
                except Exception as e:
                    print(f"Error testing '{test_pwd}': {e}")
        else:
            print("No student accounts found")

if __name__ == '__main__':
    test_student_login()
