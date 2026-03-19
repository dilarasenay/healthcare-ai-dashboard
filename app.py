import streamlit as st
from utils.data_loader import load_data
from panels import veri_inceleme, kpi, karar_paneli, akilli_oneri

st.set_page_config(
    page_title="AI Healthcare System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* =========================================================
   GENEL APP
========================================================= */
html, body, [class*="css"] {
    margin-top: 0 !important;
    padding-top: 0 !important;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(168, 85, 247, 0.05), transparent 20%),
        radial-gradient(circle at bottom right, rgba(244, 114, 182, 0.04), transparent 24%),
        linear-gradient(180deg, #fcfbff 0%, #f6f4fb 50%, #f4f6fb 100%);
}

header[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] {
    display: none !important;
}

.block-container {
    padding-top: 0.4rem !important;
    padding-bottom: 1.5rem !important;
}

/* =========================================================
   SIDEBAR TOGGLE KALDIR (<< tamamen yok)
========================================================= */
[data-testid="collapsedControl"],
div[data-testid="stSidebarCollapseButton"],
button[kind="header"],
button[title],
button[aria-label] {
    display: none !important;
}

/* =========================================================
   SIDEBAR
========================================================= */
section[data-testid="stSidebar"] {
    min-width: 260px !important;
    max-width: 260px !important;
    background:
        radial-gradient(circle at top left, rgba(196, 181, 253, 0.18), transparent 22%),
        radial-gradient(circle at bottom right, rgba(244, 114, 182, 0.10), transparent 22%),
        linear-gradient(180deg, #fffdfd 0%, #faf7ff 46%, #f7f4fb 100%);
    border-right: 1px solid rgba(176,166,201,0.08);
}

section[data-testid="stSidebar"] .block-container {
    padding: 0.9rem 1rem;
}

/* =========================================================
   BRAND
========================================================= */
.sidebar-brand {
    background: linear-gradient(135deg, #9b5cf6, #ec4899);
    border-radius: 22px;
    padding: 16px;
    color: white;
    margin-bottom: 1rem;
    box-shadow: 0 16px 30px rgba(168,85,247,0.18);
}

.sidebar-brand-title {
    font-weight: 900;
    font-size: 1.1rem;
}

.sidebar-brand-sub {
    font-size: 0.9rem;
    opacity: 0.95;
}

/* =========================================================
   NAVIGATION
========================================================= */
.nav-title {
    font-size: 1.5rem;
    font-weight: 900;
    background: linear-gradient(90deg, #a855f7, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}

.nav-subtitle {
    font-size: 0.85rem;
    color: #8f7fa5;
    margin-bottom: 0.6rem;
}

/* radio label gizle */
section[data-testid="stSidebar"] .stRadio > label {
    display: none !important;
}

/* kart layout */
section[data-testid="stSidebar"] .stRadio > div {
    gap: 0.6rem !important;
}

/* kart */
section[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.85);
    border-radius: 16px;
    padding: 10px;
    border: 1px solid rgba(170,150,200,0.15);
    transition: all 0.25s ease;
}

/* hover */
section[data-testid="stSidebar"] .stRadio label:hover {
    transform: translateX(4px);
    box-shadow: 0 10px 20px rgba(168,85,247,0.1);
}

/* selected */
section[data-testid="stSidebar"] .stRadio label:has(input:checked) {
    background: linear-gradient(135deg, #f3e8ff, #fde2f3);
    border: 1px solid rgba(168,85,247,0.3);
    box-shadow:
        0 20px 40px rgba(168,85,247,0.18),
        0 6px 16px rgba(244,114,182,0.12);
}

/* text */
section[data-testid="stSidebar"] .stRadio label p {
    font-weight: 800;
    color: #43325c;
}

/* =========================================================
   SCROLLBAR
========================================================= */
section[data-testid="stSidebar"] ::-webkit-scrollbar {
    width: 6px;
}
section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #d3b3ff, #f7a8cf);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# DATA
df = load_data()

# SIDEBAR
st.sidebar.markdown("""
<div class="sidebar-brand">
    <div class="sidebar-brand-title">🏥 AI Health Command</div>
    <div class="sidebar-brand-sub">
        KPI, karar ve öneri motorunu tek merkezde yönet.
    </div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div class="nav-title">✦ Navigation</div>
<div class="nav-subtitle">
    Paneller arasında akıcı geçiş yap.
</div>
""", unsafe_allow_html=True)

# PANEL SELECT (label kaldırıldı)
panel = st.sidebar.radio(
    "",
    [
        "📊 Veri Seti Analizi",
        "📈 KPI Merkezi",
        "🧠 Karar Paneli",
        "🤖 Akıllı Öneri"
    ],
    label_visibility="collapsed"
)

# ROUTING
if panel == "📊 Veri Seti Analizi":
    veri_inceleme.show(df)

elif panel == "📈 KPI Merkezi":
    kpi.show(df)

elif panel == "🧠 Karar Paneli":
    karar_paneli.show(df)

elif panel == "🤖 Akıllı Öneri":
    akilli_oneri.show(df)