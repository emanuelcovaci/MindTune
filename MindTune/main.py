import base64

from modules.analyze import show_analyze
from modules.home import show_home
from modules.loading_page import show_loading_page
from modules.result_analyze import show_result_analyze
from modules.state_detection import show_state_detection
from modules.about_us import show_about_us
from modules.questionnaire import questionnaire

import streamlit as st

if 'prediction' not in st.session_state:
    st.session_state.prediction = -1

st.markdown(
    """
    <style>
    
    body, html {
        overflow: hidden !important;
    }
    
    [data-testid="stSidebar"] {
        overflow: hidden !important;
    }
    
    .stApp {
        background-color: black !important;
        color: white !important;
    }

    div[data-testid="stAppViewContainer"] h1 {
        color: white !important;
    }

    .css-1d391kg, .css-1d391kg * {
        background-color: black !important;
        color: white !important;
    }

    .speech-bubble-left {
        background-color: #f0f0f0;
        border-radius: 15px;
        padding: 10px 15px;
        font-size: 16px;
        max-width: 80%;
        color: black;
        position: relative;
        display: inline-block;
    }
    .speech-bubble-left::after {
        content: '';
        position: absolute;
        left: -10px;
        top: 15px;
        border-width: 10px;
        border-style: solid;
        border-color: transparent #f0f0f0 transparent transparent;
    }
    .speech-bubble-right {
        background-color: #e0eaff;
        border-radius: 15px;
        padding: 10px 15px;
        font-size: 16px;
        max-width: 80%;
        color: black;
        position: relative;
        display: inline-block;
    }
    .speech-bubble-right::after {
        content: '';
        position: absolute;
        right: -10px;
        top: 15px;
        border-width: 10px;
        border-style: solid;
        border-color: transparent transparent transparent #e0eaff;
    }

    .user-input-bubble {
        background-color: #cce5ff;
        border-radius: 15px;
        padding: 10px 15px;
        font-size: 16px;
        max-width: 60%;
        color: black;
        display: inline-block;
        margin-top: 10px;
        border: 1px solid #99ccff;
        position: relative;
        float: right;
        text-align: right;
    }
    .user-input-bubble::before {
        content: '';
        position: absolute;
        right: -10px;
        top: 15px;
        border-width: 10px;
        border-style: solid;
        border-color: transparent transparent transparent #cce5ff;
    }

    .custom-input-container {
        background-color: #cce5ff;
        border: 1px solid #99ccff;
        border-radius: 15px;
        padding: 10px;
        max-width: 60%;
        margin-top: 10px;
        text-align: right;
        float: right;
    }
    .custom-input-container input[type="text"] {
        border: none;
        background-color: #cce5ff;
        color: black;
        padding: 8px;
        border-radius: 10px;
        width: 90%;
        text-align: right;
    }
    
    .stButton>button {
        width: 100%;
        text-align: left;
        background-color: transparent; 
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px;
        font-size: 16px;
        font-weight: normal;
    }
    .stButton>button:hover {
        background-color: #89CFF0; 
        color: white;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
        """
        <style>
        div.stButton > button {
            border: 2px solid #5FA8D3 !important;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            transition: 0.3s ease-in-out;
        }

        div.stButton > button:after {
            content: attr(data-text);
            display: inline-block;
            visibility: hidden;
            height: 0;
        }
        
        .sidebar-image-container {
        background-color: #261741;
        bottom: 1000px; 
        text-align: center;
        }
        

    .sidebar-image-container img {
        width: 40%;
        border-radius: 5px;
    }
        
        [data-testid="stSidebar"] {
        background: #000000 !important; 
        padding-top: 20px;
        padding-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

background_image_path = "media/background.jpg"

with open(background_image_path, "rb") as img_file:
    background_image_base64 = base64.b64encode(img_file.read()).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("data:image/jpg;base64,{background_image_base64}") no-repeat center center fixed;
        background-size: cover;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

st.session_state.previous_page = st.session_state.page
image_path = "media/itfest.jpg"

st.sidebar.markdown("<h1 style='text-align: center;'>🌠 Navigation</h1>", unsafe_allow_html=True)
if st.sidebar.button("🛸 NeuroSurvey"):
    st.session_state.page = "home"
if st.sidebar.button("🔬 State Detection"):
    st.session_state.page = "state_detection"
if st.sidebar.button("👨‍💻 About Us"):
    st.session_state.page = "about_us"

st.sidebar.markdown(
    f"""
    <div class="sidebar-image-container">
        <img src="data:image/png;base64,{base64.b64encode(open(image_path, "rb").read()).decode()}" 
        width="350" alt="Sidebar Image">
    </div>
    """,
    unsafe_allow_html=True
)


if st.session_state["page"] == "home":
    show_home()
elif st.session_state["page"] == "state_detection":
    show_state_detection()
elif st.session_state["page"] == "about_us":
    show_about_us()
elif st.session_state["page"] == "loading_page":
    show_loading_page()
elif st.session_state["page"] == "analyze":
    show_analyze()
elif st.session_state["page"] == "result_analyze":
    show_result_analyze()
elif st.session_state["page"] == "questionnaire":
    questionnaire()