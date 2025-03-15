import base64

import time
from openai import OpenAI
import streamlit as st
#from predict_api import *

if 'prediction' not in st.session_state:
    st.session_state.prediction = -1

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;
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
    </style>
    """,
    unsafe_allow_html=True
)

def type_text(container, text, bubble_class, delay=0.01):
    displayed_text = ""
    for char in text:
        displayed_text += char
        container.markdown(
            f"<div class='{bubble_class}'>{displayed_text}</div>",
            unsafe_allow_html=True
        )
        time.sleep(delay)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

st.session_state.previous_page = st.session_state.page

st.sidebar.title("🌠 Navigation")
if st.sidebar.button("🛸 Home"):
    st.session_state.page = "home"
if st.sidebar.button("👽 State Detection"):
    st.session_state.page = "state_detection"
if st.sidebar.button("🧑‍🤝‍🧑 About Us"):
    st.session_state.page = "about_us"

def show_home():
    st.markdown(
        """
        <style>
        .title {
            color: #89CFF0;
            font-size: 2.5em;
            font-weight: bold;
            text-align: center;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='title'>Welcome to NeuroSurvey 🚀</h1>", unsafe_allow_html=True)

    left_container = st.empty()
    if "intro_message_displayed" not in st.session_state:
        with left_container.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.image("media/robot.png", width=130)
            with col2:
                type_text(st.empty(), "Hey, I’m glad you chose me today to guide you through your emotional journey.\n"
                                      "Think of me as your personal guide to help you better understand the emotions "
                                      "you’re feeling right now.\n"
                                      "Let’s tune in to how you’re feeling today and "
                                      "explore some tools to help you easily process those emotions. 💫",
                          "speech-bubble-left")
        st.session_state.intro_message_displayed = True
    else:
        with left_container.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.image("media/robot.png", width=130)
            with col2:
                st.markdown("<div class='speech-bubble-left'>Hey, I’m glad you chose me today to guide "
                            "you through your emotional journey.\n"
                            "Think of me as your personal guide to help you better understand the emotions "
                            "you’re feeling right now.\n"
                            "Let’s tune in to how you’re feeling today and "
                            "explore some tools to help you easily process those emotions. 💫</div>",
                            unsafe_allow_html=True)


def show_state_detection():
    st.title("🌟 Revolutionize Emotional Insights with the EEG Headset")

    st.subheader("A New Era in Understanding Emotions")
    st.write("""
    In the digital age, where understanding the human experience is paramount, the **EEG Headset** represents a revolution in capturing and interpreting emotions. Imagine the power of knowing exactly how someone feels at any given moment, capturing their state of well-being and pinpointing sources of discomfort or stress – no words needed, just brainwaves.
    """)

    st.subheader("📊 Real-Time Emotional Tracking")
    st.write("""
    **We collect and analyze EEG data** to create **personalized surveys** based on your current emotional state. Detecting stress, joy, or other emotions in real-time allows us to tailor insights directly to you.
    """)

    st.subheader("🔬 How It Works")
    st.write("""
    The **EEG headset** uses **advanced electrodes** to capture brainwave data with precision. By analyzing waves such as alpha, beta, and theta, each linked to mental states like relaxation, focus, or stress, we gain real-time insights into your mind.
    Our **AI algorithms** process this data instantly, generating a **customized survey** that helps uncover the factors affecting your emotions.
    """)

    st.subheader("🚀 Join Us in Redefining Health & Wellness")
    st.write("""
    With EEG and our expertise, you can harness a powerful tool to enhance mental and physical health, and even prevent potential crises. Our platform provides a secure, intuitive interface to monitor and understand brain activity.
    """)
    st.markdown("**Ready to experience the future of emotional insights?**")

def show_about_us():
    st.title("About Us")
    st.write("""
            👋 We are a passionate team from Timișoara, driven to explore, develop, and innovate in the fascinating world of AI. 
            🌱 From a spark of an idea to a fully-realized project, we’re committed to crafting solutions that are as close to real-world impact as possible.

            💡 Our journey is fueled by creativity, resilience, and a deep-seated curiosity to see how far we can push the boundaries of technology. 
            Each project starts with the ambition to solve complex challenges, and through teamwork and dedication, we turn those ideas into tangible, high-quality results.

            🌍 With every new project, we strive to make a meaningful difference, bridging the gap between imagination and reality. 
            We believe that AI, driven by purpose and innovation, has the power to transform lives and shape the future for the better.

            🤝 Together, we’re more than just a team—we’re a community, constantly learning and growing, ready to tackle the next big idea and bring it to life. Join us on our journey to create, innovate, and make an impact!
        """)

if st.session_state["page"] == "home":
    show_home()
elif st.session_state["page"] == "state_detection":
    show_state_detection()
elif st.session_state["page"] == "about_us":
    show_about_us()