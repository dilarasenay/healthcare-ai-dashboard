import streamlit as st
import pandas as pd
from textwrap import dedent


def show(df):
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        padding-top: 0.4rem;
    }

    header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0px;
    }

    .block-container {
        max-width: 1280px;
        padding-top: 2.2rem !important;
        padding-bottom: 2rem !important;
    }

    .kpi-header-wrap {
        position: relative;
        margin-top: 0.2rem;
        margin-bottom: 1rem;
    }

    .kpi-header-glow {
        position: absolute;
        top: -8px;
        left: 0;
        width: 340px;
        height: 90px;
        background: radial-gradient(circle, rgba(168,85,247,0.20) 0%, rgba(6,182,212,0.14) 45%, rgba(255,255,255,0) 75%);
        filter: blur(10px);
        z-index: 0;
    }

    .kpi-header {
        position: relative;
        z-index: 1;
        font-size: 2.9rem;
        font-weight: 900;
        line-height: 1.15;
        margin-bottom: 0.35rem;
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 35%, #a855f7 68%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .kpi-sub {
        position: relative;
        z-index: 1;
        color: #64748b;
        font-size: 1rem;
        font-weight: 500;
    }

    .group-title {
        font-size: 1.18rem;
        font-weight: 800;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        padding: 1rem 1.1rem;
        border-radius: 22px;
        background: linear-gradient(90deg, #eef2ff, #f5f3ff, #ecfeff);
        border: 1px solid #dbeafe;
        border-left: 8px solid #8b5cf6;
        box-shadow: 0 10px 26px rgba(99, 102, 241, 0.12);
        color: #1e1b4b;
    }

    .metric-card {
        position: relative;
        overflow: hidden;
        border-radius: 28px;
        padding: 18px 18px 16px 18px;
        min-height: 185px;
        background:
            radial-gradient(circle at top right, rgba(168,85,247,0.24), transparent 32%),
            radial-gradient(circle at bottom left, rgba(6,182,212,0.20), transparent 32%),
            linear-gradient(135deg, #ffffff 0%, #eef2ff 48%, #f5f3ff 100%);
        border: 1px solid #dbeafe;
        box-shadow:
            0 18px 40px rgba(124, 58, 237, 0.13),
            0 6px 20px rgba(6, 182, 212, 0.08);
        transition: transform .28s ease, box-shadow .28s ease, border-color .28s ease;
        margin-bottom: 18px;
    }

    .metric-card:hover {
        transform: translateY(-6px) scale(1.01);
        border-color: #c4b5fd;
        box-shadow:
            0 22px 45px rgba(124, 58, 237, 0.18),
            0 10px 26px rgba(6, 182, 212, 0.12);
    }

    .metric-card::before {
        content: "";
        position: absolute;
        top: -45px;
        right: -35px;
        width: 130px;
        height: 130px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(168,85,247,0.18), transparent 68%);
    }

    .metric-card::after {
        content: "";
        position: absolute;
        bottom: -55px;
        left: -35px;
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(34,211,238,0.16), transparent 68%);
    }

    .top-glow {
        height: 10px;
        width: 148px;
        border-radius: 999px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #67e8f9);
        margin-bottom: 0.95rem;
        box-shadow: 0 6px 20px rgba(129, 140, 248, 0.34);
        position: relative;
        z-index: 1;
    }

    .metric-head {
        display: flex;
        align-items: center;
        gap: 0.55rem;
        margin-bottom: 0.65rem;
        position: relative;
        z-index: 1;
    }

    .metric-icon {
        width: 38px;
        height: 38px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.05rem;
        background: linear-gradient(135deg, #ede9fe, #cffafe);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.8);
    }

    .metric-label {
        font-size: 0.97rem;
        font-weight: 800;
        color: #475569;
        line-height: 1.25;
    }

    .metric-value {
        font-size: 2.25rem;
        font-weight: 900;
        color: #172554;
        margin-top: 0.3rem;
        margin-bottom: 0.75rem;
        position: relative;
        z-index: 1;
    }

    .metric-delta {
        display: inline-block;
        padding: 0.38rem 0.82rem;
        border-radius: 999px;
        font-size: 0.86rem;
        font-weight: 800;
        position: relative;
        z-index: 1;
        box-shadow: 0 5px 14px rgba(0,0,0,0.05);
        margin-bottom: 0.8rem;
    }

    .delta-pos {
        background: linear-gradient(90deg, #dcfce7, #bbf7d0);
        color: #15803d;
    }

    .delta-neg {
        background: linear-gradient(90deg, #fee2e2, #fecaca);
        color: #b91c1c;
    }

    .delta-zero {
        background: linear-gradient(90deg, #ede9fe, #ddd6fe);
        color: #6d28d9;
    }

    .trend-badge {
        display: inline-block;
        padding: 0.42rem 0.75rem;
        border-radius: 14px;
        font-size: 0.82rem;
        font-weight: 700;
        background: rgba(255,255,255,0.55);
        border: 1px solid #dbeafe;
        color: #475569;
        position: relative;
        z-index: 1;
    }

    .summary-box {
        background:
            radial-gradient(circle at top right, rgba(168,85,247,0.16), transparent 32%),
            radial-gradient(circle at bottom left, rgba(6,182,212,0.13), transparent 32%),
            linear-gradient(135deg, #eef2ff, #f5f3ff, #ecfeff);
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 12px 30px rgba(124, 58, 237, 0.12);
        border: 1px solid #ddd6fe;
    }

    .summary-title {
        font-size: 2rem;
        font-weight: 900;
        margin-bottom: 1rem;
        color: #1e293b;
    }

    .summary-item {
        font-size: 1.04rem;
        margin-bottom: 0.62rem;
        color: #334155;
        line-height: 1.7;
        font-weight: 500;
    }

    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #67e8f9);
        border-radius: 999px;
        margin-top: 1.4rem !important;
        margin-bottom: 1.2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

    local_df = df.copy()

    local_df.columns = local_df.columns.str.strip()
    local_df.columns = local_df.columns.str.replace(" ", "_")
    local_df.columns = local_df.columns.str.replace(r"[^\w]", "", regex=True)

    if "Day" not in local_df.columns:
        st.error("KPI paneli için 'Day' kolonu gerekli.")
        return

    local_df["Day"] = pd.to_numeric(local_df["Day"], errors="coerce")
    local_df = local_df.dropna(subset=["Day"]).copy()
    local_df["Day"] = local_df["Day"].astype(int)

    for col in local_df.columns:
        if col != "Day":
            local_df[col] = pd.to_numeric(local_df[col], errors="coerce")

    local_df = local_df.sort_values("Day").reset_index(drop=True)

    if len(local_df) < 2:
        st.warning("KPI karşılaştırması için en az 2 günlük veri gerekli.")
        return

    last = local_df.iloc[-1]
    prev = local_df.iloc[-2]

    def delta(col):
        return round(float(last[col] - prev[col]), 2)

    def format_delta(d):
        if d > 0:
            return f"↑ {d}", "delta-pos"
        if d < 0:
            return f"↓ {abs(d)}", "delta-neg"
        return f"• {d}", "delta-zero"

    def trend_text(col_name):
        recent = local_df[col_name].dropna().tail(3).tolist()
        if len(recent) < 3:
            return "Trend izleniyor"
        if recent[-1] > recent[0]:
            return "Son günlerde yükseliş"
        if recent[-1] < recent[0]:
            return "Son günlerde düşüş"
        return "Stabil seyir"

    ICON_MAP = {
        "Daily_Patient_Admissions": "🧑‍🤝‍🧑",
        "Outpatient_Demand": "🩺",
        "Emergency_Department_Visits": "🚑",
        "Bed_Occupancy_Rate": "🛏️",
        "Average_Length_of_Stay": "⏳",
        "Service_Capacity_Utilization": "🏥",
        "Medical_Device_Utilization": "🧪",
        "Lab_Test_Count": "🔬",
        "Medical_Supply_Consumption": "💊",
        "Patients_per_Physician": "👨‍⚕️",
        "Patients_per_Nurse": "👩‍⚕️",
        "Staff_Capacity_Rate": "👥",
    }

    groups = {
        "🩺 Hizmet Talebi Göstergeleri": {
            "Günlük Hasta Başvurusu": "Daily_Patient_Admissions",
            "Poliklinik Yoğunluğu": "Outpatient_Demand",
            "Acil Servis Başvurusu": "Emergency_Department_Visits",
        },
        "🏥 Kapasite Kullanım Göstergeleri": {
            "Yatak Doluluk Oranı (%)": "Bed_Occupancy_Rate",
            "Ortalama Yatış Süresi": "Average_Length_of_Stay",
            "Servis Kapasite Kullanımı (%)": "Service_Capacity_Utilization",
        },
        "🧪 Kaynak Kullanım Göstergeleri": {
            "Cihaz Kullanım Oranı (%)": "Medical_Device_Utilization",
            "Laboratuvar Test Sayısı": "Lab_Test_Count",
            "Sarf Malzeme Tüketimi": "Medical_Supply_Consumption",
        },
        "👩‍⚕️ İş Gücü Kapasitesi Göstergeleri": {
            "Doktor Başına Hasta": "Patients_per_Physician",
            "Hemşire Başına Hasta": "Patients_per_Nurse",
            "Personel Kapasite Oranı (%)": "Staff_Capacity_Rate",
        }
    }

    def metric_card(label, value, diff, icon, trend):
        delta_text, delta_class = format_delta(diff)
        return dedent(f"""
        <div class="metric-card">
            <div class="top-glow"></div>
            <div class="metric-head">
                <div class="metric-icon">{icon}</div>
                <div class="metric-label">{label}</div>
            </div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta {delta_class}">{delta_text}</div>
            <div class="trend-badge">{trend}</div>
        </div>
        """)

    st.markdown(dedent("""
    <div class="kpi-header-wrap">
        <div class="kpi-header-glow"></div>
        <div class="kpi-header">📊 KPI Paneli</div>
        <div class="kpi-sub">Sağlık operasyon göstergeleri, değişimler ve kısa dönem trend görünümü</div>
    </div>
    """), unsafe_allow_html=True)

    for group_name, metrics in groups.items():
        st.markdown(f'<div class="group-title">{group_name}</div>', unsafe_allow_html=True)
        cols = st.columns(3)

        for i, (label, col_name) in enumerate(metrics.items()):
            with cols[i % 3]:
                if col_name in local_df.columns and pd.notna(last[col_name]) and pd.notna(prev[col_name]):
                    icon = ICON_MAP.get(col_name, "📈")
                    value = round(float(last[col_name]), 2)
                    diff = delta(col_name)
                    trend = trend_text(col_name)
                    st.markdown(metric_card(label, value, diff, icon, trend), unsafe_allow_html=True)
                else:
                    st.info(f"{label} kolonu veride bulunamadı.")

    st.markdown("---")

    def generate_insights(last_row, prev_row):
        insights = []

        if "Daily_Patient_Admissions" in local_df.columns and last_row["Daily_Patient_Admissions"] > prev_row["Daily_Patient_Admissions"]:
            insights.append("🔴 Hasta başvuruları artıyor, sistem yükü yükseliyor.")

        if "Bed_Occupancy_Rate" in local_df.columns and last_row["Bed_Occupancy_Rate"] > 90:
            insights.append("🔴 Yatak doluluk oranı kritik seviyede.")

        if "Patients_per_Physician" in local_df.columns and last_row["Patients_per_Physician"] > prev_row["Patients_per_Physician"]:
            insights.append("🟡 Doktor başına düşen hasta sayısı artıyor.")

        if "Medical_Device_Utilization" in local_df.columns and last_row["Medical_Device_Utilization"] > prev_row["Medical_Device_Utilization"]:
            insights.append("🟡 Cihaz kullanımı artıyor.")

        if "Medical_Supply_Consumption" in local_df.columns and last_row["Medical_Supply_Consumption"] > prev_row["Medical_Supply_Consumption"]:
            insights.append("🟡 Sarf malzeme tüketimi artıyor.")

        if not insights:
            insights.append("🟢 Sistem dengeli çalışıyor, kritik bir durum yok.")

        return insights

    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
    st.markdown('<div class="summary-title">📌 Kısa Değerlendirme</div>', unsafe_allow_html=True)

    for item in generate_insights(last, prev):
        st.markdown(f'<div class="summary-item">{item}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)