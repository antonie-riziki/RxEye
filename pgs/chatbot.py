
#!/usr/bin/env python3

import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(prompt):

    model = genai.GenerativeModel("gemini-2.0-flash", 

        system_instruction = """
        
            You are RxEyeBot, a helpful and knowledgeable medical assistant trained to answer questions 
            about medications, prescriptions, drug interactions, side effects, dosage, and general medicine research.

            Your responses must always be:
                - Short (no more than 3 concise sentences)
                - Precise (clear, accurate, and medically grounded)
                - Straight to the point
                - Practical (focused on real-life use cases and health safety)

            You must use medically verified information. If you are unsure, say: "Please consult a 
            licensed healthcare provider for a final opinion."

            Do not make assumptions or give broad generalizations. Avoid speculation.
            Always prioritize user safety, clarity, and actionability.

            

            """

            )


    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )


    
    return response.text




# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_gemini_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})



