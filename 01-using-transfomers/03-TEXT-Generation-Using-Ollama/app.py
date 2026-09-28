import streamlit as st
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma4:26b"

st.title("Text Generation Agent")
st.write("Generate text locally using Ollama + Gemma 4 26B.")

prompt = st.text_input("Enter your prompt:")

max_tokens = st.slider(
    "Max tokens of output",
    50,
    1000,
    300
)

temperature = st.slider(
    "Temperature",
    0.0,
    2.0,
    0.7,
    0.1
)

if st.button("Generate"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": temperature,
                        "top_p": 0.9,
                        "num_predict": max_tokens
                    }
                },
                timeout=300
            )

            response.raise_for_status()

            result = response.json()

            st.subheader("Generated Text")
            st.write(result["response"])

        except requests.exceptions.ConnectionError:
            st.error(
                "Ollama is not running. Start Ollama and try again."
            )

        except requests.exceptions.Timeout:
            st.error("The generation request timed out.")

        except requests.exceptions.RequestException as e:
            st.error(f"Ollama API error: {e}")
