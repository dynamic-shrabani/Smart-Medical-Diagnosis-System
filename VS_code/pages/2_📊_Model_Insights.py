
import streamlit as st
import joblib
from pathlib import Path


# ============================================================
# MODEL INSIGHTS NAVIGATION
# ============================================================

# ---------- TOP RIGHT NAVIGATION ----------

top_space, top_home, top_diagnosis = st.columns([7.0, 1.25, 1.85])

with top_home:
    if st.button("🏠  Home", key="top_home_btn", use_container_width=True):
        st.switch_page("app.py")

with top_diagnosis:
    if st.button("🩺  Diagnosis", key="top_diagnosis_btn", use_container_width=True):
        st.switch_page("pages/1_🩺_Diagnosis.py")


# ---------- NAVIGATION STYLING ----------

st.markdown("""
<style>

/* =========================================================
   TOP RIGHT LINKS
   ========================================================= */

div[data-testid="stHorizontalBlock"]
div[data-testid="column"]
div[data-testid="stPageLink"] a {

    background: linear-gradient(
        135deg,
        #55d9ff 0%,
        #9b6cff 48%,
        #ff69c4 100%
    ) !important;

    color: #ffffff !important;

    border: 1px solid rgba(255,255,255,0.35) !important;

    border-radius: 12px !important;

    min-height: 44px !important;

    padding: 10px 18px !important;

    justify-content: center !important;

    font-weight: 700 !important;

    white-space: nowrap !important;

    box-shadow:
        0 6px 20px rgba(85,217,255,0.25),
        0 6px 20px rgba(255,105,196,0.25) !important;

    text-decoration: none !important;
}


/* =========================================================
   SIDEBAR LINKS
   ========================================================= */

section[data-testid="stSidebar"]
div[data-testid="stPageLink"] a {

    background: linear-gradient(
        135deg,
        #ff69c4 0%,
        #d95cff 50%,
        #a96cff 100%
    ) !important;

    color: #ffffff !important;

    border: 1px solid rgba(255,255,255,0.25) !important;

    border-radius: 12px !important;

    min-height: 42px !important;

    padding: 10px 14px !important;

    font-weight: 700 !important;

    text-decoration: none !important;

    box-shadow:
        0 6px 18px rgba(255,105,196,0.25) !important;
}


/* Sidebar hover */

section[data-testid="stSidebar"]
div[data-testid="stPageLink"] a:hover {

    background: linear-gradient(
        135deg,
        #ff7dcc 0%,
        #e56cff 50%,
        #b77aff 100%
    ) !important;

    transform: translateX(3px);

}


/* Top hover */

div[data-testid="stHorizontalBlock"]
div[data-testid="column"]
div[data-testid="stPageLink"] a:hover {

    background: linear-gradient(
        135deg,
        #6ee0ff 0%,
        #aa78ff 48%,
        #ff7bcf 100%
    ) !important;

}

</style>
""", unsafe_allow_html=True)

# ============================================================






