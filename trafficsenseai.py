import streamlit as st
import pickle, numpy as np, requests, folium, pandas as pd
import plotly.express as px
from streamlit_folium import st_folium

st.set_page_config(page_title="TrafficSense AI", page_icon="🚦", layout="wide")

# --- Load Model ---
DIR = r"C:\Users\utkar\Downloads\traffic_sense_ai_dataset.xlsx"
model = pickle.load(open(f"{DIR}\\traffic_classifier.sav", "rb"))
te    = pickle.load(open(f"{DIR}\\time_encoder.sav", "rb"))
de    = pickle.load(open(f"{DIR}\\day_encoder.sav", "rb"))
tgt   = pickle.load(open(f"{DIR}\\target_encoder.sav", "rb"))
df    = pd.read_excel(r"C:\Users\utkar\Downloads\traffic_sense_ai_dataset.xlsx", header=2)
df["Traffic Situation"] = df["Traffic Situation"].str.strip().str.lower()

TIMES = [f"{h%12 or 12}:{m:02d}:00 {'AM' if h<12 else 'PM'}" for h in range(24) for m in [0,15,30,45]]

# --- Sidebar ---
st.sidebar.title("🚦 TrafficSense AI")
origin = st.sidebar.text_input("Origin", "Connaught Place, Delhi")
dest   = st.sidebar.text_input("Destination", "Hauz Khas, Delhi")
time_s = st.sidebar.selectbox("Time", TIMES)
day_s  = st.sidebar.selectbox("Day", list(de.classes_))
date_s = st.sidebar.slider("Date", 1, 31, 15)
cars   = st.sidebar.slider("Cars",   0, 300, 80)
bikes  = st.sidebar.slider("Bikes",  0, 300, 40)
buses  = st.sidebar.slider("Buses",  0, 100, 10)
trucks = st.sidebar.slider("Trucks", 0, 100,  5)

for k,v in {"pred":None,"map_obj":None,"chat":[]}.items():
    if k not in st.session_state: st.session_state[k] = v

# --- Predict ---
if st.sidebar.button("🔍 Predict Traffic", use_container_width=True):
    t = te.transform([time_s])[0] if time_s in te.classes_ else te.transform([te.classes_[0]])[0]
    X = np.array([[t, date_s, de.transform([day_s])[0], cars, bikes, buses, trucks]])
    st.session_state.pred = tgt.inverse_transform(model.predict(X))[0].strip().lower()

    def geocode(p):
        try:
            r = requests.get("https://nominatim.openstreetmap.org/search",
                params={"q":p,"format":"json","limit":1},headers={"User-Agent":"ts"},timeout=5).json()
            return (float(r[0]["lat"]),float(r[0]["lon"])) if r else (None,None)
        except: return None,None

    o_lat,o_lon = geocode(origin)
    d_lat,d_lon = geocode(dest)
    if o_lat is not None and o_lon is not None and d_lat is not None and d_lon is not None:
        oc:tuple[float,float] = (o_lat,o_lon)
        dc:tuple[float,float] = (d_lat,d_lon)
        color = {"low":"green","medium":"orange","high":"red","very high":"darkred"}.get(st.session_state.pred,"blue")
        try:
            r = requests.get(f"http://router.project-osrm.org/route/v1/driving/{oc[1]},{oc[0]};{dc[1]},{dc[0]}?overview=full&geometries=geojson",timeout=8).json()
            route = [(c[1],c[0]) for c in r["routes"][0]["geometry"]["coordinates"]]
        except: route=[]
        m = folium.Map(location=oc,zoom_start=12)
        folium.Marker(oc,tooltip="Origin",icon=folium.Icon(color="blue")).add_to(m)
        folium.Marker(dc,tooltip="Destination",icon=folium.Icon(color="red")).add_to(m)
        if route: folium.PolyLine(route,color=color,weight=5).add_to(m)
        st.session_state.map_obj = m

# --- Main ---
st.title("🚦 TrafficSense AI — Traffic Prediction System")
tab1, tab2, tab3 = st.tabs(["🗺️ Prediction & Map", "📊 Data Charts", "🤖 ChatBot"])

