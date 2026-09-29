import streamlit as st
from transformers import pipeline

# Load GPT-2 text generator
generator = pipeline("text-generation", model="gpt2")

# Streamlit UI
st.title("Text Generation Agent V1.0")
st.write("Type any prompt below and GPT-2 will generate text for you.")

# Runtime input from user
prompt = st.text_input("Enter your prompt:")

# Slider for length
max_len = st.slider("Max length of output", 50, 300, 100)

# Generate only when user clicks
if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt first.")
    else:
        output = generator(
            prompt
        )
        st.subheader("Generated Text:")
        st.write(output[0]['generated_text'])
