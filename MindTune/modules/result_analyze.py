import streamlit as st
from utils import get_image_base64


def show_result_analyze():
    image_stressed_path = "media/stressed.png"
    image_relaxed_path = "media/relaxed.png"
    result = st.session_state.prediction
    print(f'Result: {result}')
    if result == 1:
        st.markdown(
            """
            <style>
            .title {
                color: white;
                font-size: 1em;
                text-align: center;
                animation: pulse 2s infinite;
            }
            
            .result {
                color: white;
                font-size: 1.5em;
                font-weight: bold;
                text-align: center;
                animation: pulse 2s infinite;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            '<p class="title">The predicted result based on the analysis of data extracted using the EEG headset is: </p>',
            unsafe_allow_html=True)
        st.markdown(
            '<p class="result">Stressed</p>',
            unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image_base64 = get_image_base64(image_stressed_path)
            if image_base64:
                st.markdown(
                    f"""
                                                        <style>
                                                        .fixed-image {{
                                                            width: 450px;
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
    elif result == 0:
        st.markdown(
            """
            <style>
            .title {
                color: white; 
                font-size: 1em;
                text-align: center;
                animation: pulse 2s infinite; 
            }
            
            .result {
                color: white;
                font-size: 1.5em;
                font-weight: bold;
                text-align: center;
                animation: pulse 2s infinite;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            '<p class="title">The predicted result based on the analysis of data extracted using the EEG headset is:</p>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="result">Relaxed</p>',
            unsafe_allow_html=True
        )

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image_base64 = get_image_base64(image_relaxed_path)
            if image_base64:
                st.markdown(
                    f"""
                                                                    <style>
                                                                    .fixed-image {{
                                                                        width: 450px;
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

    st.markdown(
        """
        <style>
        /* Default button styling */
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
        </style>
        """,
        unsafe_allow_html=True
    )

    button_clicked = st.button("📊 Let's start a survey")
    if button_clicked:
            st.session_state["page"] = "questionnaire"
