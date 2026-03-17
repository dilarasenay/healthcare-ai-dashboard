import streamlit as st
import pandas as pd
import numpy as np


def show(df):
    # ---------------- STYLE ----------------
    st.markdown("""
    <style>
    .block-container {
        max-width: 1280px;
        padding-top: 1.6rem !important;
        padding-bottom: 2rem !important;
    }

    .decision-header-wrap {
        position: relative;
        margin-bottom: 1rem;
    }

    .decision-header-glow {
        position: absolute;
        top: -10px;
        left: 0;
        width: 380px;
        height: 95px;
        background: radial-gradient(circle, rgba(168,85,247,0.22) 0%, rgba(6,182,212,0.14) 45%, rgba(255,255,255,0) 75%);
        filter: blur(10px);
        z-index: 0;
    }

    .decision-header {
        position: relative;
        z-index: 1;
        font-size: 2.8rem;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 0.35rem;
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 35%, #a855f7 68%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .decision-sub {
        position: relative;
        z-index: 1;
        color: #64748b;
        font-size: 1rem;
        font-weight: 500;
        line-height: 1.7;
    }

    .section-title {
        font-size: 1.16rem;
        font-weight: 800;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        padding: 1rem 1.1rem;
        border-radius: 22px;
        background: linear-gradient(90deg, #eef2ff, #f5f3ff, #ecfeff);
        border: 1px solid #dbeafe;
        border-left: 8px solid #8b5cf6;
        box-shadow: 0 10px 26px rgba(99, 102, 241, 0.10);
        color: #1e1b4b;
    }

    .metric-card {
        position: relative;
        overflow: hidden;
        border-radius: 26px;
        padding: 18px 18px 16px 18px;
        min-height: 165px;
        background:
            radial-gradient(circle at top right, rgba(168,85,247,0.24), transparent 32%),
            radial-gradient(circle at bottom left, rgba(6,182,212,0.18), transparent 32%),
            linear-gradient(135deg, #ffffff 0%, #eef2ff 48%, #f5f3ff 100%);
        border: 1px solid #dbeafe;
        box-shadow:
            0 18px 40px rgba(124, 58, 237, 0.12),
            0 6px 20px rgba(6, 182, 212, 0.08);
        margin-bottom: 18px;
    }

    .metric-top {
        height: 9px;
        width: 140px;
        border-radius: 999px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #67e8f9);
        margin-bottom: 0.9rem;
        box-shadow: 0 6px 20px rgba(129, 140, 248, 0.28);
    }

    .metric-label {
        font-size: 0.96rem;
        font-weight: 800;
        color: #475569;
        margin-bottom: 0.65rem;
    }

    .metric-value {
        font-size: 2.15rem;
        font-weight: 900;
        color: #172554;
        margin-bottom: 0.65rem;
    }

    .metric-note {
        display: inline-block;
        padding: 0.42rem 0.8rem;
        border-radius: 999px;
        font-size: 0.84rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ede9fe, #dbeafe);
        color: #5b21b6;
    }

    .content-card {
        background:
            radial-gradient(circle at bottom left, rgba(103, 232, 249, 0.12), transparent 30%),
            radial-gradient(circle at top right, rgba(216, 180, 254, 0.16), transparent 35%),
            linear-gradient(180deg, rgba(255,255,255,0.97), rgba(243,246,255,0.95));
        border: 1px solid rgba(129, 140, 248, 0.12);
        border-radius: 24px;
        padding: 16px;
        box-shadow: 0 14px 30px rgba(99, 102, 241, 0.06);
    }

    .glow-line {
        height: 6px;
        border-radius: 999px;
        margin-bottom: 14px;
        background: linear-gradient(90deg, #6366f1, #a855f7, #67e8f9);
        opacity: 0.95;
    }

    .decision-box {
        border-radius: 22px;
        padding: 18px 18px;
        margin-bottom: 12px;
        background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(241,245,255,0.96));
        border: 1px solid #dbeafe;
        box-shadow: 0 10px 24px rgba(99, 102, 241, 0.08);
    }

    .decision-title {
        font-size: 1.02rem;
        font-weight: 900;
        color: #1e1b4b;
        margin-bottom: 0.4rem;
    }

    .decision-text {
        font-size: 0.98rem;
        color: #475569;
        line-height: 1.7;
        font-weight: 500;
    }

    .badge-red {
        display: inline-block;
        padding: 0.38rem 0.7rem;
        border-radius: 999px;
        background: linear-gradient(90deg, #fee2e2, #fecaca);
        color: #b91c1c;
        font-weight: 800;
        font-size: 0.82rem;
        margin-bottom: 0.65rem;
    }

    .badge-yellow {
        display: inline-block;
        padding: 0.38rem 0.7rem;
        border-radius: 999px;
        background: linear-gradient(90deg, #fef3c7, #fde68a);
        color: #92400e;
        font-weight: 800;
        font-size: 0.82rem;
        margin-bottom: 0.65rem;
    }

    .badge-green {
        display: inline-block;
        padding: 0.38rem 0.7rem;
        border-radius: 999px;
        background: linear-gradient(90deg, #dcfce7, #bbf7d0);
        color: #15803d;
        font-weight: 800;
        font-size: 0.82rem;
        margin-bottom: 0.65rem;
    }

    .mini-note {
        color: #64748b;
        font-size: 0.92rem;
        line-height: 1.65;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- DATA PREP ----------------
    local_df = df.copy()

    local_df.columns = local_df.columns.str.strip()
    local_df.columns = local_df.columns.str.replace(" ", "_")
    local_df.columns = local_df.columns.str.replace(r"[^\w]", "", regex=True)

    required_cols = [
        "Day",
        "Daily_Patient_Admissions",
        "Bed_Occupancy_Rate",
        "Patients_per_Physician",
        "Medical_Device_Utilization",
        "Medical_Supply_Consumption"
    ]

    missing_required = [c for c in required_cols if c not in local_df.columns]
    if missing_required:
        st.error(f"Eksik kolonlar var: {', '.join(missing_required)}")
        return

    for col in local_df.columns:
        local_df[col] = pd.to_numeric(local_df[col], errors="coerce")

    local_df = local_df.dropna(subset=["Day"]).copy()
    local_df["Day"] = local_df["Day"].astype(int)
    local_df = local_df.sort_values("Day").reset_index(drop=True)

    if len(local_df) < 3:
        st.warning("Karar paneli için en az 3 günlük veri gerekli.")
        return

    last = local_df.iloc[-1]
    prev = local_df.iloc[-2]

    # ---------------- HELPERS ----------------
    def safe_delta(col):
        if pd.isna(last[col]) or pd.isna(prev[col]):
            return 0.0
        return round(float(last[col] - prev[col]), 2)

    def trend_label(col):
        series = local_df[col].dropna().tail(5)
        if len(series) < 2:
            return "İzleniyor"
        if series.iloc[-1] > series.iloc[0]:
            return "Yükseliş eğilimi"
        if series.iloc[-1] < series.iloc[0]:
            return "Düşüş eğilimi"
        return "Stabil"

    def linear_forecast(x, y, future_days):
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)

        mask = ~np.isnan(x) & ~np.isnan(y)
        x = x[mask]
        y = y[mask]

        if len(x) < 2:
            return {d: np.nan for d in future_days}, np.nan, np.nan

        slope, intercept = np.polyfit(x, y, 1)
        preds = {d: round(float(slope * d + intercept), 2) for d in future_days}
        y_hat = slope * x + intercept

        ss_res = np.sum((y - y_hat) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else np.nan

        return preds, round(float(slope), 4), round(float(r2), 4)

    def corr_text(value):
        if pd.isna(value):
            return "Hesaplanamadı"
        abs_v = abs(value)
        if abs_v >= 0.80:
            return "Çok güçlü ilişki"
        if abs_v >= 0.60:
            return "Güçlü ilişki"
        if abs_v >= 0.40:
            return "Orta düzey ilişki"
        if abs_v >= 0.20:
            return "Zayıf ilişki"
        return "Çok zayıf ilişki"

    def risk_badge(level):
        if level == "Kritik":
            return '<div class="badge-red">Kritik</div>'
        if level == "Dikkat":
            return '<div class="badge-yellow">Dikkat</div>'
        return '<div class="badge-green">Stabil</div>'

    # ---------------- ANALYSIS ----------------
    future_days = [31, 32]
    forecasts, slope, r2 = linear_forecast(
        local_df["Day"],
        local_df["Daily_Patient_Admissions"],
        future_days
    )

    corr_val = local_df["Daily_Patient_Admissions"].corr(local_df["Bed_Occupancy_Rate"])

    bed_last = float(last["Bed_Occupancy_Rate"]) if pd.notna(last["Bed_Occupancy_Rate"]) else np.nan
    physician_last = float(last["Patients_per_Physician"]) if pd.notna(last["Patients_per_Physician"]) else np.nan
    device_last = float(last["Medical_Device_Utilization"]) if pd.notna(last["Medical_Device_Utilization"]) else np.nan
    supply_last = float(last["Medical_Supply_Consumption"]) if pd.notna(last["Medical_Supply_Consumption"]) else np.nan

    if not np.isnan(bed_last) and bed_last >= 90:
        capacity_risk = "Kritik"
    elif not np.isnan(bed_last) and bed_last >= 80:
        capacity_risk = "Dikkat"
    else:
        capacity_risk = "Stabil"

    if safe_delta("Patients_per_Physician") > 0:
        workforce_risk = "Dikkat"
    else:
        workforce_risk = "Stabil"

    if safe_delta("Medical_Device_Utilization") > 0 or safe_delta("Medical_Supply_Consumption") > 0:
        resource_risk = "Dikkat"
    else:
        resource_risk = "Stabil"

    if safe_delta("Daily_Patient_Admissions") > 0 and capacity_risk == "Kritik":
        overall_risk = "Kritik"
    elif safe_delta("Daily_Patient_Admissions") > 0 or capacity_risk == "Dikkat":
        overall_risk = "Dikkat"
    else:
        overall_risk = "Stabil"

    # ---------------- HEADER ----------------
    st.markdown("""
    <div class="decision-header-wrap">
        <div class="decision-header-glow"></div>
        <div class="decision-header">🧠 Karar Paneli</div>
        <div class="decision-sub">
            Operasyonel göstergeleri analitik olarak yorumlar, kısa vadeli hasta talebi tahmini üretir
            ve yönetsel karar önerilerine dönüştürür.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- TOP CARDS ----------------
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top"></div>
            <div class="metric-label">Genel Risk Düzeyi</div>
            <div class="metric-value">{overall_risk}</div>
            <div class="metric-note">{trend_label("Daily_Patient_Admissions")}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        day31 = forecasts.get(31, np.nan)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top"></div>
            <div class="metric-label">31. Gün Tahmini</div>
            <div class="metric-value">{day31 if not np.isnan(day31) else "-"}</div>
            <div class="metric-note">Hasta başvurusu</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        day32 = forecasts.get(32, np.nan)
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top"></div>
            <div class="metric-label">32. Gün Tahmini</div>
            <div class="metric-value">{day32 if not np.isnan(day32) else "-"}</div>
            <div class="metric-note">Hasta başvurusu</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-top"></div>
            <div class="metric-label">R² Uyum Skoru</div>
            <div class="metric-value">{r2 if not np.isnan(r2) else "-"}</div>
            <div class="metric-note">Lineer trend modeli</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- TREND ANALYSIS ----------------
    st.markdown('<div class="section-title">📈 Analitik Bulgular</div>', unsafe_allow_html=True)

    a1, a2 = st.columns(2)

    with a1:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

        trend_df = pd.DataFrame({
            "Gösterge": [
                "Günlük Hasta Başvurusu",
                "Yatak Doluluk Oranı",
                "Doktor Başına Hasta",
                "Cihaz Kullanım Oranı",
                "Sarf Malzeme Tüketimi"
            ],
            "Son Değer": [
                round(float(last["Daily_Patient_Admissions"]), 2),
                round(float(last["Bed_Occupancy_Rate"]), 2),
                round(float(last["Patients_per_Physician"]), 2),
                round(float(last["Medical_Device_Utilization"]), 2),
                round(float(last["Medical_Supply_Consumption"]), 2),
            ],
            "Son Gün Değişim": [
                safe_delta("Daily_Patient_Admissions"),
                safe_delta("Bed_Occupancy_Rate"),
                safe_delta("Patients_per_Physician"),
                safe_delta("Medical_Device_Utilization"),
                safe_delta("Medical_Supply_Consumption"),
            ],
            "Trend": [
                trend_label("Daily_Patient_Admissions"),
                trend_label("Bed_Occupancy_Rate"),
                trend_label("Patients_per_Physician"),
                trend_label("Medical_Device_Utilization"),
                trend_label("Medical_Supply_Consumption"),
            ]
        })

        st.dataframe(trend_df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with a2:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

        if pd.notna(corr_val):
            relation_text = (
                f"Günlük hasta başvurusu ile yatak doluluk oranı arasındaki korelasyon: "
                f"{round(float(corr_val), 3)} ({corr_text(corr_val)})."
            )
        else:
            relation_text = "Korelasyon hesaplanamadı."

        st.markdown(f"""
        <div class="decision-box">
            <div class="decision-title">Talep-Kapasite İlişkisi</div>
            <div class="decision-text">{relation_text}</div>
        </div>
        <div class="decision-box">
            <div class="decision-title">Talep Tahmini</div>
            <div class="decision-text">
                Lineer trend analizine göre 31. gün için beklenen hasta başvurusu <b>{day31 if not np.isnan(day31) else "-"}</b>,
                32. gün için ise <b>{day32 if not np.isnan(day32) else "-"}</b> düzeyindedir.
                Model eğimi {slope if not np.isnan(slope) else "-"} olduğu için genel yön
                {"artan" if pd.notna(slope) and slope > 0 else "azalan" if pd.notna(slope) and slope < 0 else "yatay"} görünmektedir.
            </div>
        </div>
        <div class="mini-note">
            Bu panel, hizmet talebi tahmini, kapasite baskısı ve iş gücü yükünü birlikte yorumlamaya odaklanır.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- CHARTS ----------------
    st.markdown('<div class="section-title">📊 Senaryo Eğilim Grafikleri</div>', unsafe_allow_html=True)

    g1, g2, g3 = st.columns(3)

    with g1:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)
        chart1 = local_df.set_index("Day")["Daily_Patient_Admissions"]
        st.line_chart(chart1)
        st.markdown('</div>', unsafe_allow_html=True)

    with g2:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)
        chart2 = local_df.set_index("Day")["Bed_Occupancy_Rate"]
        st.line_chart(chart2)
        st.markdown('</div>', unsafe_allow_html=True)

    with g3:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)
        chart3 = local_df.set_index("Day")["Patients_per_Physician"]
        st.line_chart(chart3)
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- RISK BLOCKS ----------------
    st.markdown('<div class="section-title">🚨 Risk ve Yönetimsel Yorum</div>', unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(risk_badge(capacity_risk), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="decision-title">Kapasite Riski</div>
        <div class="decision-text">
            Son yatak doluluk oranı <b>{round(bed_last, 2)}</b> seviyesindedir.
            Bu değer kapasite baskısının {"kritik" if capacity_risk == "Kritik" else "artmakta" if capacity_risk == "Dikkat" else "kontrol altında"} olduğunu göstermektedir.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with r2:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(risk_badge(workforce_risk), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="decision-title">İş Gücü Riski</div>
        <div class="decision-text">
            Doktor başına hasta göstergesi son günde <b>{safe_delta("Patients_per_Physician")}</b> değişmiştir.
            Personel yükü {"artış eğiliminde" if workforce_risk == "Dikkat" else "stabil görünmektedir"}.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with r3:
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown(risk_badge(resource_risk), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="decision-title">Kaynak Riski</div>
        <div class="decision-text">
            Cihaz kullanım oranı <b>{round(device_last, 2)}</b>, sarf malzeme tüketimi <b>{round(supply_last, 2)}</b> düzeyindedir.
            Kaynak baskısı {"yükselmektedir" if resource_risk == "Dikkat" else "kontrol altındadır"}.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- DECISION OUTPUTS ----------------
    st.markdown('<div class="section-title">🤖 Karar Destek Önerileri</div>', unsafe_allow_html=True)

    decisions = []

    if safe_delta("Daily_Patient_Admissions") > 0:
        decisions.append((
            "Hizmet Talebi Artıyor",
            "Poliklinik kapasitesi artırılmalı ve randevu planı gözden geçirilmeli."
        ))

    if bed_last >= 90:
        decisions.append((
            "Yatak Doluluk Kritik",
            "Servis kapasitesi yeniden planlanmalı ve hasta akışı dengelenmeli."
        ))
    elif bed_last >= 80:
        decisions.append((
            "Yatak Doluluk Yüksek",
            "Kısa vadeli kapasite esnekliği oluşturulmalı."
        ))

    if safe_delta("Patients_per_Physician") > 0:
        decisions.append((
            "Personel Yükü Artıyor",
            "Ek vardiya, görev dağılımı düzenlemesi veya geçici personel desteği planlanmalı."
        ))

    if safe_delta("Medical_Device_Utilization") > 0:
        decisions.append((
            "Cihaz Kullanımı Artıyor",
            "Cihaz planlama ve bakım takvimi optimize edilmeli."
        ))

    if safe_delta("Medical_Supply_Consumption") > 0:
        decisions.append((
            "Sarf Tüketimi Artıyor",
            "Tedarik ve stok planı güncellenmeli."
        ))

    if not decisions:
        decisions.append((
            "Sistem Stabil",
            "Mevcut operasyonel akış korunabilir, rutin izleme devam etmeli."
        ))

    for title, text in decisions:
        st.markdown(f"""
        <div class="decision-box">
            <div class="decision-title">{title}</div>
            <div class="decision-text">{text}</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- FINAL SUMMARY ----------------
    st.markdown('<div class="section-title">📝 Akademik Yorum Özeti</div>', unsafe_allow_html=True)
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<div class="glow-line"></div>', unsafe_allow_html=True)

    summary_text = f"""
    Simüle edilmiş operasyonel veri üzerinde yapılan analizler, hizmet talebindeki değişimin kapasite kullanımı,
    iş gücü yükü ve kaynak tüketimi üzerinde doğrudan etkili olabileceğini göstermektedir. Günlük hasta başvuru
    göstergesi için kurulan basit lineer tahmin modeli, 31. gün için {day31 if not np.isnan(day31) else "-"},
    32. gün için {day32 if not np.isnan(day32) else "-"} düzeyinde başvuru öngörmektedir. Ayrıca günlük hasta
    başvurusu ile yatak doluluk oranı arasındaki ilişki {corr_text(corr_val).lower()} olarak değerlendirilmiştir.
    Bu bulgular, veri temelli kapasite planlaması, vardiya yönetimi ve kaynak tahsisi kararlarının önemini
    desteklemektedir.
    """

    st.markdown(f"""
    <div class="decision-text">{summary_text}</div>
    <div class="mini-note" style="margin-top:10px;">
        Bu yaklaşım, analitik sonuçların karar destek önerilerine dönüştürülmesi mantığıyla uyumludur.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)