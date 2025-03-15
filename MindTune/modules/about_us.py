import streamlit as st

def show_about_us():
    st.markdown(
        """
        <style>
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