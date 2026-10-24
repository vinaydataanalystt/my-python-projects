# Restaurant Sales Analysis - Streamlit App
# Run locally:  streamlit run app.py
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Restaurant Sales Analysis", layout="wide")
st.title("🍽️ Restaurant Sales Analysis")

# ---- 1. Load data ----
df = pd.read_csv("restaurant_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%Y-%m")

# ---- 2. Sidebar filters ----
st.sidebar.header("Filters")
categories = st.sidebar.multiselect(
    "Category", df["Category"].unique(), default=list(df["Category"].unique())
)
payments = st.sidebar.multiselect(
    "Payment Method", df["Payment"].unique(), default=list(df["Payment"].unique())
)

df = df[df["Category"].isin(categories) & df["Payment"].isin(payments)]

# ---- 3. Key numbers ----
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales (₹)", f"{df['Total'].sum():,}")
col2.metric("Total Orders", len(df))
col3.metric("Items Sold", int(df["Quantity"].sum()))

st.divider()

# ---- 4. Charts ----
left, right = st.columns(2)

with left:
    st.subheader("Monthly Sales")
    monthly = df.groupby("Month")["Total"].sum()
    st.line_chart(monthly)

with right:
    st.subheader("Sales by Category")
    by_category = df.groupby("Category")["Total"].sum()
    st.bar_chart(by_category)

left2, right2 = st.columns(2)

with left2:
    st.subheader("Top 5 Items")
    top_items = df.groupby("Item")["Total"].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_items)

with right2:
    st.subheader("Payment Methods")
    st.bar_chart(df["Payment"].value_counts())

# ---- 5. Raw data ----
with st.expander("Show raw data"):
    st.dataframe(df)
