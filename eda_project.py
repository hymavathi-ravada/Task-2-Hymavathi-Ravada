# ============================================
# PROJECT 2 - EXPLORATORY DATA ANALYSIS (EDA)
# Internship Project
# ============================================

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------
# STEP 1: LOAD THE DATASET
# --------------------------------------------

# Load Excel dataset
df = pd.read_excel("cleaned_dataset.xlsx")

# Display first 5 rows
print("\n========== FIRST 5 RECORDS ==========\n")
print(df.head())

# Dataset shape
print("\n========== DATASET SHAPE ==========\n")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# Column names
print("\n========== COLUMN NAMES ==========\n")
print(df.columns)


# --------------------------------------------
# STEP 2: DATA CLEANING
# --------------------------------------------

print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())

# Fill missing coupon codes
df['couponcode'] = df['couponcode'].fillna('No coupon')

# Check missing values again after cleaning
print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# Convert Date column into datetime format
df['date'] = pd.to_datetime(df['date'])

# Check duplicate records
print("\n========== DUPLICATE RECORDS ==========\n")
print(df.duplicated().sum())


# --------------------------------------------
# STEP 3: BASIC STATISTICS
# --------------------------------------------

print("\n========== BASIC STATISTICS ==========\n")
print(df.describe())

# Mean, Median and Count
print("\n========== CUSTOM STATISTICS ==========\n")

print(f"Average Quantity Sold : {df['quantity'].mean():.2f}")
print(f"Median Quantity Sold  : {df['quantity'].median()}")

print(f"\nAverage Unit Price    : {df['unitprice'].mean():.2f}")
print(f"Median Unit Price     : {df['unitprice'].median():.2f}")

print(f"\nAverage Total Price   : {df['totalprice'].mean():.2f}")
print(f"Median Total Price    : {df['totalprice'].median():.2f}")

print(f"\nTotal Orders          : {df['orderid'].count()}")


# --------------------------------------------
# STEP 4: PRODUCT ANALYSIS
# --------------------------------------------

print("\n========== TOP SELLING PRODUCTS ==========\n")

top_products = df.groupby('product')['quantity'].sum().sort_values(ascending=False)

print(top_products)

# Visualization
plt.figure(figsize=(10,5))
top_products.plot(kind='bar')

plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Total Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# --------------------------------------------
# STEP 5: PAYMENT METHOD ANALYSIS
# --------------------------------------------

print("\n========== PAYMENT METHOD USAGE ==========\n")

payment_analysis = df['paymentmethod'].value_counts()

print(payment_analysis)

# Pie Chart
plt.figure(figsize=(7,7))
plt.pie(payment_analysis,
        labels=payment_analysis.index,
        autopct='%1.1f%%')

plt.title("Payment Method Distribution")
plt.show()


# --------------------------------------------
# STEP 6: ORDER STATUS ANALYSIS
# --------------------------------------------

print("\n========== ORDER STATUS ==========\n")

status_analysis = df['orderstatus'].value_counts()

print(status_analysis)

# Bar Chart
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='orderstatus')

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Count")
plt.show()


# --------------------------------------------
# STEP 7: MONTHLY SALES TREND
# --------------------------------------------

# Extract month from Date
df['Month'] = df['date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['totalprice'].sum()

print("\n========== MONTHLY SALES TREND ==========\n")
print(monthly_sales)

# Line Plot
plt.figure(figsize=(12,5))

monthly_sales.plot(marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)

plt.show()


# --------------------------------------------
# STEP 8: OUTLIER DETECTION
# --------------------------------------------

print("\n========== OUTLIER DETECTION ==========\n")

# Boxplot for TotalPrice
plt.figure(figsize=(8,5))

sns.boxplot(x=df['totalprice'])

plt.title("Outlier Detection - Total Price")

plt.show()

# Identify Outliers using IQR Method

Q1 = df['totalprice'].quantile(0.25)
Q3 = df['totalprice'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df['totalprice'] < lower_limit) |
    (df['totalprice'] > upper_limit)
]

print(f"Total Outliers Found : {len(outliers)}")

print("\nTop Outlier Records:\n")
print(outliers[['orderid', 'product', 'totalprice']].head())


# --------------------------------------------
# STEP 9: CORRELATION ANALYSIS
# --------------------------------------------

print("\n========== CORRELATION MATRIX ==========\n")

correlation = df[['quantity', 'unitprice',
                  'itemsincart', 'totalprice']].corr()

print(correlation)

# Heatmap
plt.figure(figsize=(8,5))

sns.heatmap(correlation,
            annot=True,
            cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.show()


# --------------------------------------------
# STEP 10: KEY OBSERVATIONS
# --------------------------------------------

print("\n========== KEY OBSERVATIONS ==========\n")

print("""
1. The dataset contains customer order details and sales information.

2. Monthly sales trend helps identify high revenue periods.

3. Some products have significantly higher sales quantity.

4. Multiple outliers exist in TotalPrice indicating unusually high-value orders.

5. Correlation analysis shows how Quantity and UnitPrice affect TotalPrice.

6. Payment methods and order statuses reveal customer purchasing behavior.

7. Visualization makes trend analysis easier and improves business understanding.
""")


# --------------------------------------------
# STEP 11: FINAL CONCLUSION
# --------------------------------------------

print("\n========== FINAL CONCLUSION ==========\n")

print("""
Exploratory Data Analysis (EDA) was successfully performed on the dataset.
The project identified sales trends, customer behavior, top-selling products,
outliers, and important statistical insights using Python libraries such as
Pandas, Matplotlib, and Seaborn.

This analysis helps businesses make data-driven decisions and improve sales strategies.
""")