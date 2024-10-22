import streamlit as st
import json
from PIL import Image

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

with st.sidebar.expander("Operations"):
    st.markdown(
r"""| **KaTeX** | **Text** |
|----------------------------------------|--------------------------------------|
| $\text{text}$ (litteral text)          | "(text)                              |
| $a^x$                                  | a^(x)                                |
| $a_x$                                  | a_(x)                                |
| $\int{x}$                              | int_(x)                              |
| $\int_{a}^{b}{x}$                      | Int_(a)(b)(x)                        |
| $\sum_{a}^{b}{x}$                      | sum(a)(b)(x)                         |
| $\prod_{a}^{b}{x}$                     | prod(a)(b)(x)                        |
| $\lim_{x \to 2}{x}$                    | lim(x to 2)(x)                       |
| $\frac{a}{b}$                          | frac(a)(b)                           |
| $\sqrt{x}$                             | sqrt(x)                              |
| $\sqrt[n]{x}$                          | rt(n)(x)                             |
| $\forall$                              | forall                               |
| $\exists$                              | exists                               |
| $\lceil$                               | lceil                                |
| $\rceil$                               | rceil                                |
| $\lfloor$                              | lfloor                               |
| $\rfloor$                              | rfloor                               |
| $\neg a$                               | neg a                                |
| $\not a$                               | not a                                |
| $\to$                                  | to                                   |
| $\approx$                              | approx                               |
| $\neq$                                 | neq                                  |
| $\Leftrightarrow$                      | equiv                                |
| $\Rightarrow$                          | implies                              |
| $\Leftarrow$                           | implied                              |
| $\geqslant$                            | gequal                               |
| $\leqslant$                            | lequal                               |
| $\cong$                                | cong                                 |
| $\in$                                  | in_                                  |
| $\notin$                               | nin                                  |
| $\subset$                              | subset                               |"""
    )

with st.sidebar.expander("Structures"):
    st.markdown(
r"""| **KaTeX** | **Text** |
|----------------------------------------|--------------------------------------|
| $\begin{aligned}a&=b+c \\ a-c&=b\end{aligned}$| align(a &= b \\\\ a-c &= b)   |
| $\begin{matrix}a&b\\c&d\end{matrix}$   | matrix(a & b \\\\ c & d)             |
| $\begin{cases}a&b\\c&d\end{cases}$     | cases(a & b \\\\ c & d)              |
| $\begin{rcases}a&b\\c&d\end{rcases}$   | rcases(a & b \\\\ c & d)             |
| $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ | pmatrix(a & b \\\\ c & d)            |
| $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ | bmatrix(a & b \\\\ c & d)            |
| $\begin{Bmatrix}a&b\\c&d\end{Bmatrix}$ | Bmatrix(a & b \\\\ c & d)            |
| $\begin{vmatrix}a&b\\c&d\end{vmatrix}$ | vmatrix(a & b \\\\ c & d)            |
| $\begin{Vmatrix}a&b\\c&d\end{Vmatrix}$ | Vmatrix(a & b \\\\ c & d)            |"""
    )

with st.sidebar.expander("Sets"):
    st.markdown(
r"""| **KaTeX** | **Text** |
|----------------------------------------|--------------------------------------|
| $\char"2115$                           | natural                              |
| $\char"2124$                           | integer                              |
| $\char"211A$                           | rational                             |
| $\char"211D$                           | real                                 |
| $\char"2102$                           | complex                              |"""
    )

with st.sidebar.expander("Others"):
    st.markdown(
r"""| **KaTeX** | **Text** |
|----------------------------------------|--------------------------------------|
| $\color{red}a=b+c$                     | color(red)a=b+c                      |
| $\bar{x}$                              | bar(x)                               |
| $\dot{x}$                              | dot(x)                               |
| $\ddot{x}$                             | ddot(x)                              |
| $\vec{x}$                              | vec(x)                               |
| $\widehat{x}$                          | widehat(x)                           |
| $\infty$                               | inf                                  |
| $\alpha$                               | alpha                                |
| $\beta$                                | beta                                 |
| $\gamma$                               | gamma                                |
| $\delta$                               | delta                                |
| $\epsilon$                             | epsilon                              |
| $\zeta$                                | zeta                                 |
| $\eta$                                 | eta                                  |
| $\theta$                               | theta                                |
| $\iota$                                | iota                                 |
| $\kappa$                               | kappa                                |
| $\lambda$                              | lambda                               |
| $\mu$                                  | mu                                   |
| $\nu$                                  | nu                                   |
| $\xi$                                  | xi                                   |
| $\pi$                                  | pi                                   |
| $\rho$                                 | rho                                  |
| $\sigma$                               | sigma                                |
| $\tau$                                 | tau                                  |
| $\upsilon$                             | upsilon                              |
| $\phi$                                 | phi                                  |
| $\chi$                                 | chi                                  |
| $\psi$                                 | psi                                  |
| $\omega$                               | omega                                |
| $\Gamma$                               | Gamma                                |
| $\Delta$                               | Delta                                |
| $\Theta$                               | Theta                                |
| $\Lambda$                              | Lambda                               |
| $\Xi$                                  | Xi                                   |
| $\Pi$                                  | Pi                                   |
| $\Sigma$                               | Sigma                                |
| $\Upsilon$                             | Upsilon                              |
| $\Phi$                                 | Phi                                  |
| $\Psi$                                 | Psi                                  |
| $\Omega$                               | Omega                                |"""
    )

st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

if "text" not in st.session_state:
    st.session_state.text = ""

def evaluate_latex(text):
    try:
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
                            if func[0] == "\\text{¤1}":
                                arg_list.append(text[1:i])
                            else:
                                arg_list.append(evaluate_latex(text[1:i]))
                        i += 1
                    end = False
                    text = text[i:]
                    i = 0
                    nb_args -= 1
                for i, arg in enumerate(arg_list):
                    latex = latex.replace(f"¤{i+1}", arg)
                i = 0 
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
    except:
        latex += '\\\\\\color{red}\\text{!! Error !!}'
    return latex

def update_text():
    latex = evaluate_latex(input)
    latex_container.latex(latex)
    st.session_state.text = input

latex_container = st.container()
with st.expander(label="Input Zone", expanded=True):
    input = st.text_area(label="Input", placeholder="Input", value=st.session_state.text, key="input", height=400, label_visibility="collapsed", on_change=update_text)
    col1, col2 = st.columns(2)
    submit = col1.button("Submit")
    if submit:
        update_text(input)
    if col2.button("Clear"):
        st.session_state.text = ""
        st.rerun()
