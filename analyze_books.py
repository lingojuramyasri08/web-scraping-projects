import pandas as pd

# Read the scraped data
df = pd.read_csv("books.csv")

# Show first 5 rows
print("First few records:")
print(df.head())

# Find average price
df['Price'] = (
    df['Price']
    .str.replace('Â', '', regex=False)
    .str.replace('£', '', regex=False)
    .astype(float)
)
print("\nAverage Book Price:", df['Price'].mean())

# Top 5 most expensive books
print("\nTop 5 Expensive Books:")
print(df.sort_values(by='Price', ascending=False).head())
