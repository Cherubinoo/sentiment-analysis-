"""
Import SQL dump to Railway database
"""
import pymysql
import os

# Railway database connection
RAILWAY_DB = {
    'host': 'shinkansen.proxy.rlwy.net',
    'user': 'root',
    'password': 'ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV',
    'database': 'railway',
    'port': 43189
}

def import_database(sql_file='sentiment_db_export.sql'):
    """Import SQL dump to Railway database"""
    try:
        if not os.path.exists(sql_file):
            print(f"❌ File not found: {sql_file}")
            print("Run export_database.py first!")
            return
        
        print("Connecting to Railway database...")
        conn = pymysql.connect(**RAILWAY_DB)
        cursor = conn.cursor()
        
        print(f"Reading SQL file: {sql_file}")
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Split by semicolon and execute each statement
        statements = sql_content.split(';\n')
        
        total = len(statements)
        for i, statement in enumerate(statements, 1):
            statement = statement.strip()
            if statement and not statement.startswith('--'):
                try:
                    cursor.execute(statement)
                    if i % 10 == 0:
                        print(f"Progress: {i}/{total} statements...")
                except Exception as e:
                    # Skip errors for statements that might already exist
                    if 'already exists' not in str(e).lower():
                        print(f"Warning: {e}")
        
        conn.commit()
        print("\n✅ Import successful!")
        print("🎉 Your database is now on Railway!")
        
        # Show table counts
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        print(f"\n📊 Tables imported: {len(tables)}")
        for (table,) in tables:
            cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
            count = cursor.fetchone()[0]
            print(f"  - {table}: {count} rows")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure:")
        print("1. Railway database is running")
        print("2. Connection details are correct")
        print("3. SQL file exists")

if __name__ == '__main__':
    import_database()
