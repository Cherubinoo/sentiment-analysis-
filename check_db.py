"""
Quick database connection checker
Run this to verify your database is configured correctly
"""
import os
from app import app, db

def check_database():
    print("=" * 50)
    print("DATABASE CONNECTION CHECK")
    print("=" * 50)
    
    # Check environment variables
    db_uri = os.getenv('DATABASE_URI')
    if not db_uri:
        print("❌ DATABASE_URI not set in environment variables")
        print("   Set it in Render dashboard → Environment")
        return False
    
    print(f"✓ DATABASE_URI is set")
    print(f"  Type: {'PostgreSQL' if 'postgresql' in db_uri else 'MySQL' if 'mysql' in db_uri else 'Unknown'}")
    
    # Try to connect
    try:
        with app.app_context():
            # Try a simple query
            db.engine.connect()
            print("✓ Database connection successful!")
            
            # Check if tables exist
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            if tables:
                print(f"✓ Found {len(tables)} tables: {', '.join(tables)}")
            else:
                print("⚠ No tables found - run 'python init_db.py' to create them")
            
            return True
            
    except Exception as e:
        print(f"❌ Database connection failed!")
        print(f"   Error: {str(e)}")
        print("\nPossible fixes:")
        print("1. Check DATABASE_URI format is correct")
        print("2. Verify database is running")
        print("3. Check firewall/network settings")
        return False

if __name__ == '__main__':
    success = check_database()
    print("=" * 50)
    if success:
        print("✓ Everything looks good!")
    else:
        print("❌ Please fix the issues above")
    print("=" * 50)
