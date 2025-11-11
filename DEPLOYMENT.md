# Deployment Guide

## Option 1: Render (Recommended - Free Tier Available)

### Steps:
1. Push your code to GitHub
2. Go to [render.com](https://render.com) and sign up
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Render will auto-detect the `render.yaml` config
6. Set environment variables:
   - `SECRET_KEY` (auto-generated or set your own)
   - `DATABASE_URI` (use Render's MySQL or external DB)
7. Click "Create Web Service"

### Database Setup on Render:
- Create a new PostgreSQL database (free tier) OR
- Use MySQL from external provider (PlanetScale, Railway)
- Copy the connection string to `DATABASE_URI`

---

## Option 2: Railway

### Steps:
1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repo
5. Add MySQL database from Railway marketplace
6. Set environment variables:
   - `SECRET_KEY` = random string
   - `DATABASE_URI` = `${{MySQL.DATABASE_URL}}` (Railway auto-fills)
7. Deploy!

---

## Option 3: Heroku

### Steps:
```bash
# Install Heroku CLI
heroku login
heroku create your-app-name

# Add MySQL addon (ClearDB)
heroku addons:create cleardb:ignite

# Get database URL
heroku config:get CLEARDB_DATABASE_URL

# Set environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DATABASE_URI="mysql+pymysql://..."

# Deploy
git push heroku main
```

---

## Option 4: PythonAnywhere

1. Upload files via Files tab
2. Create a new web app (Flask)
3. Configure WSGI file to point to `app.py`
4. Set up MySQL database in Databases tab
5. Update `.env` with database credentials

---

## Environment Variables Required

All platforms need these:
- `SECRET_KEY` - Random string for Flask sessions
- `DATABASE_URI` - MySQL connection string format:
  ```
  mysql+pymysql://username:password@host:port/database_name
  ```

---

## Pre-Deployment Checklist

- [ ] Update `requirements.txt` with gunicorn
- [ ] Create `.env.example` for reference
- [ ] Test locally with production settings
- [ ] Ensure database migrations work
- [ ] Remove debug mode in production
- [ ] Set strong SECRET_KEY

---

## Post-Deployment

1. Initialize database:
   ```bash
   # SSH into your server or use platform console
   python
   >>> from app import app, db
   >>> with app.app_context():
   ...     db.create_all()
   ```

2. Create admin user (run `create_admin.py` or similar)

3. Test all routes and functionality

---

## Troubleshooting

- **Database connection fails**: Check DATABASE_URI format
- **Module not found**: Ensure all dependencies in requirements.txt
- **Static files not loading**: Check static file serving config
- **App crashes on start**: Check logs for errors
