"""
Student Sentiment Analysis - Google Colab Version
Complete Data Cleaning, Preprocessing, and Visualization Pipeline
No frontend dependencies - Standalone analysis and visualization

Usage:
    1. Upload your CSV file with student feedback
    2. Run: analyzer = SentimentAnalysisColab('your_file.csv')
    3. Run: analyzer.run_complete_analysis()
"""

# ============================================================================
# IMPORTS
# ============================================================================

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Word cloud (optional)
try:
    from wordcloud import WordCloud
    WORDCLOUD_AVAILABLE = True
except ImportError:
    WORDCLOUD_AVAILABLE = False

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


# ============================================================================
# TEXT PREPROCESSING
# ============================================================================

class TextPreprocessor:
    """Text preprocessing utilities"""
    
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
        if not text or pd.isna(text) or text == 'submitted':
            return ""
        text = str(text).lower()
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def remove_stopwords(self, text):
        """Remove stopwords"""
        words = text.split()
        filtered = [w for w in words if w not in self.stopwords and len(w) > 2]
        return ' '.join(filtered)
    
    def preprocess(self, text):
        """Complete preprocessing"""
        text = self.clean_text(text)
        text = self.remove_stopwords(text)
        return text
    
    def extract_keywords(self, text, top_n=10):
        """Extract top keywords"""
        text = self.preprocess(text)
        words = text.split()
        return Counter(words).most_common(top_n)


class SentimentAnalyzer:
    """Sentiment analysis with TextBlob"""
    
    def __init__(self):
        self.preprocessor = TextPreprocessor()
    
    def analyze_sentiment(self, text):
        """Analyze sentiment"""
        if not text or pd.isna(text) or text == 'submitted':
            return {'sentiment': 'neutral', 'polarity': 0.0, 'subjectivity': 0.0}
        
        cleaned = self.preprocessor.clean_text(str(text))
        if not cleaned:
            return {'sentiment': 'neutral', 'polarity': 0.0, 'subjectivity': 0.0}
        
        blob = TextBlob(cleaned)
        polarity = blob.sentiment.polarity
        
        if polarity > 0.1:
            sentiment = 'happy'
        elif polarity < -0.1:
            sentiment = 'bad'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'polarity': round(polarity, 3),
            'subjectivity': round(blob.sentiment.subjectivity, 3)
        }


# ============================================================================
# DATA CLEANER
# ============================================================================

class DataCleaner:
    """Clean and prepare data"""
    
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.sentiment_analyzer = SentimentAnalyzer()
    
    def text_to_rating(self, text_value):
        """Convert text ratings to numeric"""
        if not text_value or pd.isna(text_value):
            return 0
        
        text_value = str(text_value).lower().strip()
        rating_map = {
            'excellent': 5, 'very good': 4, 'good': 4,
            'average': 3, 'fair': 3,
            'poor': 2, 'bad': 2,
            'very bad': 1, 'terrible': 1
        }
        return rating_map.get(text_value, 3)
    
    def clean_dataframe(self, df):
        """Clean entire dataframe"""
        print("=" * 60)
        print("DATA CLEANING IN PROGRESS...")
        print("=" * 60 + "\n")
        
        df_clean = df.copy()
        
        rating_cols = ['teaching', 'course_content', 'examination', 
                      'lab_support', 'teaching_method', 'library_support']
        
        # Convert ratings to numeric
        for col in rating_cols:
            if col in df_clean.columns:
                df_clean[f'{col}_numeric'] = df_clean[col].apply(self.text_to_rating)
        
        # Process comments
        comment_col = 'comment' if 'comment' in df_clean.columns else 'feedback'
        if comment_col in df_clean.columns:
            df_clean['cleaned_comment'] = df_clean[comment_col].apply(
                lambda x: self.preprocessor.preprocess(str(x)) if pd.notna(x) else ''
            )
            
            sentiment_results = df_clean[comment_col].apply(
                lambda x: self.sentiment_analyzer.analyze_sentiment(str(x))
            )
            
            df_clean['comment_sentiment'] = sentiment_results.apply(lambda x: x['sentiment'])
            df_clean['comment_polarity'] = sentiment_results.apply(lambda x: x['polarity'])
            df_clean['comment_subjectivity'] = sentiment_results.apply(lambda x: x['subjectivity'])
        
        # Process dates
        if 'created_at' in df_clean.columns:
            df_clean['date'] = pd.to_datetime(df_clean['created_at'])
        
        print(f"✓ Cleaned {len(df_clean)} rows")
        print("=" * 60 + "\n")
        return df_clean


# ============================================================================
# VISUALIZER
# ============================================================================

