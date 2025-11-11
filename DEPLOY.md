# Deployment Guide

## 🎯 Quick Start: PythonAnywhere (Recommended)

**Best for:** sentimentanalysis.lovestoblog.com

### Steps:

1. **Sign up:** [pythonanywhere.com](https://www.pythonanywhere.com) (Free)

2. **Upload code:**
   ```bash
   # In PythonAnywhere Bash console
   git clone https://github.com/Cherubinoo/sentiment-analysis-.git
   cd sentiment-analysis-
   pip3 install --user -r requirements.txt
   ```

3. **Setup database:**
   - Go to "Databases" tab
   - Create: `sentiment_db`
   - Note username/password

4. **Create .env:**
   ```
   SECRET_KEY=your-random-secret-key
   DATABASE_URI=mysql+pymysql://username:password@username.mysql.pythonanywhere-services.com/username$sentiment_db
   FLASK_ENV=production
   ```

5. **Initialize:**
   ```bash
   python3 init_db.py
   ```

6. **Setup web app:**
   - "Web" tab → "Add new web app"
   - Manual config → Python 3.10
   - Source: `/home/yourusername/sentiment-analysis-`
   - WSGI file:
   ```python
   import sys
   path = '/home/yourusername/sentiment-analysis-'
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```

7. **Add domain:**
   - "Web" tab → "Custom domains"
   - Add: `sentimentanalysis.lovestoblog.com`
   - Update DNS CNAME to: `yourusername.pythonanywhere.com`

8. **Reload** and done!

---

## 🔧 Vercel (If you must)

### Requirements:
- External database (Railway MySQL)
- Environment variables configured

### Fix "Internal Server Error":

1. **Get database from Railway:**
   - [railway.app](https://railway.app) → Provision MySQL
   - Copy connection URL
   - Format: `mysql+pymysql://user:pass@host:port/railway`

2. **Add to Vercel:**
   - Settings → Environment Variables
   - `DATABASE_URI` = your Railway URL
   - `SECRET_KEY` = random string
   - `FLASK_ENV` = production

3. **Initialize database locally:**
   ```bash
   set DATABASE_URI=your-railway-url
   python init_db.py
   ```

4. **Redeploy** on Vercel

See `VERCEL_FIX.md` for detailed troubleshooting.

---

## 🖥️ Shared Hosting (cPanel)

If lovestoblog.com is on cPanel:

1. Upload files via FTP to `public_html/sentimentanalysis/`
2. Create MySQL database in cPanel
3. Create `.env` with database credentials
4. Install dependencies: `pip3 install -r requirements.txt --user`
5. Run: `python3 init_db.py`
6. Create subdomain pointing to folder
7. Files `passenger_wsgi.py` and `.htaccess` are ready

See `TRADITIONAL_HOSTING.md` for details.

---

## 💻 VPS (DigitalOcean/Linode)

For full control ($5/month):

```bash
# Install
apt update
apt install python3-pip nginx mysql-server git -y

# Clone
cd /var/www
git clone https://github.com/Cherubinoo/sentiment-analysis-.git
cd sentiment-analysis-

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Database
mysql -u root -p
CREATE DATABASE sentiment_db;
# ... create user and grant privileges

# Configure
nano .env  # Add credentials
python init_db.py

# Setup Gunicorn + Nginx
# See TRADITIONAL_HOSTING.md for full config
```

---

## 📊 Comparison

| Platform | Cost | Setup Time | Custom Domain | Best For |
|----------|------|------------|---------------|----------|
| PythonAnywhere | Free | 15 min | ✅ Yes | Easiest |
| Vercel | Free | 20 min | ✅ Yes | Serverless |
| cPanel | Varies | 30 min | ✅ Yes | Existing hosting |
| VPS | $5/mo | 45 min | ✅ Yes | Full control |

**Recommendation:** Start with PythonAnywhere!
