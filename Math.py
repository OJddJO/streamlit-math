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
| $\int x$                               | int x                                |
| $\int_{a}^{b} x$                       | int_(a)^(b) x                        |
| $\displaystyle\sum_{a}^{b}{x}$         | sum(a)(b)(x)                         |
| $\displaystyle\prod_{a}^{b}{x}$        | prod(a)(b)(x)                        |
| $\lim\limits_{x \to 2}{x}$             | lim(x to 2)(x)                       |
| $\frac{a}{b}$                          | frac(a)(b)                           |
| $\sqrt{x}$                             | sqrt(x)                              |
| $\sqrt[n]{x}$                          | rt(n)(x)                             |
| $\forall$                              | forall                               |
| $\exists$                              | exists                               |
| $\lceil{x}\rceil$                      | ceil(x)                              |
| $\lfloor{x}\rfloor$                    | floor(x)                             |
| $\text{\textquotedblleft}{quote}\text{\textquotedblright}$| quote(quote)      |
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
| $\in$                                  | in                                   |
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

if "latex" not in st.session_state:
    st.session_state.latex = []
if "text" not in st.session_state:
    st.session_state.text = []

latex_dict = json.load(open("latex.json", "r", encoding="utf-8"))
latex_func = json.load(open("latex_func.json", "r", encoding="utf-8"))

def evaluate_latex(text:str) -> str:
    try:
        latex = ""
        i = 0
        while text != '':
            #check if text[:i] is in latex_dict
            parenthesis = text.find("(")
            if parenthesis != -1 and text[:parenthesis] in latex_dict:
                i = parenthesis
            if text[:i] in latex_func and text[i]=="(": #if it is
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
                next_space = text.find(" ")
                if next_space != -1:
                    if text[:next_space] in latex_dict:
                        i = next_space
                latex += latex_dict[text[:i]] #add latex
                text = text[i:] #remove from text
                i = 0
            else: #if not
                i += 1
                if i > len(text):
                    if text.find("\n") == 0:
                        latex += ' \\\\ '
                    else:
                        latex += text[0]
                    text = text[1:]
                    i = 0
    except:
        latex += '\\\\\\color{red}\\text{!! Error !!}'
    return latex

latex_container, source_container = st.tabs(["Latex", "Source"])

prompt = st.chat_input("Enter your text here", key="latex_prompt")
if prompt:
    st.session_state.latex.append(evaluate_latex(prompt))
    st.session_state.text.append(prompt)

edit_container, delete_container, clear_container, save_container, save_as_latex_container, load_container = st.columns(6)

if clear_container.button("Clear", icon="🗑️", use_container_width=True):
    st.session_state.latex = []
    st.session_state.text = []

with delete_container.popover("Delete line", icon="❌", use_container_width=True):
    for i in range(len(st.session_state.latex)):
        latex_render, del_button = st.columns([9, 1])
        latex_render.latex(st.session_state.latex[i])
        if del_button.button(label="❌", key=i, use_container_width=True):
            del st.session_state.latex[i]
            del st.session_state.text[i]
            st.rerun()

@st.dialog("Edit line")
def edit_line(i):
    st.latex(st.session_state.latex[i])
    edit = st.text_input("Edit your text here", value=st.session_state.text[i], key=f"edit_prompt_{i}")
    if edit != st.session_state.text[i]:
        st.session_state.latex[i] = evaluate_latex(edit)
        st.session_state.text[i] = edit
        st.rerun()
with edit_container.popover("Edit line", icon="✏️", use_container_width=True):
    for i in range(len(st.session_state.latex)):
        latex_render, edit_button = st.columns([9, 1])
        latex_render.latex(st.session_state.latex[i])
        if edit_button.button(label="✏️", key=f"edit_btn_{i}", use_container_width=True):
            edit_line(i)

@st.dialog("Save")
def save():
    filename = st.text_input("File name", value="my_math_save.sm", key="file_name")
    if filename.split(".")[-1] != "sm":
        filename += "sm"
    st.download_button("Download", icon="📥", data=str(st.session_state.text), file_name=filename)
if save_container.button("Save", icon="📥", use_container_width=True):
    save()

@st.dialog("Save as Markdown")
def save_as_latex():
    filename = st.text_input("File name", value="my_math_save.md", key="file_name")
    if filename.split(".")[-1] != "md":
        filename += "md"
    st.download_button("Download", icon="📥", data="$"+"\n\\\\".join(st.session_state.latex)+"$", file_name=filename)
if save_as_latex_container.button("Save as .md",  icon="📥", use_container_width=True):
    save_as_latex()

@st.dialog("Load")
def load():
    file = st.file_uploader("Upload a file", type="sm")
    if file:
        st.session_state.text = eval(file.read())
        for line in st.session_state.text:
            st.session_state.latex.append(evaluate_latex(line))
        st.rerun()
if load_container.button("Load", icon="📤", use_container_width=True):
    load()


with latex_container:
    st.container(border=True, height=550).latex("\\\\".join(st.session_state.latex))

with source_container:
    st.container(border=True, height=550).code("\n".join(st.session_state.text), language=None)
