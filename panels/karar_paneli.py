import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go


def show(df):
    # =========================================================
    # DATA CHECK / CLEAN
    # =========================================================
    if df is None or df.empty:
        st.warning("Veri bulunamadı.")
        return

    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )

    rename_map = {
        "DailyPatientAdmissions": "Daily_Patient_Admissions",
        "Daily_Patient_Admissions": "Daily_Patient_Admissions",
        "BedOccupancyRate": "Bed_Occupancy_Rate",
        "Bed_Occupancy_Rate": "Bed_Occupancy_Rate",
        "PatientsperPhysician": "Patients_per_Physician",
        "Patients_per_Physician": "Patients_per_Physician",
        "EquipmentUtilization": "Equipment_Utilization",
        "Equipment_Utilization": "Equipment_Utilization",
        "Medical_Device_Utilization": "Equipment_Utilization",
        "MedicalSuppliesConsumption": "Medical_Supplies_Consumption",
        "Medical_Supplies_Consumption": "Medical_Supplies_Consumption",
        "Medical_Supply_Consumption": "Medical_Supplies_Consumption",
    }
    df = df.rename(columns=rename_map)

    required_cols = [
        "Day",
        "Daily_Patient_Admissions",
        "Bed_Occupancy_Rate",
        "Patients_per_Physician",
        "Equipment_Utilization",
        "Medical_Supplies_Consumption",
    ]

    for col in required_cols:
        if col not in df.columns:
            df[col] = np.nan

    df["Day"] = pd.to_numeric(df["Day"], errors="coerce")
    for col in required_cols[1:]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["Day"]).copy()
    if df.empty:
        st.error("Geçerli gün bilgisi içeren veri bulunamadı.")
        return

    df["Day"] = df["Day"].astype(int)
    df = df.sort_values("Day").reset_index(drop=True)

    for col in required_cols[1:]:
        if not df[col].isna().all():
            df[col] = df[col].interpolate().bfill().ffill()

    # =========================================================
    # CALCULATIONS
    # =========================================================
    last_day = int(df["Day"].max())
    last_admissions = float(df["Daily_Patient_Admissions"].iloc[-1])
    last_bed = float(df["Bed_Occupancy_Rate"].iloc[-1])
    last_physician = float(df["Patients_per_Physician"].iloc[-1])

    last_equipment = df["Equipment_Utilization"].iloc[-1]
    last_supply = df["Medical_Supplies_Consumption"].iloc[-1]

    last_equipment = None if pd.isna(last_equipment) else float(last_equipment)
    last_supply = None if pd.isna(last_supply) else float(last_supply)

    equipment_text = f"%{last_equipment:.1f}" if last_equipment is not None else "Veri yok"
    supply_text = f"{last_supply:.1f}" if last_supply is not None else "Veri yok"

    x = df["Day"].values
    y = df["Daily_Patient_Admissions"].values
    coef = np.polyfit(x, y, 1)
    pred_31 = int(round(np.polyval(coef, 31)))
    pred_32 = int(round(np.polyval(coef, 32)))

    corr_val = df["Daily_Patient_Admissions"].corr(df["Bed_Occupancy_Rate"])

    admissions_delta = (
        float(df["Daily_Patient_Admissions"].iloc[-1] - df["Daily_Patient_Admissions"].iloc[-2])
        if len(df) > 1 else 0
    )
    bed_delta = (
        float(df["Bed_Occupancy_Rate"].iloc[-1] - df["Bed_Occupancy_Rate"].iloc[-2])
        if len(df) > 1 else 0
    )

    risk_score = 0
    if last_bed >= 95:
        risk_score += 3
    elif last_bed >= 90:
        risk_score += 2
    else:
        risk_score += 1

    if last_physician >= 44:
        risk_score += 3
    elif last_physician >= 38:
        risk_score += 2
    else:
        risk_score += 1

    if last_equipment is not None:
        if last_equipment >= 95:
            risk_score += 2
        elif last_equipment >= 88:
            risk_score += 1

    if risk_score >= 7:
        risk_label = "Kritik"
        risk_note = "Anında müdahale gerekli"
        risk_color = "#FF4D7A"
        risk_glow = "rgba(255,77,122,0.20)"
    elif risk_score >= 5:
        risk_label = "Dikkat"
        risk_note = "Yakın takip önerilir"
        risk_color = "#F59E0B"
        risk_glow = "rgba(245,158,11,0.16)"
    else:
        risk_label = "Kontrollü"
        risk_note = "Operasyon dengeli"
        risk_color = "#22C55E"
        risk_glow = "rgba(34,197,94,0.16)"

    if last_bed >= 95:
        primary_message = (
            "Kapasite kritik eşiğe ulaştı. Yatak, servis akışı ve doktor planlaması "
            "eş zamanlı olarak güncellenmelidir."
        )
    elif last_bed >= 90:
        primary_message = (
            "Talep artışı kapasite üzerinde baskı oluşturuyor. Önleyici hizmet planı ve "
            "vardiya optimizasyonu önerilmektedir."
        )
    else:
        primary_message = (
            "Operasyon kontrollü görünmektedir; ancak artan talep eğilimi nedeniyle "
            "proaktif planlama sürdürülmelidir."
        )

    # =========================================================
    # STYLE
    # =========================================================
    st.markdown("""
<style>
:root {
    --text-main: #132866;
    --text-soft: #5C6C98;

    --primary: #5B4CF0;
    --primary-2: #8B5CF6;
    --cyan: #56CCF2;
    --cyan-2: #39C7F5;
    --pink: #FF5FD2;
    --pink-soft: #FF9AE8;
    --red-strong: #FF4D7A;
    --amber: #F59E0B;
    --success: #22C55E;

    --shadow-soft: 0 12px 28px rgba(49, 63, 120, 0.08);
    --shadow-mid: 0 16px 34px rgba(49, 63, 120, 0.10);
    --shadow-strong: 0 18px 42px rgba(49, 63, 120, 0.12);
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(91,76,240,0.13), transparent 22%),
        radial-gradient(circle at 90% 12%, rgba(57,199,245,0.12), transparent 24%),
        radial-gradient(circle at 18% 82%, rgba(255,95,210,0.07), transparent 18%),
        linear-gradient(135deg, #f7f8ff 0%, #f5f8ff 48%, #eef7ff 100%);
}

.block-container {
    max-width: 1320px;
    padding-top: 1.15rem !important;
    padding-bottom: 3rem !important;
}

.space-sm { height: 8px; }
.space-md { height: 14px; }
.space-lg { height: 22px; }

.hero-wrap {
    background: linear-gradient(135deg, rgba(255,255,255,0.84), rgba(239,246,255,0.96));
    border: 1px solid rgba(91,76,240,0.08);
    border-radius: 30px;
    padding: 28px 30px;
    box-shadow: var(--shadow-strong);
    position: relative;
    overflow: hidden;
    min-height: 210px;
}

.hero-wrap::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 88% 18%, rgba(57,199,245,0.16), transparent 24%),
        radial-gradient(circle at 15% 15%, rgba(139,92,246,0.12), transparent 22%);
    pointer-events: none;
}

.hero-badge {
    display: inline-block;
    padding: 9px 15px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(91,76,240,0.14), rgba(57,199,245,0.16));
    color: #4E46E5;
    font-size: 0.82rem;
    font-weight: 900;
    margin-bottom: 14px;
    position: relative;
    z-index: 2;
}

.hero-title {
    font-size: 2.95rem;
    font-weight: 900;
    line-height: 1.02;
    letter-spacing: -0.03em;
    color: #10245F;
    margin-bottom: 12px;
    position: relative;
    z-index: 2;
}

.hero-desc {
    font-size: 1.04rem;
    line-height: 1.9;
    color: #55668F;
    max-width: 760px;
    position: relative;
    z-index: 2;
}

.status-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.92), rgba(248,251,255,0.99));
    border: 1px solid rgba(91,76,240,0.10);
    border-radius: 28px;
    padding: 22px 22px 18px 22px;
    box-shadow: var(--shadow-strong);
    min-height: 210px;
    position: relative;
    overflow: hidden;
}

.status-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 90% 12%, rgba(57,199,245,0.08), transparent 26%);
    pointer-events: none;
}

.status-label {
    color: #7A86AB;
    font-size: 0.82rem;
    font-weight: 900;
    letter-spacing: 0.08em;
    margin-bottom: 14px;
    text-transform: uppercase;
    position: relative;
    z-index: 2;
}

.status-value {
    font-size: 2.1rem;
    font-weight: 900;
    margin-bottom: 8px;
    letter-spacing: -0.02em;
    position: relative;
    z-index: 2;
}

.status-note {
    color: #5B6C97;
    line-height: 1.8;
    font-size: 0.97rem;
    position: relative;
    z-index: 2;
}

.kpi-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.90), rgba(244,248,255,0.98));
    border: 1px solid rgba(91,76,240,0.08);
    border-radius: 26px;
    padding: 18px 18px 16px 18px;
    box-shadow: var(--shadow-soft);
    min-height: 172px;
    position: relative;
    overflow: hidden;
    margin-bottom: 8px;
}

.kpi-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 14px;
    width: 118px;
    height: 5px;
    border-radius: 999px;
    background: linear-gradient(90deg, #5B4CF0 0%, #39C7F5 100%);
}

.kpi-card::after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 88% 12%, rgba(139,92,246,0.08), transparent 24%);
    pointer-events: none;
}

.kpi-risk {
    background: linear-gradient(145deg, rgba(255,243,247,0.98), rgba(255,239,244,0.99));
    border: 1px solid rgba(255,77,122,0.22);
    box-shadow: 0 14px 30px rgba(255,77,122,0.12);
}

.kpi-label {
    color: #62739C;
    font-size: 0.95rem;
    font-weight: 800;
    margin-top: 14px;
    margin-bottom: 10px;
    position: relative;
    z-index: 2;
}

.kpi-value {
    color: #132866;
    font-size: 2.2rem;
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: 8px;
    letter-spacing: -0.03em;
    position: relative;
    z-index: 2;
}

.kpi-foot {
    color: #4E46E5;
    font-size: 0.90rem;
    font-weight: 700;
    position: relative;
    z-index: 2;
}

.mini-chip {
    display: inline-block;
    margin-top: 12px;
    padding: 8px 12px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(91,76,240,0.08), rgba(57,199,245,0.08));
    color: #4E46E5;
    font-size: 0.79rem;
    font-weight: 800;
    position: relative;
    z-index: 2;
}

.section-box {
    background: linear-gradient(90deg, rgba(255,255,255,0.82), rgba(226,243,255,0.92));
    border: 1px solid rgba(91,76,240,0.08);
    border-radius: 24px;
    padding: 17px 20px 17px 22px;
    color: #10245F;
    font-size: 1.22rem;
    font-weight: 900;
    letter-spacing: -0.01em;
    margin: 30px 0 22px 0;
    box-shadow: 0 10px 24px rgba(45, 60, 115, 0.06);
    position: relative;
    overflow: hidden;
}

.section-box::before {
    content: "";
    position: absolute;
    left: 0;
    top: 10px;
    bottom: 10px;
    width: 6px;
    border-radius: 999px;
    background: linear-gradient(180deg, #8B5CF6 0%, #39C7F5 100%);
}

.section-box::after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(139,92,246,0.03), transparent 30%, rgba(57,199,245,0.04) 100%);
    pointer-events: none;
}

.glass-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.92), rgba(243,247,255,0.99));
    border: 1px solid rgba(91,76,240,0.08);
    border-radius: 28px;
    padding: 24px 22px 22px 22px;
    box-shadow: var(--shadow-mid);
    min-height: 374px;
    margin-top: 8px;
    position: relative;
    overflow: hidden;
}

.glass-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 85% 15%, rgba(57,199,245,0.14), transparent 22%),
        radial-gradient(circle at 12% 88%, rgba(139,92,246,0.10), transparent 20%);
    pointer-events: none;
}

.insight-label {
    display: inline-block;
    padding: 8px 13px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(245,158,11,0.16), rgba(255,95,210,0.08));
    color: #B45309;
    font-size: 0.78rem;
    font-weight: 900;
    margin-bottom: 14px;
    position: relative;
    z-index: 2;
}

.insight-title {
    color: #132866;
    font-size: 1.28rem;
    font-weight: 900;
    margin-bottom: 12px;
    position: relative;
    z-index: 2;
}

.insight-text {
    color: #4F608A;
    line-height: 1.92;
    font-size: 1rem;
    margin-bottom: 14px;
    position: relative;
    z-index: 2;
}

.tag-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
}

.tag {
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 900;
    color: #4E46E5;
    background: linear-gradient(90deg, rgba(91,76,240,0.08), rgba(57,199,245,0.08));
}

.risk-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.92), rgba(244,248,255,0.99));
    border: 1px solid rgba(91,76,240,0.08);
    border-radius: 26px;
    padding: 20px;
    box-shadow: var(--shadow-soft);
    min-height: 196px;
    position: relative;
    overflow: hidden;
}

.risk-card::after {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 88% 12%, rgba(139,92,246,0.05), transparent 25%);
    pointer-events: none;
}

.risk-card.red { border-left: 6px solid #FF4D7A; }
.risk-card.amber { border-left: 6px solid #F59E0B; }
.risk-card.cyan { border-left: 6px solid #39C7F5; }

.risk-chip {
    display: inline-block;
    padding: 8px 13px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 900;
    margin-bottom: 14px;
    position: relative;
    z-index: 2;
}

.risk-chip.red {
    background: linear-gradient(90deg, rgba(255,77,122,0.16), rgba(255,127,164,0.10));
    color: #E11D48;
    border: 1px solid rgba(255,77,122,0.16);
}

.risk-chip.amber {
    background: rgba(245,158,11,0.15);
    color: #B45309;
    border: 1px solid rgba(245,158,11,0.14);
}

.risk-chip.cyan {
    background: rgba(57,199,245,0.14);
    color: #007FA6;
    border: 1px solid rgba(57,199,245,0.14);
}

.risk-title {
    color: #152968;
    font-size: 1.2rem;
    font-weight: 900;
    margin-bottom: 10px;
    position: relative;
    z-index: 2;
}

.risk-text {
    color: #53648E;
    font-size: 0.98rem;
    line-height: 1.82;
    position: relative;
    z-index: 2;
}

.chart-shell {
    background: linear-gradient(145deg, rgba(255,255,255,0.88), rgba(244,248,255,0.98));
    border: 1px solid rgba(91,76,240,0.08);
    border-radius: 24px;
    padding: 12px 14px 4px 14px;
    box-shadow: var(--shadow-soft);
    margin-bottom: 6px;
    position: relative;
    overflow: hidden;
}

.chart-shell::before {
    content: "";
    position: absolute;
    top: 0;
    left: 16px;
    width: 148px;
    height: 5px;
    border-radius: 999px;
    background: linear-gradient(90deg, #5B4CF0 0%, #8B5CF6 48%, #39C7F5 100%);
}

.analysis-table-shell {
    background: linear-gradient(145deg, rgba(255,255,255,0.92), rgba(244,248,255,0.99));
    border: 1px solid rgba(91,76,240,0.10);
    border-radius: 24px;
    padding: 16px;
    box-shadow: 0 12px 28px rgba(45, 60, 115, 0.08);
    position: relative;
    overflow: hidden;
}

.analysis-table-shell::before {
    content: "";
    position: absolute;
    left: 0;
    top: 14px;
    bottom: 14px;
    width: 6px;
    border-radius: 999px;
    background: linear-gradient(180deg, #8B5CF6 0%, #39C7F5 100%);
}

.analysis-mini-badge {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 999px;
    background: linear-gradient(90deg, rgba(91,76,240,0.10), rgba(57,199,245,0.10));
    color: #4E46E5;
    font-size: 0.76rem;
    font-weight: 900;
    margin-bottom: 12px;
}

.analysis-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.94), rgba(242,247,255,0.99));
    border: 1px solid rgba(91,76,240,0.10);
    border-radius: 26px;
    padding: 20px;
    box-shadow: 0 14px 30px rgba(45,60,115,0.09);
    position: relative;
    overflow: hidden;
}

.analysis-card::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 85% 15%, rgba(57,199,245,0.12), transparent 22%),
        radial-gradient(circle at 12% 88%, rgba(139,92,246,0.10), transparent 20%);
    pointer-events: none;
}

.decision-stack {
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-top: 4px;
}

.decision-action {
    position: relative;
    border-radius: 26px;
    padding: 20px 20px 18px 20px;
    overflow: hidden;
    transition: all 0.24s ease;
    border: 1px solid rgba(255,255,255,0.38);
    box-shadow: 0 12px 26px rgba(45,60,115,0.08);
}

.decision-action:hover {
    transform: translateY(-4px);
    box-shadow: 0 18px 36px rgba(45,60,115,0.12);
}

.decision-action::before {
    content: "";
    position: absolute;
    left: 0;
    top: 14px;
    bottom: 14px;
    width: 6px;
    border-radius: 999px;
}

.decision-action::after {
    content: "";
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top right, rgba(255,255,255,0.56), transparent 34%);
    pointer-events: none;
}

.decision-action.high {
    background: linear-gradient(135deg, #fff2f7 0%, #fff8fb 50%, #ffeef8 100%);
    border: 1px solid rgba(255,95,210,0.18);
}

.decision-action.high::before {
    background: linear-gradient(180deg, #FF4D7A 0%, #FF7CC7 100%);
}

.decision-action.medium {
    background: linear-gradient(135deg, #fff8ee 0%, #fffaf4 50%, #fff3e2 100%);
    border: 1px solid rgba(245,158,11,0.18);
}

.decision-action.medium::before {
    background: linear-gradient(180deg, #F59E0B 0%, #FFC857 100%);
}

.decision-action.low {
    background: linear-gradient(135deg, #eefdf3 0%, #f7fef9 50%, #eafaf0 100%);
    border: 1px solid rgba(34,197,94,0.17);
}

.decision-action.low::before {
    background: linear-gradient(180deg, #22C55E 0%, #6EE7A4 100%);
}

.decision-top {
    display: flex;
    justify-content: space-between;
    gap: 14px;
    align-items: flex-start;
    margin-bottom: 14px;
    position: relative;
    z-index: 2;
}

.decision-name {
    color: #132866;
    font-size: 1.08rem;
    font-weight: 900;
    line-height: 1.45;
    letter-spacing: -0.01em;
}

.decision-badge {
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 0.73rem;
    font-weight: 800;
    white-space: nowrap;
    position: relative;
    z-index: 2;
}

.priority-high {
    background: linear-gradient(90deg, rgba(255,77,122,0.14), rgba(255,95,210,0.10));
    color: #E11D48;
    border: 1px solid rgba(225,29,72,0.12);
}

.priority-medium {
    background: rgba(245,158,11,0.14);
    color: #B45309;
    border: 1px solid rgba(180,83,9,0.14);
}

.priority-low {
    background: rgba(34,197,94,0.12);
    color: #15803D;
    border: 1px solid rgba(21,128,61,0.14);
}

.decision-desc {
    color: #55668F;
    font-size: 0.98rem;
    line-height: 1.86;
    position: relative;
    z-index: 2;
}

.manager-note {
    background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(238,247,255,0.97));
    border: 1px solid rgba(91,76,240,0.10);
    border-radius: 30px;
    padding: 24px 24px 22px 24px;
    box-shadow: 0 14px 30px rgba(45,60,115,0.08);
    position: relative;
    overflow: hidden;
    margin-top: 24px;
}

.manager-note::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 88% 16%, rgba(57,199,245,0.12), transparent 24%),
        radial-gradient(circle at 12% 88%, rgba(139,92,246,0.10), transparent 20%);
    pointer-events: none;
}

.manager-note::after {
    content: "";
    position: absolute;
    top: 0;
    left: 18px;
    width: 132px;
    height: 5px;
    border-radius: 999px;
    background: linear-gradient(90deg, #5B4CF0 0%, #8B5CF6 48%, #39C7F5 100%);
}

.manager-title {
    color: #142865;
    font-size: 1.3rem;
    font-weight: 900;
    margin-bottom: 12px;
    position: relative;
    z-index: 2;
}

.manager-text {
    color: #55668F;
    font-size: 1rem;
    line-height: 1.95;
    position: relative;
    z-index: 2;
}

.manager-tag-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 14px;
    position: relative;
    z-index: 2;
}

.manager-tag {
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 900;
    color: #4E46E5;
    background: linear-gradient(90deg, rgba(91,76,240,0.08), rgba(57,199,245,0.08));
}

div[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

    # =========================================================
    # HELPERS
    # =========================================================
    def render_kpi(label, value, foot, chip=None, risk=False):
        extra_class = "kpi-risk" if risk else ""
        chip_html = f'<div class="mini-chip">{chip}</div>' if chip else ""
        st.markdown(
            f"""<div class="kpi-card {extra_class}">
<div class="kpi-label">{label}</div>
<div class="kpi-value">{value}</div>
<div class="kpi-foot">{foot}</div>
{chip_html}
</div>""",
            unsafe_allow_html=True,
        )

    def section_title(text):
        st.markdown(f"""<div class="section-box">{text}</div>""", unsafe_allow_html=True)
        st.markdown("""<div class="space-md"></div>""", unsafe_allow_html=True)

    def card_line_chart(data, x_col, y_col, title, line_color, fill_color):
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=data[x_col],
                y=data[y_col],
                mode="lines+markers",
                line=dict(color=line_color, width=3.4),
                marker=dict(size=4.8, color=line_color),
                fill="tozeroy",
                fillcolor=fill_color,
                hovertemplate=f"<b>{title}</b><br>Gün: %{{x}}<br>Değer: %{{y}}<extra></extra>",
            )
        )

        fig.update_layout(
            title=dict(text=title, font=dict(size=16, color="#172B6A")),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(255,255,255,0)",
            margin=dict(l=8, r=8, t=42, b=8),
            height=250,
            xaxis=dict(
                title="Day",
                showgrid=True,
                gridcolor="rgba(120,140,180,0.12)",
                zeroline=False,
                tickfont=dict(color="#6C7AA0"),
                title_font=dict(color="#6C7AA0"),
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor="rgba(120,140,180,0.12)",
                zeroline=False,
                tickfont=dict(color="#6C7AA0"),
                title_font=dict(color="#6C7AA0"),
            ),
            font=dict(color="#55668F"),
        )
        return fig

    # =========================================================
    # HERO
    # =========================================================
    hero_left, hero_right = st.columns([1.95, 1])

    with hero_left:
        st.markdown(
            """<div class="hero-wrap">
<div class="hero-badge">Executive Decision Intelligence</div>
<div class="hero-title">Stratejik Karar Paneli</div>
<div class="hero-desc">
Operasyonel sağlık göstergelerini tek ekranda yorumlayan, kısa vadeli hasta başvurusu
tahmini üreten ve yönetime kapasite, iş gücü ve kaynak planlaması için uygulanabilir
aksiyonlar sunan stratejik karar görünümü.
</div>
</div>""",
            unsafe_allow_html=True,
        )

    with hero_right:
        st.markdown(
            f"""<div class="status-card" style="box-shadow: 0 16px 34px {risk_glow};">
<div class="status-label">Operasyonel Risk Durumu</div>
<div class="status-value" style="color:{risk_color};">{risk_label}</div>
<div class="status-note">
{risk_note}. Son gün doluluk <b>%{last_bed:.1f}</b> ve
kısa vadeli tahmin <b>{pred_31:,}</b> seviyesindedir.
</div>
</div>""",
            unsafe_allow_html=True,
        )

    st.markdown("""<div class="space-lg"></div>""", unsafe_allow_html=True)

    # =========================================================
    # KPI ROW
    # =========================================================
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_kpi(
            "Güncel Başvuru Hacmi",
            f"{int(last_admissions):,}",
            f"Gün {last_day} gerçekleşen seviye",
            chip=f"{admissions_delta:+.0f} günlük değişim"
        )

    with c2:
        render_kpi(
            "Kısa Vadeli Talep Tahmini",
            f"{pred_31:,}",
            "Yakın dönem başvuru öngörüsü",
            chip=f"32. gün: {pred_32:,}"
        )

    with c3:
        render_kpi(
            "Yatak Doluluk Oranı",
            f"%{last_bed:.1f}",
            "Anlık kapasite görünümü",
            chip=f"{bed_delta:+.1f} puan değişim"
        )

    with c4:
        render_kpi(
            "Operasyonel Risk Seviyesi",
            risk_label,
            "Genel alarm durumu",
            chip=risk_note,
            risk=True
        )

    st.markdown("""<div class="space-lg"></div>""", unsafe_allow_html=True)

    # =========================================================
    # TREND + INSIGHT
    # =========================================================
    section_title("Başvuru Trendleri ve Yönetici İçgörüsü")
    left, right = st.columns([1.85, 1])

    with left:
        actual_df = df[["Day", "Daily_Patient_Admissions"]].copy()
        pred_df = pd.DataFrame({
            "Day": [31, 32],
            "Daily_Patient_Admissions": [pred_31, pred_32]
        })

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=actual_df["Day"],
            y=actual_df["Daily_Patient_Admissions"],
            mode="lines+markers",
            name="Gerçek Veri",
            line=dict(color="#5B4CF0", width=3.6),
            marker=dict(size=5.0, color="#5B4CF0"),
            fill="tozeroy",
            fillcolor="rgba(91,76,240,0.09)",
            hovertemplate="<b>Gerçek Veri</b><br>Gün: %{x}<br>Başvuru: %{y}<extra></extra>"
        ))

        fig.add_trace(go.Scatter(
            x=pred_df["Day"],
            y=pred_df["Daily_Patient_Admissions"],
            mode="lines+markers",
            name="Tahmin",
            line=dict(color="#39C7F5", width=3.4, dash="dot"),
            marker=dict(size=5.8, color="#39C7F5"),
            hovertemplate="<b>Tahmin</b><br>Gün: %{x}<br>Başvuru: %{y}<extra></extra>"
        ))

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(255,255,255,0)",
            margin=dict(l=8, r=8, t=10, b=8),
            height=360,
            xaxis=dict(
                title="Gün",
                showgrid=True,
                gridcolor="rgba(120,140,180,0.14)",
                zeroline=False,
                tickfont=dict(color="#6C7AA0"),
                title_font=dict(color="#6C7AA0"),
            ),
            yaxis=dict(
                title="Hasta Başvurusu",
                showgrid=True,
                gridcolor="rgba(120,140,180,0.14)",
                zeroline=False,
                tickfont=dict(color="#6C7AA0"),
                title_font=dict(color="#6C7AA0"),
            ),
            legend=dict(orientation="h", y=1.08, x=0, bgcolor="rgba(255,255,255,0)"),
            font=dict(color="#55668F"),
        )

        st.plotly_chart(fig, width="stretch")

    with right:
        st.markdown(
            f"""<div class="glass-card">
<div class="insight-label">AI Executive Insight</div>
<div class="insight-title">Stratejik Yönetim Özeti</div>
<div class="insight-text">
{primary_message}
Model, <b>31. gün için {pred_31:,}</b> ve <b>32. gün için {pred_32:,}</b>
başvuru beklemektedir. Son görünümde doktor başına yük <b>{last_physician:.1f}</b>,
cihaz kullanım oranı <b>{equipment_text}</b> seviyesindedir.
</div>
<div class="tag-row">
<div class="tag">Demand Growth</div>
<div class="tag">Capacity Pressure</div>
<div class="tag">Staff Load</div>
<div class="tag">Action Required</div>
</div>
</div>""",
            unsafe_allow_html=True,
        )

    # =========================================================
    # RISK AREAS
    # =========================================================
    section_title("Kritik Risk Alanları")
    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown(
            f"""<div class="risk-card red">
<div class="risk-chip red">Kapasite Riski</div>
<div class="risk-title">Yatak Doluluk Baskısı</div>
<div class="risk-text">
Yatak doluluk oranı şu anda <b>%{last_bed:.1f}</b>. Bu görünüm servis akışında
esnekliği azaltır ve ani talep artışlarında darboğaz oluşturabilir.
</div>
</div>""",
            unsafe_allow_html=True,
        )

    with r2:
        st.markdown(
            f"""<div class="risk-card amber">
<div class="risk-chip amber">İş Gücü Riski</div>
<div class="risk-title">Doktor Başına Hasta Yükü</div>
<div class="risk-text">
Doktor başına hasta göstergesi <b>{last_physician:.1f}</b>. Bu artış; bekleme süresi,
vardiya verimliliği ve hizmet kalitesi üzerinde baskı yaratabilir.
</div>
</div>""",
            unsafe_allow_html=True,
        )

    with r3:
        st.markdown(
            f"""<div class="risk-card cyan">
<div class="risk-chip cyan">Kaynak Riski</div>
<div class="risk-title">Cihaz ve Sarf Kullanımı</div>
<div class="risk-text">
Cihaz kullanım oranı <b>{equipment_text}</b>, sarf tüketimi <b>{supply_text}</b>.
Bu yapı bakım, tedarik ve stok planlamasını daha kritik hale getirir.
</div>
</div>""",
            unsafe_allow_html=True,
        )

    # =========================================================
    # CORE METRICS
    # =========================================================
    section_title("Karar Destek Göstergeleri")
    g1, g2, g3 = st.columns(3)

    with g1:
        st.markdown('<div class="chart-shell">', unsafe_allow_html=True)
        st.plotly_chart(
            card_line_chart(df, "Day", "Daily_Patient_Admissions", "Günlük Hasta Başvurusu", "#5B4CF0", "rgba(91,76,240,0.09)"),
            width="stretch"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with g2:
        st.markdown('<div class="chart-shell">', unsafe_allow_html=True)
        st.plotly_chart(
            card_line_chart(df, "Day", "Bed_Occupancy_Rate", "Yatak Doluluk Oranı", "#39C7F5", "rgba(57,199,245,0.10)"),
            width="stretch"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with g3:
        st.markdown('<div class="chart-shell">', unsafe_allow_html=True)
        st.plotly_chart(
            card_line_chart(df, "Day", "Patients_per_Physician", "Doktor Başına Hasta", "#8B5CF6", "rgba(139,92,246,0.10)"),
            width="stretch"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================
    # RELATIONSHIP ANALYSIS
    # =========================================================
    section_title("Talep ve Kapasite İlişkisi")
    a1, a2 = st.columns([1.05, 1])

    with a1:
        analysis_df = pd.DataFrame({
            "Analiz Başlığı": [
                "Korelasyon Katsayısı",
                "İlişki Düzeyi",
                "Talep Trendi",
                "Kapasite Yorumu"
            ],
            "Sonuç": [
                f"{corr_val:.3f}",
                "Çok güçlü ilişki" if corr_val >= 0.85 else "Orta ilişki",
                "Artan",
                "Kritik" if last_bed >= 95 else "Dikkat" if last_bed >= 90 else "Kontrollü"
            ]
        })

        st.markdown('<div class="analysis-table-shell"><div class="analysis-mini-badge">Capacity Analytics</div>', unsafe_allow_html=True)
        st.dataframe(analysis_df, width="stretch", hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with a2:
        st.markdown(
            f"""<div class="analysis-card">
<div class="insight-title">Analitik Değerlendirme</div>
<div class="insight-text">
Günlük hasta başvurusu ile yatak doluluk oranı arasında <b>{corr_val:.3f}</b>
seviyesinde güçlü bir ilişki vardır. Bu görünüm, talep artışının kapasiteye doğrudan
baskı uyguladığını göstermektedir. Özellikle doluluk oranının <b>%{last_bed:.1f}</b>
seviyesine çıkması, kapasite planlaması ile personel dağılımının birlikte ele alınmasını
zorunlu hale getirir.
</div>
<div class="tag-row">
<div class="tag">High Correlation</div>
<div class="tag">Resource Planning</div>
<div class="tag">Capacity Review</div>
</div>
</div>""",
            unsafe_allow_html=True,
        )

    # =========================================================
    # ACTIONS
    # =========================================================
    section_title("Yönetim İçin Öncelikli Aksiyonlar")

    decisions = [
        (
            "Poliklinik kapasitesini artır",
            "Randevu akışı ve poliklinik kapasitesi kısa dönem talep eğrisine göre yeniden dengelenmelidir.",
            "Yüksek Öncelik",
            "high",
        ),
        (
            "Taburculuk planını hızlandır",
            "Yatak devir hızını artırmak için servis çıkış planı günlük operasyon toplantılarında izlenmelidir.",
            "Yüksek Öncelik",
            "high",
        ),
        (
            "Ek vardiya ve görev dağılımı yap",
            "Personel yükünü azaltmak için vardiya ve görev dağılımı yeniden optimize edilmelidir.",
            "Orta Öncelik",
            "medium",
        ),
        (
            "Cihaz kullanım planını optimize et",
            "Yoğun kullanılan cihazlar için bakım ve kullanım sıralaması operasyon yoğunluğuna göre düzenlenmelidir.",
            "Orta Öncelik",
            "medium",
        ),
        (
            "Sarf stok eşiğini güncelle",
            "Kısa dönem talep projeksiyonuna göre kritik sarf stok seviyeleri yeniden belirlenmelidir.",
            "Düşük Öncelik",
            "low",
        ),
    ]

    cards_html = '<div class="decision-stack">'

    for name, desc, badge, level in decisions:
        badge_class = (
            "priority-high" if level == "high"
            else "priority-medium" if level == "medium"
            else "priority-low"
        )

        cards_html += f"""<div class="decision-action {level}">
<div class="decision-top">
<div class="decision-name">{name}</div>
<div class="decision-badge {badge_class}">{badge}</div>
</div>
<div class="decision-desc">{desc}</div>
</div>"""

    cards_html += "</div>"

    st.markdown(cards_html, unsafe_allow_html=True)

    st.markdown(
        f"""<div class="manager-note">
<div class="manager-title">Üst Yönetim Değerlendirmesi</div>
<div class="manager-text">
Kurumun mevcut görünümünde ana problem tek bir metrik değildir; <b>talep, kapasite ve iş gücü</b>
aynı anda yükselmektedir. Özellikle <b>{pred_31:,}</b> ve <b>{pred_32:,}</b> seviyesindeki
kısa vadeli başvuru beklentisi, yönetimin reaktif değil proaktif hareket etmesini gerektirir.
En doğru yaklaşım; kısa dönem hizmet planı, doktor dağılımı, yatak yönetimi ve kaynak kullanımını
tek karar çerçevesinde toplamaktır.
</div>
<div class="manager-tag-row">
<div class="manager-tag">Executive Action Plan</div>
<div class="manager-tag">Capacity Governance</div>
<div class="manager-tag">Operational Response</div>
</div>
</div>""",
        unsafe_allow_html=True,
    )