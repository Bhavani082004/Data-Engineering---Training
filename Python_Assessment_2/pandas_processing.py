import pandas as pd
shipments = pd.read_csv("shipments.csv")

delivered_shipments = shipments[shipments["status"] == "Delivered"]
print(delivered_shipments)

status_counts = shipments["status"].value_counts()
print(status_counts)

shipments["shipment_date"] = pd.to_datetime(shipments["shipment_date"])

shipments["month"] = shipments["shipment_date"].dt.to_period("M")
monthly_status = shipments.groupby(["month", "status"]).size().reset_index(name="count")
print(monthly_status)

average_cost = shipments.groupby("destination")["cost"].mean().reset_index(name="average_cost")
print(average_cost)

total_weight = shipments.groupby("destination")["weight"].sum().reset_index(name="total_weight")
print(total_weight)

usecols = ["shipment_id", "hub_id", "destination", "status", "cost"]
selected_shipments = pd.read_csv("shipments.csv", usecols=usecols)
print(selected_shipments)

hubs = pd.read_csv("hubs.csv")

joined_data = pd.merge(shipments, hubs, on="hub_id", how="inner")
print(joined_data)

hub_cost = joined_data.groupby(["hub_id", "hub_name"])["cost"].sum().reset_index(name="total_shipment_cost")
print(hub_cost)

hub_count = joined_data.groupby(["hub_id", "hub_name"]).size().reset_index(name="total_shipments")
print(hub_count)

hub_summary = pd.merge(hub_cost, hub_count, on=["hub_id", "hub_name"])
hub_summary = hub_summary.sort_values(by="total_shipment_cost", ascending=False)
print(hub_summary)

joined_data.to_csv("joined_shipments.csv", index=False)
hub_summary.to_csv("hub_summary.csv", index=False)
joined_data.to_json("joined_shipments.json", orient="records", indent=4, date_format="iso")
hub_summary.to_json("hub_summary.json", orient="records", indent=4, date_format="iso")