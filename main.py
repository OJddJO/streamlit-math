import streamlit as st
import json

st.set_page_config(page_title="Math", page_icon="🟰", layout="wide")
st.title("Math")

st.session_state.text = ''

st.sidebar.markdown(r"""| **Latex** | **Text** |
|-----------|----------|
| $\alpha$  | alpha    |
|           |          |
|           |          |
""")

latex_container = st.container()

def evaluate_latex(text):
    latex = ""
    latex_dict = json.load(open("latex.json", "r"))
    latex_func = json.load(open("latex_func.json", "r"))
    i = 0
    while text != '':
        #check if text[:i] is in latex_dict
        if text[:i] in latex_func: #if it is
            func = latex_func[text[:i]] #add latex to func
            latex += func[0]
            nb_args = func[1] #get number of args
            text = text[i:]
            #check nested in func
            i = 0
            nested = 0
            end = False
            arg_list = []
            while nb_args > 0:
                while not end:
                    if text[i] == '(':
                        nested += 1
                    elif text[i] == ')':
                        nested -= 1
                    if nested == 0:
                        end = True
                        arg_list.append(evaluate_latex(text[1:i]))
                        print(arg_list)
                    else:
                        i += 1
                    print(i, text[i], nested, text)
                end = False
                text = text[i+1:]
                i = 0
                nb_args -= 1
            for i, arg in enumerate(arg_list):
                print(arg, i+1)
                latex = latex.replace(f"¤{i+1}", arg)
            text = text[i:] #remove from text
        elif text[:i] in latex_dict: #if in latex_dict
            latex += latex_dict[text[:i]] #add latex
            text = text[i:] #remove from text
        else: #if not
            i += 1
            if i > len(text):
                if text[0] == '\n':
                    latex += '\\\\'
                else:
                    latex += text[0]
                text = text[1:]
                i = 0
    return latex

def update_text():
    st.session_state.text = input
    tmp = st.session_state.text
    tmp = evaluate_latex(tmp)
    with latex_container:
        st.latex(tmp)

with st.form(key="input_form"):
    input = st.text_area(label="Input", placeholder="Input", key="input", height=100, label_visibility="collapsed")
    if st.form_submit_button("Submit"):
        update_text()