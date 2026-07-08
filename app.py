
import streamlit as st

# The Titles
st.title('🤖My First AI Web App')
st.header('Welcome to the Dashboard')
st.subheader('Sub-Section: Data Analysis')

# Standard text
st.write("This is a standard text. st.write() is the 'print' function of Streamlit")

st.text("This is fixed-width text, good for showing raw code or logs.")

st.markdown("**Bold Text**, *Italic text*, and even [Links](https://streamlit.io).")

# Status Message
st.success("The AI successfully processed your request!")
st.error("Critical Error: API Key missing.")
st.warning("Warning: The model might hallucinate.")
st.info("Fun Fact: Llama-3 has 8 billion parameters.")
