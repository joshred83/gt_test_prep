

question_1_unif_to_other_distributions = {
    'question': (
        "TRUE or FALSE? Unif(0,1) random variables can be used to generate random variables from any continuous "
        "distribution, such as exponential, gamma, and lognormal, using the appropriate transformations."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "Using the inverse transform method, you can generate random variables from any continuous distribution "
        "by applying the inverse of the cumulative distribution function (c.d.f.) to Unif(0,1) random variables. "
        "This is a common technique for generating random variables from non-uniform distributions."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_2_inverse_transform_uniform = {
    'question': (
        "If $U \\sim Unif(0,1)$, what is the distribution of $-\\ln(U)$?"
    ),
    'options_list': [
        'Exp(1)', 'Exp(\\lambda)', 'Normal(0,1)', 'Lognormal', 'Uniform(0,1)'
    ],
    'correct_answer': 'Exp(1)',
    'explanation': (
        "If $U \\sim Unif(0,1)$, then $-\\ln(U)$ follows an Exponential distribution with parameter $\\lambda=1$. "
        "This is a standard result from inverse transform sampling for the exponential distribution."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_3_exponential_random_variables = {
    'question': (
        "If $U \\sim Unif(0,1)$, what distribution does $-\\ln(U)$ follow?"
    ),
    'options_list': [
        'Uniform(0,1)', 'Exponential(\\lambda)', 'Lognormal', 'Normal(0,1)'
    ],
    'correct_answer': 'Exponential(\\lambda)',
    'explanation': (
        "As per the inverse transform method, $-\\ln(U)$, where $U \\sim Unif(0,1)$, will follow an Exponential "
        "distribution with rate $\\lambda=1$. This transformation is frequently used to simulate exponential random "
        "variables from uniformly distributed random numbers."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_4_sum_two_uniforms = {
    'question': (
        "If $X_1 \\sim Unif(0,1)$ and $X_2 \\sim Unif(0,1)$, what is the distribution of $X_1 + X_2$?"
    ),
    'options_list': [
        'Uniform(0,2)', 'Normal(0,2)', 'Triangular(0,1,2)', 'Exponential(1)', 'None of the above'
    ],
    'correct_answer': 'Triangular(0,1,2)',
    'explanation': (
        "The sum of two independent $Unif(0,1)$ random variables follows a triangular distribution with support on "
        "the interval [0, 2]. This distribution has a peak at 1 and is symmetric about that value."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_5_inverse_normal_cdf = {
    'question': (
        "TRUE or FALSE? The inverse c.d.f. of the standard normal distribution can be computed directly using a closed-form expression."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "The inverse c.d.f. (quantile function) of the standard normal distribution does not have a closed-form solution. "
        "It must be approximated using numerical methods like the Newton-Raphson method or through precomputed tables or "
        "algorithms such as Erf."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_6_discrete_random_variables = {
    'question': (
        "If $U \\sim Unif(0,1)$, what distribution does $\\lceil 6U \\rceil$ represent?"
    ),
    'options_list': [
        'Geometric(1/6)', 'Bernoulli(1/6)', 'Uniform(0,6)', 'Discrete Uniform(1,6)'
    ],
    'correct_answer': 'Discrete Uniform(1,6)',
    'explanation': (
        "The transformation $\\lceil 6U \\rceil$, where $U \\sim Unif(0,1)$, produces a discrete random variable "
        "with a uniform distribution on the set {1, 2, 3, 4, 5, 6}. This is equivalent to simulating the roll of a 6-sided die."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_7_convolution_method = {
    'question': (
        "TRUE or FALSE? The convolution method is used to find the distribution of the sum of two independent random variables."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "The convolution method is used to find the probability distribution of the sum of two or more independent random "
        "variables. This method involves convolving the probability density functions (p.d.f.s) of the individual variables."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_8_acceptance_rejection_method = {
    'question': (
        "TRUE or FALSE? In the acceptance-rejection method, you accept a generated value only if it lies below the target distribution’s c.d.f. value."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "In the acceptance-rejection method, a value is generated using a proposal distribution. If the value lies below "
        "the acceptance criterion (which often involves the c.d.f. of the target distribution), it is accepted. If not, "
        "it is rejected and the process is repeated."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_9_box_muller_transform = {
    'question': (
        "What method would you use to generate a normal distribution from a pair of Unif(0,1) random variables?"
    ),
    'options_list': [
        'Box-Muller transform', 'Inverse transform', 'Rejection sampling', 'Central Limit Theorem'
    ],
    'correct_answer': 'Box-Muller transform',
    'explanation': (
        "The Box-Muller transform is a method used to generate pairs of independent standard normal variables from two "
        "independent Unif(0,1) random variables. This method is widely used in simulations."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_10_sum_of_exponentials = {
    'question': (
        "If $X_1 \\sim Exp(1)$ and $X_2 \\sim Exp(1)$, what is the distribution of $X_1 + X_2$?"
    ),
    'options_list': [
        'Exponential(2)', 'Gamma(2, 1)', 'Normal(2, 2)', 'Uniform(0, 2)'
    ],
    'correct_answer': 'Gamma(2, 1)',
    'explanation': (
        "The sum of two independent exponential random variables with the same rate $\\lambda=1$ follows a Gamma distribution "
        "with shape parameter $k=2$ and rate $\\lambda=1$. The Gamma distribution generalizes the exponential distribution."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}

question_11_poisson_distribution = {
    'question': (
        "Which method can be used to generate a Poisson distribution using Unif(0,1) random variables?"
    ),
    'options_list': [
        'Inverse transform method', 'Acceptance-rejection method', 'Convolution method', 'Box-Muller transform'
    ],
    'correct_answer': 'Inverse transform method',
    'explanation': (
        "The inverse transform method can be used to generate Poisson-distributed random variables by applying the inverse "
        "of the Poisson distribution’s c.d.f. to a Unif(0,1) random variable. The result is a Poisson random variable."
    ),
    'chapter_information': 'Module 7 Week 8 - chat gpt'
}



###############################

# Reformatting each question into separate Python dictionaries following the quiz app structure

question_1_gamma_transformation = {
    'question': (
        "If $X \\sim \\text{Gamma}(\\alpha, \\beta)$ and $Y = X/\\beta$, what is the distribution of $Y$?"
    ),
    'options_list': ['Gamma(α, 1)', 'Gamma(1, β)', 'Exponential(β)', 'Uniform(0,1)'],
    'correct_answer': 'Gamma(α, 1)',
    'explanation': (
        "Transforming $Y = X/\\beta$, apply change of variable with Jacobian $1/\\beta$.\n"
        "PDF becomes: $f_Y(y) = \\frac{1}{\\Gamma(\\alpha)} y^{\\alpha - 1} e^{-y}$, which is Gamma$(\\alpha, 1)$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_2_ln_uniform = {
    'question': (
        "Let $U_1 \\sim \\text{Unif}(0,1)$. What is the distribution of $Z = -\\ln(U_1)$?"
    ),
    'options_list': ['Exponential(1)', 'Gamma(2,1)', 'Uniform(0,1)', 'Normal(0,1)'],
    'correct_answer': 'Exponential(1)',
    'explanation': (
        "CDF of $Z$ is $P(-\\ln(U_1) \\le x) = P(U_1 \\ge e^{-x}) = 1 - e^{-x}$ for $x > 0$, "
        "which matches the CDF of Exp(1)."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_3_expected_inverse_pdf = {
    'question': (
        "Suppose $X$ has CDF $F(x)$ and PDF $f(x)$, and $Y = F(X)$. What is $\\mathbb{E}[1/f(X)]$?"
    ),
    'options_list': ['1', '0', 'Depends on $f$', 'Cannot be determined'],
    'correct_answer': '1',
    'explanation': (
        "$Y = F(X) \\sim \\text{Unif}(0,1)$. Then:\n"
        "$\\mathbb{E}[1/f(X)] = \\int_0^1 \\frac{1}{f(x)} f(x) dx = \\int_0^1 dx = 1$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_4_inverse_transform = {
    'question': (
        "You want to generate a random variable from $f(x) = 3x^2$ for $0 \\le x \\le 1$. "
        "If $U = 0.729$, what is the generated value using inverse transform?"
    ),
    'options_list': ['0.9', '0.81', '0.6', '0.27'],
    'correct_answer': '0.9',
    'explanation': (
        "CDF: $F(x) = x^3$. Solve $x^3 = 0.729$ gives $x = 0.9$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_5_clt_exponential_sum = {
    'question': (
        "Let $X_1, ..., X_{12}$ be i.i.d. Exponential(1). What is the approximate distribution of "
        "$Y = (\\sum X_i - 12)/\\sqrt{12}$?"
    ),
    'options_list': ['Normal(0,1)', 'Gamma(12,1)', 'Uniform(0,1)', 'Exponential(1)'],
    'correct_answer': 'Normal(0,1)',
    'explanation': (
        "By CLT, $\\sum X_i \\approx \\mathcal{N}(12, 12)$. Standardizing gives $Y \\sim \\mathcal{N}(0,1)$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_6_acceptance_rejection_c = {
    'question': (
        "You want to use the acceptance-rejection method to generate from Beta(2,3) using Unif(0,1) proposal. "
        "What is the minimum value of constant $c$?"
    ),
    'options_list': ['16/9', '4/3', '2', '1'],
    'correct_answer': '16/9',
    'explanation': (
        "Beta(2,3) has $f(x) = 12x(1-x)^2$. Max at $x = 1/3$ gives $f(1/3) = 16/9$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_7_ln_product_uniforms = {
    'question': (
        "Let $U_1, U_2, U_3 \\sim \\text{Unif}(0,1)$. What is the distribution of "
        "$X = -\\ln(U_1 U_2 U_3)$?"
    ),
    'options_list': ['Gamma(3,1)', 'Exponential(1)', 'Normal(0,1)', 'Beta(3,1)'],
    'correct_answer': 'Gamma(3,1)',
    'explanation': (
        "$X = -\\ln(U_1) - \\ln(U_2) - \\ln(U_3)$ is the sum of 3 Exp(1) RVs → Gamma(3,1)."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_8_acceptance_rate = {
    'question': (
        "You are using acceptance-rejection with $c = \\sup f(x)/g(x) = 4$. "
        "How many proposals needed to get 100 accepted values (approximately)?"
    ),
    'options_list': ['400', '100', '25', '300'],
    'correct_answer': '400',
    'explanation': (
        "Acceptance probability = $1/4$. Expected proposals = $100 / (1/4) = 400$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_9_weibull_inverse = {
    'question': (
        "If $X$ follows Weibull with $F(x) = 1 - e^{-(x/\\lambda)^k}$ and $U \\sim \\text{Unif}(0,1)$, what is the inverse transform expression?"
    ),
    'options_list': ['X = λ[-ln(1-U)]^{1/k}', 'X = λU^{1/k}', 'X = -ln(U)/λ', 'X = λU^k'],
    'correct_answer': 'X = λ[-ln(1-U)]^{1/k}',
    'explanation': (
        "Set $F(x) = U$, solve: $1 - e^{-(x/\\lambda)^k} = U$ → $x = \\lambda[-\\ln(1 - U)]^{1/k}$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}

question_10_clt_probability_interval = {
    'question': (
        "Let $X_1, ..., X_{100}$ be i.i.d. with $\\mathbb{E}[X] = 5$, $\\text{Var}(X) = 9$. "
        "Approximate $P(490 < \\sum X_i < 510)$ using CLT."
    ),
    'options_list': ['0.2586', '0.6826', '0.9544', '0.3413'],
    'correct_answer': '0.2586',
    'explanation': (
        "Sum has $\\mu = 500$, $\\sigma = \\sqrt{900} = 30$.\n"
        "Standardize: $P(-1/3 < Z < 1/3) = \\Phi(1/3) - \\Phi(-1/3) = 0.6293 - 0.3707 = 0.2586$."
    ),
    'chapter_information': 'Module 7 (Claude 3.7 generated - deepseek checked)'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_7_MPC = KC_MPC_QUESTIONS[:-1]