"""
Test the updated analytics processing
"""

from app import app, db, Review
from preprocessing import ReviewDataProcessor, get_review_statistics

def test_analytics():
    """Test analytics with actual review data"""
    with app.app_context():
        # Get some reviews
        reviews = Review.query.limit(10).all()
        
        print(f"Testing with {len(reviews)} reviews")
        
        # Test the processor
        processor = ReviewDataProcessor()
        
        # Test average ratings
        averages = processor.calculate_average_ratings(reviews)
        print(f"\nAverage Ratings: {averages}")
        
        # Test rating distribution
        teaching_dist = processor.get_rating_distribution(reviews, 'teaching')
        print(f"\nTeaching Rating Distribution: {teaching_dist}")
        
        # Test themes
        themes = processor.extract_common_themes(reviews)
        print(f"\nCommon Themes: {themes}")
        
        # Test overall statistics
        stats = get_review_statistics(reviews)
        print(f"\nOverall Statistics:")
        print(f"  Total Reviews: {stats['total_reviews']}")
        print(f"  Satisfaction Score: {stats['overall_satisfaction']}")
        print(f"  Sentiment Distribution: {stats['sentiment_distribution']}")

if __name__ == '__main__':
    test_analytics()
