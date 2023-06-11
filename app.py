import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the preprocessed dataset
df = pd.read_csv('/Users/apple/Documents/Projects/Product-recommendation/preprocessed_product_data.csv')

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['about_product'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on selected category, subcategory, and rating
def get_recommendations(category, sub_category, rating, cosine_sim=cosine_sim, df=df):
    # Filter the dataset based on the selected category, subcategory, and rating
    filtered_df = df[(df['category'] == category) & (df['sub_category'] == sub_category) & (df['rating'] >= rating)]

    # Get the indices of the filtered dataset
    indices = filtered_df.index

    # Get the pairwise similarity scores of the filtered dataset
    sim_scores = cosine_sim[indices]

    # Compute the average similarity score for each product
    avg_sim_scores = sim_scores.mean(axis=1)

    # Sort the products based on the average similarity scores
    sorted_indices = avg_sim_scores.argsort()[::-1]

    # Get the top 5 recommended product indices
    top_indices = sorted_indices[:5]

    # Return the recommended products
    return df.iloc[top_indices]['product_name']


# Main app
def main():
    st.title('Product Recommendation')

    # Sidebar - Select category, subcategory, and rating
    category = st.sidebar.selectbox('Select category', df['category'].unique())
    sub_category = st.sidebar.selectbox('Select subcategory', df['sub_category'].unique())
    rating = st.sidebar.slider('Select minimum rating', 1, 5, 1)

    # Get recommendations based on user selections
    recommendations = get_recommendations(category, sub_category, rating)

    # Display recommended products
    if recommendations.empty:
        st.info('No recommendations found.')
    else:
        st.success('Top 5 Recommended Products:')
        for i, product in enumerate(recommendations):
            st.write(f'{i+1}. {product}')

if __name__ == '__main__':
    main()
