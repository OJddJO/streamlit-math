import streamlit as st

st.set_page_config(page_title="Math", page_icon="🟰", layout="wide")
st.title("Math")

st.session_state.text = ''

columns = st.columns(2)

def update_text():
    st.session_state.text = input
    with columns[1]:
        st.latex(st.session_state.text)

with columns[0]:
    with st.form(key="input_form"):
        input = st.text_area(label="Input", placeholder="Input", key="input", height=200, label_visibility="collapsed")
        if st.form_submit_button("Update"):
            update_text()
