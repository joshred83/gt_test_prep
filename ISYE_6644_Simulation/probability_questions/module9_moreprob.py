exercise_pdfs = {
    'question': (
        "Let $X$ be a continuous random variable with a PDF of the form:\n"
        "\\[ f_X(x) = \\begin{cases} c(1 - x), & \\text{if } x \\in [0, 1], \\\\ 0, & \\text{otherwise}. \\end{cases} \\]\n"
        "Find the following values:\n"
        "1. $c$.\n"
        "2. $P(X = 1/2)$.\n"
        "3. $P(X \\in \\{1/k : k \\text{ integer, } k \\geq 2\\})$.\n"
        "4. $P(X \\leq 1/2)$."
    ),
    'options_list': [
        "1. $c = 2$, $P(X = 1/2) = 0$, $P(X \\in \\{1/k : k \\geq 2\\}) = 0$, $P(X \\leq 1/2) = 3/4$.",
        "2. $c = 1$, $P(X = 1/2) = 1/4$, $P(X \\in \\{1/k : k \\geq 2\\}) = 1/2$, $P(X \\leq 1/2) = 1/2$.",
        "3. $c = 2$, $P(X = 1/2) = 1$, $P(X \\in \\{1/k : k \\geq 2\\}) = 0$, $P(X \\leq 1/2) = 1/2$.",
        "4. $c = 3$, $P(X = 1/2) = 0$, $P(X \\in \\{1/k : k \\geq 2\\}) = 1$, $P(X \\leq 1/2) = 3/4$."
    ],
    'correct_answer': (
        "1. $c = 2$, $P(X = 1/2) = 0$, $P(X \\in \\{1/k : k \\geq 2\\}) = 0$, $P(X \\leq 1/2) = 3/4$."
    ),
    'explanation': (
        "1. **Finding $c$**: Normalize the PDF such that the integral over all $x$ equals 1:\n"
        "\\[ \\int_{-\\infty}^\\infty f_X(x) dx = \\int_0^1 c(1 - x) dx = c \\int_0^1 (1 - x) dx = c \\left[x - \\frac{x^2}{2} \\right]_0^1 = c \\cdot \\frac{1}{2}. \\]\n"
        "Solving for $c$, we find $c = 2$.\n\n"
        "2. **$P(X = 1/2)$**: For a continuous random variable, the probability of a specific point is zero:\n"
        "\\[ P(X = 1/2) = 0. \\]\n\n"
        "3. **$P(X \\in \\{1/k : k \\geq 2\\})$**: Using countable additivity and the fact that single points have zero probability:\n"
        "\\[ P\\left(X \\in \\left\\{\\frac{1}{k} : k \\geq 2\\right\\}\\right) = \\sum_{k=2}^\\infty P\\left(X = \\frac{1}{k}\\right) = 0. \\]\n\n"
        "4. **$P(X \\leq 1/2)$**: Compute the cumulative probability:\n"
        "\\[ P(X \\leq 1/2) = \\int_{-\\infty}^{1/2} f_X(x) dx = \\int_0^{1/2} 2(1 - x) dx = 2 \\int_0^{1/2} (1 - x) dx = 2 \\left[x - \\frac{x^2}{2} \\right]_0^{1/2} = \\frac{3}{4}. \\]"
    ),
    'chapter_information': "MITx 6.431x Unit 5 Lesson 8"
}
