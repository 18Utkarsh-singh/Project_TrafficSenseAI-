<div align="center">

# 🚦 TrafficSense AI

### Machine Learning–Powered Traffic Congestion Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)
[![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-Mapping-green?style=for-the-badge&logo=openstreetmap)](https://openstreetmap.org)

*Predict traffic congestion levels before you travel — using Random Forest classification, real-time route visualization, and an interactive web interface.*

</div>

---

## 📖 Overview

**TrafficSense AI** is an intelligent transportation system that uses a trained **Random Forest classifier** to predict urban traffic congestion levels based on vehicle counts, time of day, day of week, and date. The system provides an interactive **Streamlit** web interface and visualizes routes on **OpenStreetMap**, making it a practical demonstration of how machine learning can assist smart city mobility planning.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🚗 **Traffic Prediction** | Predicts congestion level using a Random Forest classifier |
| 🕒 **96 Time Slots** | Granular 15-minute interval support across the full day |
| 📅 **Temporal Awareness** | Uses day of week and date for context-aware predictions |
| 🚦 **Multi-Vehicle Input** | Accepts counts for cars, bikes, buses, and trucks |
| 🗺️ **Route Visualization** | Displays routes interactively on OpenStreetMap via Folium |
| 📍 **Geocoding Support** | Converts origin/destination addresses to coordinates |
| 📊 **Interactive UI** | Clean, user-friendly Streamlit interface |

---

## 🧠 Machine Learning Model

### Algorithm: Random Forest Classifier

Random Forest was selected for its strong performance on tabular/structured data, natural resistance to overfitting, and interpretability — making it well-suited for transportation prediction tasks.

### Input Features

| Feature | Type | Description |
|---|---|---|
| `Time` | Categorical | One of 96 time slots (every 15 minutes) |
| `Date` | Numerical | Day of the month |
| `Day` | Categorical | Day of the week (Mon–Sun) |
| `Cars` | Numerical | Number of cars on road |
| `Bikes` | Numerical | Number of bikes on road |
| `Buses` | Numerical | Number of buses on road |
| `Trucks` | Numerical | Number of trucks on road |

### Output: Congestion Level
```
🟢 Low     🟡 Medium     🟠 High     🔴 Very High
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Interactive web UI |
| **Scikit-learn** | Random Forest model training & inference |
| **Folium** | Interactive map rendering |
| **OpenStreetMap + OSRM** | Geocoding & route planning |
| **NumPy** | Numerical computations |
| **Pickle** | Model serialization |

---

## 📂 Project Structure
```
TrafficSense-AI/
│
├── traffic_app.py              # Main Streamlit application
│
├── model/
│   ├── traffic_classifier.sav  # Trained Random Forest model
│   ├── time_encoder.sav        # Encoder for time slots
│   ├── day_encoder.sav         # Encoder for day of week
│   └── target_encoder.sav      # Encoder for output labels
│
└── dataset/
    └── traffic_dataset.csv     # Training dataset
```

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/thenakulcode/Traffic_SenseAI_.git
cd TrafficSense-AI
```

### 2. Install Dependencies
```bash
pip install streamlit folium streamlit-folium scikit-learn numpy requests
```

> **Python 3.8+** is recommended.

---

## ▶️ Running the Application
```bash
streamlit run traffic_app.py
```

The app will automatically open in your default browser at `http://localhost:8501`.

---

## 🔄 How It Works
```
User Input  →  Encoding  →  ML Prediction  →  Route Fetch  →  Map Display
```

1. **User provides inputs** — time slot, day, date, vehicle counts, and origin/destination
2. **Data is encoded** using the pre-trained label encoders
3. **Random Forest model** predicts the traffic congestion level
4. **OSRM API** retrieves the road route between origin and destination
5. **Folium + OpenStreetMap** renders the route and prediction on an interactive map

---

## 🌍 Real-World Applications

- 🏙️ **Smart City Traffic Monitoring** — Support urban traffic management centers
- 🧭 **Route Planning & Navigation** — Help commuters choose optimal travel times
- 📦 **Logistics & Delivery Optimization** — Reduce delays in last-mile delivery
- 🏗️ **Urban Transportation Planning** — Inform infrastructure and policy decisions
- 🚦 **Congestion Forecasting** — Predict peak-hour congestion before it occurs

---

## 🚧 Limitations

- Uses a **historical dataset** — not connected to live traffic feeds
- Prediction accuracy is dependent on **dataset quality and coverage**
- Does **not currently integrate** real-time traffic APIs (e.g., Google Maps, HERE)

---

## 🔮 Future Roadmap

- [ ] 🔴 Integration with real-time traffic data APIs
- [ ] 🤖 Deep learning models (LSTM, Transformer) for improved sequence prediction
- [ ] 📱 Mobile application version
- [ ] 📡 Real-time IoT vehicle sensor data integration
- [ ] 🚦 Smart traffic signal prediction and optimization
- [ ] 🌐 Multi-city dataset support

---

## 👨‍💻 Author

Developed as a machine learning project for **Intelligent Transportation Systems (ITS)**.  
Built with ❤️ using Python, Scikit-learn, and Streamlit.

---

<div align="center">

⭐ If you found this project useful, please consider giving it a star!

</div>
