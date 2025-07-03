import streamlit as st 



reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
dashboard_page = st.Page("./pgs/dashboard.py", title="dashboard", icon=":material/dashboard:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")



pg = st.navigation([reg_page, signin_page, dashboard_page, home_page, chatbot_page])

st.set_page_config(
    page_title="RxEye",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': 
        
        """
        RxEye is an innovative AI-powered health-tech system designed to empower users with instant, 
        intelligent insights about medications simply by scanning an image of the drug or its packaging.

        Whether you're a patient, pharmacist, or healthcare provider, RxEye helps you identify medicines, 
        understand their uses, check for interactions, and stay informed about safety — all in real-time.
        """
    }
)

pg.run()



