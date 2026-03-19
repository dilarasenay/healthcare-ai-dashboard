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
    # PREMIUM STYLE
    # =========================================================
    st.markdown("""
    <style>
    /* =========================================================
       PAGE
    ========================================================= */
    .block-container {
        max-width: 1340px;
        padding-top: 0.95rem !important;
        padding-bottom: 2.6rem !important;
        padding-left: 1.8rem !important;
        padding-right: 1.8rem !important;
    }

    .stApp {
        background:
            radial-gradient(circle at 8% 12%, rgba(168, 85, 247, 0.08), transparent 18%),
            radial-gradient(circle at 92% 16%, rgba(34, 211, 238, 0.10), transparent 18%),
            radial-gradient(circle at 50% 75%, rgba(59, 130, 246, 0.06), transparent 22%),
            linear-gradient(180deg, #fcfbff 0%, #f4f7ff 52%, #f8fbff 100%);
    }

    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    h1, h2, h3, h4 {
        letter-spacing: -0.025em;
    }

    /* =========================================================
       HERO
    ========================================================= */
    .op-hero {
        position: relative;
        overflow: hidden;
        border-radius: 30px;
        padding: 26px 28px 22px 28px;
        margin-bottom: 1.15rem;
        background:
            radial-gradient(circle at top right, rgba(255,255,255,0.72), transparent 24%),
            radial-gradient(circle at bottom left, rgba(255,255,255,0.48), transparent 20%),
            linear-gradient(135deg, rgba(242,236,255,0.98) 0%, rgba(235,244,255,0.98) 48%, rgba(233,250,248,0.97) 100%);
        border: 1px solid rgba(164, 151, 212, 0.14);
        box-shadow:
            0 24px 48px rgba(114, 121, 185, 0.08),
            inset 0 1px 0 rgba(255,255,255,0.68);
        backdrop-filter: blur(8px);
    }

    .op-hero::before {
        content: "";
        position: absolute;
        left: -40px;
        bottom: -50px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(168,85,247,0.10), rgba(59,130,246,0.04));
        filter: blur(12px);
    }

    .op-hero::after {
        content: "";
        position: absolute;
        right: -28px;
        top: -34px;
        width: 180px;
        height: 180px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(34,211,238,0.10), rgba(168,85,247,0.10));
        filter: blur(12px);
    }

    .op-hero-top {
        position: relative;
        z-index: 2;
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 0.55rem;
    }

    .op-hero-icon {
        width: 58px;
        height: 58px;
        border-radius: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.45rem;
        color: #5b4ce6;
        background: linear-gradient(135deg, rgba(123,92,255,0.12), rgba(34,193,195,0.10));
        border: 1px solid rgba(123,92,255,0.12);
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.72),
            0 10px 20px rgba(123,92,255,0.08);
    }

    .op-hero-title {
        font-size: 2.22rem;
        font-weight: 950;
        line-height: 1.05;
        margin: 0;
        background: linear-gradient(90deg, #5b4ce6 0%, #7c3aed 45%, #0891b2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .op-hero-sub {
        position: relative;
        z-index: 2;
        color: #5e759a;
        font-size: 1.02rem;
        line-height: 1.78;
        max-width: 980px;
        margin-bottom: 1rem;
        font-weight: 650;
    }

    .op-hero-badges {
        position: relative;
        z-index: 2;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .op-badge {
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.74);
        border: 1px solid rgba(164, 151, 212, 0.14);
        color: #51688f;
        font-size: 0.88rem;
        font-weight: 800;
        box-shadow: 0 8px 16px rgba(90, 104, 160, 0.05);
    }

    /* =========================================================
       TITLES
    ========================================================= */
    .section-title {
        font-size: 1.95rem;
        font-weight: 950;
        color: #12357a;
        margin-top: 0.1rem;
        margin-bottom: 0.28rem;
        letter-spacing: -0.03em;
    }

    .section-sub {
        color: #60789d;
        font-size: 1rem;
        line-height: 1.72;
        margin-bottom: 0.95rem;
        font-weight: 600;
    }

    /* =========================================================
       KPI METRICS
    ========================================================= */
    .metric-card {
        position: relative;
        overflow: hidden;
        border-radius: 24px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.92), rgba(247,250,255,0.96));
        border: 1px solid rgba(129, 148, 199, 0.13);
        box-shadow:
            0 18px 34px rgba(73, 98, 160, 0.07),
            inset 0 1px 0 rgba(255,255,255,0.76);
        padding: 18px 18px 16px 18px;
        min-height: 150px;
        backdrop-filter: blur(6px);
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
        width: 90px;
        height: 90px;
        border-radius: 50%;
        opacity: 0.18;
    }

    .metric-a::after { background: linear-gradient(135deg, #7b5cff, #c4b5fd); }
    .metric-b::after { background: linear-gradient(135deg, #3b82f6, #bfdbfe); }
    .metric-c::after { background: linear-gradient(135deg, #22c1c3, #a5f3fc); }
    .metric-d::after { background: linear-gradient(135deg, #8b5cf6, #99f6e4); }

    .metric-label {
        color: #62779a;
        font-size: 0.98rem;
        font-weight: 850;
        margin-bottom: 0.55rem;
    }

    .metric-value {
        color: #0f2f72;
        font-size: 2.18rem;
        font-weight: 950;
        line-height: 1;
        margin-bottom: 0.55rem;
    }

    .metric-note {
        color: #61789c;
        font-size: 0.95rem;
        line-height: 1.62;
        font-weight: 640;
    }

    /* =========================================================
       ACTION SELECT / RADIO
    ========================================================= */
    div[data-baseweb="radio"] > div {
        gap: 0.72rem;
    }

    div[data-baseweb="radio"] label {
        background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(248,250,255,0.96));
        border: 1px solid rgba(150, 160, 210, 0.14);
        border-radius: 18px;
        padding: 12px 14px;
        box-shadow:
            0 10px 22px rgba(70, 90, 150, 0.05),
            inset 0 1px 0 rgba(255,255,255,0.82);
        transition: all 0.24s ease;
        min-height: 52px;
    }

    div[data-baseweb="radio"] label:hover {
        transform: translateX(4px);
        border: 1px solid rgba(123, 92, 255, 0.22);
        box-shadow:
            0 14px 24px rgba(123,92,255,0.09),
            0 6px 14px rgba(34,193,195,0.05);
        background: linear-gradient(180deg, rgba(255,255,255,0.96), rgba(244,248,255,0.98));
    }

    div[data-baseweb="radio"] label span {
        font-weight: 700 !important;
        color: #45608f !important;
    }

    div[data-baseweb="radio"] input[type="radio"] {
        accent-color: #7b5cff !important;
        transform: scale(1.08);
    }

    /* =========================================================
       ACTION CARDS
    ========================================================= */
    .action-card {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.95), rgba(247,250,255,0.97));
        border-radius: 24px;
        padding: 18px 18px 15px 18px;
        box-shadow:
            0 14px 28px rgba(76, 98, 150, 0.07),
            inset 0 1px 0 rgba(255,255,255,0.72);
        border: 1px solid rgba(129,148,199,0.11);
        border-left: 5px solid #7b5cff;
        margin-bottom: 14px;
        backdrop-filter: blur(8px);
    }

    .action-card.alt-blue { border-left-color: #3b82f6; }
    .action-card.alt-cyan { border-left-color: #22c1c3; }

    .action-card.primary {
        background:
            radial-gradient(circle at top right, rgba(255,255,255,0.62), transparent 24%),
            linear-gradient(180deg, rgba(255,255,255,0.98), rgba(245,248,255,0.99));
        box-shadow:
            0 26px 46px rgba(123,92,255,0.14),
            0 10px 24px rgba(34,193,195,0.06),
            inset 0 1px 0 rgba(255,255,255,0.88);
        transform: translateY(-2px);
        border: 1px solid rgba(123,92,255,0.20);
        position: relative;
    }

    .action-card.primary::after {
        content: "";
        position: absolute;
        right: 18px;
        top: 18px;
        width: 72px;
        height: 72px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(123,92,255,0.10), rgba(34,193,195,0.08));
        filter: blur(4px);
        pointer-events: none;
    }

    .action-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }

    .action-title {
        font-size: 1.12rem;
        font-weight: 950;
        color: #12357a;
    }

    .action-desc {
        color: #60789d;
        font-size: 1rem;
        line-height: 1.75;
        margin-bottom: 0.5rem;
        font-weight: 650;
    }

    .action-note {
        font-size: 0.9rem;
        color: #748ab0;
        line-height: 1.62;
        font-weight: 650;
    }

    .action-chip {
        border-radius: 999px;
        padding: 8px 14px;
        font-size: 0.83rem;
        font-weight: 950;
        color: white;
        white-space: nowrap;
        box-shadow: 0 8px 16px rgba(90,100,180,0.10);
    }

    .chip-purple { background: linear-gradient(135deg, #7b5cff, #8b5cf6); }
    .chip-blue { background: linear-gradient(135deg, #3b82f6, #60a5fa); }
    .chip-cyan { background: linear-gradient(135deg, #06b6d4, #22c1c3); }

    /* =========================================================
       AI COMMENT BOX
    ========================================================= */
    .ai-box {
        border-radius: 26px;
        padding: 20px 20px 16px 20px;
        background:
            radial-gradient(circle at top right, rgba(255,255,255,0.62), transparent 26%),
            linear-gradient(135deg, rgba(123,92,255,0.12), rgba(59,130,246,0.09), rgba(34,193,195,0.12));
        border: 1px solid rgba(123,92,255,0.14);
        box-shadow:
            0 18px 32px rgba(59,130,246,0.08),
            0 8px 18px rgba(123,92,255,0.05),
            inset 0 1px 0 rgba(255,255,255,0.78);
        margin-top: 0.65rem;
        margin-bottom: 1rem;
    }

    .ai-box-title {
        font-size: 1.08rem;
        font-weight: 950;
        color: #12357a;
        margin-bottom: 0.7rem;
    }

    .ai-box-text {
        font-size: 1.01rem;
        line-height: 1.84;
        color: #21467f;
        font-weight: 720;
    }

    /* =========================================================
       MINI STATS
    ========================================================= */
    .mini-stat {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.94), rgba(247,250,255,0.98));
        border-radius: 22px;
        padding: 18px 18px 15px 18px;
        min-height: 118px;
        box-shadow:
            0 14px 26px rgba(70,97,155,0.06),
            inset 0 1px 0 rgba(255,255,255,0.78);
        border: 1px solid rgba(129,148,199,0.11);
    }

    .mini-label {
        color: #667aa0;
        font-size: 0.95rem;
        margin-bottom: 0.7rem;
        font-weight: 850;
    }

    .mini-value {
        color: #12357a;
        font-size: 2rem;
        font-weight: 950;
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
        margin-top: 0.78rem;
        margin-bottom: 0.9rem;
    }

    .risk-track {
        width: 100%;
        height: 16px;
        border-radius: 999px;
        background: linear-gradient(90deg, #22c1c3 0%, #3b82f6 45%, #8b5cf6 100%);
        position: relative;
        overflow: hidden;
        box-shadow:
            inset 0 2px 4px rgba(0,0,0,0.05),
            0 8px 18px rgba(90,100,180,0.05);
    }

    .risk-mask {
        position: absolute;
        right: 0;
        top: 0;
        height: 16px;
        background: rgba(255,255,255,0.74);
        border-radius: 0 999px 999px 0;
    }

    .risk-value {
        font-size: 1.95rem;
        font-weight: 950;
        color: #ef4444;
        margin-top: 0.7rem;
    }

    /* =========================================================
       EXEC CARD
    ========================================================= */
    .exec-card {
        border-radius: 24px;
        padding: 22px 22px 18px 22px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.94), rgba(247,250,255,0.98));
        border: 1px solid rgba(129,148,199,0.11);
        box-shadow:
            0 16px 28px rgba(70,97,155,0.06),
            inset 0 1px 0 rgba(255,255,255,0.78);
    }

    .exec-title {
        font-size: 1.45rem;
        font-weight: 950;
        color: #12357a;
        margin-bottom: 0.85rem;
    }

    .exec-text {
        font-size: 1.02rem;
        line-height: 1.92;
        color: #566f96;
        font-weight: 650;
    }

    /* =========================================================
       INSIGHT CARDS
    ========================================================= */
    .insight-card {
        background:
            linear-gradient(180deg, rgba(255,255,255,0.94), rgba(247,250,255,0.98));
        border-radius: 22px;
        padding: 20px;
        min-height: 205px;
        box-shadow:
            0 14px 26px rgba(60,90,150,0.06),
            inset 0 1px 0 rgba(255,255,255,0.76);
        border: 1px solid rgba(129,148,199,0.11);
    }

    .insight-title {
        color: #12357a;
        font-weight: 950;
        font-size: 1.18rem;
        margin-bottom: 0.75rem;
    }

    .insight-text {
        color: #60789d;
        font-size: 1rem;
        line-height: 1.82;
        font-weight: 650;
    }

    /* =========================================================
       SUMMARY BANDS
    ========================================================= */
    .summary-band {
        margin-top: 0.9rem;
        border-radius: 26px;
        padding: 22px 24px;
        background:
            radial-gradient(circle at top left, rgba(255,255,255,0.22), transparent 22%),
            linear-gradient(135deg, #7b5cff 0%, #3b82f6 48%, #22c1c3 100%);
        color: white;
        box-shadow: 0 22px 42px rgba(91, 92, 240, 0.12);
        border: 1px solid rgba(255,255,255,0.14);
    }

    .summary-title {
        font-size: 1.18rem;
        font-weight: 950;
        margin-bottom: 0.55rem;
    }

    .summary-text {
        font-size: 1.02rem;
        line-height: 1.86;
        color: rgba(255,255,255,0.98);
        font-weight: 760;
    }

    /* =========================================================
       SLIDERS
    ========================================================= */
    div[data-baseweb="slider"] {
        padding-top: 0.45rem;
        padding-bottom: 0.9rem;
    }

    div[data-baseweb="slider"] > div {
        background: rgba(255,255,255,0.40);
        border-radius: 18px;
        padding: 8px 10px 2px 10px;
    }

    div[data-baseweb="slider"] [role="slider"] {
        box-shadow:
            0 0 0 4px rgba(123,92,255,0.10),
            0 6px 14px rgba(123,92,255,0.16) !important;
        border: 2px solid white !important;
    }

    div[data-baseweb="slider"] [data-testid="stTickBar"] {
        opacity: 0.55;
    }

    .stSlider label {
        font-weight: 800 !important;
        color: #4a628f !important;
        letter-spacing: -0.01em;
    }

    .stSlider [role="slider"] {
        background: linear-gradient(135deg, #7b5cff, #22c1c3) !important;
    }

    /* =========================================================
       RESPONSIVE
    ========================================================= */
    @media (max-width: 1100px) {
        .op-hero-title { font-size: 1.8rem; }
        .section-title { font-size: 1.6rem; }
    }
    </style>
    """, unsafe_allow_html=True)

    # =========================================================
    # ACTION CONFIG
    # =========================================================
    action_data = {
        "Poliklinik kapasitesini artır": {
            "card_class": "action-card",
            "icon": "🎯",
            "title": "Poliklinik kapasitesini artır",
            "chip": "Öncelik 1",
            "chip_class": "chip-purple",
            "desc": "İlk müdahalenin başvuru yoğunluğunu karşılayan hatta yapılması, bekleme süresi üzerinde en hızlı iyileşmeyi üretir.",
            "note": "💡 Yönetim notu: Kısa vadede en görünür operasyonel rahatlama bu alanda beklenir.",
            "exec_title": "Öncelik 1: Poliklinik kapasitesini artır",
            "exec_text": """İlk müdahalenin ana talep darboğazını hedeflemesi gerekir. Bu aksiyon, hasta akışında en hızlı görünür rahatlamayı üretir.<br><br>
            1) Poliklinik kapasitesini artır<br>
            2) Yatak dönüş sürecini hızlandır<br>
            3) Ek vardiya ve görev dağılımını güncelle""",
            "summary_focus": "poliklinik kapasitesi",
        },
        "Yatak dönüş sürecini hızlandır": {
            "card_class": "action-card alt-blue",
            "icon": "🛏️",
            "title": "Yatak dönüş sürecini hızlandır",
            "chip": "Öncelik 2",
            "chip_class": "chip-blue",
            "desc": "Yatak çevrim hızındaki iyileşme kapasite sıkışıklığını azaltır ve yoğun saatlerde akışın korunmasını destekler.",
            "note": "💡 Yönetim notu: İlk aksiyonu destekleyen ikinci faz kapasite müdahalesi olarak değerlendirilmelidir.",
            "exec_title": "Öncelik: Yatak dönüş sürecini hızlandır",
            "exec_text": """Yatak akışının hızlandırılması, kapasite darboğazını doğrudan gevşetir ve servis döngüsünü daha verimli hale getirir.<br><br>
            1) Yatak dönüş sürecini hızlandır<br>
            2) Poliklinik kapasitesini güçlendir<br>
            3) İş gücü planını destekleyici olarak güncelle""",
            "summary_focus": "yatak dönüş hızı",
        },
        "Ek vardiya ve görev planı uygula": {
            "card_class": "action-card alt-cyan",
            "icon": "👩‍⚕️",
            "title": "Ek vardiya ve görev planı uygula",
            "chip": "Öncelik 3",
            "chip_class": "chip-cyan",
            "desc": "İş gücü dağılımının güçlendirilmesi hizmet kalitesini korur ve kapasite iyileştirmelerinin sürdürülebilirliğini artırır.",
            "note": "💡 Yönetim notu: Kaynak ve vardiya dengesi, operasyonel istikrar için destekleyici bir kaldıraçtır.",
            "exec_title": "Öncelik: Ek vardiya ve görev planı uygula",
            "exec_text": """Personel dağılımını güçlendirmek, yoğunluk saatlerinde hizmet seviyesini korur ve sistemdeki kırılgan alanları azaltır.<br><br>
            1) Ek vardiya ve görev planı uygula<br>
            2) Poliklinik kapasitesini destekle<br>
            3) Yatak çevrim süreçlerini paralel iyileştir""",
            "summary_focus": "iş gücü planlaması",
        }
    }

    ordered_actions = [
        "Poliklinik kapasitesini artır",
        "Yatak dönüş sürecini hızlandır",
        "Ek vardiya ve görev planı uygula"
    ]

    # =========================================================
    # HERO
    # =========================================================
    st.markdown("""
    <div class="op-hero">
        <div class="op-hero-top">
            <div class="op-hero-icon">✦</div>
            <div class="op-hero-title">Akıllı Operasyon Önerileri</div>
        </div>
        <div class="op-hero-sub">
            Operasyonel baskı alanlarını önceliklendirir, müdahale senaryolarının beklenen etkisini görünür hale getirir
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
    left, right = st.columns([1.12, 1], gap="large")

    with left:
        st.markdown("<div class='section-title'>🎯 Öncelikli Aksiyonlar</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-sub'>Mevcut tabloya göre en yüksek etki üretmesi beklenen müdahale sırası aşağıdadır.</div>", unsafe_allow_html=True)

        selected_action = st.radio(
            "Aksiyon seç:",
            ordered_actions
        )

        current = action_data[selected_action]

        st.markdown(f"""
        <div class="{current['card_class']} primary">
            <div class="action-top">
                <div class="action-title">{current['icon']} {current['title']}</div>
                <div class="action-chip {current['chip_class']}">{current['chip']}</div>
            </div>
            <div class="action-desc">
                {current['desc']}
            </div>
            <div class="action-note">
                {current['note']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        for action_name in ordered_actions:
            if action_name == selected_action:
                continue
            item = action_data[action_name]
            st.markdown(f"""
            <div class="{item['card_class']}">
                <div class="action-top">
                    <div class="action-title">{item['icon']} {item['title']}</div>
                    <div class="action-chip {item['chip_class']}">{item['chip']}</div>
                </div>
                <div class="action-desc">
                    {item['desc']}
                </div>
                <div class="action-note">
                    {item['note']}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:0.35rem;'></div>", unsafe_allow_html=True)

        st.markdown("<div class='section-title'>📌 Yöneticiye Net Yönlendirme</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="exec-card">
            <div class="exec-title">{current['exec_title']}</div>
            <div class="exec-text">
                {current['exec_text']}
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
                Seçili ana odak <b>{current['summary_focus']}</b> olarak değerlendirilmektedir.
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

        st.markdown("<div class='section-sub' style='margin-top:0.9rem; margin-bottom:0.2rem; font-weight:850; color:#12357a;'>🚨 Risk seviyesi</div>", unsafe_allow_html=True)
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
                Seçili öncelik <b>{current['title']}</b> olarak öne çıkmaktadır.
                Bu odak alanı üzerinden müdahale başlatıldığında risk seviyesi
                <b>{before_risk}/100</b> düzeyinden yaklaşık <b>{after_risk}/100</b> seviyesine çekilebilir.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 0.95rem;'></div>", unsafe_allow_html=True)

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
                Simülasyona göre seçili aksiyon <b>{current['title']}</b> için bekleme süresinde yaklaşık
                <b>%{abs(wait_effect)}</b> iyileşme ve toplam risk skorunda anlamlı bir geri çekilme beklenmektedir.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">Karar Notu</div>
            <div class="insight-text">
                Yönetimin odak noktası şu anda <b>{current['summary_focus']}</b> ekseninde şekillenmelidir.
                Destekleyici ikinci faz müdahaleler ile birlikte daha dengeli bir operasyon akışı kurulabilir.
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
            Mevcut tablo, öncelikli müdahale gerektirmektedir; seçili ilk adım <b>{current['title']}</b> olup,
            simülasyon sonucuna göre toplam risk seviyesi <b>{before_risk}/100</b> düzeyinden yaklaşık
            <b>{after_risk}/100</b> seviyesine çekilebilir.
        </div>
    </div>
    """, unsafe_allow_html=True)