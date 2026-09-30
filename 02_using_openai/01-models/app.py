from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st

# Load env variables
load_dotenv()

# Get API key and model name
api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME")

# Init OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("Chat with LLMs without Agents- Generator")
input_prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if input_prompt:
        try:
            response = client.responses.create(
                model=model_name,
                input=input_prompt
            )

            st.write("### LLM Response")
            st.write(response.output[0].content[0].text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")