"""
Import from sentiment_db.sql file to Railway
"""
import pymysql
import re

# Railway database connection
RAILWAY_DB = {
    'host': 'shinkansen.proxy.rlwy.net',
    'user': 'root',
    'password': 'ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV',
    'database': 'railway',
    'port': 43189
}

def import_from_sql_file(sql_file='sentiment_db.sql'):
    """Import SQL file to Railway database"""
    try:
        print(f"Reading SQL file: {sql_file}")
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        print("Connecting to Railway database...")
        conn = pymysql.connect(**RAILWAY_DB)
        cursor = conn.cursor()
        
        # Disable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute("SET sql_mode = ''")
        
        # Split by semicolon and execute each statement
        statements = sql_content.split(';\n')
        
        total = len(statements)
        insert_count = 0
        error_count = 0
        
        print(f"\nProcessing {total} statements...")
        
        for i, statement in enumerate(statements, 1):
            statement = statement.strip()
            
            # Skip empty statements and comments
            if not statement or statement.startswith('--') or statement.startswith('/*'):
                continue
            
            try:
                cursor.execute(statement)
                
                # Count INSERT statements
                if statement.upper().startswith('INSERT'):
                    insert_count += 1
                    if insert_count % 100 == 0:
                        print(f"  Inserted {insert_count} rows...")
                        
            except Exception as e:
                error_str = str(e)
                # Only show non-duplicate errors
                if 'already exists' not in error_str.lower() and 'duplicate' not in error_str.lower():
                    error_count += 1
                    if error_count <= 5:  # Show first 5 errors
                        print(f"  Warning: {e}")
        
        conn.commit()
        
        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        conn.commit()
        
        print(f"\n✅ Import complete!")
        print(f"   Total INSERT statements: {insert_count}")
        
        # Show table counts
        print("\n📊 Final table counts:")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        for (table,) in tables:
            cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
            count = cursor.fetchone()[0]
            print(f"   {table}: {count} rows")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    import_from_sql_file('sentiment_db.sql')
