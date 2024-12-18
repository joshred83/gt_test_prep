isye6739_module5_q1 = {
    'question': (
        "A sample of shelf life data (in days) for a high-speed photographic film is given as:\n"
        "126, 129, 134, 141\n"
        "131, 132, 136, 145\n"
        "116, 128, 130, 162\n"
        "125, 126, 134, 129\n"
        "134, 127, 120, 127\n"
        "120, 122, 129, 133\n"
        "125, 111, 147, 129\n"
        "150, 148, 126, 140\n"
        "130, 120, 117, 131\n"
        "149, 117, 143, 133\n\n"
        "Construct a histogram and comment on the properties of the data."
    ),
    'options_list': ['Calculate'],
    'correct_answer': "$\\bar{x} = 131.30$, $s^2 = 113.85$, $s = 10.67$",
    'explanation': (
        "The sample mean is calculated as $\\bar{x} = 131.30$, the variance as $s^2 = 113.85$, "
        "and the standard deviation as $s = 10.67$. These values describe the central tendency and spread."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q2 = {
    'question': (
        "Consider the quantity $\\sum_{i=1}^n (x_i - a)^2$. For what value of $a$ is this minimized?\n\n"
        "Now consider the quantity $\\sum_{i=1}^n |x_i - a|$. What value of $a$ minimizes this?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) The value of $a$ that minimizes $\\sum_{i=1}^n (x_i - a)^2$ is the mean $\\bar{x}$.\n"
        "(b) The value of $a$ that minimizes $\\sum_{i=1}^n |x_i - a|$ is the median."
    ),
    'explanation': (
        "Differentiating the first equation shows that the mean minimizes the squared error. For the second, "
        "the median minimizes the absolute deviations."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q3 = {
    'question': (
        "Suppose we have a random sample of size $2n$ from a population $X$, where $E[X] = \\mu$ "
        "and $\\text{Var}(X) = \\sigma^2$. Two estimators of $\\mu$ are:\n"
        "\\[ \\bar{X}_1 = \\frac{1}{2n} \\sum_{i=1}^{2n} X_i \\quad \\text{and} \\quad \\bar{X}_2 = \\frac{1}{n} \\sum_{i=1}^n X_i. \\]\n"
        "Which is the better estimator of $\\mu$? Explain your choice."
    ),
    'options_list': ['Choose the estimator'],
    'correct_answer': "$\\bar{X}_1$ is better because $\\text{Var}(\\bar{X}_1) = \\sigma^2 / (2n) < \\sigma^2 / n = \\text{Var}(\\bar{X}_2)$.",
    'explanation': (
        "Both estimators are unbiased, but $\\bar{X}_1$ has a smaller variance and is thus a more efficient estimator."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q4 = {
    'question': (
        "Suppose $\\hat{\\theta}_1$, $\\hat{\\theta}_2$, and $\\hat{\\theta}_3$ are estimators of $\\theta$ with:\n"
        "$E[\\hat{\\theta}_1] = E[\\hat{\\theta}_2] = \\theta$, $E[\\hat{\\theta}_3] \\neq \\theta$,\n"
        "$\\text{Var}(\\hat{\\theta}_1) = 12$, $\\text{Var}(\\hat{\\theta}_2) = 10$, and $E[(\\hat{\\theta}_3 - \\theta)^2] = 6$.\n"
        "Which estimator is preferred and why?"
    ),
    'options_list': ['Choose the estimator'],
    'correct_answer': "$\\hat{\\theta}_3$ is preferred because it has the smallest mean squared error (MSE).",
    'explanation': (
        "The MSE combines variance and bias. While $\\hat{\\theta}_3$ is biased, it has the smallest overall MSE: 6."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q5 = {
    'question': (
        "Let $X_1, \\dots, X_n$ be an i.i.d. sample of geometric random variables with parameter $p$.\n"
        "(a) Find the maximum likelihood estimator (MLE) of $p$.\n"
        "(b) Suppose the observations are $3, 5, 1, 2, 7$. What is the resulting MLE?\n"
        "(c) What is the MLE of $p^2$?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) The MLE of $p$ is $\\hat{p} = 1 / \\bar{x}$.\n"
        "(b) For $\\bar{x} = 3.6$, the MLE is $\\hat{p} = 0.278$.\n"
        "(c) The MLE of $p^2$ is $\\hat{p}^2 = 1 / \\bar{x}^2 = 0.0773$."
    ),
    'explanation': (
        "The likelihood function for a geometric distribution is maximized when $\\hat{p} = 1 / \\bar{x}$. "
        "By the invariance property of MLEs, the MLE of $p^2$ is $1 / \\bar{x}^2$."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}


isye6739_module5_q6 = {
    'question': (
        "Let $X_1, \\dots, X_n$ be an i.i.d. sample of Bernoulli random variables with parameter $p$.\n"
        "(a) Find the maximum likelihood estimator (MLE) of $p$ based on a sample of size $n$.\n"
        "(b) Find a method of moments (MOM) estimator for $p$. Are there multiple MOM estimators?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) The MLE of $p$ is $\\hat{p} = \\bar{x}$.\n"
        "(b) The MOM estimator of $p$ is also $\\bar{x}$. However, for any integer $k$, an MOM estimator can be of the form "
        "$\\frac{1}{n} \\sum_{i=1}^n X_i^k$."
    ),
    'explanation': (
        "For Bernoulli random variables, the likelihood function is maximized when $\\hat{p} = \\bar{x}$. "
        "The method of moments also yields $\\bar{x}$, but other estimators are possible when higher moments are used."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q7 = {
    'question': (
        "A population of power supplies for a personal computer has an output voltage that is normally distributed "
        "with a mean of 5.00 V and a standard deviation of 0.10 V. A random sample of eight power supplies is selected.\n"
        "Specify the sampling distribution of $\\bar{X}$."
    ),
    'options_list': ['Choose the distribution'],
    'correct_answer': "$\\bar{X} \\sim N(5, 0.00125)$",
    'explanation': (
        "For a sample mean $\\bar{X}$ of size $n$, the variance of the sampling distribution is given by "
        "$\\sigma^2 / n$. Here, $\\sigma = 0.10$ and $n = 8$, so the sampling distribution is $N(5, 0.00125)$."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q8 = {
    'question': (
        "Find the $\\chi^2$ quantile for $\\chi^2_{0.95,8}$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': "2.73",
    'explanation': (
        "The $\\chi^2$ quantile for $0.95$ with 8 degrees of freedom is obtained from a statistical table or software."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q9 = {
    'question': (
        "Find the $t$ quantile $t_{0.25,10}$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': "0.700",
    'explanation': (
        "The $t$ quantile for $0.25$ with 10 degrees of freedom is $0.700$, obtained using a $t$-table or software."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}

isye6739_module5_q10 = {
    'question': (
        "Find the $F$ quantile $F_{0.25,4,9}$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': "1.63",
    'explanation': (
        "The $F$ quantile for $0.25$ with numerator degrees of freedom 4 and denominator degrees of freedom 9 is $1.63$, "
        "as obtained from an $F$-table or software."
    ),
    'chapter_information': 'ISYE 6739 - Module 5'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_5_MPC = KC_MPC_QUESTIONS[:-1]