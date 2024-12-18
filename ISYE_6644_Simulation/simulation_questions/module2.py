isye6739_module2_discrete_rv_question_1 = {
    'question': "Let $X$ be a discrete random variable with a uniform distribution over $\\{1, 2, ..., n\\}$, where each value has probability $\\frac{1}{n}$. What is $P(X = 3)$ if $n = 10$?",
    'options_list': [
        'A) 0.05',
        'B) 0.10',
        'C) 0.20',
        'D) 0.50'
    ],
    'correct_answer': 'B) 0.10',
    'explanation': (
        "In a uniform distribution, each value has an equal probability of $\\frac{1}{n}$.\n"
        "Here, $P(X = 3) = \\frac{1}{n} = \\frac{1}{10} = 0.10$."
    ),
    'chapter_information': 'ISYE 6739, Module 2'
}

isye6739_module2_discrete_rv_question_2 = {
    'question': "Suppose $X \\sim \\text{Bin}(3, \\frac{1}{6})$. What is $P(X = 2)$?",
    'options_list': [
        'A) $\\frac{5}{36}$',
        'B) $\\frac{10}{36}$',
        'C) $\\frac{15}{216}$',
        'D) $\\frac{15}{36}$'
    ],
    'correct_answer': 'C) $\\frac{15}{216}$',
    'explanation': (
        "The probability mass function of a binomial distribution is given by:\n"
        "$P(X = k) = \\binom{n}{k} p^k (1-p)^{n-k}$\n"
        "Here, $n = 3$, $k = 2$, $p = \\frac{1}{6}$, and $1-p = \\frac{5}{6}$.\n"
        "$P(X = 2) = \\binom{3}{2} \\left(\\frac{1}{6}\\right)^2 \\left(\\frac{5}{6}\\right)^1 = 3 \\cdot \\frac{1}{36} \\cdot \\frac{5}{6} = \\frac{15}{216}$."
    ),
    'chapter_information': 'ISYE 6739, Module 2'
}

isye6739_module2_discrete_rv_question_3 = {
    'question': "Roll two dice and get the sum. Repeat this experiment 12 times. What is $P($Sum will be 7 or 11 exactly 3 times$)$?",
    'options_list': [
        'A) $\\binom{12}{3} \\left(\\frac{2}{9}\\right)^3 \\left(\\frac{7}{9}\\right)^9$',
        'B) $\\binom{12}{3} \\left(\\frac{1}{9}\\right)^3 \\left(\\frac{8}{9}\\right)^9$',
        'C) $\\binom{12}{3} \\left(\\frac{1}{6}\\right)^3 \\left(\\frac{5}{6}\\right)^9$',
        'D) $\\binom{12}{3} \\left(\\frac{2}{9}\\right)^3 \\left(\\frac{5}{9}\\right)^9$'
    ],
    'correct_answer': 'A) $\\binom{12}{3} \\left(\\frac{2}{9}\\right)^3 \\left(\\frac{7}{9}\\right)^9$',
    'explanation': (
        "Let $X$ denote the number of times the sum is 7 or 11. This follows a binomial distribution: $X \\sim \\text{Bin}(12, \\frac{2}{9})$.\n"
        "$P(X = 3) = \\binom{12}{3} \\left(\\frac{2}{9}\\right)^3 \\left(\\frac{7}{9}\\right)^9$."
    ),
    'chapter_information': 'ISYE 6739, Module 2'
}

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

isye6739_module2_discrete_rv_question_5 = {
    'question': "Suppose $X \\sim \\text{Bin}(5, 0.2)$. What is the expected value and variance of $X$?",
    'options_list': [
        'A) $E(X) = 1$, $Var(X) = 0.8$',
        'B) $E(X) = 2$, $Var(X) = 0.8$',
        'C) $E(X) = 1$, $Var(X) = 0.6$',
        'D) $E(X) = 2$, $Var(X) = 0.6$'
    ],
    'correct_answer': 'D) $E(X) = 2$, $Var(X) = 0.6$',
    'explanation': (
        "For a binomial random variable $X \\sim \\text{Bin}(n, p)$, the expected value is:\n"
        "$E(X) = np$, and the variance is $Var(X) = np(1-p)$.\n"
        "Here, $n = 5$ and $p = 0.2$.\n"
        "$E(X) = 5 \\cdot 0.2 = 1$, and $Var(X) = 5 \\cdot 0.2 \\cdot 0.8 = 0.6$."
    ),
    'chapter_information': 'ISYE 6739, Module 2'
}

