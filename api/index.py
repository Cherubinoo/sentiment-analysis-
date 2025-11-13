"""
Vercel serverless function entry point
"""
import sys
import os

# Add parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Set environment to production if not set
if not os.getenv('FLASK_ENV'):
    os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application

# Vercel handler
def handler(event, context):
    return application
