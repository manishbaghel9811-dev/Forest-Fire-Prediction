import streamlit as st
import pandas as pd
import pickle

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Forest Fire Weather Index Predictor",
    page_icon="🔥",
    layout="wide"
)

# ---------------------------
# Load Model and Scaler
# ---------------------------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("scaler.pkl", "rb") as file:
        scaler = pickle.load(file)

    return model, scaler


model, scaler = load_model()

# ---------------------------
# Title
# ---------------------------
st.title("🔥 Forest Fire Weather Index Prediction")
st.write(
    "Predict the **Fire Weather Index (FWI)** using a Multiple Linear Regression model."
)

st.divider()

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("About")

st.sidebar.info(
    """
This application predicts the **Fire Weather Index (FWI)** using a
Machine Learning Multiple Linear Regression model.

Model Performance

• R² Score : 0.9848

• MAE : 0.5468
"""
)

# ---------------------------
# Input Section
# ---------------------------
st.subheader("Enter Input Features")

col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input(
        "Temperature",
        min_value=0.0,
        max_value=60.0,
        value=25.0
    )

    rh = st.number_input(
        "Relative Humidity (RH)",
        min_value=0.0,
        max_value=100.0,
        value=45.0
    )

    ws = st.number_input(
        "Wind Speed (Ws)",
        min_value=0.0,
        max_value=100.0,
        value=15.0
    )

    rain = st.number_input(
        "Rain",
        min_value=0.0,
        value=0.0
    )

    ffmc = st.number_input(
        "FFMC",
        value=85.0
    )

with col2:
    dmc = st.number_input(
        "DMC",
        value=26.0
    )

    isi = st.number_input(
        "ISI",
        value=5.0
    )

    classes = st.selectbox(
        "Fire Class",
        options=[0, 1],
        format_func=lambda x: "Not Fire" if x == 0 else "Fire"
    )

    region = st.selectbox(
        "Region",
        options=[0, 1],
        format_func=lambda x: "Bejaia" if x == 0 else "Sidi Bel-Abbes"
    )

# ---------------------------
# Prediction Button
# ---------------------------
if st.button("Predict FWI", use_container_width=True):

    input_data = pd.DataFrame(
        [[
            temperature,
            rh,
            ws,
            rain,
            ffmc,
            dmc,
            isi,
            classes,
            region
        ]],
        columns=[
            "Temperature",
            "RH",
            "Ws",
            "Rain",
            "FFMC",
            "DMC",
            "ISI",
            "Classes",
            "Region"
        ]
    )

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)

    st.success(f"🔥 Predicted Fire Weather Index (FWI): **{prediction[0]:.2f}**")

st.divider()

st.markdown(
    """
### Feature Description

| Feature | Description |
|----------|-------------|
| Temperature | Air temperature (°C) |
| RH | Relative Humidity (%) |
| Ws | Wind Speed |
| Rain | Rainfall |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| ISI | Initial Spread Index |
| Classes | Fire / Not Fire |
| Region | Bejaia / Sidi Bel-Abbes |
"""
)

st.divider()

st.caption("Developed using Streamlit | Machine Learning | Multiple Linear Regression")