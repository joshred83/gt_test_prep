linear_regression_assumptions = {
    'question': (
        "Assume that we are given a collection of $n$ points $\\{(x_i, y_i)\\}_{i=1}^n$. "
        "Which one of the following choices, on its own, provides a sufficient condition under which a unique least-squares estimator "
        "$(\\hat{a}, \\hat{b})$ exists?\n\n"
        "(A) There are at least two total observations; i.e., $(n \\geq 2)$.\n"
        "(B) There are at least two distinct $x$'s in the collection; i.e., $x_1 \\neq x_2$.\n"
        "(C) There are at least two distinct $y$'s in the collection; i.e., $y_1 \\neq y_2$."
    ),
    'options_list': ['(A)', '(B)', '(C)'],
    'correct_answer': "(B) There are at least two distinct $x$'s in the collection; i.e., $x_1 \\neq x_2$.",
    'explanation': (
        "The correct choice is **(B) There are at least two distinct $x$'s in the collection; i.e., $x_1 \\neq x_2$**. "
        "If all the $x$'s are equal (e.g., $x_1 = \\dots = x_n$), the empirical variance is zero, and there is no unique solution for the least-squares estimator."
    ),
    'chapter_information': 'MITx 18.6501x Fundamentals of Statistics - Linear Regression'
}

linear_regression_numerical_example = {
    'question': (
        "Consider the four points $(x_1, y_1) = (-5, -10)$, $(x_2, y_2) = (0, 3)$, $(x_3, y_3) = (2, 11)$, "
        "and $(x_4, y_4) = (3, 14)$. The line that minimizes the empirical squared error can be expressed as:\n"
        "$y = \\hat{a} + \\hat{b}x$.\n\n"
        "Find the values of $\\hat{a}$ and $\\hat{b}$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "$\\hat{a} = 4.5, \\; \\hat{b} = 3$."
    ),
    'explanation': (
        "We compute the slope $\\hat{b}$ using:\n"
        "$$\n"
        "\\hat{b} = \\frac{\\sum_{i=1}^n (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum_{i=1}^n (x_i - \\bar{x})^2}\n"
        "$$\n"
        "and then calculate $\\hat{a} = \\bar{y} - \\hat{b}\\bar{x}$. "
        "Using the given points, $\\bar{x} = 0$ and $\\bar{y} = 4.5$, leading to $\\hat{b} = 3$ and $\\hat{a} = 4.5$."
    ),
    'chapter_information': 'MITx 18.6501x Fundamentals of Statistics - Linear Regression'
}

linear_regression_goal = {
    'question': (
        "Which one of the following best represents the goal(s) of linear regression?\n\n"
        "(A) Given data points $\\{(X_i, Y_i)\\}$, try to explain **why** $Y$ is changing depending on $X$.\n"
        "(B) Given data points $\\{(X_i, Y_i)\\}$, fit a model and try to **predict** $Y$ given a value for $X$.\n"
        "(C) Given data points $\\{(X_i, Y_i)\\}$, **prove** that the relationship between $Y$ and $X$ is linear.\n"
        "(D) Given data points $\\{(X_i, Y_i)\\}$, obtain the **functional relationship** between $Y$ and $X$."
    ),
    'options_list': ['(A)', '(B)', '(C)', '(D)'],
    'correct_answer': "(B) Given data points $\\{(X_i, Y_i)\\}$, fit a model and try to **predict** $Y$ given a value for $X$.",
    'explanation': (
        "The main goal of linear regression is to predict $Y$ given a value of $X$, by fitting a model to the data. "
        "It does not aim to explain 'why' (causal relationships) or rigorously prove a linear relationship."
    ),
    'chapter_information': 'MITx 18.6501x Fundamentals of Statistics - Linear Regression'
}

