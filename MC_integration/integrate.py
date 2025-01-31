import numpy as np
import scipy.integrate as spi
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt


# Define function dictionary
function_dict = {
    "sin(x)": np.sin,
    "cos(x)": np.cos,
    "x^2": lambda x: x**2,
    "e^x": np.exp,
    "log(x)": lambda x: np.log(np.maximum(x, 1e-8)),  # Avoid log(0)
    "tan(x)": np.tan,
    "sin(x^2)": lambda x: np.sin(x**2),
    "cos(x^2)": lambda x: np.cos(x**2),
    "sin(x)/x": lambda x: np.sin(x) / np.where(x == 0, 1, x),  # Avoid division by zero
    "sin(x) * cos(x)": lambda x: np.sin(x) * np.cos(x),
    "e^(-x^2)": lambda x: np.exp(-(x**2)),  # Gaussian function
    "e^(sin(x))": lambda x: np.exp(np.sin(x)),
    "log(1 + x)": lambda x: np.log(1 + x),
    "log(x^2 + 1)": lambda x: np.log(x**2 + 1),
    "x * e^(-x)": lambda x: x * np.exp(-x),  # Exponential decay with linear term
    "x^3 - 2x^2 + x": lambda x: x**3 - 2 * x**2 + x,
    "x^4 + 3x^3 - 2x + 1": lambda x: x**4 + 3 * x**3 - 2 * x + 1,
    "1 / (1 + x^2)": lambda x: 1 / (1 + x**2),  # Lorentzian function
    "1 / (x^2 + 1e-8)": lambda x: 1 / (x**2 + 1e-8),  # Avoid division by zero
    "sqrt(x)": lambda x: np.sqrt(np.maximum(x, 0)),  # Avoid sqrt of negative numbers
    "sinc(x)": lambda x: np.sinc(x / np.pi),  # Normalized sinc function
    "exp(-x) * sin(x)": lambda x: np.exp(-x) * np.sin(x),  # Damped sine wave
    "exp(-x^2) * cos(x)": lambda x: np.exp(-(x**2)) * np.cos(x),  # Gaussian modulated cosine
    "sin(x) / sqrt(x + 1e-8)": lambda x: np.sin(x) / np.sqrt(np.maximum(x, 1e-8)),  # Avoid division by zero
    "x * sin(x)": lambda x: x * np.sin(x),  # Oscillatory function with increasing amplitude
    "abs(x)": np.abs,
    "x * (x > 0)": lambda x: x * (x > 0),  # Ramp function
    "sin(x) * (x > 0)": lambda x: np.sin(x) * (x > 0),  # Sinusoidal function for x > 0
}

# LaTeX formatted function names for dropdown display
latex_function_labels = {
    "sin(x)": "$\\sin(x)$",
    "cos(x)": "$\\cos(x)$",
    "x^2": "$x^2$",
    "e^x": "$e^x$",
    "log(x)": "$\\log(x)$",
    "tan(x)": "$\\tan(x)$",
    "sin(x^2)": "$\\sin(x^2)$",
    "cos(x^2)": "$\\cos(x^2)$",
    "sin(x)/x": "$\\frac{\\sin(x)}{x}$",
    "sin(x) * cos(x)": "$\\sin(x) \\cdot \\cos(x)$",
    "e^(-x^2)": "$e^{-x^2}$",
    "e^(sin(x))": "$e^{\\sin(x)}$",
    "log(1 + x)": "$\\log(1 + x)$",
    "log(x^2 + 1)": "$\\log(x^2 + 1)$",
    "x * e^(-x)": "$x e^{-x}$",
    "x^3 - 2x^2 + x": "$x^3 - 2x^2 + x$",
    "x^4 + 3x^3 - 2x + 1": "$x^4 + 3x^3 - 2x + 1$",
    "1 / (1 + x^2)": "$\\frac{1}{1 + x^2}$",
    "1 / (x^2 + 1e-8)": "$\\frac{1}{x^2 + 10^{-8}}$",
    "sqrt(x)": "$\\sqrt{x}$",
    "sinc(x)": "$\\text{sinc}(x)$",
    "exp(-x) * sin(x)": "$e^{-x} \\sin(x)$",
    "exp(-x^2) * cos(x)": "$e^{-x^2} \\cos(x)$",
    "sin(x) / sqrt(x + 1e-8)": "$\\frac{\\sin(x)}{\\sqrt{x + 10^{-8}}}$",
    "x * sin(x)": "$x \\sin(x)$",
    "abs(x)": "$|x|$",
    "x * (x > 0)": "$x \\cdot \\Theta(x)$",
    "sin(x) * (x > 0)": "$\\sin(x) \\cdot \\Theta(x)$",
}

# Reverse mapping so we can fetch function names from their LaTeX labels
latex_to_function_name = {v: k for k, v in latex_function_labels.items()}


