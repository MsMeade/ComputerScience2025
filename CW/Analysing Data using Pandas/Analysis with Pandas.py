import pandas as pd

# Step 1: Load the database (CSV file, database file, or any other format)
# In this example, I'm using a CSV file. You can change it to any database type like SQL, Excel, etc.
df = pd.read_csv('path/to/your/database.csv')  # Change path to your file

# Step 2: Data cleaning
# Clean missing values (e.g., fill or drop them)
df = df.dropna()  # Drop rows with any missing values (you can also use df.fillna() to fill them)
# You can also clean or handle any outliers here if needed, depending on your dataset.

# Step 3: Calculate statistics
# Mean
mean = df.mean()

# Median
median = df.median()

# Mode
mode = df.mode().iloc[0]  # pandas mode() can return multiple values, so we take the first one

# Range
data_range = df.max() - df.min()

# Max and Min
maximum = df.max()
minimum = df.min()

# Step 4: Print results
print("Mean:")
print(mean)

print("\nMedian:")
print(median)

print("\nMode:")
print(mode)

print("\nRange:")
print(data_range)

print("\nMaximum:")
print(maximum)

print("\nMinimum:")
print(minimum)