class SentimentVisualizer:
    """Create visualizations"""
    
    def __init__(self, df):
        self.df = df
    
    def plot_sentiment_distribution(self):
        """Sentiment bar chart"""
        if 'comment_sentiment' not in self.df.columns:
            return
        
        counts = self.df['comment_sentiment'].value_counts()
        colors = {'happy': '#4CAF50', 'neutral': '#FFC107', 'bad': '#F44336'}
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(counts.index, counts.values, 
                      color=[colors.get(x, '#888') for x in counts.index])
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        plt.xlabel('Sentiment', fontweight='bold')
        plt.ylabel('Count', fontweight='bold')
        plt.title('Overall Sentiment Distribution', fontweight='bold', fontsize=14)
        plt.tight_layout()
        plt.show()
    
    def plot_sentiment_pie(self):
        """Sentiment pie chart"""
        if 'comment_sentiment' not in self.df.columns:
            return
        
        counts = self.df['comment_sentiment'].value_counts()
        colors = {'happy': '#4CAF50', 'neutral': '#FFC107', 'bad': '#F44336'}
        
        plt.figure(figsize=(8, 8))
        plt.pie(counts.values, labels=counts.index,
               colors=[colors.get(x, '#888') for x in counts.index],
               autopct='%1.1f%%', startangle=90,
               textprops={'fontsize': 12, 'fontweight': 'bold'})
        plt.title('Sentiment Distribution', fontweight='bold', fontsize=14)
        plt.tight_layout()
        plt.show()
    
    def plot_average_ratings(self):
        """Average ratings bar chart"""
        rating_cols = ['teaching', 'course_content', 'examination',
                      'lab_support', 'teaching_method', 'library_support']
        
        averages = {}
        for col in rating_cols:
            num_col = f'{col}_numeric'
            if num_col in self.df.columns:
                avg = self.df[num_col][self.df[num_col] > 0].mean()
                averages[col.replace('_', ' ').title()] = avg
        
        plt.figure(figsize=(12, 6))
        bars = plt.barh(list(averages.keys()), list(averages.values()), color='#2196F3')
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width + 0.1, bar.get_y() + bar.get_height()/2.,
                    f'{list(averages.values())[i]:.2f}',
                    ha='left', va='center', fontweight='bold')
        
        plt.xlabel('Average Rating (out of 5)', fontweight='bold')
        plt.ylabel('Category', fontweight='bold')
        plt.title('Average Ratings by Category', fontweight='bold', fontsize=14)
        plt.xlim(0, 5)
        plt.tight_layout()
        plt.show()
    
    def plot_all_ratings(self):
        """All rating distributions"""
        rating_cols = ['teaching', 'course_content', 'examination',
                      'lab_support', 'teaching_method', 'library_support']
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        colors = ['#2196F3', '#4CAF50', '#FFC107', '#F44336', '#9C27B0', '#00BCD4']
        
        for idx, col in enumerate(rating_cols):
            num_col = f'{col}_numeric'
            if num_col in self.df.columns:
                counts = self.df[num_col][self.df[num_col] > 0].value_counts().sort_index()
                axes[idx].bar(counts.index, counts.values, color=colors[idx])
                axes[idx].set_title(col.replace('_', ' ').title(), fontweight='bold')
                axes[idx].set_xlabel('Rating')
                axes[idx].set_ylabel('Count')
                axes[idx].set_xticks(range(1, 6))
        
        plt.suptitle('Rating Distribution Across All Categories', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    def plot_wordcloud(self):
        """Generate word cloud"""
        if not WORDCLOUD_AVAILABLE:
            print("Install wordcloud: pip install wordcloud")
            return
        
        if 'cleaned_comment' not in self.df.columns:
            return
        
        text = ' '.join(self.df['cleaned_comment'].dropna().astype(str))
        if not text.strip():
            return
        
        wc = WordCloud(width=1200, height=600, background_color='white',
                      colormap='viridis', max_words=100).generate(text)
        
        plt.figure(figsize=(15, 8))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title('Most Common Words in Feedback', fontweight='bold', fontsize=16)
        plt.tight_layout()
        plt.show()
    
    def plot_top_keywords(self, top_n=20):
        """Top keywords bar chart"""
        if 'cleaned_comment' not in self.df.columns:
            return
        
        preprocessor = TextPreprocessor()
        text = ' '.join(self.df['cleaned_comment'].dropna().astype(str))
        keywords = preprocessor.extract_keywords(text, top_n)
        
        if not keywords:
            return
        
        words, counts = zip(*keywords)
        
        plt.figure(figsize=(12, 8))
        plt.barh(list(words), list(counts), color='#FF5722')
        plt.xlabel('Frequency', fontweight='bold')
        plt.ylabel('Keywords', fontweight='bold')
        plt.title(f'Top {top_n} Keywords', fontweight='bold', fontsize=14)
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()
    
    def plot_polarity_distribution(self):
        """Polarity histogram"""
        if 'comment_polarity' not in self.df.columns:
            return
        
        plt.figure(figsize=(12, 6))
        plt.hist(self.df['comment_polarity'].dropna(), bins=30,
                color='#3F51B5', edgecolor='black', alpha=0.7)
        plt.axvline(0, color='red', linestyle='--', linewidth=2, label='Neutral')
        plt.xlabel('Polarity Score', fontweight='bold')
        plt.ylabel('Frequency', fontweight='bold')
        plt.title('Distribution of Sentiment Polarity', fontweight='bold', fontsize=14)
        plt.legend()
        plt.tight_layout()
        plt.show()


# ============================================================================
# MAIN CLASS
# ============================================================================

class SentimentAnalysisColab:
    """Complete sentiment analysis pipeline for Colab"""
    
    def __init__(self, csv_file_path=None):
        """Initialize with optional CSV file"""
        self.df_raw = None
        self.df_clean = None
        self.cleaner = DataCleaner()
        
        if csv_file_path:
            self.load_data(csv_file_path)
    
    def load_data(self, csv_file_path):
        """Load data from CSV"""
        print(f"Loading data from {csv_file_path}...")
        self.df_raw = pd.read_csv(csv_file_path)
        print(f"✓ Loaded {len(self.df_raw)} rows\n")
        return self.df_raw
    
    def clean_data(self):
        """Clean the loaded data"""
        if self.df_raw is None:
            print("No data loaded. Use load_data() first.")
            return None
        
        self.df_clean = self.cleaner.clean_dataframe(self.df_raw)
        return self.df_clean
    
    def show_summary(self):
        """Display summary statistics"""
        if self.df_clean is None:
            print("No cleaned data. Run clean_data() first.")
            return
        
        print("\n" + "=" * 60)
        print("SUMMARY STATISTICS")
        print("=" * 60)
        print(f"\nTotal Reviews: {len(self.df_clean)}")
        
        if 'comment_sentiment' in self.df_clean.columns:
            print("\nSentiment Distribution:")
            counts = self.df_clean['comment_sentiment'].value_counts()
            for sent, count in counts.items():
                pct = (count / len(self.df_clean)) * 100
                print(f"  {sent.title()}: {count} ({pct:.1f}%)")
        
        print("\nAverage Ratings:")
        rating_cols = ['teaching', 'course_content', 'examination',
                      'lab_support', 'teaching_method', 'library_support']
        for col in rating_cols:
            num_col = f'{col}_numeric'
            if num_col in self.df_clean.columns:
                valid = self.df_clean[num_col][self.df_clean[num_col] > 0]
                if len(valid) > 0:
                    print(f"  {col.replace('_', ' ').title()}: {valid.mean():.2f}")
        
        if 'comment_polarity' in self.df_clean.columns:
            pol = self.df_clean['comment_polarity'].dropna()
            print(f"\nPolarity: Mean={pol.mean():.3f}, Std={pol.std():.3f}")
        
        print("=" * 60 + "\n")
    
    def visualize_all(self):
        """Generate all visualizations"""
        if self.df_clean is None:
            print("No cleaned data. Run clean_data() first.")
            return
        
        viz = SentimentVisualizer(self.df_clean)
        
        print("\n📊 Generating visualizations...\n")
        
        print("1. Sentiment Distribution (Bar)")
        viz.plot_sentiment_distribution()
        
        print("2. Sentiment Distribution (Pie)")
        viz.plot_sentiment_pie()
        
        print("3. Average Ratings")
        viz.plot_average_ratings()
        
        print("4. All Ratings Distribution")
        viz.plot_all_ratings()
        
        print("5. Top Keywords")
        viz.plot_top_keywords(20)
        
        print("6. Word Cloud")
        viz.plot_wordcloud()
        
        print("7. Polarity Distribution")
        viz.plot_polarity_distribution()
        
        print("\n✓ All visualizations completed!\n")
    
    def run_complete_analysis(self):
        """Run complete analysis pipeline"""
        print("\n" + "=" * 60)
        print("STARTING COMPLETE SENTIMENT ANALYSIS")
        print("=" * 60 + "\n")
        
        # Clean data
        if self.df_clean is None:
            self.clean_data()
        
        # Show summary
        self.show_summary()
        
        # Generate visualizations
        self.visualize_all()
        
        print("=" * 60)
        print("ANALYSIS COMPLETED!")
        print("=" * 60 + "\n")
        
        return self.df_clean
    
    def export_cleaned_data(self, output_path='cleaned_sentiment_data.csv'):
        """Export cleaned data to CSV"""
        if self.df_clean is None:
            print("No cleaned data to export.")
            return
        
        self.df_clean.to_csv(output_path, index=False)
        print(f"✓ Cleaned data exported to {output_path}")


# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║     STUDENT SENTIMENT ANALYSIS - GOOGLE COLAB VERSION        ║
    ╚══════════════════════════════════════════════════════════════╝
    
    USAGE:
    
    # 1. Load and analyze data
    analyzer = SentimentAnalysisColab('your_data.csv')
    analyzer.run_complete_analysis()
    
    # 2. Or step by step
    analyzer = SentimentAnalysisColab()
    analyzer.load_data('your_data.csv')
    analyzer.clean_data()
    analyzer.show_summary()
    analyzer.visualize_all()
    
    # 3. Export cleaned data
    analyzer.export_cleaned_data('output.csv')
    
    # 4. Access cleaned dataframe
    df = analyzer.df_clean
    
    ══════════════════════════════════════════════════════════════
    """)
