

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

KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_7_MPC = KC_MPC_QUESTIONS[:-1]