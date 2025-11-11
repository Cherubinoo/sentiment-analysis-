# Deploy with Custom Domain: sentimentanalysis.lovestoblog.com

## Option 1: Render (Recommended - Easy Custom Domain)

### Step 1: Deploy to Render
1. Go to [render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Render auto-detects from `render.yaml`
6. Click "Create Web Service"
7. Wait 2-3 minutes for deployment

### Step 2: Add Custom Domain
1. In Render dashboard, go to your web service
2. Click "Settings" tab
3. Scroll to "Custom Domain" section
4. Click "Add Custom Domain"
5. Enter: `sentimentanalysis.lovestoblog.com`
6. Render will show you DNS records to add

### Step 3: Update DNS (at lovestoblog.com)
Go to your domain registrar/DNS provider and add:

**CNAME Record:**
```
Type: CNAME
Name: sentimentanalysis
Value: [your-app-name].onrender.com
TTL: 3600
```

Or if they give you an A record:
```
Type: A
Name: sentimentanalysis
Value: [IP address from Render]
TTL: 3600
```

### Step 4: Initialize Database
After deployment, go to Shell tab:
```bash
python init_db.py
```

### Step 5: Wait for DNS (5-30 minutes)
- DNS changes take time to propagate
- Check status in Render dashboard
- Once verified, your site is live at sentimentanalysis.lovestoblog.com

---

## Option 2: Railway (Also Easy)

### Step 1: Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. "New Project" → "Deploy from GitHub"
3. Select your repo
4. Add PostgreSQL or MySQL from marketplace
5. Set environment variables:
   - `SECRET_KEY` = random string
   - `DATABASE_URI` = `${{MySQL.DATABASE_URL}}`
6. Deploy!

### Step 2: Add Custom Domain
1. In Railway project, click your service
2. Go to "Settings" tab
3. Scroll to "Domains"
4. Click "Custom Domain"
5. Enter: `sentimentanalysis.lovestoblog.com`
6. Railway shows DNS records

### Step 3: Update DNS
Add CNAME record at your DNS provider:
```
Type: CNAME
Name: sentimentanalysis
Value: [your-app].up.railway.app
TTL: 3600
```

---

## Option 3: Traditional Hosting (cPanel/Shared Hosting)

If lovestoblog.com is on shared hosting with cPanel:

### Requirements:
- Python support (check with host)
- SSH access
- Passenger or similar WSGI support

### Steps:
1. Upload files via FTP/SSH
2. Install dependencies: `pip install -r requirements.txt`
3. Setup MySQL database in cPanel
4. Configure `.env` with database credentials
5. Point subdomain to app directory
6. Configure WSGI (passenger_wsgi.py)

### Create passenger_wsgi.py:
```python
import sys
import os

# Add your app directory to path
sys.path.insert(0, os.path.dirname(__file__))

from app import app as application
```

---

## Option 4: VPS/Cloud Server

If you have a VPS or cloud server:

### Quick Setup with Nginx:
```bash
# Install dependencies
sudo apt update
sudo apt install python3-pip nginx

# Clone repo
git clone https://github.com/Cherubinoo/sentiment-analysis-.git
cd sentiment-analysis-

# Install Python packages
pip3 install -r requirements.txt

# Setup database
python3 init_db.py

# Run with gunicorn
gunicorn app:app --bind 0.0.0.0:8000
```

### Nginx Config:
```nginx
server {
    listen 80;
    server_name sentimentanalysis.lovestoblog.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Recommended: Use Render

**Why Render?**
- ✅ Free tier available
- ✅ Easy custom domain setup
- ✅ Automatic SSL certificate
- ✅ Built-in database
- ✅ No server management
- ✅ Auto-deploys from GitHub

**Setup time:** 10 minutes total

---

## DNS Propagation Check

After updating DNS, check if it's working:
```bash
# Windows
nslookup sentimentanalysis.lovestoblog.com

# Should show the IP/CNAME you configured
```

Or use online tools:
- https://dnschecker.org
- https://www.whatsmydns.net

---

## SSL Certificate (HTTPS)

Both Render and Railway provide **free SSL automatically**!

Your site will be:
- ✅ https://sentimentanalysis.lovestoblog.com (secure)
- No manual SSL setup needed

---

## Need Help?

1. **Render not working?** Check deployment logs
2. **DNS not updating?** Wait 30 minutes, check with DNS checker
3. **Database errors?** Run `python init_db.py` in Shell
4. **Domain not connecting?** Verify CNAME record is correct
