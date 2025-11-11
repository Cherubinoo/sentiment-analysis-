"""
Preprocessing Module for Student Sentiment Analysis
Handles data cleaning, text preprocessing, and sentiment analysis
"""

import re
import string
from textblob import TextBlob
from collections import Counter

class TextPreprocessor:
    """Text preprocessing utilities for sentiment analysis"""
    
    def __init__(self):
        self.stopwords = set([
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
            'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself',
            'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them',
            'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
            'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
            'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
            'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
            'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
            'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to',
            'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
            'further', 'then', 'once'
        ])
    
    def clean_text(self, text):
        """Clean and normalize text"""
        if not text or text == 'submitted':
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    def remove_stopwords(self, text):
        """Remove stopwords from text"""
        words = text.split()
        filtered_words = [word for word in words if word not in self.stopwords and len(word) > 2]
        return ' '.join(filtered_words)
    
    def preprocess(self, text):
        """Complete preprocessing pipeline"""
        text = self.clean_text(text)
        text = self.remove_stopwords(text)
        return text
    
    def extract_keywords(self, text, top_n=10):
        """Extract top keywords from text"""
        text = self.preprocess(text)
        words = text.split()
        word_freq = Counter(words)
        return word_freq.most_common(top_n)


class SentimentAnalyzer:
    """Enhanced sentiment analysis with detailed metrics"""
    
    def __init__(self):
        self.preprocessor = TextPreprocessor()
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of text
        Returns: dict with sentiment, polarity, subjectivity, and label
        """
        if not text or text == 'submitted':
            return {
                'sentiment': 'neutral',
                'polarity': 0.0,
                'subjectivity': 0.0,
                'label': 'neutral'
            }
        
        # Clean text
        cleaned_text = self.preprocessor.clean_text(text)
        
        # Analyze with TextBlob
        blob = TextBlob(cleaned_text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Determine sentiment label (mapped to happy/neutral/bad)
        if polarity > 0.1:
            sentiment = 'happy'
        elif polarity < -0.1:
            sentiment = 'bad'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'polarity': round(polarity, 3),
            'subjectivity': round(subjectivity, 3),
            'label': sentiment
        }
    
    def analyze_rating(self, rating_value):
        """
        Analyze sentiment based on rating scale (1-5)
        Returns sentiment category
        """
        try:
            rating = int(rating_value)
            if rating >= 4:
                return 'happy'
            elif rating == 3:
                return 'neutral'
            else:
                return 'bad'
        except:
            return 'neutral'
    
    def get_sentiment_score(self, text):
        """Get numerical sentiment score (-1 to 1)"""
        analysis = self.analyze_sentiment(text)
        return analysis['polarity']


class ReviewDataProcessor:
    """Process review data for analysis and visualization"""
    
    def __init__(self):
        self.sentiment_analyzer = SentimentAnalyzer()
        self.preprocessor = TextPreprocessor()
    
    def process_review(self, review):
        """
        Process a single review object
        Returns processed data dict
        """
        processed = {
            'id': review.id,
            'student_id': review.student_id,
            'regulation_id': review.regulation_id,
            'semester_id': review.semester_id,
            'subject_id': review.subject_id,
            'created_at': review.created_at,
        }
        
        # Process rating fields
        rating_fields = ['teaching', 'course_content', 'examination', 
                        'lab_support', 'teaching_method', 'library_support']
        
        for field in rating_fields:
            value = getattr(review, field, None)
            processed[field] = value
            processed[f'{field}_sentiment'] = self.sentiment_analyzer.analyze_rating(value)
        
        # Process text feedback
        comment = review.comment or review.feedback
        if comment and comment != 'submitted':
            sentiment_data = self.sentiment_analyzer.analyze_sentiment(comment)
            processed['comment'] = comment
            processed['comment_sentiment'] = sentiment_data['sentiment']
            processed['comment_polarity'] = sentiment_data['polarity']
            processed['comment_subjectivity'] = sentiment_data['subjectivity']
            processed['cleaned_comment'] = self.preprocessor.preprocess(comment)
        else:
            processed['comment'] = ''
            processed['comment_sentiment'] = 'neutral'
            processed['comment_polarity'] = 0.0
            processed['cleaned_comment'] = ''
        
        return processed
    
    def text_to_rating(self, text_value):
        """Convert text ratings to numeric values"""
        if not text_value:
            return 0
        
        text_value = text_value.lower().strip()
        
        # Mapping text to numeric ratings
        rating_map = {
            'excellent': 5,
            'very good': 4,
            'good': 4,
            'average': 3,
            'fair': 3,
            'poor': 2,
            'bad': 2,
            'very bad': 1,
            'terrible': 1
        }
        
        return rating_map.get(text_value, 3)  # Default to 3 if unknown
    
    def calculate_average_ratings(self, reviews):
        """Calculate average ratings for each category"""
        fields = ['teaching', 'course_content', 'examination', 'lab_support', 'teaching_method', 'library_support']
        averages = {}
        
        for field in fields:
            values = []
            for review in reviews:
                try:
                    text_value = getattr(review, field, '')
                    numeric_value = self.text_to_rating(text_value)
                    if numeric_value > 0:
                        values.append(numeric_value)
                except:
                    pass
            
            averages[field] = round(sum(values) / len(values), 2) if values else 0
        
        return averages
    
    def get_sentiment_distribution(self, reviews):
        """Get distribution of sentiments across reviews"""
        sentiments = {'happy': 0, 'neutral': 0, 'bad': 0}
        
        # Include rating text as part of the sentiment input so non-empty
        # reviews without comments still contribute to trends.
        fields = ['teaching', 'course_content', 'examination', 'lab_support', 'teaching_method', 'library_support']
        
        for review in reviews:
            comment = (review.comment or '').strip()
            # Build synthetic text from ratings (e.g., "good bad average")
            rating_tokens = []
            for f in fields:
                val = getattr(review, f, '') or ''
                if isinstance(val, str) and val.strip():
                    rating_tokens.append(val.strip())
            combined_text = ' '.join([comment] + rating_tokens).strip() or 'submitted'
            sentiment = self.sentiment_analyzer.analyze_sentiment(combined_text)['sentiment']
            if sentiment in sentiments:
                sentiments[sentiment] += 1
        
        return sentiments
    
    def get_rating_distribution(self, reviews, field='teaching'):
        """Get distribution of ratings for a specific field"""
        distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        
        for review in reviews:
            try:
                text_value = getattr(review, field, '')
                numeric_value = self.text_to_rating(text_value)
                if numeric_value in distribution:
                    distribution[numeric_value] += 1
            except:
                pass
        
        return distribution
    
    def extract_common_themes(self, reviews, top_n=15):
        """Extract common themes/keywords from review comments and ratings"""
        all_text = []
        
        for review in reviews:
            # Include comments
            comment = review.comment or review.feedback
            if comment and comment != 'submitted':
                all_text.append(comment)
            
            # Include rating text from all fields
            fields = ['teaching', 'course_content', 'examination', 'lab_support', 'teaching_method', 'library_support']
            for field in fields:
                rating_text = getattr(review, field, '')
                if rating_text and rating_text.strip():
                    all_text.append(rating_text)
        
        if not all_text:
            return []
        
        combined_text = ' '.join(all_text)
        keywords = self.preprocessor.extract_keywords(combined_text, top_n)
        
        return keywords
    
    def get_time_series_data(self, reviews):
        """Get sentiment trends over time"""
        time_data = []
        
        fields = ['teaching', 'course_content', 'examination', 'lab_support', 'teaching_method', 'library_support']
        
        for review in reviews:
            # Combine comment with rating text for better sentiment signal
            comment = (review.comment or '').strip()
            rating_tokens = []
            for f in fields:
                val = getattr(review, f, '') or ''
                if isinstance(val, str) and val.strip():
                    rating_tokens.append(val.strip())
            combined_text = ' '.join([comment] + rating_tokens).strip() or 'submitted'
            sentiment = self.sentiment_analyzer.analyze_sentiment(combined_text)
            time_data.append({
                'date': review.created_at.strftime('%Y-%m-%d'),
                'sentiment': sentiment['sentiment'],
                'polarity': sentiment['polarity']
            })
        
        return time_data


# Utility functions for quick access
def analyze_text_sentiment(text):
    """Quick function to analyze text sentiment"""
    analyzer = SentimentAnalyzer()
    return analyzer.analyze_sentiment(text)


def preprocess_text(text):
    """Quick function to preprocess text"""
    preprocessor = TextPreprocessor()
    return preprocessor.preprocess(text)


def get_review_statistics(reviews):
    """Get comprehensive statistics for a set of reviews"""
    processor = ReviewDataProcessor()
    
    stats = {
        'total_reviews': len(reviews),
        'average_ratings': processor.calculate_average_ratings(reviews),
        'sentiment_distribution': processor.get_sentiment_distribution(reviews),
        'common_themes': processor.extract_common_themes(reviews),
    }
    
    # Calculate overall satisfaction score
    avg_ratings = stats['average_ratings']
    if avg_ratings:
        overall_score = sum(avg_ratings.values()) / len(avg_ratings)
        stats['overall_satisfaction'] = round(overall_score, 2)
    else:
        stats['overall_satisfaction'] = 0
    
    return stats
