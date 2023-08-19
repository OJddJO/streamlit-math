import streamlit as st
import streamlit_elements as elements

st.title("Math")

st.session_state["boxes"] = 0
if st.button("Add a new box"):
    with elements.elements(st.session_state["boxes"]):
        tabs = st.tabs(["View", "Edit"])
    st.session_state["boxes"] += 1