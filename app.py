import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")

st.title("Sprinkler Prediction System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# Collect sensor inputs (scaled values)
sensor_values = []
cols = st.columns(4) 
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)


st.markdown(
    """
    <style>
    .main {
        background-color: #e6f2ff;
    }
    .stButton > button {
        background-color: #3399ff;
        color: white;
        font-weight: bold;
        padding: 0.5em 1em;
    }
    .sprinkler-on {
        color: green;
        font-weight: bold;
    }
    .sprinkler-off {
        color: red;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("### 📋 Input Summary")
summary_cols = st.columns(5)
for i, val in enumerate(sensor_values):
    with summary_cols[i % 5]:
        st.metric(label=f"Sensor {i}", value=round(val, 2))

# Predict button
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1,-1)
    prediction = model.predict(input_array)[0]

    st.markdown("### 🔎 Prediction Result")
    result_cols = st.columns(2)
    for i, status in enumerate(prediction):
        with result_cols[i % 2]:
            if status == 1:
                st.markdown(f"<div class='sprinkler-on'>Sprinkler {i} (parcel_{i}): ON</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='sprinkler-off'>Sprinkler {i} (parcel_{i}): OFF</div>", unsafe_allow_html=True)