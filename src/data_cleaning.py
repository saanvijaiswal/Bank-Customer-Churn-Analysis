import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("data/raw/Churn_Modelling.csv")


print("\nDataset Summary:")
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

print("\nFinding Out Messy Data Parts:")
print(df.isnull().sum())
print(df.duplicated().sum())

#dataset categorical info
print(df.describe())
print(df.describe(include='str'))

df = df.drop(columns=[
    "RowNumber",
    "CustomerId",
    "Surname"
])

print(df.head())

df.to_csv("data/cleaned/bank_customer_cleaned.csv", index=False)

print("Saved Cleaned Dataset")


# feature engineering
numerical_cols = df.select_dtypes(include=['int64', 'float64'])
numerical_cols.hist(figsize=(15,10))
plt.show()


categorical_cols = df.select_dtypes(include='str')
print(categorical_cols.columns)

for col in categorical_cols.columns:
    print("f\n{col}")
    print(df[col].value_counts())
    print("-" * 40)

df_analysis = df.copy()
df_analysis = df_analysis.drop(columns=['CustomerId', 'Surname'])
print(df_analysis.columns)

