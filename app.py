import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

# -----------------------------
# TRAIN A SIMPLE MODEL
# -----------------------------
# Dummy dataset: [income, credit_score]
X = np.array([
    [20000, 300],
    [35000, 450],
    [50000, 600],
    [65000, 700],
    [80000, 750],
    [100000, 800]
])

# Labels: 0 = Not approved, 1 = Approved
y = np.array([0, 0, 1, 1, 1, 1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# -----------------------------
# STREAMlit UI
# -----------------------------
st.title("🏦 Loan Prediction App")
st.write("Enter your Income and Credit Score to predict loan approval.")

# Inputs
income = st.number_input("Enter your Monthly Income (₹)", min_value=0, value=30000)
credit_score = st.number_input("Credit Score", 300, 900, 600)

if st.button("Predict"):
    # Predict
    features = np.array([[income, credit_score]])
    prediction = model.predict(features)[0]

    # Display result
    if prediction == 1:
        st.success("🎉 Loan Approved!")
    else:
        st.error("❌ Loan Rejected!")

