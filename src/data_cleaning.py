import pandas as pd
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

df.columns =[
    "credit_score",
    "geography",
    "gender",
    "age",
    "tenure",
    "balance",
    "num_products",
    "has_credit_card",
    "is_active_member",
    "estimated_salary",
    "exited"
]
print(df.columns)

df.to_csv(
    "data/cleaned/bank_customer_cleaned.csv", index=False
)

print("Saved Cleaned Dataset")