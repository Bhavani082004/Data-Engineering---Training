import pandas as pd
import numpy as np

shipments = pd.read_csv("shipments.csv")

shipments["cost_per_kg"] = shipments["cost"] / shipments["weight"]

shipments["cost_category"] = np.where(
    shipments["cost"] >= 1200,
    "Expensive",
    "Normal"
)

conditions = [
    (shipments["status"] == "Delivered") & (shipments["cost"] >= 1200),
    (shipments["status"] == "Delivered") & (shipments["cost"] < 1200),
    (shipments["status"] == "In Transit") & (shipments["cost"] >= 1200),
    (shipments["status"] == "In Transit") & (shipments["cost"] < 1200),
    (shipments["status"] == "Pending") & (shipments["cost"] >= 1200),
    (shipments["status"] == "Pending") & (shipments["cost"] < 1200)
]

categories = [
    "High Performance",
    "Good Performance",
    "Expensive In Transit",
    "Normal In Transit",
    "Expensive Pending",
    "Normal Pending"
]

shipments["performance_category"] = np.select(
    conditions,
    categories,
    default="Other"
)

shipments.to_csv("shipment_analysis.csv", index=False)

print(shipments)