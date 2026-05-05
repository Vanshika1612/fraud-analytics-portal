import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="Vanshika Choudhary | Fraud Strategy Portal", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Vanshika Choudhary")
st.sidebar.caption("Fraud Strategy & Risk Analytics")
st.sidebar.write("📍 Bentonville, AR")
menu = st.sidebar.radio("Go to", ["Executive Summary", "Rule Optimization Lab", "Entity Link Analysis", "Experience"])

# --- DATA SIMULATION (To show your logic) ---
def get_rule_data(overlap_pct):
    # Simulating the 20% reduction in rule overlap impact
    rules = ['Device ID Proxy', 'Velocity Check', 'Address Mismatch', 'Email Age', 'High Value Check']
    efficiency = [85, 70, 60, 45, 90]
    overlap = [overlap_pct * (100-x)/100 for x in efficiency]
    return pd.DataFrame({'Rule': rules, 'Precision': efficiency, 'Redundancy': overlap})

# --- PAGE 1: EXECUTIVE SUMMARY ---
if menu == "Executive Summary":
    st.header("Strategic Fraud Operations Hub")
    st.markdown("#### High-Volume Transaction Risk Management")
    
    # Key Metrics from your Resume
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Weekly Volume", "5M+", "E-commerce")
    col2.metric("Monthly Exposure", "$10M+", "Secured")
    col3.metric("Rule Precision", "20% ↑", "Optimization")
    col4.metric("Risk Reduction", "30%", "Activation Logic")

    # Fraud Lifecycle Chart
    st.subheader("Fraud Classification Analysis")
    fraud_types = pd.DataFrame({
        'Category': ['Chargeback', 'Confirmed Fraud', 'Suspected Fraud', 'Return Abuse', 'False Positive'],
        'Volume': [25, 35, 20, 15, 5]
    })
    fig = px.pie(fraud_types, values='Volume', names='Category', hole=0.4, 
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 2: RULE OPTIMIZATION LAB ---
elif menu == "Rule Optimization Lab":
    st.header("Fraud Decision Engine Optimization")
    st.write("Demonstrating the impact of auditing 400+ fraud rules to improve signal precision.")
    
    overlap_slider = st.slider("Adjust Rule Overlap (Redundancy)", 0, 50, 20)
    df_rules = get_rule_data(overlap_slider)
    
    fig_rules = px.bar(df_rules, x='Rule', y=['Precision', 'Redundancy'], 
                       title="Signal vs. Noise in Decision Logic",
                       barmode='group', color_discrete_sequence=['#2ecc71', '#e74c3c'])
    st.plotly_chart(fig_rules, use_container_width=True)
    
    st.success(f"By reducing overlap to {overlap_slider}%, operational efficiency is increased by {50 - overlap_slider}%.")

# --- PAGE 3: ENTITY LINK ANALYSIS ---
elif menu == "Entity Link Analysis":
    st.header("Reflector ID Entity Framework")
    st.write("Visualizing coordinated fraud patterns through attribute aggregation.")
    
    # Image placeholder for the logic visualization
    st.info("This module simulates the identification of synthetic identities across repeated attributes.")
    
    # Simple Network simulation using Plotly
    edge_x = [1, 2, 1, 3, 1, 4]
    edge_y = [1, 2, 1, 0, 1, 1.5]
    
    node_x = [1, 2, 3, 4]
    node_y = [1, 2, 0, 1.5]
    labels = ["Reflector ID (Master)", "IP Address A", "Device ID B", "Address C"]
    
    fig_net = go.Figure(data=[go.Scatter(x=edge_x, y=edge_y, line=dict(width=2, color='#888'), hoverinfo='none', mode='lines'),
                             go.Scatter(x=node_x, y=node_y, mode='markers+text', text=labels, textposition="top center",
                                        marker=dict(size=20, color='red'))])
    fig_net.update_layout(title="Coordinated Fraud Cluster Detection", showlegend=False)
    st.plotly_chart(fig_net, use_container_width=True)

# --- PAGE 4: EXPERIENCE ---
elif menu == "Experience":
    st.header("Professional Timeline")
    st.markdown("""
    **Data Analyst — Fraud Strategy & Risk Operations | Walmart** *Oct 2025 – Present*
    - Led analytics across 5M+ weekly transactions.
    - Optimized 400+ fraud decision rules.
    
    **Data Analyst — Metaverse | Accenture** *May 2022 – Aug 2023*
    - Built churn-prediction models (Gradient Boosting, Random Forests).
    
    **Data Scientist | Zeta (Fintech)** *May 2020 – April 2022*
    - Reduced operational latency by 40%.
    """)