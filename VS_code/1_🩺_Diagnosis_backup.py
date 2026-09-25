
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Diagnosis | Smart Medical Diagnosis",
    page_icon="🩺",
    layout="wide"
)

# Load model
model_path = "../Model/smart_medical_diagnosis_model.pkl"
model_package = joblib.load(model_path)

model = model_package["model"]
features = model_package["features"]

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 17px;
    margin-bottom: 35px;
}

.result-card {
    padding: 30px;
    border-radius: 20px;
    background: #f4f8ff;
    border: 1px solid #dce6f7;
    text-align: center;
    margin-top: 25px;
}

.result-disease {
    font-size: 32px;
    font-weight: 800;
    margin: 10px;
}

.probability {
    font-size: 22px;
    font-weight: 700;
}

.info-card {
    padding: 20px;
    border-radius: 16px;
    background: #fafafa;
    border: 1px solid #e5e5e5;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(
    '<div class="title">🩺 AI SYMPTOM ANALYSIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Select your symptoms and let the machine-learning model analyze the pattern.</div>',
    unsafe_allow_html=True
)

# ---------- SYMPTOM SELECTION ----------
st.subheader("🔍 Select Symptoms")

selected_symptoms = st.multiselect(
    "Search and select symptoms",
    options=features,
    placeholder="Type to search symptoms..."
)

if selected_symptoms:
    st.write("**Selected Symptoms:**")

    cols = st.columns(min(len(selected_symptoms), 4))

    for i, symptom in enumerate(selected_symptoms):
        with cols[i % len(cols)]:
            st.info(f"✓ {symptom}")

st.write("")

# ---------- PREDICT ----------
if st.button("🔬 ANALYZE SYMPTOMS", use_container_width=True):

    if not selected_symptoms:

        st.warning("⚠️ Please select at least one symptom.")

    else:

        input_data = pd.DataFrame(
            0,
            index=[0],
            columns=features
        )

        for symptom in selected_symptoms:
            input_data.loc[0, symptom] = 1

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        predicted_index = list(model.classes_).index(prediction)

        probability = probabilities[predicted_index] * 100

        # ---------- RESULT ----------
        st.markdown("""
        <div class="result-card">
        <div>🧠 AI PREDICTION</div>
        """, unsafe_allow_html=True)

        st.markdown(
            f'<div class="result-disease">{prediction}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="probability">Prediction Probability: {probability:.2f}%</div>',
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

        # ---------- TOP 3 ----------
        st.subheader("🏆 Top 3 Possible Predictions")

        top_indices = probabilities.argsort()[-3:][::-1]

        for rank, index in enumerate(top_indices, start=1):

            disease = model.classes_[index]
            prob = probabilities[index] * 100

            st.progress(
                float(prob / 100),
                text=f"{rank}. {disease} — {prob:.2f}%"
            )

        # ---------- SELECTED SYMPTOMS ----------
        st.subheader("📋 Analysis Summary")

        st.markdown(
            f"""
            <div class="info-card">
            <b>Symptoms analyzed:</b> {len(selected_symptoms)}<br><br>
            <b>Machine-learning model:</b> Logistic Regression<br><br>
            <b>Prediction:</b> {prediction}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            "⚠️ This is an educational decision-support prototype and not a substitute for professional medical advice."
        )
