
isye6739_module2_discrete_rv_question_4 = {
    'question': "Suppose $X \\sim \\text{Pois}(10)$. What is the probability that a cup of dough has at least 4 raisins?",
    'options_list': [
        'A) $1 - \\sum_{k=0}^3 \\frac{10^k e^{-10}}{k!}$',
        'B) $\\sum_{k=4}^\\infty \\frac{10^k e^{-10}}{k!}$',
        'C) $1 - \\frac{e^{-10} (10^0 + 10^1 + 10^2 + 10^3)}{3!}$',
        'D) $\\frac{e^{-10} (10^4 + 10^5)}{4!}$'
    ],
    'correct_answer': 'A) $1 - \\sum_{k=0}^3 \\frac{10^k e^{-10}}{k!}$',
    'explanation': (
        "The Poisson distribution probability mass function is:\n"
        "$P(X = k) = \\frac{\\lambda^k e^{-\\lambda}}{k!}$.\n"
        "To find $P(X \\geq 4)$, use the complement rule:\n"
        "$P(X \\geq 4) = 1 - P(X < 4) = 1 - P(X = 0, 1, 2, 3)$.\n"
        "Expanding:\n"
        "$P(X \\geq 4) = 1 - \\sum_{k=0}^3 \\frac{10^k e^{-10}}{k!}$."
    ),
    'chapter_information': 'ISYE 6739, Module 2'
}


