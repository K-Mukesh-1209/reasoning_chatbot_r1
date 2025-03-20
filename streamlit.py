import streamlit as st

uploaded_file = st.file_uploader("Upload Here",
                                 type="pdf",
                                 accept_multiple_files=False)
user_query = st.text_area("Enter your prompt: ",height=150,placeholder = "Ask anything!")

ask_question = st.button("ASK AI Lawyer")

if ask_question:
    
    if uploaded_file:
        st.chat_message("user").write(user_query)
    
        fixed_response = "Hi, this is a fixed response!"
        st.chat_message("AI Lawyer").write(fixed_response)
    else:
        st.error("Upload a valid file")
        
    