# 🩺 AI Healthcare Decision Dashboard

An intelligent, data-driven healthcare analytics dashboard built with **Streamlit**, designed to support **data exploration, KPI monitoring, decision-making, and AI-powered recommendations**.

---

## 🚀 Overview

This project is a **modular healthcare decision support system** that enables users to:

* Analyze healthcare operational data
* Monitor critical KPIs in real-time
* Support decision-making with insights
* Generate intelligent recommendations

The system is structured into **4 main panels**, each serving a distinct analytical purpose.

---

## 🧩 Features

### 📊 1. Data Exploration Panel

* Dataset overview and inspection
* Interactive visualizations
* Trend analysis across time (Day-based)

### 📈 2. KPI Dashboard

* Key healthcare metrics visualization
* Clean and modern KPI cards
* Performance tracking (Admissions, Bed Occupancy, etc.)

### 🧠 3. Decision Panel

* Analytical insights for decision support
* Pattern detection and interpretation
* Data-driven strategic suggestions

### 🤖 4. Smart Recommendation Panel

* Intelligent recommendation system
* Visual insights + contextual suggestions
* Designed for future LLM integration

---

## 🏗️ Project Structure

```
healthcare-ai-dashboard/
│
├── app.py                # Main entry point (Streamlit app)
│
├── panels/              # UI Panels
│   ├── veri_inceleme.py
│   ├── kpi.py
│   ├── karar_paneli.py
│   └── akilli_oneri.py
│
├── utils/               # Utility functions
│   └── data_loader.py
│
├── data/
│   └── raw/
│       └── healthcare_operational_dataset_30_days.csv
│
├── .streamlit/          # Streamlit config (optional)
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Installation & Run

### 1. Clone the repository

```bash
git clone https://github.com/dilarasenay/healthcare-ai-dashboard.git
cd healthcare-ai-dashboard
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

✨ *If you like this project, don’t forget to give it a star!*
