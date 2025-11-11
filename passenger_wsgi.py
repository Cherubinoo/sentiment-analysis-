"""
WSGI entry point for shared hosting (cPanel/Passenger)
"""
import sys
import os

# Add your application directory to the Python path
INTERP = os.path.expanduser("~/sentiment-analysis-/venv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add the app directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from app import app as application

if __name__ == '__main__':
    application.run()
