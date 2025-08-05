import streamlit as st

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Levophed Rate Calculator", layout="centered")
st.title("💉 Levophed Infusion Rate Calculator")

# --- Input: Weight ---
weight = st.number_input(
    "Enter Patient Weight (kg):",
    min_value=1.0,
    max_value=300.0,
    value=70.0,
    step=0.5
)

# --- Input: Dose selection ---
dose_options = [round(x * 0.1, 1) for x in range(1, 11)]  # 0.1 to 1.0
dose = st.selectbox("Select Dose (mcg/kg/min):", options=dose_options)

# --- Input: Concentration selection ---
concentration_mg = st.selectbox(
    "Select Concentration (mg per 50 mL):",
    options=[4, 8]
)

# --- Fixed dilution volume ---
volume_ml = 50

# --- Calculation Function ---
def calculate_rate(dose, weight, volume, concentration):
    return round((dose * 60 * weight * volume) / (1000 * concentration), 2)

# --- Calculate and Display ---
rate = calculate_rate(dose, weight, volume_ml, concentration_mg)

st.success(f"💧 Infusion Rate: **{rate} mL/hr**")
st.markdown(f"➡️ Based on: {dose} mcg/kg/min, {weight} kg, {concentration_mg} mg/mL")

