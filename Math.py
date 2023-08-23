import streamlit as st
import json
from PIL import Image
from db import getUser, updateData

icon = Image.open("icon.png")
st.set_page_config(page_title="Math", page_icon=icon, layout="wide", initial_sidebar_state="expanded")
st.title("Math")

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 350px !important;
        }
        .css-1i2wz1k {
            width: 0 !important;
            height: 0 !important;
        }
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.css-1cypcdb.eczjsme11 > div:nth-child(2) > div {
            width: 0 !important;
            height: 0 !important;
        }
        .css-1oe5cao {
            max-height: 100% !important;
        }
        .css-40ynm6 {
            width: 0 !important;
            height: 0 !important;
        }
        .css-912zdv {
            width: 0 !important;
            height: 0 !important;
            display: none !important;
        }
        .css-1pxazr7 {
            width: 0 !important;
            height: 0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar.expander("Help"):
    st.markdown(r"""| **KaTeX** | **Text** |
|-----------|----------|
| $\text{text}$| text(text)| #latex_func.json
| $a^x$    | a^(x)    |
| $a_x$    | a_(x)    |
| $\int{x}$ | int(x)   |
| $\int_{a}^{b}{x}$| Int(a)(b)(x)|
| $\sum_{a}^{b}{x}$| sum(a)(b)(x)|
| $\prod_{a}^{b}{x}$| prod(a)(b)(x)|
| $\lim_{x \to 2}{x}$| lim(x to 2)(x)|
| $\frac{a}{b}$| frac(a)(b)|
| $\sqrt{x}$| sqrt(x)  |
| $\sqrt[n]{x}$| rt\[n\](x)|
| $\bar{x}$ | bar(x)   |
| $\dot{x}$ | dot(x)   |
| $\ddot{x}$| ddot(x)  |
| $\vec{x}$ | vec(x)   |
| $\widehat{x}$| widehat(x)|
| $\begin{matrix}a&b\\c&d\end{matrix}$| matrix(a & b \\\\ c & d)|
| $\begin{pmatrix}a&b\\c&d\end{pmatrix}$| pmatrix(a & b \\\\ c & d)|
| $\begin{bmatrix}a&b\\c&d\end{bmatrix}$| bmatrix(a & b \\\\ c & d)|
| $\begin{Bmatrix}a&b\\c&d\end{Bmatrix}$| Bmatrix(a & b \\\\ c & d)|
| $\begin{vmatrix}a&b\\c&d\end{vmatrix}$| vmatrix(a & b \\\\ c & d)|
| $\begin{Vmatrix}a&b\\c&d\end{Vmatrix}$| Vmatrix(a & b \\\\ c & d)|
| $\begin{cases}a&b\\c&d\end{cases}$| cases(a & b \\\\ c & d)|
| $\begin{rcases}a&b\\c&d\end{rcases}$| rcases(a & b \\\\ c & d)|
| $\infty$  | infty    | #latex.json
| $\forall$ | forall   |
| $\lceil$  | lceil    |
| $\rceil$  | rceil    |
| $\lfloor$ | lfloor   |
| $\rfloor$ | rfloor   |
| $\to$     | to       |
| $\approx$ | approx   |
| $\neq$    | neq      |
| $\Leftrightarrow$| equiv|
| $\Rightarrow$| implies|
| $\geqslant$| gequal  |
| $\leqslant$| lequal  |
| $\in$     | in       |
| $\notin$  | nin      |
| $\subset$ | subset   |
| $\alpha$  | alpha    |
| $\beta$   | beta     |
| $\gamma$  | gamma    |
| $\delta$  | delta    |
| $\epsilon$| epsilon  |
| $\zeta$   | zeta     |
| $\eta$    | eta      |
| $\theta$  | theta    |
| $\iota$   | iota     |
| $\kappa$  | kappa    |
| $\lambda$ | lambda   |
| $\mu$     | mu       |
| $\nu$     | nu       |
| $\xi$     | xi       |
| $\pi$     | pi       |
| $\rho$    | rho      |
| $\sigma$  | sigma    |
| $\tau$    | tau      |
| $\upsilon$| upsilon  |
| $\phi$    | phi      |
| $\chi$    | chi      |
| $\psi$    | psi      |
| $\omega$  | omega    |
| $\Gamma$  | Gamma    |
| $\Delta$  | Delta    |
| $\Theta$  | Theta    |
| $\Lambda$ | Lambda   |
| $\Xi$     | Xi       |
| $\Pi$     | Pi       |
| $\Sigma$  | Sigma    |
| $\Upsilon$| Upsilon  |
| $\Phi$    | Phi      |
| $\Psi$    | Psi      |
| $\Omega$  | Omega    |
""")

st.session_state.text = []

st.session_state.latex_container = []

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
                        i += 1
                    else:
                        i += 1
                end = False
                text = text[i:]
                i = 0
                nb_args -= 1
            for i, arg in enumerate(arg_list):
                latex = latex.replace(f"¤{i+1}", arg)
            text = text[i:] #remove from text
        elif text[:i] in latex_dict: #if in latex_dict
            latex += latex_dict[text[:i]] #add latex
            text = text[i:] #remove from text
            i = 0
        else: #if not
            i += 1
            if i > len(text):
                if text.find("\n") == 0:
                    latex += '\\\\ '
                else:
                    latex += text[0]
                text = text[1:]
                i = 0
    return latex

def update_text(page, text):
    latex = text
    latex = evaluate_latex(latex)
    with st.session_state.latex_container[page]:
        st.latex(latex)

def not_logged_page():
    st.session_state.latex_container.append(st.container())
    with st.form(key="input_form"):
        input = st.text_area(label="Input", placeholder="Input", key="input", height=100, label_visibility="collapsed")
        if st.form_submit_button("Submit"):
            update_text(0, input)
    st.info("If you want to save your work, please login")

def logged_page():
    data = getUser(st.session_state.username)
    saved = data["save"]
    tabs_name = [save[1] for save in saved]
    tabs_name.append("New page")
    tabs = st.tabs(tabs_name)
    for i, save in enumerate(saved):
        st.session_state.text.append(save)
        with tabs[i]:
            st.session_state.latex_container.append(st.container())
            with st.form(key=f"input_form{i}"):
                input = st.text_area(label="Input", placeholder="Input", key=f"input{i}", height=100, label_visibility="collapsed", value=st.session_state.text[i][0])
                if st.form_submit_button("Submit"):
                    update_text(i, input)
                    st.session_state.text[i][0] = input
                    updateData({"save": st.session_state.text}, st.session_state.username)
            if st.button("Delete page", key=f"delete{i}"):
                st.session_state.text.pop(i)
                updateData({"save": st.session_state.text}, st.session_state.username)
                st.experimental_rerun()
    with tabs[-1]:
        with st.form(key=f"input_form{len(saved)}"):
            title = st.text_input(label="Title", placeholder="Title", key="title", label_visibility="collapsed")
            if st.form_submit_button("Add new page"):
                st.session_state.text.append(["", title])
                updateData({"save": st.session_state.text}, st.session_state.username)
                st.experimental_rerun()

try:
    if st.session_state.authentication_status == True:
        logged_page()
        st.session_state.authenticator.logout("Logout", "sidebar")

    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        not_logged_page()

except Exception as e:
    not_logged_page()