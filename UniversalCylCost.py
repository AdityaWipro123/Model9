import streamlit as st
import numpy as np
import pandas as pd
import joblib

# === Load the trained model ===
model = joblib.load("D:/CostEstApp/Model/Model12.pkl")

# === Define encoding mappings ===
cushioning_map = {'CC': 0, 'CH': 1, 'NC': 2}
bearing_map = {'N': 0, 'Y': 1}
cyltype_map = {
    'Arm': 0, 'Boom': 1, 'Bucket': 2, 'Lift': 3,
     'Stabilizer': 4, 'Steering': 5, 'Swing': 6, 'Tilt': 7
}
mounting_map = {'TM+RE': 0,'CM+RE' : 1,'CM+RM' :2,'CC+RE' : 3,'SPL' : 4}

# === Define input headers (must match training model) ===
input_headers = [
    "Pressure", "Bore", "Rod diameter", "Stroke","Piston_Thickness","CEC_Thickness","HEC-OD","HEC_Thickness","Tube_OD","Rod_Length","Cushioning", 
    "BearingY-N","Cyl Type","Mounting"
]

st.set_page_config(page_title="Hydraulic Cost Estimator", layout="centered")
st.title("🔩 Hydraulic Cylinder Cost Estimator")

st.markdown("### Enter parameters below to predict the cost:")

# === Slider + Manual Input Function ===
def slider_with_input(label, min_val, max_val, step, default):
    col1, col2 = st.columns([3, 1])
    with col1:
        slider_val = st.slider(label, min_value=min_val, max_value=max_val, step=step, value=default, key=label+"_slider")
    with col2:
        box_val = st.number_input("Enter manually", min_value=min_val, max_value=max_val, step=step, value=slider_val, key=label+"_input")
    return box_val

# # === Numeric Inputs ===
# pressure = slider_with_input("Pressure", 100, 500, 10, 250)
# bore = slider_with_input("Bore", 10, 500, 1, 100)
# rod_dia = slider_with_input("Rod diameter", 10, 500, 1, 75)
# stroke = slider_with_input("Stroke", 100, 5000, 1, 750)
# piston_thickness = slider_with_input("Piston_Thickness", 10, 500, 1, 100)
# cec_thickness = slider_with_input("CEC_Thickness", 10, 500, 1, 100)
# hec_od = slider_with_input("HEC-OD", 10, 500, 1, 100)
# hec_thickness = slider_with_input("HEC-Thickness", 10, 500, 1, 100)
# tube_od = slider_with_input("Tube_OD", 10, 500, 1, 100)
# rod_length = slider_with_input("Rod_Length", 100, 5000, 1, 750)

# === Numeric Inputs ===
pressure = slider_with_input("Pressure", 100, 500, 10, 250)
bore = slider_with_input("Bore", 10, 500, 1, 100)
rod_dia = slider_with_input("Rod diameter", 10, 500, 1, 75)
stroke = slider_with_input("Stroke", 100, 5000, 1, 750)
piston_thickness = slider_with_input("Piston_Thickness", 10, 500, 1, 100)
cec_thickness = slider_with_input("CEC_Thickness", 10, 500, 1, 100)
hec_od = slider_with_input("HEC-OD", 10, 500, 1, 100)
hec_thickness = slider_with_input("HEC-Thickness", 10, 500, 1, 100)
tube_od = slider_with_input("Tube_OD", 10, 500, 1, 100)
rod_length = slider_with_input("Rod_Length", 100, 5000, 1, 750)


# # === Categorical Inputs ===
# cushioning = st.selectbox("Cushioning", options=list(cushioning_map.keys()))
# bearing = st.selectbox("BearingY-N", options=list(bearing_map.keys()))
# cyl_type = st.selectbox("Cyl Type", options=list(cyltype_map.keys()))
# mounting = st.selectbox("Mounting", options=list(mounting_map.keys()))
# === Categorical Inputs ===
cushioning = st.selectbox("Cushioning", options=list(cushioning_map.keys()))
bearing = st.selectbox("BearingY-N", options=list(bearing_map.keys()))
cyl_type = st.selectbox("Cyl Type", options=list(cyltype_map.keys()))
mounting = st.selectbox("Mounting", options=list(mounting_map.keys()))


# === Predict ===
if st.button("Predict Cost 💰"):
    # Prepare the input in the correct order and format
    # input_data = pd.DataFrame([[
    #     pressure, bore, rod_dia, stroke,piston_thickness,cec_thickness,hec_od,hec_thickness,tube_od, rod_length,
    #     cushioning_map[cushioning],
    #     bearing_map[bearing],
    #     cyltype_map[cyl_type], 
    #     mounting_map[mounting] 
    # ]], columns=input_headers)

    input_data = pd.DataFrame([[
        pressure, bore, rod_dia, stroke,piston_thickness,cec_thickness,hec_od,hec_thickness,tube_od, rod_length,
        cushioning_map[cushioning],
        bearing_map[bearing],
        cyltype_map[cyl_type], 
        mounting_map[mounting] 
    ]], columns=input_headers)

    # Predict
    predicted_cost = model.predict(input_data)[0]

    # Show result
    st.success(f"🧾 Estimated Cost: ₹ {predicted_cost:,.2f}")
