import pandas as pd
import numpy as np

sales = pd.read_csv("sales.csv")
products = pd.read_csv("products.csv")

print("Original Sales Data:")
print(sales)

print("\nMissing Values:")
print(sales.isnull().sum())

numeric_columns = [
    "sale_id", "store_id", "product_id",
    "quantity", "price", "cost", "discount"
]

for column in numeric_columns:
    sales[column] = pd.to_numeric(sales[column], errors="coerce")

sales = sales.dropna(subset=numeric_columns)
sales = sales.drop_duplicates(subset=["sale_id"])

sales = sales[
    (sales["quantity"] >= 0)
    & (sales["price"] >= 0)
    & (sales["cost"] >= 0)
    & (sales["discount"] >= 0)
    & (sales["discount"] <= sales["price"])
]

sales["sale_id"] = sales["sale_id"].astype(int)
sales["store_id"] = sales["store_id"].astype(int)
sales["product_id"] = sales["product_id"].astype(int)
sales["quantity"] = sales["quantity"].astype(int)

products["product_id"] = pd.to_numeric(
    products["product_id"], errors="coerce"
)
products = products.dropna(subset=["product_id"])
products["product_id"] = products["product_id"].astype(int)
products = products.drop_duplicates(subset=["product_id"])

sales["revenue"] = sales["quantity"] * sales["price"]
sales["discount_amount"] = sales["quantity"] * sales["discount"]
sales["net_revenue"] = sales["revenue"] - sales["discount_amount"]
sales["total_cost"] = sales["quantity"] * sales["cost"]
sales["profit"] = sales["net_revenue"] - sales["total_cost"]

sales["discount_percentage"] = np.where(
    sales["price"] > 0,
    sales["discount"] / sales["price"] * 100,
    0
)

sales["profit_margin"] = np.where(
    sales["net_revenue"] > 0,
    sales["profit"] / sales["net_revenue"] * 100,
    0
)

sales = sales.merge(products, on="product_id", how="left")

sales["product_name"] = sales["product_name"].fillna("Unknown Product")
sales["category"] = sales["category"].fillna("Unknown Category")

product_summary = sales.groupby(
    ["product_id", "product_name"], as_index=False
).agg(
    total_quantity=("quantity", "sum"),
    total_revenue=("net_revenue", "sum"),
    total_profit=("profit", "sum")
)

store_summary = sales.groupby(
    "store_id", as_index=False
).agg(
    total_quantity=("quantity", "sum"),
    total_revenue=("net_revenue", "sum"),
    total_profit=("profit", "sum")
)

sales.to_csv("cleaned_sales.csv", index=False)
product_summary.to_csv("product_summary.csv", index=False)
store_summary.to_csv("store_sales_summary.csv", index=False)

print("\nRevenue and Profit by Product:")
print(product_summary)

print("\nRevenue and Profit by Store:")
print(store_summary)

print("\nAll output files created successfully!")