linear_regression_assumption = {
    'question': (
        "Assume that we are given a collection of \( n \) points \\( \\{(x_i, y_i)\\}_{i=1}^n \\). "
        "Which one of the following choices, on its own, provides a sufficient condition under which a unique least-squares estimator "
        "\\( (\\hat{a}, \\hat{b}) \\) exists?\n\n"
        "1. There are at least two total observations; i.e., \( n \\geq 2 \).\n"
        "2. There are at least two distinct \( x \)'s in the collection; i.e., \( x_1 \\neq x_2 \).\n"
        "3. There are at least two distinct \( y \)'s in the collection; i.e., \( y_1 \\neq y_2 \)."
    ),
    'options_list': [
        "There are at least two total observations; i.e., \( n \\geq 2 \).",
        "There are at least two distinct \( x \)'s in the collection; i.e., \( x_1 \\neq x_2 \).",
        "There are at least two distinct \( y \)'s in the collection; i.e., \( y_1 \\neq y_2 \)."
    ],
    'correct_answer': "There are at least two distinct \( x \)'s in the collection; i.e., \( x_1 \\neq x_2 \).",
    'explanation': (
        "The correct condition for the existence of a unique least-squares estimator is that the collection "
        "of points must include at least two distinct \( x \)-values. If all \( x \)-values are equal, the empirical variance "
        "is zero, and an infinite number of lines can minimize the squared error. In this case, any line crossing \( (\\bar{x}, \\bar{y}) \\) "
        "is a minimizer regardless of its slope."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

linear_regression_goal = {
    'question': (
        "Which one of the following best represents the goal(s) of linear regression?\n\n"
        "1. Given data points \\( \\{(X_i, Y_i)\\} \\), try to explain why \( Y \) is changing depending on \( X \).\n"
        "2. Given data points \\( \\{(X_i, Y_i)\\} \\), fit a model and try to predict \( Y \) given a value for \( X \).\n"
        "3. Given data points \\( \\{(X_i, Y_i)\\} \\), prove that the relationship between \( Y \) and \( X \) is linear.\n"
        "4. Given data points \\( \\{(X_i, Y_i)\\} \\), obtain the functional relationship between \( Y \) and \( X \)."
    ),
    'options_list': [
        "Given data points \\( \\{(X_i, Y_i)\\} \\), try to explain why \( Y \) is changing depending on \( X \).",
        "Given data points \\( \\{(X_i, Y_i)\\} \\), fit a model and try to predict \( Y \) given a value for \( X \).",
        "Given data points \\( \\{(X_i, Y_i)\\} \\), prove that the relationship between \( Y \) and \( X \) is linear.",
        "Given data points \\( \\{(X_i, Y_i)\\} \\), obtain the functional relationship between \( Y \) and \( X \)."
    ],
    'correct_answer': "Given data points \\( \\{(X_i, Y_i)\\} \\), fit a model and try to predict \( Y \) given a value for \( X \).",
    'explanation': (
        "The main goal of linear regression is to fit a model to the data points \\( \\{(X_i, Y_i)\\} \\) and predict \( Y \) for a given \( X \). "
        "Linear regression focuses on correlations between variables, not causation or exact functional relationships."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

conditional_variance_question = {
    'question': (
        "Consider a joint density setup \( h(x, y) = x + y \) over the space \( [0, 1]^2 \). "
        "What is the variance of \( Y \) given \( X = x \)?"
    ),
    'options_list': [
        "\\( \\text{Var}(Y|X=x) = \\frac{(6x^2 + 2 \\cdot 6x + 1)}{18(2x+1)^2} \\)",
        "\\( \\text{Var}(Y|X=x) = \\frac{(x/3 + 1/4)}{(0.5 + x)} - \\left( \\frac{x/2 + 1/3}{(0.5 + x)} \\right)^2 \\)",
        "\\( \\text{Var}(Y|X=x) = \\frac{2x+1}{12} \\)",
        "\\( \\text{Var}(Y|X=x) = \\frac{y^0}{(2x+1)^2} \\)"
    ],
    'correct_answer': "\\( \\text{Var}(Y|X=x) = \\frac{(x/3 + 1/4)}{(0.5 + x)} - \\left( \\frac{x/2 + 1/3}{(0.5 + x)} \\right)^2 \\)",
    'explanation': (
        "The conditional variance of \( Y \) given \( X = x \) is obtained using the conditional density "
        "\\( h(y|x) \\), which is the ratio of the joint density to the marginal density of \( X \). The expectations "
        "\\( E[Y|X=x] \\) and \\( E[Y^2|X=x] \\) are computed first, and the variance is then calculated as "
        "\\( \\text{Var}(Y|X=x) = E[Y^2|X=x] - (E[Y|X=x])^2 \\)."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

linear_model_expectation = {
    'question': (
        "Assume \( (X, Y) \) is a pair such that \( Y = 3X + 5 + \epsilon \), where \( \\epsilon \\sim \\mathcal{N}(0, 1) \\) and "
        "\\( X \\) is independent of \( \\epsilon \\). What is \\( E[Y|X = x] \\)?"
    ),
    'options_list': [
        "\\( 3x \\)",
        "\\( 5 + x \\)",
        "\\( 3x + 5 \\)",
        "\\( E[Y] \\)"
    ],
    'correct_answer': "\\( 3x + 5 \\)",
    'explanation': (
        "By the definition of conditional expectation, we know that \( E[Y|X=x] = E[3X + 5 + \\epsilon | X = x] \\). "
        "Using linearity of expectation and the fact that \( E[\\epsilon] = 0 \), the result simplifies to \( 3x + 5 \\)."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

concept_check_quantile = {
    'question': (
        "Let \( (X, Y) \) be a pair of random variables with joint density \( f(x, y) = x + y \\) over the space \( [0, 1]^2 \\). "
        "For a given \( x \), what is the conditional \\( (1 - \\alpha) \\)-quantile function of \( Y \\) given \( X = x \\)?"
    ),
    'options_list': [
        "\\( q_{\\alpha}(x) = \\frac{1}{2}(-2x + \\sqrt{4x^2 + 8(1 - \\alpha)(x + 0.5)}) \\)",
        "\\( q_{\\alpha}(x) = x + 1 \\)",
        "\\( q_{\\alpha}(x) = 0.5 \\cdot x \\)",
        "\\( q_{\\alpha}(x) = x^2 + \\alpha \\)"
    ],
    'correct_answer': "\\( q_{\\alpha}(x) = \\frac{1}{2}(-2x + \\sqrt{4x^2 + 8(1 - \\alpha)(x + 0.5)}) \\)",
    'explanation': (
        "To find the conditional \\( (1 - \\alpha) \\)-quantile function of \( Y \\) given \( X = x \\), "
        "we solve for the quantile using the conditional density \( h(y|x) = \\frac{x + y}{x + 0.5} \\). "
        "Integrating this density and solving for \( y \\) provides the given quantile function."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

minimization_problem = {
    'question': (
        "Let \( X \) be a random variable with mean \( \\mu \) and variance \( \\sigma^2 \\). "
        "Which scalar \( k \) uniquely minimizes the function \\( f(k) = E[(X - k)^2] \\)?"
    ),
    'options_list': [
        "\\( k = \\mu \\)",
        "\\( k = \\sigma \\)",
        "\\( k = \\sigma^2 \\)",
        "\\( k = 0 \\)"
    ],
    'correct_answer': "\\( k = \\mu \\)",
    'explanation': (
        "The function \( f(k) = E[(X - k)^2] \\) is minimized when \( k \\) is the mean of \( X \\), i.e., \( k = E[X] = \\mu \\). "
        "This can be derived by differentiating \( f(k) \\) with respect to \( k \\) and solving for the critical point."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

estimator_minimizer = {
    'question': (
        "Let \( (X, Y) \) be a pair of random variables for which the regression function "
        "\\( \\nu(x) = E[Y | X = x] \\) takes the form \\( \\nu(x) = a + bX \\). "
        "What is the random variable \\( \\hat{Y} \\) that minimizes \\( E[(Y - \\hat{Y})^2 | X = x] \\)?"
    ),
    'options_list': [
        "\\( \\hat{Y} = a + bX \\)",
        "\\( \\hat{Y} = a + b \\)",
        "\\( \\hat{Y} = X \\)",
        "\\( \\hat{Y} = 0 \\)"
    ],
    'correct_answer': "\\( \\hat{Y} = a + bX \\)",
    'explanation': (
        "The regression function \( \\nu(x) = E[Y | X = x] \\) minimizes the mean squared error given \( X = x \\). "
        "If the regression function takes the form \( a + bX \\), the best predictor is \( \\hat{Y} = a + bX \\)."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

linear_regression_assumption_false = {
    'question': (
        "In theoretical linear regression, which of the following statements is false?\n\n"
        "1. There is an infinite family of solutions \( (a, b) \\) that minimize the squared mean error, "
        "\\( E[(Y - a - bX)^2] \\).\n"
        "2. There is no line \( y = a + bx \\) that predicts \( Y \\) given \( X \\) with probability 1, regardless of their distribution.\n"
        "3. With probability equal to 1, the random pair \( (X, Y) \\) lies on the vertical line \( x = E[X] \\)."
    ),
    'options_list': [
        "There is an infinite family of solutions \( (a, b) \\) that minimize the squared mean error.",
        "There is no line \( y = a + bx \\) that predicts \( Y \\) given \( X \\) with probability 1, regardless of their distribution.",
        "With probability equal to 1, the random pair \( (X, Y) \\) lies on the vertical line \( x = E[X] \\)."
    ],
    'correct_answer': "There is no line \( y = a + bx \\) that predicts \( Y \\) given \( X \\) with probability 1, regardless of their distribution.",
    'explanation': (
        "The statement that 'there is no line \( y = a + bx \\) that predicts \( Y \\) given \( X \\) with probability 1' is false. "
        "For deterministic data (when \( X \\) is constant), \( Y \\) can always be perfectly predicted by a constant line. "
        "The other two statements are true when \( \\text{Var}(X) = 0 \\)."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}


derivation_linear_regression_I = {
    'question': (
        "In deriving the theoretical linear least squares regression, assume \\( \\text{Var}(X) \\neq 0 \\). "
        "The regression of \\( Y \\) on \\( X \\) minimizes \\( E[(Y - a - bX)^2] \\). "
        "What are the partial derivatives \\( \\partial_a f \\) and \\( \\partial_b f \\) of this expression with respect to \\( a \\) and \\( b \\)?"
    ),
    'options_list': [
        "\\( \\partial_a f = E[-2Y + 2a + 2bX] \\) and \\( \\partial_b f = E[-2XY + 2aX + 2bX^2] \\)",
        "\\( \\partial_a f = E[-Y + a + bX] \\) and \\( \\partial_b f = E[-XY + aX + bX^2] \\)",
        "\\( \\partial_a f = E[Y - a - bX] \\) and \\( \\partial_b f = E[XY - aX - bX^2] \\)",
        "\\( \\partial_a f = E[2Y - 2a - 2bX] \\) and \\( \\partial_b f = E[2XY - 2aX - 2bX^2] \\)"
    ],
    'correct_answer': "\\( \\partial_a f = E[-2Y + 2a + 2bX] \\) and \\( \\partial_b f = E[-2XY + 2aX + 2bX^2] \\)",
    'explanation': (
        "The partial derivatives are obtained by differentiating \\( E[(Y - a - bX)^2] \\) with respect to \\( a \\) and \\( b \\), "
        "applying the chain rule. The derivatives simplify to \\( \\partial_a f = E[-2Y + 2a + 2bX] \\) and \\( \\partial_b f = E[-2XY + 2aX + 2bX^2] \\)."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

derivation_linear_regression_II = {
    'question': (
        "In theoretical linear regression, we solve the system of equations:\n\n"
        "1. \\( E[Y] = a + E[X]b \\)\n"
        "2. \\( E[XY] = E[X]a + E[X^2]b \\).\n\n"
        "What is the solution for \\( b \\) (slope) and \\( a \\) (intercept)?"
    ),
    'options_list': [
        "\\( b = \\text{Cov}(X, Y) / \\text{Var}(X), a = E[Y] - bE[X] \\)",
        "\\( b = \\text{Var}(X) / \\text{Cov}(X, Y), a = E[Y] + bE[X] \\)",
        "\\( b = E[XY] / E[X^2], a = E[Y] \\)",
        "\\( b = E[Y] / E[X], a = 0 \\)"
    ],
    'correct_answer': "\\( b = \\text{Cov}(X, Y) / \\text{Var}(X), a = E[Y] - bE[X] \\)",
    'explanation': (
        "By solving the normal equations derived from minimizing the mean squared error, we find:\n"
        "\\( b = \\text{Cov}(X, Y) / \\text{Var}(X) \\) and \\( a = E[Y] - bE[X] \\). "
        "These values minimize the mean squared error in theoretical linear regression."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

assumptions_linear_regression = {
    'question': (
        "Which of the following statements is false in theoretical linear regression if \\( \\text{Var}(X) = 0 \\)?\n\n"
        "1. There is an infinite family of solutions \\( (a, b) \\) that minimize the squared mean error.\n"
        "2. There is no line \\( y = a + bx \\) that predicts \\( Y \\) given \\( X \\) with probability 1.\n"
        "3. With probability 1, the random pair \\( (X, Y) \\) lies on the vertical line \\( x = E[X] \\)."
    ),
    'options_list': [
        "There is an infinite family of solutions \\( (a, b) \\) that minimize the squared mean error.",
        "There is no line \\( y = a + bx \\) that predicts \\( Y \\) given \\( X \\) with probability 1.",
        "With probability 1, the random pair \\( (X, Y) \\) lies on the vertical line \\( x = E[X] \\)."
    ],
    'correct_answer': "There is no line \\( y = a + bx \\) that predicts \\( Y \\) given \\( X \\) with probability 1.",
    'explanation': (
        "If \\( \\text{Var}(X) = 0 \\), the random variable \\( X \\) takes a constant value. "
        "In this case, the line \\( y = a + bx \\) can perfectly predict \\( Y \\) since \\( X \\) does not vary. "
        "Thus, this statement is false."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

conditional_quantile = {
    'question': (
        "Let \\( (X, Y) \\) be a pair of random variables with joint density \\( f(x, y) = x + y \\) over the space \\( [0, 1]^2 \\). "
        "What is the conditional \\( (1 - \\alpha) \\)-quantile function of \\( Y \\) given \\( X = x \\)?"
    ),
    'options_list': [
        "\\( q_{\\alpha}(x) = x + \\alpha \\)",
        "\\( q_{\\alpha}(x) = 1/2(-2x + \\sqrt{4x^2 + 8(1 - \\alpha)(x + 0.5)}) \\)",
        "\\( q_{\\alpha}(x) = x \\cdot \\alpha \\)",
        "\\( q_{\\alpha}(x) = \\alpha + 0.5 \\cdot x \\)"
    ],
    'correct_answer': "\\( q_{\\alpha}(x) = 1/2(-2x + \\sqrt{4x^2 + 8(1 - \\alpha)(x + 0.5)}) \\)",
    'explanation': (
        "The conditional quantile function is derived by integrating the conditional density "
        "\\( h(y|x) = \\frac{x + y}{x + 0.5} \\) and solving for \\( y \\) such that the cumulative distribution equals \\( 1 - \\alpha \\)."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}

regression_function = {
    'question': (
        "Given a joint probability distribution \\( P \\) for the random pair \\( (X, Y) \\), the regression function of \\( Y \\) with respect to \\( X \\) is defined as:"
    ),
    'options_list': [
        "\\( \\nu(x) = E[Y | X = x] \\)",
        "\\( \\nu(x) = P(Y = y | X = x) \\)",
        "\\( \\nu(x) = \\text{Cov}(X, Y) / \\text{Var}(X) \\)",
        "\\( \\nu(x) = E[X | Y = y] \\)"
    ],
    'correct_answer': "\\( \\nu(x) = E[Y | X = x] \\)",
    'explanation': (
        "The regression function \\( \\nu(x) \\) is defined as the conditional expectation of \\( Y \\) given \\( X = x \\), "
        "i.e., \\( \\nu(x) = E[Y | X = x] \\). This function represents the best predictor of \\( Y \\) given \\( X \\) in the mean squared error sense."
    ),
    'chapter_information': "MITx 18.6501x Fundamentals of Statistics - Linear Regression"
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_10_MPC = KC_MPC_QUESTIONS[:-1]