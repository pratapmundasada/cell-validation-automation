import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. Branding & Security Title
st.set_page_config(page_title="Validation Portal", page_icon="🔋")
st.title("Pilot prject")
st.markdown("### *Automated CI/CD Telemetry Pipeline*")
st.divider()

# 2. Defensive Data Loading
FILE_NAME = 'latest_results.csv'

if os.path.exists(FILE_NAME):
    df = pd.read_csv(FILE_NAME)
    
    # KPI Row for Leadership
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Cells Tested", len(df))
    with col2:
        pass_rate = (len(df[df['status'] == 'PASS']) / len(df)) * 100 if len(df) > 0 else 0
        st.metric("Yield Rate", f"{pass_rate:.1f}%")
    with col3:
        st.metric("Active Test Stage", df['test_stage'].iloc[-1] if not df.empty else "N/A")

    # High-Level Visual for Directors
    st.subheader("Capacity Distribution (SOH Analysis)")
    fig = px.histogram(df, x="discharge_capacity_ah", color="status", 
                       title="Batch Consistency: Discharge Capacity (Ah)",
                       color_discrete_map={'PASS': '#2ecc71', 'FAIL': '#e74c3c'})
    st.plotly_chart(fig, use_container_width=True)

    # Raw Data for Engineers
    with st.expander("View Full Validation Log"):
        st.dataframe(df.style.highlight_max(axis=0, subset=['max_temp_c'], color='#ff4b4b'))

else:
    # This block prevents the "FileNotFound" crash
    st.warning("📡 System Online: Awaiting Telemetry from GitHub Pipeline...")
    st.info("The automated script has not yet committed the first dataset. Please trigger a 'Push' to the repository.")
