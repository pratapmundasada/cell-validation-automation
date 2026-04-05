import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Cell Validation Dashboard", layout="wide")
st.title("🔋 Cell Validation Live Results")

# Load the processed data
df = pd.read_csv("processed_results.csv")

# Metric Row
col1, col2, col3 = st.columns(3)
col1.metric("Total Cells", len(df))
col2.metric("Avg Voltage", f"{df['voltage'].mean():.2f}V")
col3.metric("Failures", len(df[df['temp_c'] > 60]))

# Visualization
fig = px.scatter(df, x="voltage", y="temp_c", color="temp_c",
                 color_continuous_scale="RdYlGn_r",
                 title="Temperature vs Voltage Validation")
st.plotly_chart(fig, use_container_width=True)

st.write("### Raw Validation Data", df)
