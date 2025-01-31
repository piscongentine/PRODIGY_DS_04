import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Ensure necessary NLTK resources are downloaded
nltk.download('vader_lexicon')

# Load the dataset
file_path = r"C:\Users\bhara\OneDrive\Pictures\Desktop\bklkal\twitter_training.csv"
df = pd.read_csv(file_path, encoding="utf-8", header=None)
df.columns = ["ID", "Topic", "Sentiment", "Tweet"]

# Drop rows with missing tweets
df = df.dropna(subset=['Tweet'])

# Convert all tweets to string
df['Tweet'] = df['Tweet'].astype(str)

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

def get_sentiment_score(text):
    """Calculate sentiment polarity score using VADER."""
    return sia.polarity_scores(text)['compound']

# Apply sentiment analysis
df['Sentiment Score'] = df['Tweet'].apply(get_sentiment_score)

# Visualizing sentiment distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Sentiment', data=df, palette='coolwarm')
plt.title('Sentiment Distribution')
plt.text(0.5, max(df['Sentiment'].value_counts()) * 0.9, 'Piscongentine_man', fontsize=12, ha='center', color='black')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Generate a Word Cloud for Positive Sentiments
positive_tweets = ' '.join(df[df['Sentiment'] == 'Positive']['Tweet'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(positive_tweets)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud for Positive Tweets")
plt.text(400, 50, 'Piscongentine_man', fontsize=12, ha='center', color='black')
plt.show()

# Displaying sentiment trends over topics
plt.figure(figsize=(12, 6))
sns.boxplot(x='Sentiment', y='Sentiment Score', data=df)
plt.title('Sentiment Score Distribution by Sentiment Label')
plt.text(0.5, max(df['Sentiment Score']) * 0.9, 'Piscongentine_man', fontsize=12, ha='center', color='black')
plt.show()

# Display the first few rows
df.head()

