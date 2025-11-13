"""
Vercel serverless function entry point
"""
import sys
import os

# Set environment variables before importing app
os.environ['FLASK_ENV'] = os.getenv('FLASK_ENV', 'production')
os.environ['PYTHONUNBUFFERED'] = '1'

# Add parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Import the Flask app
try:
    from app import app
except Exception as e:
    print(f"Error importing app: {e}")
    import traceback
    traceback.print_exc()
    raise

# Export app for Vercel
# Vercel expects the app to be named 'app' or 'application'
application = app
