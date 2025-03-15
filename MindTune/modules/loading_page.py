import streamlit as st

def show_loading_page():
    st.markdown("<h1 style='text-align: center;'>⏳ Preparing EEG Analysis...</h1>", unsafe_allow_html=True)
    st.write("Please calibrate your headset to begin the analysis. Once it's calibrated, press Start Analysis")

    if st.button("Start Analysis"):
        st.session_state["page"] = "analyze"