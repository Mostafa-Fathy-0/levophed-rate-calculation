import streamlit as st

# --- Streamlit App Config ---
st.set_page_config(page_title="Levophed Calculator", layout="centered")
st.title("💉 Levophed Infusion Rate Calculator")

# --- Inputs ---
# Weight input
weight = st.number_input("Enter Patient Weight (kg):", min_value=1.0, max_value=300.0, value=70.0, step=0.5)

# Dose selection (0.1 to 1.0)
dose_options = [round(x * 0.1, 1) for x in range(1, 11)]  # 0.1 to 1.0
dose = st.selectbox("Select Dose (mcg/kg/min):", options=dose_options)

# Concentration selection (4 mg or 8 mg)
concentration_options = [4, 8]
concentration_mg = st.selectbox("Select Concentration (mg per 50 mL ampoule):", options=concentration_options)

# --- Fixed Volume ---
volume_ml = 50  # Dilution volume in mL

# --- Calculation Function ---
def calculate_rate(dose, weight, volume, concentration):
    return round((dose * 60 * weight * volume) / (1000 * concentration), 2)

# --- Calculate and Display Result ---
rate = calculate_rate(dose, weight, volume_ml, concentration_mg)

st.success(f"💧 Infusion Rate: **{rate} mL/hr**\n\nFor {dose} mcg/kg/min, {weight} kg, {concentration_mg} mg in 50 mL")
