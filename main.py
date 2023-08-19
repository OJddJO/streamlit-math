import streamlit as st
import streamlit_elements as elements

st.title("Math")

st.session_state.layout = []
st.session_state.text = []

page = elements.elements("page")

if st.button("Add a new box"):
    with page:
        # Add a new tab
        st.session_state.layout.append(elements.dashboard.Item(i=f"Box {len(st.session_state.layout)+1}", x=len(st.session_state.layout)%2, y=len(st.session_state.layout)//2, w=1, h=1))
        with elements.dashboard.Grid([st.session_state.layout[-1]]):
            tabs = st.tabs(["Edit", "View"])
            with tabs[0]:
                st.session_state.text.append("")
                def update_text(value):
                    st.session_state.text[-1] = value
                elements.editor.Monaco(
                    height=200,
                    value=st.session_state.text[-1],
                    onChange=update_text,
                )
                elements.mui.Button("Update content", onClick=elements.sync())
            with tabs[1]:
                st.write(st.session_state.text[-1])
        tabs = st.tabs(["View", "Edit"])