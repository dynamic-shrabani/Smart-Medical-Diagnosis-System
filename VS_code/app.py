
import streamlit as st
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Smart Medical Diagnosis System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 5%, rgba(91,72,180,.15), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(236,72,153,.10), transparent 25%),
        #080d22;
}

/* Hide Streamlit default multipage navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #090d25 0%,
        #11143b 55%,
        #1a1049 100%
    );
    border-right: 1px solid rgba(160,130,255,.18);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.2rem;
}

.brand {
    padding: 10px 8px 20px 8px;
}

.brand-title {
    font-size: 22px;
    font-weight: 900;
    color: white;
}

.brand-title span {
    color: #c678ff;
}

.brand-subtitle {
    margin-top: 4px;
    color: #ff78c8;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.nav-label {
    color: #9997c9;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.5px;
    margin: 12px 8px 8px 8px;
}

section[data-testid="stSidebar"] .stButton {
    margin-bottom: 4px;
}

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    min-height: 42px;
    border-radius: 11px;
    border: 1px solid rgba(141,116,240,.22);
    background: rgba(49,43,105,.45);
    color: #ddd9ff;
    font-size: 13px;
    font-weight: 700;
    text-align: left;
    padding-left: 14px;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: linear-gradient(90deg,#4735b3,#7938ae);
    border-color: #ff75c7;
    color: white;
}

.ecg-box {
    margin: 40px 8px 0 8px;
    padding-top: 15px;
    border-top: 1px solid rgba(170,145,245,.15);
}

.ecg-title {
    color: #ff79c8;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.4px;
}

.ecg-sub {
    color: #8886b9;
    font-size: 10px;
    margin-top: 4px;
}

/* =========================================================
TOP NAV
========================================================= */

.top-space {
    height: 3px;
}

.top-title {
    color: #aaa8d2;
    font-size: 12px;
    padding-top: 8px;
}

.top-button .stButton > button {
    background: transparent;
    border: none;
    color: #aaa9d4;
    font-size: 13px;
    font-weight: 700;
    border-radius: 9px;
}

.top-button .stButton > button:hover {
    color: #ff7bc8;
    background: rgba(170,80,220,.12);
}

/* =========================================================
HERO
========================================================= */

.hero-box {
    margin-top: 16px;
    border-radius: 25px;
    padding: 43px 45px;
    min-height: 315px;
    background:
        radial-gradient(circle at 80% 50%, rgba(255,85,187,.25), transparent 25%),
        linear-gradient(125deg,#182d68 0%,#34217e 50%,#60247f 100%);
    border: 1px solid rgba(185,160,255,.25);
    box-shadow: 0 20px 60px rgba(0,0,0,.35);
}

.hero-badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 20px;
    background: rgba(255,118,200,.13);
    border: 1px solid rgba(255,130,210,.40);
    color: #ffb2df;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1px;
}

.hero-title {
    color: white;
    font-size: 45px;
    line-height: 1.06;
    font-weight: 900;
    letter-spacing: -1.7px;
    margin-top: 18px;
}

.hero-title span {
    color: #ff83ce;
}

.hero-text {
    color: #d4d3ec;
    font-size: 14px;
    line-height: 1.7;
    max-width: 650px;
    margin-top: 15px;
}

.hero-note {
    color: #aaa8d2;
    font-size: 10px;
    margin-top: 10px;
}

.visual-box {
    margin-top: 16px;
    min-height: 315px;
    border-radius: 25px;
    background:
        radial-gradient(circle at center,rgba(231,91,198,.27),transparent 42%),
        linear-gradient(145deg,#22246d,#562080);
    border: 1px solid rgba(185,160,255,.24);
    display: flex;
    justify-content: center;
    align-items: center;
}

.orbit {
    width: 205px;
    height: 205px;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,.18);
    box-shadow:
        0 0 0 20px rgba(170,120,255,.05),
        0 0 70px rgba(235,84,196,.18);
    display: flex;
    justify-content: center;
    align-items: center;
}

