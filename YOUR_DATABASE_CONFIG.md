# Your Database Configuration

## Railway MySQL Connection Details

**Original URL:**
```
mysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway
```

## For Vercel - Use This:

**DATABASE_URI:**
```
mysql+pymysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway
```

## Setup Steps

### 1. Add to Vercel Environment Variables

Go to your Vercel project → Settings → Environment Variables

Add these:

```
Name: DATABASE_URI
Value: mysql+pymysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway

Name: SECRET_KEY
Value: your-secret-key-make-it-random-12345

Name: FLASK_ENV
Value: production

Name: FLASK_DEBUG
Value: False
```

### 2. Initialize Database Tables

Run this on your local machine:

**Windows:**
```bash
set DATABASE_URI=mysql+pymysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway
python init_db.py
```

**Mac/Linux:**
```bash
export DATABASE_URI=mysql+pymysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway
python init_db.py
```

You should see: "Database tables created successfully!"

### 3. Redeploy Vercel

1. Go to Vercel dashboard
2. Click "Deployments" tab
3. Click three dots on latest deployment
4. Click "Redeploy"
5. Wait 2-3 minutes

### 4. Test Your App

Visit your Vercel URL - it should work now!

---

## Create Admin User

After deployment works, create an admin account:

```bash
# Set the database URL
set DATABASE_URI=mysql+pymysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway

# Run the script
python create_admin.py
```

Follow the prompts to create your admin account.

---

## Connection Details Breakdown

- **Host:** shinkansen.proxy.rlwy.net
- **Port:** 43189
- **User:** root
- **Password:** ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV
- **Database:** railway

---

## Test Connection Locally

Before deploying, test if the connection works:

```bash
set DATABASE_URI=mysql+pymysql://root:ZfmGLtbaVIBYbSIvywaygnkdyWoAGuvV@shinkansen.proxy.rlwy.net:43189/railway
python -c "from app import db; print('Connected!' if db else 'Failed')"
```

If this works locally, it will work on Vercel!
