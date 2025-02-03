question_1_geometric_distribution = {
    'question': (
        "A student plays a video game level until completing it successfully. If the probability of completing the level on any attempt is $p = \\frac{1}{12}$, what is the expected number of attempts needed?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The expected number of attempts is $E[X] = \\frac{1}{p} = 12$ attempts.",
    'explanation': (
        "For a geometric distribution with success probability $p$, the expected number of attempts $E[X]$ is given by:\n"
        "$$\n"
        "E[X] = \\frac{1}{p}.\n"
        "$$\n"
        "Substituting $p = \\frac{1}{12}$:\n"
        "$$\n"
        "E[X] = \\frac{1}{\\frac{1}{12}} = 12.\n"
        "$$"
    ),
    'chapter_information': "Deepseek Generated"
}

question_2_poisson_process = {
    'question': (
        "At a coffee shop, customers arrive according to a Poisson process with rate $\\lambda = 4$ customers per hour. What is the distribution of time between the 7th and 8th customer arrivals?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The time between the 7th and 8th customer arrivals follows an Exponential(4) distribution.",
    'explanation': (
        "For a Poisson process with rate $\\lambda$, the time between consecutive arrivals follows an exponential distribution with parameter $\\lambda$:\n"
        "$$\n"
        f"f(t) = \\lambda e^{-\\lambda t}, \\quad t \\geq 0.\n"
        "$$\n"
        "Here, $\\lambda = 4$, so the time between arrivals follows an $\\text{Exp}(4)$ distribution."
    ),
    'chapter_information': "Deepseek Generated"
}

question_3_random_variable_transformation = {
    'question': (
        "Let $X$ have pdf $f(x) = 3x^2$ for $0 \\leq x \\leq 1$. Find the pdf of $Y = \\ln(X)$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$g(y) = 3e^{3y}$ for $-\\infty < y \\leq 0$.",
    'explanation': (
        "Using the transformation method:\n"
        "1. Let $Y = \\ln(X)$, so $X = e^Y$.\n"
        "2. The pdf is given by:\n"
        "$$\n"
        "g(y) = f(x) \\left| \\frac{dx}{dy} \\right|,\n"
        "$$\n"
        "where $x = e^y$ and $\\frac{dx}{dy} = e^y$.\n"
        "3. Substitute $f(x) = 3x^2$ and $x = e^y$:\n"
        "$$\n"
        "g(y) = 3(e^y)^2 \\cdot e^y = 3e^{3y}, \\quad -\\infty < y \\leq 0.\n"
        "$$"
    ),
    'chapter_information': "Deepseek Generated"
}

question_4_joint_distributions = {
    'question': (
        "Let $X$ and $Y$ have joint pdf $f(x, y) = 6xy$ for $0 \\leq x \\leq 1$, $0 \\leq y \\leq 1$. Find:\n"
        "a) $E[X]$\n"
        "b) $E[XY]$\n"
        "c) $\\text{Cov}(X, Y)$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "a) $E[X] = \\frac{1}{2}$\n"
        "b) $E[XY] = \\frac{1}{4}$\n"
        "c) $\\text{Cov}(X, Y) = \\frac{1}{12}$"
    ),
    'explanation': (
        "1. Compute $E[X]$:\n"
        "$$\n"
        "E[X] = \\int_0^1 \\int_0^1 6xy \\, dx \\, dy = \\frac{1}{2}.\n"
        "$$\n"
        "2. Compute $E[XY]$:\n"
        "$$\n"
        "E[XY] = \\int_0^1 \\int_0^1 6x^2y^2 \\, dx \\, dy = \\frac{1}{4}.\n"
        "$$\n"
        "3. Compute $\\text{Cov}(X, Y)$:\n"
        "$$\n"
        "\\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = \\frac{1}{4} - \\frac{1}{2} \\cdot \\frac{1}{2} = \\frac{1}{12}.\n"
        "$$"
    ),
    'chapter_information': "Deepseek Generated"
}

question_5_normal_distribution = {
    'question': (
        "Let $X$ and $Y$ be $\\text{Normal}(2, 16)$ random variables with $\\text{Cov}(X, Y) = 8$. Find $\\text{Var}(X + Y)$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$\\text{Var}(X + Y) = 48$",
    'explanation': (
        "The variance of the sum of two random variables is given by:\n"
        "$$\n"
        "\\text{Var}(X + Y) = \\text{Var}(X) + \\text{Var}(Y) + 2\\,\\text{Cov}(X, Y).\n"
        "$$\n"
        "Substitute $\\text{Var}(X) = \\text{Var}(Y) = 16$ and $\\text{Cov}(X, Y) = 8$:\n"
        "$$\n"
        "\\text{Var}(X + Y) = 16 + 16 + 2(8) = 48.\n"
        "$$"
    ),
    'chapter_information': "Deepseek Generated"
}

question_6_sum_of_exponentials = {
    'question': (
        "If $X$ and $Y$ are independent exponential random variables with rate $\\lambda = 2$, find $P(X + Y \\leq 1)$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$P(X + Y \\leq 1) \\approx 0.594$",
    'explanation': (
        "The sum $X + Y$ follows an Erlang(2, 2) distribution with pdf:\n"
        "$$\n"
        "f_{X+Y}(t) = 4t e^{-2t}, \\quad t \\geq 0.\n"
        "$$\n"
        "The cumulative probability is:\n"
        "$$\n"
        "P(X + Y \\leq 1) = \\int_0^1 4t e^{-2t} \\, dt.\n"
        "$$\n"
        "Compute this integral:\n"
        "$$\n"
        "\\int_0^1 4t e^{-2t} \\, dt = 1 - e^{-2}(1 + 2) \\approx 0.594.\n"
        "$$"
    ),
    'chapter_information': "Deepseek Generated"
}

question_1_geometric_waiting_time = {
    'question': (
        "You roll two fair dice repeatedly. What is the expected number of rolls until the sum of the dice is 10?\n\n"
        "Hint: Recall that the number of rolls until the first occurrence of an event with probability \( p \) is geometrically distributed with mean \( 1/p \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The expected number of rolls is 12.",
    'explanation': (
        "1. Determine the probability of rolling a sum of 10:\n"
        "   - There are 36 total equally-likely outcomes.\n"
        "   - The pairs that sum to 10 are (4,6), (5,5), (6,4), so there are 3 favorable outcomes.\n"
        "   - Thus, the probability of rolling a 10 is:\n"
        "     $$ p = \\frac{3}{36} = \\frac{1}{12}. $$\n\n"
        "2. The number of rolls required follows a geometric distribution:\n"
        "   $$ E[X] = \\frac{1}{p} = \\frac{1}{1/12} = 12. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_2_poisson_interarrival_time = {
    'question': (
        "Consider a Poisson process with rate \( \\lambda = 3 \). What is the distribution of the time between the 7th and 8th arrivals?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The time between the 7th and 8th arrivals is distributed as \( \\text{Exp}(3) \).",
    'explanation': (
        "In a Poisson process with rate \( \\lambda \), the interarrival times are independent and exponentially distributed:\n"
        "$$ T_i \\sim \\text{Exp}(\\lambda). $$\n"
        "Thus, regardless of the arrival number, the time between any consecutive arrivals follows an exponential distribution with parameter \( \\lambda \)."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_3_independence_uncorrelated_exponentials = {
    'question': (
        "Suppose that \( X \) and \( Y \) are independent exponential random variables with parameters 5 and 7 respectively. Are \( X \) and \( Y \) necessarily uncorrelated?"
    ),
    'options_list': ["Yes", "No"],
    'correct_answer': "Yes",
    'explanation': (
        "Two independent random variables always have zero covariance. Since the correlation is a scaled version of covariance,\n"
        "independence implies that they are uncorrelated."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_4_poisson_process_properties = {
    'question': (
        "True or False? A homogeneous Poisson process has both stationary and independent increments."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "By definition, a homogeneous Poisson process has:\n"
        "- **Stationary increments**: The number of events in any time interval depends only on the interval length.\n"
        "- **Independent increments**: The number of events in disjoint time intervals are independent."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_5_expectation_transformation = {
    'question': (
        "Suppose a continuous random variable \( Y \) has probability density function:\n"
        "$$ g(y) = 6y(1 - y), \quad 0 < y < 1. $$\n"
        "Find the expected value of \( E[3Y + 2] \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The expected value is 11.",
    'explanation': (
        "Using the linearity of expectation:\n"
        "$$ E[3Y + 2] = 3E[Y] + 2. $$\n"
        "First, compute \( E[Y] \):\n"
        "$$ E[Y] = \\int_0^1 y \\cdot 6y(1 - y) dy. $$\n"
        "Evaluating the integral, we obtain:\n"
        "$$ E[Y] = \\frac{1}{2}. $$\n"
        "Thus,\n"
        "$$ E[3Y + 2] = 3 \\cdot \\frac{1}{2} + 2 = 11. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_6_variance_sum_correlated_normals = {
    'question': (
        "Suppose \( U \) and \( V \) are both normally distributed with mean 3 and variance 5, and their covariance is \( \\text{Cov}(U, V) = 2 \). "
        "What is the variance of \( U + V \)?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of \( U + V \) is 14.",
    'explanation': (
        "Using the formula for the variance of the sum:\n"
        "$$ \\text{Var}(U + V) = \\text{Var}(U) + \\text{Var}(V) + 2\\text{Cov}(U, V). $$\n"
        "Substituting the given values:\n"
        "$$ \\text{Var}(U + V) = 5 + 5 + 2(2) = 10 + 4 = 14. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_1_geometric_distribution = {
    'question': (
        "You roll two fair dice repeatedly and record their sum each time. Let \(X\) be the number of rolls needed until you first observe a sum of 7. "
        "What is \(\\mathbb{E}[X]\)?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The expected number of rolls is 6.",
    'explanation': (
        "1. **Probability of 'success'**: A sum of 7 occurs with probability:\n"
        "   $$ p = \\frac{6}{36} = \\frac{1}{6}. $$\n\n"
        "2. **Geometric expectation formula**: For \(X \sim \\text{Geom}(p)\),\n"
        "   $$ \\mathbb{E}[X] = \\frac{1}{p} = \\frac{1}{1/6} = 6. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_2_poisson_interarrival_time = {
    'question': (
        "Let \\(\\{N(t)\\}\\) be a Poisson process with rate \\(\\lambda = 3\\). "
        "What is the distribution of the time between the 10th and 11th arrivals?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The time between the 10th and 11th arrivals is distributed as \( \\text{Exponential}(3) \).",
    'explanation': (
        "1. **Poisson process basics**: Interarrival times in a Poisson process are i.i.d. exponential random variables with rate \\(\\lambda\\).\n"
        "2. **Interarrival time distribution**: The time from the 10th to the 11th arrival is also an exponential sample with rate \\(\\lambda = 3\\), "
        "thus follows \\( \\text{Exp}(3) \\)."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_3_independence_and_correlation = {
    'question': (
        "Suppose \\(X\\) and \\(Y\\) are independent exponential random variables with possibly different rates. "
        "Must \\(X\\) and \\(Y\\) be uncorrelated?"
    ),
    'options_list': ["Yes", "No"],
    'correct_answer': "Yes",
    'explanation': (
        "1. **Definition of correlation**: Correlation is given by\n"
        "   $$ \\operatorname{Corr}(X,Y) = \\frac{\\operatorname{Cov}(X,Y)}{\\sigma_X \\sigma_Y}. $$\n"
        "2. **Independence implies zero covariance**: Since \\(X\\) and \\(Y\\) are independent, we have:\n"
        "   $$ \\mathbb{E}[XY] = \\mathbb{E}[X] \\mathbb{E}[Y], $$\n"
        "   which means \\(\\operatorname{Cov}(X,Y) = 0\\), thus \\(X\\) and \\(Y\\) are uncorrelated."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_4_poisson_process_properties = {
    'question': (
        "A homogeneous Poisson process with rate \\(\\lambda = 5\\) is observed over time. "
        "Are the increments over disjoint intervals stationary and independent?"
    ),
    'options_list': ["Yes", "No"],
    'correct_answer': "Yes",
    'explanation': (
        "1. **Homogeneous Poisson process**: This process has two key properties:\n"
        "   - **Stationary increments**: The number of arrivals in an interval depends only on its length.\n"
        "   - **Independent increments**: Non-overlapping time intervals have independent counts.\n"
        "2. **Conclusion**: Since both properties hold, the answer is 'Yes'."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_5_expectation_inverse_x = {
    'question': (
        "Let \\(X\\) be a random variable on \\((0,1)\\) with pdf\n"
        "$$ f_X(x) = 5x^4, \\quad 0 < x < 1. $$\n"
        "Compute \\(\\mathbb{E}[\\frac{3}{X} - 1]\\)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\\(\\frac{11}{4}\\).",
    'explanation': (
        "1. **Expectation of \\(1/X\\)**:\n"
        "   $$ \\mathbb{E}[1/X] = \\int_0^1 \\frac{1}{x} 5x^4 dx = 5 \\int_0^1 x^3 dx = 5 \\cdot \\frac{1}{4} = \\frac{5}{4}. $$\n"
        "2. **Compute \\(\\mathbb{E}[3/X - 1]\\)**:\n"
        "   $$ \\mathbb{E}[3/X - 1] = 3\\mathbb{E}[1/X] - 1 = 3 \\cdot \\frac{5}{4} - 1 = \\frac{15}{4} - 1 = \\frac{11}{4}. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_6_variance_sum_correlated_normals = {
    'question': (
        "Let \\(X\\) and \\(Y\\) be jointly normal with mean 3 and variance 5, and their covariance is \\(\\operatorname{Cov}(X,Y) = 2\\). "
        "Find \\(\\operatorname{Var}(X + Y)\\)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of \(X + Y\) is 14.",
    'explanation': (
        "1. **Variance of sum formula**:\n"
        "   $$ \\operatorname{Var}(X + Y) = \\operatorname{Var}(X) + \\operatorname{Var}(Y) + 2 \\operatorname{Cov}(X, Y). $$\n"
        "2. **Substituting given values**:\n"
        "   $$ \\operatorname{Var}(X + Y) = 5 + 5 + 2(2) = 10 + 4 = 14. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_1_one_to_one_transformation = {
    'question': (
        "Let \(X\) be a continuous random variable with probability density function (pdf):\n"
        "$$ f_X(x) = 3x^2, \quad 0 < x < 1. $$\n"
        "Define the transformation \(Y = -\ln(x)\). Determine the pdf of \(Y\)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of \(Y\) is \( f_Y(y) = 3e^{-3y}, \quad y > 0. \)",
    'explanation': (
        "1. **Find the inverse transformation:**\n"
        "   $$ Y = -\ln(x) \Rightarrow x = e^{-Y}. $$\n"
        "2. **Compute the derivative:**\n"
        "   $$ \\frac{dx}{dy} = -e^{-Y}. $$\n"
        "   Taking the absolute value, we get \( |dx/dy| = e^{-Y} \).\n"
        "3. **Use the transformation formula:**\n"
        "   $$ f_Y(y) = f_X(x) |dx/dy| \text{ with } x = e^{-y}. $$\n"
        "   Substituting \( f_X(x) = 3x^2 = 3e^{-2y} \),\n"
        "   $$ f_Y(y) = 3e^{-2y} e^{-y} = 3e^{-3y}. $$\n"
        "4. **Verify normalization:**\n"
        "   $$ \\int_0^{\infty} 3e^{-3y} dy = 1, $$ confirming validity."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_2_transformation_nonlinear = {
    'question': (
        "Let \(X\) be a continuous random variable with pdf:\n"
        "$$ f_X(x) = 2x, \quad 0 < x < 1. $$\n"
        "Define \(Y = 1 - x\). Find the pdf of \(Y\)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of \(Y\) is \( f_Y(y) = 4y(1 - y^2), \quad 0 < y < 1. \)",
    'explanation': (
        "1. **Determine the range of \(Y\):**\n"
        "   - When \( x = 0 \), we get \( Y = 1 \).\n"
        "   - When \( x = 1 \), we get \( Y = 0 \).\n"
        "   Thus, \( Y \) ranges from \( 0 \) to \( 1 \).\n\n"
        "2. **Find the inverse transformation:**\n"
        "   $$ x = 1 - Y. $$\n"
        "   Compute the derivative:\n"
        "   $$ \\frac{dx}{dy} = -1. $$\n"
        "   Taking the absolute value: \( |dx/dy| = 1 \).\n\n"
        "3. **Apply the transformation formula:**\n"
        "   $$ f_Y(y) = f_X(x) |dx/dy| \text{ with } x = 1 - y. $$\n"
        "   Substituting \( f_X(x) = 2(1 - y) \), we get:\n"
        "   $$ f_Y(y) = 2(1 - y) \cdot 1 = 4y(1 - y^2). $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_3_joint_transformation = {
    'question': (
        "Let \(X\) and \(Y\) be independent exponential random variables with parameter \( \\lambda = 1 \). Define new variables:\n"
        "$$ U = X + Y, \quad V = \\frac{X}{X + Y}. $$\n"
        "Find the joint pdf of \((U, V)\)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The joint pdf of \((U, V)\) is \( f_{U,V}(u,v) = u e^{-u}, \quad u > 0, \quad 0 < v < 1. \)",
    'explanation': (
        "1. **Find the inverse transformation:**\n"
        "   $$ X = U V, \quad Y = U (1 - V). $$\n"
        "2. **Compute the Jacobian determinant:**\n"
        "   $$ J = \\begin{vmatrix} V & U \\\\ (1 - V) & -U \\end{vmatrix} = -U. $$\n"
        "   Taking the absolute value: \( |J| = U \).\n"
        "3. **Apply the transformation formula:**\n"
        "   - Since \( X, Y \sim \\text{Exp}(1) \), their joint pdf is:\n"
        "   $$ f_{X,Y}(x,y) = e^{-(x+y)} = e^{-U}. $$\n"
        "   - Using the Jacobian:\n"
        "   $$ f_{U,V}(u,v) = f_{X,Y}(X,Y) |J| = e^{-u} \cdot U = u e^{-u}. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_4_transformation_non_monotonic = {
    'question': (
        "Let \(Z\) be a continuous random variable with pdf:\n"
        "$$ f_Z(z) = \\frac{1}{2}, \quad -1 < z < 1. $$\n"
        "Define \( W = Z^2 \). Find the pdf of \(W\)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of \(W\) is \( f_W(w) = \\frac{1}{\\sqrt{w}}, \quad 0 < w < 1. \)",
    'explanation': (
        "1. **Determine the range of \(W\):**\n"
        "   - Since \( Z \in (-1,1) \), we have \( W = Z^2 \) taking values in \( (0,1) \).\n"
        "   - The transformation is not one-to-one, since \( Z = \pm \sqrt{W} \) both map to the same \( W \).\n\n"
        "2. **Apply the formula for transformations with multiple pre-images:**\n"
        "   $$ f_W(w) = \\sum_{z: g(z) = w} \\frac{f_Z(z)}{|g'(z)|}. $$\n"
        "   - The derivative of \( W = Z^2 \) is \( g'(z) = 2z \).\n"
        "   - Taking absolute values, \( |g'(z)| = 2\sqrt{W} \).\n\n"
        "3. **Compute contributions for both roots \( Z = \pm \sqrt{W} \):**\n"
        "   - For \( Z = \sqrt{W} \), the contribution is:\n"
        "     $$ f_Z(\sqrt{W}) \\frac{1}{|g'(\sqrt{W})|} = \\frac{1}{2} \\cdot \\frac{1}{2\sqrt{W}} = \\frac{1}{4\sqrt{W}}. $$\n"
        "   - For \( Z = -\sqrt{W} \), the contribution is the same.\n"
        "   - Summing both contributions:\n"
        "     $$ f_W(w) = \\frac{1}{4\sqrt{W}} + \\frac{1}{4\sqrt{W}} = \\frac{1}{2\sqrt{W}}, \quad 0 < w < 1. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}
KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MIDTERM_1_MPC = KC_MPC_QUESTIONS[:-1]