st.markdown("""
<style>

/* =========================================================
   TOP RIGHT NAVIGATION BUTTONS
   ========================================================= */

div[data-testid="stHorizontalBlock"] div[data-testid="column"] button {
    background: linear-gradient(
        135deg,
        #55d9ff 0%,
        #9b6cff 48%,
        #ff69c4 100%
    ) !important;

    color: #ffffff !important;

    border: 1px solid rgba(255,255,255,0.35) !important;

    border-radius: 12px !important;

    font-weight: 700 !important;

    font-size: 14px !important;

    height: 46px !important;

    min-width: 115px !important;

    width: 100% !important;

    padding: 8px 14px !important;

    white-space: nowrap !important;

    overflow: visible !important;

    text-overflow: clip !important;

    box-shadow:
        0 6px 20px rgba(85,217,255,0.25),
        0 6px 20px rgba(255,105,196,0.25) !important;

    transition: all 0.25s ease !important;
}


/* Diagnosis button wider */

div[data-testid="stHorizontalBlock"]
div[data-testid="column"]:last-child
button {
    min-width: 155px !important;
}


/* Top button hover */

div[data-testid="stHorizontalBlock"] div[data-testid="column"] button:hover {
    background: linear-gradient(
        135deg,
        #6ee0ff 0%,
        #aa78ff 48%,
        #ff7bcf 100%
    ) !important;

    transform: translateY(-2px) !important;

    box-shadow:
        0 8px 25px rgba(85,217,255,0.35),
        0 8px 25px rgba(255,105,196,0.35) !important;
}


/* =========================================================
   SIDEBAR NAVIGATION BUTTONS
   ========================================================= */

section[data-testid="stSidebar"] div.stButton > button {

    background: linear-gradient(
        135deg,
        #ff69c4 0%,
        #d95cff 50%,
        #a96cff 100%
    ) !important;

    color: #ffffff !important;

    border: 1px solid rgba(255,255,255,0.25) !important;

    border-radius: 12px !important;

    font-weight: 700 !important;

    font-size: 15px !important;

    width: 100% !important;

    min-height: 42px !important;

    padding: 10px 14px !important;

    box-shadow:
        0 6px 20px rgba(255,105,196,0.25) !important;

    transition: all 0.25s ease !important;
}


/* Sidebar hover */

section[data-testid="stSidebar"] div.stButton > button:hover {

    background: linear-gradient(
        135deg,
        #ff7dcc 0%,
        #e56cff 50%,
        #b77aff 100%
    ) !important;

    transform: translateX(3px) !important;

    box-shadow:
        0 8px 25px rgba(255,105,196,0.40) !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================








# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(



    page_title="Model Insights | Smart Medical Diagnosis System",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR.parent / "Model" / "smart_medical_diagnosis_model.pkl"

# ============================================================
# LOAD MODEL
# ============================================================

try:
    package = joblib.load(MODEL_PATH)

    model = package["model"]
    features = package["features"]

    model_loaded = True

except Exception:
    model_loaded = False
    features = []
    model = None

# ============================================================
# PREMIUM UI
# ============================================================

st.html("""
<style>

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 85% 8%,
            rgba(154,72,255,0.16),
            transparent 30%
        ),
        radial-gradient(
            circle at 10% 20%,
            rgba(40,190,255,0.08),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #06142f 0%,
            #071b3d 48%,
            #10102f 100%
        );
}

/* Hide default Streamlit navigation */

[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Main container */

.block-container {
    max-width: 1500px !important;
    padding-top: 28px !important;
    padding-bottom: 50px !important;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #242632 0%,
            #20212b 100%
        ) !important;
    border-right: 1px solid rgba(255,255,255,0.05);
}

.brand-title {
    color: #ffffff;
    font-size: 20px;
    font-weight: 900;
    letter-spacing: -0.5px;
}

.brand-title span {
    color: #55d9ff;
}

.brand-subtitle {
    margin-top: 6px;
    color: #55d9ff;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 3px;
}

.nav-label {
    margin-top: 28px;
    margin-bottom: 14px;
    color: #6ea9dd;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 3px;
}

.ecg-box {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.10);
}

.ecg-title {
    color: #ff79c8;
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 1.5px;
}

.ecg-sub {
    color: #829bc0;
    font-size: 10px;
    margin-top: 5px;
}

/* Sidebar buttons */

section[data-testid="stSidebar"] div.stButton > button {
    width: 100% !important;
    background: transparent !important;
    color: #e8eaff !important;
    border: 1px solid transparent !important;
    border-radius: 12px !important;
    text-align: left !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    min-height: 44px !important;
    box-shadow: none !important;
}

section[data-testid="stSidebar"] div.stButton > button:hover {
    background: linear-gradient(
        90deg,
        rgba(255,105,196,0.22),
        rgba(85,217,255,0.14)
    ) !important;
    border-color: rgba(255,255,255,0.12) !important;
}

/* Page heading */

.page-title {
    font-size: 38px;
    line-height: 1.1;
    font-weight: 900;
    color: #ffffff;
    margin-bottom: 8px;
}

