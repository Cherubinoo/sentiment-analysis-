# Student Sentiment Analysis System

Flask web app for collecting and analyzing student feedback on courses.

## 🚀 Deploy to Vercel

### 1. Setup Database (Required)
Get a free MySQL database from [Railway](https://railway.app):
- New Project → Provision MySQL
- Copy connection string
- Format: `mysql+pymysql://user:pass@host:port/railway`

### 2. Deploy
1. Go to [vercel.com](https://vercel.com)
2. Import this GitHub repo
3. Add environment variables:
   - `SECRET_KEY` = any random string
   - `DATABASE_URI` = your Railway MySQL URL
   - `FLASK_ENV` = production
   - `FLASK_DEBUG` = False
4. Deploy!

### 3. Initialize Database
```bash
# Set your production database URL
set DATABASE_URI=your-railway-database-url

# Create tables
python init_db.py
```

Done! Your app is live at `https://your-app.vercel.app`

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
