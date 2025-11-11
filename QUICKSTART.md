# Quick Deployment Guide

## 🚀 Deploy to Render (Easiest - 5 minutes)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Render**
   - Go to https://render.com/
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Select your repo
   - Render auto-detects settings from `render.yaml`
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment

3. **Database Auto-Created**
   - Render will automatically create a PostgreSQL database from `render.yaml`
   - The `DATABASE_URI` is automatically set
   - No manual database setup needed!

4. **Initialize Database**
   - After first deployment, go to your web service → "Shell" tab
   - Run:
     ```bash
     python init_db.py
     ```
   - This creates all database tables

5. **Done!** Your app is live at `https://your-app-name.onrender.com`

---

## 🚂 Deploy to Railway (Alternative)

1. Push to GitHub (same as above)
2. Go to https://railway.app/
3. "New Project" → "Deploy from GitHub"
4. Select your repo
5. Add MySQL from marketplace
6. Set `DATABASE_URI` = `${{MySQL.DATABASE_URL}}`
7. Deploy automatically happens!

---

## 📝 Important Notes

- **Free tier limitations**: Apps may sleep after inactivity
- **Database**: Use MySQL or PostgreSQL (both work)
- **Environment variables**: Set `SECRET_KEY` and `DATABASE_URI`
- **First run**: Initialize database with `db.create_all()`

---

## 🔧 Local Testing Before Deploy

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your local database

# Run locally
python app.py
```

Visit http://localhost:5000

---

## ❓ Need Help?

Check `DEPLOYMENT.md` for detailed instructions for all platforms.
