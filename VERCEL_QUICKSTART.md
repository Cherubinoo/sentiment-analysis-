# Deploy to Vercel - Quick Guide

## ⚠️ Before You Start

Your Flask app needs an **external database** for Vercel. Choose one:

### Option 1: Railway MySQL (Easiest - Free)
```bash
1. Go to railway.app
2. New Project → Provision MySQL
3. Copy the "MySQL Connection URL"
4. Format: mysql+pymysql://user:pass@host:port/railway
```

### Option 2: PlanetScale MySQL (Free)
```bash
1. Go to planetscale.com
2. Create database
3. Get connection string
4. Add ?ssl_ca=/etc/ssl/cert.pem at the end
```

---

## 🚀 Deploy Steps

### 1. Push to GitHub
```bash
git add .
git commit -m "Add Vercel configuration"
git push origin deployment-ready
```

### 2. Deploy on Vercel
1. Go to [vercel.com](https://vercel.com)
2. Click "Add New" → "Project"
3. Import your GitHub repo
4. Vercel auto-detects settings
5. **Add Environment Variables**:
   ```
   SECRET_KEY = your-random-secret-key-here
   DATABASE_URI = your-database-connection-string
   FLASK_ENV = production
   FLASK_DEBUG = False
   ```
6. Click "Deploy"
7. Wait 2-3 minutes

### 3. Initialize Database
Since Vercel is serverless, run this locally:

```bash
# In your terminal
# Set your production database URL
set DATABASE_URI=your-production-database-url

# Initialize tables
python init_db.py
```

Or use Railway/Render temporarily to run `python init_db.py`

### 4. Test Your App
Visit your Vercel URL: `https://your-app.vercel.app`

---

## 🔧 If Something Goes Wrong

### Check Vercel Logs
1. Go to your project on Vercel
2. Click "Deployments"
3. Click latest deployment
4. Check "Function Logs"

### Common Fixes

**"Module not found"**
- Make sure all files are pushed to GitHub
- Check requirements.txt is complete

**"Database connection failed"**
- Verify DATABASE_URI in Vercel environment variables
- Test connection string locally first
- Make sure database allows external connections

**"Function timeout"**
- Your request took > 10 seconds
- Optimize slow database queries
- Add database indexes

**"502 Bad Gateway"**
- Check Function Logs for actual error
- Usually a Python error in your code

---

## 📝 Files Created for Vercel

- `vercel.json` - Vercel configuration
- `api/index.py` - Serverless entry point
- `wsgi.py` - WSGI wrapper

---

## 🎯 Pro Tips

1. **Use Railway for database** - Free, easy, works great with Vercel
2. **Test locally first** - Make sure app works before deploying
3. **Check logs** - Vercel logs show all errors
4. **Keep it simple** - Serverless has limitations

---

## 🔄 Switch to Render Instead?

If Vercel gives you trouble, Render is easier for Flask apps:
- No serverless limitations
- Built-in database
- No timeout issues
- Follow `QUICKSTART.md` instead

Both work, but Render is more straightforward for your app!
