import streamlit as st
import pandas as pd
import pickle as pk
from streamlit_lottie import st_lottie
import requests
import json

# Load the model and scaler
model = pk.load(open('model.pkl', 'rb'))
scaler = pk.load(open('scaler.pkl', 'rb'))

# Function to load Lottie animations from a URL
def load_lottie(url: str):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to load animation from {url}")
            return None
    except Exception as e:
        st.error(f"Error fetching Lottie animation: {e}")
        return None

# Alternative: Function to load Lottie animations locally
def load_lottie_local(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Failed to load JSON file {filepath}: {e}")
        return None

       
approved_animation = load_lottie_local("assets/approved.json")
rejected_animation = load_lottie_local("assets/rejected.json")
ai_animation = load_lottie_local("assets/aianimation.json")
# Load animations (replace with local files if needed)
#ai_animation = load_lottie("https://assets7.lottiefiles.com/packages/lf20_jcikwtux.json")


# App title and header
st.title("🏦 Loan Approval Prediction App")
st.markdown("### Streamlined predictions for banks and financial institutions! 🚀")

# AI animation
if ai_animation:
    st_lottie(ai_animation, height=200, key="ai_animation")

# Sidebar inputs
st.sidebar.header("🔍 Input Customer Details")
no_of_dep = st.sidebar.slider("Number of Dependents", 0, 5, step=1)
grad = st.sidebar.selectbox("Education Level", ["Graduated", "Not Graduated"])
self_emp = st.sidebar.selectbox("Self-Employed?", ["Yes", "No"])
annual_income = st.sidebar.number_input("Annual Income (in ₹)", min_value=0, step=100000)
loan_amount = st.sidebar.number_input("Loan Amount (in ₹)", min_value=0, step=100000)
loan_dur = st.sidebar.slider("Loan Duration (in years)", 1, 30, step=1)
cibil_score = st.sidebar.slider("CIBIL Score", 300, 900, step=1)
assets = st.sidebar.number_input("Total Assets Value (in ₹)", min_value=0, step=100000)

# Convert categorical inputs
grad_s = 0 if grad == "Graduated" else 1
emp_s = 0 if self_emp == "No" else 1

# Prediction button
if st.sidebar.button("Predict Loan Status"):
    pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, annual_income, loan_amount, loan_dur, cibil_score, assets]], 
                             columns=["no_of_dependents", "education", "self_employed", "income_annum", "loan_amount", "loan_term", "cibil_score", "Assets"])
    pred_scaled_data = scaler.transform(pred_data)
    prediction = model.predict(pred_scaled_data)
    
    st.write("### Loan Prediction Result:")
    if prediction[0] == 1:
        st.success("Congratulations! The Loan is Approved ✅")
        if approved_animation:
            st_lottie(approved_animation, height=200, key="approved_animation")
        else:
            st.markdown("✔️ Loan Approved!")
    else:
        st.error("Sorry! The Loan is Rejected ❌")
        if rejected_animation:
            st_lottie(rejected_animation, height=200, key="rejected_animation")
        else:
            st.markdown("❌ Loan Rejected!")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center;">
        <p>Developed with ❤️ by <b>Subhankar Maji</b></p>
        <p>📫 Connect with me on <a href="https://www.linkedin.com/in/subhankar-maji-7aba49238" target="_blank">LinkedIn</a> | <a href="https://github.com/subhankamaji12" target="_blank">GitHub</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)
