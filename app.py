import streamlit as st
import pickle
import numpy as np

# --- Load Model, Scaler, and Encoders ---
with open("ada_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


# --- Streamlit UI ---
st.title("🏦 Loan Approval Prediction App")
st.write("This app predicts whether a loan will be **Approved** or **Rejected** using AdaBoost Classifier.")

st.sidebar.header("Enter Applicant Details")

no_of_dependents = st.sidebar.number_input("Number of Dependents", min_value=0, max_value=10, step=1)
education = st.sidebar.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.sidebar.selectbox("Self Employed", ["Yes", "No"])
income_annum = st.sidebar.number_input("Annual Income (₹)", min_value=0, max_value=1_00_00_000, step=50000)
loan_amount = st.sidebar.number_input("Loan Amount (₹)", min_value=0, max_value=1_00_00_000, step=10000)
loan_term = st.sidebar.number_input("Loan Term (months)",min_value=0,max_value=240)
cibil_score = st.sidebar.number_input("CIBIL Score", min_value=200, max_value=900, step=1)
residential_asset_value = st.sidebar.number_input("Residential Asset Value (₹)", min_value=0, max_value=5_00_00_000, step=50000)
commercial_assets_value = st.sidebar.number_input("Commercial Asset Value (₹)", min_value=0, max_value=5_00_00_000, step=50000)
luxury_assets_value = st.sidebar.number_input("Luxury Asset Value (₹)", min_value=0, max_value=5_00_00_000, step=50000)
bank_asset_value = st.sidebar.number_input("Bank Asset Value (₹)", min_value=0, max_value=5_00_00_000, step=50000)

# --- Encode categorical values using same encoders as training ---
education_val = 1 if education == "Graduate" else 0
self_employed_val = 1 if self_employed == "Yes" else 0


# --- Feature vector (same order as training data) ---
features = np.array([[no_of_dependents,education_val,self_employed_val,income_annum,loan_amount, loan_term, cibil_score, residential_asset_value,commercial_assets_value,luxury_assets_value,bank_asset_value]])

# --- Apply Scaling ---
features_scaled = scaler.transform(features)

# --- Prediction ---
if st.button("🔍 Predict Loan Status"):
    prediction = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]

    if prediction == 0:  # Assuming  : Approved=0, Rejected=1
        st.success(f"✅ Loan Approved (Confidence: {prob:.2f})")
    else:
        st.error(f"❌ Loan Rejected (Confidence: {prob:.2f})")


st.subheader("📌 Applicant Summary")
st.write({
    "Dependents": no_of_dependents,
    "Education": education,
    "Self Employed": self_employed,
    "Annual Income": income_annum,
    "Loan Amount": loan_amount,
    "Loan Term": loan_term,
    "CIBIL Score": cibil_score,
    "Residential Asset Value": residential_asset_value,
    "Commercial Assets Value": commercial_assets_value,
    "Luxury Assets Value": luxury_assets_value,
    "Bank Asset Value": bank_asset_value
})
