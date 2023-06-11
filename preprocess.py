import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/apple/Documents/Projects/Product-recommendation/amazon.csv')

# Preprocessing steps
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['sub_category'] = df['category'].apply(lambda x: x.split('|')[1] if '|' in x else x)
df['category'] = df['category'].apply(lambda x: x.split('|')[0] if '|' in x else x)
df['actual_price'] = df['actual_price'].str.replace('[^\d.]', '', regex=True).astype(float)
df['discounted_price'] = df['discounted_price'].str.replace('[^\d.]', '', regex=True).astype(float)
df['discount_percentage'] = (df['actual_price'] - df['discounted_price']) / df['actual_price'] * 100

# Save the preprocessed dataset
df.to_csv('preprocessed_product_data.csv', index=False)