.page-title span {
    background: linear-gradient(
        90deg,
        #ff79c8,
        #c06cff,
        #58dcff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.page-subtitle {
    color: #9db8dc;
    font-size: 15px;
    line-height: 1.7;
    margin-bottom: 26px;
}

/* Section title */

.section-title {
    margin-top: 30px;
    margin-bottom: 14px;
    color: #ffffff;
    font-size: 19px;
    font-weight: 850;
}

.section-title span {
    color: #55d9ff;
}

/* Metric cards */

.metric-card {
    min-height: 150px;
    padding: 22px;
    border-radius: 20px;
    background:
        linear-gradient(
            145deg,
            rgba(24,57,116,0.90),
            rgba(49,31,102,0.90)
        );
    border: 1px solid rgba(105,194,255,0.20);
    box-shadow: 0 15px 40px rgba(0,0,0,0.20);
}

.metric-icon {
    font-size: 24px;
    margin-bottom: 10px;
}

.metric-value {
    font-size: 30px;
    font-weight: 900;
    background: linear-gradient(
        90deg,
        #ff79c8,
        #66ddff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-label {
    color: #ffffff;
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 1px;
    margin-top: 4px;
}

.metric-desc {
    color: #a8bfe0;
    font-size: 11px;
    line-height: 1.5;
    margin-top: 7px;
}

/* Model cards */

.model-card {
    min-height: 155px;
    padding: 21px;
    border-radius: 18px;
    background: rgba(9,32,72,0.82);
    border: 1px solid rgba(86,168,255,0.18);
    margin-bottom: 12px;
}

.model-card.selected {
    background:
        linear-gradient(
            135deg,
            rgba(121,59,164,0.55),
            rgba(24,78,133,0.70)
        );
    border: 1px solid rgba(255,111,202,0.48);
    box-shadow:
        0 0 30px rgba(255,88,190,0.10);
}

.model-name {
    color: #ffffff;
    font-size: 17px;
    font-weight: 850;
}

.model-status {
    display: inline-block;
    margin-top: 8px;
    padding: 5px 10px;
    border-radius: 20px;
    background: rgba(255,111,202,0.13);
    color: #ff8dce;
    font-size: 9px;
    font-weight: 900;
    letter-spacing: 1px;
}

.model-desc {
    color: #9fb9d9;
    font-size: 11px;
    line-height: 1.6;
    margin-top: 12px;
}

/* Pipeline */

.pipeline-card {
    padding: 20px;
    border-radius: 18px;
    background: rgba(8,30,68,0.80);
    border: 1px solid rgba(79,180,255,0.16);
    text-align: center;
    min-height: 130px;
}

.pipeline-number {
    width: 32px;
    height: 32px;
    margin: auto;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(
        135deg,
        #ff70c5,
        #55d9ff
    );
    color: white;
    font-weight: 900;
}

.pipeline-name {
    color: #ffffff;
    font-size: 13px;
    font-weight: 800;
    margin-top: 12px;
}

.pipeline-desc {
    color: #8fa9cc;
    font-size: 10px;
    line-height: 1.5;
    margin-top: 6px;
}

/* Info cards */

.info-card {
    padding: 22px;
    border-radius: 18px;
    background: rgba(10,35,76,0.78);
    border: 1px solid rgba(90,170,255,0.16);
    color: #b4c9e5;
    font-size: 12px;
    line-height: 1.7;
}

.info-title {
    color: #ffffff;
    font-size: 16px;
    font-weight: 850;
    margin-bottom: 10px;
}

/* Disclaimer */

.disclaimer {
    margin-top: 30px;
    padding: 16px 20px;
    border-radius: 14px;
    background: rgba(41,38,31,0.70);
    border: 1px solid rgba(255,190,80,0.25);
    color: #ffc45d;
    font-size: 11px;
    line-height: 1.6;
}


/* ============================================================
   MODEL INSIGHTS - CLEAN FULL PAGE
   ============================================================ */

/* Remove Streamlit top black header */
[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
}

/* Remove top toolbar */
[data-testid="stToolbar"] {
    display: none !important;
}

/* Main content */
section.main {
    background: transparent !important;
}

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(
            circle at 85% 8%,
            rgba(154,72,255,0.16),
            transparent 30%
        ),
        radial-gradient(
            circle at 10% 20%,
            rgba(40,190,255,0.08),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #06142f 0%,
            #071b3d 48%,
            #10102f 100%
        ) !important;
}

/* Full available content width */
.block-container {
    max-width: 1500px !important;
    width: 100% !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-top: 30px !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-bottom: 50px !important;
}

/* Sidebar stays clean */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #242632 0%,
        #20212b 100%
    ) !important;
}

