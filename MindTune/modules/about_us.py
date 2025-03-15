import streamlit as st

def show_about_us():
    st.write(
        """
        <style>
        .title { 
            font-size: 1.7em; 
            font-weight: bold; 
            text-align: center; 
            margin-bottom: 25px; 
        }
        .centered-subtitle { 
            font-size: 1.1em; 
            font-weight: bold; 
            text-align: center; 
            margin-top: 20px; 
        }
        .text { 
            font-size: 0.875em; 
            line-height: 1.5; 
        }
        .bold { 
            font-weight: bold; 
        }
        .call-to-action { 
            font-size: 1em; 
            text-align: center; 
            padding: 15px; 
        }
        .divider { 
            border-top: 1px solid #ccc; 
            margin: 15px 0; 
        }
        </style>

        <div class="title">🤖 Meet the Team Behind the Innovation</div>

        <div class="centered-subtitle">🚀 Who We Are</div>
        <div class="text">
            We are a passionate team from <span class="bold">Timișoara</span>, united by a shared mission: 
            <span class="bold">to explore, develop, and innovate</span> in the world of AI.  
            From a spark of an idea to fully realized projects, we are committed to crafting solutions that make a real-world impact.
        </div>

        <div class="divider"></div>

        <div class="centered-subtitle">💡 Our Vision</div>
        <div class="text">
            Our journey is fueled by <span class="bold">creativity, resilience, and curiosity</span>.  
            Each project starts with an <span class="bold">ambition to solve complex challenges</span>,  
            and through teamwork and dedication, we turn ideas into tangible, high-quality results.
        </div>

        <div class="divider"></div>

        <div class="centered-subtitle">🌍 Our Impact</div>
        <div class="text">
            We believe AI has the power to <span class="bold">transform lives</span> and shape the future for the better.  
            With every project, we strive to bridge the gap between <span class="bold">imagination and reality</span>,  
            ensuring that technology serves a greater purpose.
        </div>

        <div class="divider"></div>

        <div class="centered-subtitle">🤝 Join Us on Our Journey</div>
        <div class="text">
            We are more than just a team—we are a <span class="bold">community</span>.  
            Constantly learning, growing, and pushing boundaries, we are ready to tackle the next big idea.  
            <span class="bold">Let’s innovate together!</span>
        </div>

        <div class="call-to-action"><span class="bold">✨ Ready to be part of the future of AI? ✨</span></div>
        """,
        unsafe_allow_html=True
    )
