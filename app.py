import streamlit as st
import google.generativeai as genai
st.write("Mohamed mydeen")
genai.configure(api_key="AIzaSyCBwiYm-68EHhtEYBs7HmhNAG7L8HPKABE")
text = text = st.text_input("Enter your question :")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
