import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import plotly.express as px

# Load environment variables
load_dotenv()

# Get database connection string
DATABASE_URL = os.getenv("DATABASE_URL")

# Create database engine
engine = create_engine(DATABASE_URL)

@st.cache_data(ttl=600)
def load_data():
    """Load data from database"""
    query = text("SELECT * FROM fund_positions")
    return pd.read_sql(query, engine)

def main():
    st.set_page_config(page_title="Fund Positions Pivot Table", layout="wide")
    st.title("📊 Fund Positions Pivot Table")

    df = load_data()

    st.sidebar.header("Pivot Configuration")

    # Dropdowns for pivot configuration
    rows = st.sidebar.multiselect("Rows", options=df.columns.tolist(), default=["fund_name"])
    cols = st.sidebar.multiselect("Columns", options=df.columns.tolist(), default=["date"])
    values = st.sidebar.multiselect("Values", options=["quantity", "market_value"], default=["market_value"])
    aggfunc = st.sidebar.selectbox("Aggregation", options=["sum", "mean", "count", "min", "max"], index=0)

    if not values:
        st.warning("Please select at least one value to aggregate.")
        return

    try:
        pivot_table = pd.pivot_table(
            df,
            index=rows,
            columns=cols,
            values=values,
            aggfunc=aggfunc,
            fill_value=0
        )
        st.dataframe(pivot_table, use_container_width=True)

        # Optional: Show as flattened dataframe for plotting
        pivot_reset = pivot_table.reset_index()
        st.markdown("### 📈 Pivot Table Visualization")

        if len(values) == 1:
            val = values[0]
            if len(cols) == 1:
                fig = px.bar(pivot_reset, x=rows[0], y=val, color=cols[0], barmode='group')
                st.plotly_chart(fig, use_container_width=True)
            elif len(rows) == 1:
                fig = px.bar(pivot_reset, x=cols[0], y=val, color=rows[0], barmode='group')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Select only one row and one column to display a chart.")
        else:
            st.info("Select only one value to enable charting.")

    except Exception as e:
        st.error(f"Error generating pivot table: {e}")

    with st.expander("🔍 View Raw Data"):
        st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    main()