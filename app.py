import streamlit as st 
from st_social_media_links import SocialMediaIcons
from streamlit.components.v1 import html



reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
dashboard_page = st.Page("./pgs/dashboard.py", title="dashboard", icon=":material/dashboard:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")







with st.sidebar:
    button = """
        <script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="echominds" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>
        """

    html(button, height=70, width=220)
    st.markdown(
        """
        <style>
            iframe[width="220"] {
                position: fixed;
                bottom: 60px;
                right: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


    social_media_links = [
        "https://www.x.com/am_tonie",
        "https://www.youtube.com/@echobytes-ke",
        "https://www.instagram.com/antonie_generall",
        "https://www.github.com/antonie-riziki",
    ]

    social_media_icons = SocialMediaIcons(social_media_links)

    social_media_icons.render()

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