probability_theory_ucboulder_question_6 = {
    'question': "A skilled worker requires at least 10 minutes, and no more than 20 minutes, to complete a certain task. The completion time $X$ is a continuous random variable with density function $f(x) = \\frac{c}{x^2}$ for $10 \\leq x \\leq 20$ and $f(x) = 0$ otherwise. What is the value of $c$?",
    'options_list': [
        'A) 20',
        'B) 10',
        'C) 0.5',
        'D) 1'
    ],
    'correct_answer': 'A) 20',
    'explanation': (
        "To find the normalization constant $c$, ensure the total probability is 1:\n"
        "$\\int_{10}^{20} \\frac{c}{x^2} dx = 1$\n"
        "Solve:\n"
        "$\\left[ -\\frac{c}{x} \\right]_{10}^{20} = 1$\n"
        "$\\frac{c}{10} - \\frac{c}{20} = 1$\n"
        "$\\frac{2c - c}{20} = 1$\n"
        "$c = 20$."
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_7 = {
    'question': "A skilled worker requires at least 10 minutes, and no more than 20 minutes, to complete a certain task. The completion time $X$ is a continuous random variable with density function $f(x) = \\frac{c}{x^2}$ for $10 \\leq x \\leq 20$ and $f(x) = 0$ otherwise. Find the probability that the worker completes the task in 15 minutes or less. Round your answer to three decimal places.",
    'options_list': [
        'A) 0.333',
        'B) 0.667',
        'C) 0.500',
        'D) 0.250'
    ],
    'correct_answer': 'B) 0.667',
    'explanation': (
        "The cumulative probability is:\n"
        "$P(X \\leq 15) = \\int_{10}^{15} \\frac{20}{x^2} dx$\n"
        "$= 20 \\left[ -\\frac{1}{x} \\right]_{10}^{15}$\n"
        "$= 20 \\left(-\\frac{1}{15} + \\frac{1}{10}\\right)$\n"
        "$= 20 \\cdot \\frac{1}{30} = 0.667$"
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_8 = {
    'question': "A skilled worker requires at least 10 minutes, and no more than 20 minutes, to complete a certain task. The completion time $X$ is a continuous random variable with density function $f(x) = \\frac{c}{x^2}$ for $10 \\leq x \\leq 20$ and $f(x) = 0$ otherwise. Find the expected time for the worker to complete the task. Round your answer to three decimal places.",
    'options_list': [
        'A) 13.863',
        'B) 15.000',
        'C) 12.500',
        'D) 10.000'
    ],
    'correct_answer': 'A) 13.863',
    'explanation': (
        "The expected value is given by:\n"
        "$E[X] = \\int_{10}^{20} x \\cdot \\frac{20}{x^2} dx$\n"
        "$= 20 \\int_{10}^{20} \\frac{1}{x} dx$\n"
        "$= 20 \\left[ \\ln(x) \\right]_{10}^{20}$\n"
        "$= 20 \\cdot (\\ln(20) - \\ln(10))$\n"
        "$= 20 \\cdot \\ln(2) \\approx 13.863$"
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_9 = {
    'question': "The number of eggs laid on a tree leaf by an insect of a certain type is a Poisson random variable $X$ with parameter $c$, where $E(X) = c$. However, the random variable can only be observed if it is positive. Let $Y$ denote the observed number of eggs, where $P(Y=i) = P(X=i \\mid X>0)$. Find $E(Y)$.",
    'options_list': [
        'A) $\\frac{c}{1 - e^{-c}}$',
        'B) $\\frac{1 - e^{-c}}{c}$',
        'C) $1 - e^{-c}$',
        'D) $e^{-c}$'
    ],
    'correct_answer': 'A) $\\frac{c}{1 - e^{-c}}$',
    'explanation': (
        "The expected value of $Y$ is given by:\n"
        "$E[Y] = \\frac{E[X \\mid X > 0]}{P(X > 0)}$\n"
        "Since $P(X > 0) = 1 - e^{-c}$ for a Poisson random variable:\n"
        "$E[Y] = \\frac{c}{1 - e^{-c}}$"
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_10 = {
    'question': "Suppose $X$ is a random variable $X \\sim N(12, 4)$. Find the probability that $X$ is within 1.5 standard deviations of the mean. Round your answer to four decimal places.",
    'options_list': [
        'A) 0.9332',
        'B) 0.8664',
        'C) 0.0668',
        'D) 0.5000'
    ],
    'correct_answer': 'B) 0.8664',
    'explanation': (
        "For a normal random variable $X$, the probability is:\n"
        "$P(9 \\leq X \\leq 15) = P(-1.5 \\leq Z \\leq 1.5)$\n"
        "$= \\Phi(1.5) - \\Phi(-1.5)$\n"
        "$\\Phi(1.5) \\approx 0.9332$ and $\\Phi(-1.5) \\approx 0.0668$\n"
        "$P(9 \\leq X \\leq 15) = 0.9332 - 0.0668 = 0.8664$"
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}


isye6739_lecture6_question_5 = {
    'question': "Suppose $X \\sim \\text{Exp}(\\lambda)$. What is the CDF $F(x)$ of $X$?",
    'options_list': [
        'A) $F(x) = 0$ for $x \\leq 0$, $F(x) = 1 - e^{-\\lambda x}$ for $x > 0$',
        'B) $F(x) = e^{-\\lambda x}$ for $x > 0$',
        'C) $F(x) = \\lambda x$ for $x > 0$',
        'D) $F(x) = x^2$ for $x > 0$'
    ],
    'correct_answer': 'A) $F(x) = 0$ for $x \\leq 0$, $F(x) = 1 - e^{-\\lambda x}$ for $x > 0$',
    'explanation': (
        "For an exponential random variable $X$ with rate parameter $\\lambda$, the CDF is:\n"
        "$F(x) = \\int_{-\\infty}^x \\lambda e^{-\\lambda t} dt$\n"
        "This gives:\n"
        "$F(x) = \\begin{cases} 0 & x \\leq 0 \\\\ 1 - e^{-\\lambda x} & x > 0 \\end{cases}$."
    ),
    'chapter_information': 'ISYE 6739 Lecture 6'
}


problem_4_parking_lot_question = {
    'question': (
        "Mary and Tom park their cars in an empty parking lot with $n \\geq 2$ consecutive parking spaces "
        "(i.e., $n$ spaces in a row, where only one car fits in each space). Mary and Tom pick parking spaces at random, "
        "and to ensure privacy, they must each choose a different space. All pairs of distinct parking spaces are equally likely.\n\n"
        "What is the probability that there is at most one empty parking space between them?"
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(A) = \\frac{4n - 6}{n(n-1)}$",
    'explanation': (
        "1. Define the sample space as:\n"
        "$$ \\Omega = \\{(i, j) : i \\neq j, 1 \\leq i, j \\leq n\\}, $$\n"
        "where $(i, j)$ indicates that Mary and Tom parked in slots $i$ and $j$, respectively.\n\n"
        "2. The size of $\\Omega$ is $n^2 - n = n(n-1)$ since there are $n^2$ pairs but we exclude outcomes where $i = j$.\n\n"
        "3. Define the event of interest $A$ as:\n"
        "$$ A = \\{(i, j) \\in \\Omega : |i - j| \\leq 2\\}. $$\n\n"
        "4. If $n \\geq 3$, the event $A$ contains four lines (e.g., $i = j+1$, $i = j-1$, $i = j+2$, $i = j-2$). Each line contains $2(n-2) + 2 = 4n - 6$ outcomes.\n\n"
        "5. The probability of the event $A$ is:\n"
        "$$ P(A) = \\frac{|A|}{|\\Omega|} = \\frac{4n - 6}{n(n-1)}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

question_7_diastolic_blood_pressure = {
    'question': (
        "Suppose that diastolic blood pressures (DBPs) for men aged 35–44 are normally distributed with a mean of 80 mm Hg "
        "and a standard deviation of 10 mm Hg. What is the probability that a random 35–44-year-old has a DBP greater than 100 mm Hg?"
    ),
    'options_list': [
        "A. About 5%",
        "B. About 2.5%",
        "C. About 16%",
        "D. About 1%",
        "E. About 50%"
    ],
    'correct_answer': "B. About 2.5%",
    'explanation': (
        "First, calculate how many standard deviations 100 mm Hg is above the mean:\n"
        "$$Z = \\frac{100 - 80}{10} = 2.$$"
        "Using the standard normal distribution, the probability of being more than 2 standard deviations above the mean is 2.5%.\n"
        "This can be computed using statistical software such as R with:\n"
        "`pnorm(100, mean = 80, sd = 10, lower.tail = FALSE)` or equivalently `pnorm(2, lower.tail = FALSE)`."
    ),
    'chapter_information': "Mathematical Biostatistics Boot Camp 1, Johns Hopkins University"
}

question_8_brain_volume_percentile = {
    'question': (
        "Brain volume for adult women is approximately normally distributed with a mean of 1,100 cc and a standard deviation of 75 cc. "
        "What brain volume represents the 10th percentile of this distribution?"
    ),
    'options_list': [
        "A. 1020 cc",
        "B. 950 cc",
        "C. 980 cc",
        "D. 1000 cc"
    ],
    'correct_answer': "D. 1000 cc",
    'explanation': (
        "The 10th percentile corresponds to a Z-score of -1.28 from the standard normal distribution. Using the formula for a value in a normal distribution:\n"
        "$$X = \\text{mean} + Z \\cdot \\text{SD}$$\n"
        "Substitute the values:\n"
        "$$X = 1100 + (-1.28) \\cdot 75 = 1100 - 96 = 1000 \\text{ cc}.$$"
        "This can also be calculated using a statistical function like `qnorm(0.1, mean = 1100, sd = 75)`."
    ),
    'chapter_information': "Mathematical Biostatistics Boot Camp 1, Johns Hopkins University"
}

question_9_sample_mean_percentile = {
    'question': (
        "Brain volume for adult women is approximately normally distributed with a mean of 1,100 cc and a standard deviation of 75 cc. "
        "Consider the sample mean of 144 random adult women from this population. What is the 10th percentile "
        "of the distribution of sample means for this sample size?"
    ),
    'options_list': [
        "A. 1085 cc",
        "B. 1090 cc",
        "C. 1088 cc",
        "D. 1092 cc"
    ],
    'correct_answer': "D. 1092 cc",
    'explanation': (
        "The standard deviation of the sample mean (standard error) is calculated as:\n"
        "$$\\text{SE} = \\frac{\\text{SD}}{\\sqrt{n}} = \\frac{75}{\\sqrt{144}} = 6.25.$$"
        "The 10th percentile corresponds to a Z-score of -1.28. Use the formula for the sample mean distribution:\n"
        "$$X = \\text{mean} + Z \\cdot \\text{SE}.$$"
        "Substitute the values:\n"
        "$$X = 1100 + (-1.28) \\cdot 6.25 = 1100 - 8 = 1092 \\text{ cc}.$$"
        "This can also be computed using a statistical function like `qnorm(0.1, mean = 1100, sd = 6.25)`."
    ),
    'chapter_information': "Mathematical Biostatistics Boot Camp 1, Johns Hopkins University"
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_3_MPC = KC_MPC_QUESTIONS[:-1]