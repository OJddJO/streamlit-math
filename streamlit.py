import streamlit as st
import streamlit_elements as elements

st.title("Math")

st.session_state["boxes"] = []
if st.button("Add a new box"):
    with st.session_state["boxes"].append(elements.elements(len(st.session_state["boxes"]))):
        tabs = st.tabs(["View", "Edit"])