import pandas as pd
import matplotlib.pyplot as plt


# Create sample product sales data
data = {
    "Product": [
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Headphones",
        "Phone",
        "Tablet",
        "Charger",
        "Desk",
        "Chair",
    ],
    "Category": [
        "Electronics",
        "Accessories",
        "Accessories",
        "Electronics",
        "Accessories",
        "Electronics",
        "Electronics",
        "Accessories",
        "Furniture",
        "Furniture",
    ],
    "Price": [900, 25, 45, 250, 70, 700, 400, 30, 200, 150],
    "Units_Sold": [12, 80, 45, 20, 35, 18, 15, 60, 10, 25],
}

df = pd.DataFrame(data)

# Calculate total revenue for each product
df["Total_Revenue"] = df["Price"] * df["Units_Sold"]

print("Product Sales Data:")
print(df)

# Find the best-selling product in each category
best_selling_products = df.loc[
    df.groupby("Category")["Units_Sold"].idxmax()
]

print("\nBest-selling product in each category:")
print(best_selling_products[["Category", "Product", "Units_Sold"]])

# Calculate total revenue by category
revenue_by_category = (
    df.groupby("Category")["Total_Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal revenue by category:")
print(revenue_by_category)

# Create a bar chart
revenue_by_category.plot(
    kind="bar",
    title="Total Revenue by Category",
)

plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()