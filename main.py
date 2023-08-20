import streamlit as st
import json

st.set_page_config(page_title="Math", page_icon="🟰", layout="wide")
st.title("Math")

st.session_state.text = ''

st.sidebar.markdown(r"""| **Latex** | **Text** |
|-----------|----------|
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
| $\infty$  | infty    |
| $\forall$ | forall   |
| $\lceil$  | lceil    |
| $\rceil$  | rceil    |
| $\lfloor$ | lfloor   |
| $\rfloor$ | rfloor   |
| $\to$     | to       |
| $\bar{x}$ | bar(x)   | #latex_func.json
| $\dot{x}$ | dot(x)   |
| $\ddot{x}$| ddot(x)  |
| $\vec{x}$ | vec(x)   |
| $\widehat{x}$| widehat(x)|
| $\text{text}$| text(text)|
| $a^x$    | a^(x)    |
| $a_x$    | a_(x)    |
| $\int{x}$ | int(x)   |
| $\int_{a}^{b}{x}$| _int(a)(b)(x)|
| $\sum_{a}^{b}{x}$| sum(a)(b)(x)|
| $\prod_{a}^{b}{x}$| prod(a)(b)(x)|
| $\lim_{x \to 2}{x}$| lim(x to 2)(x)|
| $\frac{a}{b}$| frac(a)(b)|
| $\sqrt{x}$| sqrt(x)  |
| $\sqrt[n]{x}$| rt\[n\](x)|
| $\begin{matrix}a&b\\c&d\end{matrix}$| matrix(a & b \\\\ c & d)|
| $\begin{pmatrix}a&b\\c&d\end{pmatrix}$| pmatrix(a & b \\\\ c & d)|
| $\begin{bmatrix}a&b\\c&d\end{bmatrix}$| bmatrix(a & b \\\\ c & d)|
| $\begin{Bmatrix}a&b\\c&d\end{Bmatrix}$| Bmatrix(a & b \\\\ c & d)|
| $\begin{vmatrix}a&b\\c&d\end{vmatrix}$| vmatrix(a & b \\\\ c & d)|
| $\begin{Vmatrix}a&b\\c&d\end{Vmatrix}$| Vmatrix(a & b \\\\ c & d)|
| $\begin{cases}a&b\\c&d\end{cases}$| cases(a & b \\\\ c & d)|
| $\begin{rcases}a&b\\c&d\end{rcases}$| rcases(a & b \\\\ c & d)|
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