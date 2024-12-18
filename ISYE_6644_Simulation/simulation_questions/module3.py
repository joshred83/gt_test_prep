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


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_3_MPC = KC_MPC_QUESTIONS[:-1]