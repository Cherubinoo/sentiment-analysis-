"""
WSGI entry point for Vercel
"""
from app import app

# Vercel expects 'app' to be the Flask application
if __name__ == "__main__":
    app.run()
