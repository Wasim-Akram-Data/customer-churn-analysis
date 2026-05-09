# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("customers.csv")
print(df.head())

# Basic Exploration
print("Total Customers:", df.shape[0])
print(df.columns)
print(df["Churn"].value_counts())

# Data Cleaning
print(df.isnull().sum())
df.drop_duplicates(inplace=True)

# Churn Percentage
churn_rate = (df["Churn"].value_counts(normalize=True) * 100)
print(churn_rate)

# City-wise Churn
city_churn = df.groupby("City")["Churn"].value_counts()
print(city_churn)

# Subscription-wise Churn
subscription_churn = df.groupby("Subscription")["Churn"].value_counts()
print(subscription_churn)

# Average Monthly Bill
avg_bill = df.groupby("Subscription")["Monthly_Bill"].mean()
print(avg_bill)

# Age Analysis
print(df.groupby("Churn")["Age"].mean())

# Visualization
    # Churn Pie Chart
df["Churn"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.title("Customer Churn Distribution")
plt.show()
    
    # Subscription Revenue Bar Chart
df.groupby("Subscription")["Monthly_Bill"].sum().plot(kind="bar")
plt.title("Revenue by Subscription")
plt.xlabel("Subscription")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Export Cleaned Data
df.to_csv("cleaned_customers.csv", index=False)

print("Data exported successfully!")

# High Churn Customers Analysis
low_tenure = df[df["Tenure"] < 10]
print(low_tenure)

# Churn Customers Only
churn_customers = df[df["Churn"] == "Yes"]
print(churn_customers)

# Average Bill of Churn Customers
print(churn_customers["Monthly_Bill"].mean())

# Highest Paying Customers
top_customers = df.sort_values(by="Monthly_Bill",ascending=False)
print(top_customers.head())

# Multiple Aggregations
summary = df.groupby("Subscription").agg({
    "Monthly_Bill": ["mean", "sum"],
    "Tenure": "mean"
})
print(summary)

# Churn by Age Group
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[20, 30, 40, 50],
    labels=["20-30", "30-40", "40-50"]
)

# Age Group Churn Analysis
print(df.groupby("Age_Group")["Churn"].value_counts())

# Save Important Insights
summary.to_csv("subscription_summary.csv")