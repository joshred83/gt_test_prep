module3_question1 = {
    'question': (
        "A refrigerator manufacturer subjects his finished products to a final inspection. Of interest are two categories of defects: scratches or flaws in the porcelain finish, and mechanical defects. "
        "The number of each type of defect is a random variable. The results of inspecting 50 refrigerators are shown in the following joint pmf table, where $X$ represents the occurrence of finish defects and $Y$ represents the occurrence of mechanical defects:\n\n"
        "| Y \\ X | 0  | 1  | 2  | 3  | 4  | 5  |\n"
        "|--------|----|----|----|----|----|----|\n"
        "| 0      | 11/50 | 4/50 | 2/50 | 1/50 | 1/50 | 1/50 |\n"
        "| 1      | 8/50  | 3/50 | 2/50 | 1/50 | 1/50 |     |\n"
        "| 2      | 4/50  | 3/50 | 2/50 | 1/50 |     |     |\n"
        "| 3      | 3/50  | 1/50 |      |      |     |     |\n"
        "| 4      | 1/50  |      |      |      |     |     |\n\n"
        "Find the marginal probability mass functions of $X$ and $Y$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The marginal pmf for $X$ is:\n"
        "$f_X(x) = \\{27/50, 11/50, 6/50, 3/50, 2/50, 1/50\\}$ for $x = 0, 1, 2, 3, 4, 5$\n\n"
        "The marginal pmf for $Y$ is:\n"
        "$f_Y(y) = \\{20/50, 15/50, 10/50, 4/50, 1/50\\}$ for $y = 0, 1, 2, 3, 4$."
    ),
    'explanation': (
        "To find the marginal pmf of $X$, sum over all values of $Y$ for each $X$. Similarly, to find the marginal pmf of $Y$, sum over all values of $X$ for each $Y$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question2 = {
    'question': (
        "Find the conditional pmf of mechanical defects $Y$, given that there are no finish defects ($X=0$)."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "$f_{Y|X=0}(y) = \\frac{f(0, y)}{f_X(0)} = \\left\\{\n"
        "\\begin{array}{ll}\n"
        "11/27 & \\text{if } y = 0 \\\\\n"
        "8/27 & \\text{if } y = 1 \\\\\n"
        "4/27 & \\text{if } y = 2 \\\\\n"
        "3/27 & \\text{if } y = 3 \\\\\n"
        "1/27 & \\text{if } y = 4 \\\\\n"
        "0 & \\text{otherwise.}\n"
        "\\end{array}\n"
        "\\right.$"
    ),
    'explanation': (
        "The conditional pmf is obtained by dividing the joint probability $f(0,y)$ by the marginal probability $f_X(0)$, which is $27/50$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question3 = {
    'question': (
        "Consider a situation in which the surface tension and acidity of a chemical product are measured. The variables are coded such that surface tension is measured on a scale $0 \\leq X \\leq 2$, and acidity is measured on a scale $2 \\leq Y \\leq 4$. The joint pdf of $(X, Y)$ is:\n\n"
        "$f(x, y) = \\left\\{ \\begin{array}{ll} c(6 - x - y) & \\text{if } 0 \\leq x \\leq 2, 2 \\leq y \\leq 4 \\\\\n"
        "0 & \\text{otherwise}. \\end{array} \\right.$\n\n"
        "(a) Find the appropriate value of $c$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "By integrating $f(x, y)$ over the given range and setting it equal to 1:\n\n"
        "$\\int_{2}^{4} \\int_{0}^{2} c(6 - x - y) \\ dx \\ dy = 1$.\n\n"
        "This gives $c = 1/8$."
    ),
    'explanation': (
        "The total probability must integrate to 1. Solving for $c$ involves evaluating the double integral of $c(6 - x - y)$ over the given region."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question4 = {
    'question': (
        "Consider the joint pdf $f(x, y) = c(6 - x - y)$ for $0 \\leq x \\leq 2$ and $2 \\leq y \\leq 4$. "
        "Calculate the probability that $X < 1$ and $Y < 3$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The probability is:\n\n"
        "$P(X < 1, Y < 3) = \\int_{2}^{3} \\int_{0}^{1} \\frac{1}{8} (6 - x - y) \\, dx \\, dy = \\frac{3}{8}$."
    ),
    'explanation': (
        "Integrate the given joint pdf $f(x, y)$ over the region $0 \\leq x < 1$ and $2 \\leq y < 3$ to compute the desired probability."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question5 = {
    'question': (
        "For the joint pdf $f(x, y) = c(6 - x - y)$, calculate the probability that $X + Y \\leq 4$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The probability is:\n\n"
        "$P(X + Y \\leq 4) = \\int_{2}^{4} \\int_{0}^{4 - y} \\frac{1}{8} (6 - x - y) \\, dx \\, dy = \\frac{2}{3}$."
    ),
    'explanation': (
        "To find $P(X + Y \\leq 4)$, integrate the joint pdf over the appropriate triangular region defined by $0 \\leq x \\leq 2$, $2 \\leq y \\leq 4$, and $x + y \\leq 4$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question6 = {
    'question': (
        "Find the marginal pdf of $X$ for the joint pdf $f(x, y) = c(6 - x - y)$ where $0 \\leq x \\leq 2$ and $2 \\leq y \\leq 4$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The marginal pdf of $X$ is:\n\n"
        "$f_X(x) = \\int_{2}^{4} \\frac{1}{8} (6 - x - y) \\, dy = \\frac{3 - x}{4}, \\ 0 < x < 2$."
    ),
    'explanation': (
        "To find the marginal pdf $f_X(x)$, integrate the joint pdf $f(x, y)$ over $y$ in the range $[2, 4]$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question7 = {
    'question': (
        "Given the joint pdf $f(x, y) = cxy^2$ for $0 < x < y^2 < 1$, find the constant $c$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The constant $c$ is:\n\n"
        "$1 = \\int_{0}^{1} \\int_{0}^{y^2} cxy^2 \\, dx \\, dy \\implies c = 14$."
    ),
    'explanation': (
        "To determine $c$, integrate $f(x, y)$ over the given range $0 < x < y^2$ and $0 < y < 1$, and set the integral equal to 1."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question8 = {
    'question': (
        "For the joint pdf $f(x, y) = 14xy^2$ where $0 < x < y^2 < 1$, find the marginal pdf of $Y$, $f_Y(y)$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The marginal pdf of $Y$ is:\n\n"
        "$f_Y(y) = \\int_{0}^{y^2} 14xy^2 \\, dx = 7y^6, \\ 0 < y < 1$."
    ),
    'explanation': (
        "To find $f_Y(y)$, integrate the joint pdf $f(x, y)$ with respect to $x$ over the range $0 < x < y^2$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question9 = {
    'question': (
        "Given the joint pdf $f(x, y) = 14xy^2$ for $0 < x < y^2 < 1$, find the conditional pdf of $X$ given $Y = y$, $f(x|y)$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "The conditional pdf is:\n\n"
        "$f(x|y) = \\frac{f(x, y)}{f_Y(y)} = \\frac{2x}{y^4}, \\ 0 < x < y^2 < 1$."
    ),
    'explanation': (
        "The conditional pdf $f(x|y)$ is obtained by dividing the joint pdf $f(x, y)$ by the marginal pdf $f_Y(y)$."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}

module3_question10 = {
    'question': (
        "Given the joint pdf $g(x, y) = 4xye^{-(x^2 + y^2)}$, determine whether $X$ and $Y$ are independent."
    ),
    'options_list': ['Independent', 'Not Independent'],
    'correct_answer': "Independent",
    'explanation': (
        "The joint pdf $g(x, y) = 4xye^{-(x^2 + y^2)}$ can be factored as $g(x, y) = (4xe^{-x^2})(ye^{-y^2})$, "
        "showing that $X$ and $Y$ are independent."
    ),
    'chapter_information': 'ISYE 6739 - Module 3'
}



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

gtx_isye6739xi_probability_and_statistics_i_fa24_question_6 = {
    'question': "If the sample space $S$ for rolling two dice is all possible ordered pairs of numbers, what is the cardinality of $S$?",
    'options_list': [
        '6',
        '12',
        '36',
        '72'
    ],
    'correct_answer': '36',
    'explanation': (
        "The sample space $S$ consists of all ordered pairs (e.g., $(1, 1), (1, 2), \\ldots, (6, 6)$). "
        "Since each die has 6 faces, the total outcomes are $6 \\times 6 = 36$, making the cardinality of $S$ equal to 36."
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

exercise_14_discrete_prob_question = {
    'question': (
        "Consider the model of two rolls of a tetrahedral die (with 16 outcomes equally likely). Find the probability of the following events:\n"
        "1. The value in the first roll is strictly larger than the value in the second roll.\n"
        "2. The sum of the values obtained in the two rolls is an even number."
    ),
    'options_list': [
        "For (a): 0.375, For (b): 0.5",
        "For (a): 0.25, For (b): 0.75",
        "For (a): 0.5, For (b): 0.375",
        "For (a): 0.25, For (b): 0.25"
    ],
    'correct_answer': "For (a): 0.375, For (b): 0.5",
    'explanation': (
        "**(a)** The sample space consists of all pairs $(x_1, x_2)$ where $x_1, x_2 \\in \\{1, 2, 3, 4\\}$, with 16 total outcomes. "
        "The event where the first roll is strictly larger than the second includes outcomes "
        "$\\{(2, 1), (3, 1), (4, 1), (3, 2), (4, 2), (4, 3)\\}$, with 6 outcomes. The probability is:\n"
        "$$ \\frac{6}{16} = \\frac{3}{8} = 0.375 $$\n"
        "**(b)** The event where the sum of the values is even includes outcomes "
        "$\\{(1, 1), (2, 2), (3, 3), (4, 4), (1, 3), (3, 1), (2, 4), (4, 2)\\}$, with 8 outcomes. The probability is:\n"
        "$$ \\frac{8}{16} = \\frac{1}{2} = 0.5 $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

exercise_continuous_prob_question = {
    'question': (
        "Consider a sample space defined as the rectangular region $[0,1] \\times [0,2]$. Assume a uniform probability law "
        "(the probability of an event is proportional to its area). Find the probability of the following events:\n"
        "1. The two components $x$ and $y$ have the same values.\n"
        "2. $x \\geq y$, where $x$ is the first component and $y$ the second.\n"
        "3. $x^2 \\geq y$."
    ),
    'options_list': [
        "For (a): 0, For (b): 0.25, For (c): 0.16667",
        "For (a): 0, For (b): 0.5, For (c): 0.2",
        "For (a): 0.1, For (b): 0.25, For (c): 0.3",
        "For (a): 0.1, For (b): 0.5, For (c): 0.16667"
    ],
    'correct_answer': "For (a): 0, For (b): 0.25, For (c): 0.16667",
    'explanation': (
        "**(a)** The condition $x = y$ corresponds to a line, and a line has zero area. Therefore, the probability is $0$.\n"
        "**(b)** The event $x \\geq y$ describes a triangle with vertices $(0, 0)$, $(1, 0)$, and $(1, 1)$. The area is:\n"
        "$$ \\text{Area} = \\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times 1 \\times 1 = \\frac{1}{4}. $$\n"
        "**(c)** The event $x^2 \\geq y$ corresponds to the region below the curve $y = x^2$ for $x \\in [0, 1]$. The area is:\n"
        "$$ \\int_0^1 x^2 \\, dx = \\frac{x^3}{3} \\Big|_0^1 = \\frac{1}{3} \\approx 0.16667. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

exercise_countable_additivity_question = {
    'question': (
        "Let the sample space be the set of positive integers, and suppose $P(n) = \\frac{1}{2^n}$, for $n = 1, 2, \\dots$. "
        "Find the probability of the set $\\{3, 6, 9, \\dots\\}$, i.e., the set of positive integers that are multiples of 3."
    ),
    'options_list': [
        "0.1",
        "0.14286",
        "0.2",
        "0.25"
    ],
    'correct_answer': "0.14286",
    'explanation': (
        "The set of multiples of 3 forms a geometric series:\n"
        "$$ P(3) + P(6) + P(9) + \\dots = \\frac{1}{2^3} + \\frac{1}{2^6} + \\frac{1}{2^9} + \\dots. $$\n"
        "Let $\\alpha = \\frac{1}{2^3} = \\frac{1}{8}$. Using the sum of a geometric series:\n"
        "$$ \\frac{\\alpha}{1 - \\alpha} = \\frac{1/8}{1 - 1/8} = \\frac{1/8}{7/8} = \\frac{1}{7} \\approx 0.14286. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

exercise_uniform_probabilities_question = {
    'question': (
        "Let the sample space be the set of all positive integers. Is it possible to have a 'uniform' probability law "
        "that assigns the same probability $c$ to each positive integer?"
    ),
    'options_list': [
        "Yes",
        "No"
    ],
    'correct_answer': "No",
    'explanation': (
        "If $c = 0$, then by countable additivity:\n"
        "$$ P(\\{1\\} \\cup \\{2\\} \\cup \\{3\\} \\dots) = c + c + c + \\dots = 0, $$\n"
        "which contradicts the normalization axiom requiring $P(\\Omega) = 1$.\n"
        "If $c > 0$, the sum $kc > 1$ for sufficiently large $k$, which also contradicts the normalization axiom.\n"
        "Thus, it is not possible."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

exercise_countable_additivity_2_question = {
    'question': (
        "Let the sample space be the two-dimensional plane. For any real number $x$, let $A_x$ be the subset of the plane "
        "that consists of all points on the vertical line through the point $(x, 0)$, i.e., $A_x = \\{(x, y): y \\in \\mathbb{R}\\}$.\n"
        "1. Do the axioms of probability theory imply that the probability of the union of the sets $A_x$ (the whole plane) is equal to "
        "the sum of the probabilities $P(A_x)$?\n"
        "2. Do the axioms of probability theory imply that:\n"
        "$$ P(A_1 \\cup A_2 \\cup \\dots) = \\sum_{x=1}^\\infty P(A_x)? $$"
    ),
    'options_list': [
        "For (a): Yes, For (b): No",
        "For (a): No, For (b): Yes",
        "For (a): Yes, For (b): Yes",
        "For (a): No, For (b): No"
    ],
    'correct_answer': "For (a): No, For (b): Yes",
    'explanation': (
        "**(a)** The collection of sets $A_x$ is uncountable because $x \\in \\mathbb{R}$. Additivity applies only to countable unions, "
        "so the answer is No.\n"
        "**(b)** Here, we consider only positive integers for $x$, making the collection countable. Countable additivity applies, "
        "so the answer is Yes."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

exercise_probabilities_continuous_question = {
    'question': (
        "Alice and Bob each choose at random a real number between 0 and 1. Assume the pair of numbers is chosen "
        "according to the uniform probability law on the unit square, so the probability of an event is equal to its area.\n\n"
        "We define the following events:\n"
        "- $A$: The magnitude of the difference (for any two real numbers $x$ and $y$, where the value $\\lvert x - y \\rvert$) "
        "of the two numbers is greater than $1/3$.\n"
        "- $B$: At least one of the numbers is greater than $1/4$.\n"
        "- $C$: The sum of the two numbers is 1.\n"
        "- $D$: Alice's number is greater than $1/4$.\n\n"
        "Find the probabilities:\n"
        "1. $P(A)$\n"
        "2. $P(B)$\n"
        "3. $P(A \\cap B)$\n"
        "4. $P(C)$\n"
        "5. $P(D)$\n"
        "6. $P(A \\cap D)$"
    ),
    'options_list': ['Do the Math'],
    'correct_answer': (
        "1. $P(A) = \\frac{4}{9} = 0.44444$\n"
        "2. $P(B) = \\frac{15}{16} = 0.9375$\n"
        "3. $P(A \\cap B) = \\frac{4}{9} = 0.44444$\n"
        "4. $P(C) = 0$\n"
        "5. $P(D) = \\frac{3}{4} = 0.75$\n"
        "6. $P(A \\cap D) = \\frac{89}{288} = 0.30903$"
    ),
    'explanation': (
        "**1. $P(A)$**: Event $A$ corresponds to all points $(x, y)$ where $\\lvert x - y \\rvert > 1/3$, forming two triangular regions. "
        "The area of each triangle is $\\frac{2}{9}$, so:\n"
        "$$ P(A) = 2 \\cdot \\frac{2}{9} = \\frac{4}{9} = 0.44444. $$\n\n"
        "**2. $P(B)$**: The complement of $B$ (both numbers $\\leq 1/4$) has an area of $\\frac{1}{16}$, so:\n"
        "$$ P(B) = 1 - \\frac{1}{16} = \\frac{15}{16} = 0.9375. $$\n\n"
        "**3. $P(A \\cap B)$**: Event $A$ is a subset of $B$, so:\n"
        "$$ P(A \\cap B) = P(A) = \\frac{4}{9} = 0.44444. $$\n\n"
        "**4. $P(C)$**: Event $C$ corresponds to a line ($x + y = 1$), which has zero area:\n"
        "$$ P(C) = 0. $$\n\n"
        "**5. $P(D)$**: Event $D$ corresponds to $x > 1/4$, forming a rectangle of area:\n"
        "$$ P(D) = \\frac{3}{4} = 0.75. $$\n\n"
        "**6. $P(A \\cap D)$**: This intersection involves triangular regions restricted to $x > 1/4$, with total area:\n"
        "$$ P(A \\cap D) = \\frac{89}{288} = 0.30903. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_2_set_operations_question_1 = {
    'question': (
        "Consider the following events:\n"
        "- $A$, $B$, and $C$ are subsets of a sample space.\n"
        "- $B^c$ and $C^c$ represent the complements of $B$ and $C$, respectively.\n\n"
        "The events $A$, $B$, and $C$ are disjoint events, and $P(A) = \\frac{2}{5}$. Find $P(A \\cup (B^c \\cup C^c)^c)$."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(A \\cup (B^c \\cup C^c)^c) = 0.4$",
    'explanation': (
        "1. Using De Morgan's law, $(B^c \\cup C^c)^c = B \\cap C$, so the expression simplifies to:\n"
        "$$ P(A \\cup (B^c \\cup C^c)^c) = P(A \\cup \\emptyset) = P(A). $$\n"
        "2. Since $P(A) = \\frac{2}{5}$:\n"
        "$$ P(A \\cup (B^c \\cup C^c)^c) = \\frac{2}{5} = 0.4. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_2_set_operations_question_2 = {
    'question': (
        "Consider the following events:\n"
        "- $A$, $B$, and $C$ are subsets of a sample space.\n"
        "- $B^c$ and $C^c$ represent the complements of $B$ and $C$, respectively.\n\n"
        "The events $A$ and $C$ are disjoint, $P(A) = \\frac{1}{2}$, and $P(B \\cap C) = \\frac{1}{4}$. Find $P(A \\cup (B^c \\cup C^c)^c)$."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(A \\cup (B^c \\cup C^c)^c) = 0.75$",
    'explanation': (
        "1. Using De Morgan's law again, $(B^c \\cup C^c)^c = B \\cap C$. The union simplifies to:\n"
        "$$ P(A \\cup (B^c \\cup C^c)^c) = P(A \\cup (B \\cap C)). $$\n"
        "2. Since $A$ and $B \\cap C$ are disjoint, we use the additivity axiom for disjoint events:\n"
        "$$ P(A \\cup (B^c \\cup C^c)^c) = P(A) + P(B \\cap C). $$\n"
        "3. Substituting the given values:\n"
        "$$ P(A) = \\frac{1}{2}, \\quad P(B \\cap C) = \\frac{1}{4}. $$\n"
        "Thus:\n"
        "$$ P(A \\cup (B^c \\cup C^c)^c) = \\frac{1}{2} + \\frac{1}{4} = \\frac{3}{4} = 0.75. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_2_set_operations_question_3 = {
    'question': (
        "Consider the following events:\n"
        "- $A$, $B$, and $C$ are subsets of a sample space.\n"
        "- $B^c$ and $C^c$ represent the complements of $B$ and $C$, respectively.\n\n"
        "We are given $P(A^c \\cap (B^c \\cup C^c)^c) = 0.7$. Find $P(A \\cup (B^c \\cup C^c)^c)$."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(A \\cup (B^c \\cup C^c)^c) = 0.3$",
    'explanation': (
        "1. De Morgan's law implies:\n"
        "$$ A^c \\cap (B^c \\cup C^c)^c = (A \\cup (B^c \\cup C^c)^c)^c. $$\n"
        "2. Using the complement rule:\n"
        "$$ P(A \\cup (B^c \\cup C^c)^c) = 1 - P(A^c \\cap (B^c \\cup C^c)^c). $$\n"
        "3. Substituting $P(A^c \\cap (B^c \\cup C^c)^c) = 0.7$:\n"
        "$$ P(A \\cup (B^c \\cup C^c)^c) = 1 - 0.7 = 0.3. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_3_three_tosses_question_1 = {
    'question': (
        "You flip a fair coin (i.e., the probability of obtaining Heads is $\\frac{1}{2}$) three times. "
        "Assume that all sequences of coin flip results, of length 3, are equally likely. Determine the probability of the event:\n\n"
        "1. The sequence $\\{HHH\\}$: 3 Heads."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(\\{HHH\\}) = 0.125$",
    'explanation': (
        "1. Since all outcomes are equally likely, we use a discrete uniform probability law. The probability of any particular sequence is "
        "$\\frac{1}{8}$, as there are $2^3 = 8$ total possible sequences of three coin flips.\n"
        "2. For the sequence $\\{HHH\\}$, this event consists of a single sequence. Thus:\n"
        "$$ P(\\{HHH\\}) = \\frac{1}{8}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_3_three_tosses_question_2 = {
    'question': (
        "You flip a fair coin (i.e., the probability of obtaining Heads is $\\frac{1}{2}$) three times. "
        "Assume that all sequences of coin flip results, of length 3, are equally likely. Determine the probability of the event:\n\n"
        "2. The sequence $\\{HTH\\}$: Heads, Tails, Heads."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(\\{HTH\\}) = 0.125$",
    'explanation': (
        "1. Similar to Question 1, the sequence $\\{HTH\\}$ is a specific outcome in the sample space. As there are $8$ total outcomes and this event consists of exactly one sequence:\n"
        "$$ P(\\{HTH\\}) = \\frac{1}{8}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_3_three_tosses_question_3 = {
    'question': (
        "You flip a fair coin (i.e., the probability of obtaining Heads is $\\frac{1}{2}$) three times. "
        "Assume that all sequences of coin flip results, of length 3, are equally likely. Determine the probability of the event:\n\n"
        "3. Any sequence with 2 Heads and 1 Tail (in any order)."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(\\{\\text{2 Heads, 1 Tail}\\}) = 0.375$",
    'explanation': (
        "1. The event of interest is $\\{HHT, HTH, THH\\}$. This consists of $3$ sequences in the sample space.\n"
        "2. Since there are $8$ total sequences, the probability is:\n"
        "$$ P(\\{\\text{2 Heads, 1 Tail}\\}) = \\frac{3}{8}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_3_three_tosses_question_4 = {
    'question': (
        "You flip a fair coin (i.e., the probability of obtaining Heads is $\\frac{1}{2}$) three times. "
        "Assume that all sequences of coin flip results, of length 3, are equally likely. Determine the probability of the event:\n\n"
        "4. Any sequence in which the number of Heads is greater than or equal to the number of Tails."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(\\{\\text{Heads} \\geq \\text{Tails}\\}) = 0.5$",
    'explanation': (
        "1. The set of sequences in which the number of Heads is greater than or equal to the number of Tails is:\n"
        "$$ \\{HHH, HHT, HTH, THH\\}. $$\n"
        "This consists of $4$ sequences in the sample space.\n"
        "2. The probability is:\n"
        "$$ P(\\{\\text{Heads} \\geq \\text{Tails}\\}) = \\frac{4}{8} = \\frac{1}{2}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_6_upper_lower_bounds_question_1 = {
    'question': (
        "Given two events $A$ and $B$ with $P(A) = \\frac{3}{4}$ and $P(B) = \\frac{1}{3}$, determine the smallest possible value of $P(A \\cap B)$."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$a = \\frac{1}{12}$",
    'explanation': (
        "1. Recall that $P(A \\cap B)$ obeys the inequality:\n"
        "$$ P(A \\cap B) \\geq P(A) + P(B) - P(A \\cup B). $$\n\n"
        "2. For the lower bound, note that $P(A \\cup B) \\leq 1$, since the probability of any event cannot exceed 1. Hence:\n"
        "$$ P(A \\cap B) \\geq P(A) + P(B) - 1 = \\frac{3}{4} + \\frac{1}{3} - 1 = \\frac{1}{12}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

problem_6_upper_lower_bounds_question_2 = {
    'question': (
        "Given two events $A$ and $B$ with $P(A) = \\frac{3}{4}$ and $P(B) = \\frac{1}{3}$, determine the largest possible value of $P(A \\cap B)$."
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$b = \\frac{1}{3}$",
    'explanation': (
        "1. For the upper bound, use the fact that $A \\cap B \\subseteq A$ and $A \\cap B \\subseteq B$. Thus:\n"
        "$$ P(A \\cap B) \\leq \\min(P(A), P(B)). $$\n\n"
        "2. Since $\\min(P(A), P(B)) = \\frac{1}{3}$:\n"
        "$$ P(A \\cap B) \\leq \\frac{1}{3}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

independence_question_1 = {
    'question': (
        "For each of the following statements about events $A$, $B$, and $C$ defined on a common sample space, determine whether it is true or false.\n\n"
        "Suppose that $A$, $B$, and $C$ are pairwise independent. Then, $A \\cap C$ is independent of $B$."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': "False",
    'explanation': (
        "1. Consider tossing a fair coin twice:\n"
        "- Let $A$ be the event that the first toss is Heads.\n"
        "- Let $B$ be the event that the second toss is Heads.\n"
        "- Let $C$ be the event that both the first and second tosses are different.\n\n"
        "2. It is easy to check that $A$, $B$, and $C$ are pairwise independent. However:\n"
        "$$ P(A \\cap B \\cap C) \\neq P(A \\cap C)P(B). $$\n\n"
        "3. Therefore, the statement is **False**."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

independence_question_2 = {
    'question': (
        "For each of the following statements about events $A$, $B$, and $C$ defined on a common sample space, determine whether it is true or false.\n\n"
        "Suppose that $A$, $B$, and $C$ are pairwise independent. Then, $A$, $B$, and $C$ are independent."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': "False",
    'explanation': (
        "1. Consider the same coin-tossing example:\n"
        "- $P(A) = P(B) = P(C) = \\frac{1}{2}$.\n"
        "- $P(A \\cap B \\cap C) = 0$, whereas $P(A)P(B)P(C) = \\frac{1}{8}$.\n\n"
        "2. Thus, pairwise independence does not imply independence among all three events.\n\n"
        "3. The statement is **False**."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

independence_question_3 = {
    'question': (
        "For each of the following statements about events $A$, $B$, and $C$ defined on a common sample space, determine whether it is true or false.\n\n"
        "Suppose that $A$, $B$, and $C$ are independent events; then $A^c$ and $B \\cup C^c$ are independent."
    ),
    'options_list': ['True', 'False'],
    'correct_answer': "True",
    'explanation': (
        "1. This follows from the intuitive meaning of event independence: when $A$, $B$, and $C$ are independent, "
        "the occurrence or non-occurrence of some of these events does not provide any information on the occurrence or non-occurrence of the remaining ones.\n\n"
        "2. The formal proof is omitted but the result holds.\n\n"
        "3. The statement is **True**."
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

drawing_balls_question_1 = {
    'question': (
        "An urn contains 5 blue balls, 6 red balls, and 7 black balls. Two balls are randomly drawn without replacement.\n\n"
        "What is the probability they are both blue?"
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(\\text{both blue}) = \\frac{10}{153}$",
    'explanation': (
        "1. The probability the first ball is blue is $\\frac{5}{18}$.\n"
        "2. Given the first ball is blue, the probability the second ball is blue is $\\frac{4}{17}$.\n"
        "3. Thus:\n"
        "$$ P(\\text{both blue}) = \\frac{5}{18} \\cdot \\frac{4}{17} = \\frac{20}{306} = \\frac{10}{153}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

drawing_balls_question_2 = {
    'question': (
        "An urn contains 5 blue balls, 6 red balls, and 7 black balls. Two balls are randomly drawn without replacement.\n\n"
        "What is the probability they have different colors?"
    ),
    'options_list': ['Do the Math'],
    'correct_answer': "$P(\\text{different colors}) = \\frac{107}{153}$",
    'explanation': (
        "1. Let $p_A$, $p_B$, and $p_C$ represent the probabilities the two balls are both blue, both red, and both black, respectively:\n"
        "- $p_A = \\frac{10}{153}$ (calculated in Question 1).\n"
        "- $p_B = \\frac{6}{18} \\cdot \\frac{5}{17} = \\frac{30}{306} = \\frac{10}{102}$.\n"
        "- $p_C = \\frac{7}{18} \\cdot \\frac{6}{17} = \\frac{42}{306} = \\frac{14}{102}$.\n\n"
        "2. The probability of different colors is:\n"
        "$$ 1 - p_A - p_B - p_C = 1 - \\frac{10}{153} - \\frac{30}{306} - \\frac{42}{306} = \\frac{107}{153}. $$"
    ),
    'chapter_information': 'MITx 6.431x Probability - The Science of Uncertainty and Data'
}

set_theory_question_1 = {
    'question': (
        "Let $A = \\{1, 3, 5\\}$ and $B = \\{3, 4, 5\\}$. What is $A \\cap B$?"
    ),
    'options_list': [
        "$\\{1, 3, 5\\}$",
        "$\\{3, 5\\}$",
        "$\\{1, 4\\}$",
        "$\\emptyset$"
    ],
    'correct_answer': "$\\{3, 5\\}$",
    'explanation': (
        "The intersection of $A$ and $B$ includes elements that are in both sets. "
        "$A \\cap B = \\{3, 5\\}$."
    ),
    'chapter_information': 'Set Theory: Key Concepts and Questions'
}

set_theory_question_2 = {
    'question': (
        "If $X = \\{1, 2, 3, 4\\}$ and $Y = \\{3, 4, 5, 6\\}$, what is $X \\cup Y$?"
    ),
    'options_list': [
        "$\\{1, 2, 3, 4\\}$",
        "$\\{3, 4\\}$",
        "$\\{1, 2, 3, 4, 5, 6\\}$",
        "$\\{5, 6\\}$"
    ],
    'correct_answer': "$\\{1, 2, 3, 4, 5, 6\\}$",
    'explanation': (
        "The union of $X$ and $Y$ includes all elements that are in either set. "
        "$X \\cup Y = \\{1, 2, 3, 4, 5, 6\\}$."
    ),
    'chapter_information': 'Set Theory: Key Concepts and Questions'
}

set_theory_question_3 = {
    'question': (
        "If $A = \\{a, b, c\\}$ and $B = \\{c, d, e\\}$, what is $A - B$?"
    ),
    'options_list': [
        "$\\{a, b, c, d, e\\}$",
        "$\\{a, b\\}$",
        "$\\{c\\}$",
        "$\\emptyset$"
    ],
    'correct_answer': "$\\{a, b\\}$",
    'explanation': (
        "The set difference $A - B$ includes all elements in $A$ that are not in $B$. "
        "$A - B = \\{a, b\\}$."
    ),
    'chapter_information': 'Set Theory: Key Concepts and Questions'
}

set_theory_question_4 = {
    'question': (
        "Which of the following statements is **true** according to DeMorgan's Laws?"
    ),
    'options_list': [
        "$(A \\cup B)^c = A^c \\cap B^c$",
        "$(A \\cup B)^c = A^c \\cup B^c$",
        "$(A \\cap B)^c = A^c \\cap B^c$",
        "$(A \\cap B)^c = A^c \\cup B$"
    ],
    'correct_answer': "$(A \\cup B)^c = A^c \\cap B^c$",
    'explanation': (
        "DeMorgan's Laws state that the complement of a union is the intersection of the complements: "
        "$(A \\cup B)^c = A^c \\cap B^c$."
    ),
    'chapter_information': 'Set Theory: Key Concepts and Questions'
}

set_theory_question_5 = {
    'question': (
        "If $U = \\{1, 2, 3, 4, 5\\}$, $A = \\{1, 2, 3\\}$, and $B = \\{3, 4, 5\\}$, what is $A \\Delta B$?"
    ),
    'options_list': [
        "$\\{1, 2, 3\\}$",
        "$\\{3\\}$",
        "$\\{1, 2, 4, 5\\}$",
        "$\\{4, 5\\}$"
    ],
    'correct_answer': "$\\{1, 2, 4, 5\\}$",
    'explanation': (
        "The symmetric difference $A \\Delta B$ includes elements in $A$ or $B$ but not in both: "
        "$A \\Delta B = \\{1, 2, 4, 5\\}$."
    ),
    'chapter_information': 'Set Theory: Key Concepts and Questions'
}

proba1bility_question_1 = {
    'question': (
        "For each of the following scenarios, find the requested probability. Assume the sets $A$, $B$, and $C$ are events from the same sample space $S$.\n\n"
        "If $P(A) = 0.4$, $P(B^c) = 0.7$, and $P(A \\cap B^c) = 0.2$, find $P(A \\cap B)$."
    ),
    'options_list': ["$0.2$", "$0.3$", "$0.4$", "$0.5$"],
    'correct_answer': "$0.2$",
    'explanation': (
        "Using the complement rule, $P(B) = 1 - P(B^c) = 1 - 0.7 = 0.3$. "
        "Since $P(A \\cap B^c) = 0.2$, we use the relationship $P(A) = P(A \\cap B) + P(A \\cap B^c)$. "
        "Substituting the known values:\n"
        "$$ 0.4 = P(A \\cap B) + 0.2, $$\n"
        "$$ P(A \\cap B) = 0.2. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

prob1ability_question_2 = {
    'question': (
        "For each of the following scenarios, find the requested probability. Assume the sets $A$, $B$, and $C$ are events from the same sample space $S$.\n\n"
        "If $P(A) = 0.9$ and $P(B) = 0.9$, what is the lower bound for $P(A \\cup B)$?"
    ),
    'options_list': ["$0.8$", "$0.9$", "$1.0$", "$0.81$"],
    'correct_answer': "$0.9$",
    'explanation': (
        "Using the formula for the union of probabilities, $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$. "
        "To find the lower bound, assume $P(A \\cap B) = 0$. Therefore:\n"
        "$$ P(A \\cup B) = 0.9 + 0.9 - 0 = 0.9. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

probabi1lity_question_3 = {
    'question': (
        "Three popular options on a certain type of car are $A$ (leather seats), $B$ (a sunroof), and $C$ (heated seats). "
        "In the past, $P(A) = 0.55$, $P(B) = 0.45$, $P(C) = 0.4$. Furthermore, $P(A \\cap B) = 0.25$, $P(A \\cap C) = 0.2$, "
        "$P(B \\cap C) = 0.15$, and $P(A \\cap B \\cap C) = 0.1$.\n\n"
        "Find the probability that a customer will ask for at least one of the three options."
    ),
    'options_list': ["$0.8$", "$0.85$", "$0.9$", "$0.95$"],
    'correct_answer': "$0.9$",
    'explanation': (
        "Using the inclusion-exclusion principle:\n"
        "$$ P(A \\cup B \\cup C) = P(A) + P(B) + P(C) - P(A \\cap B) - P(A \\cap C) - P(B \\cap C) + P(A \\cap B \\cap C). $$\n"
        "Substitute the values:\n"
        "$$ P(A \\cup B \\cup C) = 0.55 + 0.45 + 0.4 - 0.25 - 0.2 - 0.15 + 0.1 = 0.9. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

pro1bability_question_4 = {
    'question': (
        "Three popular options on a certain type of car are $A$ (leather seats), $B$ (a sunroof), and $C$ (heated seats). "
        "In the past, $P(A) = 0.55$, $P(B) = 0.45$, $P(C) = 0.4$. Furthermore, $P(A \\cap B) = 0.25$, $P(A \\cap C) = 0.2$, "
        "$P(B \\cap C) = 0.15$, and $P(A \\cap B \\cap C) = 0.1$.\n\n"
        "Find the probability that a customer will not ask for any of these three options."
    ),
    'options_list': ["$0.1$", "$0.15$", "$0.2$", "$0.25$"],
    'correct_answer': "$0.1$",
    'explanation': (
        "The probability of 'not asking for any of the three options' is the complement of asking for at least one. Thus:\n"
        "$$ P(\\text{none}) = 1 - P(A \\cup B \\cup C). $$\n"
        "From the previous question, $P(A \\cup B \\cup C) = 0.9$. Therefore:\n"
        "$$ P(\\text{none}) = 1 - 0.9 = 0.1. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

probabili1ty_quest2ion_5 = {
    'question': (
        "Three popular options on a certain type of car are $A$ (leather seats), $B$ (a sunroof), and $C$ (heated seats). "
        "In the past, $P(A) = 0.55$, $P(B) = 0.45$, $P(C) = 0.4$. Furthermore, $P(A \\cap B) = 0.25$, $P(A \\cap C) = 0.2$, "
        "$P(B \\cap C) = 0.15$, and $P(A \\cap B \\cap C) = 0.1$.\n\n"
        "Find the probability that a customer will ask for heated leather seats but not a sunroof."
    ),
    'options_list': ["$0.1$", "$0.15$", "$0.2$", "$0.25$"],
    'correct_answer': "$0.1$",
    'explanation': (
        "The event 'heated leather seats but not a sunroof' corresponds to $A \\cap C \\cap B^c$. "
        "Using the inclusion-exclusion principle:\n"
        "$$ P(A \\cap C \\cap B^c) = P(A \\cap C) - P(A \\cap B \\cap C). $$\n"
        "Substitute the values:\n"
        "$$ P(A \\cap C \\cap B^c) = 0.2 - 0.1 = 0.1. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

probab1ility_quest2ion_6 = {
    'question': (
        "Three popular options on a certain type of car are $A$ (leather seats), $B$ (a sunroof), and $C$ (heated seats). "
        "In the past, $P(A) = 0.55$, $P(B) = 0.45$, $P(C) = 0.4$. Furthermore, $P(A \\cap B) = 0.25$, $P(A \\cap C) = 0.2$, "
        "$P(B \\cap C) = 0.15$, and $P(A \\cap B \\cap C) = 0.1$.\n\n"
        "Find the probability that a customer will ask for at most two of the options."
    ),
    'options_list': ["$0.7$", "$0.8$", "$0.9$", "$1.0$"],
    'correct_answer': "$0.9$",
    'explanation': (
        "The event 'at most two of the options' is the complement of 'all three options'.\n"
        "$$ P(\\text{at most two}) = 1 - P(A \\cap B \\cap C). $$\n"
        "From the given values:\n"
        "$$ P(\\text{at most two}) = 1 - 0.1 = 0.9. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}


probability_que2stion_7 = {
    'question': (
        "Three popular options on a certain type of car are $A$ (leather seats), $B$ (a sunroof), and $C$ (heated seats). "
        "In the past, $P(A) = 0.55$, $P(B) = 0.45$, $P(C) = 0.4$. Furthermore, $P(A \\cap B) = 0.25$, $P(A \\cap C) = 0.2$, "
        "$P(B \\cap C) = 0.15$, and $P(A \\cap B \\cap C) = 0.1$.\n\n"
        "Find the probability that a customer will ask for exactly two of the options."
    ),
    'options_list': ["$0.2$", "$0.25$", "$0.3$", "$0.35$"],
    'correct_answer': "$0.3$",
    'explanation': (
        "The event 'exactly two options' corresponds to the union of events where two options are chosen, excluding the overlap with all three options. "
        "Using the inclusion-exclusion principle:\n"
        "$$ P(\\text{exactly two}) = P(A \\cap B) + P(A \\cap C) + P(B \\cap C) - 3 \\cdot P(A \\cap B \\cap C). $$\n"
        "Substituting the values:\n"
        "$$ P(\\text{exactly two}) = 0.25 + 0.2 + 0.15 - 3 \\cdot 0.1 = 0.3. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

probability_quest2ion_8 = {
    'question': (
        "A message of length 5 digits is to be sent. Each digit can be a $0$, $1$, or $2$.\n\n"
        "What is the cardinality of the sample space?"
    ),
    'options_list': ["$243$", "$125$", "$81$", "$729$"],
    'correct_answer': "$243$",
    'explanation': (
        "Each digit can take 3 possible values ($0$, $1$, or $2$), and the message contains 5 digits. Thus, the total number of possible messages is:\n"
        "$$ 3^5 = 243. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

probability_qu2estion_9 = {
    'question': (
        "A message of length 5 digits is to be sent. Each digit can be a $0$, $1$, or $2$.\n\n"
        "If every message is equally likely, what is the probability that the message consists of 2 zeros, 2 ones, and 1 two? "
        "Round your answer to four decimal places."
    ),
    'options_list': ["$0.1235$", "$0.2345$", "$0.0982$", "$0.1124$"],
    'correct_answer': "$0.1235$",
    'explanation': (
        "The total number of possible messages is $243$, as calculated earlier. The number of favorable outcomes is given by the multinomial coefficient:\n"
        "$$ \\binom{5}{2, 2, 1} = \\frac{5!}{2! \\cdot 2! \\cdot 1!} = 30. $$\n"
        "Thus, the probability is:\n"
        "$$ P = \\frac{30}{243} \\approx 0.1235. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

probability_quest2ion_10 = {
    'question': (
        "A message of length 5 digits is to be sent. Each digit can be a $0$, $1$, or $2$.\n\n"
        "What is the probability that the message contains at least one zero? Round your answer to three decimal places."
    ),
    'options_list': ["$0.756$", "$0.868$", "$0.943$", "$0.652$"],
    'correct_answer': "$0.868$",
    'explanation': (
        "The complement of 'at least one zero' is 'no zeros at all.' The number of messages with no zeros is:\n"
        "$$ 2^5 = 32. $$\n"
        "The total number of messages is $243$. Therefore, the probability of 'no zeros' is:\n"
        "$$ P(\\text{no zeros}) = \\frac{32}{243}. $$\n"
        "The probability of 'at least one zero' is:\n"
        "$$ P(\\text{at least one zero}) = 1 - P(\\text{no zeros}) = 1 - \\frac{32}{243} \\approx 0.868. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}


grocery_store_question_1 = {
    'question': (
        "Suppose we are interested in the buying habits of shoppers at a particular grocery store with regards to whether they purchase apples, milk, and/or bread. "
        "Now suppose 30\\% of all shoppers at this particular grocery store buy apples, 45\\% buy milk, and 40\\% buy a loaf of bread. "
        "Let $A$ be the event that a randomly selected shopper buys apples, $B$ be the event that the same randomly selected shopper buys milk, "
        "and $C$ the event that they buy bread. Suppose we also know (from data collected) the following information:\n\n"
        "- The probability that the shopper buys apples and milk is $P(A \\cap B) = 0.20$.\n"
        "- The probability that the shopper buys milk and bread is $P(B \\cap C) = 0.25$.\n"
        "- The probability that the shopper buys apples and bread is $P(A \\cap C) = 0.12$.\n"
        "- The probability that the shopper buys all three items is $P(A \\cap B \\cap C) = 0.07$.\n\n"
        "What is the probability that the shopper purchases at least one of the three items?"
    ),
    'options_list': ["$0.50$", "$0.65$", "$0.72$", "$0.85$"],
    'correct_answer': "$0.65$",
    'explanation': (
        "The probability of purchasing at least one item is calculated using the inclusion-exclusion principle:\n"
        "$$ P(A \\cup B \\cup C) = P(A) + P(B) + P(C) - [P(A \\cap B) + P(B \\cap C) + P(A \\cap C)] + P(A \\cap B \\cap C). $$\n"
        "Substituting the given probabilities:\n"
        "$$ P(A \\cup B \\cup C) = 0.30 + 0.45 + 0.40 - [0.20 + 0.25 + 0.12] + 0.07 = 0.65. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

grocery_store_question_2 = {
    'question': (
        "Suppose we are interested in the buying habits of shoppers at a particular grocery store with regards to whether they purchase apples, milk, and/or bread. "
        "Now suppose 30\\% of all shoppers at this particular grocery store buy apples, 45\\% buy milk, and 40\\% buy a loaf of bread. "
        "Let $A$ be the event that a randomly selected shopper buys apples, $B$ be the event that the same randomly selected shopper buys milk, "
        "and $C$ the event that they buy bread. Suppose we also know (from data collected) the following information:\n\n"
        "- The probability that the shopper buys apples and milk is $P(A \\cap B) = 0.20$.\n"
        "- The probability that the shopper buys milk and bread is $P(B \\cap C) = 0.25$.\n"
        "- The probability that the shopper buys apples and bread is $P(A \\cap C) = 0.12$.\n"
        "- The probability that the shopper buys all three items is $P(A \\cap B \\cap C) = 0.07$.\n\n"
        "What is the probability that the shopper purchases none of the three items?"
    ),
    'options_list': ["$0.25$", "$0.35$", "$0.50$", "$0.65$"],
    'correct_answer': "$0.35$",
    'explanation': (
        "The probability of purchasing none of the three items is the complement of the probability of purchasing at least one:\n"
        "$$ P(\\text{none}) = 1 - P(A \\cup B \\cup C). $$\n"
        "Substituting the calculated value of $P(A \\cup B \\cup C)$:\n"
        "$$ P(\\text{none}) = 1 - 0.65 = 0.35. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

grocery_store_question_3 = {
    'question': (
        "Suppose we are interested in the buying habits of shoppers at a particular grocery store with regards to whether they purchase apples, milk, and/or bread. "
        "Now suppose 30\\% of all shoppers at this particular grocery store buy apples, 45\\% buy milk, and 40\\% buy a loaf of bread. "
        "Let $A$ be the event that a randomly selected shopper buys apples, $B$ be the event that the same randomly selected shopper buys milk, "
        "and $C$ the event that they buy bread. Suppose we also know (from data collected) the following information:\n\n"
        "- The probability that the shopper buys apples and milk is $P(A \\cap B) = 0.20$.\n"
        "- The probability that the shopper buys milk and bread is $P(B \\cap C) = 0.25$.\n"
        "- The probability that the shopper buys apples and bread is $P(A \\cap C) = 0.12$.\n"
        "- The probability that the shopper buys all three items is $P(A \\cap B \\cap C) = 0.07$.\n\n"
        "What is the probability that the shopper buys milk and bread but not apples?"
    ),
    'options_list': ["$0.10$", "$0.15$", "$0.18$", "$0.25$"],
    'correct_answer': "$0.18$",
    'explanation': (
        "The probability of buying milk and bread but not apples is:\n"
        "$$ P(B \\cap C \\cap A^c) = P(B \\cap C) - P(A \\cap B \\cap C). $$\n"
        "Substituting the given probabilities:\n"
        "$$ P(B \\cap C \\cap A^c) = 0.25 - 0.07 = 0.18. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

multiple_choice_test_question_1 = {
    'question': (
        "A student takes a multiple-choice test with $20$ questions. Each question has 5 possible answers, only one of which is correct. "
        "How many ways can the test be completed? (Find the cardinality of the sample space.)"
    ),
    'options_list': ["$10^{12}$", "$5^{20}$", "$20!$", "$10^{10}$"],
    'correct_answer': "$5^{20}$",
    'explanation': (
        "Each of the $20$ questions has $5$ possible answers. Therefore, the total number of ways the test can be completed is:\n"
        "$$ 5^{20} = 9.536743 \\times 10^{13}. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

multiple_choice_test_question_2 = {
    'question': (
        "A student takes a multiple-choice test with $20$ questions. Each question has 5 possible answers, only one of which is correct. "
        "If a student answers each question at random, what is the probability that they will answer at least $14$ questions correctly? "
        "Round your answer to seven decimal places."
    ),
    'options_list': ["$0.000018$", "$0.0000018$", "$0.000001$", "$0.000002$"],
    'correct_answer': "$0.0000018$",
    'explanation': (
        "This is a binomial probability problem where:\n"
        "- $n = 20$ (number of questions),\n"
        "- $p = 0.2$ (probability of answering a question correctly),\n"
        "- $q = 1 - p = 0.8$ (probability of answering a question incorrectly).\n\n"
        "The probability of answering at least $14$ questions correctly is:\n"
        "$$ P(X \\geq 14) = \\sum_{i=14}^{20} \\binom{20}{i} p^i (1-p)^{20-i}. $$\n\n"
        "Using a loop or binomial expansion, we find:\n"
        "$$ P(X \\geq 14) \\approx 0.0000018. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

multiple_choice_test_question_3 = {
    'question': (
        "A student takes a multiple-choice test with $20$ questions. Each question has 5 possible answers, only one of which is correct. "
        "If the student knows the answer to each question with probability $0.9$, what is the probability that they will answer at least $14$ questions correctly? "
        "Round your answer to four decimal places."
    ),
    'options_list': ["$0.9000$", "$0.9976$", "$0.9990$", "$0.9985$"],
    'correct_answer': "$0.9976$",
    'explanation': (
        "This is another binomial probability problem where:\n"
        "- $n = 20$ (number of questions),\n"
        "- $p = 0.9$ (probability of answering a question correctly),\n"
        "- $q = 1 - p = 0.1$ (probability of answering a question incorrectly).\n\n"
        "The probability of answering at least $14$ questions correctly is:\n"
        "$$ P(X \\geq 14) = \\sum_{i=14}^{20} \\binom{20}{i} p^i (1-p)^{20-i}. $$\n\n"
        "Substituting the values and summing the probabilities:\n"
        "$$ P(X \\geq 14) \\approx 0.9976. $$"
    ),
    'chapter_information': 'https://www.coursera.org/learn/probability-theory-foundation-for-data-science'
}

problem_1_probability_with_dice_question_a = {
    'question': (
        "You roll three fair six-sided dice. What is the probability that the same number appears on exactly two of the three dice?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "$6 \\cdot \\binom{3}{2} \\cdot \\left(\\frac{1}{6}\\right)^2 \\cdot \\left(\\frac{5}{6}\\right)$"
    ),
    'explanation': (
        "Let $X$ represent the number of times a specific number appears. Since $X \\sim \\text{Bin}(3, \\frac{1}{6})$, "
        "the probability of a specific number appearing exactly twice is: "
        "$P(X = 2) = \\binom{3}{2} \\cdot \\left(\\frac{1}{6}\\right)^2 \\cdot \\left(\\frac{5}{6}\\right).$ "
        "Since there are six possible numbers, multiply by 6."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_2_probability_correct_matches_question_a = {
    'question': (
        "Suppose you have 5 index cards, each labeled with a unique name, and 5 matching envelopes. "
        "You randomly place each card into an envelope. What is the probability that at least one card is placed in the correct envelope?"
    ),
    'options_list': ['Use Complement Rule'],
    'correct_answer': (
        "$P(\\text{at least one match}) = 1 - P(\\text{no matches})$"
    ),
    'explanation': (
        "The probability of no matches is given by the derangement formula: "
        "$P(\\text{no matches}) = 1 - \\frac{1}{1!} + \\frac{1}{2!} - \\frac{1}{3!} + \\frac{1}{4!} - \\frac{1}{5!}$. "
        "Thus, $P(\\text{at least one match}) = 1 - P(\\text{no matches})$."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_3_set_operations_question = {
    'question': (
        "Given the intervals $U = [0,2]$, $A = [0.5,1]$, and $B = [0.5,1.5]$, find the following: "
        "(a) $\\bar{A}$, (b) $A \\cup B$, and (c) $A \\cap B$."
    ),
    'options_list': ['Find Intervals'],
    'correct_answer': (
        "$\\bar{A} = [0,0.5) \\cup (1,2]$, $A \\cup B = [0.5,1.5]$, $A \\cap B = [0.5,1]$"
    ),
    'explanation': (
        "- The complement of $A$ is everything in $U$ that is not in $A$. "
        "- The union $A \\cup B$ includes all points in either $A$ or $B$. "
        "- The intersection $A \\cap B$ includes points in both $A$ and $B$."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_6_probability_with_coins_question_a = {
    'question': (
        "Suppose you flip three fair coins. What is the probability of getting exactly two heads?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "$P(X=2) = \\binom{3}{2} \\cdot \\left(\\frac{1}{2}\\right)^2 \\cdot \\left(\\frac{1}{2}\\right)$"
    ),
    'explanation': (
        "The probability of getting exactly two heads follows a binomial distribution: "
        "$X \\sim \\text{Bin}(3, 0.5)$ where $n=3$ and $p=0.5$. "
        "Thus, $P(X=2) = \\binom{3}{2} \\cdot \\left(\\frac{1}{2}\\right)^2 \\cdot \\left(\\frac{1}{2}\\right).$"
    ),
    'chapter_information': 'ISYE 6739'
}

problem_7_assigning_tasks_question_a = {
    'question': (
        "Suppose there are 6 tasks to assign to 4 workers, where each worker can take multiple tasks. "
        "How many ways can the tasks be assigned to workers?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "$4^6$"
    ),
    'explanation': (
        "Each of the 6 tasks has 4 possible assignments, so the total number of ways is $4^6$."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_8_drawing_balls_from_bag_question = {
    'question': (
        "A bag contains 4 red balls, 5 blue balls, and 6 green balls.\n"
        "(a) What is the probability of drawing 2 blue balls if you draw two balls without replacement?\n"
        "(b) What is the probability of drawing one red and one green ball without replacement?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $P(\\text{2 blue}) = \\frac{\\binom{5}{2}}{\\binom{15}{2}}$\n"
        "(b) $P(\\text{1 red, 1 green}) = \\frac{\\binom{4}{1} \\cdot \\binom{6}{1}}{\\binom{15}{2}}$"
    ),
    'explanation': (
        "(a) Use combinations: The number of ways to draw 2 blue balls is $\\binom{5}{2}$, and the total ways is $\\binom{15}{2}$.\n"
        "(b) Draw one red and one green: Multiply the ways to choose 1 red and 1 green, then divide by the total ways."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_9_probability_of_winning_contest_question = {
    'question': (
        "A contest has 10 participants, and 3 will win prizes (first, second, and third place, order matters).\n"
        "(a) How many ways can the prizes be distributed?\n"
        "(b) If you and two friends enter the contest, what is the probability that the three of you will win all the prizes?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $P(10,3) = \\frac{10!}{(10-3)!}$\n"
        "(b) $\\frac{3!}{\\frac{10!}{(10-3)!}}$"
    ),
    'explanation': (
        "(a) Use the permutation formula $P(n, r) = \\frac{n!}{(n-r)!}$.\n"
        "(b) Consider that only one specific permutation works if you and two friends win."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_10_forming_committees_question = {
    'question': (
        "A company has 12 employees and wants to form a 5-person committee.\n"
        "(a) How many different committees can be formed?\n"
        "(b) If the committee must include at least 2 women, and there are 4 women among the employees, how many different committees can be formed?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $\\binom{12}{5}$\n"
        "(b) $\\sum_{k=2}^{4} \\binom{4}{k} \\cdot \\binom{8}{5-k}$"
    ),
    'explanation': (
        "(a) The number of 5-person committees is $\\binom{12}{5}$.\n"
        "(b) Sum the cases where the committee has 2, 3, 4, or 5 women."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_11_probability_of_poker_hand_question = {
    'question': (
        "In a standard deck of 52 cards, you are dealt a 5-card hand.\n"
        "(a) What is the probability of getting a full house (3 cards of one rank and 2 cards of another rank)?\n"
        "(b) What is the probability of getting four of a kind?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $P(\\text{full house}) = \\frac{\\binom{13}{1} \\cdot \\binom{4}{3} \\cdot \\binom{12}{1} \\cdot \\binom{4}{2}}{\\binom{52}{5}}$\n"
        "(b) $P(\\text{four of a kind}) = \\frac{\\binom{13}{1} \\cdot \\binom{4}{4} \\cdot \\binom{48}{1}}{\\binom{52}{5}}$"
    ),
    'explanation': (
        "(a) Choose the rank for 3 cards, then 2 cards of a different rank, and divide by total hands.\n"
        "(b) Choose the rank for 4 cards and one more card from remaining cards."
    ),
    'chapter_information': 'ISYE 6739'
}

problem_12_probability_with_letters_question = {
    'question': (
        "Suppose you are forming a password using the English alphabet (26 letters). The password is 6 characters long.\n"
        "(a) How many passwords can be formed if there are no restrictions?\n"
        "(b) How many passwords can be formed if the first character must be a vowel?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $26^6$\n"
        "(b) $5 \\cdot 26^5$"
    ),
    'explanation': (
        "(a) There are 26 choices for each of the 6 characters.\n"
        "(b) If the first character is a vowel, there are 5 choices for the first character, and 26 for each of the remaining characters."
    ),
    'chapter_information': 'ISYE 6739'
}

question_1_die_thrown_eight_times = {
    'question': (
        "A die is thrown 8 times.\n"
        "(a) What is the probability that a '6' comes up at least once?\n"
        "(b) What is the probability that each face appears at least once in the 8 rolls?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $1 - \\left(\\frac{5}{6}\\right)^8$\n"
        "(b) $\\frac{6 \\cdot \\binom{8}{2} \\cdot 5!}{6^8}$"
    ),
    'explanation': (
        "(a) Use the complement rule: $1 - \\text{Pr(no 6’s appear)} = 1 - \\left(\\frac{5}{6}\\right)^8$\n"
        "(b) Assign two occurrences to one face using $\\binom{8}{2}$ and permute the other faces using $5!$. Multiply by 6 for all faces."
    ),
    'chapter_information': 'ISYE 6739'
}

question_2_selecting_items = {
    'question': (
        "You have 25 items, 15 are bad, and 10 are good. Suppose you choose 3 of these items randomly.\n"
        "(a) What is the probability that all 3 are bad?\n"
        "(b) What is the probability that at least one is good?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $\\frac{\\binom{15}{3}}{\\binom{25}{3}}$\n"
        "(b) $1 - \\frac{\\binom{15}{3}}{\\binom{25}{3}}$"
    ),
    'explanation': (
        "(a) Count the number of ways to choose 3 bad items out of 15 and divide by total combinations.\n"
        "(b) Use the complement rule: $1 - \\text{Pr(all 3 are bad)}$."
    ),
    'chapter_information': 'ISYE 6739'
}

question_3_gender_class_independence = {
    'question': (
        "In a class, there are 5 freshman boys, 4 freshman girls, 7 sophomore boys, and 5 sophomore girls. "
        "How many junior boys must be present to ensure that gender and class are independent when a student is selected at random?"
    ),
    'options_list': ['Solve'],
    'correct_answer': "Solve for $x$ in $\\frac{5}{21+x} = \\frac{12}{21+x} \\cdot \\frac{5}{21+x}$",
    'explanation': (
        "Use the independence condition: $\\text{Pr(B ∩ F)} = \\text{Pr(B)} \\cdot \\text{Pr(F)}$. "
        "Set proportions accordingly and solve for $x$."
    ),
    'chapter_information': 'ISYE 6739'
}

question_4_independent_events_probability = {
    'question': (
        "If $A$ and $B$ are independent, $\\text{Pr}(A) = 0.5$, and $\\text{Pr}(A \\cup B) = 0.75$, find $\\text{Pr}(B)$."
    ),
    'options_list': ['Solve'],
    'correct_answer': "Solve $0.75 = 0.5 + \\text{Pr}(B) - 0.5 \\cdot \\text{Pr}(B)$",
    'explanation': (
        "Use the inclusion-exclusion formula: $\\text{Pr}(A \\cup B) = \\text{Pr}(A) + \\text{Pr}(B) - \\text{Pr}(A) \\cdot \\text{Pr}(B)$. "
        "Plug in values and solve for $\\text{Pr}(B)$."
    ),
    'chapter_information': 'ISYE 6739'
}

question_5_bridge_hand_probability = {
    'question': (
        "A bridge hand contains 13 cards from a standard deck. Find the probability that the hand contains:\n"
        "(a) Exactly 3 queens\n"
        "(b) At least 2 queens\n"
        "(c) No queens"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $\\frac{\\binom{4}{3} \\cdot \\binom{48}{10}}{\\binom{52}{13}}$\n"
        "(b) $\\frac{\\sum_{i=2}^{4} \\binom{4}{i} \\cdot \\binom{48}{13-i}}{\\binom{52}{13}}$\n"
        "(c) $\\frac{\\binom{48}{13}}{\\binom{52}{13}}$"
    ),
    'explanation': (
        "(a) Count ways to choose 3 queens and 10 non-queens. Divide by total hands.\n"
        "(b) Use the complement rule or sum cases for 2, 3, or 4 queens.\n"
        "(c) Choose 13 cards from the 48 non-queens."
    ),
    'chapter_information': 'ISYE 6739'
}

question_1_conditional_probability_proof = {
    'question': (
        "Prove: If $\\Pr(A|B) > \\Pr(A)$, then $\\Pr(B|A) > \\Pr(B)$."
    ),
    'options_list': ['Show Proof'],
    'correct_answer': (
        "Starting with $\\Pr(A|B) > \\Pr(A)$:\n"
        "$\\frac{\\Pr(A \\cap B)}{\\Pr(B)} > \\Pr(A)$\n"
        "$\\Pr(A \\cap B) > \\Pr(A) \\cdot \\Pr(B)$\n"
        "Dividing by $\\Pr(A)$ gives:\n"
        "$\\Pr(B|A) = \\frac{\\Pr(A \\cap B)}{\\Pr(A)} > \\Pr(B)$"
    ),
    'explanation': (
        "Apply the definitions of conditional probability and rearrange the inequality to "
        "show $\\Pr(B|A) > \\Pr(B)$."
    ),
    'chapter_information': 'ISYE 6739'
}

question_2_joe_and_fred_basketball = {
    'question': (
        "Joe and Fred shoot baskets. The probability of scoring a basket is $p$. "
        "Joe shoots first. If he misses, Fred gets to shoot, and they alternate turns. "
        "What is the probability that Joe wins?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "$\\Pr(\\text{Joe wins}) = \\frac{p}{2 - p}$"
    ),
    'explanation': (
        "The probability that Joe wins is a geometric series:\n"
        "$\\Pr(\\text{Joe wins}) = p + (1 - p)^2 p + (1 - p)^4 p + \\cdots$\n"
        "Summing the series gives $\\frac{p}{2 - p}$."
    ),
    'chapter_information': 'ISYE 6739'
}

question_3_bayes_theorem_with_boxes = {
    'question': (
        "There are two boxes:\n"
        "- Box 1: 1 black marble, 1 white marble\n"
        "- Box 2: 2 black marbles, 1 white marble\n"
        "A box is selected at random, and a marble is drawn at random.\n"
        "(a) Find $\\Pr(\\text{the marble is black})$.\n"
        "(b) What is the probability that the marble came from Box 1 given that it is white?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $\\Pr(B) = \\frac{1}{2} \\cdot \\frac{1}{2} + \\frac{2}{3} \\cdot \\frac{1}{2} = \\frac{7}{12}$\n"
        "(b) $\\Pr(I|W) = \\frac{\\frac{1}{2} \\cdot \\frac{1}{2}}{\\frac{1}{2} \\cdot \\frac{1}{2} + \\frac{1}{3} \\cdot \\frac{1}{2}} = \\frac{3}{5}$"
    ),
    'explanation': (
        "(a) Use the law of total probability.\n"
        "(b) Use Bayes' Theorem: $\\Pr(I|W) = \\frac{\\Pr(W|I) \\Pr(I)}{\\Pr(W|I) \\Pr(I) + \\Pr(W|II) \\Pr(II)}$."
    ),
    'chapter_information': 'ISYE 6739'
}

question_4_gamblers_coin = {
    'question': (
        "A gambler has a fair coin and a two-headed coin. He selects one at random and flips it. "
        "It shows heads.\n"
        "(a) What is the probability that the coin is fair?\n"
        "(b) The gambler flips the same coin, and it shows heads again. What is the probability that the coin is fair?\n"
        "(c) The gambler flips the coin a third time, and it shows tails. What is the probability that the coin is fair?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $\\Pr(F|H) = \\frac{\\frac{1}{2} \\cdot \\frac{1}{2}}{\\frac{1}{2} \\cdot \\frac{1}{2} + 1 \\cdot \\frac{1}{2}} = \\frac{1}{3}$\n"
        "(b) $\\Pr(F|HH) = \\frac{\\frac{1}{4} \\cdot \\frac{1}{2}}{\\frac{1}{4} \\cdot \\frac{1}{2} + 1 \\cdot \\frac{1}{2}} = \\frac{1}{5}$\n"
        "(c) $\\Pr(F|HHT) = 1$"
    ),
    'explanation': (
        "(a) Use Bayes' Theorem: $\\Pr(F|H) = \\frac{\\Pr(H|F) \\Pr(F)}{\\Pr(H|F) \\Pr(F) + \\Pr(H|U) \\Pr(U)}$\n"
        "(b) Repeat Bayes' Theorem for two heads in a row.\n"
        "(c) If tails appears, the coin must be fair."
    ),
    'chapter_information': 'ISYE 6739'
}

strategic_practice_1_question_4a = {
    'question': (
        "For a group of 7 people, find the probability that all 4 seasons (winter, spring, summer, fall) occur at least once among their birthdays, assuming that all seasons are equally likely."
    ),
    'options_list': ['A) 0.413', 'B) 0.513', 'C) 0.613', 'D) 0.713'],
    'correct_answer': 'B) 0.513',
    'explanation': (
        "Using inclusion-exclusion, let $A_i$ be the event that there are no birthdays in the $i$-th season. "
        "The probability is given by:\n"
        "$P(A_1 \\cup A_2 \\cup A_3 \\cup A_4) = 4P(A_1) - 6P(A_1 \\cap A_2) + 4P(A_1 \\cap A_2 \\cap A_3)$, where:\n"
        "$P(A_1) = (3/4)^7$, $P(A_1 \\cap A_2) = 1/2^7$, and $P(A_1 \\cap A_2 \\cap A_3) = 1/4^7$.\n"
        "Thus, the probability is $1 - \\left(4 (3/4)^7 - 6 (1/2)^7 + 4 (1/4)^7\\right) \\approx 0.513$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice_1_question_4b = {
    'question': (
        "Alice attends a small college in which each class meets only once a week. There are 6 classes to choose from for each day, Monday through Friday. "
        "She registers for 7 randomly selected classes out of 30. What is the probability that she will have classes every day, Monday through Friday?"
    ),
    'options_list': ['A) 0.202', 'B) 0.302', 'C) 0.402', 'D) 0.502'],
    'correct_answer': 'B) 0.302',
    'explanation': (
        "Using combinatorics, we compute the probability as follows:\n"
        "- The total number of ways to select 7 classes from 30 is $\\binom{30}{7}$.\n"
        "- The favorable outcomes include possibilities where Alice has classes every day, calculated as:\n"
        "$\\binom{5}{2} \\cdot \\binom{6}{2} \\cdot 6^3 + \\binom{5}{1} \\cdot \\binom{6}{3} \\cdot 6^4$.\n"
        "Dividing the favorable outcomes by the total outcomes gives:\n"
        "$\\frac{114}{377} \\approx 0.302$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice_1_question_5a = {
    'question': (
        "Is it possible that an event is independent of itself? If so, when?"
    ),
    'options_list': ['A) No, never', 'B) Yes, always', 'C) Yes, if the probability is 0 or 1'],
    'correct_answer': 'C) Yes, if the probability is 0 or 1',
    'explanation': (
        "An event $A$ is independent of itself if $P(A \\cap A) = P(A)P(A)$. "
        "This simplifies to $P(A) = P(A)^2$, which holds only when $P(A) = 0$ or $P(A) = 1$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice_1_question_5b = {
    'question': (
        "Is it always true that if $A$ and $B$ are independent events, then $A^c$ and $B^c$ are also independent? Show that it is, or give a counterexample."
    ),
    'options_list': ['A) Yes, always', 'B) No, never', 'C) Sometimes'],
    'correct_answer': 'A) Yes, always',
    'explanation': (
        "If $A$ and $B$ are independent, then $P(A \\cap B) = P(A)P(B)$. "
        "For complements $A^c$ and $B^c$, we have:\n"
        "$P(A^c \\cap B^c) = 1 - P(A \\cup B)$, and independence implies that $P(A^c)P(B^c) = (1 - P(A))(1 - P(B))$. "
        "Thus, $A^c$ and $B^c$ are also independent."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice_1_question_6 = {
    'question': (
        "Give an example of 3 events $A$, $B$, $C$ which are pairwise independent but not independent as a group. "
        "Hint: Find an example where whether $C$ occurs is completely determined if we know whether $A$ and $B$ occurred."
    ),
    'options_list': [
        'A) XOR relation among $A$, $B$, and $C$', 
        'B) Coin flips with dependent outcomes',
        'C) Mutually exclusive events',
        'D) Events with unequal probabilities'
    ],
    'correct_answer': 'A) XOR relation among $A$, $B$, and $C$',
    'explanation': (
        "Consider three events where $A$ and $B$ are independent coin flips, and $C$ is the XOR (exclusive OR) of $A$ and $B$. "
        "This setup ensures pairwise independence but violates group independence because knowing $A$ and $B$ determines $C$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

harvard_stat110_independence_question_1 = {
    'question': (
        "Is it possible that an event is independent of itself? If so, when?"
    ),
    'options_list': [
        'A) Yes, when the probability of the event is 0 or 1',
        'B) No, it is never possible',
        'C) Yes, when the event is symmetric',
        'D) No, unless the event has equal probability'
    ],
    'correct_answer': 'A) Yes, when the probability of the event is 0 or 1',
    'explanation': (
        "Let $A$ be an event. If $A$ is independent of itself, then $P(A) = P(A \\cap A) = P(A)^2$, "
        "so $P(A)$ must be 0 or 1. This is only possible in extreme cases where the event occurs with certainty or not at all."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

harvard_stat110_independence_question_2 = {
    'question': (
        "Is it always true that if $A$ and $B$ are independent events, then $A^c$ and $B^c$ are independent events? "
        "Show that it is, or give a counterexample."
    ),
    'options_list': [
        'A) Yes, because independence holds for complements',
        'B) No, because complements are not always independent',
        'C) Yes, because of the union rule',
        'D) No, because independence breaks for complements'
    ],
    'correct_answer': 'A) Yes, because independence holds for complements',
    'explanation': (
        "We know that $P(A^c \\cap B^c) = 1 - P(A \\cup B) = 1 - (P(A) + P(B) - P(A \\cap B))$. "
        "Since $A$ and $B$ are independent, $P(A \\cap B) = P(A)P(B)$, so:\n"
        "$P(A^c \\cap B^c) = (1 - P(A))(1 - P(B)) = P(A^c)P(B^c)$. "
        "Thus, $A^c$ and $B^c$ are independent."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

harvard_stat110_independence_question_3 = {
    'question': (
        "Give an example of 3 events $A, B, C$ which are pairwise independent but not independent."
    ),
    'options_list': [
        'A) Two fair coin tosses and an indicator event for both heads',
        'B) Three dice rolls with pairwise sums equal',
        'C) Events $A$ and $B$ independent, but $C$ fully determined by $A$ and $B$',
        'D) A fair die roll with sums adding to 7'
    ],
    'correct_answer': 'A) Two fair coin tosses and an indicator event for both heads',
    'explanation': (
        "Let $A$ be the event that the first coin toss is Heads, $B$ be the event that the second toss is Heads, "
        "and $C$ be the event that both tosses are the same. The events $A$, $B$, and $C$ are pairwise independent:\n"
        "- $P(A \\cap B) = P(A)P(B)$,\n"
        "- $P(A \\cap C) = P(A)P(C)$, etc.\n"
        "However, they are not mutually independent since $C$ is fully determined by $A$ and $B$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

harvard_stat110_independence_question_4 = {
    'question': (
        "Give an example of 3 events $A, B, C$ which are not independent, yet satisfy "
        "$P(A \\cap B \\cap C) = P(A)P(B)P(C)$. Hint: consider simple and extreme cases."
    ),
    'options_list': [
        'A) Events where $P(A) = 0$',
        'B) Events determined by subsets of each other',
        'C) Coin toss events where all probabilities multiply to 0.5',
        'D) Events where $A$, $B$, and $C$ are pairwise symmetric'
    ],
    'correct_answer': 'A) Events where $P(A) = 0$',
    'explanation': (
        "If $P(A) = 0$, then $P(A \\cap B \\cap C) = 0$ automatically holds, and the equation $P(A \\cap B \\cap C) = P(A)P(B)P(C)$ "
        "is satisfied. This occurs in extreme cases where events are defined to have zero probability."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_8 = {
    'question': (
        "A bag contains one marble which is either green or blue, with equal probabilities. "
        "A green marble is put in the bag (so there are 2 marbles now), and then a random marble is taken out. "
        "The marble taken out is green. What is the probability that the remaining marble is also green?"
    ),
    'options_list': [
        'A) 1/2',
        'B) 1/3',
        'C) 2/3',
        'D) 3/4'
    ],
    'correct_answer': 'C) 2/3',
    'explanation': (
        "Let $A$ be the event that the initial marble is green, $B$ be the event that the removed marble is green, "
        "and $C$ be the event that the remaining marble is green. We want to compute $P(C|B)$.\n\n"
        "Using conditional probability:\n"
        "$P(C|B) = P(C|B,A)P(A|B) + P(C|B,A^c)P(A^c|B)$.\n\n"
        "Using Bayes' Rule for $P(A|B)$, we compute:\n"
        "$P(A|B) = \\frac{P(B|A)P(A)}{P(B)} = \\frac{1/2}{1/2 + 1/4} = 2/3$.\n\n"
        "Thus, $P(C|B) = 2/3$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_9 = {
    'question': (
        "A spam filter is designed by looking at commonly occurring phrases in spam. "
        "Suppose that 80% of email is spam. In 10% of spam emails, the phrase 'free money' is used, "
        "whereas this phrase is only used in 1% of non-spam emails. A new email mentions 'free money'. "
        "What is the probability that it is spam?"
    ),
    'options_list': [
        'A) 0.75',
        'B) 0.80',
        'C) 0.9756',
        'D) 0.90'
    ],
    'correct_answer': 'C) 0.9756',
    'explanation': (
        "Using Bayes' Rule:\n"
        "$P(S|F) = \\frac{P(F|S)P(S)}{P(F)}$, where $S$ is the event that the email is spam, "
        "and $F$ is the phrase 'free money'.\n\n"
        "Given: $P(S) = 0.8$, $P(F|S) = 0.1$, $P(F|S^c) = 0.01$, and $P(S^c) = 0.2$.\n"
        "We calculate $P(F) = P(F|S)P(S) + P(F|S^c)P(S^c) = (0.1)(0.8) + (0.01)(0.2) = 0.082$.\n\n"
        "Thus, $P(S|F) = \\frac{(0.1)(0.8)}{0.082} = 0.9756$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_10 = {
    'question': (
        "Let $G$ be the event that an individual is guilty of a certain robbery. In gathering evidence, "
        "it is learned that event $E_1$ occurred and later that another event $E_2$ also occurred.\n\n"
        "(a) Is it possible that individually, these pieces of evidence increase the chance of guilt "
        "(so $P(G|E_1) > P(G)$ and $P(G|E_2) > P(G)$), but together they decrease the chance of guilt "
        "(so $P(G|E_1, E_2) < P(G)$)?\n\n"
        "(b) Show that the probability of guilt given the evidence is the same regardless of whether "
        "we update our probabilities all at once or in two steps."
    ),
    'options_list': [
        "A) Yes, it's possible and shown with an example.",
        "B) No, it's not possible as probabilities always increase.",
        "C) It depends on $P(E_1, E_2)$.",
        "D) The probability remains constant by definition."
    ],
    'correct_answer': 'A) Yes, it\'s possible and shown with an example.',
    'explanation': (
        "(a) Yes, it is possible. Consider the example where $E_1$ and $E_2$ independently increase "
        "the likelihood of guilt, but together they preclude $G$ (e.g., events creating an alibi).\n\n"
        "(b) Using conditional probability laws, we confirm:\n"
        "$P_{\\text{new}}(G|E_1, E_2) = \\frac{P(G, E_1, E_2)}{P(E_1, E_2)}$, "
        "which is consistent whether updated sequentially or all at once."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_11 = {
    'question': (
        "A crime is committed by one of two suspects, $A$ and $B$. Initially, there is equal evidence against both. "
        "It is later found that the guilty party had a blood type matching 10% of the population. "
        "Suspect $A$ does match this blood type, while the blood type of $B$ is unknown.\n\n"
        "(a) What is the probability that $A$ is guilty given this new information?\n"
        "(b) What is the probability that $B$ matches the blood type found at the crime scene?"
    ),
    'options_list': [
        "A) 2/3 and 1/5",
        "B) 10/11 and 2/11",
        "C) 1/2 and 1/10",
        "D) 3/4 and 1/4"
    ],
    'correct_answer': 'B) 10/11 and 2/11',
    'explanation': (
        "(a) By Bayes' Rule:\n"
        "$P(A|M) = \\frac{P(M|A)P(A)}{P(M)} = \\frac{(1/2)(1/10)}{(1/2)(1/10) + (1/2)(1)} = 10/11$.\n\n"
        "(b) For suspect $B$, we compute the probability of matching the blood type:\n"
        "$P(C|M) = P(C|M,A)P(A|M) + P(C|M,B)P(B|M) = \\frac{1}{10}(1) + \\frac{1}{10}(1/2) = 2/11$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_12 = {
    'question': (
        "You are going to play 2 games of chess with an opponent whom you have never played before. "
        "Your opponent is equally likely to be a beginner, intermediate, or a master. "
        "Depending on their skill level, your chances of winning an individual game are 90%, 50%, or 30%, respectively.\n\n"
        "(a) What is your probability of winning the first game?\n"
        "(b) Given that you won the first game, what is the probability that you will also win the second game "
        "(assuming that, given the opponent's skill level, the outcomes of the games are independent)?\n"
        "(c) Explain the distinction between assuming that the outcomes of the games are independent and "
        "assuming that they are conditionally independent given the opponent's skill level. Which of these assumptions seems more reasonable, and why?"
    ),
    'options_list': [
        "A) (a) 17/30, (b) 23/34, (c) Conditional independence is more reasonable.",
        "B) (a) 1/2, (b) 2/3, (c) Independence is more reasonable.",
        "C) (a) 3/4, (b) 4/5, (c) Both assumptions are equally reasonable.",
        "D) (a) 2/3, (b) 23/30, (c) Conditional independence is more reasonable."
    ],
    'correct_answer': "A) (a) 17/30, (b) 23/34, (c) Conditional independence is more reasonable.",
    'explanation': (
        "(a) By the law of total probability:\n"
        "$P(W_1) = \\frac{1}{3}(0.9) + \\frac{1}{3}(0.5) + \\frac{1}{3}(0.3) = 17/30$.\n\n"
        "(b) Given that you won the first game, we condition on the opponent's skill level. "
        "Using Bayes' Rule and computing $P(W_2 | W_1)$:\n"
        "$P(W_2 | W_1) = \\frac{\\frac{1}{3}(0.9^2) + \\frac{1}{3}(0.5^2) + \\frac{1}{3}(0.3^2)}{17/30} = 23/34$.\n\n"
        "(c) Independence assumes outcomes are unrelated, whereas conditional independence "
        "accounts for the opponent's skill level. Conditional independence is more reasonable "
        "since winning one game provides information about the opponent's skill level."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_13 = {
    'question': (
        "Let $G$ be the event that a certain individual is guilty of a certain robbery. "
        "In gathering evidence, event $E_1$ occurred, and later another event $E_2$ also occurred.\n\n"
        "(a) Is it possible that individually, $P(G|E_1) > P(G)$ and $P(G|E_2) > P(G)$, but together $P(G|E_1, E_2) < P(G)$?\n"
        "(b) Show that the probability of guilt given the evidence is the same regardless of whether "
        "we update probabilities all at once or in two steps."
    ),
    'options_list': [
        "A) Yes, evidence can preclude guilt when combined.",
        "B) No, evidence cannot decrease probabilities together.",
        "C) Probabilities must always increase together.",
        "D) It depends on whether $E_1$ and $E_2$ overlap."
    ],
    'correct_answer': "A) Yes, evidence can preclude guilt when combined.",
    'explanation': (
        "(a) Yes, it is possible. For instance, $E_1$ and $E_2$ may independently increase the likelihood of guilt "
        "but together preclude it (e.g., they create an alibi for the full crime window).\n\n"
        "(b) Using conditional probability laws, we confirm:\n"
        "$P_{\\text{new}}(G|E_1, E_2) = \\frac{P(G, E_1, E_2)}{P(E_1, E_2)}$, "
        "which holds whether updating sequentially or all at once."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_14 = {
    'question': (
        "A crime is committed by one of two suspects, $A$ and $B$. Initially, there is equal evidence against both. "
        "It is later discovered that the guilty party's blood type matches a rare type found in 10% of the population. "
        "Suspect $A$ has this blood type, while Suspect $B$'s blood type is unknown.\n\n"
        "(a) Given this new information, what is the probability that $A$ is guilty?\n"
        "(b) What is the probability that $B$'s blood type matches the type found at the crime scene?"
    ),
    'options_list': [
        "A) 10/11 and 1/10",
        "B) 10/11 and 2/11",
        "C) 1/2 and 2/10",
        "D) 1/11 and 3/11"
    ],
    'correct_answer': "B) 10/11 and 2/11",
    'explanation': (
        "(a) By Bayes' Rule, the probability that $A$ is guilty given the blood type match is:\n"
        "$P(A|M) = \\frac{P(M|A)P(A)}{P(M)} = \\frac{1/2}{1/2 + 1/20} = 10/11$.\n\n"
        "(b) The probability that $B$ matches the blood type given the evidence is:\n"
        "$P(C|M) = P(C|M,A)P(A|M) + P(C|M,B)P(B|M) = \\frac{1}{10}(1) + \\frac{1}{10}(1/2) = 2/11$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_15 = {
    'question': (
        "You are going to play 2 games of chess with an opponent whom you have never played before. "
        "Your opponent is equally likely to be a beginner, intermediate, or a master. "
        "Depending on their skill level, your chances of winning an individual game are 90%, 50%, or 30%, respectively.\n\n"
        "(c) Explain the distinction between assuming that the outcomes of the games are independent and "
        "assuming that they are conditionally independent given the opponent's skill level. "
        "Which of these assumptions seems more reasonable, and why?"
    ),
    'options_list': [
        "A) Independence assumes no relationship between outcomes; conditional independence accounts for shared factors like skill level.",
        "B) Conditional independence assumes no skill level effect; independence assumes outcomes depend on skill.",
        "C) Independence and conditional independence are identical assumptions.",
        "D) Independence is always more reasonable in this case."
    ],
    'correct_answer': "A) Independence assumes no relationship between outcomes; conditional independence accounts for shared factors like skill level.",
    'explanation': (
        "Independence means the outcomes of the games are unrelated, whereas conditional independence "
        "means that outcomes are independent only when conditioned on the opponent's skill level. "
        "Conditional independence is more reasonable because the skill level affects both games, "
        "and winning the first game gives information about the opponent's skill level, which affects "
        "the probability of winning the second game."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_16 = {
    'question': (
        "A bag contains one marble which is either green or blue, with equal probabilities. "
        "A green marble is put in the bag (so there are now 2 marbles), and then a random marble is taken out. "
        "The marble taken out is green. What is the probability that the remaining marble is also green?"
    ),
    'options_list': [
        "A) 1/2",
        "B) 2/3",
        "C) 3/4",
        "D) 1/3"
    ],
    'correct_answer': "B) 2/3",
    'explanation': (
        "Let $A$ be the event that the initial marble is green, $B$ the event that the removed marble is green, "
        "and $C$ the event that the remaining marble is green. We condition on whether the initial marble was green.\n\n"
        "Using Bayes' Rule:\n"
        "$P(C|B) = P(C|B, A)P(A|B) + P(C|B, A^c)P(A^c|B) = 1 \\cdot P(A|B) + 0 \\cdot P(A^c|B).$\n\n"
        "To find $P(A|B)$, we use Bayes' Rule:\n"
        "$P(A|B) = \\frac{P(B|A)P(A)}{P(B)} = \\frac{1/2}{1/2 + 1/4} = 2/3.$\n\n"
        "Thus, $P(C|B) = 2/3$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_17 = {
    'question': (
        "A spam filter is designed by looking at commonly occurring phrases in spam. "
        "Suppose that 80% of email is spam. In 10% of spam emails, the phrase 'free money' is used, "
        "whereas this phrase is only used in 1% of non-spam emails. A new email just arrived, "
        "which does mention 'free money'. What is the probability that it is spam?"
    ),
    'options_list': [
        "A) 0.5",
        "B) 0.8",
        "C) 0.9756",
        "D) 0.6"
    ],
    'correct_answer': "C) 0.9756",
    'explanation': (
        "We use Bayes' Rule to find $P(S|F)$, where $S$ is the event the email is spam and $F$ is the event the phrase 'free money' appears.\n\n"
        "Bayes' Rule:\n"
        "$P(S|F) = \\frac{P(F|S)P(S)}{P(F)}.$\n"
        "We know $P(S) = 0.8$, $P(F|S) = 0.1$, and $P(F|S^c) = 0.01$. Using the law of total probability:\n"
        "$P(F) = P(F|S)P(S) + P(F|S^c)P(S^c) = 0.1 \\cdot 0.8 + 0.01 \\cdot 0.2 = 0.082.$\n\n"
        "Thus:\n"
        "$P(S|F) = \\frac{0.1 \\cdot 0.8}{0.082} = 0.9756$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

strategic_practice1_question_18 = {
    'question': (
        "A crime is committed by one of two suspects, $A$ and $B$. Initially, there is equal evidence against both. "
        "It is discovered that the guilty party's blood type matches a rare type found in 10% of the population. "
        "Suspect $A$ has this blood type, while Suspect $B$'s blood type is unknown. What is the probability that "
        "$A$ is the guilty party?"
    ),
    'options_list': [
        "A) 1/2",
        "B) 10/11",
        "C) 1/10",
        "D) 2/11"
    ],
    'correct_answer': "B) 10/11",
    'explanation': (
        "Using Bayes' Rule, let $M$ be the event that the guilty party's blood type matches the rare type. "
        "We calculate $P(A|M)$:\n"
        "$P(A|M) = \\frac{P(M|A)P(A)}{P(M)}.$\n\n"
        "Given $P(M|A) = 1$, $P(A) = 1/2$, and $P(M) = 1/2 + 1/10$, we compute:\n"
        "$P(A|M) = \\frac{1 \\cdot 1/2}{1/2 + 1/10} = 10/11$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

question_1_intersection_probability = {
    'question': (
        "What is the probability of the intersection of three independent events $A, B, C$, given $P(A) = 0.4$, $P(B) = 0.5$, and $P(C) = 0.6$?"
    ),
    'options_list': [
        "A. 0.06",
        "B. 0.10",
        "C. 0.12",
        "D. 0.15"
    ],
    'correct_answer': "C. 0.12",
    'explanation': (
        "For independent events, the probability of their intersection is given by the product of their individual probabilities:\n"
        "$$P(A \\cap B \\cap C) = P(A) \\cdot P(B) \\cdot P(C)$$\n"
        "Substituting the given values:\n"
        "$$P(A \\cap B \\cap C) = 0.4 \\cdot 0.5 \\cdot 0.6 = 0.12$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_2_pdf_of_transformed_variable = {
    'question': (
        "What is the PDF of $Y = \\cos(\\pi X)$ if $X \\sim \\text{Uniform}(0, 1)$?"
    ),
    'options_list': [
        "A. $\\frac{1}{\\pi \\sqrt{1 - y^2}}, \\quad -1 \\leq y \\leq 1$",
        "B. $\\pi \\sqrt{1 - y^2}, \\quad 0 \\leq y \\leq 1$",
        "C. $\\frac{1}{2\\pi}, \\quad -1 \\leq y \\leq 1$",
        "D. $\\frac{1}{\\sqrt{1 - y^2}}, \\quad -1 \\leq y \\leq 1$"
    ],
    'correct_answer': "A. $\\frac{1}{\\pi \\sqrt{1 - y^2}}, \\quad -1 \\leq y \\leq 1$",
    'explanation': (
        "The transformation $Y = \\cos(\\pi X)$ maps $X \\in [0, 1]$ to $Y \\in [-1, 1]$. Using the relationship between the PDFs:\n"
        "$$f_Y(y) = f_X(x) \\left| \\frac{dx}{dy} \\right|$$\n"
        "For $X \\sim \\text{Uniform}(0, 1)$, $f_X(x) = 1$. Substituting the inverse transformation $X = \\frac{\\arccos(y)}{\\pi}$, "
        "the derivative $\\frac{dx}{dy} = \\frac{-1}{\\pi \\sqrt{1 - y^2}}$, leading to:\n"
        "$$f_Y(y) = \\frac{1}{\\pi \\sqrt{1 - y^2}}, \\quad -1 \\leq y \\leq 1.$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_3_riemann_sum = {
    'question': (
        "Evaluate the Riemann sum for $\\int_0^1 x^2 dx$ using 4 subintervals and the right-endpoint method."
    ),
    'options_list': [
        "A. $\\frac{9}{32}$",
        "B. $\\frac{27}{64}$",
        "C. $\\frac{15}{64}$",
        "D. $\\frac{21}{64}$"
    ],
    'correct_answer': "B. $\\frac{27}{64}$",
    'explanation': (
        "Divide the interval $[0, 1]$ into 4 subintervals with $\\Delta x = \\frac{1}{4}$. Using right-endpoints $x_1 = \\frac{1}{4}$, "
        "$x_2 = \\frac{1}{2}$, $x_3 = \\frac{3}{4}$, $x_4 = 1$, evaluate $f(x) = x^2$:\n"
        "$$f(x_1) = \\frac{1}{16}, \\quad f(x_2) = \\frac{1}{4}, \\quad f(x_3) = \\frac{9}{16}, \\quad f(x_4) = 1.$$"
        "The Riemann sum is:\n"
        "$$\\Delta x \\sum_{i=1}^4 f(x_i) = \\frac{1}{4} \\left( \\frac{1}{16} + \\frac{4}{16} + \\frac{9}{16} + \\frac{16}{16} \\right) = \\frac{27}{64}.$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_4_joint_probability = {
    'question': (
        "If $f(x, y) = 6x$ for $0 \\leq x \\leq 1$, $x \\leq y \\leq 1$, find $P(X < 0.5 \\text{ and } Y < 0.5)$."
    ),
    'options_list': [
        "A. $\\frac{1}{16}$",
        "B. $\\frac{1}{8}$",
        "C. $\\frac{3}{16}$",
        "D. $\\frac{1}{4}$"
    ],
    'correct_answer': "B. $\\frac{1}{8}$",
    'explanation': (
        "Integrate $f(x, y)$ over $0 \\leq x \\leq 0.5$ and $x \\leq y \\leq 0.5$:\n"
        "$$P(X < 0.5, Y < 0.5) = \\int_0^{0.5} \\int_x^{0.5} 6x \\; dy \\; dx = \\int_0^{0.5} 6x (0.5 - x) \\; dx.$$"
        "Simplify:\n"
        "$$\\int_0^{0.5} 6x (0.5 - x) \\; dx = \\int_0^{0.5} (3x - 6x^2) \\; dx.$$"
        "Compute:\n"
        "$$\\int_0^{0.5} 3x \\; dx = \\frac{3}{8}, \\quad \\int_0^{0.5} 6x^2 \\; dx = \\frac{1}{4}, \\quad \\frac{3}{8} - \\frac{1}{4} = \\frac{1}{8}.$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_5_limit = {
    'question': (
        "Evaluate the limit $\\lim_{x \\to 0} \\frac{\\sin(x) - x}{x}$."
    ),
    'options_list': [
        "A. 0",
        "B. 1",
        "C. -1",
        "D. Undefined"
    ],
    'correct_answer': "A. 0",
    'explanation': (
        "Rewrite the expression as $\\frac{\\sin(x) - x}{x} = \\frac{\\sin(x)}{x} - 1$. As $x \\to 0$, $\\frac{\\sin(x)}{x} \\to 1$ (a well-known limit), "
        "so $1 - 1 = 0$."
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_6_expected_value = {
    'question': (
        "For $X \\sim \\text{Uniform}(0, 3)$, find the expected value of $Y = 2X + 1$."
    ),
    'options_list': [
        "A. 2.5",
        "B. 3",
        "C. 4",
        "D. 5"
    ],
    'correct_answer': "C. 4",
    'explanation': (
        "Using linearity of expectation, $E[Y] = E[2X + 1] = 2E[X] + 1$. For $X \\sim \\text{Uniform}(0, 3)$, $E[X] = \\frac{0 + 3}{2} = 1.5$, "
        "so $E[Y] = 2(1.5) + 1 = 4$."
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_1_derivative_evaluation = {
    'question': (
        "Evaluate the derivative of $f(x) = 3x^4 - 5x^3 + 2x - 7$ at $x = 2$."
    ),
    'options_list': [
        "A. 28",
        "B. 32",
        "C. 38",
        "D. 42"
    ],
    'correct_answer': "C. 38",
    'explanation': (
        "Differentiate $f(x)$:\n"
        "$$f'(x) = 12x^3 - 15x^2 + 2$$\n"
        "Substitute $x = 2$:\n"
        "$$f'(2) = 12(2)^3 - 15(2)^2 + 2 = 96 - 60 + 2 = 38$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_2_definite_integral = {
    'question': (
        "Find the integral of $f(x) = 5x^2 - 3x + 4$ over the interval $[1, 3]$."
    ),
    'options_list': [
        "A. 40",
        "B. 42",
        "C. 46",
        "D. 48"
    ],
    'correct_answer': "C. 46",
    'explanation': (
        "Compute the indefinite integral:\n"
        "$$\\int (5x^2 - 3x + 4) \\, dx = \\frac{5x^3}{3} - \\frac{3x^2}{2} + 4x + C$$\n"
        "Evaluate the definite integral:\n"
        "$$\\int_1^3 (5x^2 - 3x + 4) \\, dx = \\left[ \\frac{5x^3}{3} - \\frac{3x^2}{2} + 4x \\right]_1^3$$\n"
        "At $x = 3$: $\\frac{5(3)^3}{3} - \\frac{3(3)^2}{2} + 4(3) = 43.5$.\n"
        "At $x = 1$: $\\frac{5(1)^3}{3} - \\frac{3(1)^2}{2} + 4(1) = 2.5$.\n"
        "Subtract: $43.5 - 2.5 = 46$."
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_3_double_integral = {
    'question': (
        "Evaluate the double integral $\\int_0^1 \\int_0^x (x + y) \\, dy \\, dx$."
    ),
    'options_list': [
        "A. $\\frac{1}{3}$",
        "B. $\\frac{5}{12}$",
        "C. $\\frac{7}{12}$",
        "D. $\\frac{3}{4}$"
    ],
    'correct_answer': "C. $\\frac{7}{12}$",
    'explanation': (
        "Integrate with respect to $y$:\n"
        "$$\\int_0^x (x + y) \\, dy = \\left[ xy + \\frac{y^2}{2} \\right]_0^x = x^2 + \\frac{x^2}{2} = \\frac{3x^2}{2}.$$"
        "Integrate with respect to $x$:\n"
        "$$\\int_0^1 \\frac{3x^2}{2} \\, dx = \\frac{3}{2} \\int_0^1 x^2 \\, dx = \\frac{3}{2} \\left[ \\frac{x^3}{3} \\right]_0^1 = \\frac{3}{2} \\cdot \\frac{1}{3} = \\frac{7}{12}.$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_4_partial_derivative = {
    'question': (
        "Find $\\frac{\\partial}{\\partial x} \\int_0^x \\int_0^y (y^2 + 1) \\, dy \\, dx$."
    ),
    'options_list': [
        "A. $x^2 + 1$",
        "B. $x^3 + 1$",
        "C. $x^3 - x$",
        "D. $x^2 - 1$"
    ],
    'correct_answer': "B. $x^3 + 1$",
    'explanation': (
        "Compute the inner integral:\n"
        "$$\\int_0^y (y^2 + 1) \\, dy = \\left[ \\frac{y^3}{3} + y \\right]_0^y = \\frac{y^3}{3} + y.$$"
        "Substitute into the outer integral:\n"
        "$$\\int_0^x \\left( \\frac{y^3}{3} + y \\right) \\, dx = \\left[ \\frac{x^3}{3} + x \\right]_0^x = \\frac{x^3}{3} + x.$$"
        "Differentiate with respect to $x$:\n"
        "$$\\frac{\\partial}{\\partial x} \\left( \\frac{x^3}{3} + x \\right) = x^2 + 1.$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}

question_5_nested_integral = {
    'question': (
        "Solve $\\int_0^{\\pi} \\int_0^{\\sin(x)} y^2 \\, dy \\, dx$."
    ),
    'options_list': [
        "A. $\\frac{1}{3}$",
        "B. $\\frac{2}{3}$",
        "C. $1$",
        "D. $\\frac{5}{6}$"
    ],
    'correct_answer': "B. $\\frac{2}{3}$",
    'explanation': (
        "Compute the inner integral:\n"
        "$$\\int_0^{\\sin(x)} y^2 \\, dy = \\left[ \\frac{y^3}{3} \\right]_0^{\\sin(x)} = \\frac{\\sin^3(x)}{3}.$$"
        "Substitute into the outer integral:\n"
        "$$\\int_0^{\\pi} \\frac{\\sin^3(x)}{3} \\, dx = \\frac{1}{3} \\int_0^{\\pi} \\sin^3(x) \\, dx.$$"
        "Simplify $\\sin^3(x)$ as $\\sin(x)(1 - \\cos^2(x))$ and split the integral:\n"
        "$$\\frac{1}{3} \\int_0^{\\pi} \\sin(x) \\, dx - \\frac{1}{3} \\int_0^{\\pi} \\sin(x) \\cos^2(x) \\, dx.$$"
        "Evaluate:\n"
        "- $\\int_0^{\\pi} \\sin(x) \\, dx = 2$\n"
        "- $\\int_0^{\\pi} \\sin(x) \\cos^2(x) \\, dx$ using substitution $u = \\cos(x)$ gives $\\frac{2}{3}$.\n"
        "Combine results:\n"
        "$$\\frac{1}{3}(2 - \\frac{2}{3}) = \\frac{2}{3}.$$"
    ),
    'chapter_information': "Simulation Week 2 - GPT Generated Questions"
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_2_MPC = KC_MPC_QUESTIONS[:-1]