import gradio as gr
import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# LaTeX formatted function names for display
latex_function_labels = {
    "sin(x)": r"$\sin(x)$",
    "cos(x)": r"$\cos(x)$",
    "x^2": r"$x^2$",
    "e^x": r"$e^x$",
    "log(x)": r"$\log(x)$",
    "tan(x)": r"$\tan(x)$",
    "sin(x^2)": r"$\sin(x^2)$",
    "cos(x^2)": r"$\cos(x^2)$",
    "sin(x)/x": r"$\frac{\sin(x)}{x}$",
    "sin(x) * cos(x)": r"$\sin(x) \cdot \cos(x)$",
    "e^(-x^2)": r"$e^{-x^2}$",
    "e^(sin(x))": r"$e^{\sin(x)}$",
    "log(1 + x)": r"$\log(1 + x)$",
    "log(x^2 + 1)": r"$\log(x^2 + 1)$",
    "x * e^(-x)": r"$x e^{-x}$",
    "x^3 - 2x^2 + x": r"$x^3 - 2x^2 + x$",
    "x^4 + 3x^3 - 2x + 1": r"$x^4 + 3x^3 - 2x + 1$",
    "1 / (1 + x^2)": r"$\frac{1}{1 + x^2}$",
    "1 / (x^2 + 1e-8)": r"$\frac{1}{x^2 + 10^{-8}}$",
    "sqrt(x)": r"$\sqrt{x}$",
    "sinc(x)": r"$\text{sinc}(x)$",
    "exp(-x) * sin(x)": r"$e^{-x} \sin(x)$",
    "exp(-x^2) * cos(x)": r"$e^{-x^2} \cos(x)$",
    "sin(x) / sqrt(x + 1e-8)": r"$\frac{\sin(x)}{\sqrt{x + 10^{-8}}}$",
    "x * sin(x)": r"$x \sin(x)$",
    "abs(x)": r"$|x|$",
    "x * (x > 0)": r"$x \cdot \Theta(x)$",
    "sin(x) * (x > 0)": r"$\sin(x) \cdot \Theta(x)$",
}

# Reverse lookup for function names
latex_to_function_name = {v: k for k, v in latex_function_labels.items()}

# Function dictionary
function_dict = {
    key: eval("lambda x: " + key.replace("^", "**").replace("log", "np.log").replace("e^", "np.exp").replace("sin", "np.sin").replace("cos", "np.cos").replace("tan", "np.tan").replace("sqrt", "np.sqrt").replace("sinc", "np.sinc").replace("abs", "np.abs"))
    for key in latex_function_labels
}

# Function selection logic
def function_selection(selection_type, selected_function, custom_function):
    if selection_type == "Predefined":
        latex_equation = latex_function_labels[selected_function]
        return f"**Selected Function:**\n\n{latex_equation}", function_dict[selected_function]
    elif selection_type == "Custom":
        try:
            func = eval(f"lambda x: {custom_function}", {"np": np})
            return f"**Custom Function:**\n\n`{custom_function}`", func
        except:
            return "**Invalid function syntax!** Use `x` and NumPy functions like `np.sin(x)`.", None

# Gradio Interface
with gr.Blocks() as demo:
    function_type = gr.Radio(["Predefined", "Custom"], label="Function Type", value="Predefined")
    
    function_dropdown = gr.Dropdown(choices=list(latex_function_labels.keys()), label="Choose a Function", value="sin(x)")
    custom_function_input = gr.Textbox(label="Enter Custom Function (if selected)", visible=False)

    function_display = gr.Markdown("**Selected Function:** ")

    function_type.change(lambda t: (function_dropdown.update(visible=t=="Predefined"),
                                     custom_function_input.update(visible=t=="Custom")),
                         inputs=[function_type], outputs=[function_dropdown, custom_function_input])

    function_dropdown.change(function_selection, inputs=[function_type, function_dropdown, custom_function_input], outputs=[function_display])
    custom_function_input.change(function_selection, inputs=[function_type, function_dropdown, custom_function_input], outputs=[function_display])

    gr.Interface(fn=function_selection, inputs=[function_type, function_dropdown, custom_function_input], outputs=[function_display])

demo.launch()
