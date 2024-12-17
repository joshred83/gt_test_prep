gtx_isye6739xi_probability_and_statistics_i_fa24_question_1 = {
    'question': "If there are 23 people in the room, what are the odds that two have the same birthday?",
    'options_list': [
        '0.462',
        '0.538',
        '0.939',
        '0.061'
    ],
    'correct_answer': '0.538',
    'explanation': (
        "The probability of at least two people sharing a birthday in a group of 23 is the complement of the probability "
        "that everyone has a unique birthday. Let $P(A)$ represent the probability of all 23 people having unique birthdays. "
        "For the first person, any birthday is valid: $365/365$. For the second person, only 364 days are valid: $364/365$, and so on. "
        "This gives:\n\n"
        "$P(A) = \\frac{365}{365} \\cdot \\frac{364}{365} \\cdot \\frac{363}{365} \\cdots \\frac{343}{365} = 0.4927$\n\n"
        "Thus, the probability of at least two people sharing a birthday is $1 - P(A) = 1 - 0.4927 = 0.5073$."
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_2 = {
    'question': "How many people do you need in a class for the probability that two share the same birthday to exceed 50%?",
    'options_list': [
        '2',
        '23',
        '50',
        '183'
    ],
    'correct_answer': '23',
    'explanation': (
        "The birthday paradox shows that with 23 people, the probability of at least two sharing a birthday exceeds 50%. "
        "This is derived from the same formula used in Question 1, where we calculate the probability of all unique birthdays:\n\n"
        "$P(A) = \\prod_{i=0}^{n-1} \\frac{365-i}{365}$\n\n"
        "Solving iteratively for $n = 23$, $P(A) \\approx 0.4927$, so $1 - P(A) \\approx 0.5073$, exceeding 50%."
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_3 = {
    'question': "At $n = 50$, what is the probability that two people share the same birthday?",
    'options_list': [
        '0.850',
        '0.870',
        '0.970',
        '0.990'
    ],
    'correct_answer': '0.970',
    'explanation': (
        "Using the same formula for the probability of unique birthdays:\n\n"
        "$P(A) = \\prod_{i=0}^{n-1} \\frac{365-i}{365}$\n\n"
        "For $n = 50$, the result is $P(A) \\approx 0.0296$. Therefore, the probability of at least two people sharing a birthday is:\n\n"
        "$1 - P(A) = 1 - 0.0296 = 0.9704$."
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_4 = {
    'question': "In Muskville, where there are 687 days in a Martian year, how many students are needed in a class for the probability of two sharing a birthday to exceed 50%?",
    'options_list': [
        '20',
        '25',
        '32',
        '50'
    ],
    'correct_answer': '32',
    'explanation': (
        "With 687 days in a Martian year, the formula for unique birthdays is:\n\n"
        "$P(A) = \\prod_{i=0}^{n-1} \\frac{687-i}{687}$\n\n"
        "Iteratively solving, the probability of all unique birthdays falls below 50% at $n = 32$. "
        "Thus, with 32 students, the probability of at least two sharing a birthday exceeds 50%."
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
}

gtx_isye6739xi_probability_and_statistics_i_fa24_question_5 = {
    'question': "Which of the following is true according to the associative property of sets?",
    'options_list': [
        '$A \\cup (B \\cup C) = (A \\cup B) \\cup C$',
        '$A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C)$',
        '$A \\cap (B \\cap C) = (A \\cup B) \\cap C$',
        '$A \\cup (B \\cap C) = (A \\cup B) \\cap C$'
    ],
    'correct_answer': '$A \\cup (B \\cup C) = (A \\cup B) \\cup C$',
    'explanation': (
        "The associative property states that the grouping of sets does not affect the outcome. "
        "For union, this means $A \\cup (B \\cup C) = (A \\cup B) \\cup C$. Similarly, for intersection, "
        "$A \\cap (B \\cap C) = (A \\cap B) \\cap C$."
    ),
    'chapter_information': 'GTx ISYE6739xI Probability and Statistics I: A Gentle Introduction to Probability (FA24)'
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



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

MODULE_1_MPC = KC_MPC_QUESTIONS[:-1]
