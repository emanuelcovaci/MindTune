import base64

import streamlit as st

def show_analyze():
    video_path = "media/video.mp4"
    image_path = "media/robot.png"

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

    st.markdown("<h1 class='title'>Recording Data with EEG Headset</h1>", unsafe_allow_html=True)

    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
        video_base64 = base64.b64encode(video_bytes).decode()

    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        img_base64 = base64.b64encode(img_bytes).decode()

    video_html = f"""
        <div id="media-container">
            <video width="700" height="400" autoplay muted id="video-element">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>
        <script>
            setTimeout(function() {{
                document.getElementById('media-container').innerHTML = '<img src="data:image/png;base64,{img_base64}" width="700" height="400"/>';
            }}, 8000);
        </script>
    """

    st.markdown(video_html, unsafe_allow_html=True)

    if "read_bci" not in st.session_state:
        st.session_state["read_bci"] = 0
        # model = init_model()
        # streams = resolve_stream()
        # inlet = StreamInlet(streams[0])
        # user = record_data(inlet, 5)
        # user_raw = preporcess_data(user)
        # predicted_class = predict(model, user_raw)
        st.session_state.prediction = 1
        # print(f'ST prediction: {st.session_state.prediction}')
        st.write('Brain Waves recorded. Let\'s see the results!')

    if st.session_state.prediction > -1:
        if st.button("Run the analysis"):
            st.session_state["page"] = "result_analyze"