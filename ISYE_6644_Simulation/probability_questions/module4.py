#Distributions + Central Limit Theorem (updated 8/5/20)

isye6739_module4_question_1 = {
    'question': (
        "A company manufactures six independent projects, each with an estimated success probability of 0.9. "
        "What is the probability that at least five of the projects will be successful?"
    ),
    'options_list': [
        "A) 0.729",
        "B) 0.886",
        "C) 0.657",
        "D) 0.943"
    ],
    'correct_answer': "B) 0.886",
    'explanation': (
        "Since the number of successful projects follows a binomial distribution $X \\sim \\text{Bin}(6, 0.9)$, we calculate:\n"
        "$\\Pr(X \\geq 5) = \\sum_{x=5}^6 \\binom{6}{x} (0.9)^x (0.1)^{6-x}$.\n"
        "This gives $\\Pr(X \\geq 5) = 0.9^5 \\cdot 6(0.1) + 0.9^6 = 0.886$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_2 = {
    'question': (
        "Assume you can make 80% of your basketball free throws. If the shots are independent, "
        "what is the probability that your first missed shot occurs on the fourth toss?"
    ),
    'options_list': [
        "A) 0.0512",
        "B) 0.1024",
        "C) 0.2048",
        "D) 0.2560"
    ],
    'correct_answer': "B) 0.1024",
    'explanation': (
        "The number of shots before the first miss follows a geometric distribution $X \\sim \\text{Geom}(0.2)$.\n"
        "The probability that the first miss occurs on the fourth toss is:\n"
        "$\\Pr(X = 4) = (0.8)^3 (0.2) = 0.1024$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_3 = {
    'question': (
        "Customers arrive at a bakery according to a Poisson process with a rate of 10 customers per hour. "
        "The bakery can handle up to 15 customers in an hour. What is the probability of an overload (more than 15 customers) "
        "in the next hour?"
    ),
    'options_list': [
        "A) 0.0287",
        "B) 0.0487",
        "C) 0.0584",
        "D) 0.0763"
    ],
    'correct_answer': "B) 0.0487",
    'explanation': (
        "The number of customers arriving follows a Poisson distribution $X \\sim \\text{Pois}(10)$. We need:\n"
        "$\\Pr(X > 15) = 1 - \\Pr(X \\leq 15) = 1 - \\sum_{x=0}^{15} \\frac{e^{-10} 10^x}{x!}$.\n"
        "Using cumulative probability, we get $\\Pr(X > 15) \\approx 0.0487$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_4 = {
    'question': (
        "The time to failure of an air conditioner is exponentially distributed with a mean of four years. "
        "What is the probability that the air conditioner will fail before the four-year mark?"
    ),
    'options_list': [
        "A) 0.632",
        "B) 0.432",
        "C) 0.368",
        "D) 0.500"
    ],
    'correct_answer': "A) 0.632",
    'explanation': (
        "The time to failure $X$ is exponentially distributed with rate $\\lambda = 1/4$ (mean is 4 years). We compute:\n"
        "$\\Pr(X \\leq 4) = 1 - e^{-\\lambda x} = 1 - e^{-(1/4)(4)} = 1 - e^{-1} \\approx 0.632$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_5 = {
    'question': (
        "Suppose the air conditioner from the previous question has already lasted 2 years. "
        "What is the probability that it will fail before the six-year mark?"
    ),
    'options_list': [
        "A) 0.368",
        "B) 0.432",
        "C) 0.632",
        "D) 0.500"
    ],
    'correct_answer': "C) 0.632",
    'explanation': (
        "Using the memoryless property of the exponential distribution:\n"
        "$\\Pr(X \\leq 6 \\mid X > 2) = \\Pr(X \\leq 4) = 0.632$ (as computed in the previous question)."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_6 = {
    'question': (
        "Let $X$ and $Y$ be independent and identically distributed exponential random variables with rate $\\lambda = 1/3$. "
        "Find $\\Pr(1 \\leq X + Y \\leq 2)$."
    ),
    'options_list': [
        "A) 0.0497",
        "B) 0.0997",
        "C) 0.1497",
        "D) 0.1997"
    ],
    'correct_answer': "B) 0.0997",
    'explanation': (
        "The sum of two independent exponential random variables with rate $\\lambda$ follows an Erlang distribution:\n"
        "$X + Y \\sim \\text{Erlang}(k=2, \\lambda=1/3)$.\n"
        "The cumulative distribution function is:\n"
        "$\\Pr(a \\leq X+Y \\leq b) = \\left[1 - \\sum_{i=0}^1 \\frac{e^{-\\lambda b}(\\lambda b)^i}{i!}\\right] - \\left[1 - \\sum_{i=0}^1 \\frac{e^{-\\lambda a}(\\lambda a)^i}{i!}\\right].$\n"
        "Plugging in $\\lambda = 1/3$, $a = 1$, and $b = 2$:\n"
        "We get $\\Pr(1 \\leq X + Y \\leq 2) \\approx 0.0997$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_7 = {
    'question': (
        "Suppose $Z$ is a standard normal random variable. Find the following probabilities:\n"
        "(a) $\\Pr(-2 < Z < 0)$\n"
        "(b) $\\Pr(-1 < Z < 1)$\n"
        "(c) $\\Pr(Z > 1.65)$\n"
        "(d) $\\Pr(Z > -1.96)$\n"
        "(e) $\\Pr(|Z| > 1.2)$."
    ),
    'options_list': ['Calculate'],
    'correct_answer': (
        "(a) $0.4773$; (b) $0.6827$; (c) $0.0495$; (d) $0.9750$; (e) $0.2301$."
    ),
    'explanation': (
        "Using the cumulative distribution function (CDF) $\\Phi(z)$ for the standard normal distribution:\n\n"
        "(a) $\\Pr(-2 < Z < 0) = \\Phi(0) - \\Phi(-2) = 0.5 - (1 - \\Phi(2)) = 0.4773$.\n\n"
        "(b) $\\Pr(-1 < Z < 1) = \\Phi(1) - \\Phi(-1) = 2\\Phi(1) - 1 = 0.6827$.\n\n"
        "(c) $\\Pr(Z > 1.65) = 1 - \\Phi(1.65) = 0.0495$.\n\n"
        "(d) $\\Pr(Z > -1.96) = \\Phi(1.96) = 0.9750$.\n\n"
        "(e) $\\Pr(|Z| > 1.2) = 2(1 - \\Phi(1.2)) = 0.2301$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_8 = {
    'question': (
        "Find $z$ such that $\\Phi(z) = 0.92$, where $\\Phi$ is the cumulative distribution function of the standard normal distribution."
    ),
    'options_list': [
        "A) 1.405",
        "B) 1.325",
        "C) 1.645",
        "D) 1.282"
    ],
    'correct_answer': "A) 1.405",
    'explanation': (
        "To find $z$ such that $\\Phi(z) = 0.92$, we use tables or software to find the corresponding quantile:\n"
        "$z = \\Phi^{-1}(0.92) = 1.405$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_9 = {
    'question': (
        "A manager requires job applicants to score at least 1000 on a test that is normally distributed with a mean of 960 and a standard deviation of 80. "
        "What percentage of applicants will pass?"
    ),
    'options_list': [
        "A) 30.854%",
        "B) 40.125%",
        "C) 50.000%",
        "D) 25.946%"
    ],
    'correct_answer': "A) 30.854%",
    'explanation': (
        "Let $X$ be the test score, $X \\sim N(960, 80^2)$. We need $\\Pr(X \\geq 1000)$:\n"
        "Standardize to find $Z$: $Z = \\frac{1000 - 960}{80} = 0.5$.\n"
        "$\\Pr(X \\geq 1000) = 1 - \\Phi(0.5) = 1 - 0.6915 = 0.30854$ (or 30.854%)."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_10 = {
    'question': (
        "If $W$, $X$, $Y$, and $Z$ are independent standard normal random variables, find $\\Pr(W + X + Y + Z \\leq 2)$."
    ),
    'options_list': [
        "A) 0.8413",
        "B) 0.7580",
        "C) 0.9200",
        "D) 0.6915"
    ],
    'correct_answer': "A) 0.8413",
    'explanation': (
        "The sum of four independent standard normal random variables follows a normal distribution:\n"
        "$W + X + Y + Z \\sim N(0, 4)$ (mean $0$ and variance $4$).\n"
        "Standardize: $Z = \\frac{A - 0}{\\sqrt{4}} = \\frac{2}{2} = 1$.\n"
        "$\\Pr(W + X + Y + Z \\leq 2) = \\Phi(1) = 0.8413$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_11 = {
    'question': (
        "Suppose that $X_1, X_2, \\dots, X_{600}$ are iid with values 1, 0, and -1, each with probability $1/3$. "
        "Find the approximate probability that the sum $\\sum_{i=1}^{600} X_i$ will be at most 40 using the Central Limit Theorem."
    ),
    'options_list': [
        'A) 0.9773',
        'B) 0.8413',
        'C) 0.3270',
        'D) 0.6826'
    ],
    'correct_answer': 'A) 0.9773',
    'explanation': (
        "Using the Central Limit Theorem, the sum $\\sum_{i=1}^{600} X_i$ is approximately normally distributed. "
        "The mean and variance of $X_i$ are:\n"
        "$E[X_i] = 0, \\; E[X_i^2] = \\sum x^2 \\Pr(X = x) = 2/3, \\; \\text{Var}(X_i) = 2/3.$\n"
        "Thus, $\\sum_{i=1}^{600} X_i \\sim \\text{Nor}(0, 600(2/3)) \\sim \\text{Nor}(0, 400)$.\n"
        "Standardize to find $P(Z \\leq 2)$:\n"
        "$P\\left(\\frac{\\sum X_i - 0}{\\sqrt{400}} \\leq \\frac{40 - 0}{\\sqrt{400}}\\right) = P(Z \\leq 2) = 0.9773$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_12 = {
    'question': (
        "A production process produces items, 6% of which are defective. A random sample of 200 items is selected daily, "
        "and the number of defective items $X$ is counted. Using the normal approximation to the binomial, find $P(X \\leq 10)$."
    ),
    'options_list': [
        'A) 0.327',
        'B) 0.475',
        'C) 0.182',
        'D) 0.682'
    ],
    'correct_answer': 'A) 0.327',
    'explanation': (
        "For $p = 0.06$, $n = 200$, $\\mu = np = 12$ and $\\sigma = \\sqrt{npq} = \\sqrt{200 \\cdot 0.06 \\cdot 0.94} = 3.359$.\n"
        "Using continuity correction, $P(X \\leq 10) \\approx P(Z \\leq \\frac{10.5 - 12}{3.359}) = P(Z \\leq -0.447) = 0.327$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_13 = {
    'question': (
        "Suppose that $Y$ has a $\\text{Nor}(50, 25)$ distribution, and $X = e^Y$. Find the mean, variance of $X$, and $P(X \\leq E[X])$."
    ),
    'options_list': [
        'A) $E[X] = e^{62.5}, P(X \\leq E[X]) = 0.9938$',
        'B) $E[X] = e^{50}, P(X \\leq E[X]) = 0.8413$',
        'C) $E[X] = e^{75}, P(X \\leq E[X]) = 0.9990$',
        'D) $E[X] = e^{55}, P(X \\leq E[X]) = 0.9000$'
    ],
    'correct_answer': 'A) $E[X] = e^{62.5}, P(X \\leq E[X]) = 0.9938$',
    'explanation': (
        "For a lognormal distribution with $Y \\sim \\text{Nor}(50, 25)$, $X = e^Y$ has:\n"
        "$E[X] = \\exp(\\mu + \\sigma^2 / 2) = e^{50 + 25/2} = e^{62.5}$.\n"
        "Using standardization to compute $P(X \\leq E[X])$:\n"
        "$P(Y \\leq 62.5) = P\\left(Z \\leq \\frac{62.5 - 50}{\\sqrt{25}}\\right) = P(Z \\leq 2.5) = 0.9938$."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_14 = {
    'question': (
        "Suppose IBM stock is currently $134 per share, and I want to guarantee the ability to buy a share for $145 on Nov 15, 2019. "
        "What is the corresponding stock option price?"
    ),
    'options_list': [
        'A) $2.02',
        'B) $3.50',
        'C) $1.75',
        'D) $2.50'
    ],
    'correct_answer': 'A) $2.02',
    'explanation': (
        "Using the normal/lognormal properties of stock prices, the option price on the market at the time was $2.02. "
        "This may change depending on market conditions, but this price reflects the given date."
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}

isye6739_module4_question_15 = {
    'question': (
        "Suppose $U_1 = 0.6$ and $U_2 = 0.9$ are iid $\\text{Unif}(0,1)$ random variables. "
        "Use the Box-Muller method to generate two iid $\\text{Nor}(0,1)$ RVs, $Z_1$ and $Z_2$."
    ),
    'options_list': [
        'A) $Z_1 = -0.594, Z_2 = 0.817$',
        'B) $Z_1 = -0.817, Z_2 = 0.594$',
        'C) $Z_1 = -1.0, Z_2 = 1.0$',
        'D) $Z_1 = 0.594, Z_2 = -0.817$'
    ],
    'correct_answer': 'A) $Z_1 = -0.594, Z_2 = 0.817$',
    'explanation': (
        "Using the Box-Muller method:\n"
        "$Z_1 = \\sqrt{-2 \\ln(U_1)} \\sin(2 \\pi U_2) = \\sqrt{-2 \\ln(0.6)} \\sin(2 \\pi \\cdot 0.9) = -0.594,$\n"
        "$Z_2 = \\sqrt{-2 \\ln(U_1)} \\cos(2 \\pi U_2) = \\sqrt{-2 \\ln(0.6)} \\cos(2 \\pi \\cdot 0.9) = 0.817.$"
    ),
    'chapter_information': 'ISYE 6739 - Module 4'
}
probability_woman_taller_man = {
    'question': (
        "Select a man and a woman at random (independent heights). Let \\( W \\) represent the height of the woman and \\( M \\) the height of the man. "
        "Find the probability that the woman is taller than the man, \\( P(W > M) \\)."
    ),
    'options_list': [
        "\\( P(W > M) = 0.09 \\)",
        "\\( P(W > M) = 0.05 \\)",
        "\\( P(W > M) = 0.95 \\)",
        "\\( P(W > M) = 0.91 \\)"
    ],
    'correct_answer': "\\( P(W > M) = 0.09 \\)",
    'explanation': (
        "### Step 1: Define the setup\n"
        "The difference \\( W - M \\) follows a Normal distribution because it is a linear combination of independent normal random variables. "
        "Given \\( W \\sim N(\\mu_W, \\sigma_W^2) \\) and \\( M \\sim N(\\mu_M, \\sigma_M^2) \\), we have:\n"
        "\\[ W - M \\sim N(\\mu_W - \\mu_M, \\sigma_W^2 + \\sigma_M^2). \\]\n"
        "Substituting \\( \\mu_W = 0 \\), \\( \\mu_M = -3 \\), \\( \\sigma_W^2 = 1 \\), and \\( \\sigma_M^2 = 4 \\):\n"
        "\\[ W - M \\sim N(-3, 5). \\]\n\n"
        "### Step 2: Standardize the variable\n"
        "To find \\( P(W > M) \\), standardize \\( W - M \\) using the standard normal distribution:\n"
        "\\[ P(W > M) = P\\left( \\frac{W - M - (-3)}{\\sqrt{5}} > \\frac{0 - (-3)}{\\sqrt{5}} \\right). \\]\n"
        "This simplifies to:\n"
        "\\[ P(W > M) = P\\left(Z > \\frac{3}{\\sqrt{5}} \\right), \\quad Z \\sim N(0, 1). \\]\n\n"
        "### Step 3: Evaluate the probability\n"
        "Using the cumulative distribution function (CDF) for the standard normal distribution, \\( \\Phi(\\cdot) \\):\n"
        "\\[ P(Z > 3 / \\sqrt{5}) = 1 - \\Phi(3 / \\sqrt{5}). \\]\n"
        "Substituting \\( \\Phi(3 / \\sqrt{5}) = 0.91 \\):\n"
        "\\[ P(W > M) = 1 - 0.91 = 0.09. \\]"
    ),
    'chapter_information': "Module 4 Lecture 13"
}

question_sample_size_n = {
    'question': (
        "Find the sample size $n$ such that $P(|\\bar{X} - \\mu| \\leq 1) \\geq 0.95$, "
        "where $\\bar{X} \\sim N(\\mu, \\frac{16}{n})$."
    ),
    'options_list': [
        "n = 50",
        "n = 62",
        "n = 75",
        "n = 100"
    ],
    'correct_answer': "n = 62",
    'explanation': (
        "To ensure $P(|\\bar{X} - \\mu| \\leq 1) \\geq 0.95$, standardize the probability: "
        "$P\\left(-\\frac{1}{\\sqrt{16/n}} \\leq Z \\leq \\frac{1}{\\sqrt{16/n}}\\right) = 0.95$. "
        "This leads to solving $2\\Phi(\\sqrt{n}/4) - 1 \\geq 0.95$. Using $\\Phi^{-1}(0.975) = 1.96$, "
        "$\\sqrt{n}/4 \\geq 1.96$ implies $n \\geq 62$."
    ),
    'chapter_information': "Module 4, Lecture 13"
}

probability_sample_mean_range = {
    'question': (
        "Suppose \\( X_1, X_2, ..., X_{100} \\) are i.i.d. random variables following an exponential distribution "
        "with rate parameter \\( \\lambda = \\frac{1}{1000} \\). Find the probability \\( P(950 \\leq \\bar{X} \\leq 1050) \\)."
    ),
    'options_list': ['Compute'],
    'correct_answer': (
        "The probability is calculated using standardization and the properties of the normal distribution:\n"
        "\\[ P(950 \\leq \\bar{X} \\leq 1050) = 2\\Phi(0.5) - 1 \\approx 0.383 \\]."
    ),
    'explanation': (
        "Step 1: Determine \\( \\mathbb{E}[X_i] \\) and \\( \\text{Var}(X_i) \\):\n"
        "- For \\( X_i \\sim \\text{Exp}(\\lambda) \\), \\( \\mathbb{E}[X_i] = \\frac{1}{\\lambda} = 1000 \\) and "
        "\\( \\text{Var}(X_i) = \\frac{1}{\\lambda^2} = 1000^2 \\).\n\n"
        "Step 2: Compute \\( \\mathbb{E}[\\bar{X}] \\) and \\( \\text{Var}(\\bar{X}) \\):\n"
        "- \\( \\mathbb{E}[\\bar{X}] = \\mathbb{E}[X_i] = 1000 \\).\n"
        "- \\( \\text{Var}(\\bar{X}) = \\frac{\\text{Var}(X_i)}{n} = \\frac{1000^2}{100} = 10000 \\).\n\n"
        "Step 3: Standardize the range \\( 950 \\leq \\bar{X} \\leq 1050 \\):\n"
        "\\[ P(950 \\leq \\bar{X} \\leq 1050) = P\\left(\\frac{950 - 1000}{\\sqrt{10000}} \\leq Z \\leq "
        "\\frac{1050 - 1000}{\\sqrt{10000}}\\right), \\]\n"
        "where \\( Z \\sim N(0,1) \\).\n"
        "\\[ P(950 \\leq \\bar{X} \\leq 1050) = P\\left(-0.5 \\leq Z \\leq 0.5\\right) = 2\\Phi(0.5) - 1 \\approx 0.383. \\]"
    ),
    'chapter_information': "Module 4 Lecture 13"
}

braves_win_probability = {
    'question': (
        "The Braves play 100 independent baseball games, each of which they have a probability of 0.8 of winning. "
        "What is the probability that they win at least 84 games?"
    ),
    'options_list': ['Compute'],
    'correct_answer': (
        "Using the Central Limit Theorem and continuity correction, the probability is:\n"
        "\\[ P(Y \\geq 84) = P(Y \\geq 83.5) \\approx P\\left(Z \\geq \\frac{83.5 - np}{\\sqrt{npq}}\\right) \\approx 0.1908. \\]"
    ),
    'explanation': (
        "Step 1: Identify the parameters:\n"
        "- \\( n = 100 \\), \\( p = 0.8 \\), \\( q = 1 - p = 0.2 \\).\n"
        "- \\( np = 100(0.8) = 80 \\).\n"
        "- \\( npq = 100(0.8)(0.2) = 16 \\).\n\n"
        "Step 2: Apply the Central Limit Theorem:\n"
        "The binomial random variable \\( Y \\sim \\text{Bin}(100, 0.8) \\) can be approximated by a normal distribution:\n"
        "\\[ Y \\sim N(np, npq) = N(80, 16). \\]\n\n"
        "Step 3: Continuity correction:\n"
        "To find \\( P(Y \\geq 84) \\), apply the continuity correction:\n"
        "\\[ P(Y \\geq 84) = P(Y \\geq 83.5). \\]\n\n"
        "Step 4: Standardize and calculate:\n"
        "Standardize using \\( Z = \\frac{Y - np}{\\sqrt{npq}} \\):\n"
        "\\[ P(Y \\geq 83.5) = P\\left(Z \\geq \\frac{83.5 - 80}{\\sqrt{16}}\\right) = P(Z \\geq 0.875). \\]\n"
        "Using the standard normal table, \\( P(Z \\geq 0.875) \\approx 0.1908. \\]"
    ),
    'chapter_information': "Module 4 Lecture 14"
}

uga_higher_iq_probability = {
    'question': (
        "Suppose that a random Georgia Tech student's IQ is $X \\sim N(115, 15)$ "
        "and a random UGA student's IQ is $Y \\sim N(75, 20)$. Find the probability "
        "that a random UGA student has a higher IQ than a random Georgia Tech student."
    ),
    'options_list': [
        "$6.841 \\times 10^{-12}$",
        "$0.001$",
        "$0.05$",
        "$0.10$"
    ],
    'correct_answer': "$6.841 \\times 10^{-12}$",
    'explanation': (
        "### Step 1: Define $Z = Y - X$\n"
        "The difference $Z$ between the IQs of UGA and Georgia Tech students is:\n"
        "\\[ Z \\sim N(\\mu_Z, \\sigma_Z^2), \\]\n"
        "where the mean and variance of $Z$ are:\n"
        "\\[ \\mu_Z = \\mu_Y - \\mu_X = 75 - 115 = -40, \\]\n"
        "\\[ \\sigma_Z^2 = \\sigma_Y^2 + \\sigma_X^2 = 20^2 + 15^2 = 400 + 225 = 625, \\]\n"
        "so $\\sigma_Z = \\sqrt{625} = 25$.\n\n"
        "### Step 2: Standardize $Z$\n"
        "To find $P(Z > 0)$, convert $Z$ to a standard normal variable $Z'$:\n"
        "\\[ Z' = \\frac{Z - \\mu_Z}{\\sigma_Z} = \\frac{Z + 40}{25}. \\]\n"
        "Thus:\n"
        "\\[ P(Z > 0) = P\\left(Z' > \\frac{40}{25}\\right) = P(Z' > 1.6). \\]\n\n"
        "### Step 3: Find the Probability\n"
        "From standard normal tables, $P(Z' > 1.6) \\approx 6.841 \\times 10^{-12}$."
    ),
    'chapter_information': "Module 4"
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

MODULE_4_MPC = KC_MPC_QUESTIONS[:-1]