import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"
st.title("Bike Rental Prediction!!!")

with st.form("prediction_form"):
 
    season = st.selectbox("Season", [1, 2, 3, 4])
    yr = st.selectbox("yr", [0, 1])
    mnth = st.number_input("mnth", min_value=1, max_value=12)
    holiday = st.selectbox("holiday", [0, 1])
    weekday = st.number_input('weekday', min_value=0, max_value=6)
    workingday = st.selectbox('workingday', [0, 1])
    weathersit = st.selectbox('weathersit', [0, 1, 2])
    temp = st.number_input('Normalized Temperature', min_value = 0.0, max_value =1000.0)
    atemp = st.number_input('Normalized Feeling Temperature', min_value = 0.0, max_value =1000.0)
    hum = st.number_input('Humidity', min_value = 0.0, max_value =1000.0)
    windspeed = st.number_input('Windspeed', min_value = 0.0, max_value =1000.0)
    year = st.selectbox('Year', [2011, 2012])
    month = st.number_input("Month", min_value=0, max_value=12)
    day = st.number_input("Day", min_value = 0, max_value =31)
    dayofweek = st.number_input("Day of the Week", min_value = 0, max_value =7)

    submit = st.form_submit_button("Predict!!!")

if submit:
    payload = test_data = {
        "season": season,
        "yr": yr,
        "mnth": mnth,
        "holiday": holiday,
        "weekday": weekday,
        "workingday": workingday,
        "weathersit": weathersit,
        "temp": temp,
        "atemp": atemp,
        "hum": hum,
        "windspeed": windspeed,
        "year": year,
        "month": month,
        "day": day,
        "dayofweek": dayofweek
    }
        
    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        st.write(f"Response status code: {response.status_code}")

        try:
            result = response.json()
        except Exception as e:
            st.error("Response is not in JSON!!!")
            st.write(response.text)
            result = None

        if response.status_code == 200 and result is not None:
            predicted = result.get("Bike_Count", result)
            st.success(f"Predicted Bike Counts: **{predicted}**")
            st.json(result)
        else:
            st.error(f"Error : {response.status_code}")
            st.write(response.text)
        
    except requests.exceptions.RequestException as e:
        st.error("API not reachable!!!")
        st.write(str(e))

