# Student Sentiment Analysis System

Flask-based web application for collecting and analyzing student feedback on courses.

## 🚀 Quick Deploy

**Your app is crashing?** → Read `FIX_RENDER_DEPLOYMENT.md`

**First time deploying?** → Read `QUICKSTART.md` (5 minutes)

**Need detailed guide?** → Read `DEPLOYMENT.md`

## 📋 Features

- Student feedback collection system
- Multi-semester course reviews
- Admin dashboard with analytics
- Sentiment analysis on feedback
- CSV export functionality
- Role-based access (Student/Admin)

## 🛠️ Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your database credentials

# Initialize database
python init_db.py

# Run app
python app.py
```

Visit http://localhost:5000

## 🔧 Database Setup

### Check Connection
```bash
python check_db.py
```

### Initialize Tables
```bash
python init_db.py
```

## 📦 Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Database**: MySQL or PostgreSQL
- **Auth**: Flask-Login
- **Sentiment**: TextBlob
- **Deployment**: Gunicorn

## 🌐 Deployment Platforms

- ✅ Render (Recommended)
- ✅ Railway
- ✅ Heroku
- ✅ PythonAnywhere

## 📝 Environment Variables

Required:
- `SECRET_KEY` - Flask secret key
- `DATABASE_URI` - Database connection string
- `FLASK_ENV` - development/production
- `FLASK_DEBUG` - True/False

## 🐛 Troubleshooting

**App crashes on startup?**
- Check `FIX_RENDER_DEPLOYMENT.md`
- Run `python check_db.py` to verify database

**Database connection error?**
- Verify `DATABASE_URI` format
- Check database is running
- Run `python check_db.py`

**Tables don't exist?**
- Run `python init_db.py`

## 📄 License

MIT License - feel free to use for your projects!
