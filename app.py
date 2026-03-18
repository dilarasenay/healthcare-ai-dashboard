import streamlit as st
from utils.data_loader import load_data
from panels import veri_inceleme, kpi, karar_paneli, akilli_oneri

st.set_page_config(
    page_title="AI Healthcare System",
    layout="wide"
)

df = load_data()

st.sidebar.markdown("## 🧭 Navigation")

panel = st.sidebar.radio(
    "Panel Seç",
    ["📊 Veri", "📈 KPI", "🧠 Karar", "🤖 Öneri"]
)

if panel == "📊 Veri":
    veri_inceleme.show(df)

elif panel == "📈 KPI":
    kpi.show(df)

elif panel == "🧠 Karar":
    karar_paneli.show(df)

elif panel == "🤖 Öneri":
    akilli_oneri.show(df)