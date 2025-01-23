question_1_radioactive_decay = {
    'question': (
        "The amount of a radioactive substance in a sample decreases over time at a rate proportional to the amount present. "
        "Which differential equation describes this process?"
    ),
    'options_list': [
        "A) $\\frac{dN}{dt} = -kN$",
        "B) $\\frac{dN}{dt} = kN$",
        "C) $\\frac{dN}{dt} = -kN^2$",
        "D) $\\frac{dN}{dt} = kN^2$"
    ],
    'correct_answer': "A) $\\frac{dN}{dt} = -kN$",
    'explanation': (
        "This is the classic exponential decay equation. The rate of change of the substance $N$ is proportional to the current "
        "amount of substance present. The negative sign indicates that the substance is decaying over time."
    ),
    'chapter_information': "Mathematical Biostatistics Boot Camp 1, Johns Hopkins University"
}

question_2_population_growth = {
    'question': (
        "A population of bacteria grows exponentially, but it also has a limiting factor that decreases the growth rate as the population reaches its carrying capacity $K$. "
        "Which equation describes this logistic growth?"
    ),
    'options_list': [
        "A) $\\frac{dP}{dt} = kP(K - P)$",
        "B) $\\frac{dP}{dt} = kP(K + P)$",
        "C) $\\frac{dP}{dt} = kP - K$",
        "D) $\\frac{dP}{dt} = kP^2$"
    ],
    'correct_answer': "A) $\\frac{dP}{dt} = kP(K - P)$",
    'explanation': (
        "This is the logistic growth model, which accounts for limited resources by incorporating a carrying capacity $K$. "
        "As the population $P$ approaches $K$, the growth slows down and eventually stops."
    ),
    'chapter_information': "Mathematical Biostatistics Boot Camp 1, Johns Hopkins University"
}

question_3_newtons_law_of_cooling = {
    'question': (
        "A warm object cools in a room where the ambient temperature is constant. The rate of temperature change is proportional to the difference between the object's temperature and the room temperature. "
        "However, the proportionality constant changes over time. Which equation would model this scenario?"
    ),
    'options_list': [
        "A) $\\frac{dT}{dt} = -k(T - T_a)$",
        "B) $\\frac{dT}{dt} = k(T_a - T)$",
        "C) $\\frac{dT}{dt} = -k(t)(T - T_a)$",
        "D) $\\frac{dT}{dt} = k(T - T_a) + t$"
    ],
    'correct_answer': "A) $\\frac{dT}{dt} = -k(T - T_a)$",
    'explanation': (
        "This is Newton's Law of Cooling. The rate of temperature change is proportional to the difference between the object's "
        "temperature $T$ and the ambient temperature $T_a$. The constant $k$ is typically constant, so the equation doesn't include a time-dependent "
        "proportionality factor (which was incorrectly introduced in option C)."
    ),
    'chapter_information': "Mathematical Biostatistics Boot Camp 1, Johns Hopkins University"
}

question_4_bank_account_growth = {
    'question': (
        "A bank account has an interest rate of $r$ compounded continuously. The account balance $B(t)$ grows over time according to a rate proportional to the current balance. "
        "Which equation describes this scenario?"
    ),
    'options_list': [
        "A) $\\frac{dB}{dt} = rB$",
        "B) $\\frac{dB}{dt} = B + r$",
        "C) $\\frac{dB}{dt} = rB^2$",
        "D) $\\frac{dB}{dt} = B - r$"
    ],
    'correct_answer': "A) $\\frac{dB}{dt} = rB$",
    'explanation': (
        "This is the equation for continuous compounding. The rate of change of the balance $B(t)$ is proportional to the current balance at any time, and $r$ is the interest rate."
    ),
    'chapter_information': "Mathematical Biostatistics Boot Camp 1, Johns Hopkins University"
}

