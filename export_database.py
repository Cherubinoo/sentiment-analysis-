"""
Export local database to SQL file
"""
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Local database connection
LOCAL_DB = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Your local MySQL password
    'database': 'sentiment_db'
}

def export_database():
    """Export all data from local database"""
    try:
        conn = pymysql.connect(**LOCAL_DB)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        sql_dump = []
        sql_dump.append("-- Database Export\n")
        sql_dump.append("SET FOREIGN_KEY_CHECKS=0;\n\n")
        
        for (table_name,) in tables:
            print(f"Exporting table: {table_name}")
            
            # Get table structure
            cursor.execute(f"SHOW CREATE TABLE `{table_name}`")
            create_table = cursor.fetchone()[1]
            sql_dump.append(f"-- Table: {table_name}\n")
            sql_dump.append(f"DROP TABLE IF EXISTS `{table_name}`;\n")
            sql_dump.append(f"{create_table};\n\n")
            
            # Get table data
            cursor.execute(f"SELECT * FROM `{table_name}`")
            rows = cursor.fetchall()
            
            if rows:
                # Get column names
                cursor.execute(f"DESCRIBE `{table_name}`")
                columns = [col[0] for col in cursor.fetchall()]
                
                sql_dump.append(f"-- Data for table: {table_name}\n")
                for row in rows:
                    values = []
                    for val in row:
                        if val is None:
                            values.append('NULL')
                        elif isinstance(val, str):
                            # Escape single quotes
                            escaped = val.replace("'", "''")
                            values.append(f"'{escaped}'")
                        elif isinstance(val, (int, float)):
                            values.append(str(val))
                        else:
                            values.append(f"'{str(val)}'")
                    
                    cols = ', '.join([f"`{col}`" for col in columns])
                    vals = ', '.join(values)
                    sql_dump.append(f"INSERT INTO `{table_name}` ({cols}) VALUES ({vals});\n")
                
                sql_dump.append("\n")
        
        sql_dump.append("SET FOREIGN_KEY_CHECKS=1;\n")
        
        # Write to file
        with open('sentiment_db_export.sql', 'w', encoding='utf-8') as f:
            f.writelines(sql_dump)
        
        print("\n✅ Export successful!")
        print("📁 File saved: sentiment_db_export.sql")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure:")
        print("1. MySQL is running")
        print("2. Database 'sentiment_db' exists")
        print("3. Update LOCAL_DB password if needed")

if __name__ == '__main__':
    export_database()
