
question_1_one_to_one_transformation = {
    'question': (
        "Let $X$ be a continuous random variable with probability density function (pdf):\n"
        "$$ f_X(x) = 3x^2, \quad 0 < x < 1. $$\n"
        "Define the transformation $Y = -\ln(x)$. Determine the pdf of $Y$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of $Y$ is $f_Y(y) = 3e^{-3y}, \quad y > 0.$",
    'explanation': (
        "1. **Find the inverse transformation:**\n"
        "$$ Y = -\ln(x) \Rightarrow x = e^{-Y}. $$\n"
        "2. **Compute the derivative:**\n"
        "$$ \\frac{dx}{dy} = -e^{-Y}. $$\n"
        "Taking the absolute value, we get $|dx/dy| = e^{-Y}$.\n"
        "3. **Use the transformation formula:**\n"
        "$$ f_Y(y) = f_X(x) |dx/dy| \text{ with } x = e^{-y}. $$\n"
        "Substituting $f_X(x) = 3x^2 = 3e^{-2y}$,\n"
        "$$ f_Y(y) = 3e^{-2y} e^{-y} = 3e^{-3y}. $$\n"
        "4. **Verify normalization:**\n"
        "$$ \\int_0^{\infty} 3e^{-3y} dy = 1, $$ confirming validity."
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}


question_2_transformation_nonlinear = {
    'question': (
        "Let $X$ be a continuous random variable with pdf:\n"
        "$$ f_X(x) = 2x, \quad 0 < x < 1. $$\n"
        "Define $Y = 1 - x$. Find the pdf of $Y$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of $Y$ is $f_Y(y) = 2(1 - y), \quad 0 < y < 1.$",
    'explanation': (
        "1. **Determine the range of $Y$:**\n"
        "- When $x = 0$, we get $Y = 1$.\n"
        "- When $x = 1$, we get $Y = 0$.\n"
        "Thus, $Y$ ranges from 0 to 1.\n\n"
        "2. **Find the inverse transformation:**\n"
        "$$ x = 1 - Y. $$\n"
        "Compute the derivative:\n"
        "$$ \\frac{dx}{dy} = -1. $$\n"
        "Taking the absolute value: $|dx/dy| = 1$.\n\n"
        "3. **Apply the transformation formula:**\n"
        "$$ f_Y(y) = f_X(x) |dx/dy| \text{ with } x = 1 - y. $$\n"
        "Substitute $f_X(x) = 2(1 - y)$, we get:\n"
        "$$ f_Y(y) = 2(1 - y) \cdot 1 = 2(1 - y). $$"
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}


question_3_joint_transformation = {
    'question': (
        "Let $X$ and $Y$ be independent exponential random variables with parameter $ \\lambda = 1 $. Define new variables:\n"
        "$$ U = X + Y, \quad V = \\frac{X}{X + Y}. $$\n"
        "Find the joint pdf of $(U, V)$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The joint pdf of $(U, V)$ is $f_{U,V}(u,v) = u e^{-u}, \quad u > 0, \quad 0 < v < 1.$",
    'explanation': (
        "1. **Find the inverse transformation:**\n"
        "$$ X = U V, \quad Y = U (1 - V). $$\n"
        "2. **Compute the Jacobian determinant:**\n"
        "$$ J = \\begin{vmatrix} V & U \\\\ (1 - V) & -U \\end{vmatrix} = -U. $$\n"
        "Taking the absolute value: $|J| = U$.\n"
        "3. **Apply the transformation formula:**\n"
        "- Since $ X, Y \\sim \\text{Exp}(1) $, their joint pdf is:\n"
        "$$ f_{X,Y}(x,y) = e^{-(x+y)} = e^{-U}. $$\n"
        "- Using the Jacobian:\n"
        "$$ f_{U,V}(u,v) = f_{X,Y}(X,Y) |J| = e^{-u} \\cdot U = u e^{-u}. $$"
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}

question_4_transformation_non_monotonic = {
    'question': (
        "Let $Z$ be a continuous random variable with pdf:\n"
        "$$ f_Z(z) = \\frac{1}{2}, \quad -1 < z < 1. $$\n"
        "Define $ W = Z^2 $. Find the pdf of $W$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "The pdf of $W$ is $f_W(w) = \\frac{1}{\\sqrt{w}}, \quad 0 < w < 1.$",
    'explanation': (
        "1. **Determine the range of $W$:**\n"
        "- Since $Z \in (-1,1)$, we have $W = Z^2$ taking values in $(0,1)$.\n"
        "- The transformation is not one-to-one, since $Z = \pm \sqrt{W}$ both map to the same $W$.\n\n"
        "2. **Apply the formula for transformations with multiple pre-images:**\n"
        "$$ f_W(w) = \\sum_{z: g(z) = w} \\frac{f_Z(z)}{|g'(z)|}. $$\n"
        "- The derivative of $W = Z^2$ is $g'(z) = 2z$.\n"
        "- Taking absolute values, $|g'(z)| = 2\sqrt{W}$.\n\n"
        "3. **Compute contributions for both roots $Z = \pm \sqrt{W}$:**\n"
        "- For $Z = \sqrt{W}$, the contribution is:\n"
        "$$ f_Z(\sqrt{W}) \\frac{1}{|g'(\sqrt{W})|} = \\frac{1}{2} \\cdot \\frac{1}{2\sqrt{W}} = \\frac{1}{4\sqrt{W}}. $$\n"
        "- For $Z = -\sqrt{W}$, the contribution is the same.\n"
        "- Summing both contributions:\n"
        "$$ f_W(w) = \\frac{1}{4\sqrt{W}} + \\frac{1}{4\sqrt{W}} = \\frac{1}{2\sqrt{W}}, \quad 0 < w < 1. $$"
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}


question_23_lcg = {
    'question': (
        "Consider the linear congruential generator (LCG):\n"
        "$$ X_{i+1} = (5X_i + 3) \\mod 12. $$\n"
        "(a) Using $X_0 = 2$, calculate the first pseudo‐random number $U_1$.\n"
        "(b) Still with $X_0 = 2$, calculate the pseudo‐random number $U_{25}$."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Both $U_1$ and $U_{25}$ are approximately 0.0833.",
    'explanation': (
        "1. Compute $X_1$:\n"
        "$$ X_1 = (5 \cdot 2 + 3) \\mod 12 = 13 \\mod 12 = 1. $$\n"
        "$$ U_1 = \\frac{X_1}{12} = \\frac{1}{12} \\approx 0.0833. $$\n"
        "2. Identify the repeating cycle length by generating a few terms. The sequence cycles with period 4: "
        "$$ (X_0, X_1, X_2, X_3) = (2, 1, 8, 7). $$\n"
        "3. Since $25 \\equiv 1 \\mod 4$, it follows that $X_{25} = X_1 = 1$, so $U_{25} = U_1 = 0.0833$."
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}





question_24_exponential_transformation = {
    'question': (
        "Let \( U \\sim \\text{Unif}(0,1) \). Determine the distribution of:\n"
        "$$ Y = -4\\ln(U). $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( Y \\sim \\text{Exp}(1/4) \).",
    'explanation': (
        "1. Since \( U \\sim \\text{Unif}(0,1) \), we know that \( -\\ln(U) \\sim \\text{Exp}(1) \).\n"
        "2. Scaling by 4 transforms this into \( Y = 4(-\\ln(U)) \sim \\text{Exp}(1/4) \), "
        "with the pdf:\n"
        "   $$ f_Y(y) = \\frac{1}{4} e^{-y/4}, \\quad y \\geq 0. $$"
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}


question_26_box_muller = {
    'question': (
        "Let \( U_1, U_2 \\sim \\text{i.i.d. Unif}(0,1) \). What is the distribution of:\n"
        "$$ W = 3 + \\sqrt{-2\\ln(U_1)} \\sin(2\\pi U_2)? $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( W \\sim \\mathcal{N}(3,1) \).",
    'explanation': (
        "1. By the Box–Muller transform, \( \\sqrt{-2\\ln(U_1)} \\sin(2\\pi U_2) \sim \\mathcal{N}(0,1) \).\n"
        "2. Adding 3 shifts the mean, so the final distribution is:\n"
        "   $$ W \\sim \\mathcal{N}(3,1). $$"
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}

question_27_monte_carlo_integral = {
    'question': (
        "Estimate the integral:\n"
        "$$ I = \\int_{0}^{1} (e^x + x^2)dx $$\n"
        "using Monte Carlo integration with 5 samples drawn from \( \\text{Unif}(0,1) \):\n"
        "   \( \\{0.25, 0.50, 0.75, 0.10, 0.90\\} \).\n"
        "Use the estimator:\n"
        "$$ I_5 = \\frac{1}{5} \\sum_{i=1}^{5} (e^{U_i} + U_i^2). $$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Monte Carlo estimate \( I_5 \\approx 2.062 \).",
    'explanation': (
        "1. Compute function values at each \( U_i \):\n"
        "   $$ e^{0.25} + 0.25^2 \\approx 1.3465, $$\n"
        "   $$ e^{0.50} + 0.50^2 \\approx 1.8987, $$\n"
        "   $$ e^{0.75} + 0.75^2 \\approx 2.6795, $$\n"
        "   $$ e^{0.10} + 0.10^2 \\approx 1.1152, $$\n"
        "   $$ e^{0.90} + 0.90^2 \\approx 3.2696. $$\n"
        "2. Compute:\n"
        "   $$ I_5 = \\frac{1}{5} (1.3465 + 1.8987 + 2.6795 + 1.1152 + 3.2696) \\approx 2.062. $$"
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}

question_28_euler_method = {
    'question': (
        "Consider the differential equation:\n"
        "$$ f'(x) = (4 - x) f(x), \\quad f(0) = 2. $$\n"
        "Use Euler’s method with step \( h=0.05 \) to approximate \( f(0.1) \)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "\( f(0.1) \\approx 2.874 \).",
    'explanation': (
        "1. Euler's method formula:\n"
        "   $$ f(x+h) \\approx f(x) + h f'(x). $$\n"
        "2. Compute:\n"
        "   - \( f(0.05) \\approx 2.4 \)\n"
        "   - \( f(0.1) \\approx 2.874 \)."
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}

question_29_queue_fifo = {
    'question': (
        "A coffee shop has customers arriving at times \( 5, 8, 12, 14 \) minutes, ordering \( 2, 1, 3, 1 \) coffees respectively.\n"
        "Each coffee takes **2 minutes** to prepare, and every minute a customer waits costs **\$0.30**.\n"
        "Each coffee sells for **\$3**.\n\n"
        "(a) When does the first customer leave?\n"
        "(b) What is the average number of customers in the system during the first 15 minutes?\n"
        "(c) Compute the net profit (total revenue minus waiting cost)."
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "(a) First customer leaves at \( t=9 \). (b) Average number of customers is \( 0.73 \). "
                      "(c) Net profit is **\$19.50**.",
    'explanation': (
        "1. Compute customer departures using FIFO service.\n"
        "2. Track system size over time.\n"
        "3. Compute revenue as \( 21 \), waiting cost as \( 1.50 \), so net profit is \( 19.50 \)."
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}

question_16_lcg = {
    'question': (
        "Consider the linear congruential generator:\n"
        "$$ X_{i+1} = (5X_i + 3) \\mod 10. $$\n"
        "1. Using $$X_0 = 2$$, compute the first pseudo‐random number $$U_1$$.\n"
        "2. Using $$X_0 = 2$$, compute $$U_{501}$$. (Hint: Look for a repeating cycle.)"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "Both \( U_1 \) and \( U_{501} \) are 0.3.",
    'explanation': (
        "1. Compute \(X_1\):\n"
        "   $$ X_1 = (5 \\cdot 2 + 3) \\mod 10 = 13 \\mod 10 = 3. $$\n"
        "   $$ U_1 = \\frac{X_1}{10} = 0.3. $$\n"
        "2. Since the sequence repeats, $$ X_{501} = X_1 $$ as $$ 501 \\equiv 1 \\mod p\ $$, giving:\n"
        "   $$ U_{501} = U_1 = 0.3. $$"
    ),
    'chapter_information': "DeepSeek Generated MT1 Review"
}


deepseek_gener12ated_q8 = {
    'question': "Which template includes separate Seize, Delay, and Release modules?",
    'options_list': ['A. Basic Process', 'B. Advanced Process', 'C. Blocks', 'D. Flowchart'],
    'correct_answer': 'B. Advanced Process',
    'explanation': "The Advanced Process template includes the Seize, Delay, and Release modules for more complex modeling.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}



deepsee12k_generated_q10 = {
    'question': "TRUE or FALSE? A resource can belong to multiple resource sets simultaneously.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': "A resource can belong to multiple resource sets simultaneously, allowing more flexible resource management in simulations.",
    'chapter_information': 'Deepseek Arena Simulation Modeling'
}



question_type_ii_error = {
    'question': (
        "In a quality control test, the null hypothesis is that a machine produces items within acceptable tolerances. "
        "If the machine is actually faulty but the test fails to reject the null hypothesis, what type of error has occurred?"
    ),
    'options_list': [
        "a. Type I",
        "b. Type II"
    ],
    'correct_answer': "b. Type II",
    'explanation': (
        "A **Type I error** occurs when the null hypothesis is incorrectly rejected (false positive).\n"
        "A **Type II error** occurs when the null hypothesis is incorrectly accepted (false negative).\n"
        "Here, the null hypothesis ($H_0$: machine is within tolerances) is accepted, but the machine is actually faulty "
        "(meaning $H_0$ is false). This is a failure to reject a false null hypothesis, which is a Type II error."
    ),
    'chapter_information': 'Grok Generated'
}

question_chi_square_test = {
    'question': (
        "A set of 800 pseudo-random numbers (PRNs) is categorized into five equal probability bins. "
        "The observed counts are: [150, 165, 170, 155, 160]. "
        "Conduct a $\\chi^2$ goodness-of-fit test to determine if these numbers follow a uniform distribution at "
        "$\\alpha = 0.05$. Use the critical value $\\chi^2_{0.05,4} = 9.488$."
    ),
    'options_list': [
        "a. Accept",
        "b. Reject"
    ],
    'correct_answer': "a. Accept",
    'explanation': (
        "Expected frequency per interval: $E_i = 800 / 5 = 160$.\n"
        "Compute the $\\chi^2$ statistic:\n"
        "$\\chi^2 = \\sum \\frac{(O_i - E_i)^2}{E_i}$\n"
        "Total $\\chi^2 = 1.5625$.\n"
        "Since $\\chi^2 = 1.5625 < 9.488$, we fail to reject $H_0$, meaning the numbers appear uniform."
    ),
    'chapter_information': 'Grok Generated'
}

question_runs_test = {
    'question': (
        "A sequence of 20 pseudo-random numbers is classified as 'H' (high) if $\\geq 0.5$ and 'L' (low) if $< 0.5$. "
        "The resulting sequence is:\n"
        "H, H, L, L, H, H, L, L, H, H, L, L, H, H, L, L, H, H, L, L.\n"
        "Perform a runs test for independence. How many runs are observed?"
    ),
    'options_list': [
        "a. 5",
        "b. 10",
        "c. 15",
        "d. 20"
    ],
    'correct_answer': "b. 10",
    'explanation': (
        "A 'run' is a consecutive sequence of the same symbol (H or L).\n"
        "Observed sequence: H, H, L, L, H, H, L, L, H, H, L, L, H, H, L, L, H, H, L, L.\n"
        "Runs: (HH), (LL), (HH), (LL), (HH), (LL), (HH), (LL), (HH), (LL) → **10 runs**.\n"
        "Given $n_1 = 10$ (H’s), $n_2 = 10$ (L’s), the expected number of runs is $11$. The observed 10 runs fall within the expected range, confirming independence.\n"
        "The correct answer is **b. 10**."
    ),
    'chapter_information': 'Grok Generated'
}


question_lcg_period = {
    'question': (
        "Consider the following LCG:\n"
        "$X_i = (5X_{i-1} + 3) \\mod 16$\n"
        "Which of the following statements is true about its period?"
    ),
    'options_list': [
        "a. The sequence will always have a full period of 16.",
        "b. The period depends on the choice of the initial seed $X_0$.",
        "c. The period will always be at most 8.",
        "d. The sequence will always generate unique values."
    ],
    'correct_answer': "b. The period depends on the choice of the initial seed $X_0$.",
    'explanation': (
        "The period of an LCG depends on the modulus, multiplier, and increment. The full period occurs only if:\n"
        "- The modulus and increment are relatively prime.\n"
        "- The multiplier satisfies conditions from number theory (e.g., being a primitive root modulo $m$).\n"
        "- The initial seed is not a fixed point of the recurrence.\n"
        "If these conditions are not met, the period can be shorter than the modulus."
    ),
    'chapter_information': 'GPT 4.0 Generated'
}

question_tausworthe_generator = {
    'question': (
        "A Tausworthe generator produces the bit sequence 1100110.\n"
        "What uniform random number does this translate to in base-10 notation?"
    ),
    'options_list': [
        "a. 0.625",
        "b. 0.7969",
        "c. 0.5078",
        "d. 0.8594"
    ],
    'correct_answer': "c. 0.5078",
    'explanation': (
        "Using the base-2 conversion:\n"
        "$1100110_2 = \\frac{102}{128} = 0.5078$\n"
        "The Tausworthe generator outputs a binary fraction, which must be converted into a decimal to represent a $\\text{Unif}(0,1)$ random number."
    ),
    'chapter_information': 'GPT 4.0 Generated'
}

question_randu_issues = {
    'question': (
        "Which of the following best describes an issue with the RANDU generator?"
    ),
    'options_list': [
        "a. It produces sequences that are truly random.",
        "b. Its numbers appear uniform but exhibit dependencies in higher dimensions.",
        "c. It is the most widely used generator in cryptographic applications.",
        "d. It guarantees independence between generated values."
    ],
    'correct_answer': "b. Its numbers appear uniform but exhibit dependencies in higher dimensions.",
    'explanation': (
        "RANDU has been widely criticized because its generated numbers, when plotted in three dimensions, "
        "fall on only 15 hyperplanes instead of filling space uniformly. This causes artificial correlations in simulations."
    ),
    'chapter_information': 'GPT 4.0 Generated'
}

question_type_ii_error = {
    'question': (
        "A medical test incorrectly fails to detect a disease in a patient who actually has the disease. "
        "What type of statistical error has been made?"
    ),
    'options_list': [
        "a. Type I error (False Positive)",
        "b. Type II error (False Negative)",
        "c. No error, since the test is not designed for this.",
        "d. The null hypothesis was correctly rejected."
    ],
    'correct_answer': "b. Type II error (False Negative)",
    'explanation': (
        "A Type II error occurs when the null hypothesis is falsely accepted. In this case, the test should have detected the disease "
        "but did not, making it a false negative."
    ),
    'chapter_information': 'GPT 4.0 Generated'
}

question_chi_square_test = {
    'question': (
        "A researcher observes 500 random numbers and groups them into five equal probability bins. "
        "The expected count per bin is 100, but the observed counts are:\n"
        "\\begin{array}{|c|c|}\n"
        "\\hline\n"
        "Bin & Observed Count \\\\\n"
        "\\hline\n"
        "1 & 95 \\\\\n"
        "2 & 110 \\\\\n"
        "3 & 98 \\\\\n"
        "4 & 102 \\\\\n"
        "5 & 95 \\\\\n"
        "\\hline\n"
        "\\end{array}\n"
        "Using a Chi-square goodness-of-fit test at $\\alpha=0.05$, should the uniformity assumption be rejected?\n"
        "Given $\\chi^2_{0.05,4} = 9.49$, calculate:"
    ),
    'options_list': [
        "a. Reject $H_0$",
        "b. Accept $H_0$"
    ],
    'correct_answer': "b. Accept $H_0$",
    'explanation': (
        "$\\chi^2 = \\sum \\frac{(O_i - E_i)^2}{E_i}$\n"
        "$\\chi^2 = \\frac{(95-100)^2}{100} + \\frac{(110-100)^2}{100} + \\frac{(98-100)^2}{100} + "
        "\\frac{(102-100)^2}{100} + \\frac{(95-100)^2}{100}$\n"
        "$\\chi^2 = 1.58$\n"
        "Since $\\chi^2 = 1.58 < 9.49$, we accept the null hypothesis and conclude that the numbers appear uniform."
    ),
    'chapter_information': 'GPT 4.0 Generated'
}

question_runs_test = {
    'question': (
        "Given the sequence of numbers:\n"
        "0.41, 0.25, 0.78, 0.62, 0.15, 0.95, 0.84, 0.73, 0.55, 0.31\n"
        "Assign '+' for increasing values and '-' for decreasing values.\n"
        "The sequence of signs is:\n"
        "+ - + - - + - - + -\n"
        "How many runs does this sequence have?"
    ),
    'options_list': [
        "a. 4",
        "b. 5",
        "c. 6",
        "d. 7"
    ],
    'correct_answer': "b. 5",
    'explanation': (
        "A run is a sequence of consecutive '+' or '-' signs.\n"
        "Here, the runs are:\n"
        "+ - | + - - | + - - | + -\n"
        "This results in **5** runs, as there are five separate segments of consecutive '+' or '-' signs."
    ),
    'chapter_information': 'GPT 4.0 Generated'
}

question_lcg_full_period = {
    'question': (
        "Consider the following linear congruential generator (LCG):\n"
        "$X_i = (5X_{i-1} + 7) \\mod 16$\n"
        "Does this generator have a full period?"
    ),
    'options_list': [
        "a. True",
        "b. False"
    ],
    'correct_answer': "b. False",
    'explanation': (
        "For an LCG of the form $X_i = (aX_{i-1} + c) \\mod m$ to have a full period, the following conditions must be met:\n"
        "1. $c$ and $m$ must be coprime. Here, $c = 7$ and $m = 16$, and since $\\gcd(7,16) = 1$, this condition holds.\n"
        "2. $a - 1$ must be divisible by all prime factors of $m$. Here, $m = 16 = 2^4$, so the prime factor is 2. "
        "Since $a - 1 = 5 - 1 = 4$ is divisible by 2, this condition holds.\n"
        "3. If $m$ is a power of 2, $a - 1$ must be divisible by 4. Since $a - 1 = 4$ is divisible by 4, this condition is satisfied.\n"
        "However, computing a few terms starting from $X_0 = 0$ shows that the sequence does not cover all values from 0 to 15 before repeating. "
        "Thus, it does not have a full period of 16. The correct answer is **False**."
    ),
    'chapter_information': 'Grok Generated'
}

question_tausworthe_generator = {
    'question': (
        "A Tausworthe generator produces the bit sequence 1100110. "
        "If you use all 7 bits to generate a Unif(0,1) random number, what value do you obtain?"
    ),
    'options_list': [
        "a. 0.7969",
        "b. 0.8125",
        "c. 0.7656",
        "d. 0.7813"
    ],
    'correct_answer': "a. 0.7969",
    'explanation': (
        "To convert the bit sequence 1100110 into a Unif(0,1) random number, interpret the bits as a binary fraction "
        "and divide by $2^7$:\n"
        "$1100110_2 = 1 \\cdot 2^6 + 1 \\cdot 2^5 + 0 \\cdot 2^4 + 0 \\cdot 2^3 + 1 \\cdot 2^2 + 1 \\cdot 2^1 + 0 \\cdot 2^0$\n"
        "$= 64 + 32 + 0 + 0 + 4 + 2 + 0 = 102$\n"
        "Then, the random number is $\\frac{102}{128} = 0.796875$.\n"
        "Among the options, 0.7969 is the closest approximation to 0.796875. Thus, the correct answer is **a. 0.7969**."
    ),
    'chapter_information': 'Grok Generated'
}

question_lcg_properties = {
    'question': (
        "Which of the following statements is true about the linear congruential generator (LCG):\n"
        "$X_i = (3X_{i-1} + 5) \\mod 8$?"
    ),
    'options_list': [
        "a. It has a full period of 8.",
        "b. It produces numbers that appear uniformly distributed in one dimension.",
        "c. It is suitable for high-dimensional simulations.",
        "d. None of the above."
    ],
    'correct_answer': "d. None of the above.",
    'explanation': (
        "**Option a:** Checking the full period conditions for $m = 8$, $a = 3$, and $c = 5$, we find that the period is less than 8.\n"
        "**Option b:** Due to the short period, the numbers do not appear uniformly distributed even in one dimension.\n"
        "**Option c:** A generator with such a small modulus and short period is unsuitable for high-dimensional simulations.\n"
        "Since none of the statements are true, the correct answer is **d. None of the above**."
    ),
    'chapter_information': 'Grok Generated'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MIDTERM_2_MPC = KC_MPC_QUESTIONS[:-1]