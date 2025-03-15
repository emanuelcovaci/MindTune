import streamlit as st

from utils import get_image_base64, type_text


def show_home():
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
    image_path = "media/robot.png"

    if "intro_message_displayed" not in st.session_state:
        with left_container.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                image_base64 = get_image_base64(image_path)
                if image_base64:
                    st.markdown(
                        f"""
                        <style>
                        .fixed-image {{
                            width: 130px;
                            height: auto;
                            display: block;
                            pointer-events: none;
                            user-drag: none;
                            -webkit-user-drag: none;
                        }}
                        </style>
                        <img src="data:image/png;base64,{image_base64}" class="fixed-image">
                        """,
                        unsafe_allow_html=True
                    )
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
                image_base64 = get_image_base64(image_path)
                if image_base64:
                    st.markdown(
                        f"""
                                        <style>
                                        .fixed-image {{
                                            width: 130px;
                                            height: auto;
                                            display: block;
                                            pointer-events: none;
                                            user-drag: none;
                                            -webkit-user-drag: none;
                                        }}
                                        </style>
                                        <img src="data:image/png;base64,{image_base64}" class="fixed-image">
                                        """,
                        unsafe_allow_html=True
                    )
            with col2:
                st.markdown("<div class='speech-bubble-left'>Hey, I’m glad you chose me today to guide "
                            "you through your emotional journey.\n"
                            "Think of me as your personal guide to help you better understand the emotions "
                            "you’re feeling right now.\n"
                            "Let’s tune in to how you’re feeling today and "
                            "explore some tools to help you easily process those emotions. 💫</div>",
                            unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        div.stTextInput > div > input {
            background-color: #cce5ff;
            color: black;
            border: 1px solid #99ccff;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
        }
        .custom-input-container {
            background-color: #cce5ff;
            border: 1px solid #99ccff;
            border-radius: 15px;
            padding: 10px;
            max-width: 65%;
            margin-top: 10px;
            text-align: center;
            float: right;
        }

        .user-response-bubble {
            background-color: #e0eaff;
            border: 1px solid #99ccff;
            border-radius: 15px;
            padding: 10px 15px;
            color: black;
            text-align: center;
            margin-top: 10px;
            width: 85%;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # st.markdown(
    #     "<div class='user-response-bubble'>Ready to get started?</div>",
    #     unsafe_allow_html=True
    # )

    st.markdown(
        """
        <style>
        div.stRadio > div > label {
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        .centered-radio-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 0vh;
        }
        .stRadio > div {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="centered-radio-container">', unsafe_allow_html=True)
    user_response = st.radio(
        label="Choose an option:",
        options=["Yes, I'm ready", "I still need a minute"],
        index=1,
        key="user_choice",
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    if user_response == "Yes, I'm ready":
        followup_container = st.empty()
        if "response_message_displayed" not in st.session_state:
            with followup_container.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    image_base64 = get_image_base64(image_path)
                    if image_base64:
                        st.markdown(
                            f"""
                                            <style>
                                            .fixed-image {{
                                                width: 130px;
                                                height: auto;
                                                display: block;
                                                pointer-events: none;
                                                user-drag: none;
                                                -webkit-user-drag: none;
                                            }}
                                            </style>
                                            <img src="data:image/png;base64,{image_base64}" class="fixed-image">
                                            """,
                            unsafe_allow_html=True
                        )
                with col2:
                    type_text(st.empty(), "Great! Before we start I recommend you to find a comfortable place to sit. "
                                          "Maybe your sofa or an armchair.", "speech-bubble-left")
            st.session_state.response_message_displayed = True

        else:
            with followup_container.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    image_base64 = get_image_base64(image_path)
                    if image_base64:
                        st.markdown(
                            f"""
                                            <style>
                                            .fixed-image {{
                                                width: 130px;
                                                height: auto;
                                                display: block;
                                                pointer-events: none;
                                                user-drag: none;
                                                -webkit-user-drag: none;
                                            }}
                                            </style>
                                            <img src="data:image/png;base64,{image_base64}" class="fixed-image">
                                            """,
                            unsafe_allow_html=True
                        )
                with col2:
                    st.markdown("<div class='speech-bubble-left'>Great! "
                                "Before we start I recommend you to find a comfortable place to sit. "
                                "Maybe your sofa or an armchair.</div>", unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            .custom-start-button button {
                border: 2px solid #5FA8D3 !important; /* Darker Blue Border */
                color: white !important;
                background-color: transparent !important;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
                transition: 0.3s ease-in-out;
            }
            .custom-start-button button:hover {
                background-color: #5FA8D3 !important;
                color: white !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        with st.markdown('<div class="custom-start-button">', unsafe_allow_html=True):
            if st.button("Start"):
                st.session_state["page"] = "new_page"
        st.markdown('</div>', unsafe_allow_html=True)