# Import Essential Libraries
from langchain.agents import create_agent

from dotenv import load_dotenv
import os
import streamlit as st

# Load env variables
load_dotenv()

# Get API key and model name
api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("MODEL_NAME")

# Init agent
agent = create_agent(
    model=model_name,
    system_prompt="You are a helpful assistant",
)

#input_prompt = input("Enter your prompt: ")

#result = agent.invoke(
 #   {"messages": [{"role": "user", "content": input_prompt}]}
#)

#print(result["messages"][-1].content_blocks)

# Invoke the agent
# Streamlit UI
st.title("Chat with LLMs with Agents- Generator")
input_prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if input_prompt:
        try:
            result = agent.invoke(
                {"messages": [{"role": "user", "content": input_prompt}]}
            )
            st.write("### Agent Response")
            st.write(result["messages"][-1].content_blocks)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")