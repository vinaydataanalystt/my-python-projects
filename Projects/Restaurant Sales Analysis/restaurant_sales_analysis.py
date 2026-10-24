
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# STEP 1: CREATE THE SALES DATA (only the first time)
# ---------------------------------------------------------------
# If you have a real dataset, put it in this folder as
# restaurant_sales.csv with the same column names and skip this step.

FILE = "restaurant_sales.csv"

if not os.path.exists(FILE):
    np.random.seed(42)

    menu = {
        "Margherita Pizza": ("Main Course", 250),
        "Paneer Butter Masala": ("Main Course", 280),
        "Chicken Biryani": ("Main Course", 320),
        "Veg Burger": ("Fast Food", 150),
        "French Fries": ("Fast Food", 120),
        "Pasta": ("Main Course", 230),
        "Spring Rolls": ("Starters", 180),
        "Chicken Wings": ("Starters", 260),
        "Cold Coffee": ("Beverages", 130),
        "Fresh Lime Soda": ("Beverages", 90),
        "Chocolate Brownie": ("Desserts", 160),
        "Ice Cream": ("Desserts", 110),
    }

    items = list(menu.keys())
    n = 600
    dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0, 365, n), unit="D")
    chosen = np.random.choice(items, n)

    df = pd.DataFrame({
        "order_id": range(1001, 1001 + n),
        "date": dates,
        "item": chosen,
        "category": [menu[i][0] for i in chosen],
        "price": [menu[i][1] for i in chosen],
        "quantity": np.random.randint(1, 5, n),
        "payment_method": np.random.choice(["UPI", "Card", "Cash"], n, p=[0.5, 0.3, 0.2]),
    })
    df["total"] = df["price"] * df["quantity"]
    df = df.sort_values("date")
    df.to_csv(FILE, index=False)
    print("Sample data created:", FILE)


# ---------------------------------------------------------------
# STEP 2: LOAD THE DATA
# ---------------------------------------------------------------
print("\n===== STEP 2: LOAD THE DATA =====")
df = pd.read_csv(FILE)
df["date"] = pd.to_datetime(df["date"])

print("First 5 rows:")
print(df.head())
print("\nRows and columns:", df.shape)


# ---------------------------------------------------------------
# STEP 3: CHECK AND CLEAN THE DATA
# ---------------------------------------------------------------
print("\n===== STEP 3: CHECK THE DATA =====")
print("Missing values in each column:")
print(df.isnull().sum())

df = df.dropna()                 # remove rows with missing values
df = df.drop_duplicates()        # remove duplicate rows
print("\nRows after cleaning:", len(df))


# ---------------------------------------------------------------
# STEP 4: ADD NEW COLUMNS
# ---------------------------------------------------------------
df["month"] = df["date"].dt.month
df["day_name"] = df["date"].dt.day_name()


# ---------------------------------------------------------------
# STEP 5: BASIC NUMBERS
# ---------------------------------------------------------------
print("\n===== STEP 5: BASIC NUMBERS =====")
total_sales = df["total"].sum()
total_orders = len(df)
avg_order = df["total"].mean()

print("Total sales: Rs", round(total_sales))
print("Total orders:", total_orders)
print("Average order value: Rs", round(avg_order, 2))


# ---------------------------------------------------------------
# STEP 6: ANALYSIS
# ---------------------------------------------------------------
print("\n===== STEP 6: ANALYSIS =====")

# Top 5 items by sales
top_items = df.groupby("item")["total"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 items by sales:")
print(top_items)

# Sales by category
by_category = df.groupby("category")["total"].sum().sort_values(ascending=False)
print("\nSales by category:")
print(by_category)

# Sales by payment method
by_payment = df.groupby("payment_method")["total"].sum()
print("\nSales by payment method:")
print(by_payment)

# Sales by month
by_month = df.groupby("month")["total"].sum()
print("\nSales by month:")
print(by_month)

# Sales by day of the week
order_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_day = df.groupby("day_name")["total"].sum().reindex(order_days)
print("\nSales by day of the week:")
print(by_day)


# ---------------------------------------------------------------
# STEP 7: CHARTS
# ---------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Restaurant Sales Dashboard", fontsize=16)

# Chart 1: top items
top_items.plot(kind="barh", ax=axes[0, 0], color="orange")
axes[0, 0].set_title("Top 5 Items by Sales")
axes[0, 0].set_xlabel("Sales (Rs)")
axes[0, 0].invert_yaxis()

# Chart 2: sales by category
by_category.plot(kind="bar", ax=axes[0, 1], color="green")
axes[0, 1].set_title("Sales by Category")
axes[0, 1].set_ylabel("Sales (Rs)")
axes[0, 1].tick_params(axis="x", rotation=0)

# Chart 3: monthly sales
by_month.plot(kind="line", marker="o", ax=axes[1, 0], color="blue")
axes[1, 0].set_title("Monthly Sales")
axes[1, 0].set_xlabel("Month")
axes[1, 0].set_ylabel("Sales (Rs)")

# Chart 4: payment methods
axes[1, 1].pie(by_payment, labels=by_payment.index, autopct="%1.1f%%")
axes[1, 1].set_title("Payment Methods")

plt.tight_layout()
plt.savefig("sales_dashboard.png")
print("\nChart saved as sales_dashboard.png")


# ---------------------------------------------------------------
# STEP 8: INSIGHTS
# ---------------------------------------------------------------
print("\n===== STEP 8: INSIGHTS =====")
print("1. Best selling item:", top_items.index[0])
print("2. Best category:", by_category.index[0])
print("3. Best month: month", by_month.idxmax(), "with Rs", round(by_month.max()))
print("4. Best day:", by_day.idxmax())
print("5. Most used payment method:", by_payment.idxmax())

plt.show()