import pandas as pd

df = pd.read_csv("registrations.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df[["attendee_name", "city", "status", "amount"]])

print(df.query("status == 'Confirmed'"))

print(df.query("amount > 6000"))

print(df.query("status == 'Confirmed' and city == 'Hyderabad'"))

print(df.groupby("status").size())

print(df.groupby("status")["amount"].sum())

print(df.groupby("city")["amount"].mean())
