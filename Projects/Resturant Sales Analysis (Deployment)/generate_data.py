# Creates a sample restaurant sales dataset (restaurant_sales.csv)
# Run once:  python generate_data.py
import pandas as pd
import random
from datetime import date, timedelta

random.seed(42)

menu = {
    "Paneer Butter Masala": ("Main Course", 220),
    "Chicken Biryani": ("Main Course", 280),
    "Veg Biryani": ("Main Course", 200),
    "Butter Naan": ("Breads", 40),
    "Masala Dosa": ("Breakfast", 90),
    "Idli Sambar": ("Breakfast", 60),
    "Gulab Jamun": ("Dessert", 70),
    "Ice Cream": ("Dessert", 80),
    "Cold Coffee": ("Beverages", 100),
    "Masala Chai": ("Beverages", 30),
}
payments = ["Cash", "UPI", "Card"]

rows = []
start = date(2026, 1, 1)
for day in range(300):
    d = start + timedelta(days=day)
    for _ in range(random.randint(15, 35)):
        item = random.choice(list(menu))
        category, price = menu[item]
        qty = random.randint(1, 4)
        rows.append({
            "Date": d,
            "Item": item,
            "Category": category,
            "Price": price,
            "Quantity": qty,
            "Total": price * qty,
            "Payment": random.choice(payments),
        })

pd.DataFrame(rows).to_csv("restaurant_sales.csv", index=False)
print("Done! restaurant_sales.csv created with", len(rows), "rows")
