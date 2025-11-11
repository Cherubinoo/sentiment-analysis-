"""
Debug password issues
"""

from werkzeug.security import generate_password_hash, check_password_hash

def debug_password():
    password = "123"
    
    print(f"Original password: '{password}'")
    print(f"Password type: {type(password)}")
    print(f"Password length: {len(password)}")
    print(f"Password bytes: {password.encode()}")
    
    # Generate hash
    hash_val = generate_password_hash(password)
    print(f"\nGenerated hash: {hash_val}")
    
    # Test verification with exact same password
    result1 = check_password_hash(hash_val, password)
    print(f"Verification with same password: {result1}")
    
    # Test with string literal
    result2 = check_password_hash(hash_val, "123")
    print(f"Verification with literal '123': {result2}")
    
    # Test with different variations
    variations = ["123", " 123", "123 ", "123\n", "123\r\n"]
    for var in variations:
        result = check_password_hash(hash_val, var)
        print(f"Verification with '{repr(var)}': {result}")

if __name__ == '__main__':
    debug_password()
