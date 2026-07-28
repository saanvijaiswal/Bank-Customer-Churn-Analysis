import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("data/raw/Churn_Modelling.csv")
df_analysis = df.copy()
df_analysis = df_analysis.drop(columns=['CustomerId', 'Surname'])


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

#people exited by where they live
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

#how many people leave grouped by gender
gender_churn = (df_analysis.groupby('Gender')['Exited'].mean().sort_values(ascending=False)*100)
print(gender_churn)

plt.figure(figsize=(8,5))
sns.barplot(data=df_analysis, x = 'Gender', y='Exited', estimator='mean')
plt.title("Churn rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Churn Rate")
plt.show()

# age distribution
plt.figure(figsize=(10,6))
sns.boxplot(data=df_analysis,x='Exited', y='Age')
plt.title("Age Distribution by Customer Churn")
plt.xlabel("Exited(0-Stayed, 1-Left)")
plt.ylabel("Age")
plt.show()

age_by_churn = df.groupby('Exited')['Age'].mean()

print(age_by_churn)

#does activity of members affect them leaving
active_churn = (df_analysis.groupby('IsActiveMember')['Exited'].mean()* 100)
print(active_churn)

plt.figure(figsize=(8,5))
sns.barplot(data=df_analysis, x='IsActiveMember', y='Exited', estimator='mean')
plt.title("Churn Rate by Activeness of Member")
plt.xlabel("Active Member")
plt.ylabel("Churn Rate")
plt.show()

#does higher number of products mean customers stay
product_churn = (df_analysis.groupby('NumOfProducts')['Exited'].mean()*100)
print(product_churn)

plt.figure(figsize=(8,5))
sns.barplot(data=df_analysis, x='NumOfProducts', y='Exited', estimator='mean')
plt.title("Churn Rate by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Churn Rate")
plt.show()
print(df['NumOfProducts'].value_counts().sort_index())

#account balance by customer churn
balance_churn = df_analysis.groupby('Exited')['Balance'].mean()
print(balance_churn)
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x='Exited',
    y='Balance'
)

plt.title("Account Balance Distribution by Customer Churn")
plt.xlabel("Exited (0 = Stayed, 1 = Left)")
plt.ylabel("Account Balance")
plt.show()

#low credit score influences churn rate
credit_by_churn = df_analysis.groupby('Exited')['CreditScore'].mean()
print(credit_by_churn)

plt.figure(figsize=(8,5))
sns.boxplot(data=df_analysis, x='Exited', y='CreditScore')
plt.title("Credit Score by Churn Rate")
plt.xlabel("Exited")
plt.ylabel("Credit Score")
plt.show()

#estimated salary influences churn rate
salary_by_churn = df_analysis.groupby('Exited')['EstimatedSalary'].mean()
print(salary_by_churn)

numerical_df = df_analysis.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numerical_df.corr()
print(correlation_matrix)

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix - Numerical Features")
plt.show()

#advanced EDA
churn_geo_gender = (df_analysis.groupby(['Geography', 'Gender'])['Exited'].mean().reset_index())
churn_geo_gender['Exited'] *= 100
print(churn_geo_gender)

plt.figure(figsize=(8,5))
sns.barplot(data=churn_geo_gender, x='Geography', y='Exited', hue='Gender')
plt.title("Customer Churn by Geography & Gender")
plt.xlabel("Geography")
plt.ylabel("Churn Rate")
plt.show()

df_analysis['AgeGroup'] = pd.cut(df_analysis['Age'], bins=[18,30,40,50,60,100], labels=['18-30','31-40','41-50','51-60','60+'])
age_churn = (df_analysis.groupby('AgeGroup')['Exited'].mean().reset_index())
age_churn['Exited'] *= 100
print(age_churn)
plt.figure(figsize=(8,5))
sns.barplot(data=age_churn, x='AgeGroup',y='Exited')
plt.title("Customer Churn by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Churn Rate (%)")
plt.show()

geo_active = (df_analysis.groupby(['Geography', 'IsActiveMember'])['Exited'].mean().reset_index())
geo_active['Exited'] *= 100
print(geo_active)
plt.figure(figsize=(9,5))

sns.barplot(data=geo_active,x='Geography',y='Exited',hue='IsActiveMember')
plt.title("Churn by Geography and Active Membership")
plt.xlabel("Geography")
plt.ylabel("Churn Rate (%)")
plt.show()
