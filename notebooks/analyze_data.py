
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration
input_file = r'docs/amostrasdesafio0124 (1).xlsx'
output_dir = r'.'

# Load Data
print("--- Loading Data ---")
try:
    df = pd.read_excel(input_file)
    print("Data loaded successfully.")
except FileNotFoundError:
    print(f"Error: File not found at {input_file}")
    exit()

# Basic Info
print("\n--- Basic Information ---")
print(f"Shape: {df.shape}")
print("\nColumns and Types:")
print(df.dtypes)

print("\n--- Missing Values ---")
missing = df.isnull().sum()
print(missing[missing > 0])

# Descriptive Statistics
print("\n--- Descriptive Statistics (Numeric) ---")
print(df.describe().to_markdown())

print("\n--- Descriptive Statistics (Categorical) ---")
print(df.describe(include=['O']).to_markdown())

# Specific Analysis for Report
print("\n--- Specific Analysis ---")
if 'Rendimento Global (IRS e Rend. Isentos)' in df.columns:
    mean_income = df['Rendimento Global (IRS e Rend. Isentos)'].mean()
    median_income = df['Rendimento Global (IRS e Rend. Isentos)'].median()
    print(f"Mean Income: {mean_income:.2f}")
    print(f"Median Income: {median_income:.2f}")

if 'Escalão Etário' in df.columns:
    print("\nAge Distribution:")
    print(df['Escalão Etário'].value_counts())

if 'Nº Elem. Agregado' in df.columns:
    print("\nHousehold Size Distribution:")
    print(df['Nº Elem. Agregado'].value_counts().sort_index())

