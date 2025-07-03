
from __future__ import annotations

import streamlit as st 
from datetime import datetime, timedelta
from PIL import Image
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium

import folium
import overpy
import sys



sys.path.insert(1, './modules')
print(sys.path.insert(1, '../modules/'))

from func import get_medical_info, send_drug_reminder, plot_health_facilities


from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; margin-top: -90px; color: #007B8A;">RxEye 💊</h1>
            <p style="text-align: center;">Your digital eye for safe medication use.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image('https://wellness.mcmaster.ca/app/uploads/2022/05/Green-Minimal-Modern-News-Instagram-Post-1920-x-1080-px-3-1024x576.png', width=900)



tab1, tab2, tab3, tab4 = st.tabs(["📖 Smart Dose", "Rx Vision Lens", "💊 Dr. Query", "Rx Locator"])

with tab1:
    st.markdown(
        """
        <div class="overview">
            <h2 style="text-align: center; color: #007B8A;">Welcome to RxEye</h2>
            <p style="text-align: center;">Your digital eye for safe medication use.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="overview-content">
            <p>RxEye is designed to help you manage your health and medication safely and effectively. 
            Whether you're looking for information on medications, tracking your health data, or getting personalized recommendations, 
            RxEye is here to assist you.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("med_form"):
    # Row 1: Patient Info
        col1, col2, col3 = st.columns(3)
        with col1:
            name = st.text_input("Full Name")
        with col2:
            age = st.number_input("Age", min_value=0, max_value=120)
        with col3:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        # Row 2: Symptoms & History
        col4, col5 = st.columns([1, 2])
        with col4:
            temperature = st.number_input("Body Temperature (°C)", min_value=30.0, max_value=45.0, step=0.1)
            bp = st.text_input("Blood Pressure (e.g., 120/80)")
            allergies = st.text_area("Known Allergies", placeholder="Penicillin, Peanuts...")
        with col5:
            symptoms = st.text_area("Describe Symptoms", height=150)
            history = st.text_area("Medical History", height=150)

        # Row 3: Medication Context
        col6, col7, col8 = st.columns(3)
        with col6:
            pregnancy_status = st.selectbox("Pregnancy (if applicable)", ["N/A", "Yes", "No"])
        with col7:
            current_medications = st.text_area("Current Medications", height=100)
        with col8:
            chronic_conditions = st.text_area("Chronic Conditions", height=100)

        # Submit
        submitted = st.form_submit_button("🔍 Get Recommendation", type="primary", use_container_width=True)

    if submitted:
        st.success(f"Thank you {name}! Generating your recommendation...")
        # Simulated output (replace with actual logic or ML model)
        st.markdown("### 💊 Recommended Action:")
        st.info("Based on the inputs provided, consider **Paracetamol 500mg** every 6 hours for fever. Please consult a licensed physician for a full diagnosis.")


    set_reminder = st.toggle("🔔 Reminder", value=False, help="Enable to set a reminder for your medication schedule.")

    if set_reminder:
        st.markdown("#### 🕑 Drug Reminder Details")

        with st.form("reminder_form"):
            col1, col2, col3 = st.columns(3)
            
            with col1: 
                patients_name = st.text_input('Patients Name', placeholder="e.g john Doe")
                drug_name = st.text_input("Drug Name", placeholder="e.g., Amoxicillin")
                frequency = st.selectbox("Frequency", ["Once Daily", "Twice Daily", "Every 8 hours", "Weekly", "As Needed"])

            
            with col2:
                sex = st.selectbox('Sex', options=["Male", "Female"])
                drug_type = st.selectbox("Drug Type", ["Tablet", "Capsule", "Injection", "Syrup", "Topical", "Other"])
                
                col21, col22 = st.columns(2)

                with col21:
                    start_date = st.date_input("Start Date", value=None)

                with col22: #datetime.now().time()
                    start_time = st.time_input("Start Time", value=None)


            with col3:
                col33, col34 = st.columns([2, 4])

                with col33:
                    age = st.number_input('Age', value=None, min_value=1, max_value=100)
                
                with col34:
                    phone_number = st.text_input("Phone Number", placeholder="e.g., +254712345678")
                dosage = st.text_input("Dosage", placeholder="e.g., 500mg")

                col31, col32 = st.columns(2)

                with col31:
                    end_date = st.date_input("End Date", value=datetime.today())

                with col32:
                    end_time = st.time_input("End Time", value=datetime.now().time())
                  

            additional_notes = st.text_area("Additional Notes", placeholder="e.g., Take after meals, avoid alcohol...")

            submitted = st.form_submit_button("📥 Set Reminder", type="primary", use_container_width=True)
            if submitted:
                send_drug_reminder(phone_number, start_time, drug_name)
                st.success(f"⏰ Reminder Sent Successfully")
                st.info(f"💡 Frequency: {frequency} | Type: {drug_type} | Dosage: {dosage}")
                
                if additional_notes:
                    st.warning(f"📝 Notes: {additional_notes}")


with tab2:
    st.markdown(
        """
        <div class="overview">
            <h2 style="text-align: center; color: #007B8A;">Rx Vision Lens</h2>
            <p style="text-align: center;">Your digital eye for safe medication use.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="overview-content">
            <p>RxEye is designed to help you manage your health and medication safely and effectively. 
            Whether you're looking for information on medications, tracking your health data, or getting personalized recommendations, 
            RxEye is here to assist you.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader("Upload an image of your medication", type=["jpg", "jpeg", "png"], label_visibility="collapsed", help="Upload a clear image or document of your medication label or packaging. Supported formats: JPG, JPEG, PNG, PDF.") 
    query = st.text_input("Enter your query about the medication", placeholder="e.g., What is this medication for? How should I take it?", label_visibility="collapsed", help="Type your question about the medication. Be specific to get the best results.")
    submit_file = st.button('🔍 Analyze Image/Doc', use_container_width=True, type="primary")

    if submit_file and uploaded_file is not None and query is not None:
        processed_file = Image.open(uploaded_file)
        response = get_medical_info(processed_file, query)

        col1, col2 = st.columns(2)
        with col1:
            # st.markdown("### 📄 Medication Information")
            st.image(processed_file, caption="Uploaded Medication Image", use_container_width=True)

        with col2:
            # st.markdown("### 📝 Query Response")
            if response:
                st.info(response)
            else:
                st.warning("No response available. Please try again with a different image or query.")

with tab3:
    pass


with tab4:
    st.markdown(
        """
        <div class="overview">
            <h2 style="text-align: center; color: #007B8A;">Rx Locator</h2>
            <p style="text-align: center;">Your digital eye for safe medication use.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown(
        """
        <div class="overview-content">
            <p>RxEye is designed to help you manage your health and medication safely and effectively. 
            Whether you're looking for information on medications, tracking your health data, or getting personalized recommendations, 
            RxEye is here to assist you.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    location = st.text_input("Enter your location", placeholder="e.g., New York, NY", label_visibility="collapsed", help="Type your current location to find nearby pharmacies or healthcare providers.")
    search_radius = st.slider("Search Radius (km)", min_value=1, max_value=50, value=10, step=1, label_visibility="collapsed", help="Adjust the radius to search for pharmacies or healthcare providers within a specific distance from your location.")
    search_button = st.button('🔍 Search', use_container_width=True, type="primary")

    # if search_button:
    #     map_display = plot_health_facilities(location, search_radius)
    #     st_folium(map_display, width=700) 



    latitude, longitude = -1.2921, 36.8219
    radius = 3000  # meters

    # Overpass API query
    api = overpy.Overpass()
    query = f"""
    (
    node["amenity"~"clinic|hospital|pharmacy|doctors|dispensary"](around:{radius},{latitude},{longitude});
    node["healthcare"](around:{radius},{latitude},{longitude});
    node["shop"="medical_supply"](around:{radius},{latitude},{longitude});
    );
    out center;
    """

    # Fetch data
    try:
        result = api.query(query)
    except Exception as e:
        st.error(f"Error fetching data from Overpass API: {e}")
        st.stop()

    # Create Folium map
    m = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker([latitude, longitude], tooltip="Center: Nairobi").add_to(m)

    # Add nodes to map
    for node in result.nodes:
        name = node.tags.get("name", "Unnamed Facility")
        type_ = node.tags.get("amenity", node.tags.get("shop", node.tags.get("healthcare", "Facility")))
        popup = f"<b>{name}</b><br>Type: {type_.title()}"
        folium.Marker(
            location=[node.lat, node.lon],
            popup=popup,
            icon=folium.Icon(color="red", icon="plus-sign")
        ).add_to(m)

    # Display in Streamlit
    st_folium(m, width=1200, height=400)