/* Prevent HTML overflow */
.main * {
    box-sizing: border-box;
}

</style>
""")

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html(
        '<div class="brand-title">Smart <span>Med</span></div>'
        '<div class="brand-subtitle">AI HEALTHCARE SYSTEM</div>',
        
    )

    st.html(
        '<div class="nav-label">NAVIGATION</div>',
        
    )

    st.page_link(
        "app.py",
        label="🏠  Home",
        use_container_width=True
    )

    st.page_link(
        "pages/1_🩺_Diagnosis.py",
        label="🩺  Diagnosis",
        use_container_width=True
    )

    st.page_link(
        "pages/2_📊_Model_Insights.py",
        label="📊  Model Insights",
        use_container_width=True
    )

    st.html("""
    <div class="ecg-box">

        <svg width="100%" height="55" viewBox="0 0 300 55"
             xmlns="http://www.w3.org/2000/svg">

            <path
                d="M0 30 L55 30 L67 30 L75 8 L84 47 L94 30
                   L125 30 L137 30 L145 18 L154 39 L163 30
                   L205 30 L215 30 L225 11 L235 45 L245 30 L300 30"
                fill="none"
                stroke="#ff79c8"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"/>

        </svg>

        <div class="ecg-title">SMART HEALTH INSIGHTS</div>
        <div class="ecg-sub">AI-assisted symptom analysis</div>

    </div>
    """)

# ============================================================
# HEADER
# ============================================================

st.html("""
<div class="page-title">
    Model <span>Insights</span>
</div>

<div class="page-subtitle">
    Explore the machine-learning architecture, model comparison,
    evaluation summary, and technical pipeline behind the
    Smart Medical Diagnosis System.
</div>
""")

# ============================================================
# TOP METRICS
# ============================================================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.html("""
    <div class="metric-card">
        <div class="metric-icon">🧬</div>
        <div class="metric-value">132</div>
        <div class="metric-label">INPUT FEATURES</div>
        <div class="metric-desc">
            Symptom-based model input features.
        </div>
    </div>
    """)

with m2:
    st.html("""
    <div class="metric-card">
        <div class="metric-icon">🤖</div>
        <div class="metric-value">4</div>
        <div class="metric-label">ML MODELS</div>
        <div class="metric-desc">
            Classification algorithms evaluated.
        </div>
    </div>
    """)

with m3:
    st.html("""
    <div class="metric-card">
        <div class="metric-icon">🎯</div>
        <div class="metric-value">LR</div>
        <div class="metric-label">SELECTED MODEL</div>
        <div class="metric-desc">
            Logistic Regression used for prediction.
        </div>
    </div>
    """)

with m4:
    st.html("""
    <div class="metric-card">
        <div class="metric-icon">🧠</div>
        <div class="metric-value">ML</div>
        <div class="metric-label">LEARNING TYPE</div>
        <div class="metric-desc">
            Supervised multi-class classification.
        </div>
    </div>
    """)

# ============================================================
# MODEL COMPARISON
# ============================================================

st.html("""
<div class="section-title">
    Model <span>Comparison</span>
