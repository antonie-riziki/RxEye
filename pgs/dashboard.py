import streamlit as st

st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #007B8A;">RxEye 💊</h1>
            <p style="text-align: center;">Your digital eye for safe medication use.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# SECTION 1: Personal Profile
st.subheader("👤 Personal Profile")
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.info("**Name:** Jane Doe")
    col2.info("**Age:** 32")
    col3.info("**Gender:** Female")
    col4.info("**Blood Type:** O+")

# SECTION 2: Physical Attributes
st.subheader("📏 Physical Attributes")
with st.container():
    col1, col2, col3, col4 = st.columns(4, border=True)
    col1.metric(label="Height", value="165 cm")
    col2.metric(label="Weight", value="60 kg")
    col3.metric(label="BMI", value="22.0", delta="Normal")
    col4.metric(label="BMI Status", value="✅ Healthy")

# SECTION 3: Vital Signs
st.subheader("💓 Vital Signs")
with st.container():
    col1, col2, col3 = st.columns(3, border=True)
    col1.metric(label="Blood Pressure", value="118/76 mmHg", delta="Normal")
    col2.metric(label="Heart Rate", value="72 bpm", delta="Good")
    col3.metric(label="Temperature", value="36.7 °C", delta="Stable")

with st.container():
    col4, col5, col6 = st.columns(3)
    col4.metric(label="Blood Glucose", value="92 mg/dL", delta="Normal")
    col5.metric(label="Cholesterol", value="170 mg/dL", delta="Optimal")
    col6.metric(label="Oxygen Saturation", value="98%", delta="Normal")

# SECTION 4: Physical Traits
st.subheader("🧬 Physical Traits")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Skin Color:** Medium")
        st.success("**Hair Color:** Black")
    with col2:
        st.success("**Eye Color:** Brown")
        st.success("**Body Frame:** Slim")

# SECTION 5: Conditions & Allergies
st.subheader("⚕️ Medical Background")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.warning("**Allergies:** Penicillin, Pollen")
    with col2:
        st.warning("**Chronic Conditions:** Asthma")

# SECTION 6: Recommendation Summary
st.subheader("💊 Medical Recommendation")
st.info("Stay on regular asthma medication. Avoid exposure to allergens. Next full check-up is recommended in 3 months.")

st.markdown("---")
st.caption("RxEye | Your Smart Health Companion")
