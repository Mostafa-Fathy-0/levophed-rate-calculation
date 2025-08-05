import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Levophed Rate Calculator", layout="centered")

# Title
st.title("💉 Levophed Infusion Rate Calculator")

# Instructions
st.markdown("Enter patient weight to calculate infusion rates for Levophed using a fixed dose range and standard concentration.")

# Input: Only weight
weight = st.number_input("Patient Weight (kg):", min_value=1.0, max_value=300.0, value=70.0, step=0.5)

# Fixed values
dose_range = [round(x * 0.1, 2) for x in range(1, 11)]  # 0.1 to 1.0
concentration_mg = 8.0
volume_ml = 50.0

# Calculation function
def calculate_rate(dose, weight, volume, concentration):
    return round((dose * 60 * weight * volume) / (1000 * concentration), 2)

# Build results table
results = []
for dose in dose_range:
    rate = calculate_rate(dose, weight, volume_ml, concentration_mg)
    results.append({
        "Dose (mcg/kg/min)": dose,
        "Infusion Rate (mL/hr)": rate
    })

df = pd.DataFrame(results)

# Show table
st.subheader("Infusion Rate Table")
st.dataframe(df)

# Optional: download as CSV
csv = df.to_csv(index=False)
st.download_button("Download Table as CSV", data=csv, file_name="levophed_rates.csv", mime="text/csv")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               