question_1_separable_differential_equation = {
    'question': (
        "Solve the equation:\n"
        "$$\n"
        "\\frac{dy}{dx} = y^{-1}x^{-3}\n"
        "$$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$y = \\pm \\sqrt{\\frac{x^4}{2} + C}$",
    'explanation': (
        "This is a separable differential equation. Solve as follows:\n\n"
        "1. Rewrite the equation:\n"
        "$$\n"
        "y \\, dy = x^{-3} \\, dx\n"
        "$$\n\n"
        "2. Integrate both sides:\n"
        "$$\n"
        "\\int y \\, dy = \\int x^{-3} \\, dx\n"
        "$$\n"
        "The left side integrates to:\n"
        "$$\n"
        "\\frac{y^2}{2}\n"
        "$$\n"
        "The right side integrates to:\n"
        "$$\n"
        "\\int x^{-3} \\, dx = \\frac{x^{-2}}{-2} = -\\frac{1}{2x^2}\n"
        "$$\n\n"
        "3. Combine and introduce the constant of integration:\n"
        "$$\n"
        "\\frac{y^2}{2} = -\\frac{1}{2x^2} + C\n"
        "$$\n\n"
        "4. Multiply through by 2:\n"
        "$$\n"
        "y^2 = -\\frac{1}{x^2} + 2C\n"
        "$$\n\n"
        "5. Rewrite $2C$ as a single constant $k$:\n"
        "$$\n"
        "y^2 = \\frac{x^4}{2} + k\n"
        "$$\n\n"
        "6. Take the square root:\n"
        "$$\n"
        "y = \\pm \\sqrt{\\frac{x^4}{2} + C}\n"
        "$$"
    ),
    'chapter_information': "Module 3 - Differential Equations GPT Generated"
}

question_2_first_order_linear = {
    'question': (
        "Solve the equation:\n"
        "$$\n"
        "f'(x) = 4f(x), \\quad f(0) = 10\n"
        "$$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$f(x) = 10e^{4x}$",
    'explanation': (
        "This is a first-order linear differential equation. The general form is:\n"
        "$$\n"
        "f'(x) = kf(x)\n"
        "$$\n"
        "The solution is:\n"
        "$$\n"
        "f(x) = Ce^{kx}\n"
        "$$\n"
        "1. Here, $k = 4$, so the solution becomes:\n"
        "$$\n"
        "f(x) = Ce^{4x}\n"
        "$$\n"
        "2. Use the initial condition $f(0) = 10$ to solve for $C$:\n"
        "$$\n"
        "f(0) = Ce^{4 \\cdot 0} = C = 10\n"
        "$$\n"
        "3. Substitute $C$ back into the solution:\n"
        "$$\n"
        "f(x) = 10e^{4x}\n"
        "$$"
    ),
    'chapter_information': "Module 3 - Differential Equations GPT Generated"
}

question_3_first_order_linear_with_initial_condition = {
    'question': (
        "Solve the equation:\n"
        "$$\n"
        "g'(x) = 8g(x), \\quad g(2) = 7\n"
        "$$"
    ),
    'options_list': ["Solution not required"],
    'correct_answer': "$g(x) = 7e^{8x - 16}$",
    'explanation': (
        "This is another first-order linear differential equation. The general solution is:\n"
        "$$\n"
        "g(x) = Ce^{8x}\n"
        "$$\n"
        "1. Use the initial condition $g(2) = 7$ to solve for $C$:\n"
        "$$\n"
        "g(2) = Ce^{8 \\cdot 2} = Ce^{16} = 7\n"
        "$$\n"
        "Solve for $C$:\n"
        "$$\n"
        "C = 7e^{-16}\n"
        "$$\n"
        "2. Substitute $C$ back into the solution:\n"
        "$$\n"
        "g(x) = 7e^{-16}e^{8x} = 7e^{8x - 16}\n"
        "$$"
    ),
    'chapter_information': "Module 3 - Differential Equations GPT Generated"
}

question_1_numerical_differentiation = {
    'question': (
        "The speed $s(t)$ of a rocket climbing into space is modeled by:\n"
        "$$\n"
        "s(t) = e^{0.5t},\n"
        "$$\n"
        "where $t$ is time in seconds. The rocket's computer uses the formula:\n"
        "$$\n"
        "s'(t) \\approx \\frac{s(t + h) - s(t)}{h}\n"
        "$$\n"
        "to estimate the acceleration at $t = 2$ seconds, with a time step $h = 0.01$. What is the approximate acceleration $s'(2)$?"
    ),
    'options_list': [
        "A. 0.35",
        "B. 1.65",
        "C. 2.71",
        "D. 4.22"
    ],
    'correct_answer': "C. 2.71",
    'explanation': (
        "The formula for numerical differentiation is:\n"
        "$$\n"
        "s'(t) \\approx \\frac{s(t + h) - s(t)}{h}.\n"
        "$$\n"
        "Substitute $t = 2$, $h = 0.01$, and $s(t) = e^{0.5t}$:\n"
        "$$\n"
        "s'(2) \\approx \\frac{e^{0.5(2 + 0.01)} - e^{0.5(2)}}{0.01}.\n"
        "$$\n"
        "Simplify:\n"
        "$$\n"
        "s'(2) \\approx \\frac{e^{1.005} - e^{1}}{0.01} \\approx \\frac{2.732 - 2.718}{0.01} \\approx 2.71.\n"
        "$$"
    ),
    'chapter_information': "Module 3 - Differential Equations GPT Generated"
}

question_2_exact_derivative = {
    'question': (
        "The height $h(t)$ of a magical balloon expanding over time is modeled by:\n"
        "$$\n"
        "h(t) = e^{3t}.\n"
        "$$\n"
        "What is the exact value of the rate of height change, $h'(t)$, at $t = 1$ second?"
    ),
    'options_list': [
        "A. $e^3$",
        "B. $2e^3$",
        "C. $3e^3$",
        "D. $e^9$"
    ],
    'correct_answer': "C. $3e^3$",
    'explanation': (
        "The derivative of $h(t)$ is given by:\n"
        "$$\n"
        "h'(t) = \\frac{d}{dt}[e^{3t}] = 3e^{3t}.\n"
        "$$\n"
        "Substitute $t = 1$:\n"
        "$$\n"
        "h'(1) = 3e^{3(1)} = 3e^3.\n"
        "$$"
    ),
    'chapter_information': "Module 3 - Differential Equations GPT Generated"
}

question_3_solving_differential_equation = {
    'question': (
        "The population $P(t)$ of bacteria in a petri dish doubles every hour, and its growth is governed by the equation:\n"
        "$$\n"
        "P'(t) = 2(1 + t)P(t), \\quad P(0) = 100.\n"
        "$$\n"
        "Find the exact formula for $P(t)$."
    ),
    'options_list': [
        "A. $P(t) = 100e^t$",
        "B. $P(t) = 100e^{t^2 + t}$",
        "C. $P(t) = 100e^{t^2 + 2t}$",
        "D. $P(t) = e^{t^2 + t}$"
    ],
    'correct_answer': "C. $P(t) = 100e^{t^2 + 2t}$",
    'explanation': (
        "This is a first-order differential equation. Rewrite it as:\n"
        "$$\n"
        "\\frac{P'(t)}{P(t)} = 2(1 + t).\n"
        "$$\n"
        "Integrate both sides:\n"
        "$$\n"
        "\\int \\frac{1}{P(t)} P'(t) \\, dt = \\int 2(1 + t) \\, dt.\n"
        "$$\n"
        "The left side simplifies to $\\ln(P(t))$, and the right side becomes $t^2 + 2t$:\n"
        "$$\n"
        "\\ln(P(t)) = t^2 + 2t + C.\n"
        "$$\n"
        "Exponentiate both sides:\n"
        "$$\n"
        "P(t) = e^{t^2 + 2t + C}.\n"
        "$$\n"
        "Simplify by letting $e^C = 100$ (from $P(0) = 100$):\n"
        "$$\n"
        "P(t) = 100e^{t^2 + 2t}.\n"
        "$$"
    ),
    'chapter_information': "Module 3 - Differential Equations GPT Generated"
}

question_4_eulers_method = {
    'question': (
        "The temperature $T(t)$ of a cup of hot cocoa cools over time and is modeled by:\n"
        "$$\n"
        "T'(t) = -0.1T(t), \\quad T(0) = 80.\n"
        "$$\n"
        "Use Euler’s method with a step size $h = 0.1$ to approximate $T(0.5)$."
    ),
    'options_list': [
        "A. 64.8",
        "B. 72.2",
        "C. 73.6",
        "D. 75.3"
    ],
    'correct_answer': "B. 72.2",
    'explanation': (
        "Euler’s method updates the value of $T(t)$ iteratively using:\n"
        "$$\n"
        "T_{n+1} = T_n + h \\cdot T'(t_n).\n"
        "$$\n"
        "1. Start with $T(0) = 80$ and compute $T'(0) = -0.1 \\cdot 80 = -8$.\n"
        "$$\n"
        "T(0.1) = 80 + 0.1 \\cdot (-8) = 80 - 0.8 = 79.2.\n"
        "$$\n"
        "2. Compute $T'(0.1) = -0.1 \\cdot 79.2 = -7.92$:\n"
        "$$\n"
        "T(0.2) = 79.2 + 0.1 \\cdot (-7.92) = 79.2 - 0.792 = 78.41.\n"
        "$$\n"
        "3. Repeat until $T(0.5)$, and the approximate value is $T(0.5) \\approx 72.2$."
    ),
    'chapter_information': "Module 3 - Differential Equations GPT Generated"
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_3_MPC = KC_MPC_QUESTIONS[:-1]