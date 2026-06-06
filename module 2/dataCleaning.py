# ============================================================
# EMPLOYMENT INDIA DATASET - DATA CLEANING PROJECT
# ============================================================

# Step 1: Load and Inspect Dataset
# Purpose: Load dataset and view initial records

import os
from pathlib import Path

import pandas as pd
import numpy as np

script_dir = Path(__file__).resolve().parent
input_path = script_dir / "Messy_Employment_India_Dataset.csv"
output_path = script_dir / "Cleaned_Employment_India_Dataset.csv"

df = pd.read_csv(input_path)

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# ============================================================
# Step 2: Understand Structure and Data Types
# Purpose: Check columns, data types and summary statistics
# ============================================================

print("\nDataset Information:")
df.info()

print("\nSummary Statistics:")
print(df.describe(include="all"))


# ============================================================
# Step 3: Handle Missing Values
# Purpose: Find and fill missing values
# ============================================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill numeric columns with median
for col in df.select_dtypes(include="number"):
    df[col] = df[col].fillna(df[col].median())

# Fill text columns with mode
for col in df.select_dtypes(include=["object", "string"]):
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ============================================================
# Step 4: Remove Duplicate Records
# Purpose: Remove repeated rows
# ============================================================

print("\nDuplicate Rows Before Cleaning:")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicate Rows After Cleaning:")
print(df.duplicated().sum())

# ============================================================
# Step 5: Correct Inconsistent Formatting
# Purpose: Standardize text values
# ============================================================

for col in df.select_dtypes(include=["object", "string"]):
    df[col] = df[col].str.strip().str.lower()

print("\nText Formatting Standardized")

# ============================================================
# Step 6: Fix Data Type Issues
# Purpose: Convert incorrect data types if needed
# ============================================================

print("\nCurrent Data Types:")
print(df.dtypes)

# Convert Date Recorded to datetime format
df["Date Recorded"] = pd.to_datetime(df["Date Recorded"], errors="coerce")

# Ensure numeric columns are numeric
df["Years of Experience"] = pd.to_numeric(
    df["Years of Experience"], errors="coerce"
)

df["Monthly Salary (INR)"] = pd.to_numeric(
    df["Monthly Salary (INR)"], errors="coerce"
)

print("\nUpdated Data Types:")
print(df.dtypes)

# ============================================================
# Step 7: Detect and Handle Outliers
# Purpose: Handle extreme values using IQR method
# ============================================================

for col in df.select_dtypes(include="number"):

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    #If value < lower bound replace it with lower bound otherwise keep original value
    df[col] = np.where(df[col] < lower, lower, df[col])
    #If value > upper bound replace it with upper bound otherwise keep original value
    df[col] = np.where(df[col] > upper, upper, df[col])

print("\nOutliers Handled")

# ============================================================
# Step 8: Rename and Standardize Column Names
# Purpose: Make column names consistent
# ============================================================

df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

print("\nStandardized Column Names:")
print(df.columns.tolist())

# ============================================================
# Step 9: Validate Cleaned Data
# Purpose: Verify dataset quality
# ============================================================

print("\nFinal Validation")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDataset Shape:")
print(df.shape)

print("\nFinal Data Types:")
print(df.dtypes)

# ============================================================
# Step 10: Export Final Cleaned Dataset
# Purpose: Save cleaned dataset
# ============================================================

df.to_csv(output_path, index=False)

print(f"\nCleaned Dataset Exported Successfully to: {output_path}")
