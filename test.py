import json
test = """Int(a)(b)(x)
u = 3 + x"""

latex_dict = {
    "alpha": "\\alpha",
    "beta": "\\beta",
    "gamma": "\\gamma",
    "delta": "\\delta",
    "epsilon": "\\epsilon",
    "zeta": "\\zeta",
    "eta": "\\eta",
    "theta": "\\theta",
    "iota": "\\iota",
    "kappa": "\\kappa",
    "lambda": "\\lambda",
    "mu": "\\mu",
    "nu": "\\nu",
    "xi": "\\xi",
    "omicron": "\\omicron",
    "pi": "\\pi",
    "rho": "\\rho",
    "sigma": "\\sigma",
    "tau": "\\tau",
    "upsilon": "\\upsilon",
    "phi": "\\phi",
    "chi": "\\chi",
    "psi": "\\psi",
    "omega": "\\omega",
    "Gamma": "\\Gamma",
    "Delta": "\\Delta",
    "Theta": "\\Theta",
    "Lambda": "\\Lambda",
    "Xi": "\\Xi",
    "Pi": "\\Pi",
    "Sigma": "\\Sigma",
    "Upsilon": "\\Upsilon",
    "Phi": "\\Phi",
    "Psi": "\\Psi",
    "Omega": "\\Omega",
    "infty": "\\infty",
    "forall": "\\forall",

    "(": "\\left(",
    ")": "\\right)",
    "[": "\\left[",
    "]": "\\right]",
    "{": "\\left{",
    "}": "\\right}",
    "lceil": "\\left\\lceil",
    "rceil": "\\right\\rceil",
    "lfloor": "\\left\\lfloor",
    "rfloor": "\\right\\rfloor",
    "labs": "\\left|",
    "rabs": "\\right|",

    "sin": "\\sin",
    "cos": "\\cos",
    "to" : "\\to",
    "approx": "\\approx",
    "neq": "\\neq",
    "equiv": "\\Leftrightarrow",
    "implies": "\\Rightarrow",
    "gequal": "\\geqslant",
    "lequal": "\\leqslant",
    "in_": "\\in",
    "notin": "\\notin",
    "subset": "\\subset"
}
latex_func = {
    "bar": ["\\bar{¤1}", 1],
    "dot": ["\\dot{¤1}", 1],
    "ddot": ["\\ddot{¤1}", 1],
    "vec": ["\\vec{¤1}", 1],
    "widehat": ["\\widehat{¤1}", 1],

    "text": ["\\text{¤1}", 1],
    "^": ["^{¤1}", 1],
    "_": ["_{¤1}", 1],

    "int": ["\\int{¤1}", 1],
    "Int": ["\\int_{¤1}^{¤2}{¤3}", 3],
    "sum": ["\\sum_{¤1}^{¤2}{¤3}", 3],
    "prod": ["\\prod_{¤1}^{¤2}{¤3}", 3],
    "lim": ["\\lim_{¤1}{¤2}", 2],
    "frac": ["\\frac{¤1}{¤2}", 2],
    "sqrt": ["\\sqrt{¤1}", 1],
    "rt": ["\\sqrt[¤1]{¤2}", 2],

    "matrix": ["\\begin{matrix}¤1\\end{matrix}", 1],
    "pmatrix": ["\\begin{pmatrix}¤1\\end{pmatrix}", 1],
    "bmatrix": ["\\begin{bmatrix}¤1\\end{bmatrix}", 1],
    "Bmatrix": ["\\begin{Bmatrix}¤1\\end{Bmatrix}", 1],
    "vmatrix": ["\\begin{vmatrix}¤1\\end{vmatrix}", 1],
    "Vmatrix": ["\\begin{Vmatrix}¤1\\end{Vmatrix}", 1],
    "cases": ["\\begin{cases}¤1\\end{cases}", 1],
    "rcases": ["\\begin{rcases}¤1\\end{rcases}", 1]
}

def evaluate_latex(text):
    latex = ""
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
                    else:
                        i += 1
                end = False
                text = text[i+1:]
                i = 0
                nb_args -= 1
            for i, arg in enumerate(arg_list):
                latex = latex.replace(f"¤{i+1}", arg)
            text = text[i:] #remove from text
            i = 0
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

print(evaluate_latex(test))