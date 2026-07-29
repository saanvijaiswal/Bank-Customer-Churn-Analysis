import pandas as pd
import sqlite3


df = pd.read_csv("data/cleaned/bank_customer_cleaned.csv")

conn = sqlite3.connect("database/bank_churn1.db")

df.to_sql("customers", conn, if_exists="replace", index=False)

conn.close()

print("Data loaded successfully!")