</div>
""")

c1, c2 = st.columns(2)

with c1:

    st.html("""
    <div class="model-card selected">

        <div class="model-name">
            Logistic Regression
        </div>

        <div class="model-status">
            SELECTED MODEL
        </div>

        <div class="model-desc">
            Used as the final prediction model because it provides
            a simple, efficient and interpretable baseline for
            symptom-based multi-class classification.
        </div>

        <div style="margin-top:18px;padding-top:14px;
                    border-top:1px solid rgba(255,255,255,0.12);
                    font-size:14px;line-height:1.7;color:#a9c7ed;">

            <div><span style="color:#ff91c8;font-weight:700;">TYPE</span>
            &nbsp; Linear Classification</div>

            <div><span style="color:#ff91c8;font-weight:700;">ROLE</span>
            &nbsp; Final Prediction Model</div>

            <div><span style="color:#ff91c8;font-weight:700;">STRENGTH</span>
            &nbsp; Simple &amp; Interpretable</div>

            <div><span style="color:#ff91c8;font-weight:700;">TASK</span>
            &nbsp; Multi-class Disease Classification</div>

        </div>

    </div>
    """)

    st.html("""
    <div class="model-card">

        <div class="model-name">
            Random Forest
        </div>

        <div class="model-status">
            EVALUATED
        </div>

        <div class="model-desc">
            Ensemble classification approach based on multiple
            decision trees.
        </div>

        <div style="margin-top:18px;padding-top:14px;
                    border-top:1px solid rgba(255,255,255,0.12);
                    font-size:14px;line-height:1.7;color:#a9c7ed;">

            <div><span style="color:#ff91c8;font-weight:700;">TYPE</span>
            &nbsp; Ensemble Learning</div>

            <div><span style="color:#ff91c8;font-weight:700;">ROLE</span>
            &nbsp; Comparative Model</div>

            <div><span style="color:#ff91c8;font-weight:700;">STRENGTH</span>
            &nbsp; Multiple Decision Trees</div>

            <div><span style="color:#ff91c8;font-weight:700;">TASK</span>
            &nbsp; Disease Classification</div>

        </div>

    </div>
    """)

with c2:

    st.html("""
    <div class="model-card">

        <div class="model-name">
            Support Vector Machine
        </div>

        <div class="model-status">
            EVALUATED
        </div>

        <div class="model-desc">
            Margin-based classification method evaluated against
            the same symptom feature space.
        </div>

        <div style="margin-top:18px;padding-top:14px;
                    border-top:1px solid rgba(255,255,255,0.12);
                    font-size:14px;line-height:1.7;color:#a9c7ed;">

            <div><span style="color:#ff91c8;font-weight:700;">TYPE</span>
            &nbsp; Margin-based Classification</div>

            <div><span style="color:#ff91c8;font-weight:700;">ROLE</span>
            &nbsp; Comparative Model</div>

            <div><span style="color:#ff91c8;font-weight:700;">STRENGTH</span>
            &nbsp; High-dimensional Feature Space</div>

            <div><span style="color:#ff91c8;font-weight:700;">TASK</span>
            &nbsp; Multi-class Classification</div>

        </div>

    </div>
    """)

    st.html("""
    <div class="model-card">

        <div class="model-name">
            Gradient Boosting
        </div>

        <div class="model-status">
            EVALUATED
        </div>

        <div class="model-desc">
            Sequential ensemble method evaluated for disease
            classification performance.
        </div>

        <div style="margin-top:18px;padding-top:14px;
                    border-top:1px solid rgba(255,255,255,0.12);
                    font-size:14px;line-height:1.7;color:#a9c7ed;">

            <div><span style="color:#ff91c8;font-weight:700;">TYPE</span>
            &nbsp; Sequential Ensemble</div>

            <div><span style="color:#ff91c8;font-weight:700;">ROLE</span>
            &nbsp; Comparative Model</div>

            <div><span style="color:#ff91c8;font-weight:700;">STRENGTH</span>
            &nbsp; Iterative Error Reduction</div>

            <div><span style="color:#ff91c8;font-weight:700;">TASK</span>
            &nbsp; Disease Classification</div>

        </div>

    </div>
    """)

# ============================================================
# PIPELINE
# ============================================================

st.html("""
<div class="section-title">
    Machine Learning <span>Pipeline</span>
