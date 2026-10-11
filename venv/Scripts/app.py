import streamlit as st
import pandas as pd
from pathlib import Path

import numpy as np
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Customer Shopping Prediction",
    page_icon="",
    layout="wide"
)

csv_path = BASE_DIR / "Data_Science.xlsx"

st.title("Customer Shopping Prediction 🚀")

customer_df = pd.read_excel(csv_path)

# Custom CSS for modern card UI styling
st.markdown("""
<style>
    .block-container {
        padding-top: 3rem; /* Adjusts spacing above the main header */
    }
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 20px 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        font-size: 14px;
        font-weight: 600;
        color: #6c757d;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: 700;
        color: #1e293b;
    }
    .text-profit {
        color: #10b981; /* Soft Green for Profit */
    }
    .text-expense {
        color: #ef4444; /* Soft Red for Expense */
    }
</style>
""", unsafe_allow_html=True)

total_customers = customer_df['Transaction_ID'].count()
total_revenue = customer_df['Revenue'].sum()
total_expense = customer_df['Expense'].sum()
total_profit = customer_df['Profit'].sum()

# Render cards in 4 columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Total Customers</div>
        <div class="metric-value">{total_customers:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💰 Total Revenue</div>
        <div class="metric-value">₹{total_revenue:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📉 Total Expense</div>
        <div class="metric-value text-expense">₹{total_expense:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📈 Total Profit</div>
        <div class="metric-value text-profit">₹{total_profit:,.0f}</div>
    </div>
    <br/>
    """, unsafe_allow_html=True)


col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    get_product = st.text_input("Product Name")
with col2:
    get_quantity = st.text_input("How much Quantity needed?")
with col3:
    get_unit_price = st.text_input("Cost per unit")
with col4:
    get_department = st.text_input("Department")
with col5:
    get_city = st.text_input("City")
with col6:
    get_payment_method = st.text_input("Mode of Payment")

if st.button("Submit"):
    path = r'C:\MAMP\htdocs\customer_shopping_prediction_web\venv\Scripts\sales_prediction_rf_model.pkl'

    rf_loaded_model = joblib.load(path)
    
    new_data = pd.DataFrame([{
        'Quantity': get_quantity,
        'Unit_Price': get_unit_price,
        'Product': get_product,
        'City': get_city,
        'Department': get_department,
        'Payment_Method': get_payment_method
    }])

    predicted_revenue = rf_loaded_model.predict(new_data)
  
    st.success(f"Predicted Revenue: ₹{predicted_revenue[0]:,.2f}")