import pandas as pd
import numpy as np

customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")

customers.columns = customers.columns.str.strip()
orders.columns = orders.columns.str.strip()

merged = pd.merge(orders, customers, on="customer_id", how="inner")

merged["order_value"] = merged["quantity"] * merged["unit_price"]

merged["order_size"] = np.select(
    [
        merged["order_value"] >= 50000,
        merged["order_value"] >= 15000
    ],
    [
        "High",
        "Medium"
    ],
    default="Low"
)

merged["priority_customer"] = np.where(
    merged["segment"] == "Corporate",
    "Priority",
    "Normal"
)

merged.to_csv("enriched_orders.csv", index=False)

print(merged)
