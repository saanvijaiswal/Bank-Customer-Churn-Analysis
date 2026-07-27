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

df.to_csv(
    "data/cleaned/bank_customer_cleaned.csv", index=False
)

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

# exploratory data analysis
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)
print(df_analysis['Exited'].value_counts())

churn_rate = (df_analysis['Exited'].mean())*100
print(f"Overall Customer Churn Rate : {churn_rate:.2f}%")


plt.figure(figsize=(6,4))
sns.countplot(data=df_analysis, x='Exited')
plt.title("Customer Churn Distribution")
plt.xlabel("Exited(0-Stayed, 1-Left)")
plt.ylabel("Number of Customers")
plt.show() #80% Customers stayed, 20% Customers left the bank.


print(pd.crosstab(df_analysis['Geography'], df_analysis['Exited']))
churn_by_geo = (
    df_analysis.groupby('Geography')['Exited'].mean().sort_values(ascending=False)* 100
)

plt.figure(figsize=(8,5))
sns.barplot(data=df_analysis, x= 'Geography',y='Exited',estimator='mean')
plt.title("Churn Rate by Geography")
plt.xlabel("Geography")
plt.ylabel("Churn Rate")
plt.show() #germany has twice the churn rate as that of other 2 countries


gender_churn = (df_analysis.groupby('Gender')['Exited'].mean().sort_values(ascending=False)*100)
print(gender_churn)

plt.figure(figsize=(8,5))
sns.barplot(data=df_analysis, x = 'Gender', y='Exited', estimator='mean')
plt.title("Churn rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Churn Rate")
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(data=df_analysis,x='Exited', y='Age')
plt.title("Age Distribution by Customer Churn")
plt.xlabel("Exited(0-Stayed, 1-Left)")
plt.ylabel("Age")
plt.show()

age_by_churn = df.groupby('Exited')['Age'].mean()

print(age_by_churn)

active_churn = (df_analysis.groupby('IsActiveMember')['Exited'].mean()* 100)
print(active_churn)

plt.figure(figsize=(8,5))
sns.barplot(data=df_analysis, x='IsActiveMember', y='Exited', estimator='mean')
plt.title("Churn Rate by Activeness of Member")
plt.xlabel("Active Member")
plt.ylabel("Churn Rate")
plt.show()


product_churn = (df_analysis.groupby('NumOfProducts')['Exited'].mean()*100)
print(product_churn)

plt.figure(figsize=(8,5))
sns.barplot(data=df_analysis, x='NumOfProducts', y='Exited', estimator='mean')
plt.title("Churn Rate by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Churn Rate")
plt.show()
print(df['NumOfProducts'].value_counts().sort_index())