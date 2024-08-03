import streamlit as st
import joblib

# Title of the application
st.title("Smart Watch Prediction App")

# Header
st.header("Estimate the price of your Smart Watch.")

# Subheader
st.subheader("Welcome to our Smart Watch Price Estimator! This application allows you to estimate the market value of your smart watch based on various features.")

st.image("Smart.jpg", caption="Smart Watch", width=600)

st.write("Simply select the brand, model, operating system, connectivity, display type, resolution, water resistance, and input the battery life, heart rate monitor, GPS, and NFC details. Once you have filled out all the fields, click on the 'Predict' button to get an estimated price for your smartwatch. This tool provides an approximate market value of your smartwatch, helping you make informed decisions whether you're buying, selling, or just curious about its worth in the current market.")

top_12_feature_names = joblib.load("top_12_feature_names.joblib")

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Örnek veriler
brands = ['Apple', 'Samsung', 'Garmin']
models = ['Watch Series 7', 'Galaxy Watch 4', 'Forerunner 945']
operating_systems = ['watchOS', 'Wear OS', 'Garmin OS']
connectivities = ['Bluetooth, Wi-Fi', 'Bluetooth', 'Wi-Fi']
display_types = ['Retina', 'AMOLED', 'LCD']
resolutions = ['396x484', '360x360', '240x240']
water_resistances = ['50', '30', '10']
heart_rate_monitors = ['Yes', 'No']
gps_options = ['Yes', 'No']
nfc_options = ['Yes', 'No']

# LabelEncoder nesnelerini hazırlama
le_dict = {
    'Brand': LabelEncoder().fit(brands),
    'Model': LabelEncoder().fit(models),
    'Operating System': LabelEncoder().fit(operating_systems),
    'Connectivity': LabelEncoder().fit(connectivities),
    'Display Type': LabelEncoder().fit(display_types),
    'Resolution': LabelEncoder().fit(resolutions),
    'Water Resistance (meters)': LabelEncoder().fit(water_resistances),
    'Heart Rate Monitor': LabelEncoder().fit(heart_rate_monitors),
    'GPS': LabelEncoder().fit(gps_options),
    'NFC': LabelEncoder().fit(nfc_options)
}

def predict_price(features):
    # Basit bir tahmin modeli
    base_price = 200  # Temel bir başlangıç fiyatı

    # Özelliklerin fiyat üzerindeki etkileri
    brand_price = features['Brand'] * 10
    model_price = features['Model'] * 5
    os_price = features['Operating System'] * 15
    connectivity_price = features['Connectivity'] * 8
    display_type_price = features['Display Type'] * 12
    resolution_price = features['Resolution'] * 20
    water_resistance_price = features['Water Resistance (meters)'] * 2
    battery_life_price = features['Battery Life (days)'] * 3
    heart_rate_monitor_price = 50 if features['Heart Rate Monitor'] == 1 else 0
    gps_price = 40 if features['GPS'] == 1 else 0
    nfc_price = 30 if features['NFC'] == 1 else 0

    # Toplam tahmin fiyatı
    predicted_price = base_price + brand_price + model_price + os_price + connectivity_price + display_type_price + resolution_price + water_resistance_price + battery_life_price + heart_rate_monitor_price + gps_price + nfc_price

    return predicted_price

st.title('Smartwatch Price Prediction Tool')

# Kullanıcıdan veri girişi
brand = st.selectbox('Brand', brands)
model = st.selectbox('Model', models)
operating_system = st.selectbox('Operating System', operating_systems)
connectivity = st.selectbox('Connectivity', connectivities)
display_type = st.selectbox('Display Type', display_types)
resolution = st.selectbox('Resolution', resolutions)
water_resistance = st.selectbox('Water Resistance (meters)', water_resistances)
battery_life = st.slider('Battery Life (days)', min_value=1, max_value=30, value=18)
heart_rate_monitor = st.selectbox('Heart Rate Monitor', heart_rate_monitors)
gps = st.selectbox('GPS', gps_options)
nfc = st.selectbox('NFC', nfc_options)

# Kullanıcı verilerini DataFrame formatına dönüştürme
input_data = {
    'Brand': le_dict['Brand'].transform([brand])[0],
    'Model': le_dict['Model'].transform([model])[0],
    'Operating System': le_dict['Operating System'].transform([operating_system])[0],
    'Connectivity': le_dict['Connectivity'].transform([connectivity])[0],
    'Display Type': le_dict['Display Type'].transform([display_type])[0],
    'Resolution': le_dict['Resolution'].transform([resolution])[0],
    'Water Resistance (meters)': le_dict['Water Resistance (meters)'].transform([water_resistance])[0],
    'Battery Life (days)': battery_life,
    'Heart Rate Monitor': 1 if heart_rate_monitor == 'Yes' else 0,
    'GPS': 1 if gps == 'Yes' else 0,
    'NFC': 1 if nfc == 'Yes' else 0
}

# Tahmin butonu
if st.button('Predict'):
    # Fiyat tahmini yapma
    predicted_price = predict_price(input_data)
    st.markdown(f'**Prediction Result: ${predicted_price:.2f}**', unsafe_allow_html=True)
else:
    st.markdown("**Click the button to make a prediction.**", unsafe_allow_html=True)



  







