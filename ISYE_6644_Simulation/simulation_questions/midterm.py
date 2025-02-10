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
        "Hint: Recall that the number of rolls until the first occurrence of an event with probability $ p $ is geometrically distributed with mean $ 1/p $."
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
        "Consider a Poisson process with rate $ \\lambda = 3 $. What is the distribution of the time between the 7th and 8th arrivals?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The time between the 7th and 8th arrivals is distributed as $ \\text{Exp}(3) $.",
    'explanation': (
        "In a Poisson process with rate $ \\lambda $, the interarrival times are independent and exponentially distributed:\n"
        "$$ T_i \\sim \\text{Exp}(\\lambda). $$\n"
        "Thus, regardless of the arrival number, the time between any consecutive arrivals follows an exponential distribution with parameter $ \\lambda $."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_3_independence_uncorrelated_exponentials = {
    'question': (
        "Suppose that $X$ and $Y$ are independent exponential random variables with parameters 5 and 7 respectively. Are $X$ and $Y$ necessarily uncorrelated?"
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
        "Suppose a continuous random variable $Y$ has probability density function:\n"
        "$$ g(y) = 6y(1 - y), \quad 0 < y < 1. $$\n"
        "Find the expected value of $E[3Y + 2]$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The expected value is 11.",
    'explanation': (
        "Using the linearity of expectation:\n"
        "$$ E[3Y + 2] = 3E[Y] + 2. $$\n"
        "First, compute $E[Y]$:\n"
        "$$ E[Y] = \\int_0^1 y \\cdot 6y(1 - y) \\, dy. $$\n"
        "Evaluating the integral, we obtain:\n"
        "$$ E[Y] = \\frac{1}{2}. $$\n"
        "Thus,\n"
        "$$ E[3Y + 2] = 3 \\cdot \\frac{1}{2} + 2 = 3.5. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_6_variance_sum_correlated_normals = {
    'question': (
        "Suppose $U$ and $V$ are both normally distributed with mean 3 and variance 5, and their covariance is $\\text{Cov}(U, V) = 2$. "
        "What is the variance of $U + V$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of $U + V$ is 14.",
    'explanation': (
        "Using the formula for the variance of the sum:\n"
        "$$\n"
        "\\text{Var}(U + V) = \\text{Var}(U) + \\text{Var}(V) + 2\\,\\text{Cov}(U, V).\n"
        "$$\n"
        "Substituting the given values:\n"
        "$$\n"
        "\\text{Var}(U + V) = 5 + 5 + 2(2) = 10 + 4 = 14.\n"
        "$$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_1_geometric_distribution = {
    'question': (
        "You roll two fair dice repeatedly and record their sum each time. Let $X$ be the number of rolls needed until you first observe a sum of 7. "
        "What is $\\mathbb{E}[X]$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The expected number of rolls is 6.",
    'explanation': (
        "1. **Probability of 'success'**: A sum of 7 occurs with probability:\n"
        "   $$ p = \\frac{6}{36} = \\frac{1}{6}. $$\n\n"
        "2. **Geometric expectation formula**: For $X \sim \\text{Geom}(p)$,\n"
        "   $$ \\mathbb{E}[X] = \\frac{1}{p} = \\frac{1}{1/6} = 6. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_2_poisson_interarrival_time = {
    'question': (
        "Let $\\{N(t)\\}$ be a Poisson process with rate $\\lambda = 3$. "
        "What is the distribution of the time between the 10th and 11th arrivals?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The time between the 10th and 11th arrivals is distributed as $\\text{Exponential}(3)$.",
    'explanation': (
        "1. **Poisson process basics**: Interarrival times in a Poisson process are i.i.d. exponential random variables with rate $\\lambda$.\n"
        "2. **Interarrival time distribution**: The time from the 10th to the 11th arrival is also an exponential sample with rate $\\lambda = 3$, "
        "thus follows $\\text{Exp}(3)$."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_3_independence_and_correlation = {
    'question': (
        "Suppose $X$ and $Y$ are independent exponential random variables with possibly different rates. "
        "Must $X$ and $Y$ be uncorrelated?"
    ),
    'options_list': ["Yes", "No"],
    'correct_answer': "Yes",
    'explanation': (
        "1. **Definition of correlation**: Correlation is given by\n"
        "$$ \\operatorname{Corr}(X,Y) = \\frac{\\operatorname{Cov}(X,Y)}{\\sigma_X \\sigma_Y}. $$\n"
        "2. **Independence implies zero covariance**: Since $X$ and $Y$ are independent, we have:\n"
        "$$ \\mathbb{E}[XY] = \\mathbb{E}[X] \\mathbb{E}[Y], $$\n"
        "which means $\\operatorname{Cov}(X,Y) = 0$, thus $X$ and $Y$ are uncorrelated."
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_4_poisson_process_properties = {
    'question': (
        "A homogeneous Poisson process with rate $\\lambda = 5$ is observed over time. "
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
        "Let $X$ be a random variable on $(0,1)$ with pdf\n"
        "$$ f_X(x) = 5x^4, \\quad 0 < x < 1. $$\n"
        "Compute $ \\mathbb{E}[\\frac{3}{X} - 1]$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$\\frac{11}{4}$.",
    'explanation': (
        "1. **Expectation of $1/X$**:\n"
        "$$ \\mathbb{E}[1/X] = \\int_0^1 \\frac{1}{x} 5x^4 \\ dx = 5 \\int_0^1 x^3 \\ dx = 5 \\cdot \\frac{1}{4} = \\frac{5}{4}. $$\n"
        "2. **Compute $\\mathbb{E}[3/X - 1]$**:\n"
        "$$ \\mathbb{E}[3/X - 1] = 3\\mathbb{E}[1/X] - 1 = 3 \\cdot \\frac{5}{4} - 1 = \\frac{15}{4} - 1 = \\frac{11}{4}. $$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}


question_6_variance_sum_correlated_normals = {
    'question': (
        "Let $X$ and $Y$ be jointly normal with mean 3 and variance 5, and their covariance is $\\operatorname{Cov}(X,Y) = 2$. "
        "Find $\\operatorname{Var}(X + Y)$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of $X + Y$ is 14.",
    'explanation': (
        "1. **Variance of sum formula**:\n"
        "$$\n"
        "\\operatorname{Var}(X + Y) = \\operatorname{Var}(X) + \\operatorname{Var}(Y) + 2 \\operatorname{Cov}(X, Y).\n"
        "$$\n"
        "2. **Substituting given values**:\n"
        "$$\n"
        "\\operatorname{Var}(X + Y) = 5 + 5 + 2(2) = 10 + 4 = 14.\n"
        "$$"
    ),
    'chapter_information': "GPT 03-mini Generated"
}

question_1_one_to_one_transformation = {
    'question': (
        "Let $X$ be a continuous random variable with probability density function (pdf):\n"
        "$$ f_X(x) = 3x^2, \quad 0 < x < 1. $$\n"
        "Define the transformation $Y = -\ln(x)$. Determine the pdf of $Y$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of $Y$ is $f_Y(y) = 3e^{-3y}, \quad y > 0.$",
    'explanation': (
        "1. **Find the inverse transformation:**\n"
        "$$ Y = -\ln(x) \Rightarrow x = e^{-Y}. $$\n"
        "2. **Compute the derivative:**\n"
        "$$ \\frac{dx}{dy} = -e^{-Y}. $$\n"
        "Taking the absolute value, we get $|dx/dy| = e^{-Y}$.\n"
        "3. **Use the transformation formula:**\n"
        "$$ f_Y(y) = f_X(x) |dx/dy| \text{ with } x = e^{-y}. $$\n"
        "Substituting $f_X(x) = 3x^2 = 3e^{-2y}$,\n"
        "$$ f_Y(y) = 3e^{-2y} e^{-y} = 3e^{-3y}. $$\n"
        "4. **Verify normalization:**\n"
        "$$ \\int_0^{\infty} 3e^{-3y} dy = 1, $$ confirming validity."
    ),
    'chapter_information': "DeepSeek Generated"
}


question_2_transformation_nonlinear = {
    'question': (
        "Let $X$ be a continuous random variable with pdf:\n"
        "$$ f_X(x) = 2x, \quad 0 < x < 1. $$\n"
        "Define $Y = 1 - x$. Find the pdf of $Y$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of $Y$ is $f_Y(y) = 2(1 - y), \quad 0 < y < 1.$",
    'explanation': (
        "1. **Determine the range of $Y$:**\n"
        "- When $x = 0$, we get $Y = 1$.\n"
        "- When $x = 1$, we get $Y = 0$.\n"
        "Thus, $Y$ ranges from 0 to 1.\n\n"
        "2. **Find the inverse transformation:**\n"
        "$$ x = 1 - Y. $$\n"
        "Compute the derivative:\n"
        "$$ \\frac{dx}{dy} = -1. $$\n"
        "Taking the absolute value: $|dx/dy| = 1$.\n\n"
        "3. **Apply the transformation formula:**\n"
        "$$ f_Y(y) = f_X(x) |dx/dy| \text{ with } x = 1 - y. $$\n"
        "Substitute $f_X(x) = 2(1 - y)$, we get:\n"
        "$$ f_Y(y) = 2(1 - y) \cdot 1 = 2(1 - y). $$"
    ),
    'chapter_information': "DeepSeek Generated"
}


question_3_joint_transformation = {
    'question': (
        "Let $X$ and $Y$ be independent exponential random variables with parameter $ \\lambda = 1 $. Define new variables:\n"
        "$$ U = X + Y, \quad V = \\frac{X}{X + Y}. $$\n"
        "Find the joint pdf of $(U, V)$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The joint pdf of $(U, V)$ is $f_{U,V}(u,v) = u e^{-u}, \quad u > 0, \quad 0 < v < 1.$",
    'explanation': (
        "1. **Find the inverse transformation:**\n"
        "$$ X = U V, \quad Y = U (1 - V). $$\n"
        "2. **Compute the Jacobian determinant:**\n"
        "$$ J = \\begin{vmatrix} V & U \\\\ (1 - V) & -U \\end{vmatrix} = -U. $$\n"
        "Taking the absolute value: $|J| = U$.\n"
        "3. **Apply the transformation formula:**\n"
        "- Since $ X, Y \\sim \\text{Exp}(1) $, their joint pdf is:\n"
        "$$ f_{X,Y}(x,y) = e^{-(x+y)} = e^{-U}. $$\n"
        "- Using the Jacobian:\n"
        "$$ f_{U,V}(u,v) = f_{X,Y}(X,Y) |J| = e^{-u} \\cdot U = u e^{-u}. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_4_transformation_non_monotonic = {
    'question': (
        "Let $Z$ be a continuous random variable with pdf:\n"
        "$$ f_Z(z) = \\frac{1}{2}, \quad -1 < z < 1. $$\n"
        "Define $ W = Z^2 $. Find the pdf of $W$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of $W$ is $f_W(w) = \\frac{1}{\\sqrt{w}}, \quad 0 < w < 1.$",
    'explanation': (
        "1. **Determine the range of $W$:**\n"
        "- Since $Z \in (-1,1)$, we have $W = Z^2$ taking values in $(0,1)$.\n"
        "- The transformation is not one-to-one, since $Z = \pm \sqrt{W}$ both map to the same $W$.\n\n"
        "2. **Apply the formula for transformations with multiple pre-images:**\n"
        "$$ f_W(w) = \\sum_{z: g(z) = w} \\frac{f_Z(z)}{|g'(z)|}. $$\n"
        "- The derivative of $W = Z^2$ is $g'(z) = 2z$.\n"
        "- Taking absolute values, $|g'(z)| = 2\sqrt{W}$.\n\n"
        "3. **Compute contributions for both roots $Z = \pm \sqrt{W}$:**\n"
        "- For $Z = \sqrt{W}$, the contribution is:\n"
        "$$ f_Z(\sqrt{W}) \\frac{1}{|g'(\sqrt{W})|} = \\frac{1}{2} \\cdot \\frac{1}{2\sqrt{W}} = \\frac{1}{4\sqrt{W}}. $$\n"
        "- For $Z = -\sqrt{W}$, the contribution is the same.\n"
        "- Summing both contributions:\n"
        "$$ f_W(w) = \\frac{1}{4\sqrt{W}} + \\frac{1}{4\sqrt{W}} = \\frac{1}{2\sqrt{W}}, \quad 0 < w < 1. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}


question_23_lcg = {
    'question': (
        "Consider the linear congruential generator (LCG):\n"
        "$$ X_{i+1} = (5X_i + 3) \\mod 12. $$\n"
        "(a) Using $X_0 = 2$, calculate the first pseudo‐random number $U_1$.\n"
        "(b) Still with $X_0 = 2$, calculate the pseudo‐random number $U_{25}$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Both $U_1$ and $U_{25}$ are approximately 0.0833.",
    'explanation': (
        "1. Compute $X_1$:\n"
        "$$ X_1 = (5 \cdot 2 + 3) \\mod 12 = 13 \\mod 12 = 1. $$\n"
        "$$ U_1 = \\frac{X_1}{12} = \\frac{1}{12} \\approx 0.0833. $$\n"
        "2. Identify the repeating cycle length by generating a few terms. The sequence cycles with period 4: "
        "$$ (X_0, X_1, X_2, X_3) = (2, 1, 8, 7). $$\n"
        "3. Since $25 \\equiv 1 \\mod 4$, it follows that $X_{25} = X_1 = 1$, so $U_{25} = U_1 = 0.0833$."
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
        "1. Using $$X_0 = 2$$, compute the first pseudo‐random number $$U_1$$.\n"
        "2. Using $$X_0 = 2$$, compute $$U_{501}$$. (Hint: Look for a repeating cycle.)"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Both \( U_1 \) and \( U_{501} \) are 0.3.",
    'explanation': (
        "1. Compute \(X_1\):\n"
        "   $$ X_1 = (5 \\cdot 2 + 3) \\mod 10 = 13 \\mod 10 = 3. $$\n"
        "   $$ U_1 = \\frac{X_1}{10} = 0.3. $$\n"
        "2. Since the sequence repeats, $$ X_{501} = X_1 $$ as $$ 501 \\equiv 1 \\mod p\ $$, giving:\n"
        "   $$ U_{501} = U_1 = 0.3. $$"
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
        "NOT ERLANG BECAUSE THE RATES ARE DIFFERENT"
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

question_17_exp_transformation = {
    'question': (
        "Let $U \sim \text{Unif}(0,1)$. Consider the transformation:\n"
        "$$ Y = -5 \ln(U). $$\n"
        "What is the distribution (name and parameter) of $Y$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$Y \sim \text{Exp}(1/5)$",
    'explanation': (
        "1. Since $-\ln(U) \sim \text{Exp}(1)$, multiplying by 5 scales the rate by $1/5$, giving:\n"
        "$$ Y \sim \text{Exp}(1/5). $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_A_geometric_distribution = {
    'question': (
        "Suppose the Los Angeles Lakers play independent games where the probability of a win in each game is 0.7. Let:\n"
        "$$ Y = \text{the number of games until the Lakers achieve their first win}. $$\n"
        "Find the smallest positive integer $y$ such that:\n"
        "$$ P(Y \leq y) \geq 0.95. $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The smallest $y$ satisfying $P(Y \leq y) \geq 0.95$ is 3.",
    'explanation': (
        "1. Model $Y$ as a geometric random variable: $Y \sim \text{Geom}(0.7)$.\n"
        "2. The cumulative distribution function (CDF) is:\n"
        "$$ P(Y \leq y) = 1 - (0.3)^y. $$\n"
        "3. Solve for $y$ in:\n"
        "$$ 1 - (0.3)^y \geq 0.95. $$\n"
        "$$ (0.3)^y \leq 0.05. $$\n"
        "4. Taking the natural logarithm:\n"
        "$$ y \geq \\frac{\ln(0.05)}{\ln(0.3)} \approx 2.487. $$\n"
        "5. The smallest integer satisfying this is $y = 3$."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_2_bieber_clt = {
    'question': (
        "Justin Bieber releases a new album, where each song gets an average of 1,200,000 streams with variance "
        "$9 \times 10^{10}$ streams². Suppose he releases 64 songs. By the Central Limit Theorem, approximate the "
        "probability that his total album streams exceed 80,000,000."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability of exceeding 80,000,000 streams is approximately 9.2%.",
    'explanation': (
        "1. Compute mean and variance of total streams:\n"
        "   - $E[S] = 64 \times 1,200,000 = 76,800,000.$\n"
        "   - $\\operatorname{Var}(S) = 64 \times 9 \times 10^{10} = 5.76 \times 10^{12}.$\n"
        "   - Standard deviation: $\\sigma_S = \\sqrt{5.76 \times 10^{12}} = 2.4 \times 10^6.$\n"
        "2. Standardize and compute:\n"
        "$$ Z = \\frac{80,000,000 - 76,800,000}{2,400,000} \\approx 1.33. $$\n"
        "3. From normal tables, $P(Z > 1.33) \\approx 0.0918$."
    ),
    'chapter_information': "DeepSeek Generated"
}


question_3_cornell_po4isson = {
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

question_4_cat_transforma4tion = {
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
        "$$ f_Y(y) = f_X(x) \\left| \\frac{dx}{dy} \\right|, \\quad x = e^{-y}. $$\n"
        "4. Compute:\n"
        "$$ f_Y(y) = 3(e^{-y})^2 \\cdot e^{-y} = 3e^{-3y}, \\quad y \\geq 0. $$"
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
        "$$ E[Y] = 3E\\left[ \\frac{1}{X} \\right] - 2. $$\n"
        "2. Compute \( E\\left[ \\frac{1}{X} \\right] \):\n"
        "$$ E\\left[ \\frac{1}{X} \\right] = \\int_0^1 \\frac{1}{x} \\cdot 4x^3 dx. $$\n"
        "3. Solve the integral:\n"
        "$$ \\int_0^1 x^2 dx = \\frac{1}{3}, \\quad E\\left[ \\frac{1}{X} \\right] = 4 \\times \\frac{1}{3} = \\frac{4}{3}. $$\n"
        "4. Compute \( E[Y] \):\n"
        "$$ E[Y] = 3 \\times \\frac{4}{3} - 2 = 2. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}




question_1_tiktok_dance_variance = {
    'question': (
        "Suppose 100 UGA students attempt Justin Bieber's 'Baby' TikTok dance. Their coordination scores follow a normal distribution with mean $\\mu = 15$ and variance $\\sigma^2 = 25$. What is the distribution, mean, and standard deviation of the average score?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "Distribution: Normal\n"
        "Mean = 15\n"
        "Standard Deviation = $\\sqrt{\\frac{25}{100}} = 0.5$"
    ),
    'explanation': (
        "The sample mean follows a normal distribution. The mean of the sample mean is the same as the population mean ($\\mu = 15$), "
        "while the standard deviation is scaled by the sample size $\\sqrt{\\frac{\\sigma^2}{n}} = \\sqrt{\\frac{25}{100}} = 0.5$."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_2_campus_prank_sum_variance = {
    'question': (
        "Let $X_1, X_2, \\dots, X_7$ represent daily pranks by UGA students with mean $\\mu = 5$ pranks/day and variance $\\sigma^2 = 9$. What is the variance of the total number of pranks over a week?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Variance of weekly pranks = $7 \\times 9 = 63$.",
    'explanation': (
        "The variance of the sum of independent random variables is the sum of their individual variances. "
        "Thus, for the weekly pranks: $\\text{Var}(S) = 7 \\times 9 = 63$."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_4_scaled_variable = {
    'question': (
        "Suppose $X \\sim \\text{Exp}(\\lambda = 1)$, where $X$ follows an exponential distribution with rate $\\lambda = 1$. "
        "Let $Y = 3X + 2$. What are the mean and standard deviation of $Y$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The mean is 5 and the standard deviation is 3.",
    'explanation': (
        "For a scaled and shifted variable $Y = aX + b$, the mean and standard deviation are given by:\n"
        "$$ \\mu_Y = a\\mu_X + b, \\quad \\sigma_Y = |a|\\sigma_X. $$\n"
        "For $X \\sim \\text{Exp}(1)$, we know:\n"
        "- $\\mu_X = \\frac{1}{\\lambda} = 1$,\n"
        "- $\\sigma_X = \\frac{1}{\\lambda} = 1$.\n"
        "So for $Y = 3X + 2$:\n"
        "- $\\mu_Y = 3(1) + 2 = 5$,\n"
        "- $\\sigma_Y = |3| \\times 1 = 3$."
    ),
    'chapter_information': "DeepSeek Generated"
}





question_3_math_study_escape_clt = {
    'question': (
        "Kids study math 8 hours/day to avoid trouble (with a standard deviation of $\\sigma = 2.5$ hours). "
        "If 49 kids are sampled, what is the probability that the average study time is greater than 8.5 hours?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "New standard deviation = $\\frac{2.5}{\\sqrt{49}} \\approx 0.357$\n"
        "Z = $\\frac{8.5 - 8}{0.357} \\approx 1.4$\n"
        "Probability: $P(Z > 1.4) \\approx 0.0808$"
    ),
    'explanation': (
        "By the Central Limit Theorem, the sample mean is approximately normally distributed. "
        "The standard deviation of the sample mean is $\\frac{\\sigma}{\\sqrt{n}} = \\frac{2.5}{\\sqrt{49}} \\approx 0.357$. "
        "We then calculate the Z-score and use the standard normal table to find $P(Z > 1.4) \\approx 0.0808$."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_4_bieber_video_time_scaling = {
    'question': (
        "Time spent watching Justin Bieber's cringe compilation videos follows an exponential distribution with rate $\\lambda = 0.25$. "
        "Let $Y = 3X + 5$, where $X$ is the number of hours. What are the mean and standard deviation of $Y$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "Mean of $Y$: $\\mu_Y = 3 \\times 4 + 5 = 17$\n"
        "Standard deviation of $Y$: $\\sigma_Y = 3 \\times 1 = 12$"
    ),
    'explanation': (
        "For a scaled and shifted random variable $Y = aX + b$, the mean and standard deviation are given by:\n"
        "$$ \\mu_Y = a\\mu_X + b, \\quad \\sigma_Y = |a|\\sigma_X. $$\n"
        "For $X \\sim \\text{Exp}(0.25)$, $\\mu_X = 4$ and $\\sigma_X = 4$, so for $Y = 3X + 5$, we get $\\mu_Y = 17$ and $\\sigma_Y = 12$."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_5_math_app_marathon_probability = {
    'question': (
        "150 kids use a math app, where each kid's score follows a uniform distribution $\\text{Unif}(0, 20)$. "
        "What is the probability that the total score of all 150 kids is less than 2500?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability is approximately 1.",
    'explanation': (
        "The sum of the scores can be approximated by a normal distribution using the Central Limit Theorem. "
        "For $X_i \\sim \\text{Unif}(0, 20)$, the mean is $\\mu_X = 10$ and the variance is $\\sigma_X^2 = \\frac{400}{12} \\approx 33.33$. "
        "The mean of the total score is $\\mu_{\\text{total}} = 150 \\times 10 = 1500$, and the standard deviation is $\\sigma_{\\text{total}} \\approx 70.71$. "
        "We calculate the Z-score for $S < 2500$:\n"
        "$$ Z = \\frac{2500 - 1500}{70.71} \\approx 14.14 $$\n"
        "Since the Z-score is extremely large, the probability is essentially 1."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_6_concert_attendance_variability = {
    'question': (
        "Let $X_1, X_2, \\dots, X_{30}$ represent the number of Bieber concerts attended by 30 students, with $\\sigma^2 = 16$. "
        "What is the variance of the total number of concerts attended and the variance of the sample mean?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "Variance of sum: $\\text{Var}(S) = 30 \\times 16 = 480$\n"
        "Variance of sample mean: $\\text{Var}(\\bar{X}) = \\frac{16}{30} \\approx 0.533$"
    ),
    'explanation': (
        "The variance of the sum of independent random variables is the sum of their individual variances. "
        "Thus, for the sum $S = X_1 + X_2 + \\dots + X_{30}$, we have $\\text{Var}(S) = 30 \\times 16 = 480$. "
        "For the sample mean, the variance is $\\text{Var}(\\bar{X}) = \\frac{\\sigma^2}{n} = \\frac{16}{30} \\approx 0.533$."
    ),
    'chapter_information': "DeepSeek Generated"
}





question_5_normal_approximation = {
    'question': (
        "Suppose \( X_1, X_2, \dots, X_{200} \) are i.i.d. random variables from a uniform distribution \( \text{Unif}(0,10) \). "
        "What is the probability that the sum \( \sum_{i=1}^{200} X_i \) is less than 1800?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability is essentially 1 (very close to 1).",
    'explanation': (
        "The sum of the random variables \( S = \sum_{i=1}^{200} X_i \) can be approximated by a normal distribution using the Central Limit Theorem.\n"
        "For \( X_i \sim \text{Unif}(0,10) \), we know:\n"
        "- \( \mu_X = \frac{0 + 10}{2} = 5 \),\n"
        "- \( \sigma_X^2 = \frac{(10 - 0)^2}{12} = \frac{100}{12} \approx 8.33 \).\n"
        "Now for the sum \( S = \sum_{i=1}^{200} X_i \):\n"
        "- \( \mu_S = 200 \times 5 = 1000 \),\n"
        "- \( \sigma_S^2 = 200 \times 8.33 \approx 1666.67 \), so \( \sigma_S \approx 40.82 \).\n"
        "To find \( P(S < 1800) \), we use the Z-score formula:\n"
        "$$ Z = \frac{1800 - 1000}{40.82} \approx 19.64. $$\n"
        "Since \( Z = 19.64 \) is very large, the probability is essentially 1."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_6_variance_sample_mean_sum = {
    'question': (
        "Suppose \( X_1, X_2, \dots, X_{25} \) are i.i.d. random variables with variance \( \sigma^2 = 4 \). "
        "Calculate the variance of the sum \( S = \sum_{i=1}^{25} X_i \) and the variance of the sample mean \( \bar{X} \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of the sum is 100, and the variance of the sample mean is 0.16.",
    'explanation': (
        "The variance of the sum of independent random variables is the sum of their individual variances.\n"
        "For the sum \( S = \sum_{i=1}^{25} X_i \):\n"
        "$$ \text{Var}(S) = 25 \times 4 = 100. $$\n"
        "The variance of the sample mean is:\n"
        "$$ \text{Var}(\bar{X}) = \frac{\text{Var}(X)}{n} = \frac{4}{25} = 0.16. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_1_transforming_random_variables = {
    'question': (
        "Let $X$ be a continuous random variable with a uniform distribution on the interval $[0,1]$. Define a new random variable $Y = X^2$. "
        "What is the probability density function (pdf) of $Y$? "
        "What is the expected value $E[Y]$ and variance $Var(Y)$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "The pdf of $Y$ is $f_Y(y) = 2(1 - y), \quad 0 < y < 1$. "
        "The expected value $E[Y] = \\frac{1}{3}$ and variance $Var(Y) = \\frac{4}{45}$."
    ),
    'explanation': (
        "1. **Find the range of $Y$:**\n"
        "   - When $x = 0$, $Y = 1$. When $x = 1$, $Y = 0$.\n"
        "   Thus, $Y$ ranges from $0$ to $1$.\n\n"
        "2. **Find the inverse transformation:**\n"
        "$$ x = 1 - Y. $$\n"
        "Compute the derivative:\n"
        "$$ \\frac{dx}{dy} = -1. $$\n"
        "Taking the absolute value: $|dx/dy| = 1$.\n\n"
        "3. **Apply the transformation formula:**\n"
        "$$ f_Y(y) = f_X(x) |dx/dy| = 2(1 - y), \quad 0 < y < 1. $$\n"
        "4. **Expected value of $Y$:**\n"
        "$$ E[Y] = \\int_0^1 y \\cdot f_Y(y) \, dy = \\frac{1}{3}. $$\n"
        "5. **Variance of $Y$:**\n"
        "$$ Var(Y) = E[Y^2] - (E[Y])^2 = \\frac{4}{45}. $$"
    ),
    'chapter_information': "GPT Generated"
}

question_2_clt = {
    'question': (
        "You are given a random variable $X$ that follows a normal distribution with mean $\\mu = 50$ and variance $\\sigma^2 = 25$. "
        "You take a sample of size $n = 36$. "
        "What is the distribution of the sample mean $\\overline{X}$? "
        "What is the standard deviation of $\\overline{X}$? "
        "Using the Central Limit Theorem, calculate the probability that the sample mean is between 48 and 52."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "The distribution of $\\overline{X}$ is $\\mathcal{N}(50, \\frac{25}{36})$, and the standard deviation of $\\overline{X}$ is $\\frac{5}{6}$. "
        "The probability that the sample mean is between 48 and 52 is approximately 98.36%."
    ),
    'explanation': (
        "1. By the CLT, the sample mean $\\overline{X}$ follows a normal distribution with the same mean $\\mu = 50$ and variance $\\frac{\\sigma^2}{n} = \\frac{25}{36}$.\n"
        "   Therefore, $\\overline{X} \\sim \\mathcal{N}(50, \\frac{25}{36}).$\n\n"
        "2. The standard deviation of $\\overline{X}$ is:\n"
        "$$ SD(\\overline{X}) = \\frac{5}{6}. $$\n\n"
        "3. To calculate the probability that $\\overline{X}$ is between 48 and 52, we standardize the range using the Z-score:\n"
        "$$ Z = \\frac{X - \\mu}{SD(\\overline{X})} $$\n"
        "For $X = 48$, we get:\n"
        "$$ Z_1 = \\frac{48 - 50}{5/6} = -2.4 $$\n"
        "For $X = 52$, we get:\n"
        "$$ Z_2 = \\frac{52 - 50}{5/6} = 2.4 $$\n"
        "Using standard normal tables, we find the probability between $-2.4$ and $2.4$ is $P(-2.4 < Z < 2.4) = 0.9836$."
    ),
    'chapter_information': "GPT Generated"
}

question_3_clt_estimation = {
    'question': (
        "Suppose you are estimating the population mean $\\mu$ of a population with an unknown distribution. "
        "You take a random sample of size $n = 100$, and you find that the sample mean is $\\overline{X} = 80$ and the sample standard deviation is $s = 10$. "
        "Use the Central Limit Theorem to estimate the population mean $\\mu$ and the standard deviation of the sample mean. "
        "What is the 95% confidence interval for the population mean $\\mu$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "Estimated mean: $\\hat{\\mu} = 80$. Estimated standard deviation of the sample mean: $\\hat{\\sigma}_{\\overline{X}} = 1$. "
        "The 95% confidence interval for the population mean $\\mu$ is $(78.04, 81.96)$."
    ),
    'explanation': (
        "1. By the Central Limit Theorem, the sample mean $\\overline{X}$ follows a normal distribution with mean $\\mu$ and standard deviation $\\frac{s}{\\sqrt{n}}$.\n"
        "   Thus, the estimated standard deviation of the sample mean is $\\hat{\\sigma}_{\\overline{X}} = \\frac{10}{\\sqrt{100}} = 1$.\n\n"
        "2. The 95% confidence interval for the population mean is given by:\n"
        "$$ \\overline{X} \\pm Z_{\\alpha/2} \\cdot \\frac{s}{\\sqrt{n}} $$\n"
        "   Using $Z_{\\alpha/2} = 1.96$ for a 95% confidence level, the confidence interval is:\n"
        "$$ (80 - 1.96 \\cdot 1, 80 + 1.96 \\cdot 1) = (78.04, 81.96). $$"
    ),
    'chapter_information': "GPT Generated"
}

question_5_normal_approximation = {
    'question': (
        "A group of 200 students from the University of Georgia each randomly spend between 0 and 10 hours per week watching Justin Bieber videos. "
        "The total sum of hours spent by all the students is being tracked. What is the probability that the total sum is less than 1800 hours?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability is essentially 1 (very close to 1).",
    'explanation': (
        "The sum of the random variables $S = \\sum X_i$ can be approximated by a normal distribution using the Central Limit Theorem. "
        "The mean of each $X_i$ is $\\mu = \\frac{10 + 0}{2} = 5$, and the variance is $\\sigma^2 = \\frac{(10 - 0)^2}{12} \\approx 8.33$.\n"
        "The mean of the sum is $\\mu_S = 200 \\times 5 = 1000$. The variance of the sum is $\\sigma_S^2 = 200 \\times 8.33 \\approx 1666.67$, so the standard deviation is $\\sigma_S \\approx 40.82$.\n"
        "Now, we find $P(S < 1800)$ using the Z-score formula:\n"
        "- $Z = \\frac{1800 - 1000}{40.82} \\approx 19.64$.\n"
        "Since $Z = 19.64$ is very large, the probability is essentially 1."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_6_variance_sa3mple_mean_sum = {
    'question': (
        "Suppose 25 kids from the neighborhood, each studying math, score on average 75 on their math test, with a variance of 16. "
        "Calculate the variance of the sum of their scores and the variance of the sample mean."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of the sum is 400, and the variance of the sample mean is 0.64.",
    'explanation': (
        "For the sum of independent random variables:\n"
        "- $\\text{Var}(S) = \\text{Var}(X_1) + \\dots + \\text{Var}(X_{25}) = 25 \\times 16 = 400$\n"
        "For the sample mean:\n"
        "- $\\text{Var}(\\bar{X}) = \\frac{\\text{Var}(X)}{n} = \\frac{16}{25} = 0.64$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_1_sam3ple_mean_distribution = {
    'question': (
        "Suppose you have a random sample of 50 observations, $X_1, X_2, \\dots, X_{50}$, from a population that follows a normal distribution with mean $\\mu = 20$ and variance $\\sigma^2 = 16$.\n\n"
        "What is the distribution of the sample mean $\\bar{X}$? What is the mean and standard deviation of $\\bar{X}$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "The sample mean $\\bar{X}$ follows a normal distribution with mean $\\mu_{\\bar{X}} = \\mu = 20$ and standard deviation $\\sigma_{\\bar{X}} = \\frac{\\sigma}{\\sqrt{n}} = \\frac{4}{\\sqrt{50}} \\approx 0.566$."
    ),
    'explanation': (
        "The sample mean follows a normal distribution because the population is normally distributed.\n"
        "The mean of the sample mean is the same as the population mean $\\mu = 20$.\n"
        "The variance of the sample mean is $\\frac{\\sigma^2}{n} = \\frac{16}{50} = 0.32$, and the standard deviation is $\\sqrt{0.32} \\approx 0.566$."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_2_var3iance_of_sum = {
    'question': (
        "Let $X_1, X_2, \\dots, X_5$ be i.i.d. random variables with mean $\\mu = 10$ and variance $\\sigma^2 = 25$. What is the variance of the sum $S = X_1 + X_2 + X_3 + X_4 + X_5$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of the sum $S$ is 125.",
    'explanation': (
        "The variance of a sum of independent random variables is the sum of their individual variances.\n"
        "For the sum $S = X_1 + X_2 + X_3 + X_4 + X_5$:\n"
        "$$ \\text{Var}(S) = \\text{Var}(X_1) + \\text{Var}(X_2) + \\dots + \\text{Var}(X_5) = 5 \\times 25 = 125. $$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_3_cen3tral_limit_theorem = {
    'question': (
        "Suppose you have a population where the random variable $X$ has a mean $\\mu = 50$ and a standard deviation $\\sigma = 10$. "
        "You take a random sample of size $n = 64$. Using the Central Limit Theorem, what is the probability that the sample mean $\\bar{X}$ is greater than 52?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability is approximately 0.0548.",
    'explanation': (
        "According to the Central Limit Theorem, the sample mean $\\bar{X}$ will be approximately normally distributed.\n"
        "The mean of $\\bar{X}$ is $\\mu_{\\bar{X}} = \\mu = 50$, and the standard deviation of $\\bar{X}$ is:\n"
        "$$ \\sigma_{\\bar{X}} = \\frac{\\sigma}{\\sqrt{n}} = \\frac{10}{\\sqrt{64}} = 1.25. $$\n"
        "Now, we want to find $P(\\bar{X} > 52)$:\n"
        "$$ Z = \\frac{52 - 50}{1.25} = 1.6. $$\n"
        "Using the standard normal table, $P(Z > 1.6) \\approx 0.0548$."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_1_sample_mean_distribution = {
    'question': (
        "Suppose a group of 100 Justin Bieber fans are randomly surveyed, and they report how much they hate his worst song 'Baby' "
        "on a scale from 1 (most hated) to 10 (most loved). The average rating is 3 with a variance of 4. "
        "What is the distribution of the sample mean of these ratings? What is the mean and standard deviation of the sample mean?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The sample mean follows a normal distribution with mean $\\mu_{\\bar{X}} = 3$ and standard deviation $\\sigma_{\\bar{X}} = 0.2$.",
    'explanation': (
        "The sample mean follows a normal distribution because the population (the ratings) is considered to be normally distributed. "
        "The mean of the sample mean is the same as the population mean ($\\mu = 3$). "
        "The standard deviation of the sample mean is the population standard deviation divided by the square root of the sample size. "
        "For the sample of size 100, we get:\n"
        "- $\\mu_{\\bar{X}} = \\mu = 3$\n"
        "- $\\sigma_{\\bar{X}} = \\frac{\\sigma}{\\sqrt{n}} = \\frac{2}{\\sqrt{100}} = 0.2$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_2_va5riance_of_sum = {
    'question': (
        "A group of 5 University of Georgia students, each with an intelligence score (measured on a 1–10 scale), are randomly selected. "
        "The students' scores are independent with a mean of 6 and a variance of 4. What is the variance of the sum of their intelligence scores?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The variance of the sum of their intelligence scores is 20.",
    'explanation': (
        "The variance of the sum of independent random variables is the sum of their individual variances. So:\n"
        "- $\\text{Var}(S) = \\text{Var}(X_1) + \\text{Var}(X_2) + \\dots + \\text{Var}(X_5) = 5 \\times 4 = 20$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_3_cen0tral_limit_theorem = {
    'question': (
        "A group of 64 kids in a neighborhood study math to stay off the streets. The average score on their math test is 80, with a standard deviation of 12. "
        "According to the Central Limit Theorem, what is the probability that the average score of a random sample of 64 kids will be greater than 85?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The probability is approximately 0.04%.",
    'explanation': (
        "The sample mean will follow a normal distribution due to the Central Limit Theorem. The mean of the sample mean is $\\mu = 80$, "
        "and the standard deviation of the sample mean is:\n"
        "- $\\sigma_{\\bar{X}} = \\frac{\\sigma}{\\sqrt{n}} = \\frac{12}{\\sqrt{64}} = 1.5$.\n"
        "To find $P(\\bar{X} > 85)$, we use the Z-score formula:\n"
        "- $Z = \\frac{85 - 80}{1.5} = 3.33$.\n"
        "Using the standard normal table, $P(Z > 3.33) \\approx 0.0004$, which is about 0.04%."
    ),
    'chapter_information': "DeepSeek Generated"
}

question_4_scal0ed_variable = {
    'question': (
        "Suppose the number of times people listened to Justin Bieber's 'Baby' on repeat in one week follows an exponential distribution with rate $\\lambda = 2$. "
        "Let $Y = 5X + 1$, where $X$ is the number of listens. What are the mean and standard deviation of $Y$?"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The mean is 3.5 and the standard deviation is 2.5.",
    'explanation': (
        "For a scaled and shifted variable $Y = aX + b$, the mean and standard deviation are:\n"
        "- $\\mu_Y = a\\mu_X + b$\n"
        "- $\\sigma_Y = |a|\\sigma_X$\n"
        "Given $X \\sim \\text{Exp}(2)$, we know:\n"
        "- $\\mu_X = \\frac{1}{\\lambda} = 0.5$\n"
        "- $\\sigma_X = \\frac{1}{\\lambda} = 0.5$.\n"
        "So, for $Y = 5X + 1$:\n"
        "- $\\mu_Y = 5(0.5) + 1 = 3.5$\n"
        "- $\\sigma_Y = |5| \\times 0.5 = 2.5$"
    ),
    'chapter_information': "DeepSeek Generated"
}

question_1_condition1al_probability_cdf_transformation = {
    'question': (
        "Let $X \\sim \\text{Uniform}(0,1)$ and $Y = X^2$. "
        "Find $P(Y \\leq 0.25 | Y \\leq 0.5)$.\n"
        "(Use the CDF method and the conditional probability formula.)"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "Using the conditional probability formula:\n"
        "$P(Y \\leq 0.25 | Y \\leq 0.5) = \\frac{P(Y \\leq 0.25)}{P(Y \\leq 0.5)} = \\frac{0.5}{\\sqrt{0.5}} \\approx 0.707$."
    ),
    'explanation': (
        "1. We know that $Y = X^2$, so $P(Y \\leq 0.25) = P(X \\leq 0.5) = 0.5$.\n"
        "2. Similarly, $P(Y \\leq 0.5) = P(X \\leq \\sqrt{0.5}) \\approx 0.707$.\n"
        "3. Finally, we apply the conditional probability formula:\n"
        "$P(Y \\leq 0.25 | Y \\leq 0.5) = \\frac{P(Y \\leq 0.25)}{P(Y \\leq 0.5)} \\approx 0.707$."
    ),
    'chapter_information': "GPT 04 Generated"
}

question_2_m1onte_carlo_integration = {
    'question': (
        "Consider the integral $I = \\int_0^1 e^{-x^2} dx$. Use the Monte Carlo method with 4 pseudo-random numbers "
        "$U_1 = 0.1, U_2 = 0.3, U_3 = 0.6, U_4 = 0.9$ to estimate the integral."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "Using the Monte Carlo method, we compute the function values at each $U_i$ and then average them:\n"
        "$I \\approx \\frac{1}{4} (f(U_1) + f(U_2) + f(U_3) + f(U_4)) = 0.7616$."
    ),
    'explanation': (
        "The Monte Carlo estimate for the integral is:\n"
        "$I_n = \\frac{1}{n} \\sum_{i=1}^n f(U_i)$.\n"
        "For each $U_i$, we calculate $f(U_i) = e^{-U_i^2}$:\n"
        "- $f(U_1) = e^{-0.1^2} \\approx 0.9900$\n"
        "- $f(U_2) = e^{-0.3^2} \\approx 0.9139$\n"
        "- $f(U_3) = e^{-0.6^2} \\approx 0.6977$\n"
        "- $f(U_4) = e^{-0.9^2} \\approx 0.4449$\n"
        "Thus, the Monte Carlo estimate is $I_n \\approx 0.7616$."
    ),
    'chapter_information': "GPT 04 Generated"
}

question_3_inver1se_transform_method = {
    'question': (
        "Let $X$ be a discrete random variable with the following PMF:\n"
        "$P(X=x) = \\begin{cases} 0.2 & \\text{if } x=0, \\\\ 0.5 & \\text{if } x=1, \\\\ 0.3 & \\text{if } x=2. \\end{cases}$\n"
        "Use the inverse transform method with $U = 0.75$ to generate one observation of $X$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The generated observation is $X = 1$.",
    'explanation': (
        "The CDF of $X$ is:\n"
        "$F(0) = 0.2, F(1) = 0.7, F(2) = 1.0$.\n"
        "Given $U = 0.75$, we find that $U$ lies in the range $[0.7, 1.0)$, corresponding to $X = 1$."
    ),
    'chapter_information': "GPT 04 Generated"
}

question_4_transfo1rmation_of_random_variables = {
    'question': (
        "Suppose $X \\sim \\text{Exponential}(1)$ and $Y = \\ln(X)$. Find the PDF of $Y$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The PDF of $Y$ is $f_Y(y) = e^y e^{-e^y}, \\quad y \\in (-\\infty, \\infty)$.",
    'explanation': (
        "The transformation is $Y = \\ln(X)$.\n"
        "Using the change of variables method, we get the PDF of $Y$ as:\n"
        "$f_Y(y) = f_X(e^y) |\\frac{d}{dy} e^y| = e^y e^{-e^y}$. Thus, the PDF of $Y$ is:\n"
        "$f_Y(y) = e^y e^{-e^y}, \\quad y \\in (-\\infty, \\infty)$."
    ),
    'chapter_information': "GPT 04 Generated"
}

question_5_relationshi1p_between_distributions = {
    'question': (
        "Let $X \\sim \\text{Normal}(0, 1)$ and $Y = X^2$. Find the PDF of $Y$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': (
        "The PDF of $Y$ is $f_Y(y) = \\frac{1}{\\sqrt{2\\pi y}} e^{-\\frac{y}{2}}, \\quad y \\geq 0$."
    ),
    'explanation': (
        "Let $X \\sim \\text{Normal}(0, 1)$, so the PDF of $X$ is:\n"
        "$f_X(x) = \\frac{1}{\\sqrt{2\\pi}} e^{-\\frac{x^2}{2}}$.\n"
        "To find the PDF of $Y = X^2$, we use the change of variables:\n"
        "$Y = X^2$ implies $X = \\pm\\sqrt{Y}$, and the derivative of $\\sqrt{Y}$ is $\\frac{1}{2\\sqrt{Y}}$.\n"
        "Thus, the PDF of $Y$ is:\n"
        "$f_Y(y) = 2 f_X(\\sqrt{y}) \\frac{1}{2\\sqrt{y}} = \\frac{1}{\\sqrt{2\\pi y}} e^{-\\frac{y}{2}}, \\quad y \\geq 0$."
    ),
    'chapter_information': "GPT 04 Generated"
}








KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MIDTERM_1_MPC = KC_MPC_QUESTIONS[:-1]