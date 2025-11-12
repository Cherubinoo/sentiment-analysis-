# Migrate Local Database to Railway

## Quick Steps

### 1. Export Local Database

```bash
python export_database.py
```

This creates `sentiment_db_export.sql` with all your data.

**Note:** If you have a MySQL password, edit `export_database.py` and update:
```python
LOCAL_DB = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_PASSWORD_HERE',  # Add your password
    'database': 'sentiment_db'
}
```

### 2. Import to Railway

```bash
python import_to_railway.py
```

This uploads everything to your Railway database.

### 3. Done!

Your Railway database now has all your data!

---

## Alternative: Manual Export/Import

### Export using MySQL Workbench:
1. Open MySQL Workbench
2. Connect to local database
3. Server → Data Export
4. Select `sentiment_db`
5. Export to Self-Contained File
6. Save as `sentiment_db_export.sql`

### Import to Railway:
1. Use the `import_to_railway.py` script
2. Or use MySQL Workbench:
   - Connect to Railway (use connection details)
   - Server → Data Import
   - Import from Self-Contained File
   - Select `sentiment_db_export.sql`

---

## Alternative: Using Command Line

If you have MySQL command line tools:

### Export:
```bash
mysqldump -u root -p sentiment_db > sentiment_db_export.sql
```

### Import to Railway:
```bash
mysql -h shinkansen.proxy.rlwy.net -u root -pZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV --port 43189 railway < sentiment_db_export.sql
```

---

## What Gets Migrated

- ✅ All tables (users, reviews, subjects, etc.)
- ✅ All data (students, feedback, ratings)
- ✅ Table structure
- ✅ Relationships and constraints

---

## Troubleshooting

### "Can't connect to local database"
- Make sure MySQL is running
- Check username/password
- Verify database name is `sentiment_db`

### "Can't connect to Railway"
- Check Railway database is running
- Verify connection details are correct
- Check firewall/network

### "Table already exists"
- The script will skip existing tables
- Or drop tables first in Railway dashboard

---

## After Migration

Update your Vercel environment variables to use Railway:

```
DATABASE_URI = mysql+pymysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway
```

Then redeploy on Vercel!
