# Fix Your Current Render Deployment

Your app is crashing because there's no database configured. Here's how to fix it:

## Option 1: Quick Fix (Use PostgreSQL - Free on Render)

### Step 1: Add PostgreSQL Database
1. In your Render dashboard, click "New +" → "PostgreSQL"
2. Name: `sentiment-db`
3. Database: `sentiment_db`
4. User: `sentiment_user`
5. Click "Create Database"
6. Wait for it to provision (~1 minute)

### Step 2: Connect Database to Your App
1. Go to your PostgreSQL database page
2. Copy the "Internal Database URL" (starts with `postgresql://`)
3. Go to your web service → "Environment" tab
4. Find or add `DATABASE_URI` variable
5. Paste the PostgreSQL URL (keep it as `postgresql://`, SQLAlchemy will handle it)
6. Click "Save Changes"
7. Your app will auto-redeploy

### Step 3: Initialize Database Tables
1. After deployment succeeds, go to web service → "Shell" tab
2. Run:
   ```bash
   python init_db.py
   ```
3. You should see: "Database tables created successfully!"

### Step 4: Test Your App
Visit your app URL - it should work now!

---

## Option 2: Use External MySQL (If you prefer MySQL)

### Using Railway MySQL:
1. Go to [railway.app](https://railway.app)
2. Create new project → "Provision MySQL"
3. Copy the connection string
4. Convert format:
   - From: `mysql://user:pass@host:port/db`
   - To: `mysql+pymysql://user:pass@host:port/db`
5. Add to Render environment variables as `DATABASE_URI`

### Using PlanetScale (Free MySQL):
1. Go to [planetscale.com](https://planetscale.com)
2. Create free database
3. Get connection string
4. Format: `mysql+pymysql://user:pass@host/db?ssl_ca=/etc/ssl/cert.pem`
5. Add to Render as `DATABASE_URI`

---

## Option 3: Start Fresh with render.yaml

If you want automatic database setup:

1. **Delete current service** (if you want to start clean)
2. **Push updated code** to GitHub (with the new render.yaml)
3. **Deploy again** - Render will auto-create database
4. **Initialize tables** using Shell: `python init_db.py`

---

## Troubleshooting

### "Connection refused" error
- Database not created yet
- Wrong DATABASE_URI format
- Database not linked to web service

### "No module named 'psycopg2'"
- Push updated requirements.txt with `psycopg2-binary`
- Redeploy

### "Table doesn't exist"
- Run `python init_db.py` in Shell
- Tables weren't created yet

### App keeps restarting
- Check Deploy Logs for actual error
- Verify DATABASE_URI is set correctly
- Make sure database is running

---

## Current Status Check

Run this in Render Shell to check database connection:
```python
python -c "from app import db; print('Database connected!' if db else 'Failed')"
```

---

## Need More Help?

Check the full logs in Render:
1. Go to your web service
2. Click "Logs" tab
3. Look for the actual error message
4. Share it if you need more help