</div>
""")

p1, p2, p3, p4 = st.columns(4)

pipeline = [
    (
        p1,
        "1",
        "Symptom Input",
        "User selects symptoms from the available model features."
    ),
    (
        p2,
        "2",
        "Feature Vector",
        "Selected symptoms are converted into the 132-feature input vector."
    ),
    (
        p3,
        "3",
        "ML Prediction",
        "The trained Logistic Regression model processes the vector."
    ),
    (
        p4,
        "4",
        "Prediction Insight",
        "The system displays the predicted disease and probability."
    )
]

for col, number, name, desc in pipeline:

    with col:

        st.html(
            f"""
            <div class="pipeline-card">

                <div class="pipeline-number">
                    {number}
                </div>

                <div class="pipeline-name">
                    {name}
                </div>

                <div class="pipeline-desc">
                    {desc}
                </div>

            </div>
            """,
            
        )

# ============================================================
# EVALUATION
# ============================================================

st.html("""
<div class="section-title">
    Evaluation <span>Summary</span>
</div>
""")

e1, e2 = st.columns([1, 1])

with e1:

    st.html("""
    <div class="info-card">

        <div class="info-title">
            Clean Holdout Evaluation
        </div>

        The dataset contained substantial duplicate rows.
        After duplicate removal, the cleaned dataset contained
        304 unique samples.

        <br><br>

        A clean holdout evaluation used 61 samples for testing
        and 243 samples for training.

        <br><br>

        <b style="color:#ff79c8;">
            Reported clean holdout metrics:
        </b>

        Accuracy: 100% &nbsp; • &nbsp;
        Precision: 100% &nbsp; • &nbsp;
        Recall: 100% &nbsp; • &nbsp;
        F1-score: 100%

    </div>
    """)

with e2:

    st.html("""
    <div class="info-card">

        <div class="info-title">
            Dataset Overview
        </div>

        <b style="color:#55d9ff;">Original training samples:</b>
        4,920

        <br>

        <b style="color:#55d9ff;">Original feature columns:</b>
        132 model features

        <br>

        <b style="color:#55d9ff;">Unique samples after cleaning:</b>
        304

        <br>

        <b style="color:#55d9ff;">Learning approach:</b>
        Supervised multi-class classification

        <br>

        <b style="color:#55d9ff;">Selected algorithm:</b>
        Logistic Regression

    </div>
    """)

# ============================================================
# WHY LOGISTIC REGRESSION
# ============================================================

st.html("""
<div class="section-title">
    Why <span>Logistic Regression?</span>
</div>
""")

st.html("""
<div class="info-card">

    Logistic Regression provides a strong and interpretable baseline
    for binary and multi-class classification. For this project,
    the model works with a fixed symptom-feature representation,
    making the prediction pipeline lightweight and straightforward
    to integrate into the Streamlit application.

    <br><br>

    The selected model is used for the final prototype because it
    provides a practical balance between classification performance,
    simplicity, and deployment efficiency.

</div>
""")

# ============================================================
# TECH STACK
# ============================================================

st.html("""
<div class="section-title">
    Technical <span>Stack</span>
</div>
""")

t1, t2, t3, t4 = st.columns(4)

tech = [
    (t1, "🐍", "Python", "Core programming language"),
    (t2, "📐", "Scikit-learn", "Machine-learning algorithms"),
    (t3, "📊", "Pandas", "Data preparation and processing"),
    (t4, "⚡", "Streamlit", "Interactive application interface")
]

for col, icon, name, desc in tech:

    with col:

        st.html(
            f"""
            <div class="pipeline-card">

                <div style="font-size:25px;">
                    {icon}
                </div>

                <div class="pipeline-name">
                    {name}
                </div>

                <div class="pipeline-desc">
                    {desc}
                </div>

            </div>
            """,
            
        )

# ============================================================
# DISCLAIMER
# ============================================================

st.html("""
<div class="disclaimer">
    ⚠️ Educational decision-support prototype only.
    The reported evaluation results describe this project's
    cleaned dataset and holdout experiment; they do not establish
    clinical accuracy or real-world diagnostic reliability.
    The system should not replace advice from a qualified
    healthcare professional.
</div>
""")

st.markdown("""
<style>