class Integrator:
    def __init__(self, n, funct, limits):
        self.n = n
        self.function = funct
        self.a, self.b = limits[0], limits[1]

    def single_point_sampling(self):
        sample = np.random.uniform(self.a, self.b, 1)
        estimate = (self.b - self.a) * self.function(sample)
        return estimate

    def endpoint_sampling(self):
        fa = self.function(self.a)
        fb = self.function(self.b)
        estimate = (self.b - self.a) * (fa + fb) / 2
        return estimate

    def overlapping_intervals(self):
        interval_size = (self.b - self.a) / self.n
        samples = np.array([np.random.uniform(self.a + i * interval_size, self.a + (i + 1.5) * interval_size) for i in range(self.n)])
        vals = self.function(samples)
        estimate = (self.b - self.a) * np.mean(vals)
        return estimate

    def classic_monte_carlo(self):
        samples = np.random.uniform(self.a, self.b, self.n)
        vals = self.function(samples)
        estimate = (self.b - self.a) * np.mean(vals)
        return estimate

    def trapezoidal_rule(self):
        x = np.linspace(self.a, self.b, self.n)
        y = self.function(x)
        estimate = np.trapz(y, x)
        return estimate

    def simpsons_rule(self):
        x = np.linspace(self.a, self.b, self.n)
        y = self.function(x)
        estimate = spi.simpson(y, x=x)  
        return estimate

    def midpoint_rule(self):
        x = np.linspace(self.a, self.b, self.n)
        midpoints = (x[:-1] + x[1:]) / 2
        y = self.function(midpoints)
        estimate = np.sum(y) * (self.b - self.a) / (self.n - 1)
        return estimate

    def scipy_integrate(self):
        result, _ = spi.quad(self.function, self.a, self.b)
        return result

    def stratified_sampling(self):
        strata = np.linspace(self.a, self.b, self.n + 1)
        samples = np.concatenate([np.random.uniform(strata[i], strata[i+1], 1) for i in range(self.n)])
        vals = self.function(samples)
        estimate = (self.b - self.a) * np.mean(vals)
        return estimate

    def latin_hypercube_sampling(self):
        sub_intervals = np.linspace(self.a, self.b, self.n + 1)
        samples = np.array([np.random.uniform(sub_intervals[i], sub_intervals[i+1]) for i in range(self.n)])
        np.random.shuffle(samples)  # Shuffle to randomize order
        vals = self.function(samples)
        estimate = (self.b - self.a) * np.mean(vals)
        return estimate

    def adaptive_monte_carlo(self, tol=1e-4):
        def recursive_integrate(a, b, n, tol):
            samples = np.random.uniform(a, b, n)
            vals = self.function(samples)
            estimate = (b - a) * np.mean(vals)
            error = np.std(vals) / np.sqrt(n)
            if error < tol:
                return estimate
            else:
                mid = (a + b) / 2
                return recursive_integrate(a, mid, n // 2, tol) + recursive_integrate(mid, b, n // 2, tol)
        return recursive_integrate(self.a, self.b, self.n, tol)



def plot_function_and_approximations(f, a, b, n, selected_methods, integrator):
    x_vals = np.linspace(a, b, 1000)
    y_vals = f(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label="True Function", color="black", linewidth=2, alpha=0.7)

    # Define color scheme using "tab10" colormap
    cmap = plt.get_cmap("tab10")
    method_colors = {method: cmap(i) for i, method in enumerate(selected_methods)}

    method_linewidths = {
        "Endpoint Sampling": 1.5,
        "Overlapping Intervals": 1.5,
        "Classic Monte Carlo": 1.5,
        "Trapezoidal Rule": 2.0,
        "Simpson's Rule": 2.5,
        "Midpoint Rule": 2.0,
        "Stratified Sampling": 1.5,
        "Latin Hypercube Sampling": 1.5,
        "Adaptive Monte Carlo": 2.5
    }

    for method in selected_methods:
        if method in method_linewidths:
            color = method_colors[method]
            linewidth = method_linewidths[method]

            x_approx = np.linspace(a, b, n)
            y_approx = [integrator.function(x) for x in x_approx]
            ax.plot(x_approx, y_approx, color=color, linewidth=linewidth, label=method, alpha=0.68)

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Function and Approximations")
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.5)

    return fig

