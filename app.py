import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("loan_model.sav", "rb"))

st.title("🏦 Loan Prediction App")
st.write("Enter your Income and Credit Score to predict loan approval.")


income = st.number_input("Enter your Monthly Income (₹)", min_value=0, value=30000)
credit_score = st.number_input("Credit Score", 300, 900, 600)

if st.button("Predict"):
    features = np.array([[income, credit_score]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("🎉 Loan Approved!")
    else:
        st.error("❌ Loan Rejected!")

