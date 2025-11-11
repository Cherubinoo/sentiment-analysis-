# Student Sentiment Analysis System

Flask web app for collecting and analyzing student feedback on courses.

## 🚀 Deploy to Your Domain

**Your domain:** sentimentanalysis.lovestoblog.com

### Option 1: PythonAnywhere (Easiest - Free)
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload code or clone from GitHub
3. Setup MySQL database
4. Configure web app
5. Add custom domain

**Setup time:** 15 minutes  
📖 **Full guide:** `TRADITIONAL_HOSTING.md`

### Option 2: Your Existing Hosting
If lovestoblog.com is on shared hosting (cPanel):
- Upload files via FTP
- Create MySQL database
- Setup subdomain
- Use `passenger_wsgi.py` and `.htaccess`

📖 **Full guide:** `TRADITIONAL_HOSTING.md`

### Option 3: VPS (DigitalOcean/Linode)
- $5/month
- Full control
- Nginx + Gunicorn setup

📖 **Full guide:** `TRADITIONAL_HOSTING.md`

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
