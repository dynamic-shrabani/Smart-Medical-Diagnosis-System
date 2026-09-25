
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Diagnosis | Smart Medical Diagnosis System",
    page_icon="🩺",
    layout="wide"
)

# Analysis state
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "saved_prediction" not in st.session_state:
    st.session_state.saved_prediction = None




# ============================================================
# LOAD MODEL
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR.parent / "Model" / "smart_medical_diagnosis_model.pkl"

try:
    package = joblib.load(MODEL_PATH)
    model = package["model"]
    features = package["features"]
    model_loaded = True
except Exception as e:
    model = None
    features = []
    model_loaded = False


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

#MainMenu,
footer,
header {
    visibility: hidden;
}

.stApp {
    background:
        radial-gradient(circle at 82% 8%, rgba(0,150,255,0.13), transparent 28%),
        radial-gradient(circle at 10% 85%, rgba(110,45,220,0.14), transparent 30%),
        linear-gradient(135deg, #030817, #06152f 50%, #031b3b);
}

.main .block-container {
    max-width: 1400px;
    padding-top: 1rem;
    padding-left: 2.5rem;
    padding-right: 2.5rem;
    padding-bottom: 3rem;
}

/* Headings */

.page-title {
    color: #ffffff;
    font-size: 34px;
    font-weight: 950;
    line-height: 1.05;
    margin-top: 10px;
}

.page-title span {
    color: #55c9ff;
}

.page-subtitle {
    color: #8da8c9;
    font-size: 12px;
    margin-top: 8px;
}

/* Main cards */

.analysis-card {
    margin-top: 25px;
    padding: 24px;
    border-radius: 18px;
    background:
        linear-gradient(
            145deg,
            rgba(15,70,140,0.72),
            rgba(6,35,75,0.88)
        );
    border: 1px solid rgba(70,180,255,0.25);
    box-shadow: 0 15px 35px rgba(0,0,0,0.20);
}

.card-title {
    color: #ffffff;
    font-size: 17px;
    font-weight: 850;
}

.card-description {
    color: #819fc2;
    font-size: 10px;
    margin-top: 5px;
    margin-bottom: 15px;
}

/* Multiselect */

div[data-baseweb="select"] > div {
    background-color: #081b3b !important;
    border: 1px solid rgba(75,190,255,0.30) !important;
    border-radius: 11px !important;
}

div[data-baseweb="select"] span {
    color: #ffffff !important;
}

div[data-baseweb="select"] input {
    color: #ffffff !important;
}

/* Analyze button */

div.stButton > button {
    min-height: 45px !important;
    border-radius: 25px !important;
    border: none !important;
    background: linear-gradient(
        90deg,
        #ff73bd,
        #8f78ff
    ) !important;
    color: #ffffff !important;
    font-weight: 900 !important;
    box-shadow: 0 8px 25px rgba(255,80,170,0.20) !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(255,80,170,0.30) !important;
}

/* Result */

.result-card {
    margin-top: 22px;
    padding: 23px;
    border-radius: 18px;
    background:
        linear-gradient(
            135deg,
            rgba(18,85,160,0.78),
            rgba(7,40,85,0.88)
        );
    border: 1px solid rgba(75,190,255,0.30);
}

.result-label {
    color: #79a0ca;
    font-size: 9px;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.result-disease {
    color: #ffffff;
    font-size: 29px;
    font-weight: 950;
    margin-top: 6px;
}

.probability {
    color: #ff82c5;
    font-size: 20px;
    font-weight: 900;
    margin-top: 7px;
}

/* Top predictions */

.prediction-card {
    margin-top: 12px;
    padding: 13px 15px;
    border-radius: 11px;
    background: rgba(7,30,65,0.70);
    border: 1px solid rgba(75,170,255,0.18);
}

.prediction-name {
    color: #ffffff;
    font-size: 11px;
    font-weight: 750;
}

.prediction-percent {
    color: #65d6ff;
    font-size: 10px;
    font-weight: 800;
}

.bar-bg {
    height: 6px;
    margin-top: 7px;
    border-radius: 10px;
    background: rgba(255,255,255,0.08);
}

.bar-fill {
    height: 6px;
    border-radius: 10px;
    background: linear-gradient(90deg,#54d9ff,#a76fff);
}

/* Summary */

.summary-card {
    margin-top: 18px;
    padding: 18px;
    border-radius: 14px;
    background: rgba(8,43,88,0.72);
    border: 1px solid rgba(75,180,255,0.18);
}

.summary-title {
    color: #ffffff;
    font-size: 13px;
    font-weight: 850;
}

.summary-text {
    color: #f3efff;
    font-size: 17px;
    line-height: 1.75;
    margin-top: 10px;
}

/* Disclaimer */

.disclaimer {
    margin-top: 22px;
    padding: 13px;
    border-radius: 11px;
    background: rgba(255,179,0,0.06);
    border: 1px solid rgba(255,192,52,0.18);
    color: #d8c48d;
    font-size: 9px;
    line-height: 1.55;
}


.summary-box {
    font-size: 17px !important;
    line-height: 1.8 !important;
    color: #f3efff !important;
    padding: 22px 26px !important;
    margin-top: 10px !important;
}

.summary-box strong {
    color: #ff79c8 !important;
    font-size: 18px !important;
}


/* Hide Streamlit default page navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.html("""
    <div style="
        padding:15px 10px 20px 10px;
        border-bottom:1px solid rgba(255,255,255,0.08);
    ">

        <div style="
            font-size:25px;
            margin-bottom:6px;
        ">
            🩺
        </div>

        <div style="
            color:white;
            font-size:22px;
            font-weight:900;
        ">
            SMART MEDICAL
        </div>

        <div style="
            color:#55d9ff;
            font-size:13px;
            font-weight:900;
            letter-spacing:2.5px;
            margin-top:5px;
        ">
            DIAGNOSIS SYSTEM
        </div>

    </div>
    """)

    st.html("""
    <div style="
        color:#55d9ff;
        font-size:14px;
        font-weight:800;
        letter-spacing:2.5px;
        margin:24px 7px 12px;
    ">
        NAVIGATION
    </div>
    """)

    if st.button("⌂  Home", key="diag_home"):
        st.switch_page("app.py")

    if st.button("🩺  Diagnosis", key="diag_current"):
        st.switch_page("pages/1_🩺_Diagnosis.py")

    if st.button("📊  Model Insights", key="diag_model"):
        st.switch_page("pages/2_📊_Model_Insights.py")

    # Medical ECG line

    st.html("""
    <div style="
        margin-top:75px;
        padding:18px 5px;
        border-top:1px solid rgba(255,255,255,0.07);
        text-align:center;
    ">

        <svg
            width="170"
            height="55"
            viewBox="0 0 170 55"
            style="max-width:100%;"
        >

            <polyline
                points="
                    0,28
                    25,28
                    34,28
                    42,27
                    48,8
                    54,45
                    61,27
                    82,27
                    91,27
                    99,26
                    105,12
                    111,42
                    118,27
                    143,27
                    152,27
                    170,27
                "
                fill="none"
                stroke="#4ed8ff"
                stroke-width="2.5"
                stroke-linecap="round"
                stroke-linejoin="round"
            />

            <circle
                cx="54"
                cy="45"
                r="3"
                fill="#ff72bd"
            />

        </svg>

        <div style="
            
            
            
            margin-top:2px; font-size:16px; color:#55d9ff; font-weight:900; letter-spacing:2px;">
            AI HEALTH ANALYSIS
        </div>

        <div style="
            
            
            margin-top:4px; font-size:16px; color:#ff69c4; font-weight:900; letter-spacing:2px;">
            Better Insights
        </div>

    </div>
    """)



# ============================================================
# BACK TO HOME
# ============================================================

# Home + Model Insights navigation
nav1, nav2 = st.columns(2)

with nav1:
    if st.button(
        "←  Back to Home",
        key="back_home"
    ):
        st.switch_page("app.py")

with nav2:
    if st.button(
        "📊  Model Insights",
        key="model_insights_nav"
    ):
        st.switch_page("pages/2_📊_Model_Insights.py")


# ============================================================
# PAGE HEADER
# ============================================================

st.html("""
<div class="page-title">
    AI Symptom <span>Analysis</span>
</div>

<div class="page-subtitle">
    Select symptoms and let the trained machine-learning model
    analyze the symptom pattern.
</div>
""")


# ============================================================
# MODEL ERROR
# ============================================================

if not model_loaded:

    st.error(
        "Model could not be loaded. Please check the Model folder."
    )

    st.stop()


# ============================================================
# SYMPTOM SELECTION
# ============================================================

st.html("""
<div class="analysis-card">

    <div class="card-title" style="
        color:#ff69c4 !important;
        font-size:24px !important;
        font-weight:800 !important;
    ">
        🩺 Select Your Symptoms
    </div>

    <div class="card-description" style="
        color:#ffffff !important;
        font-size:15px !important;
        font-weight:500 !important;
    ">
        Search and select one or more symptoms from the available
        model input features.
    </div>

</div>
""")


selected_symptoms = st.multiselect(
    "Symptoms",
    options=features,
    placeholder="Search symptoms...",
    label_visibility="collapsed"
)


# ============================================================
# SELECTED SYMPTOMS
# ============================================================

if selected_symptoms:

    selected_text = " &nbsp; ".join(
        [
            f'<span style="'
            f'background:rgba(255,105,190,0.12);'
            f'border:1px solid rgba(255,105,190,0.30);'
            f'color:#ff9bd0;'
            f'padding:5px 9px;'
            f'border-radius:20px;'
            f'font-size:9px;'
            f'display:inline-block;'
            f'margin:3px;'
            f'">{s.replace("_", " ")}</span>'
            for s in selected_symptoms
        ]
    )

    st.html(f"""
    <div style="
        margin-top:12px;
        padding:13px;
        border-radius:12px;
        background:rgba(8,38,78,0.60);
        border:1px solid rgba(70,180,255,0.16);
    ">

        <div style="
            color:#7d9abc;
            font-size:8px;
            font-weight:800;
            letter-spacing:1px;
            margin-bottom:5px;
        ">
            SELECTED SYMPTOMS
        </div>

        {selected_text}

    </div>
    """)


# ============================================================
# ANALYZE
# ============================================================

st.write("")

if st.button(
    "✦  ANALYZE SYMPTOMS",
    key="analyze_symptoms",
    type="primary"
):

    if len(selected_symptoms) == 0:

        st.warning(
            "Please select at least one symptom before analysis."
        )

    else:

        # Create input vector

        input_data = pd.DataFrame(
            0,
            index=[0],
            columns=features
        )

        for symptom in selected_symptoms:
            if symptom in input_data.columns:
                input_data.loc[0, symptom] = 1

        # Prediction

        prediction = model.predict(input_data)[0]

        # Save analysis result for the Summary section
        st.session_state.saved_prediction = prediction
        st.session_state.analysis_done = True

        probability = None
        probabilities = None

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(input_data)[0]

            classes = list(model.classes_)

            prediction_index = classes.index(prediction)

            probability = float(
                probabilities[prediction_index] * 100
            )

        # ====================================================
        # RESULT
        # ====================================================

        if probability is not None:

            st.html(f"""
            <div class="result-card">

                <div class="result-label">
                    PREDICTED CONDITION
                </div>

                <div class="result-disease">
                    {str(prediction).replace("_", " ")}
                </div>

                <div class="probability">
                    {probability:.2f}%
                </div>

                <div style="
                    color:#7694b7;
                    font-size:8px;
                    margin-top:2px;
                ">
                    Model prediction probability
                </div>

            </div>
            """)

        else:

            st.html(f"""
            <div class="result-card">

                <div class="result-label">
                    PREDICTED CONDITION
                </div>

                <div class="result-disease">
                    {str(prediction).replace("_", " ")}
                </div>

            </div>
            """)


        # ====================================================
        # TOP 3
        # ====================================================

        if probabilities is not None:

            classes = list(model.classes_)

            ranked = sorted(
                zip(classes, probabilities),
                key=lambda x: x[1],
                reverse=True
            )[:3]

            st.html("""
            <div style="
                margin-top:25px;
                color:white;
                font-size:16px;
                font-weight:850;
            ">
                <span style="color:#4bc8ff;">│</span>
                Top Possible Predictions
            </div>
            """)

            for disease, prob in ranked:

                percent = float(prob * 100)

                st.html(f"""
                <div class="prediction-card">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                    ">

                        <div class="prediction-name">
                            {str(disease).replace("_", " ")}
                        </div>

                        <div class="prediction-percent">
                            {percent:.2f}%
                        </div>

                    </div>

                    <div class="bar-bg">

                        <div
                            class="bar-fill"
                            style="width:{min(percent,100):.2f}%;">
                        </div>

                    </div>

                </div>
                """)


# ============================================================
# SUMMARY
# ============================================================

if not st.session_state.analysis_done:

    st.html("""
    <div class="summary-card">

        <div class="summary-title">
            📋 Analysis Summary
        </div>

        <div class="summary-text">
            The selected symptom pattern will be processed through the
            trained machine-learning model to identify the most relevant
            disease class. Select symptoms and click Analyze Symptoms to
            generate the prediction.
        </div>

    </div>
    """)

else:

    predicted_name = str(
        st.session_state.saved_prediction
    ).replace("_", " ")

    st.html(f"""
    <div class="summary-card">

        <div class="summary-title">
            📋 Analysis Summary
        </div>

        <div class="summary-text">

            <b style="color:#ff91c8;">Predicted Disease:</b>
            {predicted_name}

            <br><br>

            <b style="color:#ff91c8;">Symptom Insight:</b>
            The selected symptoms show a pattern associated with
            {predicted_name} in the training dataset.

        </div>

    </div>
    """)

# ============================================================
# DISCLAIMER
# ============================================================

st.html("""
<div class="disclaimer">
    ⚠️ &nbsp;
    Educational decision-support prototype only.
    The prediction is not a medical diagnosis and should not
    replace advice from a qualified healthcare professional.
</div>
""")

st.markdown('\n<style>\n\n/* =========================================================\n   DIAGNOSIS PAGE — MATCH HOME + MODEL INSIGHTS UI\n   ========================================================= */\n\n/* ---------- MAIN BACKGROUND ---------- */\n\n[data-testid="stAppViewContainer"] {\n    background:\n        radial-gradient(\n            circle at 85% 10%,\n            rgba(150,80,255,0.18),\n            transparent 30%\n        ),\n        linear-gradient(\n            135deg,\n            #061936 0%,\n            #071f48 48%,\n            #17154b 100%\n        ) !important;\n}\n\n[data-testid="stMain"] {\n    background: transparent !important;\n}\n\n.block-container {\n    padding-top: 2rem !important;\n}\n\n\n/* ---------- SIDEBAR ---------- */\n\nsection[data-testid="stSidebar"] {\n    background:\n        linear-gradient(\n            180deg,\n            #202330 0%,\n            #20222d 55%,\n            #1d1f29 100%\n        ) !important;\n}\n\nsection[data-testid="stSidebar"] > div {\n    background: transparent !important;\n}\n\n\n/* ---------- SIDEBAR BRAND ---------- */\n\nsection[data-testid="stSidebar"] .brand,\nsection[data-testid="stSidebar"] .sidebar-brand {\n    color: #ffffff !important;\n}\n\nsection[data-testid="stSidebar"] .brand span,\nsection[data-testid="stSidebar"] .sidebar-brand span {\n    color: #55d9ff !important;\n}\n\n\n/* ---------- SIDEBAR NAV BUTTONS ---------- */\n\nsection[data-testid="stSidebar"]\ndiv.stButton > button {\n\n    background: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    background-image: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    color: #ffffff !important;\n    border: 1px solid rgba(255,255,255,0.35) !important;\n    border-radius: 12px !important;\n    min-height: 44px !important;\n\n    font-weight: 700 !important;\n\n    box-shadow:\n        0 7px 20px rgba(85,217,255,0.20),\n        0 7px 20px rgba(255,105,196,0.20) !important;\n}\n\nsection[data-testid="stSidebar"]\ndiv.stButton > button:hover {\n\n    background: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n\n    transform: translateY(-1px) !important;\n}\n\nsection[data-testid="stSidebar"]\ndiv.stButton > button * {\n    color: #ffffff !important;\n}\n\n\n/* ---------- TOP NAVIGATION ---------- */\n\ndiv.stButton > button {\n\n    border-radius: 12px !important;\n    font-weight: 700 !important;\n}\n\n\n/* ---------- PAGE LINKS ---------- */\n\na[data-testid="stPageLink-NavLink"] {\n\n    border-radius: 12px !important;\n    font-weight: 700 !important;\n}\n\n\n/* ---------- DIAGNOSIS MAIN CARDS ---------- */\n\n.symptom-card,\n.summary-card,\n.result-card,\n.prediction-card,\n.top3-card,\n.analysis-card {\n\n    background:\n        linear-gradient(\n            135deg,\n            rgba(20,66,130,0.94),\n            rgba(20,45,100,0.92)\n        ) !important;\n\n    border: 1px solid rgba(85,217,255,0.30) !important;\n\n    border-radius: 22px !important;\n\n    box-shadow:\n        0 10px 30px rgba(0,0,0,0.25),\n        0 0 25px rgba(85,217,255,0.08) !important;\n}\n\n\n/* ---------- CARD HEADINGS ---------- */\n\n.symptom-card h1,\n.symptom-card h2,\n.symptom-card h3,\n.summary-card h1,\n.summary-card h2,\n.summary-card h3,\n.result-card h1,\n.result-card h2,\n.result-card h3 {\n\n    color: #ffffff !important;\n}\n\n\n/* ---------- PINK ACCENT ---------- */\n\n.summary-title,\n.result-title,\n.prediction-title {\n\n    color: #ff91c8 !important;\n}\n\n\n/* ---------- INPUT / MULTISELECT ---------- */\n\ndiv[data-baseweb="select"] > div {\n\n    background: rgba(8,30,70,0.90) !important;\n\n    border: 1px solid rgba(85,217,255,0.38) !important;\n\n    border-radius: 12px !important;\n}\n\ndiv[data-baseweb="select"] span {\n    color: #ffffff !important;\n}\n\n\n/* ---------- SELECTED SYMPTOM CHIPS ---------- */\n\ndiv[data-baseweb="tag"] {\n\n    background: linear-gradient(\n        135deg,\n        #9b6cff,\n        #ff69c4\n    ) !important;\n\n    border: none !important;\n    border-radius: 8px !important;\n}\n\ndiv[data-baseweb="tag"] span {\n    color: #ffffff !important;\n}\n\n\n/* ---------- ANALYZE BUTTON ---------- */\n\ndiv.stButton > button {\n\n    background: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    background-image: linear-gradient(\n        135deg,\n        #55d9ff 0%,\n        #9b6cff 50%,\n        #ff69c4 100%\n    ) !important;\n\n    color: #ffffff !important;\n\n    border: 1px solid rgba(255,255,255,0.35) !important;\n\n    border-radius: 12px !important;\n\n    font-weight: 700 !important;\n\n    box-shadow:\n        0 8px 24px rgba(85,217,255,0.20),\n        0 8px 24px rgba(255,105,196,0.20) !important;\n}\n\ndiv.stButton > button:hover {\n\n    background: linear-gradient(\n        135deg,\n        #6de0ff 0%,\n        #aa7aff 50%,\n        #ff7bca 100%\n    ) !important;\n\n    transform: translateY(-1px) !important;\n}\n\n\n/* ---------- GENERAL TEXT ---------- */\n\n[data-testid="stMarkdownContainer"] p {\n    color: #a9c7ed;\n}\n\n\n/* ---------- DISCLAIMER ---------- */\n\n.disclaimer,\n.warning-card {\n\n    background: rgba(255,105,196,0.08) !important;\n\n    border: 1px solid rgba(255,145,200,0.25) !important;\n\n    border-radius: 14px !important;\n\n}\n\n\n/* ---------- SCROLLBAR ---------- */\n\n::-webkit-scrollbar {\n    width: 7px;\n}\n\n::-webkit-scrollbar-track {\n    background: #111522;\n}\n\n::-webkit-scrollbar-thumb {\n    background: linear-gradient(\n        #55d9ff,\n        #9b6cff,\n        #ff69c4\n    );\n    border-radius: 10px;\n}\n\n</style>\n', unsafe_allow_html=True)

st.markdown('\n<style>\n\n/* =========================================================\n   DIAGNOSIS BUTTON TEXT — CLEAR WHITE\n   ========================================================= */\n\n/* All Streamlit buttons */\ndiv.stButton > button,\ndiv.stButton > button p,\ndiv.stButton > button span,\ndiv.stButton > button div {\n\n    color: #ffffff !important;\n    opacity: 1 !important;\n    font-weight: 700 !important;\n    text-shadow: 0 1px 2px rgba(0,0,0,0.20) !important;\n}\n\n\n/* Top Home / Model Insights page links */\na[data-testid="stPageLink-NavLink"],\na[data-testid="stPageLink-NavLink"] span,\na[data-testid="stPageLink-NavLink"] p,\na[data-testid="stPageLink-NavLink"] div {\n\n    color: #ffffff !important;\n    opacity: 1 !important;\n    font-weight: 700 !important;\n    text-shadow: 0 1px 2px rgba(0,0,0,0.20) !important;\n}\n\n\n/* Sidebar navigation buttons */\nsection[data-testid="stSidebar"] div.stButton > button,\nsection[data-testid="stSidebar"] div.stButton > button p,\nsection[data-testid="stSidebar"] div.stButton > button span,\nsection[data-testid="stSidebar"] div.stButton > button div {\n\n    color: #ffffff !important;\n    opacity: 1 !important;\n    font-weight: 700 !important;\n    text-shadow: 0 1px 2px rgba(0,0,0,0.25) !important;\n}\n\n\n/* Analyze Symptoms button */\nbutton[kind="primary"],\nbutton[kind="primary"] p,\nbutton[kind="primary"] span,\nbutton[kind="primary"] div {\n\n    color: #ffffff !important;\n    opacity: 1 !important;\n    font-weight: 700 !important;\n    text-shadow: 0 1px 2px rgba(0,0,0,0.25) !important;\n}\n\n\n/* Hover — keep text white */\ndiv.stButton > button:hover,\ndiv.stButton > button:hover p,\ndiv.stButton > button:hover span,\na[data-testid="stPageLink-NavLink"]:hover,\na[data-testid="stPageLink-NavLink"]:hover span {\n\n    color: #ffffff !important;\n    opacity: 1 !important;\n}\n\n\n/* Make icons/text equally visible */\ndiv.stButton > button svg,\na[data-testid="stPageLink-NavLink"] svg {\n\n    opacity: 1 !important;\n}\n\n</style>\n', unsafe_allow_html=True)

st.markdown('\n<style>\n\n/* =========================================================\n   DIAGNOSIS SIDEBAR — TEXT SIZE & VISIBILITY\n   ========================================================= */\n\n/* Project title: SMART MEDICAL */\nsection[data-testid="stSidebar"] .brand,\nsection[data-testid="stSidebar"] .sidebar-brand,\nsection[data-testid="stSidebar"] .brand-title {\n\n    font-size: 22px !important;\n    line-height: 1.25 !important;\n    font-weight: 800 !important;\n    color: #ffffff !important;\n    letter-spacing: 0.2px !important;\n}\n\n\n/* MEDICAL word / colored part */\nsection[data-testid="stSidebar"] .brand span,\nsection[data-testid="stSidebar"] .sidebar-brand span,\nsection[data-testid="stSidebar"] .brand-title span {\n\n    font-size: 22px !important;\n    font-weight: 800 !important;\n    color: #55d9ff !important;\n}\n\n\n/* AI HEALTHCARE / DIAGNOSIS SYSTEM subtitle */\nsection[data-testid="stSidebar"] .brand-subtitle,\nsection[data-testid="stSidebar"] .sidebar-subtitle,\nsection[data-testid="stSidebar"] .subtitle {\n\n    font-size: 13px !important;\n    font-weight: 800 !important;\n    letter-spacing: 3px !important;\n    color: #55d9ff !important;\n}\n\n\n/* NAVIGATION heading */\nsection[data-testid="stSidebar"] .nav-label,\nsection[data-testid="stSidebar"] .navigation-label {\n\n    font-size: 14px !important;\n    font-weight: 800 !important;\n    letter-spacing: 3px !important;\n    color: #55d9ff !important;\n    margin-top: 10px !important;\n    margin-bottom: 18px !important;\n}\n\n\n/* If navigation heading is plain markdown text */\nsection[data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] {\n\n    color: #ffffff;\n}\n\n\n/* Sidebar button text — readable size */\nsection[data-testid="stSidebar"]\ndiv.stButton > button {\n\n    font-size: 16px !important;\n    min-height: 46px !important;\n}\n\n\n/* Sidebar button inner text */\nsection[data-testid="stSidebar"]\ndiv.stButton > button p,\nsection[data-testid="stSidebar"]\ndiv.stButton > button span {\n\n    font-size: 16px !important;\n    font-weight: 700 !important;\n    color: #ffffff !important;\n}\n\n\n/* Sidebar spacing */\nsection[data-testid="stSidebar"] div.stButton {\n    margin-bottom: 10px !important;\n}\n\n</style>\n', unsafe_allow_html=True)

st.html('\n<style>\n/* Select Your Symptoms — PINK HEADING */\n\n/* Select Your Symptoms heading */\n.select-symptoms-title {\n    color: #ff69c4 !important;\n    font-size: 24px !important;\n    font-weight: 800 !important;\n}\n\n\n/* Stethoscope icon */\n.select-symptoms-icon {\n    color: #c2185b !important;\n    font-size: 28px !important;\n    filter: brightness(0.75) saturate(1.5) !important;\n}\n\n</style>\n')
