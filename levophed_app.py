import streamlit as st

# Fixed values
concentration_mg = 8
volume_ml = 50
doses = [0.1, 0.2, 0.3, 0.5, 1.0]  # Common dose examples in mcg/kg/min

# Title
st.title("💉 Levophed Infusion Rate Calculator")

# Input: only weight
weight = st.number_input("Enter Patient Weight (kg):", min_value=1.0, max_value=300.0, value=70.0, step=0.5)

# Function to calculate rate
def calculate_rate(dose, weight, volume, concentration):
    return round((dose * 60 * weight * volume) / (1000 * concentration), 2)

# Output results
st.subheader("Infusion Rates (mL/hr):")
for dose in doses:
    rate = calculate_rate(dose, weight, volume_ml, concentration_mg)
    st.write(f"- For {dose} mcg/kg/min: **{rate} mL/hr**")