with tab1:
    if st.session_state.pred:
        alerts = {
            "low":      ("🟢 LOW TRAFFIC",      "green",   "Roads are clear! Safe to travel."),
            "medium":   ("🟡 MEDIUM TRAFFIC",    "orange",  "Moderate congestion. Leave 10–15 min early."),
            "high":     ("🔴 HIGH TRAFFIC",      "red",     "Heavy traffic! Consider an alternate route."),
            "very high":("🚨 VERY HIGH TRAFFIC", "darkred", "Severe congestion! Use Metro or reschedule."),
        }
        title,color,tip = alerts.get(st.session_state.pred, alerts["medium"])
        st.markdown(f"""<div style="border-left:6px solid {color};background:#111;padding:1rem 1.5rem;border-radius:8px;margin-bottom:1rem">
            <h3 style="color:{color};margin:0">{title}</h3>
            <p style="color:#ccc;margin:0.3rem 0 0 0">📍 {origin} → {dest}<br>💡 {tip}</p>
        </div>""", unsafe_allow_html=True)
    if st.session_state.map_obj:
        st_folium(st.session_state.map_obj, width=None, height=450, key="map", returned_objects=[])
    else:
        st.info("Fill in the sidebar and click **Predict Traffic** to see your route.")

with tab2:
    st.subheader("📊 Traffic Data Analysis")
    CM = {"low":"#00c853","medium":"#ffab00","high":"#ff5722","very high":"#b71c1c"}
    c1,c2 = st.columns(2)
    pie = df["Traffic Situation"].value_counts().reset_index()
    pie.columns = ["Situation","Count"]
    c1.plotly_chart(px.pie(pie,names="Situation",values="Count",hole=0.4,title="Traffic Distribution",color="Situation",color_discrete_map=CM), use_container_width=True)
    day_g = df.groupby(["Day of the Week","Traffic Situation"]).size().reset_index(name="Count")
    c2.plotly_chart(px.bar(day_g,x="Day of the Week",y="Count",color="Traffic Situation",barmode="stack",title="Traffic by Day",
        color_discrete_map=CM,category_orders={"Day of the Week":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]}), use_container_width=True)
    veh = df.groupby("Traffic Situation")[["CarCount","BikeCount","BusCount","TruckCount"]].mean().reset_index()
    st.plotly_chart(px.bar(veh.melt(id_vars="Traffic Situation"),x="Traffic Situation",y="value",color="variable",barmode="group",title="Avg Vehicles per Traffic Level"), use_container_width=True)

with tab3:
    st.subheader("🤖 TrafficBot — Ask Me Anything!")
    BOT = {
        "peak":     "Peak hours are **7–9 AM** and **5–8 PM** on weekdays.",
        "best":     "Best time to travel: **before 7 AM** or **after 9 PM**.",
        "metro":    "Delhi Metro is the best option during peak hours!",
        "alternate":"Try **Ring Road**, NH-48, or Peripheral Expressways.",
        "rain":     "Rain adds 30–60 min to travel time. Plan accordingly!",
        "weekend":  "Weekends are much lighter. Sunday afternoon is ideal.",
        "help":     "Ask: peak | best time | metro | alternate | rain | weekend",
    }
    if not st.session_state.chat:
        st.session_state.chat.append({"role":"assistant","content":"Hi! I'm TrafficBot 🚦 Ask: **peak hours**, **best time**, **metro**, **alternate**, **rain**, or **weekend**!"})
    for msg in st.session_state.chat:
        st.chat_message(msg["role"]).markdown(msg["content"])
    if user := st.chat_input("Ask about traffic..."):
        st.session_state.chat.append({"role":"user","content":user})
        reply = next((v for k,v in BOT.items() if k in user.lower()), "Try: peak | best time | metro | alternate | rain | weekend 🚦")
        if st.session_state.pred and any(w in user.lower() for w in ["current","status","now"]):
            reply = f"Current prediction: **{st.session_state.pred.upper()}** on {origin} → {dest}."
        st.session_state.chat.append({"role":"assistant","content":reply})
        st.rerun()
