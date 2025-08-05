import streamlit as st

# --- Fixed Parameters ---
concentration_mg = 8  # mg
volume_ml = 50        # mL

# --- Streamlit App ---
st.set_page_config(page_title="Levophed Calculator", layout="centered")
st.title("💉 Levophed Infusion Rate Calculator")

# --- User Inputs ---
weight = st.number_input("Enter Patient Weight (kg):", min_value=1.0, max_value=300.0, value=70.0, step=0.5)

dose_options = [round(x * 0.1, 1) for x in range(1, 11)]  # 0.1 to 1.0
dose = st.selectbox("Select Dose (mcg/kg/min):", options=dose_options)

# --- Calculation Function ---
def calculate_rate(dose, weight, volume, concentration):
    return round((dose * 60 * weight * volume) / (1000 * concentration), 2)

# --- Calculate & Display ---
rate = calculate_rate(dose, weight, volume_ml, concentration_mg)
st.success(f"💧 Infusion Rate: **{rate} mL/hr** for {dose} mcg/kg/min at {weight} kg")
