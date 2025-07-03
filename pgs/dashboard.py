import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, timedelta
import random

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

def generate_dummy_data(days=7):
    dates = [datetime.now() - timedelta(days=i) for i in range(days)][::-1]
    bp_systolic = [random.randint(110, 135) for _ in range(days)]
    bp_diastolic = [random.randint(70, 90) for _ in range(days)]
    heart_rate = [random.randint(60, 100) for _ in range(days)]
    return dates, bp_systolic, bp_diastolic, heart_rate

# Generate Data
dates, systolic, diastolic, heart_rate = generate_dummy_data()



def generate_dummy_vitals(days=7):
    dates = [datetime.now() - timedelta(days=i) for i in range(days)][::-1]
    systolic = [random.randint(110, 135) for _ in range(days)]
    diastolic = [random.randint(70, 90) for _ in range(days)]
    heart_rate = [random.randint(60, 100) for _ in range(days)]
    weight = [round(random.uniform(60.0, 75.0), 1) for _ in range(days)]
    bmi = [round(w / ((1.7)**2), 1) for w in weight]  # Assuming constant height
    return dates, systolic, diastolic, heart_rate, weight, bmi

# Get dummy data
dates_b, systolic_b, diastolic_b, heart_rate_b, weight, bmi = generate_dummy_vitals()


# SECTION 1: Personal Profile
st.subheader("👤 Personal Profile")
with st.container():
    col1, col2, col3, col4 = st.columns(4)
    col1.info("**Name:** Jane Doe")
    col1.info("**Height:** ")
    col2.info("**Age:** 32")
    col2.info("**Weight:** 65 kg")
    col3.info("**Gender:** Female")
    col3.info("**BMI Status:** Normal")
    col4.info("**Blood Type:** O+")
    col4.info("**BMI:** 22.5")


with st.container():
    col5, col6 = st.columns(2)
    with col5:
        fig_bp = go.Figure()
        fig_bp.add_trace(go.Scatter(x=dates, y=systolic, mode='lines+markers', name='Systolic',
                                    line=dict(color='crimson')))
        fig_bp.add_trace(go.Scatter(x=dates, y=diastolic, mode='lines+markers', name='Diastolic',
                                    line=dict(color='darkblue')))
        fig_bp.update_layout(
            title="Blood Pressure Over Time",
            xaxis_title="Date",
            yaxis_title="Pressure (mmHg)",
            template="plotly_white"
        )
        st.plotly_chart(fig_bp, use_container_width=True)


    with col6:
        fig_hr = go.Figure()
        fig_hr.add_trace(go.Bar(x=dates, y=heart_rate, marker_color='mediumseagreen', name="Heart Rate"))
        fig_hr.update_layout(
            title="Heart Rate Over Time",
            xaxis_title="Date",
            yaxis_title="Beats Per Minute (bpm)",
            template="plotly_white"
        )
        st.plotly_chart(fig_hr, use_container_width=True)

# SECTION 2: Physical Attributes
# st.subheader("📏 Physical Attributes")
# with st.container():
#     col1, col2, col3, col4 = st.columns(4, border=True)
#     col1.metric(label="Height", value="165 cm")
#     col2.metric(label="Weight", value="60 kg")
#     col3.metric(label="BMI", value="22.0", delta="Normal")
#     col4.metric(label="BMI Status", value="✅ Healthy")

# SECTION 3: Vital Signs
st.subheader("💓 Vital Signs")
with st.container():
    col1, col2, col3 = st.columns(3)
    col1.warning("**Blood Pressure:** \n118/76 mmHg.")
    col2.warning("**Heart Rate:** \n72 bmp.")
    col3.warning("**Temperature:** \n36.7 °C")
    

with st.container():
    col4, col5, col6 = st.columns(3)
    col4.metric(label="Blood Glucose", value="92 mg/dL", delta="Normal")
    col5.metric(label="Cholesterol", value="170 mg/dL", delta="Optimal")
    col6.metric(label="Oxygen Saturation", value="98%", delta="-102%")

# SECTION 4: Physical Traits
st.subheader("👤 Physical Traits")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Skin Color:** Medium")
        st.success("**Hair Color:** Black")
    with col2:
        st.success("**Eye Color:** Brown")
        st.success("**Body Frame:** Slim")


# Row 2: Weight & BMI
col7, col8 = st.columns(2)

with col7:
    fig_weight = go.Figure()
    fig_weight.add_trace(go.Scatter(
        x=dates_b, y=weight, fill='tozeroy', mode='lines', name='Weight',
        line=dict(color='orange', shape='spline')
    ))
    fig_weight.update_layout(title="Weight Trend", xaxis_title="Date", yaxis_title="kg", template="plotly_white")
    st.plotly_chart(fig_weight, use_container_width=True)

with col8:

    # BMI Classification (based on last BMI value)
    latest_bmi = bmi[-1]
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    values = [0, 0, 0, 0]
    if latest_bmi < 18.5:
        values[0] = 1
    elif 18.5 <= latest_bmi < 25:
        values[1] = 1
    elif 25 <= latest_bmi < 30:
        values[2] = 1
    else:
        values[3] = 1

    fig_bmi = go.Figure(data=[go.Pie(
        labels=categories,
        values=values,
        hole=0.5,
        marker_colors=["#6495ED", "#3CB371", "#FFA500", "#FF4500"],
        textinfo='label+percent'
    )])
    fig_bmi.update_layout(title=f"BMI Status: {latest_bmi}", template="plotly_white")
    st.plotly_chart(fig_bmi, use_container_width=True)


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
