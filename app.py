import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("car_model.pkl", "rb"))

st.title("Car Price Prediction")

st.write("Enter car details:")


year = st.number_input("Year", min_value=2000, max_value=2025)
present_price = st.number_input("Present Price")
kms_driven = st.number_input("Kms Driven")

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner", [0, 1, 2, 3])

# Convert categorical to numeric
fuel_type = 1 if fuel_type == "Diesel" else 0
seller_type = 1 if seller_type == "Individual" else 0
transmission = 1 if transmission == "Manual" else 0

# Prediction
if st.button("Predict Price"):
    data = np.array([[year, present_price, kms_driven,
                      fuel_type, seller_type, transmission, owner]])

    prediction = model.predict(data)
    
    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")



















