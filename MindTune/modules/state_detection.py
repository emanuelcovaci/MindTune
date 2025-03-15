import streamlit as st

def show_state_detection():
    st.write(
        """
        <style>
        .title { 
            font-size: 1.7em; 
            font-weight: bold; 
            text-align: center; 
            margin-bottom: 25px; 
        }
        .centered-subtitle { font-size: 1.1em; font-weight: bold; text-align: center; margin-top: 20px; }
        .text { font-size: 0.875em; line-height: 1.5; }
        .call-to-action { font-size: 1em; text-align: center; padding: 15px; }
        .divider { border-top: 1px solid #ccc; margin: 15px 0; }
        s</style>

        <div class="title">🌟 Revolutionize Emotional Insights with the EEG Headset</div>

        <div class="centered-subtitle">🧠 A New Era in Understanding Emotions</div>
        <div class="text">
            In today's digital world, where understanding human emotions is paramount, the EEG Headset 
            marks a revolution in emotion tracking. Imagine knowing how someone truly feels—detecting their state of well-being, 
            pinpointing stress, joy, or discomfort—without words, just through brainwaves.
        </div>

        <div class="divider"></div>

        <div class="centered-subtitle">📊 Real-Time Emotional Tracking</div>
        <div class="text">
            Our EEG technology continuously captures and analyzes brainwave activity to generate 
            personalized surveys tailored to your emotional state. Whether detecting stress, 
            focus, or happiness, real-time insights allow for a deeper connection with your mind.
        </div>

        <div class="divider"></div>

        <div class="centered-subtitle">🔬 How It Works</div>
        <div class="text">
            The EEG headset utilizes advanced electrodes to measure brainwave patterns, including:
            <ul>
                <li>Alpha waves → Linked to relaxation and creativity</li>
                <li>Beta waves → Associated with active thinking and focus</li>
                <li>Theta waves → Related to deep relaxation and subconscious states</li>
            </ul>
            Our AI-powered algorithms analyze these signals instantly, generating 
            customized surveys that help uncover the key factors influencing your emotions.
        </div>

        <div class="divider"></div>

        <div class="centered-subtitle">🚀 Join Us in Redefining Health & Wellness</div>
        <div class="text">
            With EEG-driven insights, you gain access to a powerful tool for enhancing mental well-being, improving 
            emotional resilience, and even preventing potential crises. Our secure and intuitive platform empowers 
            users to monitor and understand their brain activity like never before.
        </div>

        <div class="call-to-action">✨ Ready to experience the future of emotional insights? ✨</div>
        """,
        unsafe_allow_html=True
    )