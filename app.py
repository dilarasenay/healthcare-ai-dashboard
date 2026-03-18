import streamlit as st
from utils.data_loader import load_data
from panels import veri_inceleme, kpi, karar_paneli, akilli_oneri

st.set_page_config(
    page_title="AI Healthcare System",
    layout="wide"
)

st.markdown("""
<style>
/* ===== GENEL SAYFA FIX ===== */
header[data-testid="stHeader"] {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

[data-testid="stAppViewContainer"] {
    margin-top: 0 !important;
    padding-top: 0 !important;
    background: linear-gradient(180deg, #f7f8fc 0%, #eef3fb 100%);
}

.block-container {
    padding-top: 0.6rem !important;
    padding-bottom: 2rem !important;
    max-width: 100%;
}

html, body, [class*="css"] {
    margin-top: 0 !important;
    padding-top: 0 !important;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at top left, rgba(99,102,241,0.16), transparent 18%),
        linear-gradient(180deg, #f8faff 0%, #eef4ff 100%);
    border-right: 1px solid rgba(120,140,200,0.12);
    padding-top: 0rem !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1rem !important;
    padding-left: 1rem;
    padding-right: 1rem;
}

.sidebar-brand {
    background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%);
    border-radius: 22px;
    padding: 18px 16px;
    color: white;
    margin-bottom: 1rem;
    box-shadow: 0 14px 28px rgba(79,70,229,0.18);
}

.sidebar-brand-title {
    font-size: 1.25rem;
    font-weight: 900;
    margin-bottom: 0.35rem;
}

.sidebar-brand-sub {
    font-size: 0.92rem;
    line-height: 1.55;
    color: rgba(255,255,255,0.92);
}

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #153672;
}

div[role="radiogroup"] > label {
    border-radius: 16px !important;
}

/* Sidebar içindeki boşlukları biraz toparla */
section[data-testid="stSidebar"] .stRadio > div {
    gap: 0.35rem;
}
</style>
""", unsafe_allow_html=True)

# Veri yükleme
df = load_data()

# Sidebar üst alan
st.sidebar.markdown("""
<div class="sidebar-brand">
    <div class="sidebar-brand-title">🏥 AI Health Command</div>
    <div class="sidebar-brand-sub">
        Karar destek panelleri, KPI takibi ve öneri motoru tek merkezde.
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🧭 Navigation")

panel = st.sidebar.radio(
    "Panel Seç",
    ["📊 Veri", "📈 KPI", "🧠 Karar", "🤖 Öneri"]
)

# Panel yönlendirme
if panel == "📊 Veri":
    veri_inceleme.show(df)

elif panel == "📈 KPI":
    kpi.show(df)

elif panel == "🧠 Karar":
    karar_paneli.show(df)

elif panel == "🤖 Öneri":
    akilli_oneri.show(df)