def integrate_and_compare(selected_function, a, b, n, selected_methods):
    function_str = latex_to_function_name[selected_function]
    f = function_dict[function_str]
    integrator = Integrator(n, f, (a, b))

    true_value = integrator.scipy_integrate()
    results = {}

    method_mapping = {
        "Endpoint Sampling": integrator.endpoint_sampling,
        "Overlapping Intervals": integrator.overlapping_intervals,
        "Classic Monte Carlo": integrator.classic_monte_carlo,
        "Trapezoidal Rule": integrator.trapezoidal_rule,
        "Simpson's Rule": integrator.simpsons_rule,
        "Midpoint Rule": integrator.midpoint_rule,
        "Stratified Sampling": integrator.stratified_sampling,
        "Latin Hypercube Sampling": integrator.latin_hypercube_sampling,
        "Adaptive Monte Carlo": integrator.adaptive_monte_carlo
    }

    for method in selected_methods:
        estimate = method_mapping[method]()
        results[method] = {
            "estimate": estimate,
            "error": abs(estimate - true_value)
        }

    output = f"**True Value (SciPy Quad):** {true_value:.6f}\n\n"
    for method, data in results.items():
        output += f"**{method}:**\n  - Estimate: {data['estimate']:.6f}\n  - Error: {data['error']:.6f}\n\n"

    return output, plot_function_and_approximations(f, a, b, n, selected_methods, integrator)

# Add MathJax support for LaTeX rendering in the header
iface = gr.Blocks(
    title="Numerical Integration Visualization",
    head='''<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
            <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>'''
)

with iface:
    gr.Markdown("# Numerical Integration Visualization")
    gr.Markdown("Select a function and compare different numerical integration methods.")
    
    with gr.Row():
        with gr.Column(scale=1):
            # LaTeX-rendered radio buttons using HTML/MathJax
            gr.Markdown("### Function Selection")
            function_radio = gr.Radio(
                choices=[f"\({label}\)" for label in latex_function_labels.values()],
                label="Choose a Function",
                elem_id="latex-radio",
                value=list(latex_function_labels.values())[0]  # Set first as default
            )
            
            gr.Markdown("### Integration Parameters")
            a_input = gr.Number(value=0, label="Lower limit (a)")
            b_input = gr.Number(value=np.pi, label="Upper limit (b)")
            n_slider = gr.Slider(10, 1000, value=32, step=1, 
                               label="Number of intervals (n)")
            
        with gr.Column(scale=1):
            gr.Markdown("### Integration Methods")
            methods_group = gr.CheckboxGroup(
                [
                    "Endpoint Sampling",
                    "Overlapping Intervals",
                    "Classic Monte Carlo",
                    "Trapezoidal Rule",
                    "Simpson's Rule",
                    "Midpoint Rule",
                    "Stratified Sampling",
                    "Latin Hypercube Sampling",
                    "Adaptive Monte Carlo"
                ],
                value=["Classic Monte Carlo", "Trapezoidal Rule"],
                label="Select methods to compare"
            )
    
    # Add a dedicated calculate button
    calculate_btn = gr.Button("Calculate Integrals", variant="primary")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Integration Results")
            results_output = gr.Textbox(label="", show_label=False)
        with gr.Column(scale=2):
            gr.Markdown("### Function Visualization")
            plot_output = gr.Plot(label="Function Plot")

    # Connect components
    calculate_btn.click(
        integrate_and_compare,
        inputs=[function_radio, a_input, b_input, n_slider, methods_group],
        outputs=[results_output, plot_output]
    )

# Add custom CSS for better LaTeX rendering
iface.css = '''
#latex-radio .gr-radio-item label {
    font-size: 1.1em;
    padding: 8px 12px;
    margin: 4px 0;
    border-radius: 4px;
    border: 1px solid #e0e0e0;
    transition: all 0.2s;
}

#latex-radio .gr-radio-item label:hover {
    background: #f5f5f5;
    border-color: #cccccc;
}

#latex-radio .gr-radio-item input:checked + label {
    background: #e3f2fd;
    border-color: #2196f3;
}
'''

iface.launch()

# # Gradio Interface
# iface = gr.Interface(
#     fn=integrate_and_compare,
#     inputs=[
#         gr.Radio(choices=list(latex_function_labels.values()), label="Choose a Function"),
#         gr.Number(value=0, label="Lower Limit (a)"),
#         gr.Number(value=np.pi, label="Upper Limit (b)"),
#         gr.Slider(10, 1000, value=32, label="Number of Intervals (n)"),  # Default to 32
#         gr.CheckboxGroup(
#             [
#                 "Endpoint Sampling",
#                 "Overlapping Intervals",
#                 "Classic Monte Carlo",
#                 "Trapezoidal Rule",
#                 "Simpson's Rule",
#                 "Midpoint Rule",
#                 "Stratified Sampling",
#                 "Latin Hypercube Sampling",
#                 "Adaptive Monte Carlo"
#             ],
#             label="Integration Methods",
#             value=["Classic Monte Carlo", "Trapezoidal Rule"]
#         ),
#     ],
#     outputs=[
#         gr.Textbox(label="Integration Results"),
#         gr.Plot(label="Function and Approximations"),
#     ],
#     title="Numerical Integration Visualization",
#     description="Select a function and compare different numerical integration methods.",
# )

# iface.launch()

