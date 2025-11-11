"""
Test password verification directly
"""

from werkzeug.security import generate_password_hash, check_password_hash

def test_password():
    password = "123"
    
    # Generate new hash
    hash1 = generate_password_hash(password)
    print(f"Generated hash: {hash1}")
    
    # Test verification
    result = check_password_hash(hash1, password)
    print(f"Verification result: {result}")
    
    # Test with wrong password
    result2 = check_password_hash(hash1, "wrong")
    print(f"Wrong password result: {result2}")

if __name__ == '__main__':
    test_password()
