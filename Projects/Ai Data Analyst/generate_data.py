# Creates a sample dataset (sample_data.csv) to test the app
# Run once:  python generate_data.py
import pandas as pd
import random
from datetime import date, timedelta

random.seed(1)
products = {"Laptop": 55000, "Phone": 20000, "Headphones": 2500, "Keyboard": 1200, "Monitor": 9000}
regions = ["North", "South", "East", "West"]

rows = []
for day in range(180):
    d = date(2026, 1, 1) + timedelta(days=day)
    for _ in range(random.randint(3, 8)):
        product = random.choice(list(products))
        units = random.randint(1, 5)
        rows.append({
            "Date": d,
            "Product": product,
            "Region": random.choice(regions),
            "Units": units,
            "Price": products[product],
            "Revenue": units * products[product],
        })

pd.DataFrame(rows).to_csv("sample_data.csv", index=False)
print("Done! sample_data.csv created with", len(rows), "rows")
