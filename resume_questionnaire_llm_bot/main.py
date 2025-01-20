from backend.core import res_docs
import streamlit as st
from streamlit_chat import message

st.header("MY LLM RESUME")

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []
if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

prompt = st.text_input("Ask about ME", placeholder="Enter your question here...")

if prompt:
    with st.spinner("Generating response..."):
        generated_response = res_docs(
            query=prompt, chat_history=st.session_state["chat_history"]
        )
        
        st.session_state["user_prompt_history"].append(prompt)
        st.session_state["chat_answers_history"].append(generated_response["result"])
        st.session_state["chat_history"].append(("human", prompt))
        st.session_state["chat_history"].append(("ai", generated_response["result"]))

if st.session_state["chat_answers_history"]:
    for user_query, generated_response in zip(
        st.session_state["user_prompt_history"],
        st.session_state["chat_answers_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
