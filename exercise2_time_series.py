import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create daily dates for one month
dates = pd.date_range(start="2026-07-01", periods=31, freq="D")

# Generate reproducible random sales values
rng = np.random.default_rng(seed=42)
sales = rng.integers(low=100, high=500, size=len(dates))

# Create the DataFrame
df = pd.DataFrame(
    {
        "Date": dates,
        "Sales": sales,
    }
)

# Ensure the Date column uses datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Calculate the 7-day moving average
df["Moving_Average_7_Days"] = df["Sales"].rolling(window=7).mean()

# Add the day name for each date
df["Day_of_Week"] = df["Date"].dt.day_name()

print("Monthly Sales Data:")
print(df)

# Find the day of the week with the highest average sales
average_sales_by_day = (
    df.groupby("Day_of_Week")["Sales"]
    .mean()
    .sort_values(ascending=False)
)

highest_average_day = average_sales_by_day.index[0]
highest_average_sales = average_sales_by_day.iloc[0]

print("\nAverage sales by day of the week:")
print(average_sales_by_day)

print(
    f"\nDay with highest average sales: "
    f"{highest_average_day} ({highest_average_sales:.2f})"
)

# Plot original sales and the moving average
plt.figure(figsize=(12, 6))

plt.plot(
    df["Date"],
    df["Sales"],
    marker="o",
    label="Daily Sales",
)

plt.plot(
    df["Date"],
    df["Moving_Average_7_Days"],
    linewidth=2,
    label="7-Day Moving Average",
)

plt.title("Daily Sales and 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()