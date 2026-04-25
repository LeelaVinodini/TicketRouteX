import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime

# --- CONFIG & THEME ---
st.set_page_config(page_title="TickRouteX v2.0", page_icon="⚡", layout="wide")

# --- CSS FOR A MODERN LOOK ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #f0f2f6; }
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] { background-image: linear-gradient(#2e3b4e, #1a242f); color: white; }
    
    /* Modern Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    /* Interactive Footer */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: rgba(255, 255, 255, 0.8);
        color: #444;
        text-align: center;
        padding: 8px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        border-top: 1px solid #ddd;
        z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CONTENT ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/854/854878.png", width=100)
    st.title("TickRouteX v2.0")
    st.markdown("---")
    app_mode = st.selectbox("Select Workspace", ["Executive Dashboard", "Route Mapping", "Analytics"])
    st.success("System: Ready")
    st.info(f"Last Sync: {datetime.now().strftime('%H:%M:%S')}")

# --- MAIN INTERFACE ---
st.title(f"🚀 {app_mode}")

if app_mode == "Executive Dashboard":
    # Top Row: KPI Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Drivers", "128", "12%")
    col2.metric("Total Deliveries", "1,450", "+85")
    col3.metric("Fuel Costs", "$4,200", "-2%")
    col4.metric("Customer Rating", "4.8/5", "0.1")

    st.markdown("---")
    
    # Mid Row: Interactive Chart
    st.subheader("Weekly Performance Trend")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Route Speed', 'Fuel Usage', 'Package Safety']
    )
    st.area_chart(chart_data)

elif app_mode == "Route Mapping":
    st.subheader("Live Spatial Tracking")
    
    # Generating mock GPS points around Hyderabad
    map_data = pd.DataFrame(
        np.random.randn(50, 2) / [50, 50] + [17.3850, 78.4867],
        columns=['lat', 'lon']
    )
    
    st.map(map_data)
    
    if st.button("Generate Optimized Path"):
        with st.status("Calculating shortest path via AI...", expanded=True) as status:
            st.write("Checking traffic patterns...")
            st.write("Cross-referencing driver availability...")
            st.write("Finalizing GPS coordinates...")
            status.update(label="Optimization Complete!", state="complete", expanded=False)
        st.balloons()

# --- THE FOOTER (REQUIRED CHANGE) ---
st.markdown(
    """
    <div class="footer">
        <b>TickRouteX</b> | Designed & Developed by <b>Leela Vinodini</b>
    </div>
    """, 
    unsafe_allow_html=True
)