/* =========================================================
   MODEL INSIGHTS - FINAL NAVIGATION COLORS
   ========================================================= */

/* ---------- MAIN PAGE HOME + DIAGNOSIS ---------- */

div.stButton > button {
    background: linear-gradient(
        135deg,
        #55d9ff 0%,
        #9b6cff 50%,
        #ff69c4 100%
    ) !important;

    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    min-height: 42px !important;

    box-shadow:
        0 5px 18px rgba(85,217,255,0.20),
        0 5px 18px rgba(255,105,196,0.20) !important;
}

/* Main button hover */
div.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #6de0ff 0%,
        #aa7aff 50%,
        #ff7bca 100%
    ) !important;

    color: #ffffff !important;
    border-color: rgba(255,255,255,0.75) !important;

    box-shadow:
        0 8px 25px rgba(85,217,255,0.35),
        0 8px 25px rgba(255,105,196,0.30) !important;
}


/* ---------- SIDEBAR BUTTONS ---------- */

section[data-testid="stSidebar"] div.stButton > button {
    background: linear-gradient(
        135deg,
        #55d9ff 0%,
        #9b6cff 50%,
        #ff69c4 100%
    ) !important;

    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
    min-height: 42px !important;

    box-shadow:
        0 5px 18px rgba(85,217,255,0.18),
        0 5px 18px rgba(255,105,196,0.18) !important;
}


/* Sidebar hover */
section[data-testid="stSidebar"] div.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #6de0ff 0%,
        #aa7aff 50%,
        #ff7bca 100%
    ) !important;

    color: #ffffff !important;
    border-color: rgba(255,255,255,0.75) !important;

    box-shadow:
        0 8px 24px rgba(85,217,255,0.32),
        0 8px 24px rgba(255,105,196,0.28) !important;
}


