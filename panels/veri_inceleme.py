import streamlit as st
import pandas as pd


def show(df):
    st.set_page_config(page_title="Veri Seti", layout="wide")

    # ---------------- STYLE ----------------
    st.markdown("""
    <style>
    .stApp {
        background:
            radial-gradient(circle at top right, rgba(168, 85, 247, 0.08), transparent 22%),
            radial-gradient(circle at bottom left, rgba(103, 232, 249, 0.10), transparent 24%),
            linear-gradient(180deg, #f6f4ff 0%, #eef4ff 100%);
    }

    .block-container {
        max-width: 95%;
        padding-top: 1rem !important;
        padding-bottom: 2rem;
    }

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, rgba(244,242,255,0.96) 0%, rgba(237,244,255,0.97) 100%);
        border-right: 1px solid rgba(99, 102, 241, 0.10);
        backdrop-filter: blur(10px);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.25rem;
    }

    .sidebar-title {
        font-size: 2rem;
        font-weight: 900;
        color: #4f46e5;
        margin-bottom: 0.15rem;
    }

    .sidebar-sub {
        font-size: 0.98rem;
        color: #5f6f89;
        line-height: 1.55;
        margin-bottom: 1rem;
    }

    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span {
        color: #334155 !important;
    }

    [data-baseweb="tag"] {
        background: linear-gradient(135deg, #6366f1, #60a5fa) !important;
        border-radius: 999px !important;
        border: none !important;
        box-shadow: 0 6px 14px rgba(99, 102, 241, 0.18);
    }

    [data-baseweb="tag"] span {
        color: white !important;
        font-weight: 700 !important;
    }

    .hero-card {
        background:
            radial-gradient(circle at top right, rgba(192,132,252,0.12), transparent 28%),
            radial-gradient(circle at bottom left, rgba(103,232,249,0.10), transparent 24%),
            linear-gradient(135deg, rgba(255,255,255,0.98), rgba(239,243,255,0.96));
        border: 1px solid rgba(129, 140, 248, 0.12);
        border-radius: 30px;
        padding: 28px 30px 22px 30px;
        box-shadow:
            0 18px 38px rgba(99, 102, 241, 0.08),
            inset 0 1px 0 rgba(255,255,255,0.70);
        margin-bottom: 20px;
    }

    .hero-row {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .hero-icon {
        width: 38px;
        height: 38px;
        border-radius: 12px;
        background: linear-gradient(135deg, #5b4df0, #60a5fa);
        box-shadow: 0 10px 22px rgba(91, 77, 240, 0.22);
        flex-shrink: 0;
    }

    .hero-title {
        font-size: 2.35rem;
        font-weight: 900;
        line-height: 1.1;
        color: #5446e8;
        margin: 0;
        letter-spacing: -0.02em;
    }

    .hero-subtitle {
        color: #5f6f89;
        font-size: 1.02rem;
        margin-top: 10px;
        line-height: 1.6;
    }

    .metric-card {
        background:
            radial-gradient(circle at bottom left, rgba(103, 232, 249, 0.18), transparent 34%),
            radial-gradient(circle at top right, rgba(192, 132, 252, 0.18), transparent 38%),
            linear-gradient(135deg, rgba(255,255,255,0.97), rgba(242,244,255,0.95));
        border: 1px solid rgba(129, 140, 248, 0.14);
        border-radius: 24px;
        padding: 20px 16px;
        box-shadow: 0 12px 28px rgba(99, 102, 241, 0.08);
        text-align: center;
        margin-bottom: 14px;
        min-height: 126px;
    }

    .metric-top-line {
        width: 58%;
        height: 8px;
        border-radius: 999px;
        margin: 0 auto 16px auto;
        background: linear-gradient(90deg, #6366f1, #a855f7, #67e8f9);
    }

    .metric-label {
        color: #475569;
        font-size: 0.95rem;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .metric-value {
        color: #172b6a;
        font-size: 2rem;
        font-weight: 900;
        letter-spacing: -0.02em;
    }

    .section-header {
        display: flex;
        align-items: center;
        gap: 12px;
        background:
            linear-gradient(90deg, rgba(124, 58, 237, 0.10), rgba(103, 232, 249, 0.12));
        border: 1px solid rgba(129, 140, 248, 0.12);
        border-radius: 24px;
        padding: 16px 18px;
        margin-top: 22px;
        margin-bottom: 10px;
        box-shadow: 0 8px 22px rgba(99, 102, 241, 0.05);
        position: relative;
        overflow: hidden;
    }

    .section-header::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 14px;
        height: 100%;
        background: linear-gradient(180deg, #7c3aed, #6366f1);
        border-radius: 24px;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 900;
        color: #1e2f6f;
        margin-left: 10px;
        letter-spacing: -0.01em;
    }

    .content-card {
        background:
            radial-gradient(circle at bottom left, rgba(103, 232, 249, 0.12), transparent 30%),
            radial-gradient(circle at top right, rgba(216, 180, 254, 0.16), transparent 35%),
            linear-gradient(180deg, rgba(255,255,255,0.97), rgba(243,246,255,0.95));
        border: 1px solid rgba(129, 140, 248, 0.12);
        border-radius: 24px;
        padding: 14px;
        box-shadow: 0 14px 30px rgba(99, 102, 241, 0.06);
    }

    .glow-line {
        height: 6px;
        border-radius: 999px;
        margin-bottom: 12px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #67e8f9);
        opacity: 0.95;
    }

    .status-success {
        padding: 14px 16px;
        border-radius: 16px;
        background: linear-gradient(90deg, #e8fff1, #d9fbe7);
        color: #06603a;
        border: 1px solid #b7efcc;
        font-weight: 800;
        margin-bottom: 12px;
    }

    .status-warning {
        padding: 14px 16px;
        border-radius: 16px;
        background: linear-gradient(90deg, #fff6e8, #ffedd5);
        color: #9a3412;
        border: 1px solid #fdc98b;
        font-weight: 800;
        margin-bottom: 12px;
    }

    [data-testid="stDataFrame"] {
        border-radius: 18px;
        overflow: hidden;
        border: 1px solid rgba(129, 140, 248, 0.12);
    }

    .stDownloadButton > button {
        border-radius: 14px !important;
        border: 1px solid rgba(99, 102, 241, 0.16) !important;
        background: linear-gradient(135deg, #ffffff, #f3f6ff) !important;
        color: #243b7a !important;
        font-weight: 800 !important;
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.08) !important;
        padding: 0.55rem 1rem !important;
    }

    @media (max-width: 900px) {
        .hero-title {
            font-size: 1.85rem;
        }
        .metric-value {
            font-size: 1.55rem;
        }
        .sidebar-title {
            font-size: 1.65rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- DATA CLEAN ----------------
    local_df = df.copy()

    local_df.columns = local_df.columns.str.strip()
    local_df.columns = local_df.columns.str.replace(" ", "_")
    local_df.columns = local_df.columns.str.replace(r"[^\w]", "", regex=True)

    if "Day" in local_df.columns:
        local_df["Day"] = pd.to_numeric(local_df["Day"], errors="coerce")
        local_df = local_df.dropna(subset=["Day"]).copy()
        local_df["Day"] = local_df["Day"].astype(int)

        for col in local_df.columns:
            if col != "Day":
                local_df[col] = pd.to_numeric(local_df[col], errors="coerce")

        local_df = local_df.sort_values("Day").reset_index(drop=True)

        # ---------------- SIDEBAR ----------------
        st.sidebar.markdown('<div class="sidebar-title">🔎 Filtreleme</div>', unsafe_allow_html=True)
        st.sidebar.markdown(
            '<div class="sidebar-sub">Veriyi gün aralığı ve kolonlara göre filtrele.</div>',
            unsafe_allow_html=True
        )

        day_range = st.sidebar.slider(
            "Gün Aralığı",
            int(local_df["Day"].min()),
            int(local_df["Day"].max()),
            (int(local_df["Day"].min()), int(local_df["Day"].max()))
        )

        selected_columns = st.sidebar.multiselect(
            "Kolon Seç",
            local_df.columns.tolist(),
            default=local_df.columns.tolist()
        )

        if not selected_columns:
            st.warning("En az bir kolon seçmelisin.")
            st.stop()

        filtered_df = local_df[
            (local_df["Day"] >= day_range[0]) &
            (local_df["Day"] <= day_range[1])
        ][selected_columns]

        gun_araligi_text = f"{day_range[0]} - {day_range[1]}"

    else:
        st.sidebar.markdown('<div class="sidebar-title">🔎 Filtreleme</div>', unsafe_allow_html=True)
        st.sidebar.markdown(
            '<div class="sidebar-sub">Day kolonu olmadığı için sadece kolon bazlı filtreleme aktif.</div>',
            unsafe_allow_html=True
        )

        selected_columns = st.sidebar.multiselect(
            "Kolon Seç",
            local_df.columns.tolist(),
            default=local_df.columns.tolist()
        )

        if not selected_columns:
            st.warning("En az bir kolon seçmelisin.")
            st.stop()

        filtered_df = local_df[selected_columns]
        gun_araligi_text = "Yok"

    missing_count = int(filtered_df.isnull().sum().sum())
    numeric_df = filtered_df.select_dtypes(include="number")
    csv_data = filtered_df.to_csv(index=False).encode("utf-8-sig")

    # ---------------- HEADER ----------------
    st.markdown("""
    <div class="hero-card">
        <div class="hero-row">
            <div class="hero-icon"></div>
            <div class="hero-title">Veri Seti Analizi</div>
        </div>
        <div class="hero-subtitle">
            Sağlık operasyon verisini filtrele, incele, eksik verileri kontrol et ve özet istatistikleri düzenli,
            modern ve karar destek odaklı bir görünümde değerlendir.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- METRICS ----------------
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top-line"></div>
            <div class="metric-label">Toplam Satır</div>
            <div class="metric-value">{len(filtered_df)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top-line"></div>
            <div class="metric-label">Seçili Kolon</div>
            <div class="metric-value">{len(filtered_df.columns)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top-line"></div>
            <div class="metric-label">Eksik Veri</div>
            <div class="metric-value">{missing_count}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top-line"></div>
            <div class="metric-label">Gün Aralığı</div>
            <div class="metric-value" style="font-size:1.45rem;">{gun_araligi_text}</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- ACTIONS ----------------
    a1, a2 = st.columns([1, 5])
    with a1:
        st.download_button(
            label="📥 CSV İndir",
            data=csv_data,
            file_name="veri_seti_filtrelenmis.csv",
            mime="text/csv",
            use_container_width=True
        )

    # ---------------- DATA TABLE ----------------
    st.markdown("""
    <div class="section-header">
        <div class="section-title">📊 Veri Tablosu</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)
    st.dataframe(filtered_df, use_container_width=True, height=380)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- MISSING VALUES ----------------
    st.markdown("""
    <div class="section-header">
        <div class="section-title">⚠️ Eksik Veri Analizi</div>
    </div>
    """, unsafe_allow_html=True)

    missing = filtered_df.isnull().sum()
    missing = missing[missing > 0]

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

    if len(missing) > 0:
        st.markdown(
            f'<div class="status-warning">Toplam {int(missing.sum())} adet eksik veri bulundu.</div>',
            unsafe_allow_html=True
        )
        missing_df = missing.reset_index()
        missing_df.columns = ["Kolon", "Eksik Veri Sayısı"]
        st.dataframe(missing_df, use_container_width=True, hide_index=True)
    else:
        st.markdown(
            '<div class="status-success">Eksik veri yok ✅</div>',
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- STATS ----------------
    st.markdown("""
    <div class="section-header">
        <div class="section-title">📈 Özet İstatistik</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

    if not numeric_df.empty:
        st.dataframe(numeric_df.describe().T.round(2), use_container_width=True, height=320)
    else:
        st.info("Özet istatistik için sayısal kolon seçmelisin.")

    st.markdown('</div>', unsafe_allow_html=True)

    