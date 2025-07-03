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


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
     
st.markdown(
    """
        <nav class="navbar fixed-bottom navbar-expand-lg navbar-dark" style="background-color: #007B8A;">
        <a class="navbar-brand" target="_blank" style="padding-left: 280px; color: white;">Rx Eye 💊</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
            <li class="nav-item"></li>
            <li class="nav-item"></li>
            <li class="nav-item"></li>
            <li class="nav-item"></li>
            <li class="nav-item active">
                <a class="nav-link" href="https://www.echominds.africa" href="#">EchoMinds Innovation<span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="https://www.github.com" target="_blank">UTS</a>
            </li>
            <li class="nav-item">
                <a class="nav-link disabled" href="#">Cli</a>
            </li>
            </ul>
        </div>
        </nav>
        """, unsafe_allow_html=True)


pg.run()



