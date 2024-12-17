isye6739_module7_question_1 = {
    'question': (
        "The breaking strength of a fiber used in manufacturing cloth is required to be at least 160 psi. "
        "The standard deviation of breaking strength is known to be 3 psi. A random sample of 4 specimens "
        "is tested with an average breaking strength of 158 psi.\n\n"
        "(a) Should the fiber be judged acceptable with a level of significance $\\alpha = 0.05$?\n"
        "(b) What is the probability of accepting $H_0: \\mu \\leq 160$ if the true breaking strength is 165 psi?"
    ),
    'options_list': [
        'A) (a) Not acceptable; (b) 0.0466',
        'B) (a) Acceptable; (b) 0.0534',
        'C) (a) Not acceptable; (b) 0.0466 (Z = -1.688)',
        'D) (a) Acceptable; (b) 0.0684'
    ],
    'correct_answer': 'A) (a) Not acceptable; (b) 0.0466',
    'explanation': (
        "For part (a), calculate the test statistic:\n"
        "$Z_0 = \\frac{\\bar{x} - \\mu_0}{\\sigma/\\sqrt{n}} = \\frac{158 - 160}{3/2} = -1.333$\n"
        "Since $Z_0 = -1.333 < Z_{0.05} = 1.645$, we do not reject $H_0$.\n\n"
        "For part (b), compute the probability for $Z \\leq 1.645$ given $\\mu = 165$:\n"
        "$\\text{Pr}(Z \\leq 1.645 | \\mu = 165) = \\Phi(1.688) \\approx 0.0466$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_module7_question_2 = {
    'question': (
        "The yield of a chemical process has variance $\\sigma^2 = 5$ (percentage$^2$). "
        "The yields from the past five days are: 91.60, 88.75, 90.80, 89.95, 91.30.\n\n"
        "(a) Is there reason to believe the yield is less than 90% using $\\alpha = 0.05$?\n"
        "(b) What sample size is required to detect a true mean yield of 85% with probability 0.95?"
    ),
    'options_list': [
        'A) (a) No evidence; (b) 4',
        'B) (a) No evidence; (b) 3',
        'C) (a) Yes, evidence exists; (b) 4',
        'D) (a) Yes, evidence exists; (b) 5'
    ],
    'correct_answer': 'B) (a) No evidence; (b) 3',
    'explanation': (
        "For part (a), calculate the test statistic:\n"
        "$Z_0 = \\frac{\\bar{x} - \\mu_0}{\\sigma/\\sqrt{n}} = \\frac{90.48 - 90}{\\sqrt{5/5}} = 0.48$\n"
        "Since $Z_0 > -1.645$, we do not reject $H_0$.\n\n"
        "For part (b), sample size $n$ is calculated as:\n"
        "$n = \\left( (z_\\alpha + z_\\beta) \\frac{\\sigma}{\\delta} \\right)^2 = \\left( (1.645 + 1.645) \\frac{\\sqrt{5}}{5} \\right)^2 \\approx 3$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_module7_question_3 = {
    'question': (
        "Two machines are used for filling bottles with net volume 16.0 ounces. "
        "The standard deviations are $\\sigma_1 = 0.015$ and $\\sigma_2 = 0.018$. "
        "The output samples are:\n"
        "Machine 1: 16.03, 16.04, 16.05, 16.02, 15.96, 15.98, 16.02, 15.99\n"
        "Machine 2: 16.02, 15.97, 15.96, 16.01, 15.99, 16.03, 16.04, 16.00.\n\n"
        "Do you think the two machines produce the same mean volume at $\\alpha = 0.05$?"
    ),
    'options_list': [
        'A) Do not reject $H_0$; $Z = 1.349$',
        'B) Reject $H_0$; $Z = 1.645$',
        'C) Do not reject $H_0$; $Z = 1.445$',
        'D) Reject $H_0$; $Z = 1.849$'
    ],
    'correct_answer': 'A) Do not reject $H_0$; $Z = 1.349$',
    'explanation': (
        "Calculate the test statistic:\n"
        "$Z_0 = \\frac{\\bar{x}_1 - \\bar{x}_2}{\\sqrt{\\frac{\\sigma_1^2}{n_1} + \\frac{\\sigma_2^2}{n_2}}}$\n"
        "Using $\\bar{x}_1 = 16.011$, $\\bar{x}_2 = 15.989$, $\\sigma_1 = 0.015$, $\\sigma_2 = 0.018$, and $n_1 = n_2 = 8$:\n"
        "$Z_0 = 1.349$\n"
        "Since $|Z_0| < 1.96$, we do not reject $H_0$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_module7_question_4 = {
    'question': (
        "The lateral deviation in yards of a mortar shell is observed as follows:\n"
        "11.28, -10.42, -8.51, 1.95, 6.47, -9.48, 6.25, 10.11, -8.65, -0.68.\n\n"
        "Test the hypothesis that the mean lateral deviation is zero. Assume a level of significance of $\\alpha = 0.05$."
    ),
    'options_list': [
        'A) Do not reject $H_0$; $t_0 = -0.062$',
        'B) Reject $H_0$; $t_0 = 2.262$',
        'C) Do not reject $H_0$; $t_0 = -1.062$',
        'D) Reject $H_0$; $t_0 = 1.262$'
    ],
    'correct_answer': 'A) Do not reject $H_0$; $t_0 = -0.062$',
    'explanation': (
        "Calculate the test statistic using the t-distribution:\n"
        "$t_0 = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}}$\n"
        "With $\\bar{x} = -0.168$, $s = 8.5638$, and $n = 10$:\n"
        "$t_0 = -0.062$\n"
        "Since $|t_0| < t_{0.025, 9} = 2.2622$, we do not reject $H_0$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_module7_question_5 = {
    'question': (
        "An article in the *Journal of Construction Engineering and Management* presents data on the number of work hours lost "
        "per day due to weather-related incidents over 11 workdays:\n"
        "8.8, 12.5, 5.4, 12.8, 9.1, 14.7, 8.8, 12.2, 13.3, 6.9, 2.2.\n\n"
        "Assuming work hours are normally distributed, is there evidence to conclude that the mean number of work hours lost "
        "per day is greater than 8 hours? Use $\\alpha = 0.05$."
    ),
    'options_list': [
        'A) Reject $H_0$ at $\\alpha = 0.05$; $t_0 = 1.47$',
        'B) Do not reject $H_0$ at $\\alpha = 0.05$; $t_0 = 1.47$',
        'C) Reject $H_0$ at $\\alpha = 0.10$ but not $\\alpha = 0.05$; $t_0 = 1.47$',
        'D) Do not reject $H_0$ at $\\alpha = 0.10$; $t_0 = 1.47$'
    ],
    'correct_answer': 'C) Reject $H_0$ at $\\alpha = 0.10$ but not $\\alpha = 0.05$; $t_0 = 1.47$',
    'explanation': (
        "We test $H_0: \\mu \\leq 8$ vs. $H_1: \\mu > 8$. The test statistic is:\n"
        "$t_0 = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}} = \\frac{9.7 - 8}{\\sqrt{14.62 / 11}} = 1.47.$\n"
        "Using critical values:\n"
        "- For $\\alpha = 0.05$, $t_{0.05,10} = 1.812$.\n"
        "- For $\\alpha = 0.10$, $t_{0.10,10} = 1.372$.\n"
        "Since $1.47 < 1.812$ but $1.47 > 1.372$, we reject $H_0$ at $\\alpha = 0.10$ but not at $\\alpha = 0.05$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_module7_question_6 = {
    'question': (
        "The yield of a chemical process is being studied. The variance of the yield is known to be $\\sigma^2 = 5$. "
        "What sample size is required to detect a true mean yield of 85% with probability 0.95 and a significance level of $\\alpha = 0.05$?"
    ),
    'options_list': [
        'A) 2',
        'B) 3',
        'C) 4',
        'D) 5'
    ],
    'correct_answer': 'B) 3',
    'explanation': (
        "We use the formula for required sample size:\n"
        "$n = \\left( (z_\\alpha + z_\\beta) \\frac{\\sigma}{\\delta} \\right)^2$\n"
        "Where:\n"
        "- $z_{\\alpha} = 1.645$ (significance level 0.05)\n"
        "- $z_{\\beta} = 1.645$ (probability of detection 0.95)\n"
        "- $\\sigma = \\sqrt{5}$ and $\\delta = 5$.\n\n"
        "Substitute values:\n"
        "$n = \\left( (1.645 + 1.645) \\frac{\\sqrt{5}}{5} \\right)^2 \\approx 3$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_module7_question_7 = {
    'question': (
        "The lateral deviation in yards of a mortar shell is measured as follows:\n"
        "11.28, -10.42, -8.51, 1.95, 6.47, -9.48, 6.25, 10.11, -8.65, -0.68.\n\n"
        "Test the hypothesis that the mean lateral deviation is zero. Assume $\\alpha = 0.05$."
    ),
    'options_list': [
        'A) $t_0 = -0.062$, Do not reject $H_0$',
        'B) $t_0 = 0.168$, Reject $H_0$',
        'C) $t_0 = -1.062$, Do not reject $H_0$',
        'D) $t_0 = 0.462$, Reject $H_0$'
    ],
    'correct_answer': 'A) $t_0 = -0.062$, Do not reject $H_0$',
    'explanation': (
        "The test statistic is calculated using the t-distribution:\n"
        "$t_0 = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}} = \\frac{-0.168 - 0}{8.5638 / \\sqrt{10}} = -0.062.$\n"
        "The critical value for $t_{0.025,9}$ is 2.2622.\n"
        "Since $|t_0| = 0.062 < 2.2622$, we do not reject $H_0$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_module7_questio3n_6 = {
    'question': (
        "Two random samples were drawn from normal populations with equal variances. "
        "The sample data yields $\\bar{x} = 20.0$, $n = 10$, $\\sum_{i=1}^n (x_i - \\bar{x})^2 = 1480$, "
        "$\\bar{y} = 15.8$, $m = 10$, $\\sum_{i=1}^m (y_i - \\bar{y})^2 = 1425$. Test the hypothesis "
        "that the two means are equal. Use $\\alpha = 0.01$."
    ),
    'options_list': [
        'A) Reject $H_0$ at 0.01 significance level',
        'B) Fail to reject $H_0$ at 0.01 significance level',
        'C) Reject $H_0$ at 0.05 significance level',
        'D) Fail to reject $H_0$ at 0.05 significance level'
    ],
    'correct_answer': 'B) Fail to reject $H_0$ at 0.01 significance level',
    'explanation': (
        "We test $H_0: \\mu_x = \\mu_y$ vs. $H_1: \\mu_x \\ne \\mu_y$ using a pooled variance estimator. "
        "The pooled variance is:\n"
        "$s_p = \\sqrt{\\frac{(n-1)s_x^2 + (m-1)s_y^2}{n+m-2}} = \\sqrt{\\frac{1480 + 1425}{18}} = 12.704$.\n"
        "The test statistic is:\n"
        "$t_0 = \\frac{\\bar{x} - \\bar{y}}{s_p \\sqrt{\\frac{1}{n} + \\frac{1}{m}}} = "
        "\\frac{20.0 - 15.8}{12.704 \\sqrt{\\frac{1}{10} + \\frac{1}{10}}} = 0.74$.\n"
        "At $\\alpha = 0.01$, the critical value is $t_{0.005,18} = 2.878$. Since $|t_0| < t_{0.005,18}$, we fail to reject $H_0$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_mod2ule7_question_7 = {
    'question': (
        "Two machines produce metal parts. The following data have been collected:\n"
        "$n = 25, \\bar{x} = 0.984, s_x^2 = 13.46$, $m = 30, \\bar{y} = 0.907, s_y^2 = 9.65$.\n"
        "Test the hypothesis that the two machines produce parts having the same mean weight. Use $\\alpha = 0.05$."
    ),
    'options_list': [
        'A) Reject $H_0$ at $\\alpha = 0.05$',
        'B) Fail to reject $H_0$ at $\\alpha = 0.05$',
        'C) Reject $H_0$ at $\\alpha = 0.01$',
        'D) Fail to reject $H_0$ at $\\alpha = 0.01$'
    ],
    'correct_answer': 'B) Fail to reject $H_0$ at $\\alpha = 0.05$',
    'explanation': (
        "We test $H_0: \\mu_x = \\mu_y$ vs. $H_1: \\mu_x \\ne \\mu_y$, assuming unequal variances. "
        "The approximate degrees of freedom are:\n"
        "$\\nu \\equiv \\frac{\\left( \\frac{s_x^2}{n} + \\frac{s_y^2}{m} \\right)^2}{"
        "\\frac{(s_x^2/n)^2}{n-1} + \\frac{(s_y^2/m)^2}{m-1}} = 49.06 \\to 49$.\n"
        "The test statistic is:\n"
        "$t_0^* = \\frac{\\bar{x} - \\bar{y}}{\\sqrt{\\frac{s_x^2}{n} + \\frac{s_y^2}{m}}} = "
        "\\frac{0.077}{\\sqrt{\\frac{13.46}{25} + \\frac{9.65}{30}}} = 0.083$.\n"
        "At $\\alpha = 0.05$, $t_{0.025,49} = 2.01$. Since $|t_0^*| \\leq t_{0.025,49}$, we fail to reject $H_0$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6123739_module7_question_8 = {
    'question': (
        "Two types of exercise equipment, $A$ and $B$, are tested to determine their effect on heart rate. "
        "Seven subjects participated in a study, and the differences in heart rate ($D_i$) were recorded. "
        "Test the hypothesis $H_0: \\mu_D = 0$ vs. $H_1: \\mu_D \\ne 0$. Use $\\alpha = 0.05$."
    ),
    'options_list': [
        'A) Reject $H_0$ at $\\alpha = 0.05$',
        'B) Fail to reject $H_0$ at $\\alpha = 0.05$',
        'C) Reject $H_0$ at $\\alpha = 0.01$',
        'D) Fail to reject $H_0$ at $\\alpha = 0.01$'
    ],
    'correct_answer': 'A) Reject $H_0$ at $\\alpha = 0.05$',
    'explanation': (
        "We perform a paired $t$-test. The test statistic is:\n"
        "$t_0 = \\frac{\\bar{D}}{\\sqrt{s_D^2 / n}} = \\frac{-15.29}{\\sqrt{450.2 / 7}} = -1.907$.\n"
        "At $\\alpha = 0.05$, $t_{0.025,6} = 2.447$. Since $|t_0| < t_{0.025,6}$, we fail to reject $H_0$."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}
isye6739_mod123ule7_question_9 = {
    'question': (
        "A manufacturer claims that the standard deviation in the use of a precision instrument is $0.00002$ inch. "
        "An analyst tests the instrument 8 times and finds a sample standard deviation of $0.00005$ inch. "
        "Using $\\alpha = 0.01$, test the claim. Is the claim justified?"
    ),
    'options_list': [
        'A) Reject $H_0$, the claim is justified',
        'B) Fail to reject $H_0$, the claim is justified',
        'C) Reject $H_0$, the claim is unjustified',
        'D) Fail to reject $H_0$, the claim is unjustified'
    ],
    'correct_answer': 'C) Reject $H_0$, the claim is unjustified',
    'explanation': (
        "We test $H_0: \\sigma \\leq 0.00002$ vs. $H_1: \\sigma > 0.00002$. The test statistic is:\n"
        "$\\chi_0^2 = \\frac{(n-1)s^2}{\\sigma_0^2} = \\frac{7(0.00005)^2}{(0.00002)^2} = 43.75$.\n"
        "The critical value at $\\alpha = 0.01$ for $\\chi^2_{0.99,7}$ is 18.475. Since $\\chi_0^2 > 18.475$, we reject $H_0$.\n"
        "The claim that $\\sigma \\leq 0.00002$ is unjustified."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_mod1ule7_question_10 = {
    'question': (
        "Two samples drawn from two normal populations are provided below:\n"
        "Sample 1: $4.34, 5.00, 4.97, 4.25, 5.55, 6.55, 6.37, 5.55, 3.76$\n"
        "Sample 2: $1.87, 2.00, 2.00, 1.85, 2.11, 2.31, 2.28, 2.07, 1.76, 1.91, 2.00$\n"
        "Is there evidence to conclude that the variance of population 1 is greater than that of population 2? Use $\\alpha = 0.01$."
    ),
    'options_list': [
        'A) Reject $H_0$ at $\\alpha = 0.01$',
        'B) Fail to reject $H_0$ at $\\alpha = 0.01$',
        'C) Reject $H_0$ at $\\alpha = 0.05$',
        'D) Fail to reject $H_0$ at $\\alpha = 0.05$'
    ],
    'correct_answer': 'A) Reject $H_0$ at $\\alpha = 0.01$',
    'explanation': (
        "We test $H_0: \\sigma_1^2 = \\sigma_2^2$ vs. $H_1: \\sigma_1^2 > \\sigma_2^2$. The test statistic is:\n"
        "$F_0 = \\frac{s_1^2}{s_2^2} = \\frac{0.9027}{0.0294} = 30.69$.\n"
        "The critical value for $F_{0.01,8,10}$ is 5.06. Since $F_0 > 5.06$, we reject $H_0$.\n"
        "There is evidence that the variance of population 1 is greater than that of population 2."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}

isye6739_modul1e7_question_11 = {
    'question': (
        "A pollster surveyed 400 randomly selected motorists and found that 48 were uninsured. "
        "Test the hypothesis that the actual uninsured rate is at most 10% ($p_0 = 0.10$). Use $\\alpha = 0.05$."
    ),
    'options_list': [
        'A) Reject $H_0$ at $\\alpha = 0.05$',
        'B) Fail to reject $H_0$ at $\\alpha = 0.05$',
        'C) Reject $H_0$ at $\\alpha = 0.01$',
        'D) Fail to reject $H_0$ at $\\alpha = 0.01$'
    ],
    'correct_answer': 'B) Fail to reject $H_0$ at $\\alpha = 0.05$',
    'explanation': (
        "We test $H_0: p \\leq 0.10$ vs. $H_1: p > 0.10$ using the normal approximation. The test statistic is:\n"
        "$Z_0 = \\frac{x - np_0}{\\sqrt{np_0(1-p_0)}} = \\frac{48 - 400(0.1)}{\\sqrt{400(0.1)(0.9)}} = 1.333$.\n"
        "At $\\alpha = 0.05$, $z_{0.05} = 1.645$. Since $Z_0 < 1.645$, we fail to reject $H_0$.\n"
        "There is no evidence to conclude that the uninsured rate exceeds 10%."
    ),
    'chapter_information': 'ISYE 6739 - Module 7'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

MODULE_2_MPC = KC_MPC_QUESTIONS[:-1]