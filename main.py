import streamlit as st

st.set_page_config(page_title="Math", page_icon="🟰", layout="wide")
st.title("Math")

st.session_state.text = 'Hello World!'

columns = st.columns(2)

def update_data():
    st.session_state.text = input
    st.experimental_rerun()

with columns[0]:
    input = st.text_area(label="Input", placeholder="Input", key="input", value=st.session_state.text, height=200, label_visibility="collapsed", on_change=update_data)
    if st.button("Update"):
        update_data()
with columns[1]:
    st.latex(st.session_state.text)
