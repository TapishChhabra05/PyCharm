# import os
from gc import set_debug

from langchain_openai import ChatOpenAI
# from langchain.globals import set_debug
#
# set_debug(True)

# To Create UI
import streamlit as st

st.title("Ask Anything...")

with st.sidebar:
    st.title("Provide your API Key")
    OPENAI_API_KEY = st.text_input("Enter your OpenAI API Key", type="password")
    if not OPENAI_API_KEY:
        st.info("Please enter your OpenAI API Key to Continue")
        st.stop()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model= "gpt-4o", api_key=OPENAI_API_KEY)
question= st.text_input("Enter the Question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)
# Helps to access direct text
# print(response.content)