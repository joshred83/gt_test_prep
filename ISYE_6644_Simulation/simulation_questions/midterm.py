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

# question_2_poisson_process = {
#     'question': (
#         "At a coffee shop, customers arrive according to a Poisson process with rate $\\lambda = 4$ customers per hour. What is the distribution of time between the 7th and 8th customer arrivals?"
#     ),
#     'options_list': ["Solution not required"],
#     'correct_answer': "The time between the 7th and 8th customer arrivals follows an Exponential(4) distribution.",
#     'explanation': (
#         "For a Poisson process with rate $\\lambda$, the time between consecutive arrivals follows an exponential distribution with parameter $\\lambda$:\n"
#         "$$\n"
#         f"f(t) = \\lambda e^{-\\lambda t}, \\quad t \\geq 0.\n"
#         "$$\n"
#         "Here, $\\lambda = 4$, so the time between arrivals follows an $\\text{Exp}(4)$ distribution."
#     ),
#     'chapter_information': "Deepseek Generated"
# }

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


question_23_lcg = {
    'question': (
        "Consider the linear congruential generator (LCG):\n"
        "$$ X_{i+1} = (5X_i + 3) \\mod 12. $$\n"
        "(a) Using \( X_0 = 2 \), calculate the first pseudo‐random number \( U_1 \).\n"
        "(b) Still with \( X_0 = 2 \), calculate the pseudo‐random number \( U_{25} \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Both \( U_1 \) and \( U_{25} \) are approximately 0.0833.",
    'explanation': (
        "1. Compute \( X_1 \):\n"
        "   $$ X_1 = (5 \cdot 2 + 3) \\mod 12 = 13 \\mod 12 = 1. $$\n"
        "   $$ U_1 = \\frac{X_1}{12} = \\frac{1}{12} \\approx 0.0833. $$\n"
        "2. Identify the repeating cycle length by generating a few terms. The sequence cycles with period 4: "
        "   $$ (X_0, X_1, X_2, X_3) = (2, 1, 8, 7). $$\n"
        "3. Since \( 25 \\equiv 1 \\mod 4 \), it follows that \( X_{25} = X_1 = 1 \), so \( U_{25} = U_1 = 0.0833 \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_24_exponential_transformation = {
    'question': (
        "Let \( U \\sim \\text{Unif}(0,1) \). Determine the distribution of:\n"
        "$$ Y = -4\\ln(U). $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( Y \\sim \\text{Exp}(1/4) \).",
    'explanation': (
        "1. Since \( U \\sim \\text{Unif}(0,1) \), we know that \( -\\ln(U) \\sim \\text{Exp}(1) \).\n"
        "2. Scaling by 4 transforms this into \( Y = 4(-\\ln(U)) \sim \\text{Exp}(1/4) \), "
        "with the pdf:\n"
        "   $$ f_Y(y) = \\frac{1}{4} e^{-y/4}, \\quad y \\geq 0. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_25_gamma_sum = {
    'question': (
        "Suppose \( U_1, U_2 \\sim \\text{i.i.d. Unif}(0,1) \). What is the distribution of:\n"
        "$$ Z = -2\\ln(U_1 U_2)? $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( Z \\sim \\text{Gamma}(2, 1/2) \).",
    'explanation': (
        "1. Since \( -\\ln(U) \\sim \\text{Exp}(1) \), it follows that \( -2\\ln(U) \\sim \\text{Exp}(1/2) \).\n"
        "2. Since \( \\ln(U_1U_2) = \\ln(U_1) + \\ln(U_2) \), the sum follows a Gamma distribution:\n"
        "   $$ Z \\sim \\text{Gamma}(2, 1/2), $$\n"
        "   with pdf:\n"
        "   $$ f_Z(z) = \\frac{1}{4} z e^{-z/2}, \\quad z \\geq 0. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_26_box_muller = {
    'question': (
        "Let \( U_1, U_2 \\sim \\text{i.i.d. Unif}(0,1) \). What is the distribution of:\n"
        "$$ W = 3 + \\sqrt{-2\\ln(U_1)} \\sin(2\\pi U_2)? $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( W \\sim \\mathcal{N}(3,1) \).",
    'explanation': (
        "1. By the Box–Muller transform, \( \\sqrt{-2\\ln(U_1)} \\sin(2\\pi U_2) \sim \\mathcal{N}(0,1) \).\n"
        "2. Adding 3 shifts the mean, so the final distribution is:\n"
        "   $$ W \\sim \\mathcal{N}(3,1). $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_27_monte_carlo_integral = {
    'question': (
        "Estimate the integral:\n"
        "$$ I = \\int_{0}^{1} (e^x + x^2)dx $$\n"
        "using Monte Carlo integration with 5 samples drawn from \( \\text{Unif}(0,1) \):\n"
        "   \( \\{0.25, 0.50, 0.75, 0.10, 0.90\\} \).\n"
        "Use the estimator:\n"
        "$$ I_5 = \\frac{1}{5} \\sum_{i=1}^{5} (e^{U_i} + U_i^2). $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Monte Carlo estimate \( I_5 \\approx 2.062 \).",
    'explanation': (
        "1. Compute function values at each \( U_i \):\n"
        "   $$ e^{0.25} + 0.25^2 \\approx 1.3465, $$\n"
        "   $$ e^{0.50} + 0.50^2 \\approx 1.8987, $$\n"
        "   $$ e^{0.75} + 0.75^2 \\approx 2.6795, $$\n"
        "   $$ e^{0.10} + 0.10^2 \\approx 1.1152, $$\n"
        "   $$ e^{0.90} + 0.90^2 \\approx 3.2696. $$\n"
        "2. Compute:\n"
        "   $$ I_5 = \\frac{1}{5} (1.3465 + 1.8987 + 2.6795 + 1.1152 + 3.2696) \\approx 2.062. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_28_euler_method = {
    'question': (
        "Consider the differential equation:\n"
        "$$ f'(x) = (4 - x) f(x), \\quad f(0) = 2. $$\n"
        "Use Euler’s method with step \( h=0.05 \) to approximate \( f(0.1) \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( f(0.1) \\approx 2.874 \).",
    'explanation': (
        "1. Euler's method formula:\n"
        "   $$ f(x+h) \\approx f(x) + h f'(x). $$\n"
        "2. Compute:\n"
        "   - \( f(0.05) \\approx 2.4 \)\n"
        "   - \( f(0.1) \\approx 2.874 \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_29_queue_fifo = {
    'question': (
        "A coffee shop has customers arriving at times \( 5, 8, 12, 14 \) minutes, ordering \( 2, 1, 3, 1 \) coffees respectively.\n"
        "Each coffee takes **2 minutes** to prepare, and every minute a customer waits costs **\$0.30**.\n"
        "Each coffee sells for **\$3**.\n\n"
        "(a) When does the first customer leave?\n"
        "(b) What is the average number of customers in the system during the first 15 minutes?\n"
        "(c) Compute the net profit (total revenue minus waiting cost)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "(a) First customer leaves at \( t=9 \). (b) Average number of customers is \( 0.73 \). "
                      "(c) Net profit is **\$19.50**.",
    'explanation': (
        "1. Compute customer departures using FIFO service.\n"
        "2. Track system size over time.\n"
        "3. Compute revenue as \( 21 \), waiting cost as \( 1.50 \), so net profit is \( 19.50 \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_16_lcg = {
    'question': (
        "Consider the linear congruential generator:\n"
        "$$ X_{i+1} = (5X_i + 3) \\mod 10. $$\n"
        "1. Using \(X_0 = 2\), compute the first pseudo‐random number \(U_1\).\n"
        "2. Using \(X_0 = 2\), compute \(U_{501}\). (Hint: Look for a repeating cycle.)"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Both \( U_1 \) and \( U_{501} \) are 0.3.",
    'explanation': (
        "1. Compute \(X_1\):\n"
        "   $$ X_1 = (5 \\cdot 2 + 3) \\mod 10 = 13 \\mod 10 = 3. $$\n"
        "   $$ U_1 = \\frac{X_1}{10} = 0.3. $$\n"
        "2. Since the sequence repeats, \( X_{501} = X_1 \) (as \(501 \\equiv 1 \\mod p\)), giving:\n"
        "   $$ U_{501} = U_1 = 0.3. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_17_exp_transformation = {
    'question': (
        "Let \( U \\sim \\text{Unif}(0,1) \). Consider the transformation:\n"
        "$$ Y = -5\\ln(U). $$\n"
        "What is the distribution (name and parameter) of \( Y \)?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( Y \\sim \\text{Exp}(1/5) \).",
    'explanation': (
        "1. Since \( -\\ln(U) \\sim \\text{Exp}(1) \), multiplying by 5 scales the rate by \( 1/5 \), giving:\n"
        "   $$ Y \\sim \\text{Exp}(1/5). $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_18_hypoexp_sum = {
    'question': (
        "Let \( U_1, U_2 \\sim \\text{i.i.d. Unif}(0,1) \). Define:\n"
        "$$ Z = -5\\ln(U_1) + (-2\\ln(U_2)). $$\n"
        "What is the distribution of \( Z \)?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Hypoexponential with rates \( 1/5 \) and \( 1/2 \).",
    'explanation': (
        "1. \( -5\\ln(U_1) \\sim \\text{Exp}(1/5) \) and \( -2\\ln(U_2) \\sim \\text{Exp}(1/2) \).\n"
        "2. The sum of two independent exponentials with different rates follows a hypoexponential distribution."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_19_box_muller = {
    'question': (
        "Let \( U_1, U_2 \\sim \\text{i.i.d. Unif}(0,1) \). Define:\n"
        "$$ W = 1 + \\sqrt{-2\\ln(U_1)}\\sin(2\\pi U_2). $$\n"
        "What is the distribution of \( W \)?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( W \\sim \\mathcal{N}(1,1) \).",
    'explanation': (
        "1. By the Box–Muller transform, \( \\sqrt{-2\\ln(U_1)}\\sin(2\\pi U_2) \\sim \\mathcal{N}(0,1) \).\n"
        "2. Shifting by 1 gives \( W \\sim \\mathcal{N}(1,1) \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_20_monte_carlo = {
    'question': (
        "Estimate the integral:\n"
        "$$ I = \\int_{0}^{1} e^{-x^2}dx $$\n"
        "using Monte Carlo integration with 4 uniform samples \( \\{0.12, 0.44, 0.58, 0.93\\} \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( \\hat{I}_4 \\approx 0.7366 \).",
    'explanation': (
        "1. Compute \( e^{-U_i^2} \) for each \( U_i \):\n"
        "   - \( e^{-0.12^2} \\approx 0.9857 \),\n"
        "   - \( e^{-0.44^2} \\approx 0.8241 \),\n"
        "   - \( e^{-0.58^2} \\approx 0.7147 \),\n"
        "   - \( e^{-0.93^2} \\approx 0.4218 \).\n"
        "2. Compute Monte Carlo estimator:\n"
        "   $$ \\hat{I}_4 = \\frac{1}{4} (0.9857 + 0.8241 + 0.7147 + 0.4218) \\approx 0.7366. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_21_euler_method = {
    'question': (
        "Use Euler’s method with step \( h=0.02 \) to approximate \( f(0.04) \) for:\n"
        "$$ f'(x) = (5 - x) f(x), \\quad f(0) = 2. $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( f(0.04) \\approx 2.4191 \).",
    'explanation': (
        "1. Euler’s update formula:\n"
        "   $$ f(x+h) \\approx f(x) + h f'(x). $$\n"
        "2. Compute step-by-step:\n"
        "   - \( f(0.02) \\approx 2.2 \),\n"
        "   - \( f(0.04) \\approx 2.4191 \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_22_queue_lifo = {
    'question': (
        "A shop has 4 customers arriving at times \( 10, 13, 15, 19 \) minutes.\n"
        "They are served **LIFO** (last-in, first-out) and request:\n"
        "   - 4, 1, 5, 2 items (each takes **2 minutes** to prepare).\n"
        "Each item sells for **\$3** and each minute waiting costs **\$0.40**.\n"
        "1. When does the **first** customer (arrived at \( t=10 \)) leave?\n"
        "2. What is the **average number of customers** in the system over [0,25]?\n"
        "3. Compute the **net profit** (total revenue minus waiting cost)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "1. First customer leaves around \( t=27 \).\n"
        "2. Average number in system is about \( 1.2 \).\n"
        "3. Net profit is **approximately**:\n"
        "   $$ \\text{Revenue} = 12 \\times 3 = 36, $$\n"
        "   $$ \\text{Waiting cost} = 0.40 \\times \\text{total wait time}, $$\n"
        "   $$ \\text{Net Profit} \\approx 36 - \\text{waiting penalty}. $$"
    ),
    'explanation': (
        "1. Track LIFO service, ensuring new arrivals jump the queue.\n"
        "2. Count the number in system at each minute, compute average.\n"
        "3. Compute net profit using revenue and waiting cost formulas."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_A_geometric_distribution = {
    'question': (
        "Suppose the Los Angeles Lakers play independent games where the probability of a win in each game is 0.7. Let:\n"
        "$$ Y = \\text{the number of games until the Lakers achieve their first win}. $$\n"
        "Find the smallest positive integer \( y \) such that:\n"
        "$$ P(Y \\leq y) \\geq 0.95. $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The smallest \( y \) satisfying \( P(Y \\leq y) \\geq 0.95 \) is \( 3 \).",
    'explanation': (
        "1. Model \( Y \) as a geometric random variable: \( Y \\sim \\text{Geom}(0.7) \).\n"
        "2. The cumulative distribution function (CDF) is:\n"
        "   $$ P(Y \\leq y) = 1 - (0.3)^y. $$\n"
        "3. Solve for \( y \) in:\n"
        "   $$ 1 - (0.3)^y \\geq 0.95. $$\n"
        "   $$ (0.3)^y \\leq 0.05. $$\n"
        "4. Taking the natural logarithm:\n"
        "   $$ y \\geq \\frac{\\ln(0.05)}{\\ln(0.3)} \\approx 2.487. $$\n"
        "5. The smallest integer satisfying this is \( y = 3 \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_B_clt_sample_mean = {
    'question': (
        "Suppose \( X_1, X_2, \\dots, X_n \) are independent and identically distributed (i.i.d.) random variables "
        "with finite mean \( \\mu \) and finite variance \( \\sigma^2 \). Which theorem guarantees that the sample mean:\n"
        "$$ \\bar{X} = \\frac{1}{n} \\sum_{i=1}^{n} X_i $$\n"
        "is approximately normally distributed for large \( n \)?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The Central Limit Theorem (CLT).",
    'explanation': (
        "The Central Limit Theorem (CLT) states that if \( X_i \) are i.i.d. with finite mean \( \\mu \) and variance \( \\sigma^2 \), "
        "then for large \( n \), the standardized sample mean:\n"
        "   $$ \\frac{\\bar{X} - \\mu}{\\sigma / \\sqrt{n}} \\to \\mathcal{N}(0,1) $$\n"
        "in distribution, meaning the sample mean is approximately normal for large \( n \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_C_clt_sum_binary = {
    'question': (
        "Suppose \( X_1, X_2, \\dots, X_{100} \) are independent random variables taking values \( 2 \) and \( -2 \) "
        "with equal probability 0.5. Define:\n"
        "$$ S = \\sum_{i=1}^{100} X_i. $$\n"
        "Using the Central Limit Theorem, find an approximate value for:\n"
        "$$ P(S \\geq 6). $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( P(S \\geq 6) \\approx 0.3821 \).",
    'explanation': (
        "1. Compute the mean and variance of each \( X_i \):\n"
        "   - Mean: \( E[X_i] = 0 \).\n"
        "   - Variance: \( \\text{Var}(X_i) = 4 \).\n"
        "2. The sum \( S \) follows:\n"
        "   $$ S \\sim \\mathcal{N}(0, 400). $$\n"
        "3. Standardize \( S \) using the normal approximation:\n"
        "   $$ P(S \\geq 6) = P \\left( Z \\geq \\frac{6 - 0}{20} \\right) = P(Z \\geq 0.3). $$\n"
        "4. Using a standard normal table:\n"
        "   $$ P(Z \\geq 0.3) = 1 - \\Phi(0.3) \\approx 1 - 0.6179 = 0.3821. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}
question_1_cat_laser_pointer = {
    'question': (
        "Whiskers the cat is on a mission. Every time she pounces on a laser pointer’s red dot, "
        "she succeeds with probability 0.65 (and otherwise misses). Let:\n"
        "$$ X = \\text{the number of pounces until Whiskers catches the red dot.} $$\n"
        "Find the smallest number \( x \) such that:\n"
        "$$ P(X \\leq x) \\geq 0.90. $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The smallest \( x \) satisfying \( P(X \\leq x) \\geq 0.90 \) is \( 3 \).",
    'explanation': (
        "1. Model \( X \) as a geometric random variable: \( X \\sim \\operatorname{Geom}(0.65) \).\n"
        "2. The cumulative distribution function (CDF) is:\n"
        "   $$ P(X \\leq x) = 1 - (0.35)^x. $$\n"
        "3. Solve for \( x \) in:\n"
        "   $$ 1 - (0.35)^x \\geq 0.90. $$\n"
        "   $$ (0.35)^x \\leq 0.10. $$\n"
        "4. Taking natural logarithms:\n"
        "   $$ x \\geq \\frac{\\ln(0.10)}{\\ln(0.35)} \\approx 2.193. $$\n"
        "5. The smallest integer satisfying this is \( x=3 \)."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_2_bieber_clt = {
    'question': (
        "Justin Bieber releases a new album, where each song gets an average of 1,200,000 streams with variance "
        "\( 9 \\times 10^{10} \) streams². Suppose he releases 64 songs. By the Central Limit Theorem, approximate the "
        "probability that his total album streams exceed 80,000,000."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability of exceeding 80,000,000 streams is approximately 9.2%.",
    'explanation': (
        "1. Compute mean and variance of total streams:\n"
        "   - \( E[S] = 64 \\times 1,200,000 = 76,800,000. \)\n"
        "   - \( \\operatorname{Var}(S) = 64 \\times 9 \\times 10^{10} = 5.76 \\times 10^{12}. \)\n"
        "   - Standard deviation: \( \\sigma_S = \\sqrt{5.76 \\times 10^{12}} = 2.4 \\times 10^6. \)\n"
        "2. Standardize and compute:\n"
        "   $$ Z = \\frac{80,000,000 - 76,800,000}{2,400,000} \\approx 1.33. $$\n"
        "3. From normal tables, \( P(Z > 1.33) \\approx 0.0918. \)"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_3_cornell_poisson = {
    'question': (
        "At Cornell University, the Math Department runs problem‐solving workshops to keep kids off the street. "
        "Kids arrive following a Poisson process with rate \( \\lambda = 2 \) per hour. "
        "What is the probability that at least 5 kids show up in the next 3 hours?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability that at least 5 kids arrive is approximately 71.5%.",
    'explanation': (
        "1. The number of arrivals in 3 hours follows a Poisson distribution with parameter:\n"
        "   $$ \\lambda t = 2 \\times 3 = 6, \\quad N \\sim \\operatorname{Poisson}(6). $$\n"
        "2. Compute \( P(N \\geq 5) = 1 - P(N \\leq 4). \)\n"
        "3. Using the Poisson mass function, compute \( P(N=0), P(N=1), ..., P(N=4) \), sum them, and subtract from 1.\n"
        "4. The result gives \( P(N \\geq 5) \\approx 0.715. \)"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_4_cat_transformation = {
    'question': (
        "A curious cat’s curiosity level \( X \) follows the density:\n"
        "$$ f_X(x) = 3x^2, \\quad 0 < x < 1. $$\n"
        "A 'mystery measure' of curiosity is defined as:\n"
        "$$ Y = -\\ln(x). $$\n"
        "Find the pdf of \( Y \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of \( Y \) is \( f_Y(y) = 3e^{-3y}, \\quad y \\geq 0. \)",
    'explanation': (
        "1. Express the transformation: \( x = e^{-y} \).\n"
        "2. Compute the Jacobian determinant: \( \\frac{dx}{dy} = -e^{-y}, \\quad \\left| \\frac{dx}{dy} \\right| = e^{-y}. \)\n"
        "3. Apply the change-of-variable formula:\n"
        "   $$ f_Y(y) = f_X(x) \\left| \\frac{dx}{dy} \\right|, \\quad x = e^{-y}. $$\n"
        "4. Compute:\n"
        "   $$ f_Y(y) = 3(e^{-y})^2 \\cdot e^{-y} = 3e^{-3y}, \\quad y \\geq 0. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_5_math_safety_expectation = {
    'question': (
        "At a community center near Cornell, students study math to stay off the streets. "
        "The number of study hours per day \( X \) follows:\n"
        "$$ f_X(x) = 4x^3, \\quad 0 < x < 1. $$\n"
        "A 'street safety score' is given by:\n"
        "$$ Y = \\frac{3}{X} - 2. $$\n"
        "Find \( E[Y] \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The expected street safety score is 2.",
    'explanation': (
        "1. Express expectation in terms of \( X \):\n"
        "   $$ E[Y] = 3E\\left[ \\frac{1}{X} \\right] - 2. $$\n"
        "2. Compute \( E\\left[ \\frac{1}{X} \\right] \):\n"
        "   $$ E\\left[ \\frac{1}{X} \\right] = \\int_0^1 \\frac{1}{x} \\cdot 4x^3 dx. $$\n"
        "3. Solve the integral:\n"
        "   $$ \\int_0^1 x^2 dx = \\frac{1}{3}, \\quad E\\left[ \\frac{1}{X} \\right] = 4 \\times \\frac{1}{3} = \\frac{4}{3}. $$\n"
        "4. Compute \( E[Y] \):\n"
        "   $$ E[Y] = 3 \\times \\frac{4}{3} - 2 = 2. $$"
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