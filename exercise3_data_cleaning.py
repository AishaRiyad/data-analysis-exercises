import pandas as pd


# Create data with intentional quality problems
data = {
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "Alice",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Helen",
        "Ivan",
    ],
    "Age": [
        25,
        30,
        None,
        25,
        "40",
        28,
        35,
        None,
        22,
        31,
    ],
    "City": [
        "New York",
        "paris",
        "BERLIN",
        "New York",
        "London",
        None,
        "PARIS",
        "berlin",
        "london",
        "NEW YORK",
    ],
    "Email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "alice@example.com",
        "david@example.com",
        None,
        "frank@example.com",
        "grace@example.com",
        "helen@example.com",
        "ivan@example.com",
    ],
}

df = pd.DataFrame(data)

print("Original data:")
print(df)

# Step 1: Remove duplicate rows
df = df.drop_duplicates()

# Step 2: Convert Age to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Step 3: Fill missing Age values with the mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Step 4: Fill missing City and Email values
df["City"] = df["City"].fillna("unknown")
df["Email"] = df["Email"].fillna("unknown")

# Step 5: Standardize text values
df["Name"] = df["Name"].str.strip().str.lower()
df["City"] = df["City"].str.strip().str.lower()
df["Email"] = df["Email"].str.strip().str.lower()

# Step 6: Convert Age to integer after cleaning
df["Age"] = df["Age"].round().astype(int)

print("\nCleaned data:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nData types after cleaning:")
print(df.dtypes)