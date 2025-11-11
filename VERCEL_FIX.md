# Fix Vercel "Internal Server Error"

## The Problem
Your app is crashing because:
1. **No DATABASE_URI set** - Vercel doesn't have database connection
2. **Database connection fails on startup** - App tries to connect immediately

## Quick Fix

### Step 1: Get a Database
You MUST have an external database for Vercel. Get one from Railway:

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. "New Project" → "Provision MySQL"
4. Click on MySQL service
5. Go to "Variables" tab
6. Find `MYSQL_URL` variable
7. Copy the value and change format from:
   ```
   mysql://user:pass@host:port/railway
   ```
   To:
   ```
   mysql+pymysql://user:pass@host:port/railway
   ```

**Example:**
- Railway gives: `mysql://root:password@containers-us-west-123.railway.app:1234/railway`
- You use: `mysql+pymysql://root:password@containers-us-west-123.railway.app:1234/railway`

### Step 2: Add to Vercel Environment Variables

1. Go to your Vercel project dashboard
2. Click "Settings" tab
3. Click "Environment Variables"
4. Add these variables:

```
SECRET_KEY = any-random-string-here-make-it-long
DATABASE_URI = mysql+pymysql://user:pass@host:port/railway
FLASK_ENV = production
FLASK_DEBUG = False
```

5. Click "Save"

### Step 3: Redeploy

1. Go to "Deployments" tab
2. Click the three dots on latest deployment
3. Click "Redeploy"
4. Wait 2-3 minutes

### Step 4: Initialize Database

After successful deployment, run this locally:

```bash
# Set your Railway database URL
set DATABASE_URI=mysql+pymysql://user:pass@host:port/railway

# Initialize tables
python init_db.py
```

### Step 5: Test

Visit your Vercel URL - it should work now!

---

## Still Getting Errors?

### Check Vercel Function Logs

1. Go to your Vercel project
2. Click "Deployments"
3. Click on the latest deployment
4. Click "Functions" tab
5. Click on "api/index.py"
6. Check the logs for actual error

### Common Issues:

**"Module not found"**
- Make sure all files are in GitHub
- Check requirements.txt is complete
- Redeploy

**"Can't connect to MySQL"**
- Verify DATABASE_URI format is correct
- Test connection locally first
- Make sure Railway database is running

**"Table doesn't exist"**
- Run `python init_db.py` locally with production DATABASE_URI
- Tables need to be created first

**"Function timeout"**
- Your database queries are too slow
- Add indexes to database
- Optimize queries

---

## Alternative: Just Use PythonAnywhere

Honestly, Vercel is complicated for Flask apps. **PythonAnywhere is way easier**:

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your code
3. Setup MySQL (included)
4. Configure web app
5. Add custom domain
6. Done in 15 minutes!

See `TRADITIONAL_HOSTING.md` for full guide.

---

## Debug Checklist

- [ ] DATABASE_URI is set in Vercel environment variables
- [ ] DATABASE_URI format is `mysql+pymysql://...`
- [ ] Railway MySQL database is running
- [ ] Database tables are created (`python init_db.py`)
- [ ] SECRET_KEY is set
- [ ] All files are pushed to GitHub
- [ ] Redeployed after adding environment variables

---

## Test Database Connection Locally

Before deploying, test your Railway database:

```bash
# Set the Railway database URL
set DATABASE_URI=mysql+pymysql://user:pass@host:port/railway

# Test connection
python -c "from app import db; print('Connected!' if db else 'Failed')"
```

If this fails locally, it will fail on Vercel too!
