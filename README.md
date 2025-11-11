# Student Sentiment Analysis

A Flask-based web application for collecting and analyzing student feedback on subjects across different regulations and semesters.

## Features
- User registration and login (Admin and Student roles)
- Students can select regulation, semester, and submit reviews for subjects
- Sentiment analysis using TextBlob
- Admin dashboard with sentiment analytics

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Setup:**
   - Create a MySQL database named `sentiment_db` in phpMyAdmin.
   - Update `.env` with your database credentials if needed.

3. **Seed the database:**
   ```bash
   python seed.py
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access:**
   - Open http://127.0.0.1:5000
   - Register as admin or student, then login.

## Database Schema
- Users, Regulations, Semesters, Subjects, Reviews

## Usage
- Students: Register, select regulation/semester, submit ratings and comments.
- Admins: View aggregated sentiment data by regulation/semester.
