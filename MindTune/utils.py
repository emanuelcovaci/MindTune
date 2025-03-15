import base64
import time

import streamlit as st


def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Image not found: {image_path}")
        return None

def type_text(container, text, bubble_class, delay=0.01):
    displayed_text = ""
    for char in text:
        displayed_text += char
        container.markdown(
            f"<div class='{bubble_class}'>{displayed_text}</div>",
            unsafe_allow_html=True
        )
        time.sleep(delay)