# Student Sentiment Analysis System

Flask web app for collecting and analyzing student feedback on courses.

## 🚀 Quick Deploy with Custom Domain

**Your domain:** sentimentanalysis.lovestoblog.com

### Deploy to Render (Recommended)
1. Go to [render.com](https://render.com) → Sign up with GitHub
2. "New +" → "Web Service" → Select this repo
3. Click "Create Web Service" (auto-detects settings)
4. Add custom domain: `sentimentanalysis.lovestoblog.com`
5. Update DNS with CNAME record Render provides
6. Run `python init_db.py` in Shell tab

**Done!** Live at https://sentimentanalysis.lovestoblog.com

📖 **Detailed guide:** See `CUSTOM_DOMAIN_SETUP.md`

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
