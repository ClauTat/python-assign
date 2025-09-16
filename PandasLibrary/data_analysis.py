# ============================
# Task 1: Load and Explore the Dataset
# ============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# --- Option A: Load dataset from sklearn (Iris dataset) ---
iris = load_iris(as_frame=True)
df = iris.frame  # already a pandas DataFrame

# --- Option B: If you want to load from CSV instead ---
# try:
#     df = pd.read_csv("your_dataset.csv")
# except FileNotFoundError:
#     print("Error: CSV file not found. Please check the filename and path.")

# Inspect first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check structure
print("\nDataset info:")
print(df.info())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Clean data (here Iris has no missing values, but we’ll show example handling)
df = df.dropna()  # or df.fillna(method="ffill")

# ============================
# Task 2: Basic Data Analysis
# ============================

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Grouping: mean petal length by species
grouped = df.groupby("target")["petal length (cm)"].mean()
print("\nAverage petal length per species:")
print(grouped)

# Identify patterns
print("\nInteresting Finding:")
print("We see that setosa has a much smaller petal length compared to versicolor and virginica.")

# ============================
# Task 3: Data Visualization
# ============================

# 1. Line chart - trend over samples (index as x-axis)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="target", y="petal length (cm)", data=df, estimator="mean", errorbar=None)
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species (0=setosa, 1=versicolor, 2=virginica)")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram: Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - sepal length vs petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df, palette="deep")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
