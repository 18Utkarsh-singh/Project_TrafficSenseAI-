<div align="center">

# 🚦 TrafficSense AI

### Machine Learning–Powered Traffic Congestion Prediction System

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)
[![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-Mapping-green?style=for-the-badge&logo=openstreetmap)](https://openstreetmap.org)

*Predict traffic congestion levels before you travel — using Random Forest classification, real-time route visualization, smart alerts, data charts, and an AI chatbot.*

</div>

---

## 📖 Overview

**TrafficSense AI** is an intelligent transportation system that uses a trained **Random Forest classifier** to predict urban traffic congestion levels based on vehicle counts, time of day, day of week, and date. It features a **color-coded alert system**, **interactive data charts**, and a **TrafficBot chatbot** — all wrapped in a clean **Streamlit** web interface with live route visualization on **OpenStreetMap**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🚗 **Traffic Prediction** | Predicts congestion using a Random Forest classifier |
| 🚨 **Smart Alert System** | Color-coded alerts for Low / Medium / High / Very High traffic |
| 🗺️ **Route Visualization** | Color-coded route displayed on interactive OpenStreetMap |
| 📊 **Data Analytics** | 3 interactive Plotly charts from the training dataset |
| 🤖 **TrafficBot** | Built-in chatbot for traffic tips and travel advice |
| 🕒 **96 Time Slots** | Granular 15-minute interval support across the full day |
| 🚦 **Multi-Vehicle Input** | Accepts counts for cars, bikes, buses, and trucks |

---

## 🚨 Alert System

| Level | Color | Advice |
|---|---|---|
| 🟢 Low | Green | Roads are clear! Safe to travel. |
| 🟡 Medium | Orange | Moderate congestion. Leave 10–15 min early. |
| 🔴 High | Red | Heavy traffic! Consider an alternate route. |
| 🚨 Very High | Dark Red | Severe congestion! Use Metro or reschedule. |

---

## 📊 Data Charts (Tab 2)

- **Donut Chart** — Overall traffic distribution across the dataset
- **Stacked Bar Chart** — Traffic levels broken down by day of the week
- **Grouped Bar Chart** — Average vehicle counts per traffic level

---

## 🤖 TrafficBot (Tab 3)

Ask the chatbot about:

| Question | Type |
|---|---|
| `peak hours` | When is traffic heaviest? |
| `best time` | When should I travel? |
| `metro` | Should I use the Metro? |
| `alternate` | What are alternate routes? |
| `rain` | How does rain affect traffic? |
| `weekend` | Is weekend traffic lighter? |
| `current status` | What was my last prediction? |

---

## 🧠 Machine Learning Model

**Algorithm: Random Forest Classifier**

### Input Features

| Feature | Type | Description |
|---|---|---|
| `Time` | Categorical | One of 96 time slots (every 15 minutes) |
| `Date` | Numerical | Day of the month (1–31) |
| `Day` | Categorical | Day of the week (Mon–Sun) |
| `Cars` | Numerical | Number of cars on road |
| `Bikes` | Numerical | Number of bikes on road |
| `Buses` | Numerical | Number of buses on road |
| `Trucks` | Numerical | Number of trucks on road |

### Dataset: 2,000 Records
| Traffic Level | Count |
|---|---|
| 🟢 Low | 819 |
| 🟡 Medium | 560 |
| 🚨 Very High | 436 |
| 🔴 High | 185 |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Interactive web UI |
| **Scikit-learn** | Random Forest model |
| **Folium + streamlit-folium** | Interactive map rendering |
| **Plotly** | Data visualization charts |
| **OpenStreetMap + OSRM** | Geocoding & route planning |
| **Pandas + NumPy** | Data processing |
| **Pickle** | Model serialization |
| **openpyxl** | Excel dataset reading |

---

## 📂 Project Structure

```
Project_TrafficSenseAI/
│
├── trafficsenseai.py           # Main Streamlit application (119 lines)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── model/
│   ├── traffic_classifier.sav  # Trained Random Forest model
│   ├── time_encoder.sav        # Encoder for time slots
│   ├── day_encoder.sav         # Encoder for day of week
│   └── target_encoder.sav      # Encoder for output labels
│
└── dataset/
    └── traffic_sense_ai_dataset.xlsx   # Training dataset (2,000 records)
```

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/thenakulcode/Project_TrafficSenseAI-.git
cd Project_TrafficSenseAI-
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run trafficsenseai.py
```

The app opens at `http://localhost:8501`

---

## 🔄 How It Works

```
User Input → Encoding → ML Prediction → Alert → Route Fetch → Map Display
```

1. **User provides inputs** — origin, destination, time, day, date, vehicle counts
2. **Data is encoded** using pre-trained label encoders
3. **Random Forest model** predicts the traffic congestion level
4. **Smart alert** displays color-coded warning with travel advice
5. **OSRM API** retrieves the road route between origin and destination
6. **Folium + OpenStreetMap** renders the color-coded route on an interactive map

---

## 🌍 Real-World Applications

- 🏙️ **Smart City Traffic Monitoring**
- 🧭 **Route Planning & Navigation**
- 📦 **Logistics & Delivery Optimization**
- 🚦 **Congestion Forecasting**

---

## 🚧 Limitations

- Uses a **historical dataset** — not connected to live traffic feeds
- Chatbot uses **keyword matching** — not a large language model
- Route accuracy depends on **OSRM API availability**

---

## 🔮 Future Roadmap

- [ ] Real-time traffic data API integration
- [ ] Deep learning models (LSTM) for sequence prediction
- [ ] Mobile application version
- [ ] Multi-city dataset support
- [ ] AI-powered chatbot using LLM

---

## 👨‍💻 Author

**Nakul** — Developed as a machine learning project for Intelligent Transportation Systems.  
Built with ❤️ using Python, Scikit-learn, Streamlit, and Plotly.

---

<div align="center">

⭐ If you found this project useful, please consider giving it a star!

**🚀 [Live Demo](https://share.streamlit.io) | 📁 [GitHub](https://github.com/thenakulcode/Project_TrafficSenseAI-)**

</div>
