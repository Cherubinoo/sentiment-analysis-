# Railway Database Setup for Vercel

## Quick Guide

### Step 1: Create Railway MySQL Database

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"
4. Click "Provision MySQL"
5. Wait for deployment (~30 seconds)

### Step 2: Get Connection String

1. Click on the MySQL service
2. Go to "Variables" tab
3. Find `MYSQL_URL` variable
4. Copy the value - it looks like:
   ```
   mysql://root:password123@containers-us-west-123.railway.app:1234/railway
   ```

### Step 3: Convert for Flask

Change `mysql://` to `mysql+pymysql://`:

**Railway gives you:**
```
mysql://root:password123@containers-us-west-123.railway.app:1234/railway
```

**You use in Vercel:**
```
mysql+pymysql://root:password123@containers-us-west-123.railway.app:1234/railway
```

### Step 4: Add to Vercel

1. Go to your Vercel project
2. Settings → Environment Variables
3. Add:
   ```
   Name: DATABASE_URI
   Value: mysql+pymysql://root:password123@containers-us-west-123.railway.app:1234/railway
   ```
4. Add:
   ```
   Name: SECRET_KEY
   Value: make-this-a-long-random-string-12345
   ```
5. Add:
   ```
   Name: FLASK_ENV
   Value: production
   ```
6. Click "Save"

### Step 5: Initialize Database

Run this on your local machine:

**Windows:**
```bash
set DATABASE_URI=mysql+pymysql://root:password123@containers-us-west-123.railway.app:1234/railway
python init_db.py
```

**Mac/Linux:**
```bash
export DATABASE_URI=mysql+pymysql://root:password123@containers-us-west-123.railway.app:1234/railway
python init_db.py
```

You should see: "Database tables created successfully!"

### Step 6: Redeploy Vercel

1. Go to Vercel → Deployments
2. Click three dots on latest deployment
3. Click "Redeploy"
4. Wait 2-3 minutes

### Step 7: Test

Visit your Vercel URL - it should work now!

---

## Troubleshooting

### "Can't connect to MySQL server"

**Check:**
- Railway MySQL is running (green status)
- Connection string is correct
- You changed `mysql://` to `mysql+pymysql://`
- No typos in the URL

**Test locally:**
```bash
set DATABASE_URI=your-railway-url
python -c "from app import db; print('Connected!')"
```

### "Table doesn't exist"

You forgot to run `python init_db.py`!

### "Access denied for user"

- Check username/password in connection string
- Railway might have regenerated credentials
- Get fresh `MYSQL_URL` from Railway

### Railway MySQL Variables

Railway provides these variables (use `MYSQL_URL`):
- `MYSQL_URL` - Full connection string (use this!)
- `MYSQL_HOST` - Just the host
- `MYSQL_PORT` - Just the port
- `MYSQL_USER` - Username
- `MYSQL_PASSWORD` - Password
- `MYSQL_DATABASE` - Database name

---

## Alternative: Deploy to Railway Instead

If Vercel keeps giving problems, deploy to Railway directly:

1. Railway → "New Project" → "Deploy from GitHub"
2. Select your repo
3. Add MySQL from marketplace
4. Set environment variable:
   ```
   DATABASE_URI = ${{ MYSQL.MYSQL_URL }}
   ```
   (Railway auto-converts this!)
5. Deploy!

Railway is easier for Flask apps than Vercel.
