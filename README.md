# Student Sentiment Analysis System

Flask web app for collecting and analyzing student feedback on courses.

## 🚀 Quick Deploy

**Domain:** sentimentanalysis.lovestoblog.com

### Recommended: PythonAnywhere (15 minutes)
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Clone repo and install dependencies
3. Setup MySQL database
4. Configure web app
5. Add custom domain

📖 **Full guide:** `DEPLOY.md`

### Alternative: Vercel
- Requires external database (Railway)
- See `VERCEL_FIX.md` if getting errors

### Other Options
- **cPanel hosting:** Use `passenger_wsgi.py` + `.htaccess`
- **VPS:** Full setup guide in `DEPLOY.md`

---

## 📁 Files Included

- `app.py` - Main Flask application
- `passenger_wsgi.py` - For shared hosting
- `.htaccess` - Apache configuration
- `init_db.py` - Database setup
- `requirements.txt` - Dependencies

## 🔧 Quick Local Test

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your database
python init_db.py
python app.py
```

Visit http://localhost:5000

## 📁 Project Structure

```
├── api/
│   └── index.py          # Vercel entry point
├── templates/            # HTML templates
├── app.py               # Main Flask app
├── preprocessing.py     # Sentiment analysis
├── init_db.py          # Database setup
├── create_admin.py     # Create admin user
├── create_new_staff.py # Create staff user
├── vercel.json         # Vercel config
└── requirements.txt    # Dependencies
```

## 🔧 Local Development

```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your database
python init_db.py
python app.py
```

Visit http://localhost:5000

## 📝 Environment Variables

- `SECRET_KEY` - Flask secret key
- `DATABASE_URI` - Database connection string
- `FLASK_ENV` - development/production
- `FLASK_DEBUG` - True/False

## 🐛 Troubleshooting

Check `VERCEL_QUICKSTART.md` for detailed help.
