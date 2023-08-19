import streamlit as st

st.title("Math")
st.set_page_config(page_title="Math", page_icon="🟰")

st.session_state.text = 'Hello World!'

columns = st.columns(2)

with columns[0]:
    st.header("Input")
    st.text_area(label="Input", placeholder="Input", key="input", value=st.session_state.text, height=600, label_visibility="collapsed")
    with st.button("Update"):
        st.session_state.text = st.session_state.input
        st.experimental_rerun()

with columns[1]:
    st.latex(st.session_state.text)
