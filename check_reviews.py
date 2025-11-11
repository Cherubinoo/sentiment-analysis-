"""
Check what review data is actually stored in the database
"""

from app import app, db, Review

def check_reviews():
    """Check review data in database"""
    with app.app_context():
        reviews = Review.query.limit(5).all()
        
        print(f"Found {Review.query.count()} total reviews")
        print("\nSample reviews:")
        
        for review in reviews:
            print(f"Review ID: {review.id}")
            print(f"  Teaching: {review.teaching}")
            print(f"  Course Content: {review.course_content}")
            print(f"  Examination: {review.examination}")
            print(f"  Lab Support: {review.lab_support}")
            print(f"  Teaching Method: {review.teaching_method}")
            print(f"  Library Support: {review.library_support}")
            print(f"  Comment: {review.comment}")
            print(f"  Feedback: {review.feedback}")
            print("  ---")

if __name__ == '__main__':
    check_reviews()
