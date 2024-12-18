# Confidence Intervals
isye6739_module6_question_1 = {
    'question': (
        "The life in hours of a 75-W light bulb is known to be approximately normally distributed, "
        "with a standard deviation of $\\sigma = 25$ hours. A random sample of 20 bulbs has a mean life of $\\bar{x} = 1014$ hours. "
        "Construct a 95% two-sided confidence interval on the mean life."
    ),
    'options_list': [
        'A) $1000.2 \\leq \\mu \\leq 1027.8$',
        'B) $1003.04 \\leq \\mu \\leq 1024.96$',
        'C) $995.12 \\leq \\mu \\leq 1032.88$',
        'D) $1005.76 \\leq \\mu \\leq 1022.24$'
    ],
    'correct_answer': 'B) $1003.04 \\leq \\mu \\leq 1024.96$',
    'explanation': (
        "To construct the 95% confidence interval, we use:\n"
        "$\\bar{x} - z_{\\alpha/2} \\frac{\\sigma}{\\sqrt{n}} \\leq \\mu \\leq \\bar{x} + z_{\\alpha/2} \\frac{\\sigma}{\\sqrt{n}}$\n"
        "Given $z_{0.025} = 1.96$, $\\sigma = 25$, $n = 20$, and $\\bar{x} = 1014$, we compute:\n"
        "$1014 - 1.96 \\cdot \\frac{25}{\\sqrt{20}} \\leq \\mu \\leq 1014 + 1.96 \\cdot \\frac{25}{\\sqrt{20}}$\n"
        "$1003.04 \\leq \\mu \\leq 1024.96$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_2 = {
    'question': (
        "In Exercise 10-40, suppose we want to be 95% confident that the error in estimating the mean life is less than 5 hours. "
        "What sample size should be used?"
    ),
    'options_list': [
        'A) 97',
        'B) 87',
        'C) 107',
        'D) 77'
    ],
    'correct_answer': 'A) 97',
    'explanation': (
        "To determine the sample size, we use:\n"
        "$n = \\left( \\frac{z_{\\alpha/2} \\sigma}{e} \\right)^2$\n"
        "Given $z_{0.025} = 1.96$, $\\sigma = 25$, and $e = 5$, we compute:\n"
        "$n = \\left( \\frac{1.96 \\cdot 25}{5} \\right)^2 = 96.04 \\approx 97$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_3 = {
    'question': (
        "The burning rates of two different solid-fuel rocket propellants are being studied. Both propellants have a standard deviation of $\\sigma = 3$ cm/s. "
        "Two random samples of $n_1 = 20$ and $n_2 = 20$ specimens are tested. The sample mean burning rates are $\\bar{x}_1 = 18$ and $\\bar{x}_2 = 24$ cm/s. "
        "Construct a 99% confidence interval on the mean difference in burning rate."
    ),
    'options_list': [
        'A) $4.12 \\leq \\mu_2 - \\mu_1 \\leq 7.88$',
        'B) $3.56 \\leq \\mu_2 - \\mu_1 \\leq 8.44$',
        'C) $2.96 \\leq \\mu_2 - \\mu_1 \\leq 9.04$',
        'D) $3.24 \\leq \\mu_2 - \\mu_1 \\leq 8.76$'
    ],
    'correct_answer': 'B) $3.56 \\leq \\mu_2 - \\mu_1 \\leq 8.44$',
    'explanation': (
        "The confidence interval is given by:\n"
        "$\\bar{x}_2 - \\bar{x}_1 - z_{\\alpha/2} \\sqrt{\\frac{\\sigma_1^2}{n_1} + \\frac{\\sigma_2^2}{n_2}} \\leq \\mu_2 - \\mu_1 "
        "\\leq \\bar{x}_2 - \\bar{x}_1 + z_{\\alpha/2} \\sqrt{\\frac{\\sigma_1^2}{n_1} + \\frac{\\sigma_2^2}{n_2}}$\n"
        "Given $z_{0.005} = 2.576$, $\\sigma = 3$, $n_1 = n_2 = 20$, $\\bar{x}_1 = 18$, and $\\bar{x}_2 = 24$, we compute:\n"
        "$3.56 \\leq \\mu_2 - \\mu_1 \\leq 8.44$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_4 = {
    'question': (
        "The compressive strength of concrete is being tested by a civil engineer. He tests 16 specimens with the following data:\n"
        "2216, 2237, 2249, 2204, 2225, 2301, 2281, 2263,\n"
        "2318, 2255, 2275, 2295, 2250, 2238, 2300, 2217.\n"
        "Construct a 95% two-sided confidence interval on the mean compressive strength."
    ),
    'options_list': [
        'A) $2240.2 \\leq \\mu \\leq 2270.5$',
        'B) $2239.4 \\leq \\mu \\leq 2276.1$',
        'C) $2242.8 \\leq \\mu \\leq 2272.8$',
        'D) $2245.3 \\leq \\mu \\leq 2273.7$'
    ],
    'correct_answer': 'B) $2239.4 \\leq \\mu \\leq 2276.1$',
    'explanation': (
        "Since $\\sigma$ is unknown, we use the t-distribution for the confidence interval:\n"
        "$\\bar{x} - t_{\\alpha/2, n-1} \\frac{s}{\\sqrt{n}} \\leq \\mu \\leq \\bar{x} + t_{\\alpha/2, n-1} \\frac{s}{\\sqrt{n}}$\n"
        "Given $n = 16$, $\\bar{x} = 2257.75$, $s = 34.51$, and $t_{0.025,15} = 2.13$, we compute:\n"
        "$2239.4 \\leq \\mu \\leq 2276.1$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_5 = {
    'question': (
        "An article on bond strengths for energetic materials presents data for 15 bond strength specimens:\n"
        "323, 312, 300, 284, 283, 261, 207, 183, 180, 179, 174, 167, 167, 157, 120.\n"
        "Construct a two-sided 95% confidence interval on the mean bond strength."
    ),
    'options_list': [
        'A) $185.2 \\leq \\mu \\leq 254.3$',
        'B) $183.1 \\leq \\mu \\leq 256.5$',
        'C) $182.4 \\leq \\mu \\leq 255.8$',
        'D) $184.6 \\leq \\mu \\leq 258.1$'
    ],
    'correct_answer': 'B) $183.1 \\leq \\mu \\leq 256.5$',
    'explanation': (
        "Since $\\sigma$ is unknown, we use the t-distribution for the confidence interval:\n"
        "$\\bar{x} - t_{\\alpha/2, n-1} \\frac{s}{\\sqrt{n}} \\leq \\mu \\leq \\bar{x} + t_{\\alpha/2, n-1} \\frac{s}{\\sqrt{n}}$\n"
        "Given $n = 15$, $\\bar{x} = 219.80$, $s = 66.41$, and $t_{0.025,14} = 2.14$, we compute:\n"
        "$219.80 - 2.14 \\cdot \\frac{66.41}{\\sqrt{15}} \\leq \\mu \\leq 219.80 + 2.14 \\cdot \\frac{66.41}{\\sqrt{15}}$\n"
        "This simplifies to $183.1 \\leq \\mu \\leq 256.5$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_6 = {
    'question': (
        "The wall thickness of 25 glass 2-liter bottles was measured by a quality-control engineer. "
        "The sample mean was $\\bar{x} = 4.05$ mm, and the sample standard deviation was $s = 0.08$ mm. "
        "Find a 90% lower confidence interval on the mean wall thickness."
    ),
    'options_list': [
        'A) $4.012 \\leq \\mu$',
        'B) $4.021 \\leq \\mu$',
        'C) $4.029 \\leq \\mu$',
        'D) $4.035 \\leq \\mu$'
    ],
    'correct_answer': 'C) $4.029 \\leq \\mu$',
    'explanation': (
        "The lower confidence interval for the mean is given by:\n"
        "$\\bar{x} - t_{\\alpha, n-1} \\frac{s}{\\sqrt{n}} \\leq \\mu$\n"
        "Given $n = 25$, $\\bar{x} = 4.05$, $s = 0.08$, and $t_{0.10,24} = 1.32$, we compute:\n"
        "$4.05 - 1.32 \\cdot \\frac{0.08}{\\sqrt{25}} = 4.029$\n"
        "Thus, $4.029 \\leq \\mu$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_7 = {
    'question': (
        "Two independent random samples of size $n_1 = 20$ and $n_2 = 20$ are drawn from two normal populations. "
        "The sample means and standard deviations are $\\bar{x}_1 = 22.0$, $s_1 = 1.8$, $\\bar{x}_2 = 21.5$, and $s_2 = 1.5$. "
        "Assuming that $\\sigma_1^2 = \\sigma_2^2$, construct a 95% two-sided confidence interval on $\\mu_1 - \\mu_2$."
    ),
    'options_list': [
        'A) $-0.561 \\leq \\mu_1 - \\mu_2 \\leq 1.561$',
        'B) $-0.705 \\leq \\mu_1 - \\mu_2 \\leq 1.705$',
        'C) $-0.612 \\leq \\mu_1 - \\mu_2 \\leq 1.612$',
        'D) $-0.589 \\leq \\mu_1 - \\mu_2 \\leq 1.589$'
    ],
    'correct_answer': 'A) $-0.561 \\leq \\mu_1 - \\mu_2 \\leq 1.561$',
    'explanation': (
        "The confidence interval for the difference in means with equal variances is:\n"
        "$\\bar{x}_1 - \\bar{x}_2 - t_{\\alpha/2, n_1+n_2-2} s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}} \\leq \\mu_1 - \\mu_2 "
        "\\leq \\bar{x}_1 - \\bar{x}_2 + t_{\\alpha/2, n_1+n_2-2} s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}$\n"
        "With $s_p^2 = \\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$, we find $s_p = 2.745$ and $t_{0.025,38} = 2.024$.\n"
        "Thus, the interval is $-0.561 \\leq \\mu_1 - \\mu_2 \\leq 1.561$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_8 = {
    'question': (
        "The diameter of steel rods from two extrusion machines is being investigated. "
        "Two random samples of sizes $n_1 = 15$ and $n_2 = 18$ are selected, with sample means $\\bar{x}_1 = 8.73$, $\\bar{x}_2 = 8.68$, "
        "and sample variances $s_1^2 = 0.30$, $s_2^2 = 0.34$. Assuming $\\sigma_1^2 = \\sigma_2^2$, construct a 95% confidence interval "
        "on the difference in mean rod diameter."
    ),
    'options_list': [
        'A) $-0.312 \\leq \\mu_1 - \\mu_2 \\leq 0.312$',
        'B) $-0.355 \\leq \\mu_1 - \\mu_2 \\leq 0.455$',
        'C) $-0.289 \\leq \\mu_1 - \\mu_2 \\leq 0.389$',
        'D) $-0.276 \\leq \\mu_1 - \\mu_2 \\leq 0.376$'
    ],
    'correct_answer': 'B) $-0.355 \\leq \\mu_1 - \\mu_2 \\leq 0.455$',
    'explanation': (
        "Using the pooled variance assumption and t-distribution for the confidence interval:\n"
        "$s_p^2 = \\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$ gives $s_p^2 = 0.32$.\n"
        "The confidence interval is then:\n"
        "$\\bar{x}_1 - \\bar{x}_2 - t_{\\alpha/2, n_1+n_2-2} s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}} \\leq \\mu_1 - \\mu_2 "
        "\\leq \\bar{x}_1 - \\bar{x}_2 + t_{\\alpha/2, n_1+n_2-2} s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}$\n"
        "Substituting values gives $-0.355 \\leq \\mu_1 - \\mu_2 \\leq 0.455$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}


isye6739_module6_question_6 = {
    'question': (
        "The wall thickness of 25 glass 2-liter bottles was measured by a quality-control engineer. "
        "The sample mean was $\\bar{x} = 4.05$ mm, and the sample standard deviation was $s = 0.08$ mm. "
        "Find a 90% lower confidence interval on the mean wall thickness."
    ),
    'options_list': [
        'A) $4.029 \\leq \\mu$',
        'B) $4.035 \\leq \\mu$',
        'C) $4.031 \\leq \\mu$',
        'D) $4.021 \\leq \\mu$'
    ],
    'correct_answer': 'A) $4.029 \\leq \\mu$',
    'explanation': (
        "For a 90% lower confidence interval, we use:\n"
        "$\\bar{x} - t_{\\alpha, n-1} \\frac{s}{\\sqrt{n}} \\leq \\mu$\n"
        "Given $t_{0.10, 24} = 1.32$, $\\bar{x} = 4.05$, $s = 0.08$, and $n = 25$, we compute:\n"
        "$4.05 - 1.32 \\cdot \\frac{0.08}{\\sqrt{25}} = 4.029 \\leq \\mu$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_7 = {
    'question': (
        "Random samples of size 20 were drawn from two independent normal populations. The sample means and standard deviations were:\n"
        "$\\bar{x}_1 = 22.0$, $s_1 = 1.8$, $\\bar{x}_2 = 21.5$, and $s_2 = 1.5$. "
        "Assuming that $\\sigma_1^2 = \\sigma_2^2$, find a 95% two-sided confidence interval on $\\mu_1 - \\mu_2$."
    ),
    'options_list': [
        'A) $-0.561 \\leq \\mu_1 - \\mu_2 \\leq 1.561$',
        'B) $-0.455 \\leq \\mu_1 - \\mu_2 \\leq 1.455$',
        'C) $-0.501 \\leq \\mu_1 - \\mu_2 \\leq 1.501$',
        'D) $-0.411 \\leq \\mu_1 - \\mu_2 \\leq 1.411$'
    ],
    'correct_answer': 'A) $-0.561 \\leq \\mu_1 - \\mu_2 \\leq 1.561$',
    'explanation': (
        "Since variances are assumed equal, we use the pooled variance:\n"
        "$s_p^2 = \\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$.\n"
        "Here, $n_1 = n_2 = 20$, $s_1 = 1.8$, and $s_2 = 1.5$. Pooled variance is $s_p^2 = 2.745$.\n"
        "The confidence interval is:\n"
        "$\\bar{x}_1 - \\bar{x}_2 - t_{\\alpha/2, n_1+n_2-2} s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}} \\leq \\mu_1 - \\mu_2 \\leq \\bar{x}_1 - \\bar{x}_2 + t_{\\alpha/2, n_1+n_2-2} s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}$\n"
        "Using $t_{0.025,38} = 2.024$, we compute:\n"
        "$-0.561 \\leq \\mu_1 - \\mu_2 \\leq 1.561$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_8 = {
    'question': (
        "The diameter of steel rods manufactured on two different extrusion machines is being investigated. "
        "Two random samples of sizes $n_1 = 15$ and $n_2 = 18$ are selected. The sample means and variances are:\n"
        "$\\bar{x}_1 = 8.73$, $s_1^2 = 0.30$, $\\bar{x}_2 = 8.68$, $s_2^2 = 0.34$. "
        "Assuming $\\sigma_1^2 = \\sigma_2^2$, construct a 95% two-sided confidence interval on the difference in mean rod diameter."
    ),
    'options_list': [
        'A) $-0.355 \\leq \\mu_1 - \\mu_2 \\leq 0.455$',
        'B) $-0.345 \\leq \\mu_1 - \\mu_2 \\leq 0.445$',
        'C) $-0.365 \\leq \\mu_1 - \\mu_2 \\leq 0.465$',
        'D) $-0.375 \\leq \\mu_1 - \\mu_2 \\leq 0.475$'
    ],
    'correct_answer': 'A) $-0.355 \\leq \\mu_1 - \\mu_2 \\leq 0.455$',
    'explanation': (
        "We use the pooled variance approach, similar to Question 7. Given $s_1^2 = 0.30$, $s_2^2 = 0.34$, and $n_1 = 15$, $n_2 = 18$:\n"
        "Pooled variance is computed, and the confidence interval is calculated using the formula for two samples with equal variances.\n"
        "The result is $-0.355 \\leq \\mu_1 - \\mu_2 \\leq 0.455$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}

isye6739_module6_question_9 = {
    'question': (
        "Construct a 95% two-sided confidence interval on the ratio of the population variances $\\sigma_1^2 / \\sigma_2^2$ for the data in Exercise 10-56.\n"
        "The sample variances are $s_1^2 = 1.8^2$ and $s_2^2 = 1.5^2$, with sample sizes $n_1 = n_2 = 20$."
    ),
    'options_list': [
        'A) $0.48 \\leq \\frac{\\sigma_1^2}{\\sigma_2^2} \\leq 3.71$',
        'B) $0.57 \\leq \\frac{\\sigma_1^2}{\\sigma_2^2} \\leq 3.64$',
        'C) $0.52 \\leq \\frac{\\sigma_1^2}{\\sigma_2^2} \\leq 3.85$',
        'D) $0.61 \\leq \\frac{\\sigma_1^2}{\\sigma_2^2} \\leq 3.45$'
    ],
    'correct_answer': 'B) $0.57 \\leq \\frac{\\sigma_1^2}{\\sigma_2^2} \\leq 3.64$',
    'explanation': (
        "The confidence interval for the ratio of variances is given by:\n"
        "$\\frac{s_1^2}{s_2^2} \\cdot \\frac{1}{F_{\\alpha/2, n_1-1, n_2-1}} \\leq \\frac{\\sigma_1^2}{\\sigma_2^2} \\leq \\frac{s_1^2}{s_2^2} \\cdot F_{\\alpha/2, n_2-1, n_1-1}$.\n"
        "Using $F_{0.025, 19, 19} = 2.526$ and $s_1^2 = 1.8^2$, $s_2^2 = 1.5^2$, we compute:\n"
        "$0.57 \\leq \\frac{\\sigma_1^2}{\\sigma_2^2} \\leq 3.64$."
    ),
    'chapter_information': 'ISYE 6739 - Module 6'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_6_MPC = KC_MPC_QUESTIONS[:-1]