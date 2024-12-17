gtx_isye6739xi_probability_and_statistics_i_fa24_question_1 = {
    'question': "What is the probability of drawing a red card (hearts or diamonds) from a standard deck of 52 cards?",
    'options_list': [
        '0.25',
        '0.5',
        '0.75',
        '1.0'
    ],
    'correct_answer': '0.5',
    'explanation': (
        "A standard deck has 52 cards, with 26 red cards (13 hearts + 13 diamonds). "
        "The probability of drawing a red card is:\n"
        "$P = \\frac{26}{52} = 0.5$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_2 = {
    'question': "What is the probability of rolling an even number on a fair six-sided die?",
    'options_list': [
        '0.25',
        '0.33',
        '0.5',
        '0.67'
    ],
    'correct_answer': '0.5',
    'explanation': (
        "The even numbers on a six-sided die are 2, 4, and 6, for a total of 3 outcomes. "
        "Since there are 6 possible outcomes, the probability is:\n"
        "$P = \\frac{3}{6} = 0.5$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_3 = {
    'question': "If the universal set $U = \\{1, 2, 3, 4, 5, 6\\}$ and $A = \\{2, 4, 6\\}$, what is the complement of set $A$?",
    'options_list': [
        '$\\{1, 3, 5\\}$',
        '$\\{2, 4, 6\\}$',
        '$\\{1, 2, 3, 4, 5, 6\\}$',
        '$\\{\\}$'
    ],
    'correct_answer': '$\\{1, 3, 5\\}$',
    'explanation': (
        "The complement of set $A$ consists of elements in $U$ that are not in $A$. "
        "Since $A = \\{2, 4, 6\\}$, the complement is:\n"
        "$A^c = \\{1, 3, 5\\}$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_4 = {
    'question': "Let $A = \\{1, 2, 3, 4\\}$ and $B = \\{3, 4, 5, 6\\}$. What is $A \\cap B$?",
    'options_list': [
        '$\\{1, 2, 5, 6\\}$',
        '$\\{3, 4\\}$',
        '$\\{1, 2\\}$',
        '$\\{5, 6\\}$'
    ],
    'correct_answer': '$\\{3, 4\\}$',
    'explanation': (
        "The intersection of two sets contains elements that are common to both sets. "
        "Since $A = \\{1, 2, 3, 4\\}$ and $B = \\{3, 4, 5, 6\\}$, the intersection is:\n"
        "$A \\cap B = \\{3, 4\\}$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_5 = {
    'question': "If you flip a fair coin twice, what is the probability of getting at least one heads?",
    'options_list': [
        '0.25',
        '0.5',
        '0.75',
        '1.0'
    ],
    'correct_answer': '0.75',
    'explanation': (
        "The probability of getting no heads is $P(\\text{no heads}) = \\left(\\frac{1}{2}\\right)^2 = 0.25$. "
        "Thus, the probability of getting at least one heads is:\n"
        "$P(\\text{at least one heads}) = 1 - 0.25 = 0.75$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}


gtx_isye6739xi_probability_and_statistics_i_fa24_question_6 = {
    'question': "Suppose a box contains 5 red balls, 7 blue balls, and 8 green balls. Two balls are drawn at random without replacement. What is the probability that both balls are blue?",
    'options_list': [
        '0.102',
        '0.113',
        '0.118',
        '0.122'
    ],
    'correct_answer': '0.113',
    'explanation': (
        "The total number of balls is $5 + 7 + 8 = 20$. The probability that the first ball is blue is:\n"
        "$P(\\text{first blue}) = \\frac{7}{20}$\n"
        "If the first ball is blue, there are 6 blue balls left out of 19 remaining balls:\n"
        "$P(\\text{second blue} | \\text{first blue}) = \\frac{6}{19}$\n"
        "Thus, the probability of both balls being blue is:\n"
        "$P = \\frac{7}{20} \\cdot \\frac{6}{19} = \\frac{42}{380} \\approx 0.113$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_7 = {
    'question': "A bag contains 4 fair coins, 2 of which are double-headed. You randomly draw a coin, flip it, and observe that it shows heads. What is the probability that the selected coin is double-headed?",
    'options_list': [
        '0.5',
        '0.67',
        '0.75',
        '0.8'
    ],
    'correct_answer': '0.67',
    'explanation': (
        "Use Bayes' Theorem. Let $D$ be the event that the coin is double-headed and $H$ be the event that heads is observed.\n"
        "$P(D) = \\frac{2}{4} = 0.5$\n"
        "$P(H | D) = 1$ (since a double-headed coin always shows heads)\n"
        "$P(H | \\text{fair}) = \\frac{1}{2}$\n"
        "The total probability of observing heads is:\n"
        "$P(H) = P(H | D) P(D) + P(H | \\text{fair}) P(\\text{fair})$\n"
        "$P(H) = 1 \\cdot 0.5 + \\frac{1}{2} \\cdot 0.5 = 0.75$\n"
        "By Bayes' Theorem:\n"
        "$P(D | H) = \\frac{P(H | D) P(D)}{P(H)} = \\frac{1 \\cdot 0.5}{0.75} = \\frac{2}{3} \\approx 0.67$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_8 = {
    'question': "Consider three independent events $A$, $B$, and $C$ with probabilities $P(A) = 0.6$, $P(B) = 0.5$, and $P(C) = 0.4$. What is the probability that at least one of these events occurs?",
    'options_list': [
        '0.88',
        '0.90',
        '0.92',
        '0.94'
    ],
    'correct_answer': '0.88',
    'explanation': (
        "The probability that none of the events occurs is:\n"
        "$P(\\text{none}) = (1 - P(A))(1 - P(B))(1 - P(C))$\n"
        "$= (1 - 0.6)(1 - 0.5)(1 - 0.4) = 0.4 \\cdot 0.5 \\cdot 0.6 = 0.12$\n"
        "Thus, the probability that at least one occurs is:\n"
        "$P(\\text{at least one}) = 1 - P(\\text{none}) = 1 - 0.12 = 0.88$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_9 = {
    'question': "Given two sets $A = \\{1, 2, 3, 4, 5\\}$ and $B = \\{4, 5, 6, 7\\}$, what is $A \\Delta B$, the symmetric difference of $A$ and $B$?",
    'options_list': [
        '$\\{1, 2, 3, 6, 7\\}$',
        '$\\{4, 5\\}$',
        '$\\{1, 2, 3, 4, 5, 6, 7\\}$',
        '$\\{1, 2, 3, 6\\}$'
    ],
    'correct_answer': '$\\{1, 2, 3, 6, 7\\}$',
    'explanation': (
        "The symmetric difference of two sets consists of elements that are in either set but not in both. "
        "Thus:\n"
        "$A \\Delta B = (A - B) \\cup (B - A)$\n"
        "$= \\{1, 2, 3\\} \\cup \\{6, 7\\} = \\{1, 2, 3, 6, 7\\}$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_10 = {
    'question': "A pair of dice is rolled. What is the probability that the sum of the numbers rolled is at least 10?",
    'options_list': [
        '0.125',
        '0.167',
        '0.194',
        '0.222'
    ],
    'correct_answer': '0.167',
    'explanation': (
        "Possible sums of 10 or more are 10, 11, and 12. We count the combinations that yield these sums:\n"
        "Sum of 10: (4,6), (5,5), (6,4) → 3 ways\n"
        "Sum of 11: (5,6), (6,5) → 2 ways\n"
        "Sum of 12: (6,6) → 1 way\n"
        "Total favorable outcomes: $3 + 2 + 1 = 6$\n"
        "Total outcomes: $6 \\times 6 = 36$\n"
        "Thus, the probability is:\n"
        "$P = \\frac{6}{36} = 0.167$"
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_calculus_derivative_question_1 = {
    'question': "If $f(x) = 3x^2 + 2x - 5$, what is $f'(x)$ using the power rule?",
    'options_list': [
        'A) $6x + 2$',
        'B) $6x - 2$',
        'C) $3x^2 + 2$',
        'D) $2x - 5$'
    ],
    'correct_answer': 'A) $6x + 2$',
    'explanation': (
        "The power rule states that $\\frac{d}{dx}(x^n) = nx^{n-1}$. "
        "Applying the power rule term by term:\n"
        "$f'(x) = \\frac{d}{dx}(3x^2) + \\frac{d}{dx}(2x) - \\frac{d}{dx}(5)$\n"
        "$= 6x + 2 - 0 = 6x + 2$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Introduction + Derivatives'
}

gtx_isye6739xi_calculus_derivative_question_2 = {
    'question': "Find the derivative of $f(x) = e^{2x} \\cdot \\ln(x)$ using the product rule.",
    'options_list': [
        'A) $2e^{2x}\\ln(x) + e^{2x}/x$',
        'B) $2e^{2x}/x + e^{2x}\\ln(x)$',
        'C) $2e^{2x}\\ln(x)$',
        'D) $e^{2x}/x$'
    ],
    'correct_answer': 'A) $2e^{2x}\\ln(x) + e^{2x}/x$',
    'explanation': (
        "The product rule states: $\\frac{d}{dx}(f(x)g(x)) = f'(x)g(x) + f(x)g'(x)$.\n"
        "Let $f(x) = e^{2x}$ and $g(x) = \\ln(x)$. Then:\n"
        "$f'(x) = 2e^{2x}$ and $g'(x) = \\frac{1}{x}$.\n"
        "Thus, the derivative is:\n"
        "$f'(x)g(x) + f(x)g'(x) = 2e^{2x}\\ln(x) + e^{2x}/x$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Introduction + Derivatives'
}

gtx_isye6739xi_calculus_derivative_question_3 = {
    'question': "Find $\\frac{d}{dx}(\\sin(x)\\cdot\\cos(x))$ using the product rule.",
    'options_list': [
        'A) $\\cos(2x)$',
        'B) $\\sin(2x)$',
        'C) $\\cos^2(x) - \\sin^2(x)$',
        'D) $2\\sin(x)\\cos(x)$'
    ],
    'correct_answer': 'A) $\\cos(2x)$',
    'explanation': (
        "Using the product rule:\n"
        "$\\frac{d}{dx}(\\sin(x)\\cos(x)) = \\cos(x)\\cdot\\cos(x) - \\sin(x)\\cdot\\sin(x)$\n"
        "Simplifying using the identity $\\cos(2x) = \\cos^2(x) - \\sin^2(x)$, we get:\n"
        "$\\cos(2x)$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Introduction + Derivatives'
}

gtx_isye6739xi_calculus_derivative_question_4 = {
    'question': "Find the derivative of $f(x) = \\frac{\\ln(x)}{x}$ using the quotient rule.",
    'options_list': [
        'A) $\\frac{1 - \\ln(x)}{x^2}$',
        'B) $\\frac{1 + \\ln(x)}{x^2}$',
        'C) $\\frac{\\ln(x)}{x^2}$',
        'D) $\\frac{1}{x^2}$'
    ],
    'correct_answer': 'A) $\\frac{1 - \\ln(x)}{x^2}$',
    'explanation': (
        "The quotient rule states: $\\frac{d}{dx}\\left(\\frac{f(x)}{g(x)}\\right) = \\frac{f'(x)g(x) - f(x)g'(x)}{g^2(x)}$.\n"
        "Let $f(x) = \\ln(x)$ and $g(x) = x$.\n"
        "Then, $f'(x) = \\frac{1}{x}$ and $g'(x) = 1$.\n"
        "Applying the quotient rule:\n"
        "$\\frac{\\frac{1}{x} \\cdot x - \\ln(x) \\cdot 1}{x^2} = \\frac{1 - \\ln(x)}{x^2}$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Introduction + Derivatives'
}

gtx_isye6739xi_calculus_derivative_question_5 = {
    'question': "Find the critical points of $f(x) = e^{2x} + e^{-x}$ by setting $f'(x) = 0$.",
    'options_list': [
        'A) $x = \\ln(2)/3$',
        'B) $x = \\ln(2)$',
        'C) $x = -\\ln(2)$',
        'D) $x = \\ln(2)/2$'
    ],
    'correct_answer': 'A) $x = \\ln(2)/3$',
    'explanation': (
        "To find the critical points, take the derivative:\n"
        "$f'(x) = 2e^{2x} - e^{-x}$\n"
        "Setting $f'(x) = 0$ gives:\n"
        "$2e^{2x} = e^{-x}$\n"
        "Multiplying both sides by $e^x$ yields:\n"
        "$2e^{3x} = 1$\n"
        "Solving for $x$ gives:\n"
        "$x = \\frac{\\ln(2)}{3}$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Introduction + Derivatives'
}

gtx_isye6739xi_calculus_integral_question_1 = {
    'question': "Evaluate the definite integral: $\\int_0^1 3x^2 dx$.",
    'options_list': [
        'A) 1',
        'B) 2',
        'C) 3',
        'D) 4'
    ],
    'correct_answer': 'A) 1',
    'explanation': (
        "Use the power rule for integration:\n"
        "$\\int_0^1 3x^2 dx = \\left. x^3 \\right|_0^1$\n"
        "Applying the limits of integration:\n"
        "$= 1^3 - 0^3 = 1$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Integration and Beyond'
}

gtx_isye6739xi_calculus_integral_question_2 = {
    'question': "Find the indefinite integral: $\\int e^{3x} dx$.",
    'options_list': [
        'A) $e^{3x}$',
        'B) $\\frac{e^{3x}}{3}$',
        'C) $3e^{3x}$',
        'D) $\\frac{3e^{3x}}{2}$'
    ],
    'correct_answer': 'B) $\\frac{e^{3x}}{3}$',
    'explanation': (
        "Use the exponential integration rule:\n"
        "$\\int e^{kx} dx = \\frac{e^{kx}}{k} + C$\n"
        "So:\n"
        "$\\int e^{3x} dx = \\frac{e^{3x}}{3} + C$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Integration and Beyond'
}

gtx_isye6739xi_calculus_integral_question_3 = {
    'question': "Evaluate the definite integral: $\\int_0^\\pi \\sin(x) dx$.",
    'options_list': [
        'A) 0',
        'B) 1',
        'C) 2',
        'D) -1'
    ],
    'correct_answer': 'C) 2',
    'explanation': (
        "The antiderivative of $\\sin(x)$ is $-\\cos(x)$. So:\n"
        "$\\int_0^\\pi \\sin(x) dx = -\\cos(x) \\bigg|_0^\\pi$\n"
        "Applying the limits of integration:\n"
        "$= -\\cos(\\pi) - (-\\cos(0))$\n"
        "$= -(-1) - (-1) = 2$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Integration and Beyond'
}

gtx_isye6739xi_calculus_integral_question_4 = {
    'question': "Use integration by parts to evaluate: $\\int xe^{2x} dx$.",
    'options_list': [
        'A) $\\frac{xe^{2x}}{2} - \\frac{e^{2x}}{4}$',
        'B) $\\frac{xe^{2x}}{2} + \\frac{e^{2x}}{4}$',
        'C) $\\frac{xe^{2x}}{4} - \\frac{e^{2x}}{2}$',
        'D) $\\frac{xe^{2x}}{2} - \\frac{e^{2x}}{2}$'
    ],
    'correct_answer': 'A) $\\frac{xe^{2x}}{2} - \\frac{e^{2x}}{4}$',
    'explanation': (
        "Use integration by parts where $u = x$ and $dv = e^{2x} dx$.\n"
        "$du = dx$ and $v = \\frac{e^{2x}}{2}$.\n"
        "Applying the integration by parts formula:\n"
        "$\\int xe^{2x} dx = uv - \\int vdu$\n"
        "$= x \\cdot \\frac{e^{2x}}{2} - \\int \\frac{e^{2x}}{2} dx$\n"
        "$= \\frac{xe^{2x}}{2} - \\frac{e^{2x}}{4}$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Integration and Beyond'
}

gtx_isye6739xi_calculus_integral_question_5 = {
    'question': "Find the volume under $f(x, y) = 8xy$ over the region $0 < x < y < 1$ using double integration.",
    'options_list': [
        'A) 1',
        'B) 2',
        'C) 3',
        'D) 4'
    ],
    'correct_answer': 'A) 1',
    'explanation': (
        "The volume is given by the double integral:\n"
        "$\\int_0^1 \\int_0^y 8xy dx dy$\n"
        "First, integrate with respect to $x$:\n"
        "$\\int_0^1 \\left[ 4x^2 y \\right]_0^y dy$\n"
        "$= \\int_0^1 4y^3 dy$\n"
        "Integrate with respect to $y$:\n"
        "$= y^4 \\bigg|_0^1 = 1$"
    ),
    'chapter_information': 'GTx ISYE6739xI Calculus Bootcamp: Integration and Beyond'
}

icl_multivariable_calculus_question_1 = {
    'question': "What is the derivative of the function $f(x) = x^{3/2} + \\pi x^2 + \\sqrt{7}$ evaluated at the point $x = 2$?",
    'options_list': [
        'A) $\\frac{3}{2} + 4\\pi$',
        'B) $\\frac{3}{2} + 4\\pi + \\sqrt{7}$',
        'C) $\\frac{3\\sqrt{2}}{2} + 4\\pi + \\sqrt{7}$',
        'D) $\\frac{3\\sqrt{2}}{2} + 4\\pi$'
    ],
    'correct_answer': 'D) $\\frac{3\\sqrt{2}}{2} + 4\\pi$',
    'explanation': (
        "The derivative of $f(x) = x^{3/2} + \\pi x^2 + \\sqrt{7}$ is:\n"
        "$f'(x) = \\frac{3}{2}x^{1/2} + 2\\pi x$\n"
        "Evaluating at $x = 2$:\n"
        "$f'(2) = \\frac{3}{2}\\sqrt{2} + 4\\pi$"
    ),
    'chapter_information': 'ICL - multivariable calculus'
}

icl_multivariable_calculus_question_2 = {
    'question': "What is the derivative of the function $f(x) = x^3\\cos(x)e^{x^2}$?",
    'options_list': [
        'A) $-e^{x^2}x^3\\sin(x) + e^{x^2}x^3\\cos(x) + e^{x^2}x^2\\cos(x)$',
        'B) $-3x^2\\sin(x)e^x$',
        'C) $-x^3\\sin(x) + e^{x^3} + 3e^{x^2}x^2\\cos(x)$',
        'D) $-e^{x^2}x^3\\sin(x) + e^{x^2}x^3\\cos(x) + 3e^{x^2}x^2\\cos(x)$'
    ],
    'correct_answer': 'D) $-e^{x^2}x^3\\sin(x) + e^{x^2}x^3\\cos(x) + 3e^{x^2}x^2\\cos(x)$',
    'explanation': (
        "Using the product rule and chain rule:\n"
        "$f'(x) = \\frac{d}{dx}[x^3\\cos(x)e^{x^2}]$\n"
        "$= x^3(-\\sin(x))e^{x^2} + x^3\\cos(x)\\cdot 2xe^{x^2} + 3x^2\\cos(x)e^{x^2}$\n"
        "Simplifies to:\n"
        "$f'(x) = -e^{x^2}x^3\\sin(x) + e^{x^2}x^3\\cos(x) + 3e^{x^2}x^2\\cos(x)$"
    ),
    'chapter_information': 'ICL - multivariable calculus'
}

icl_multivariable_calculus_question_3 = {
    'question': "What is the derivative of the function $f(x) = e^{[(x+1)^2]}$?",
    'options_list': [
        'A) $2(x+1)e^{[(x+1)^2]}$',
        'B) $(x+1)e^{[(x+1)^2]}$',
        'C) $e^{2(x+1)}$',
        'D) $e^{[(x+1)^2]}$'
    ],
    'correct_answer': 'A) $2(x+1)e^{[(x+1)^2]}$',
    'explanation': (
        "Using the chain rule, the derivative of $f(x) = e^{[(x+1)^2]}$ is:\n"
        "$f'(x) = e^{[(x+1)^2]} \\cdot \\frac{d}{dx}[(x+1)^2]$\n"
        "$= e^{[(x+1)^2]} \\cdot 2(x+1)$\n"
        "Thus, $f'(x) = 2(x+1)e^{[(x+1)^2]}$."
    ),
    'chapter_information': 'ICL - multivariable calculus'
}

icl_multivariable_calculus_question_4 = {
    'question': "What is the derivative of the function $f(x) = x^2\\cos(x^3)$?",
    'options_list': [
        'A) $2\\cos(x^3) - 3x^4\\cos(x^3)$',
        'B) $2\\sin(x^3) - 3x^4\\sin(x^3)$',
        'C) $2x\\sin(x^3) - 3x^4\\sin(x^3)$',
        'D) $2x\\cos(x^3) - 3x^4\\sin(x^3)$'
    ],
    'correct_answer': 'D) $2x\\cos(x^3) - 3x^4\\sin(x^3)$',
    'explanation': (
        "Using the product rule and chain rule:\n"
        "$f'(x) = \\frac{d}{dx}[x^2\\cos(x^3)]$\n"
        "$= 2x\\cos(x^3) + x^2\\frac{d}{dx}[\\cos(x^3)]$\n"
        "$= 2x\\cos(x^3) - 3x^4\\sin(x^3)$"
    ),
    'chapter_information': 'ICL - multivariable calculus'
}

icl_multivariable_calculus_question_5 = {
    'question': "What is the derivative of the function $f(x) = \\sin(x)e^{\\cos(x)}$ at the point $x = \\pi$?",
    'options_list': [
        'A) $\\frac{1}{e^2}$',
        'B) $\\frac{1}{e}$',
        'C) $-\\frac{1}{e^2}$',
        'D) $-\\frac{1}{e}$'
    ],
    'correct_answer': 'D) $-\\frac{1}{e}$',
    'explanation': (
        "Using the product rule:\n"
        "$f'(x) = \\cos(x)e^{\\cos(x)} - \\sin(x)\\sin(x)e^{\\cos(x)}$\n"
        "At $x = \\pi$:\n"
        "$f'(\\pi) = \\cos(\\pi)e^{\\cos(\\pi)} - \\sin(\\pi)e^{\\cos(\\pi)}$\n"
        "$= (-1)\\cdot \\frac{1}{e} - 0 = -\\frac{1}{e}$"
    ),
    'chapter_information': 'ICL - multivariable calculus'
}

harvard_stat110_question_4 = {
    'question': (
        "A *norepeatword* is a sequence of letters $a,b,c,...,z$ (no repetitions allowed). Show that the probability a norepeatword uses all 26 letters "
        "is approximately $1/e$."
    ),
    'options_list': ['Prove'],
    'correct_answer': (
        "The probability is approximately $\\frac{1}{e}$."
    ),
    'explanation': (
        "The total number of norepeatwords with $k$ letters is $\\binom{26}{k} k!$ for $k=1,2,...,26$. "
        "Summing over $k$, the denominator approximates the Taylor series for $e^x$ at $x=1$. The result is approximately $1/e$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

harvard_stat110_question_3 = {
    'question': (
        "(a) How many paths are there from the point $(0,0)$ to the point $(110,111)$, where each step consists of going one unit up or one unit to the right?\n\n"
        "(b) How many paths are there from $(0,0)$ to $(210,211)$, passing through $(110,111)$?"
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $\\binom{221}{110}$.\n"
        "(b) $\\binom{221}{110} \\cdot \\binom{110}{100}$."
    ),
    'explanation': (
        "(a) Each path consists of 110 upward steps and 111 rightward steps, so the total is $\\binom{221}{110}$.\n"
        "(b) The number of paths is the product of paths to $(110,111)$ and from $(110,111)$ to $(210,211)$."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

harvard_stat110_question_2 = {
    'question': (
        "A random 5-card poker hand is dealt from a standard deck of cards. Find the probability of each of the following:\n"
        "(a) A flush (all 5 cards being of the same suit, excluding royal flush).\n"
        "(b) Two pair (e.g., two 3's, two 7's, and an Ace)."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $\\frac{4 \\cdot \\binom{13}{5} - 1}{\\binom{52}{5}}$.\n"
        "(b) $\\frac{\\binom{13}{2} \\cdot \\binom{4}{2}^2 \\cdot 44}{\\binom{52}{5}}$."
    ),
    'explanation': (
        "(a) Choose 5 cards from one suit (excluding the royal flush). Multiply by 4 for all suits.\n"
        "(b) Choose 2 ranks for the pairs, select 2 cards for each rank, and pick 1 card from the remaining ranks."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}

harvard_stat110_question_1 = {
    'question': (
        "For each part, decide whether the blank should be filled in with $=, <,$ or $>$, and give a short but clear explanation.\n\n"
        "(a) (Probability that the total after rolling 4 fair dice is 21) ____ (Probability that the total after rolling 4 fair dice is 22)\n"
        "(b) (Probability that a random 2-letter word is a palindrome) ____ (Probability that a random 3-letter word is a palindrome)"
    ),
    'options_list': ['=', '<', '>'],
    'correct_answer': "(a) $>$, (b) $=$",
    'explanation': (
        "(a) To get a total of 21 with 4 dice, there are more outcomes (e.g., $(6,6,6,3), (6,5,5,5), (6,6,5,4)$) compared to getting 22, "
        "where fewer combinations exist. Thus, the probability of 21 is greater.\n"
        "(b) For both 2-letter and 3-letter words, being a palindrome depends only on the first and last letters, so the probabilities are equal."
    ),
    'chapter_information': 'Harvard Stat110 Strategic Practice 1'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

MODULE_0_MPC = KC_MPC_QUESTIONS[:-1]
