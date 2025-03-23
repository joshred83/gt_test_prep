
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



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MIDTERM_2_MPC = KC_MPC_QUESTIONS[:-1]