probability_theory_ucboulder_question_1 = {
    'question': "A critical system has 5 different components, each of which works with probability 0.90. Assume each component works independently of the others. Let $X$ be the number of components that are working. What is $P(X=2)$? (Round your answer to four decimal places.)",
    'options_list': [
        'A) 0.0001',
        'B) 0.0081',
        'C) 0.0810',
        'D) 0.8100'
    ],
    'correct_answer': 'B) 0.0081',
    'explanation': (
        "The probability of exactly 2 components working follows a binomial distribution:\n"
        "$P(X=k) = \\binom{n}{k}p^k(1-p)^{n-k}$\n"
        "Here, $n=5$, $k=2$, $p=0.90$.\n"
        "$P(X=2) = \\binom{5}{2}(0.90)^2(0.10)^3 = 10 \\cdot 0.81 \\cdot 0.001 = 0.0081$"
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_2 = {
    'question': "A certain system can experience three different types of defects. Let $A_i$, $i=1,2,3$, be the event that the system has a defect of type $i$. Suppose that $P(A_1)=0.17$, $P(A_2)=0.07$, $P(A_3)=0.13$, $P(A_1 \\cup A_2)=0.18$, $P(A_2 \\cup A_3)=0.18$, $P(A_1 \\cup A_3)=0.19$, and $P(A_1 \\cap A_2 \\cap A_3)=0.01$. Let the random variable $X$ be the number of defects that are present. What is $P(X=0)$?",
    'options_list': [
        'A) 0.81',
        'B) 0.18',
        'C) 0.01',
        'D) 0.19'
    ],
    'correct_answer': 'A) 0.81',
    'explanation': (
        "If $X=0$, no defects are present. Using the inclusion-exclusion principle:\n"
        "$P(X=0) = 1 - P(A_1 \\cup A_2 \\cup A_3)$\n"
        "$P(A_1 \\cup A_2 \\cup A_3) = P(A_1) + P(A_2) + P(A_3) - P(A_1 \\cup A_2) - P(A_2 \\cup A_3) - P(A_1 \\cup A_3) + P(A_1 \\cap A_2 \\cap A_3)$\n"
        "$P(A_1 \\cup A_2 \\cup A_3) = 0.17 + 0.07 + 0.13 - 0.18 - 0.18 - 0.19 + 0.01 = 0.19$\n"
        "$P(X=0) = 1 - 0.19 = 0.81$"
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_3 = {
    'question': "A certain system can experience three different types of defects. Let $A_i$, $i=1,2,3$, be the event that the system has a defect of type $i$. Suppose that $P(A_1)=0.17$, $P(A_2)=0.07$, $P(A_3)=0.13$, $P(A_1 \\cup A_2)=0.18$, $P(A_2 \\cup A_3)=0.18$, $P(A_1 \\cup A_3)=0.19$, and $P(A_1 \\cap A_2 \\cap A_3)=0.01$. Let the random variable $X$ be the number of defects that are present. What is $P(X=1)$?",
    'options_list': [
        'A) 0.81',
        'B) 0.16',
        'C) 0.02',
        'D) 0.01'
    ],
    'correct_answer': 'C) 0.02',
    'explanation': (
        "To compute $P(X=1)$, calculate the probability that exactly one defect occurs using:\n"
        "$P(X=1) = P(A_1 \\cap \\neg A_2 \\cap \\neg A_3) + P(\\neg A_1 \\cap A_2 \\cap \\neg A_3) + P(\\neg A_1 \\cap \\neg A_2 \\cap A_3)$\n"
        "From the given probabilities and independence of events, $P(X=1) = 0.02$."
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_4 = {
    'question': "A certain system can experience three different types of defects. Let $A_i$, $i=1,2,3$, be the event that the system has a defect of type $i$. Suppose that $P(A_1)=0.17$, $P(A_2)=0.07$, $P(A_3)=0.13$, $P(A_1 \\cup A_2)=0.18$, $P(A_2 \\cup A_3)=0.18$, $P(A_1 \\cup A_3)=0.19$, and $P(A_1 \\cap A_2 \\cap A_3)=0.01$. Let the random variable $X$ be the number of defects that are present. What is $P(X=2)$?",
    'options_list': [
        'A) 0.01',
        'B) 0.16',
        'C) 0.81',
        'D) 0.02'
    ],
    'correct_answer': 'B) 0.16',
    'explanation': (
        "To compute $P(X=2)$, calculate the probability that exactly two defects occur using:\n"
        "$P(X=2) = P((A_1 \\cap A_2 \\cap \\neg A_3) + (A_1 \\cap \\neg A_2 \\cap A_3) + (\\neg A_1 \\cap A_2 \\cap A_3))$\n"
        "From the given probabilities and inclusion-exclusion principle, $P(X=2) = 0.16$."
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
}

probability_theory_ucboulder_question_5 = {
    'question': "A certain system can experience three different types of defects. Let $A_i$, $i=1,2,3$, be the event that the system has a defect of type $i$. Suppose that $P(A_1)=0.17$, $P(A_2)=0.07$, $P(A_3)=0.13$, $P(A_1 \\cup A_2)=0.18$, $P(A_2 \\cup A_3)=0.18$, $P(A_1 \\cup A_3)=0.19$, and $P(A_1 \\cap A_2 \\cap A_3)=0.01$. Let the random variable $X$ be the number of defects that are present. What is $P(X=3)$?",
    'options_list': [
        'A) 0.01',
        'B) 0.81',
        'C) 0.16',
        'D) 0.02'
    ],
    'correct_answer': 'A) 0.01',
    'explanation': (
        "The probability of all three defects occurring is given directly as:\n"
        "$P(X=3) = P(A_1 \\cap A_2 \\cap A_3) = 0.01$."
    ),
    'chapter_information': 'Probability Theory - Coursera UC Boulder Course'
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

mitx_6431x_probability_question_1 = {
    'question': "Two rolls of a 4-sided die are performed, with all 16 outcomes equally likely. Let $X$ be the result of the first roll and $Y$ be the result of the second roll. Define $W = XY$. What is $p_W(4)$?",
    'options_list': [
        'A) 0.1250',
        'B) 0.1875',
        'C) 0.2500',
        'D) 0.3750'
    ],
    'correct_answer': 'B) 0.1875',
    'explanation': (
        "The event $W=4$ can occur in three ways: $(1,4), (2,2), (4,1)$. Each outcome has probability $1/16$ since all outcomes are equally likely.\n"
        "Thus, $p_W(4) = \\frac{3}{16} = 0.1875$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_2 = {
    'question': "Two rolls of a 4-sided die are performed, with all 16 outcomes equally likely. Let $X$ be the result of the first roll and $Y$ be the result of the second roll. Define $W = XY$. What is $p_W(5)$?",
    'options_list': [
        'A) 0.0000',
        'B) 0.0625',
        'C) 0.1250',
        'D) 0.1875'
    ],
    'correct_answer': 'A) 0.0000',
    'explanation': (
        "The event $W=5$ cannot happen because no combination of $X$ and $Y$ (each from 1 to 4) produces $XY = 5$.\n"
        "Thus, $p_W(5) = 0$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_3 = {
    'question': "Let $X$ be a random variable that takes integer values, with PMF $p_X(x)$. Let $Y$ be another integer-valued random variable and let $y$ be a number. Is $p_X(y)$ a random variable or a number?",
    'options_list': [
        'A) Random variable',
        'B) Number',
        'C) Function',
        'D) Undefined'
    ],
    'correct_answer': 'B) Number',
    'explanation': (
        "The PMF $p_X(\\cdot)$ maps real numbers to real values. When we give it a specific numerical argument $y$, it outputs a number."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_4 = {
    'question': "Let $X$ be a random variable with PMF $p_X(x)$, and $Y$ be another random variable. Is $p_X(Y)$ a random variable or a number?",
    'options_list': [
        'A) Random variable',
        'B) Number',
        'C) Constant',
        'D) Undefined'
    ],
    'correct_answer': 'A) Random variable',
    'explanation': (
        "Here, $p_X(Y)$ is a function of the random variable $Y$. A function of a random variable is itself a random variable."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_5 = {
    'question': "Let $A$ and $B$ be two events with non-empty intersection. Let $I_A$ and $I_B$ be the associated indicator random variables. Is $I_A + I_B$ the indicator random variable of any event?",
    'options_list': [
        'A) Yes, it is the indicator of $A \\cap B$',
        'B) Yes, it is the indicator of $A \\cup B$',
        'C) No, it is not the indicator random variable of any event',
        'D) Yes, it is the indicator of $A \\setminus B$'
    ],
    'correct_answer': 'C) No, it is not the indicator random variable of any event',
    'explanation': (
        "The sum $I_A + I_B$ takes values in $\{0, 1, 2\}$. However, indicator random variables can only take values 0 or 1.\n"
        "Thus, $I_A + I_B$ is not an indicator random variable."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_6 = {
    'question': "Let $A$ and $B$ be two events with non-empty intersection. Let $I_A$ and $I_B$ be the associated indicator random variables. Is $I_A \\cdot I_B$ the indicator random variable of any event?",
    'options_list': [
        'A) Yes, it is the indicator of $A \\cup B$',
        'B) Yes, it is the indicator of $A \\cap B$',
        'C) No, it is not an indicator random variable',
        'D) Yes, it is the indicator of $A \\setminus B$'
    ],
    'correct_answer': 'B) Yes, it is the indicator of $A \\cap B$',
    'explanation': (
        "The product $I_A \\cdot I_B$ equals 1 if and only if both $A$ and $B$ occur. Thus, $I_A \\cdot I_B$ is the indicator random variable of $A \\cap B$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_7 = {
    'question': "You roll a fair six-sided die 5 times independently. Let $X$ be the number of times the roll results in a 2 or a 3. What is $p_X(2.5)$?",
    'options_list': [
        'A) 0.32922',
        'B) 0.0000',
        'C) 0.1250',
        'D) 0.5000'
    ],
    'correct_answer': 'B) 0.0000',
    'explanation': (
        "Since $X$ represents the number of rolls resulting in a 2 or 3, it must be an integer. Therefore, $p_X(2.5) = 0$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_8 = {
    'question': "You roll a fair six-sided die 5 times independently. Let $X$ be the number of times the roll results in a 2 or a 3. What is $p_X(1)$?",
    'options_list': [
        'A) 0.1250',
        'B) 0.32922',
        'C) 0.5000',
        'D) 0.0000'
    ],
    'correct_answer': 'B) 0.32922',
    'explanation': (
        "The random variable $X$ follows a binomial distribution with $n=5$ and $p=1/3$. The probability mass function is:\n"
        "$p_X(k) = \\binom{5}{k} (1/3)^k (2/3)^{5-k}$\n"
        "For $k=1$:\n"
        "$p_X(1) = \\binom{5}{1} (1/3)^1 (2/3)^4 \\approx 0.32922$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}


mitx_6431x_probability_question_9 = {
    'question': "The PMF of the random variable $Y$ satisfies $p_Y(-1) = \\frac{1}{6}$, $p_Y(2) = \\frac{2}{6}$, $p_Y(5) = \\frac{3}{6}$, and $p_Y(y) = 0$ for all other values of $y$. What is the expected value of $Y$?",
    'options_list': [
        'A) 2',
        'B) 3',
        'C) 4',
        'D) 5'
    ],
    'correct_answer': 'B) 3',
    'explanation': (
        "The expected value is calculated as:\n"
        "$E[Y] = (-1) \\cdot \\frac{1}{6} + 2 \\cdot \\frac{2}{6} + 5 \\cdot \\frac{3}{6}$\n"
        "$= \\frac{-1}{6} + \\frac{4}{6} + \\frac{15}{6} = \\frac{18}{6} = 3$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_10 = {
    'question': "Suppose a random variable $X$ can take any value in the interval $[-1, 2]$ and a random variable $Y$ can take any value in the interval $[-2, 3]$. The random variable $X - Y$ can take values in an interval $[a, b]$. What are the values of $a$ and $b$?",
    'options_list': [
        'A) $a = -4$, $b = 4$',
        'B) $a = -3$, $b = 3$',
        'C) $a = -5$, $b = 5$',
        'D) $a = -6$, $b = 6$'
    ],
    'correct_answer': 'A) $a = -4$, $b = 4$',
    'explanation': (
        "The smallest value of $X - Y$ is obtained when $X = -1$ and $Y = 3$, giving $X - Y = -1 - 3 = -4$.\n"
        "The largest value of $X - Y$ is obtained when $X = 2$ and $Y = -2$, giving $X - Y = 2 - (-2) = 4$.\n"
        "Thus, the interval is $[-4, 4]$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_11 = {
    'question': "Let $X$ be a uniform random variable on the range $\{-1, 0, 1, 2\}$. Let $Y = X^4$. Use the expected value rule to calculate $E[Y]$.",
    'options_list': [
        'A) 3.5',
        'B) 4.5',
        'C) 5.5',
        'D) 6.0'
    ],
    'correct_answer': 'B) 4.5',
    'explanation': (
        "The expected value $E[Y]$ is:\n"
        "$E[Y] = E[X^4] = \\sum_x x^4 p_X(x)$\n"
        "Given $p_X(x) = \\frac{1}{4}$ for all $x$, calculate:\n"
        "$E[Y] = (-1)^4 \\cdot \\frac{1}{4} + 0^4 \\cdot \\frac{1}{4} + 1^4 \\cdot \\frac{1}{4} + 2^4 \\cdot \\frac{1}{4}$\n"
        "$= \\frac{1}{4} + 0 + \\frac{1}{4} + \\frac{16}{4} = 4.5$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_12 = {
    'question': "The random variable $X$ satisfies $E[X] = 2$ and $E[X^2] = 7$. Find the expected value of $8 - X$.",
    'options_list': [
        'A) 6',
        'B) 4',
        'C) 2',
        'D) 8'
    ],
    'correct_answer': 'A) 6',
    'explanation': (
        "Using the linearity of expectation:\n"
        "$E[8 - X] = E[8] - E[X]$\n"
        "Since $E[8] = 8$ and $E[X] = 2$, we get:\n"
        "$E[8 - X] = 8 - 2 = 6$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

mitx_6431x_probability_question_13 = {
    'question': "The random variable $X$ satisfies $E[X] = 2$ and $E[X^2] = 7$. Find the expected value of $(X - 3)(X + 3)$.",
    'options_list': [
        'A) -2',
        'B) 0',
        'C) 2',
        'D) 7'
    ],
    'correct_answer': 'A) -2',
    'explanation': (
        "Expand $(X - 3)(X + 3)$ as $X^2 - 9$.\n"
        "Using linearity of expectation:\n"
        "$E[(X - 3)(X + 3)] = E[X^2] - 9$\n"
        "Given $E[X^2] = 7$, we get:\n"
        "$E[(X - 3)(X + 3)] = 7 - 9 = -2$."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

isye6739_lecture6_question_1 = {
    'question': "Suppose $X$ is a continuous random variable with PDF:\n"
                "$f(x) = \\begin{cases} c x^2 & \\text{if } 0 < x < 2 \\\\ 0 & \\text{otherwise} \\end{cases}$\n"
                "What is the value of $c$ such that the PDF integrates to 1?",
    'options_list': [
        'A) $\\frac{2}{3}$',
        'B) $\\frac{3}{8}$',
        'C) $\\frac{5}{8}$',
        'D) $\\frac{3}{4}$'
    ],
    'correct_answer': 'B) $\\frac{3}{8}$',
    'explanation': (
        "To normalize the PDF, we solve:\n"
        "$\\int_{0}^{2} c x^2 dx = 1$\n"
        "Integrating:\n"
        "$c \\int_{0}^{2} x^2 dx = c \\left[ \\frac{x^3}{3} \\right]_0^2 = c \\cdot \\frac{8}{3}$\n"
        "Setting this equal to 1 gives:\n"
        "$c \\cdot \\frac{8}{3} = 1 \\implies c = \\frac{3}{8}$."
    ),
    'chapter_information': 'ISYE 6739 Lecture 6'
}

isye6739_lecture6_question_2 = {
    'question': "Given $f(x) = \\frac{3}{8}x^2$ for $0 < x < 2$, what is $P(0 < X < 1)$?",
    'options_list': [
        'A) $\\frac{1}{4}$',
        'B) $\\frac{1}{8}$',
        'C) $\\frac{3}{8}$',
        'D) $\\frac{2}{3}$'
    ],
    'correct_answer': 'B) $\\frac{1}{8}$',
    'explanation': (
        "The probability is calculated as:\n"
        "$P(0 < X < 1) = \\int_{0}^{1} \\frac{3}{8}x^2 dx$\n"
        "Integrating:\n"
        "$\\int_{0}^{1} \\frac{3}{8}x^2 dx = \\frac{3}{8} \\cdot \\left[ \\frac{x^3}{3} \\right]_0^1$\n"
        "$= \\frac{3}{8} \\cdot \\frac{1}{3} = \\frac{1}{8}$."
    ),
    'chapter_information': 'ISYE 6739 Lecture 6'
}

isye6739_lecture6_question_3 = {
    'question': "For a continuous random variable $X$ with PDF $f(x) = \\frac{3}{8}x^2$ over $0 < x < 2$, compute the conditional probability:\n"
                "$P(0 < X < 1 \\mid \\frac{1}{2} < X < \\frac{3}{2})$.",
    'options_list': [
        'A) $\\frac{3}{26}$',
        'B) $\\frac{5}{26}$',
        'C) $\\frac{7}{26}$',
        'D) $\\frac{1}{4}$'
    ],
    'correct_answer': 'C) $\\frac{7}{26}$',
    'explanation': (
        "The conditional probability is given by:\n"
        "$P(0 < X < 1 \\mid \\frac{1}{2} < X < \\frac{3}{2}) = \\frac{P(0 < X < 1 \\cap \\frac{1}{2} < X < \\frac{3}{2})}{P(\\frac{1}{2} < X < \\frac{3}{2})}$\n"
        "Numerator: $P(\\frac{1}{2} < X < 1) = \\int_{1/2}^{1} \\frac{3}{8}x^2 dx$\n"
        "Denominator: $P(\\frac{1}{2} < X < \\frac{3}{2}) = \\int_{1/2}^{3/2} \\frac{3}{8}x^2 dx$\n"
        "Calculating the integrals, we find the ratio equals $\\frac{7}{26}$."
    ),
    'chapter_information': 'ISYE 6739 Lecture 6'
}

isye6739_lecture6_question_4 = {
    'question': "If $X \\sim \\text{Uniform}(0, 1)$, what is the CDF $F(x)$ of $X$?",
    'options_list': [
        'A) $F(x) = 0$ if $x \\leq 0$, $F(x) = x$ if $0 < x < 1$, $F(x) = 1$ if $x \\geq 1$',
        'B) $F(x) = 1$ for all $x > 0$',
        'C) $F(x) = e^{-x}$ for $x > 0$',
        'D) $F(x) = x^2$ for $0 < x < 1$'
    ],
    'correct_answer': 'A) $F(x) = 0$ if $x \\leq 0$, $F(x) = x$ if $0 < x < 1$, $F(x) = 1$ if $x \\geq 1$',
    'explanation': (
        "For a uniform distribution $X \\sim \\text{Uniform}(0, 1)$, the CDF is:\n"
        "$F(x) = \\begin{cases} 0 & x \\leq 0 \\\\ x & 0 < x < 1 \\\\ 1 & x \\geq 1 \\end{cases}$."
    ),
    'chapter_information': 'ISYE 6739 Lecture 6'
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


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_2_MPC = KC_MPC_QUESTIONS[:-1]