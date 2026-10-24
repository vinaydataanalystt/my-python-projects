# AI Data Analyst - Streamlit App
# Upload any CSV file and get automatic analysis, charts and answers to your questions.
# Run locally:  streamlit run app.py
import os
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AI Data Analyst", page_icon="📊", layout="wide")
st.title("📊 AI Data Analyst")
st.write("Upload a CSV file. The app will analyse it and answer your questions.")


# ---------- Function to answer simple questions ----------
def answer_question(df, question):
    q = question.lower()

    # Find which columns are mentioned in the question
    mentioned = [c for c in df.columns if c.lower() in q]
    numeric_cols = [c for c in mentioned if pd.api.types.is_numeric_dtype(df[c])]
    text_cols = [c for c in mentioned if not pd.api.types.is_numeric_dtype(df[c])]

    # Question about number of rows
    if "how many rows" in q or "number of rows" in q:
        return f"The data has {len(df)} rows."
    if "how many columns" in q or "number of columns" in q:
        return f"The data has {len(df.columns)} columns: {', '.join(df.columns)}"

    # Missing values
    if "missing" in q or "null" in q:
        missing = df.isnull().sum()
        return "Missing values per column:\n\n" + missing.to_string()

    # Need a number column for the rest
    if not numeric_cols:
        return "I could not find a number column in your question. Try: 'total Revenue' or 'average Price by Region'."

    num = numeric_cols[0]

    # Choose the calculation
    if "average" in q or "mean" in q:
        how, name = "mean", "Average"
    elif "total" in q or "sum" in q:
        how, name = "sum", "Total"
    elif "highest" in q or "max" in q or "maximum" in q:
        how, name = "max", "Highest"
    elif "lowest" in q or "min" in q or "minimum" in q:
        how, name = "min", "Lowest"
    else:
        return "Please use words like total, average, highest or lowest. Example: 'total Revenue by Region'."

    # If a text column is mentioned, calculate for each group
    if text_cols:
        group = text_cols[0]
        result = df.groupby(group)[num].agg(how).sort_values(ascending=False)
        return f"{name} {num} by {group}:\n\n" + result.round(2).to_string()

    value = df[num].agg(how)
    return f"{name} {num} is {value:,.2f}"


# ---------- 1. Upload file ----------
uploaded = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    st.info("No file uploaded. Using the sample data.")
    folder = os.path.dirname(os.path.abspath(__file__))
    sample_path = os.path.join(folder, "sample_data.csv")
    if not os.path.exists(sample_path):
        st.error("sample_data.csv not found. Upload a CSV file or run generate_data.py first.")
        st.stop()
    df = pd.read_csv(sample_path)

# ---------- 2. Overview numbers ----------
col1, col2, col3 = st.columns(3)
col1.metric("Rows", len(df))
col2.metric("Columns", len(df.columns))
col3.metric("Missing values", int(df.isnull().sum().sum()))

numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
text_columns = df.select_dtypes(exclude=np.number).columns.tolist()

# ---------- 3. Tabs ----------
tab1, tab2, tab3, tab4 = st.tabs(["📄 Data", "📈 Summary", "📊 Charts", "💬 Ask Questions"])

with tab1:
    st.subheader("First 20 rows")
    st.dataframe(df.head(20))

with tab2:
    st.subheader("Statistics of number columns")
    if numeric_columns:
        st.dataframe(df[numeric_columns].describe())
    else:
        st.write("No number columns found.")

    st.subheader("Missing values per column")
    st.dataframe(df.isnull().sum().rename("Missing"))

    if len(numeric_columns) > 1:
        st.subheader("Correlation between number columns")
        st.dataframe(df[numeric_columns].corr().round(2))

with tab3:
    if text_columns and numeric_columns:
        st.subheader("Bar chart")
        x = st.selectbox("Group by (text column)", text_columns)
        y = st.selectbox("Calculate (number column)", numeric_columns)
        how = st.selectbox("Calculation", ["sum", "mean", "max", "min", "count"])
        chart_data = df.groupby(x)[y].agg(how)
        st.bar_chart(chart_data)

    if numeric_columns:
        st.subheader("Distribution of a number column")
        col = st.selectbox("Choose column", numeric_columns, key="hist")
        counts, edges = np.histogram(df[col].dropna(), bins=10)
        labels = [f"{edges[i]:.0f}-{edges[i + 1]:.0f}" for i in range(len(counts))]
        st.bar_chart(pd.Series(counts, index=labels))

with tab4:
    st.subheader("Ask a question about your data")
    st.caption("Examples: total Revenue | average Price by Region | highest Units by Product | missing values")
    question = st.text_input("Your question")
    if question:
        st.text(answer_question(df, question))
