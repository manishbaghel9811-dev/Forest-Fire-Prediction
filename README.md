# 🔥 Forest Fire Weather Index Prediction

A Machine Learning web application built using **Streamlit** that predicts the **Fire Weather Index (FWI)** based on meteorological conditions. The model was trained using **Multiple Linear Regression** and deployed on **Streamlit Community Cloud**.

---

## 🚀 Live Demo

🔗 https://forest-fire-prediction-4a9ra29rnsxowu8hkdtm7e.streamlit.app/

---

## 📌 Project Overview

The objective of this project is to predict the **Fire Weather Index (FWI)** using weather-related input features. The application provides an easy-to-use web interface where users can enter environmental conditions and receive an instant prediction.

---

## ✨ Features

- Interactive Streamlit web application
- Predicts Fire Weather Index (FWI)
- User-friendly interface
- Data preprocessing using StandardScaler
- Machine Learning model built with Multiple Linear Regression
- Deployed on Streamlit Community Cloud

---

## 📊 Machine Learning Model

**Algorithm**

- Multiple Linear Regression

**Performance**

| Metric | Score |
|--------|-------|
| R² Score | 0.9848 |
| MAE | 0.5468 |

---

## 📥 Input Features

The model uses the following nine features:

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- FFMC
- DMC
- ISI
- Fire Class
- Region

**Target Variable**

- Fire Weather Index (FWI)

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle

---

## 📂 Project Structure

```
Forest-Fire-Prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── Algerian_forest_fires_dataset_UPDATE.csv
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Forest-Fire-Prediction.git
```

Navigate to the project folder

```bash
cd Forest-Fire-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py

---

## 👨‍💻 Author

**Manish**

GitHub: https://github.com/manishbaghel9811-dev