.core {
    width: 108px;
    height: 108px;
    border-radius: 28px;
    background: linear-gradient(145deg,#9158df,#df5eb0);
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 48px;
    font-weight: 900;
}

/* =========================================================
BUTTON
========================================================= */

.start-button .stButton > button {
    margin-top: -65px;
    margin-left: 45px;
    position: relative;
    z-index: 5;
    border: none;
    border-radius: 11px;
    background: linear-gradient(90deg,#7650e8,#d354b3);
    color: white;
    font-size: 12px;
    font-weight: 800;
    padding: 11px 20px;
    box-shadow: 0 8px 25px rgba(172,74,190,.28);
}

.start-button .stButton > button:hover {
    transform: translateY(-1px);
}

/* =========================================================
SECTIONS
========================================================= */

.section-title {
    color: #ff7ac8;
    font-size: 22px;
    font-weight: 900;
    margin-top: 32px;
}

.section-subtitle {
    color: #a9a7d0;
    font-size: 11px;
    margin-top: 3px;
    margin-bottom: 15px;
}

.card {
    background: linear-gradient(145deg,rgba(31,35,82,.96),rgba(21,21,58,.96));
    border: 1px solid rgba(145,125,225,.18);
    border-radius: 16px;
    padding: 20px;
    min-height: 135px;
}

.card-number {
    color: #a88cff;
    font-size: 10px;
    font-weight: 900;
}

.card-icon {
    font-size: 24px;
    margin: 6px 0;
}

.card-title {
    color: #ff83ce;
    font-size: 15px;
    font-weight: 800;
}

.card-text {
    color: #c1c0dc;
    font-size: 11px;
    line-height: 1.6;
    margin-top: 5px;
}

/* =========================================================
METRICS
========================================================= */

.metric {
    background: linear-gradient(145deg,rgba(31,34,82,.95),rgba(43,23,77,.95));
    border: 1px solid rgba(158,130,246,.18);
    border-radius: 15px;
    padding: 18px;
    text-align: center;
}

.metric-value {
    color: white;
    font-size: 26px;
    font-weight: 900;
}

.metric-label {
    color: #ff82cc;
    font-size: 10px;
    font-weight: 800;
    margin-top: 5px;
}

/* =========================================================
OVERVIEW
========================================================= */

.overview {
    background: rgba(20,22,56,.80);
    border: 1px solid rgba(148,124,231,.17);
    border-radius: 17px;
    padding: 24px;
}

.overview-title {
    color: #c99aff;
    font-size: 17px;
    font-weight: 900;
}

.overview-text {
    color: #c4c3df;
    font-size: 12px;
    line-height: 1.75;
    margin-top: 8px;
}

/* =========================================================
DISCLAIMER
========================================================= */

.disclaimer {
    margin-top: 22px;
    padding: 14px 17px;
    border-radius: 11px;
    background: rgba(255,111,191,.06);
    border: 1px solid rgba(255,111,191,.15);
    color: #aaa8c9;
    font-size: 10px;
    line-height: 1.6;
}

.disclaimer strong {
    color: #ff82cb;
}

.footer {
    text-align: center;
    color: #7776a4;
    font-size: 10px;
    margin-top: 28px;
    padding-top: 14px;
    border-top: 1px solid rgba(150,130,220,.10);
}


/* REMOVE DEFAULT STREAMLIT TOP HEADER */
[data-testid="stHeader"] {
    background: transparent !important;
    height: auto !important;
    min-height: 40px !important;
    visibility: visible !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

header {
    background: transparent !important;
}


/* HIDE DEFAULT STREAMLIT PAGE NAVIGATION */
[data-testid="stSidebarNav"] {
    display: none !important;
}


/* PREMIUM TOP NAVIGATION */
.top-title {
    color: #aaa8d2;
    font-size: 12px;
    padding-top: 8px;
}

.top-title + div {
    color: #aaa8d2;
}

div[data-testid="column"] .stButton > button {
    border-radius: 10px !important;
}



/* SKY BLUE START DIAGNOSIS */
.start-button .stButton > button {
    margin-top: -65px !important;
    margin-left: 45px !important;
    position: relative;
    z-index: 5;

    background: linear-gradient(
        135deg,
        #38bdf8,
        #2563eb
    ) !important;

    border: 1px solid rgba(125,211,252,.65) !important;
    color: white !important;

    border-radius: 12px !important;

    font-size: 12px !important;
    font-weight: 800 !important;

    padding: 11px 22px !important;

    box-shadow:
        0 8px 25px rgba(37,99,235,.30),
        0 0 18px rgba(56,189,248,.16) !important;
}

.start-button .stButton > button:hover {
    background: linear-gradient(
        135deg,
        #60d5ff,
        #3b82f6
    ) !important;

    border-color: #7dd3fc !important;

    transform: translateY(-2px) !important;
}


/* CLEAN SIDEBAR BRAND */
.brand {
    padding: 12px 8px 24px 8px !important;
}

.brand-title {
    font-size: 23px !important;
    font-weight: 900 !important;
    color: #ffffff !important;
    letter-spacing: -0.6px !important;
}

.brand-title span {
    color: #c678ff !important;
}

.brand-subtitle {
    color: #a99be8 !important;
    font-size: 9px !important;
    font-weight: 800 !important;
    letter-spacing: 1.8px !important;
}

.brand-tagline {
    margin-top: 5px;
    color: #a99be8;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1.8px;
}


/* PREMIUM START DIAGNOSIS BUTTON */
.start-button .stButton > button {
    margin-top: -65px !important;
    margin-left: 45px !important;
    position: relative;
    z-index: 5;

    background: linear-gradient(
        135deg,
        #7657e8,
        #a94fc4,
        #e05aaa
    ) !important;

    border: 1px solid rgba(221,169,255,0.60) !important;

    color: white !important;

    border-radius: 12px !important;

    font-size: 12px !important;
    font-weight: 800 !important;

    padding: 11px 22px !important;

    box-shadow:
        0 8px 25px rgba(135,75,210,0.32),
        0 0 18px rgba(225,90,180,0.12) !important;

    transition: all 0.2s ease !important;
}

.start-button .stButton > button:hover {
    background: linear-gradient(
        135deg,
        #8768f5,
        #bd5bd5,
        #ec6fbc
    ) !important;

    border-color: #f0b5ff !important;

    transform: translateY(-2px) !important;

    box-shadow:
        0 12px 32px rgba(140,70,220,0.38),
        0 0 24px rgba(230,90,190,0.20) !important;
}


/* START DIAGNOSIS BUTTON */
.start-button .stButton > button {
    background: linear-gradient(135deg, #38bdf8, #2563eb) !important;
    border: 1px solid #7dd3fc !important;
    color: white !important;
    border-radius: 12px !important;
    font-size: 12px !important;
    font-weight: 800 !important;
    padding: 11px 22px !important;
    box-shadow: 0 8px 25px rgba(37, 99, 235, 0.30) !important;
}

.start-button .stButton > button:hover {
    background: linear-gradient(135deg, #60d5ff, #3b82f6) !important;
    border-color: #bae6fd !important;
    transform: translateY(-2px) !important;
}


/* DIRECT START DIAGNOSIS BUTTON STYLE */
button[kind="primary"],
[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #8b5cf6 0%, #c04fcf 55%, #ec6bb5 100%) !important;
    background-color: #8b5cf6 !important;
    color: #ffffff !important;
    border: 1px solid #d8a4ff !important;
    border-radius: 12px !important;
    font-weight: 800 !important;
    box-shadow: 0 8px 25px rgba(170, 80, 210, 0.35) !important;
}

button[kind="primary"]:hover,
[data-testid="baseButton-primary"]:hover {
    background: linear-gradient(135deg, #9f75ff 0%, #d05be0 55%, #f27bc3 100%) !important;
    color: white !important;
    border-color: #f0c0ff !important;
    box-shadow: 0 10px 30px rgba(210, 90, 200, 0.45) !important;
}


/* RESTORE CUSTOM SIDEBAR */
section[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    width: 260px !important;
    min-width: 260px !important;
    background: linear-gradient(
        180deg,
        #090d25 0%,
        #11143b 55%,
        #1a1049 100%
    ) !important;
}

section[data-testid="stSidebar"] > div {
    display: block !important;
    visibility: visible !important;
}

section[data-testid="stSidebar"] .stButton {
    display: block !important;
    visibility: visible !important;
}

section[data-testid="stSidebar"] .stButton > button {
    display: block !important;
    visibility: visible !important;
}

.brand,
.nav-label,
.ecg-box,
.ecg-title,
.ecg-sub {
    display: block !important;
    visibility: visible !important;
}


/* KEEP STREAMLIT SIDEBAR TOGGLE VISIBLE */
[data-testid="stHeader"] {
    visibility: visible !important;
    background: transparent !important;
}

[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    z-index: 999999 !important;
}

[data-testid="stSidebarCollapsedControl"] button {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}


/* ===== FORCE SIDEBAR TOGGLE VISIBLE ===== */

[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: fixed !important;
    left: 8px !important;
    top: 12px !important;
    z-index: 9999999 !important;
    pointer-events: auto !important;
}

[data-testid="collapsedControl"] button {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    width: 40px !important;
    height: 40px !important;
}

[data-testid="collapsedControl"] svg {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}

[data-testid="stSidebarCollapseButton"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 9999999 !important;
}

[data-testid="stSidebarCollapseButton"] button {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
}


/* ===== FULL WIDTH HOME PAGE TEMPORARY FIX ===== */

section[data-testid="stSidebar"] {
    width: 280px !important;
    min-width: 280px !important;
}

section[data-testid="stSidebar"] > div {
    width: 280px !important;
    min-width: 280px !important;
}

section.main {
    margin-left: 0px !important;
}

[data-testid="stAppViewContainer"] > .main {
    margin-left: 0px !important;
}

.block-container {
    max-width: 1500px !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}


/* =========================================================
   MEDICAL AI HERO VISUAL
   ========================================================= */

.visual-box {
    margin-top: 16px !important;
    min-height: 315px !important;
    border-radius: 25px !important;
    background:
        radial-gradient(circle at 50% 48%, rgba(52,210,255,.20), transparent 28%),
        radial-gradient(circle at 50% 50%, rgba(168,73,255,.28), transparent 55%),
        linear-gradient(145deg,#20266f,#512080) !important;
    border: 1px solid rgba(185,160,255,.24) !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    overflow: hidden !important;
    position: relative !important;
}

.medical-scene {
    width: 285px;
    height: 285px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* glowing circular rings */
.medical-ring {
    position: absolute;
    border-radius: 50%;
    border: 1px solid rgba(111,220,255,.32);
}

.medical-ring.r1 {
    width: 185px;
    height: 185px;
}

.medical-ring.r2 {
    width: 225px;
    height: 225px;
    border-color: rgba(190,111,255,.22);
    box-shadow: 0 0 35px rgba(97,145,255,.12);
}

.medical-ring.r3 {
    width: 265px;
    height: 265px;
    border-color: rgba(255,255,255,.07);
}

/* orbit paths */
.orbit-path {
    position: absolute;
    width: 235px;
    height: 115px;
    border: 1px solid rgba(71,213,255,.32);
    border-radius: 50%;
    transform: rotate(28deg);
}

.orbit-path.two {
    transform: rotate(-28deg);
    border-color: rgba(207,92,255,.30);
}

/* central shield */
.medical-shield {
    width: 108px;
    height: 122px;
    position: relative;
    z-index: 5;
    display: flex;
    align-items: center;
    justify-content: center;
    clip-path: polygon(
        50% 0%,
        91% 15%,
        91% 56%,
        76% 79%,
        50% 100%,
        24% 79%,
        9% 56%,
        9% 15%
    );
    background:
        linear-gradient(145deg,#27c8ff 0%,#238bff 42%,#7844ff 100%);
    box-shadow:
        0 0 28px rgba(47,190,255,.55),
        0 0 55px rgba(125,75,255,.35);
}

.medical-shield::before {
    content: "";
    position: absolute;
    inset: 4px;
    clip-path: inherit;
    background: linear-gradient(145deg,#173b91,#47207d);
}

/* medical cross */
.medical-cross {
    position: relative;
    z-index: 2;
    color: white;
    font-size: 53px;
    line-height: 1;
    font-weight: 800;
    text-shadow: 0 0 18px rgba(255,255,255,.65);
}

/* floating icon bubbles */
.medical-node {
    position: absolute;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 8;
    color: white;
    font-size: 17px;
    background: linear-gradient(145deg,#16cfff,#7250ff);
    border: 1px solid rgba(255,255,255,.28);
    box-shadow: 0 0 20px rgba(48,184,255,.38);
}

.medical-node.n1 {
    top: 38px;
    left: 30px;
}

.medical-node.n2 {
    top: 24px;
    right: 28px;
    background: linear-gradient(145deg,#bd5cff,#ee68b8);
}

.medical-node.n3 {
    bottom: 39px;
    left: 42px;
    background: linear-gradient(145deg,#31d6e9,#367aff);
}

.medical-node.n4 {
    bottom: 27px;
    right: 35px;
    background: linear-gradient(145deg,#8c62ff,#d44fc1);
}

/* tiny glowing connection dots */
.medical-dot {
    position: absolute;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #7be8ff;
    box-shadow: 0 0 12px #56dfff;
    z-index: 4;
}

.medical-dot.d1 { top: 74px; left: 72px; }
.medical-dot.d2 { top: 63px; right: 74px; }
.medical-dot.d3 { bottom: 75px; left: 77px; }
.medical-dot.d4 { bottom: 62px; right: 77px; }


.metric-desc {
    color: #cbbcff;
    font-size: 13px;
    line-height: 1.45;
    margin-top: 8px;
}


/* TOP NAVIGATION - SKY + PINK */

div.stButton > button {
    background: linear-gradient(
        135deg,
        #ff69c4 0%,
        #b96cff 48%,
        #55d9ff 100%
    ) !important;

    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.30) !important;
    border-radius: 12px !important;
    font-weight: 700 !important;

    box-shadow:
        0 8px 25px rgba(255,105,196,0.22),
        0 5px 20px rgba(85,217,255,0.16) !important;

    transition: all 0.25s ease !important;
}

div.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #ff7bcf 0%,
        #b978ff 48%,
        #5fe0ff 100%
    ) !important;

    transform: translateY(-2px) !important;

    box-shadow:
        0 10px 30px rgba(255,105,196,0.35),
        0 8px 25px rgba(85,217,255,0.28) !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="brand">'
        '<div class="brand-title">Smart <span>Med</span></div>'
        '<div class="brand-subtitle">AI HEALTHCARE SYSTEM</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-label">NAVIGATION</div>',
        unsafe_allow_html=True
    )

    if st.button("⌂  Home", key="home_sidebar"):
        st.switch_page("app.py")

    if st.button("🩺  Diagnosis", key="diagnosis_sidebar"):
        st.switch_page("pages/1_🩺_Diagnosis.py")

    if st.button("📊  Model Insights", key="model_sidebar"):
        st.switch_page("pages/2_📊_Model_Insights.py")

    st.markdown(
        '<div class="ecg-box">'
        '<svg width="100%" height="55" viewBox="0 0 300 55" '
        'xmlns="http://www.w3.org/2000/svg">'
        '<path d="M0 30 L55 30 L67 30 L75 8 L84 47 L94 30 '
        'L125 30 L137 30 L145 18 L154 39 L163 30 '
        'L205 30 L215 30 L225 11 L235 45 L245 30 L300 30" '
        'fill="none" stroke="#ff79c8" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '</svg>'
        '<div class="ecg-title">SMART HEALTH INSIGHTS</div>'
        '<div class="ecg-sub">AI-assisted symptom analysis</div>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# TOP NAVIGATION
# =========================================================

top1, top2, top3, top4 = st.columns([4.5, 1.0, 1.35, 1.55])

with top1:
    st.markdown(
        '<div class="top-title">'
        'AI-powered medical decision support dashboard'
        '</div>',
        unsafe_allow_html=True
    )

with top2:
    if st.button("⌂  Home", key="top_home"):
        st.switch_page("app.py")

with top3:
    if st.button("🩺  Diagnosis", key="top_diagnosis"):
        st.switch_page("pages/1_🩺_Diagnosis.py")

with top4:
    if st.button("📊  Model Insights", key="top_model"):
        st.switch_page("pages/2_📊_Model_Insights.py")


# =========================================================
# HERO
# =========================================================

left, right = st.columns([1.65,1])

with left:

    st.markdown(
        '<div class="hero-box">'
        '<div class="hero-badge">✦ INTELLIGENT HEALTHCARE ANALYTICS</div>'
        '<div class="hero-title">'
        'Smart Medical<br>'
        '<span>Diagnosis System</span>'
        '</div>'
        '<div class="hero-text">'
        'An AI-assisted healthcare decision support system that '
        'analyzes selected symptoms and provides intelligent disease '
        'prediction with probability-based insights.'
        '</div>'
        '<div class="hero-note">'
        'Built with Machine Learning • Python • Streamlit'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="start-button">', unsafe_allow_html=True)

    if st.button("🩺  Start Diagnosis", key="start_diagnosis", type="primary"):
        st.switch_page("pages/1_🩺_Diagnosis.py")

    st.markdown('</div>', unsafe_allow_html=True)


with right:

    st.html("""
    <div class="visual-box">
        <div class="medical-scene">

            <div class="medical-ring r3"></div>
            <div class="medical-ring r2"></div>
            <div class="medical-ring r1"></div>

            <div class="orbit-path"></div>
            <div class="orbit-path two"></div>

            <div class="medical-dot d1"></div>
            <div class="medical-dot d2"></div>
            <div class="medical-dot d3"></div>
            <div class="medical-dot d4"></div>

            <div class="medical-node n1">♥</div>
            <div class="medical-node n2">✦</div>
            <div class="medical-node n3">⌁</div>
            <div class="medical-node n4">↗</div>

            <div class="medical-shield">
                <div class="medical-cross">+</div>
            </div>

        </div>
    </div>
    """)

# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown(
    '<div class="section-title">How It Works</div>'
    '<div class="section-subtitle">'
    'A simple three-step intelligent analysis workflow'
    '</div>',
    unsafe_allow_html=True
)

a, b, c = st.columns(3)

with a:
    st.markdown(
        '<div class="card">'
        '<div class="card-number">01</div>'
        '<div class="card-icon">🩺</div>'
        '<div class="card-title">Select Symptoms</div>'
        '<div class="card-text">'
        'Choose the symptoms that match the current condition.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with b:
    st.markdown(
        '<div class="card">'
        '<div class="card-number">02</div>'
        '<div class="card-icon">🧠</div>'
        '<div class="card-title">AI Analysis</div>'
        '<div class="card-text">'
        'The trained machine learning model processes the selected '
        'symptom pattern.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

with c:
    st.markdown(
        '<div class="card">'
        '<div class="card-number">03</div>'
        '<div class="card-icon">📊</div>'
        '<div class="card-title">View Insights</div>'
        '<div class="card-text">'
        'View the predicted condition, probability and top insights.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# PROJECT HIGHLIGHTS
# =========================================================

st.markdown(
    '<div class="section-title">Project Highlights</div>'
    '<div class="section-subtitle">'
    'Key technical components of the system'
    '</div>',
    unsafe_allow_html=True
)

m1,m2,m3,m4 = st.columns(4)

with m1:
    st.markdown(
        '<div class="metric">'
        '<div class="metric-value">132</div>'
        '<div class="metric-label">INPUT FEATURES</div>'
        '<div class="metric-desc">Symptom-based features used by the model</div>'
        '</div>',
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        '<div class="metric">'
        '<div class="metric-value">4</div>'
        '<div class="metric-label">ML MODELS COMPARED</div>'
        '<div class="metric-desc">Multiple classification algorithms evaluated</div>'
        '</div>',
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        '<div class="metric">'
        '<div class="metric-value">LR</div>'
        '<div class="metric-label">SELECTED MODEL</div>'
        '<div class="metric-desc">Logistic Regression selected for prediction</div>'
        '</div>',
        unsafe_allow_html=True
    )

with m4:
    st.markdown(
        '<div class="metric">'
        '<div class="metric-value">ML</div>'
        '<div class="metric-label">SUPERVISED LEARNING</div>'
        '<div class="metric-desc">Symptom-based disease classification</div>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# PROJECT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">Project Overview</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="overview">'
    '<div class="overview-title">'
    'Intelligent Symptom-Based Decision Support'
    '</div>'
    '<div class="overview-text">'
    'Smart Medical Diagnosis System is a machine-learning based '
    'academic project designed to demonstrate how symptom data can '
    'be processed through a trained classification model. The system '
    'compares multiple machine learning approaches and uses the '
    'selected model to generate prediction insights through an '
    'interactive Streamlit interface.'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# DISCLAIMER
# =========================================================

st.markdown(
    '<div class="disclaimer">'
    '<strong>Important:</strong> This project is an educational '
    'AI/ML prototype and should not be used as a substitute for '
    'professional medical diagnosis, consultation, or treatment.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    'Smart Medical Diagnosis System • AI / Machine Learning Project'
    '</div>',
    unsafe_allow_html=True
)
