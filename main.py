import streamlit as st

st.set_page_config(page_title="Math", page_icon="🟰", layout="wide")
st.title("Math")

st.session_state.text = ''

columns = st.columns(2)

with columns[0]:
    input = st.text_area(label="Input", placeholder="Input", key="input", height=200, label_visibility="collapsed")
    if st.button("Update"):
        st.session_state.text = input
        st.experimental_rerun()
with columns[1]:
    st.latex(st.session_state.text)
