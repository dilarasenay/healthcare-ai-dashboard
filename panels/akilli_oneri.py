import streamlit as st

def show(df):
    # =========================================================
    # DEMO VALUES
    # =========================================================
    demand_pressure = 92
    capacity_risk = 88
    workforce_stress = 90
    resource_load = 85
    before_risk = 97

    # =========================================================
    # STYLE
    # =========================================================
    st.markdown("""
    <style>
    /* =========================================================
       PAGE
    ========================================================= */
    .block-container {
        max-width: 1320px;
        padding-top: 1.1rem !important;
        padding-bottom: 2.4rem !important;
        padding-left: 1.8rem !important;
        padding-right: 1.8rem !important;
    }

    .stApp {
        background:
            radial-gradient(circle at 10% 12%, rgba(123, 92, 255, 0.10), transparent 18%),
            radial-gradient(circle at 86% 18%, rgba(34, 193, 195, 0.12), transparent 20%),
            radial-gradient(circle at 48% 72%, rgba(59, 130, 246, 0.08), transparent 22%),
            linear-gradient(180deg, #f7f9ff 0%, #eef4ff 52%, #f7fbff 100%);
    }

    header[data-testid="stHeader"] {
        background: rgba(0, 0, 0, 0);
    }

    h1, h2, h3, h4 {
        letter-spacing: -0.02em;
    }

    /* =========================================================
       HERO
    ========================================================= */
    .op-hero {
        position: relative;
        overflow: hidden;
        border-radius: 28px;
        padding: 24px 28px 20px 28px;
        margin-bottom: 1.15rem;
        background:
            radial-gradient(circle at top right, rgba(255,255,255,0.22), transparent 28%),
            linear-gradient(135deg, #6d5df6 0%, #3b82f6 45%, #22c1c3 100%);
        border: 1px solid rgba(255,255,255,0.16);
        box-shadow: 0 20px 42px rgba(59,130,246,0.14);
    }

    .op-hero::after {
        content: "";
        position: absolute;
        right: -36px;
        top: -44px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: rgba(255,255,255,0.10);
        filter: blur(8px);
    }

    .op-hero-top {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 0.55rem;
    }

    .op-hero-icon {
        width: 54px;
        height: 54px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        color: white;
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.22);
    }

    .op-hero-title {
        font-size: 2.05rem;
        font-weight: 900;
        color: white;
        line-height: 1.05;
        margin: 0;
    }

    .op-hero-sub {
        color: rgba(255,255,255,0.95);
        font-size: 1rem;
        line-height: 1.7;
        max-width: 950px;
        margin-bottom: 0.9rem;
    }

    .op-hero-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .op-badge {
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.13);
        border: 1px solid rgba(255,255,255,0.16);
        color: white;
        font-size: 0.90rem;
        font-weight: 700;
    }

    /* =========================================================
       SECTION TITLES
    ========================================================= */
    .section-title {
        font-size: 1.9rem;
        font-weight: 900;
        color: #12357a;
        margin-top: 0.15rem;
        margin-bottom: 0.35rem;
    }

    .section-sub {
        color: #54709b;
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 0.8rem;
    }

    /* =========================================================
       KPI / TOP METRIC CARDS
    ========================================================= */
    .metric-card {
        position: relative;
        overflow: hidden;
        border-radius: 24px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.90), rgba(247,250,255,0.94));
        border: 1px solid rgba(129, 148, 199, 0.14);
        box-shadow: 0 16px 34px rgba(73, 98, 160, 0.08);
        padding: 18px 18px 16px 18px;
        min-height: 148px;
    }

    .metric-card::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 5px;
        background: linear-gradient(90deg, #7b5cff, #22c1c3);
    }

    .metric-card::after {
        content: "";
        position: absolute;
        right: -16px;
        bottom: -16px;
        width: 88px;
        height: 88px;
        border-radius: 50%;
        opacity: 0.18;
    }

    .metric-a::after { background: linear-gradient(135deg, #7b5cff, #a78bfa); }
    .metric-b::after { background: linear-gradient(135deg, #3b82f6, #93c5fd); }
    .metric-c::after { background: linear-gradient(135deg, #22c1c3, #67e8f9); }
    .metric-d::after { background: linear-gradient(135deg, #8b5cf6, #22d3ee); }

    .metric-label {
        color: #5d7298;
        font-size: 1rem;
        font-weight: 800;
        margin-bottom: 0.55rem;
    }

    .metric-value {
        color: #0f2f72;
        font-size: 2.15rem;
        font-weight: 900;
        line-height: 1;
        margin-bottom: 0.55rem;
    }

    .metric-note {
        color: #58719a;
        font-size: 0.96rem;
        line-height: 1.6;
        font-weight: 600;
    }

    /* =========================================================
       PANEL WRAPPER
    ========================================================= */
    .glass-panel {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.80), rgba(245,249,255,0.88));
        border: 1px solid rgba(129,148,199,0.14);
        border-radius: 26px;
        padding: 22px;
        box-shadow: 0 18px 38px rgba(73, 98, 160, 0.08);
        min-height: 100%;
    }

    /* =========================================================
       ACTION CARDS
    ========================================================= */
    .action-card {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.93), rgba(247,250,255,0.96));
        border-radius: 22px;
        padding: 18px 18px 15px 18px;
        box-shadow: 0 12px 26px rgba(76, 98, 150, 0.07);
        border: 1px solid rgba(129,148,199,0.12);
        border-left: 5px solid #7b5cff;
        margin-bottom: 14px;
    }

    .action-card.alt-blue { border-left-color: #3b82f6; }
    .action-card.alt-cyan { border-left-color: #22c1c3; }

    .action-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }

    .action-title {
        font-size: 1.12rem;
        font-weight: 900;
        color: #12357a;
    }

    .action-desc {
        color: #5d7298;
        font-size: 1rem;
        line-height: 1.72;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }

    .action-note {
        font-size: 0.9rem;
        color: #7087ad;
        line-height: 1.6;
        font-weight: 600;
    }

    .action-chip {
        border-radius: 999px;
        padding: 8px 14px;
        font-size: 0.84rem;
        font-weight: 900;
        color: white;
        white-space: nowrap;
    }

    .chip-purple { background: linear-gradient(135deg, #7b5cff, #8b5cf6); }
    .chip-blue { background: linear-gradient(135deg, #3b82f6, #60a5fa); }
    .chip-cyan { background: linear-gradient(135deg, #06b6d4, #22c1c3); }

    /* =========================================================
       AI COMMENT BOX
    ========================================================= */
    .ai-box {
        border-radius: 24px;
        padding: 20px 20px 16px 20px;
        background:
            radial-gradient(circle at top right, rgba(255,255,255,0.55), transparent 26%),
            linear-gradient(135deg, rgba(123,92,255,0.12), rgba(59,130,246,0.10), rgba(34,193,195,0.12));
        border: 1px solid rgba(123,92,255,0.14);
        box-shadow: 0 16px 30px rgba(59,130,246,0.08);
        margin-top: 0.6rem;
        margin-bottom: 1rem;
    }

    .ai-box-title {
        font-size: 1.08rem;
        font-weight: 900;
        color: #12357a;
        margin-bottom: 0.7rem;
    }

    .ai-box-text {
        font-size: 1.02rem;
        line-height: 1.85;
        color: #173d7c;
        font-weight: 700;
    }

    /* =========================================================
       MINI STATS
    ========================================================= */
    .mini-stat {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.92), rgba(247,250,255,0.96));
        border-radius: 22px;
        padding: 18px 18px 15px 18px;
        min-height: 116px;
        box-shadow: 0 14px 28px rgba(70,97,155,0.06);
        border: 1px solid rgba(129,148,199,0.12);
    }

    .mini-label {
        color: #61739b;
        font-size: 0.95rem;
        margin-bottom: 0.7rem;
        font-weight: 800;
    }

    .mini-value {
        color: #12357a;
        font-size: 2rem;
        font-weight: 900;
        line-height: 1;
    }

    .mini-purple { color: #6d5df6; }
    .mini-blue { color: #2563eb; }
    .mini-cyan { color: #0891b2; }
    .mini-risk { color: #ef4444; }

    /* =========================================================
       RISK BAR
    ========================================================= */
    .risk-wrap {
        margin-top: 0.75rem;
        margin-bottom: 0.8rem;
    }

    .risk-track {
        width: 100%;
        height: 16px;
        border-radius: 999px;
        background: linear-gradient(90deg, #22c1c3 0%, #3b82f6 45%, #8b5cf6 100%);
        position: relative;
        overflow: hidden;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.06);
    }

    .risk-mask {
        position: absolute;
        right: 0;
        top: 0;
        height: 16px;
        background: rgba(255,255,255,0.72);
        border-radius: 0 999px 999px 0;
    }

    .risk-value {
        font-size: 1.95rem;
        font-weight: 900;
        color: #ef4444;
        margin-top: 0.65rem;
    }

    /* =========================================================
       EXEC CARD
    ========================================================= */
    .exec-card {
        border-radius: 24px;
        padding: 22px 22px 18px 22px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.92), rgba(247,250,255,0.95));
        border: 1px solid rgba(129,148,199,0.12);
        box-shadow: 0 15px 30px rgba(70,97,155,0.07);
    }

    .exec-title {
        font-size: 1.45rem;
        font-weight: 900;
        color: #12357a;
        margin-bottom: 0.85rem;
    }

    .exec-text {
        font-size: 1.03rem;
        line-height: 1.95;
        color: #4e678f;
        font-weight: 600;
    }

    /* =========================================================
       INSIGHT CARDS
    ========================================================= */
    .insight-card {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.92), rgba(247,250,255,0.96));
        border-radius: 22px;
        padding: 20px;
        min-height: 205px;
        box-shadow: 0 14px 28px rgba(60,90,150,0.06);
        border: 1px solid rgba(129,148,199,0.12);
    }

    .insight-title {
        color: #12357a;
        font-weight: 900;
        font-size: 1.18rem;
        margin-bottom: 0.75rem;
    }

    .insight-text {
        color: #58719a;
        font-size: 1rem;
        line-height: 1.82;
        font-weight: 600;
    }

    /* =========================================================
       SUMMARY BAND
    ========================================================= */
    .summary-band {
        margin-top: 0.9rem;
        border-radius: 24px;
        padding: 22px 24px;
        background:
            radial-gradient(circle at top left, rgba(255,255,255,0.20), transparent 22%),
            linear-gradient(135deg, #7b5cff 0%, #3b82f6 48%, #22c1c3 100%);
        color: white;
        box-shadow: 0 20px 40px rgba(91, 92, 240, 0.14);
        border: 1px solid rgba(255,255,255,0.14);
    }

    .summary-title {
        font-size: 1.18rem;
        font-weight: 900;
        margin-bottom: 0.55rem;
    }

    .summary-text {
        font-size: 1.03rem;
        line-height: 1.85;
        color: rgba(255,255,255,0.97);
        font-weight: 700;
    }

    /* =========================================================
       STREAMLIT CONTROLS
    ========================================================= */
    div[data-baseweb="radio"] > div {
        gap: 0.6rem;
    }

    div[data-baseweb="radio"] label {
        background: rgba(255,255,255,0.76);
        border: 1px solid rgba(129,148,199,0.12);
        border-radius: 16px;
        padding: 11px 13px;
        box-shadow: 0 8px 18px rgba(60,90,150,0.04);
    }

    div[data-baseweb="slider"] {
        padding-top: 0.35rem;
        padding-bottom: 0.7rem;
    }

    /* =========================================================
       RESPONSIVE
    ========================================================= */
    @media (max-width: 1100px) {
        .op-hero-title { font-size: 1.75rem; }
        .section-title { font-size: 1.6rem; }
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================================================
    # HERO
    # =========================================================
    st.markdown("""
    <div class="op-hero">
        <div class="op-hero-top">
            <div class="op-hero-icon">🧠</div>
            <div class="op-hero-title">Operasyonel Öneri ve Önceliklendirme</div>
        </div>
        <div class="op-hero-sub">
            Operasyonel baskı alanlarını önceliklendirir, müdahale senaryolarının beklenen etkisini görünür kılar
            ve yönetim için uygulanabilir aksiyon sıralaması üretir.
        </div>
        <div class="op-hero-badges">
            <div class="op-badge">📌 Kritik durum görünümü</div>
            <div class="op-badge">⚡ Öncelik motoru aktif</div>
            <div class="op-badge">📈 Simülasyon destekli karar</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # TOP METRICS
    # =========================================================
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="metric-card metric-a">
            <div class="metric-label">Talep Baskısı</div>
            <div class="metric-value">{demand_pressure}</div>
            <div class="metric-note">Başvuru akışı mevcut hizmet kapasitesinin üzerine çıkıyor.</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card metric-b">
            <div class="metric-label">Kapasite Riski</div>
            <div class="metric-value">{capacity_risk}</div>
            <div class="metric-note">İşlem çevrimi ve yatak akışı kapasite esnekliğini sınırlıyor.</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card metric-c">
            <div class="metric-label">İş Gücü Basıncı</div>
            <div class="metric-value">{workforce_stress}</div>
            <div class="metric-note">Ekip yükü operasyon içi dengeyi zorluyor.</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="metric-card metric-d">
            <div class="metric-label">Kaynak Yoğunluğu</div>
            <div class="metric-value">{resource_load}</div>
            <div class="metric-note">Kaynak kullanımı planlama esnekliğini aşağı çekiyor.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # MAIN LAYOUT
    # =========================================================
    left, right = st.columns([1.15, 1], gap="large")

    with left:
        st.markdown("<div class='section-title'>🎯 Öncelikli Aksiyonlar</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-sub'>Mevcut tabloya göre en yüksek etki üretmesi beklenen müdahale sırası aşağıdadır.</div>", unsafe_allow_html=True)

        selected_action = st.radio(
            "Aksiyon seç:",
            [
                "Poliklinik kapasitesini artır",
                "Yatak dönüş sürecini hızlandır",
                "Ek vardiya ve görev planı uygula"
            ]
        )

        st.markdown("""
        <div class="action-card">
            <div class="action-top">
                <div class="action-title">🎯 Poliklinik kapasitesini artır</div>
                <div class="action-chip chip-purple">Öncelik 1</div>
            </div>
            <div class="action-desc">
                İlk müdahalenin başvuru yoğunluğunu karşılayan hatta yapılması, bekleme süresi üzerinde en hızlı iyileşmeyi üretir.
            </div>
            <div class="action-note">
                💡 Yönetim notu: Kısa vadede en görünür operasyonel rahatlama bu alanda beklenir.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="action-card alt-blue">
            <div class="action-top">
                <div class="action-title">🛏️ Yatak dönüş sürecini hızlandır</div>
                <div class="action-chip chip-blue">Öncelik 2</div>
            </div>
            <div class="action-desc">
                Yatak çevrim hızındaki iyileşme kapasite sıkışıklığını azaltır ve yoğun saatlerde akışın korunmasını destekler.
            </div>
            <div class="action-note">
                💡 Yönetim notu: İlk aksiyonu destekleyen ikinci faz kapasite müdahalesi olarak değerlendirilmelidir.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="action-card alt-cyan">
            <div class="action-top">
                <div class="action-title">👩‍⚕️ Ek vardiya ve görev planı uygula</div>
                <div class="action-chip chip-cyan">Öncelik 3</div>
            </div>
            <div class="action-desc">
                İş gücü dağılımının güçlendirilmesi hizmet kalitesini korur ve kapasite iyileştirmelerinin sürdürülebilirliğini artırır.
            </div>
            <div class="action-note">
                💡 Yönetim notu: Kaynak ve vardiya dengesi, operasyonel istikrar için destekleyici bir kaldıraçtır.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:0.35rem;'></div>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>📌 Yöneticiye Net Yönlendirme</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class="exec-card">
            <div class="exec-title">Öncelik 1: Poliklinik kapasitesini artır</div>
            <div class="exec-text">
                İlk müdahalenin ana talep darboğazını hedeflemesi gerekir. Ardından yatak dönüş süreci ve iş gücü planı
                destekleyici ikinci faz olarak devreye alınmalıdır.<br><br>
                1) Poliklinik kapasitesini artır<br>
                2) Yatak dönüş sürecini hızlandır<br>
                3) Ek vardiya ve görev dağılımını güncelle
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("<div class='section-title'>🧪 Senaryo Simülasyonu</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-sub'>Müdahale oranlarını değiştirerek beklenen operasyon etkisini yönetim görünümünde izleyin.</div>", unsafe_allow_html=True)

        pol = st.slider("Ek poliklinik kapasitesi (%)", 0, 30, 15)
        bed = st.slider("Yatak dönüş hızında iyileşme (%)", 0, 20, 8)
        work = st.slider("İş gücü optimizasyon etkisi (%)", 0, 20, 6)

        wait_effect = round(-(pol * 1.05), 1)
        workforce_relief = round(work * 1.4, 1)
        capacity_relief = round((pol * 0.62) + (bed * 0.7), 1)
        after_risk = int(max(45, before_risk - ((pol * 0.7) + (bed * 0.8) + (work * 0.6))))
        risk_mask = 100 - after_risk

        st.markdown(f"""
        <div class="ai-box">
            <div class="ai-box-title">📊 Karar Yorumu</div>
            <div class="ai-box-text">
                Poliklinik kapasitesindeki <b>%{pol}</b> artış, bekleme süresinde yaklaşık <b>%{abs(wait_effect)}</b>
                iyileşme potansiyeli üretir. Yatak dönüş hızındaki <b>%{bed}</b> artış kapasite baskısını dengeler.
                İş gücü optimizasyonunun <b>%{work}</b> düzeyine çıkması, operasyonel akışın sürekliliğini destekler.
            </div>
        </div>
        """, unsafe_allow_html=True)

        r1, r2 = st.columns(2)
        with r1:
            st.markdown(f"""
            <div class="mini-stat">
                <div class="mini-label">Bekleme süresi etkisi</div>
                <div class="mini-value mini-purple">{wait_effect}%</div>
            </div>
            """, unsafe_allow_html=True)
        with r2:
            st.markdown(f"""
            <div class="mini-stat">
                <div class="mini-label">İş gücü rahatlaması</div>
                <div class="mini-value mini-cyan">+{workforce_relief}%</div>
            </div>
            """, unsafe_allow_html=True)

        r3, r4 = st.columns(2)
        with r3:
            st.markdown(f"""
            <div class="mini-stat">
                <div class="mini-label">Kapasite rahatlaması</div>
                <div class="mini-value mini-blue">+{capacity_relief}%</div>
            </div>
            """, unsafe_allow_html=True)
        with r4:
            st.markdown(f"""
            <div class="mini-stat">
                <div class="mini-label">Simülasyon sonrası risk</div>
                <div class="mini-value mini-risk">{after_risk}/100</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div class='section-sub' style='margin-top:0.9rem; margin-bottom:0.2rem; font-weight:800; color:#12357a;'>🚨 Risk seviyesi</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="risk-wrap">
            <div class="risk-track">
                <div class="risk-mask" style="width:{risk_mask}%;"></div>
            </div>
            <div class="risk-value">{after_risk}/100</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="summary-band" style="margin-top:0.7rem;">
            <div class="summary-title">🧠 Yönetim Özeti</div>
            <div class="summary-text">
                İlk odak alanı <b>poliklinik kapasitesi</b> olmalıdır. En yüksek ilk etki bu başlıkta oluşur.
                İkinci aşamada yatak dönüşü ve iş gücü planı devreye alındığında risk seviyesi
                <b>{before_risk}/100</b> düzeyinden yaklaşık <b>{after_risk}/100</b> seviyesine çekilebilir.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 0.9rem;'></div>", unsafe_allow_html=True)

    # =========================================================
    # INSIGHT BOARD
    # =========================================================
    st.markdown("<div class='section-title'>✨ Yönetim İçgörü Panosu</div>", unsafe_allow_html=True)

    a, b, c = st.columns(3, gap="large")
    with a:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">Ana Operasyon Problemi</div>
            <div class="insight-text">
                En belirgin sorun, artan başvuru hacmi ile kapasite darboğazının aynı anda yükselmesidir.
                Bu durum hem bekleme süresini hem de hizmet verimliliğini baskılamaktadır.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with b:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">Beklenen En Güçlü Etki</div>
            <div class="insight-text">
                Simülasyona göre ilk müdahale sonrası bekleme süresinde yaklaşık <b>%{abs(wait_effect)}</b>
                iyileşme ve toplam risk skorunda anlamlı bir geri çekilme beklenmektedir.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">Karar Notu</div>
            <div class="insight-text">
                Yönetimin ilk odak noktası poliklinik kapasitesini artırmak olmalıdır.
                Destekleyici ikinci fazda kapasite akışı ve iş gücü dengesi birlikte ele alınmalıdır.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # =========================================================
    # FINAL SUMMARY
    # =========================================================
    st.markdown(f"""
    <div class="summary-band">
        <div class="summary-title">📄 Tek Cümlelik Yönetici Sonucu</div>
        <div class="summary-text">
            Mevcut tablo, öncelikli müdahale gerektirmektedir; en doğru ilk adım <b>poliklinik kapasitesini artırmak</b> olup,
            simülasyon sonucuna göre toplam risk seviyesi <b>{before_risk}/100</b> düzeyinden yaklaşık
            <b>{after_risk}/100</b> seviyesine çekilebilir.
        </div>
    </div>
    """, unsafe_allow_html=True)