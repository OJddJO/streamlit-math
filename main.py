import streamlit as st

st.set_page_config(page_title="Math", page_icon="🟰", layout="wide")
st.title("Math")

st.session_state.text = ''

columns = st.columns(2)

def update_text(input):
    st.session_state.text = input
    with columns[1]:
        st.latex(st.session_state.text)

with columns[0]:
    input = st.text_area(label="Input", placeholder="Input", key="input", height=200, label_visibility="collapsed", on_change=update_text)
    if st.button("Update"):
        update_text(input)
