import streamlit as st
import pickle
import pandas as pd
import numpy as np

# 1. Set up the web page title and icon
st.set_page_config(
    page_title="Olist Delivery Delay Predictor", 
    page_icon="🚚",
    layout="centered"
)

st.title("🚚 Olist Delivery Delay Predictor")
st.write("""
This interactive application uses a trained Machine Learning model (Random Forest) 
to predict whether a customer's order will suffer a logistics delay based on product specs and destination.
""")

# 2. Safely load the exported model and columns list
@st.cache_resource # This caches the model so it stays in memory and runs fast!
def load_resources():
    with open('rf_delivery_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model_columns.pkl', 'rb') as f:
        columns = pickle.load(f)
    return model, columns

try:
    rf_model, model_columns = load_resources()
except FileNotFoundError:
    st.error("❌ Error: Exported model files (`rf_delivery_model.pkl` or `model_columns.pkl`) not found in the root directory! Run Cell 11 in your notebook first.")
    st.stop()

# 3. Dynamically extract unique states and categories from our 99 columns
# This saves us from hardcoding all 27 states and 70 product categories!
states = sorted([col.replace('customer_state_', '') for col in model_columns if col.startswith('customer_state_')])
categories = sorted([col.replace('product_category_name_english_', '') for col in model_columns if col.startswith('product_category_name_english_')])

# 4. Design the User Interface (Input Fields)
st.markdown("### 📦 Product Information")
col1, col2 = st.columns(2)

with col1:
    price = st.number_input("Item Price ($)", min_value=1.0, max_value=5000.0, value=50.0, step=5.0)
with col2:
    weight = st.number_input("Product Weight (grams)", min_value=1.0, max_value=50000.0, value=1000.0, step=100.0)

st.markdown("### 🗺️ Logistics & Destination")
col3, col4 = st.columns(2)

with col3:
    freight_value = st.number_input("Freight Cost / Shipping Fee ($)", min_value=0.0, max_value=500.0, value=15.0, step=1.0)
with col4:
    customer_state = st.selectbox("Destination State", options=states, index=states.index('SP') if 'SP' in states else 0)

category = st.selectbox("Product Category Group", options=categories)

# 5. Make the Prediction
st.markdown("---")
if st.button("Predict Delivery Status", type="primary"):
    
    # Create an empty template row filled with zeros matching the exact 99-column model layout
    input_data = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Map continuous inputs to the matching column slots
    input_data['price'] = price
    input_data['product_weight_g'] = weight
    input_data['freight_value'] = freight_value
    
    # Reconstruct the one-hot encoded variables by setting the chosen categories to 1
    state_column = f"customer_state_{customer_state}"
    category_column = f"product_category_name_english_{category}"
    
    if state_column in input_data.columns:
        input_data[state_column] = 1
    if category_column in input_data.columns:
        input_data[category_column] = 1
        
    # Execute the model
    prediction = rf_model.predict(input_data)[0]
    probabilities = rf_model.predict_proba(input_data)[0]
    
    # Display the result to the user
    if prediction == 1:
        st.error("⚠️ **Prediction: High Risk of Shipping Delay!**")
        st.write(f"The AI model is **{probabilities[1]*100:.1f}%** confident this package will arrive later than estimated.")
        st.info("💡 **Recommendation:** Consider coordinating with alternative regional hub fulfillment lanes or flagging for priority courier sorting.")
    else:
        st.success("✅ **Prediction: Safe Delivery Schedule**")
        st.write(f"The AI model is **{probabilities[0]*100:.1f}%** confident this package will arrive safely on time or early.")