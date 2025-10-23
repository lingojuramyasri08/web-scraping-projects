
import pandas as pd

# Step 1: Read the Excel file
df = pd.read_excel("product_prices.xlsx")

print("\nAll scraped prices:")
print(df)

# Step 2: Find cheaper prices per product
cheaper = df.loc[df.groupby("Product")["Price"].idxmin()]

print("\nCheapest prices per product:")
print(cheaper)

# Step 3: Save comparison to a new Excel file
cheaper.to_excel("cheaper_prices.xlsx", index=False)
print("\n✅ Comparison saved to cheaper_prices.xlsx")
