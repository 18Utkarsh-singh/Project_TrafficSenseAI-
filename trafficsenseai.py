import streamlit as st
import pickle
import numpy as np
import requests
import folium
from streamlit_folium import st_folium
import os

# -----------------------------
# Session State
# -----------------------------

if "map_obj" not in st.session_state:
    st.session_state.map_obj = None

if "prediction" not in st.session_state:
    st.session_state.prediction = None


# -----------------------------
# Generate all 96 time slots
# -----------------------------

#TIMES = []

for hour in range(24):
    for minute in [0, 15, 30, 45]:

        h = hour % 12
        if h == 0:
            h = 12

        period = "AM" if hour < 12 else "PM"

        TIMES.append(f"{h}:{minute:02d}:00 {period}")


st.title("Traffic Prediction System")


# -----------------------------
# Load model and encoders
# -----------------------------

model = None
time_encoder = None
day_encoder = None
target_encoder = None

base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, "model")

try:
    model = pickle.load(open(os.path.join(model_dir, "traffic_classifier.sav"), "rb"))
    time_encoder = pickle.load(open(os.path.join(model_dir, "time_encoder.sav"), "rb"))
    day_encoder = pickle.load(open(os.path.join(model_dir, "day_encoder.sav"), "rb"))
    target_encoder = pickle.load(open(os.path.join(model_dir, "target_encoder.sav"), "rb"))

    st.success("Model loaded successfully")

except Exception as e:
    st.error(f"Model loading error: {e}")


# -----------------------------
# Sidebar Inputs
# -----------------------------

st.sidebar.header("Input Traffic Data")

time = st.sidebar.selectbox("Time", TIMES)

if day_encoder is not None:
    day = st.sidebar.selectbox("Day", list(day_encoder.classes_))
else:
    day = st.sidebar.text_input("Day", "Monday")

if model is None or time_encoder is None or day_encoder is None or target_encoder is None:
    st.warning("Model or encoders not loaded. Predict button is disabled until load succeeds.")

date = st.sidebar.slider("Date", 1, 31, 15)

cars = st.sidebar.slider("Cars", 0, 300, 80)
bikes = st.sidebar.slider("Bikes", 0, 300, 40)
buses = st.sidebar.slider("Buses", 0, 100, 10)
trucks = st.sidebar.slider("Trucks", 0, 100, 5)

origin = st.text_input("Origin", "Connaught Place, Delhi")
destination = st.text_input("Destination", "Hauz Khas, Delhi")


# -----------------------------
# Geocode function
# -----------------------------

def geocode(place):

    try:

        url = "https://nominatim.openstreetmap.org/search"

        params = {
            "q": place,
            "format": "json",
            "limit": 1
        }

        headers = {
            "User-Agent": "traffic-prediction-app"
        }

        r = requests.get(url, params=params, headers=headers, timeout=5)

        if r.status_code != 200:
            return None, None

        data = r.json()

        if len(data) == 0:
            return None, None

        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])

        return lat, lon

    except:
        return None, None


# -----------------------------
# Get Route
# -----------------------------

def get_route(o, d):

    try:

        url = f"http://router.project-osrm.org/route/v1/driving/{o[1]},{o[0]};{d[1]},{d[0]}?overview=full&geometries=geojson"

        r = requests.get(url)

        if r.status_code != 200:
            return []

        data = r.json()

        if "routes" not in data:
            return []

        coords = data["routes"][0]["geometry"]["coordinates"]

        coords = [(c[1], c[0]) for c in coords]

        return coords

    except:
        return []


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Traffic"):
    if model is None or time_encoder is None or day_encoder is None or target_encoder is None:
        st.error("Cannot predict: model or encoders are not loaded.")
    else:
        try:
            try:
                t = time_encoder.transform([time])[0]
            except Exception:
                t = time_encoder.transform([time_encoder.classes_[0]])[0]

            d = day_encoder.transform([day])[0]

            X = np.array([[t, date, d, cars, bikes, buses, trucks]])

            pred = model.predict(X)
            prediction = target_encoder.inverse_transform(pred)[0]

            # save prediction
            st.session_state.prediction = prediction

            o = geocode(origin)
            d = geocode(destination)

            if o[0] and d[0]:

                coords = get_route(o, d)

                m = folium.Map(location=o, zoom_start=12)

                folium.Marker(o, tooltip="Origin").add_to(m)
                folium.Marker(d, tooltip="Destination").add_to(m)

                if coords:
                    folium.PolyLine(coords, color="red", weight=5).add_to(m)

                st.session_state.map_obj = m

            else:
                st.warning("Location not found")

        except Exception as e:
            st.error(f"Prediction failed: {e}")


# -----------------------------
# Display Prediction
# -----------------------------

if st.session_state.prediction:
    st.subheader(f"Predicted Traffic Level: {st.session_state.prediction}")


# -----------------------------
# Display Map
# -----------------------------

if st.session_state.map_obj:
    st_folium(st.session_state.map_obj, width=700, height=500)
