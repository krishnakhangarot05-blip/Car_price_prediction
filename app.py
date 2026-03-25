import streamlit as st
import pickle
import pandas as pd


model = pickle.load(open("car_model.pkl", "rb"))
columns = pickle.load(open("car_columns.pkl", "rb"))

st.title("Car Price Prediction")

# Inputs
year = st.number_input("Year", min_value=2000, max_value=2025)
present_price = st.number_input("Present Price")
kms_driven = st.number_input("Kms Driven")

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", [0, 1, 2, 3])

# Convert to dictionary
input_data = {
    "Year": year,
    "Present_Price": present_price,
    "Kms_Driven": kms_driven,
    "Owner": owner,
}

# Encoding (must match training)
input_data["Fuel_Type_Diesel"] = 1 if fuel_type == "Diesel" else 0
input_data["Seller_Type_Individual"] = 1 if seller_type == "Individual" else 0
input_data["Transmission_Manual"] = 1 if transmission == "Manual" else 0

# Convert to DataFrame
input_df = pd.DataFrame([input_data])


input_df = input_df.reindex(columns=columns, fill_value=0)

# Prediction
if st.button("Predict Price"):
    pred = model.predict(input_df)
    st.success(f"Estimated Price: ₹ {pred[0]:.2f} Lakhs")







