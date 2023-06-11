import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Load the dataset
df = pd.read_csv('/Users/apple/Documents/Projects/Product-recommendation/amazon.csv')

# Split the category column into main_category and sub_category
df[['main_category', 'sub_category']] = df['category'].str.split('|', 1, expand=True)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Apply the TF-IDF vectorizer on the about_product column
tfidf_matrix = tfidf_vectorizer.fit_transform(df['about_product'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Save the trained model
joblib.dump(cosine_sim, 'product_similarity.pkl')
