import os
from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Model and API token setup
model_id = "mistralai/Mistral-7B-Instruct-v0.3"

try:
    token_api = os.getenv("HF_TOKEN")
except:
    print('Load local secret')
    with open('../.secret') as f:
        token_api = f.readlines()
    token_api = token_api[0]


def get_llm_hf_inference(model_id=model_id, max_new_tokens=128, temperature=0.1):
    llm = HuggingFaceEndpoint(
        repo_id=model_id,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        token=token_api
    )
    return llm


def questionnaire():
    st.title("Mental Wellness Chatbot 🧠💬")

    predicted_class = st.session_state.prediction

    # Initialize session state for messages
    if "messages" not in st.session_state:
        if predicted_class == 1:
            st.session_state["messages"] = [
                {
                    "role": "assistant",
                    "content": (
                        "Hi there! 🌱 On a scale from 1 to 10, how stressed do you feel right now?\n\n"
                        "**1-3** – Calm\n\n"
                        "**4-6** – Managing\n\n"
                        "**7-8** – Stressed\n\n"
                        "**9-10** – Overwhelmed\n\n"
                    ),
                }
            ]
        else:
            st.session_state["messages"] = [
                {
                    "role": "assistant",
                    "content": (
                        "That's great to hear you're feeling relaxed! 🌿 Can you share what’s currently bringing you peace and joy? On a scale from 1 to 10, how connected do you feel to that positive state right now?\n\n"
                        "**1-3** – Disconnected: You might feel a bit distant from what’s making you happy.\n\n"
                        "**4-6** – Moderately Connected: You’re aware of the good vibes but may have some distractions.\n\n"
                        "**7-8** – Connected: You're in tune with your positive feelings and enjoying the moment.\n\n"
                        "**9-10** – Deeply Connected: You feel completely aligned with your state of relaxation and happiness!\n\n"
                        "What specific things or experiences are contributing to your current mood?"
                    )
                }
            ]

    if "count_prompt" not in st.session_state:
        st.session_state["count_prompt"] = 0

    # Display previous messages
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        elif message["role"] == "assistant":
            st.chat_message("assistant").write(message["content"])

    # Handle user input if the prompt count is below 3
    if st.session_state["count_prompt"] < 3:
        if prompt := st.chat_input("What's on your mind?"):
            st.session_state["messages"].append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            st.session_state["count_prompt"] += 1

            # Generate response if it's the first or second prompt
            if st.session_state["count_prompt"] < 3:
                st.session_state["messages"].append(
                    {"role": "system",
                     "content": "Generate a single question quiz to better understand the situation based on all the context you have."})

                try:
                    # Setup HuggingFace model
                    hf = get_llm_hf_inference(max_new_tokens=128, temperature=0.1)

                    # Create the prompt template
                    prompt = PromptTemplate.from_template(
                        (
                            "[INST] {system_message}"
                            "\nCurrent Conversation:\n{chat_history}\n\n"
                            "\nUser: {user_text}.\n [/INST]"
                            "\nAI:"
                        )
                    )

                    # Generate the response
                    chat = prompt | hf.bind(skip_prompt=True) | StrOutputParser(output_key='content')

                    # Invoke the model
                    response = chat.invoke(
                        input=dict(system_message="friendly AI conversing with a human user",
                                   user_text=prompt,
                                   chat_history=st.session_state["messages"])
                    )

                    # Extract and append the assistant's response
                    response = response.split("AI:")[-1]
                    st.session_state["messages"].append({"role": "assistant", "content": response})
                    st.chat_message("assistant").write(response)
                except Exception as e:
                    st.error("Error generating assistant response.")
                    print(f"An error occurred: {e}")

    # If the prompt count reaches 3, trigger summary and tips
    if st.session_state["count_prompt"] == 3:
        st.session_state["messages"].append(
            {"role": "system", "content": "Generate a short summary and 3 tips about the situation."})

        # Generate summary and tips response
        try:
            # Setup HuggingFace model again for summary
            hf = get_llm_hf_inference(max_new_tokens=128, temperature=0.1)

            # Create the prompt for the summary
            prompt = PromptTemplate.from_template(
                (
                    "[INST] {system_message}"
                    "\nCurrent Conversation:\n{chat_history}\n\n"
                    "\nUser: {user_text}.\n [/INST]"
                    "\nAI:"
                )
            )

            # Invoke the model for summary and tips
            chat = prompt | hf.bind(skip_prompt=True) | StrOutputParser(output_key='content')
            response = chat.invoke(
                input=dict(system_message="friendly AI conversing with a human user",
                           user_text=st.session_state["messages"][-1]["content"],
                           chat_history=st.session_state["messages"])
            )

            # Extract and append the assistant's response
            response = response.split("AI:")[-1]
            st.session_state["messages"].append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)

        except Exception as e:
            st.error("Error generating summary and tips.")
            print(f"An error occurred: {e}")

        # End conversation
        st.write("Thank you for chatting with me. Take care!")
        st.stop()

    # If the user has reached the prompt limit, stop further input
    if st.session_state["count_prompt"] >= 3:
        st.stop()
