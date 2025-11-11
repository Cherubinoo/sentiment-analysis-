# Deploy to Vercel

## ⚠️ Important Limitations

Vercel is **serverless** - your Flask app will have these limitations:
- **10 second timeout** per request (Hobby plan)
- **No persistent storage** (database must be external)
- **Cold starts** (first request may be slow)
- **Stateless** (no in-memory sessions)

For a full Flask app like yours, **Render or Railway is better**. But if you want Vercel:

---

## 🚀 Quick Deploy to Vercel

### Step 1: Setup Database (Required)

You MUST use an external database. Choose one:

**Option A: PlanetScale (Free MySQL)**
1. Go to [planetscale.com](https://planetscale.com)
2. Create account → New database
3. Get connection string
4. Format: `mysql+pymysql://user:pass@host/dbname?ssl_ca=/etc/ssl/cert.pem`

**Option B: Railway MySQL**
1. Go to [railway.app](https://railway.app)
2. New Project → Provision MySQL
3. Copy connection string
4. Format: `mysql+pymysql://user:pass@host:port/dbname`

**Option C: Supabase PostgreSQL (Free)**
1. Go to [supabase.com](https://supabase.com)
2. New project
3. Get PostgreSQL connection string
4. Use as-is: `postgresql://user:pass@host:port/dbname`

### Step 2: Deploy to Vercel

**Via Vercel Dashboard:**
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repo
3. Vercel auto-detects Python
4. Add Environment Variables:
   - `SECRET_KEY` = (generate random string)
   - `DATABASE_URI` = (your database connection string)
   - `FLASK_ENV` = `production`
   - `FLASK_DEBUG` = `False`
5. Click "Deploy"

**Via Vercel CLI:**
```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Deploy
vercel

# Set environment variables
vercel env add SECRET_KEY
vercel env add DATABASE_URI
vercel env add FLASK_ENV
vercel env add FLASK_DEBUG

# Deploy to production
vercel --prod
```

### Step 3: Initialize Database

Since Vercel is serverless, you need to initialize the database separately:

**Option 1: Run locally**
```bash
# Set your production DATABASE_URI in .env
DATABASE_URI=your-production-database-url

# Run init script
python init_db.py
```

**Option 2: Use Railway/Render for one-time setup**
- Deploy to Railway temporarily
- Run `python init_db.py` in their shell
- Database is now initialized
- Use same database with Vercel

---

## 🔧 Configuration Files

Created for you:
- `vercel.json` - Vercel configuration
- `api/index.py` - Serverless function entry
- `wsgi.py` - WSGI wrapper

---

## ⚡ Performance Tips

1. **Use connection pooling** - Add to DATABASE_URI:
   ```
   ?pool_size=5&max_overflow=10&pool_recycle=3600
   ```

2. **Optimize cold starts** - Keep dependencies minimal

3. **Use CDN** - Serve static files from Vercel's CDN

4. **Cache responses** - Add caching headers where possible

---

## 🐛 Common Issues

### "Function execution timed out"
- Your request took > 10 seconds
- Optimize database queries
- Add indexes to database
- Consider upgrading Vercel plan (60s timeout)

### "Module not found"
- Check `requirements.txt` has all dependencies
- Vercel installs from requirements.txt automatically

### "Database connection failed"
- Verify DATABASE_URI is set in Vercel dashboard
- Check database allows external connections
- Test connection string locally first

### "Static files not loading"
- Vercel serves static files automatically
- Check paths are correct
- Use relative paths, not absolute

---

## 🔄 Alternative: Use Render Instead

Honestly, for a Flask app with database like yours, **Render is better**:

✅ No timeout limits
✅ Persistent connections
✅ Free tier available
✅ Easier database setup
✅ Better for traditional web apps

Vercel is great for:
- Next.js apps
- Static sites
- Simple APIs
- Serverless functions

Your app is better suited for Render/Railway. But Vercel will work if you need it!

---

## 📊 Comparison

| Feature | Vercel | Render | Railway |
|---------|--------|--------|---------|
| Timeout | 10s (60s Pro) | No limit | No limit |
| Database | External only | Built-in | Built-in |
| Cold starts | Yes | Minimal | Minimal |
| Free tier | Yes | Yes | Yes |
| Best for | Serverless | Web apps | Web apps |

---

## 🎯 Recommendation

**For your sentiment analysis app:**
1. **Best**: Render or Railway (traditional hosting)
2. **Works**: Vercel (with external database)
3. **Avoid**: Netlify (not for Flask)

If you're already on Vercel and want to switch:
- Your code is ready for Render
- Just follow `QUICKSTART.md`
- Takes 5 minutes to deploy on Render