/* Make button text/icon clearly visible */
div.stButton > button p,
div.stButton > button span {
    color: #ffffff !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* MODEL INSIGHTS SIDEBAR BUTTONS */
section[data-testid="stSidebar"] [data-testid="stButton"] > button {
    width: 100% !important;

    background: linear-gradient(
        135deg,
        #55d9ff 0%,
        #9b6cff 48%,
        #ff69c4 100%
    ) !important;

    background-color: #9b6cff !important;

    color: #ffffff !important;
    border: 1px solid rgba(255,255,255,0.35) !important;
    border-radius: 12px !important;

    font-weight: 700 !important;
    min-height: 44px !important;

    box-shadow:
        0 6px 18px rgba(85,217,255,0.22),
        0 6px 18px rgba(255,105,196,0.22) !important;
}

/* Sidebar button text */
section[data-testid="stSidebar"] [data-testid="stButton"] > button p,
section[data-testid="stSidebar"] [data-testid="stButton"] > button span {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Hover */
section[data-testid="stSidebar"] [data-testid="stButton"] > button:hover {
    background: linear-gradient(
        135deg,
        #6de0ff 0%,
        #aa7aff 48%,
        #ff7bca 100%
    ) !important;

    color: #ffffff !important;
    border-color: rgba(255,255,255,0.75) !important;

    transform: translateY(-1px) !important;

    box-shadow:
        0 8px 24px rgba(85,217,255,0.35),
        0 8px 24px rgba(255,105,196,0.32) !important;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR FINAL SKY PINK GRADIENT
st.markdown('\n<style>\n\nsection[data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"] {\n    background: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    background-image: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    color: white !important;\n    border: 1px solid rgba(255,255,255,0.40) !important;\n    border-radius: 12px !important;\n    min-height: 44px !important;\n    font-weight: 700 !important;\n\n    box-shadow:\n        0 6px 20px rgba(85,217,255,0.25),\n        0 6px 20px rgba(255,105,196,0.25) !important;\n}\n\nsection[data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"] * {\n    color: white !important;\n}\n\nsection[data-testid="stSidebar"] button[data-testid="stBaseButton-secondary"]:hover {\n    background: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n\n    background-image: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n\n    color: white !important;\n    border-color: rgba(255,255,255,0.80) !important;\n}\n\n</style>\n', unsafe_allow_html=True)

st.markdown('\n<style>\n\n/* =========================================================\n   MODEL INSIGHTS SIDEBAR\n   FORCE GRADIENT ON ALL 3 NAVIGATION BUTTONS\n   ========================================================= */\n\nsection[data-testid="stSidebar"] div.stButton > button,\nsection[data-testid="stSidebar"] div.stButton > button:hover,\nsection[data-testid="stSidebar"] div.stButton > button:focus,\nsection[data-testid="stSidebar"] div.stButton > button:focus-visible,\nsection[data-testid="stSidebar"] div.stButton > button:active {\n\n    background: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    background-color: #9b6cff !important;\n    background-image: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    color: #ffffff !important;\n\n    border: 1px solid rgba(255,255,255,0.38) !important;\n    border-radius: 12px !important;\n\n    min-height: 44px !important;\n    width: 100% !important;\n\n    font-weight: 700 !important;\n\n    box-shadow:\n        0 6px 20px rgba(85,217,255,0.25),\n        0 6px 20px rgba(255,105,196,0.25) !important;\n}\n\n\n/* Force all inner text/icons white */\nsection[data-testid="stSidebar"] div.stButton > button *,\nsection[data-testid="stSidebar"] div.stButton > button:hover *,\nsection[data-testid="stSidebar"] div.stButton > button:focus *,\nsection[data-testid="stSidebar"] div.stButton > button:active * {\n    color: #ffffff !important;\n}\n\n\n/* Hover effect */\nsection[data-testid="stSidebar"] div.stButton > button:hover {\n    transform: translateY(-1px) !important;\n\n    background: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n\n    background-image: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n}\n\n</style>\n', unsafe_allow_html=True)

# SIDEBAR NAVIGATION CONVERTED TO PAGE LINKS
st.markdown('\n<style>\n\n/* =====================================================\n   MODEL INSIGHTS SIDEBAR NAVIGATION\n   SKY BLUE + PURPLE + PINK\n   ===================================================== */\n\nsection[data-testid="stSidebar"]\na[data-testid="stPageLink-NavLink"] {\n\n    display: flex !important;\n    align-items: center !important;\n    justify-content: center !important;\n\n    width: 100% !important;\n    min-height: 44px !important;\n\n    margin: 8px 0 !important;\n    padding: 10px 14px !important;\n\n    background: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    background-image: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    color: #ffffff !important;\n\n    border: 1px solid rgba(255,255,255,0.38) !important;\n    border-radius: 12px !important;\n\n    box-shadow:\n        0 6px 18px rgba(85,217,255,0.22),\n        0 6px 18px rgba(255,105,196,0.22) !important;\n\n    text-decoration: none !important;\n\n    font-weight: 700 !important;\n}\n\n\n/* Text inside the links */\nsection[data-testid="stSidebar"]\na[data-testid="stPageLink-NavLink"] span {\n\n    color: #ffffff !important;\n    font-weight: 700 !important;\n}\n\n\n/* Hover */\nsection[data-testid="stSidebar"]\na[data-testid="stPageLink-NavLink"]:hover {\n\n    background: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n\n    background-image: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n\n    color: #ffffff !important;\n\n    transform: translateY(-1px) !important;\n\n    box-shadow:\n        0 9px 25px rgba(85,217,255,0.32),\n        0 9px 25px rgba(255,105,196,0.30) !important;\n}\n\n</style>\n', unsafe_allow_html=True)

st.markdown('\n<style>\n.model-details {\n    margin-top: 18px;\n    padding-top: 14px;\n    border-top: 1px solid rgba(255,255,255,0.12);\n}\n\n.model-details div {\n    margin: 7px 0;\n    color: #a9c7ed;\n    font-size: 14px;\n    line-height: 1.45;\n}\n\n.model-details span {\n    display: inline-block;\n    min-width: 82px;\n    color: #ff91c8;\n    font-weight: 700;\n    text-transform: uppercase;\n    letter-spacing: 0.5px;\n    font-size: 12px;\n}\n</style>\n', unsafe_allow_html=True)
