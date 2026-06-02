# ==========================================
# DATA CLEANING & VISUALIZATION PROJECT
# Student Performance Dataset
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("student-mat.csv", sep=';')

# ==========================================
# DATA EXPLORATION
# ==========================================

print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ==========================================
# DATA CLEANING
# ==========================================

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Records
duplicates = df.duplicated().sum()
print("\nDuplicate Records:", duplicates)

# Remove Duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Cleaning:", df.shape)

# ==========================================
# VISUALIZATION 1
# Gender Distribution
# ==========================================

plt.figure(figsize=(6, 4))
sns.countplot(x='sex', data=df)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

# ==========================================
# VISUALIZATION 2
# Age Distribution
# ==========================================

plt.figure(figsize=(8, 5))
plt.hist(df['age'], bins=8)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Students")
plt.show()

# ==========================================
# VISUALIZATION 3
# Study Time vs Final Grade
# ==========================================

plt.figure(figsize=(8, 5))
sns.boxplot(x='studytime', y='G3', data=df)
plt.title("Study Time vs Final Grade")
plt.xlabel("Study
