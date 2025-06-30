
from __future__ import annotations

import streamlit as st 
import sys



sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))


from dotenv import load_dotenv

load_dotenv()



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

st.image('https://wellness.mcmaster.ca/app/uploads/2022/05/Green-Minimal-Modern-News-Instagram-Post-1920-x-1080-px-3-1024x576.png', width=900)






