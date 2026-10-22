import pandas as pd

customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")

customers.columns = customers.columns.str.strip()
orders.columns = orders.columns.str.strip()

merged = pd.merge(
    orders,
    customers,
    on="customer_id",
    how="inner"
)

merged["order_value"] = merged["quantity"] * merged["unit_price"]

print(merged[
    ["order_id", "customer_name", "city", "product", "status", "order_value"]
])

delivered_hyderabad = merged[
    (merged["status"].str.strip().str.lower() == "delivered") &
    (merged["city"].str.strip().str.lower() == "hyderabad")
]

print(delivered_hyderabad[
    ["order_id", "customer_name", "city", "product", "status", "order_value"]
])

city_summary = merged.groupby("city").agg(
    total_orders=("order_id", "count"),
    total_sales=("order_value", "sum"),
    average_order_value=("order_value", "mean")
).reset_index()

city_summary = city_summary.sort_values(
    by="total_sales",
    ascending=False
)

print(city_summary)

city_summary.to_csv("city_sales_summary.csv", index=False)

city_summary.to_json(
    "city_sales_summary.json",
    orient="records",
    indent=4
)



