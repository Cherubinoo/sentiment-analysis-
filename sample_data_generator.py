"""
Sample Data Generator for Testing Sentiment Analysis
Generates synthetic student feedback data for testing
"""

import pandas as pd
import random
from datetime import datetime, timedelta

# Sample feedback comments
HAPPY_COMMENTS = [
    "Excellent teaching methods and very clear explanations",
    "The professor is very knowledgeable and helpful",
    "Great course content, learned a lot",
    "Very engaging lectures and good lab support",
    "Outstanding teacher, makes complex topics easy",
    "Best course I've taken, highly recommend",
    "Very organized and well-structured course",
    "Professor is always available for help",
    "Great examples and real-world applications"
]

NEUTRAL_COMMENTS = [
    "Course content is okay, could be better",
    "Teaching is average, nothing special",
    "Decent course overall",
    "Some parts are good, some need improvement",
    "Moderate level of difficulty",
    "submitted",
    "Fair examination process",
    "Regular teaching methods"
]

BAD_COMMENTS = [
    "Teaching needs significant improvement",
    "Course content is outdated and boring",
    "Poor lab facilities and support",
    "Examination is too difficult",
    "Not satisfied with the teaching method",
    "Library resources are inadequate",
    "Very confusing explanations",
    "Need better organization",
    "Lack of practical examples"
]

RATING_OPTIONS = ['Excellent', 'Very Good', 'Good', 'Average', 'Fair', 'Poor', 'Bad']

def generate_sample_data(num_rows=100):
    """Generate sample student feedback data"""
    
    data = []
    start_date = datetime.now() - timedelta(days=180)
    
    for i in range(num_rows):
        # Determine overall sentiment
        sentiment_type = random.choices(['happy', 'neutral', 'bad'], weights=[0.5, 0.3, 0.2])[0]
        
        # Select comment based on sentiment
        if sentiment_type == 'happy':
            comment = random.choice(HAPPY_COMMENTS)
            rating_bias = [5, 4, 3, 2, 1]
            rating_weights = [0.6, 0.3, 0.08, 0.01, 0.01]
        elif sentiment_type == 'neutral':
            comment = random.choice(NEUTRAL_COMMENTS)
            rating_bias = [5, 4, 3, 2, 1]
            rating_weights = [0.1, 0.3, 0.5, 0.08, 0.02]
        else:
            comment = random.choice(BAD_COMMENTS)
            rating_bias = [5, 4, 3, 2, 1]
            rating_weights = [0.02, 0.08, 0.2, 0.4, 0.3]
        
        # Generate ratings based on sentiment
        def get_rating_text(num_val):
            rating_map = {5: 'Excellent', 4: 'Very Good', 3: 'Average', 2: 'Poor', 1: 'Bad'}
            return rating_map[num_val]
        
        teaching = get_rating_text(random.choices(rating_bias, rating_weights)[0])
        course_content = get_rating_text(random.choices(rating_bias, rating_weights)[0])
        examination = get_rating_text(random.choices(rating_bias, rating_weights)[0])
        lab_support = get_rating_text(random.choices(rating_bias, rating_weights)[0])
        teaching_method = get_rating_text(random.choices(rating_bias, rating_weights)[0])
        library_support = get_rating_text(random.choices(rating_bias, rating_weights)[0])
        
        # Random date
        random_days = random.randint(0, 180)
        created_at = start_date + timedelta(days=random_days)
        
        row = {
            'id': i + 1,
            'student_id': random.randint(1, 50),
            'student_name': f'Student_{random.randint(1, 50)}',
            'regulation_id': random.randint(1, 3),
            'semester_id': random.randint(1, 8),
            'subject_id': random.randint(1, 20),
            'subject_name': f'Subject_{random.randint(1, 20)}',
            'teaching': teaching,
            'course_content': course_content,
            'examination': examination,
            'lab_support': lab_support,
            'teaching_method': teaching_method,
            'library_support': library_support,
            'comment': comment,
            'feedback': comment,
            'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        data.append(row)
    
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Generate sample data
    print("Generating sample student feedback data...")
    df = generate_sample_data(150)
    
    # Save to CSV
    output_file = 'sample_student_feedback.csv'
    df.to_csv(output_file, index=False)
    
    print(f"✓ Generated {len(df)} sample rows")
    print(f"✓ Saved to {output_file}")
    print(f"\nData shape: {df.shape}")
    print(f"\nColumns: {list(df.columns)}")
    print(f"\nFirst few rows:")
    print(df.head())
