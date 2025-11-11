# Deploy to Traditional Hosting

Since cloud platforms aren't working, here are your options:

## Option 1: PythonAnywhere (Easiest - Free Tier)

### Why PythonAnywhere?
- ✅ Free tier available
- ✅ Python pre-installed
- ✅ Easy MySQL setup
- ✅ Custom domain support
- ✅ No server management

### Steps:

1. **Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)**
   - Free account works fine

2. **Upload your code:**
   - Go to "Files" tab
   - Upload all files OR clone from GitHub:
   ```bash
   git clone https://github.com/Cherubinoo/sentiment-analysis-.git
   cd sentiment-analysis-
   ```

3. **Install dependencies:**
   - Go to "Consoles" → Start a Bash console
   ```bash
   cd sentiment-analysis-
   pip3 install --user -r requirements.txt
   ```

4. **Setup MySQL Database:**
   - Go to "Databases" tab
   - Create database: `sentiment_db`
   - Note the connection details
   - Create `.env` file:
   ```
   SECRET_KEY=your-random-secret-key
   DATABASE_URI=mysql+pymysql://username:password@username.mysql.pythonanywhere-services.com/username$sentiment_db
   FLASK_ENV=production
   FLASK_DEBUG=False
   ```

5. **Initialize Database:**
   ```bash
   python3 init_db.py
   ```

6. **Setup Web App:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration" → Python 3.10
   - Set source code: `/home/yourusername/sentiment-analysis-`
   - Edit WSGI file, replace everything with:
   ```python
   import sys
   import os
   
   path = '/home/yourusername/sentiment-analysis-'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

7. **Add Custom Domain:**
   - In "Web" tab, scroll to "Custom domains"
   - Add: `sentimentanalysis.lovestoblog.com`
   - Update DNS CNAME to point to: `yourusername.pythonanywhere.com`

8. **Reload and Done!**
   - Click "Reload" button
   - Visit your site!

---

## Option 2: Shared Hosting (cPanel)

If lovestoblog.com is on shared hosting:

### Requirements Check:
- Python 3.x support
- MySQL database
- SSH access (optional but helpful)

### Steps:

1. **Create MySQL Database in cPanel:**
   - Database name: `sentiment_db`
   - Create user and grant all privileges
   - Note: host, username, password, database name

2. **Upload Files:**
   - Use FTP or File Manager
   - Upload to: `public_html/sentimentanalysis/`

3. **Create `.env` file:**
   ```
   SECRET_KEY=your-random-secret-key
   DATABASE_URI=mysql+pymysql://username:password@localhost/sentiment_db
   FLASK_ENV=production
   FLASK_DEBUG=False
   ```

4. **Install Dependencies (via SSH):**
   ```bash
   cd public_html/sentimentanalysis
   pip3 install -r requirements.txt --user
   python3 init_db.py
   ```

5. **Setup Subdomain:**
   - In cPanel → Subdomains
   - Create: `sentimentanalysis.lovestoblog.com`
   - Point to: `public_html/sentimentanalysis`

6. **Create .htaccess:**
   ```apache
   RewriteEngine On
   RewriteCond %{REQUEST_FILENAME} !-f
   RewriteRule ^(.*)$ passenger_wsgi.py [L]
   ```

7. **Create passenger_wsgi.py:**
   ```python
   import sys
   import os
   
   sys.path.insert(0, os.path.dirname(__file__))
   
   from app import app as application
   ```

8. **Restart and test!**

---

## Option 3: DigitalOcean/Linode VPS ($5/month)

### Quick Setup:

1. **Create Droplet/VPS:**
   - Ubuntu 22.04
   - $5/month plan

2. **SSH into server:**
   ```bash
   ssh root@your-server-ip
   ```

3. **Install dependencies:**
   ```bash
   apt update
   apt install python3-pip python3-venv nginx mysql-server git -y
   ```

4. **Clone and setup:**
   ```bash
   cd /var/www
   git clone https://github.com/Cherubinoo/sentiment-analysis-.git
   cd sentiment-analysis-
   
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **Setup MySQL:**
   ```bash
   mysql -u root -p
   CREATE DATABASE sentiment_db;
   CREATE USER 'sentiment_user'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON sentiment_db.* TO 'sentiment_user'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

6. **Create .env:**
   ```bash
   nano .env
   ```
   Add:
   ```
   SECRET_KEY=your-random-secret-key
   DATABASE_URI=mysql+pymysql://sentiment_user:your_password@localhost/sentiment_db
   FLASK_ENV=production
   FLASK_DEBUG=False
   ```

7. **Initialize database:**
   ```bash
   python init_db.py
   ```

8. **Setup Gunicorn service:**
   ```bash
   nano /etc/systemd/system/sentiment.service
   ```
   Add:
   ```ini
   [Unit]
   Description=Sentiment Analysis App
   After=network.target
   
   [Service]
   User=www-data
   WorkingDirectory=/var/www/sentiment-analysis-
   Environment="PATH=/var/www/sentiment-analysis-/venv/bin"
   ExecStart=/var/www/sentiment-analysis-/venv/bin/gunicorn app:app --bind 127.0.0.1:8000
   
   [Install]
   WantedBy=multi-user.target
   ```

9. **Setup Nginx:**
   ```bash
   nano /etc/nginx/sites-available/sentiment
   ```
   Add:
   ```nginx
   server {
       listen 80;
       server_name sentimentanalysis.lovestoblog.com;
   
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   
       location /static {
           alias /var/www/sentiment-analysis-/static;
       }
   }
   ```

10. **Enable and start:**
    ```bash
    ln -s /etc/nginx/sites-available/sentiment /etc/nginx/sites-enabled/
    systemctl start sentiment
    systemctl enable sentiment
    systemctl restart nginx
    ```

11. **Setup SSL (free):**
    ```bash
    apt install certbot python3-certbot-nginx -y
    certbot --nginx -d sentimentanalysis.lovestoblog.com
    ```

12. **Update DNS:**
    - Point `sentimentanalysis.lovestoblog.com` to your server IP

---

## Recommended: PythonAnywhere

**Why?**
- No server management
- Free tier available
- Easy setup (15 minutes)
- Custom domain support
- MySQL included

**Cost:** Free (or $5/month for custom domain on free tier)

---

## What's Not Working with Render/Railway?

Can you share the error? Common issues:
- Database connection timeout
- Build failures
- Module not found

I can help debug if you share the error logs!
