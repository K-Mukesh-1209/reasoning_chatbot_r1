import streamlit as st
from rag_pipeline import answer_query,retrieve_docs,llm_model
uploaded_file = st.file_uploader("Upload Here",
                                 type="pdf",
                                 accept_multiple_files=False)
user_query = st.text_area("Enter your prompt: ",height=150,placeholder = "Ask anything!")

ask_question = st.button("ASK AI Lawyer")

if ask_question:
    
    if uploaded_file:
        st.chat_message("user").write(user_query)
        retrieved_docs=retrieve_docs(user_query)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
        st.chat_message("AI Lawyer").write(response)
    else:
        st.error("Upload a valid file")
        
    