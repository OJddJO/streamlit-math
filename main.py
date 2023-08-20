import streamlit as st

st.set_page_config(page_title="Math", page_icon="🟰", layout="wide")
st.title("Math")

st.session_state.text = ''

latex_container = st.container()

def update_text():
    st.session_state.text = input
    with latex_container:
        st.latex(st.session_state.text)

with st.form(key="input_form"):
    input = st.text_area(label="Input", placeholder="Input", key="input", height=100, label_visibility="collapsed")
