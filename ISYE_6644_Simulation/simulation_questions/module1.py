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

question_2_monte_carlo_integration = {
    'question': (
        "True or False? The simulation technique described as “Monte Carlo integration” (e.g., estimating $\\pi$ by "
        "randomly throwing darts) does not rely on the idea that the proportion of points landing in the desired region "
        "approximates the area ratio."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': (
        "Monte Carlo integration does rely on the law of large numbers. It uses the proportion of hits in a region "
        "(like a circle) to estimate area ratios (e.g., $\\pi/4$)."
    ),
    'chapter_information': "Week 1 - CHAT GPT 01 Generated"
}

question_3_simulation_vs_analytic_numerical = {
    'question': (
        "According to the lectures, simulation models can be divided into at least three “big picture” categories: "
        "analytical, numerical, and simulation. Which statement best captures when one typically chooses to use a simulation approach?"
    ),
    'options_list': [
        "A. When the analytic solution has been fully derived and verified.",
        "B. When neither analytic nor numerical methods are feasible for the complexity or randomness in the system.",
        "C. When numerical solutions can be found quickly but the user prefers an animated 3D model.",
        "D. Whenever deterministic solutions exist and are easily implemented."
    ],
    'correct_answer': "B",
    'explanation': (
        "Simulation is usually resorted to when the system is too complex or random for direct analytical formulas or "
        "for straightforward numerical methods."
    ),
    'chapter_information': "Week 1 - CHAT GPT 01 Generated"
}

question_4_simulation_advantages = {
    'question': (
        "Which of the following is NOT listed as a potential advantage of using a simulation model?"
    ),
    'options_list': [
        "A. Ability to study systems too complicated for direct analytical or numerical approaches.",
        "B. Potential to be a “pretty” demo that can help sell ideas.",
        "C. Guarantee that results (e.g., mean waiting times) are exactly correct with zero random error.",
        "D. Potential to reduce design blunders by identifying bottlenecks before actual implementation."
    ],
    'correct_answer': "C",
    'explanation': (
        "Simulation is subject to random error (statistical variation), so it cannot guarantee an exact single value. "
        "One must attach confidence intervals or other statistical measures to the results."
    ),
    'chapter_information': "Week 1 - CHAT GPT 01 Generated"
}

question_6_ulam_neumann_simulation = {
    'question': (
        "The transcripts mention Stan Ulam and John von Neumann in the context of simulation. Which historical "
        "contribution are they most closely associated with?"
    ),
    'options_list': [
        "A. Improving the Student’s t distribution for quality control in breweries",
        "B. Developing the method of sequential hypothesis testing to catch criminals",
        "C. Conducting the earliest known “Buffon’s needle” experiments",
        "D. Using computer simulation for thermonuclear chain reactions in H-bomb research"
    ],
    'correct_answer': "D",
    'explanation': (
        "Stan Ulam and John von Neumann are cited as having used computer simulation methods in the post-World War II "
        "era to study thermonuclear chain reactions for the hydrogen bomb."
    ),
    'chapter_information': "Week 1 - CHAT GPT 01 Generated"
}

question_10_terminating_simulation = {
    'question': (
        "When analyzing a terminating simulation (e.g., a bank that closes at 4:30 PM), the Professor Goldsman mentions using "
        "independent replications. Which best describes why?"
    ),
    'options_list': [
        "A. Replications force the arrival and service process to be deterministic.",
        "B. Replications ensure data are identically distributed and correlated for simpler stats.",
        "C. Replications each cover the full run from opening to closing, so the daily outputs can be treated as separate i.i.d. “runs.”",
        "D. Replications automatically remove initialization bias."
    ],
    'correct_answer': "C",
    'explanation': (
        "For a terminating scenario (like a one-day bank simulation), each day is an entire replication, so the average performance "
        "across many days’ runs can be treated (approximately) as i.i.d. sample means."
    ),
    'chapter_information': "Week 1 - CHAT GPT 01 Generated"
}

question_1_simulation_model_types = {
    'question': (
        "Which of the following is NOT a primary type of simulation model discussed in Lesson 3?"
    ),
    'options_list': [
        "A. Discrete",
        "B. Continuous",
        "C. Deterministic",
        "D. Heuristic"
    ],
    'correct_answer': "D. Heuristic",
    'explanation': (
        "The transcript focuses on discrete, continuous, deterministic, stochastic, dynamic, and static models. "
        "Heuristic models are not mentioned."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_2_queue_waiting_time = {
    'question': (
        "TRUE or FALSE? The average waiting time for customers in a queue can always be derived analytically."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': (
        "While simple queues may have analytical solutions, simulations are often required for complex systems "
        "with randomness, such as customer arrival and service times."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_3_prngs = {
    'question': (
        "Which of the following statements about pseudo-random number generators (PRNGs) is TRUE?"
    ),
    'options_list': [
        "A. PRNGs generate truly random numbers.",
        "B. PRNGs rely on deterministic algorithms to simulate randomness.",
        "C. PRNGs are better than all physical random number generators.",
        "D. PRNGs always produce independent random numbers."
    ],
    'correct_answer': "B. PRNGs rely on deterministic algorithms to simulate randomness.",
    'explanation': (
        "PRNGs are deterministic algorithms that generate sequences of numbers that appear random. "
        "They are not truly random and may not produce independent outputs if poorly designed."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_4_terminating_simulation = {
    'question': (
        "Which of the following scenarios would require a terminating simulation?"
    ),
    'options_list': [
        "A. Analyzing patient flow in a hospital emergency room.",
        "B. Determining the steady-state performance of a manufacturing line running 24/7.",
        "C. Simulating the behavior of a bank for one business day.",
        "D. Modeling the long-term reliability of a power grid."
    ],
    'correct_answer': "C. Simulating the behavior of a bank for one business day.",
    'explanation': (
        "Terminating simulations are used for short-term studies, such as daily operations. "
        "Steady-state simulations, in contrast, analyze long-term behavior."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_5_flaw_of_averages = {
    'question': (
        "What is the 'Flaw of Averages' as described in the context of supply chains?"
    ),
    'options_list': [
        "A. Using averages instead of probability distributions can lead to unrealistic results.",
        "B. Simulation results often overestimate the efficiency of supply chains.",
        "C. Averages ignore the effects of outliers in simulation data.",
        "D. The mean of simulation outputs always matches real-world observations."
    ],
    'correct_answer': "A. Using averages instead of probability distributions can lead to unrealistic results.",
    'explanation': (
        "Averages fail to account for variability and randomness, which are crucial in complex systems like supply chains."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_6_random_number_guarantee = {
    'question': (
        "TRUE or FALSE? Random numbers generated on a computer are guaranteed to be independent and identically distributed."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': (
        "Random numbers generated by a computer are pseudo-random and not truly independent or identically distributed. "
        "Poorly designed algorithms may introduce patterns."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_7_steady_state_warmup = {
    'question': (
        "What is the primary purpose of warming up a steady-state simulation?"
    ),
    'options_list': [
        "A. To test the random number generator before starting the simulation.",
        "B. To ensure the simulation generates independent random numbers.",
        "C. To eliminate bias from initial conditions that do not reflect steady-state behavior.",
        "D. To calculate the initialization cost of the system."
    ],
    'correct_answer': "C. To eliminate bias from initial conditions that do not reflect steady-state behavior.",
    'explanation': (
        "Warming up ensures the data collected reflects long-term steady-state behavior, avoiding distortions from transient effects at the start of the simulation."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_8_steady_state_analysis = {
    'question': (
        "Which of the following methods is most commonly used for analyzing steady-state simulation output?"
    ),
    'options_list': [
        "A. Independent replications",
        "B. Variance reduction techniques",
        "C. Method of batch means",
        "D. Random walk generation"
    ],
    'correct_answer': "C. Method of batch means",
    'explanation': (
        "For steady-state simulations, the method of batch means divides one long run into batches to analyze means as independent observations."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_9_simulation_preference = {
    'question': (
        "TRUE or FALSE? Simulation is the preferred method when analytical and numerical methods fail."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "True",
    'explanation': (
        "Simulation is versatile and often used when other methods are too complicated or infeasible, particularly in systems with randomness or complexity."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_10_lcg_method = {
    'question': (
        "What does the linear congruential generator (LCG) method do to produce pseudo-random numbers?"
    ),
    'options_list': [
        "A. Uses physical processes like radioactive decay to generate randomness.",
        "B. Applies a modulus operation on a sequence of integers to generate numbers.",
        "C. Produces random numbers directly using a uniform distribution.",
        "D. Combines multiple random seeds for enhanced randomness."
    ],
    'correct_answer': "B. Applies a modulus operation on a sequence of integers to generate numbers.",
    'explanation': (
        "The LCG generates numbers using the formula $x_i = (a \\cdot x_{i-1} \\mod m)$, where $a$, $m$, and the seed are chosen constants."
    ),
    'chapter_information': "Week 1 - GPT 4 generated"
}

question_1_simulation_advantages = {
    'question': (
        "Which of the following is NOT mentioned as an advantage of simulation?"
    ),
    'options_list': [
        "A. Studying models too complicated for analytical treatments",
        "B. Reducing design blunders",
        "C. Providing exact solutions to complex problems",
        "D. Serving as a basis for experimental studies"
    ],
    'correct_answer': "C. Providing exact solutions to complex problems",
    'explanation': (
        "While simulation offers many advantages, providing exact solutions is not one of them. Simulation typically provides "
        "approximate results or estimates, not exact solutions."
    ),
    'chapter_information': "Module 1 - Perplexity generated questions"
}

question_2_simulation_output_analysis = {
    'question': (
        "What is the primary issue with analyzing simulation output data using standard statistical methods?"
    ),
    'options_list': [
        "A. Simulation output is always normally distributed",
        "B. Simulation output is independent and identically distributed",
        "C. Simulation output is neither independent nor identically distributed",
        "D. Simulation output requires more complex statistical software"
    ],
    'correct_answer': "C. Simulation output is neither independent nor identically distributed",
    'explanation': (
        "The transcript emphasizes that simulation output is not independent or identically distributed, which violates the assumptions "
        "of many standard statistical methods."
    ),
    'chapter_information': "Module 1 - Perplexity generated questions"
}

question_3_lcg_randomness = {
    'question': (
        "True or False: The linear congruential generator always produces truly random numbers."
    ),
    'options_list': ["True", "False"],
    'correct_answer': "False",
    'explanation': (
        "The linear congruential generator produces pseudo-random numbers, which are deterministic but appear random. They are not truly random."
    ),
    'chapter_information': "Module 1 - Perplexity generated questions"
}

question_4_terminating_simulation_analysis = {
    'question': (
        "Which method is typically used to analyze terminating simulations?"
    ),
    'options_list': [
        "A. Method of batch means",
        "B. Method of independent replications",
        "C. Spectral analysis",
        "D. Regeneration method"
    ],
    'correct_answer': "B. Method of independent replications",
    'explanation': (
        "The transcript states that terminating simulations are usually analyzed using the method of independent replications."
    ),
    'chapter_information': "Module 1 - Perplexity generated questions"
}

question_5_steady_state_warmup = {
    'question': (
        "What is the main purpose of the 'warm-up' period in steady-state simulations?"
    ),
    'options_list': [
        "A. To increase the simulation speed",
        "B. To deal with initialization bias",
        "C. To generate more random numbers",
        "D. To replicate the simulation multiple times"
    ],
    'correct_answer': "B. To deal with initialization bias",
    'explanation': (
        "The warm-up period is used to deal with initialization bias, which occurs because the beginning of a simulation may "
        "not be representative of steady-state behavior."
    ),
    'chapter_information': "Module 1 - Perplexity generated questions"
}

question_1_deter2ministic_vs_stochastic = {
    'question': (
        "In the lessons, Professor Goldsman contrasts deterministic and stochastic models. Which scenario below best illustrates "
        "a stochastic (i.e., random) model according to the transcripts?"
    ),
    'options_list': [
        "A. A rock is dropped from a cliff with no friction, and its exact trajectory is given by a known physics formula.",
        "B. A warehouse in which arrival times of delivery trucks and service times are modeled using Exponential distributions.",
        "C. A known polynomial equation is solved for its roots.",
        "D. A spreadsheet that calculates the monthly mortgage payment for a fixed-rate loan."
    ],
    'correct_answer': "B",
    'explanation': (
        "A stochastic model involves probabilistic elements: uncertain arrivals, random service times, etc. The other examples "
        "(exact physics, solving polynomials, or fixed mortgage payments) are deterministic."
    ),
    'chapter_information': "Week 1, GPT O1 Generated"
}

question_2_discrete_vs_2continuous = {
    'question': (
        "Which of the following systems described by Professor Goldsman would be considered a discrete model rather than continuous?"
    ),
    'options_list': [
        "A. Simulating weather patterns across different regions.",
        "B. Modeling the flow of customers arriving and departing a retail store queue.",
        "C. Modeling changes in temperature throughout each hour of the day.",
        "D. Modeling stock price changes via continuous Brownian motion."
    ],
    'correct_answer': "B",
    'explanation': (
        "A discrete model changes only at discrete points (arrivals, departures, etc.). Weather or temperature typically vary continuously, "
        "and many stock price models are treated as continuous processes (e.g., Brownian motion)."
    ),
    'chapter_information': "Week 1, GPT O1 Generated"
}

question_3_motivation_fo2r_simulation = {
    'question': (
        "Professor Goldsman argues that simulation is often chosen when analytical and numerical methods aren’t feasible. "
        "Which of these best captures a condition that justifies using simulation, rather than an exact formula?"
    ),
    'options_list': [
        "A. We can solve the system easily with a closed-form solution.",
        "B. The system is fully deterministic and trivially small in size.",
        "C. There is high variability and complex interactions making direct formulas or standard numerical methods impractical.",
        "D. We are not interested in the system’s random behavior, only a single average value."
    ],
    'correct_answer': "C",
    'explanation': (
        "Simulation excels where there is significant complexity or randomness that defeats simpler analytic or numeric methods."
    ),
    'chapter_information': "Week 1, GPT O1 Generated"
}

question_5_termi2nating_vs_steady_state = {
    'question': (
        "According to Professor Goldsman, a terminating simulation is appropriate when:"
    ),
    'options_list': [
        "A. The system starts empty and never ends.",
        "B. We are interested in short-run performance over a fixed window, like a bank open from 9 a.m. to 4:30 p.m.",
        "C. We want to ignore any special startup effects and jump straight to a 'long-term' viewpoint.",
        "D. We want to run one indefinite replication and batch the data into intervals."
    ],
    'correct_answer': "B",
    'explanation': (
        "Terminating simulations focus on finite-horizon contexts (e.g., daily operations from open to close). "
        "Steady-state simulations are for long-run, indefinite scenarios."
    ),
    'chapter_information': "Week 1, GPT O1 Generated"
}

question_6_warm_u2p_period = {
    'question': (
        "In a steady-state simulation, Professor Goldsman emphasizes 'warming up' the system before collecting data. "
        "This warm-up period is meant to:"
    ),
    'options_list': [
        "A. Speed up the computer’s CPU cycles.",
        "B. Guarantee that all random streams are truly random.",
        "C. Let the system reach a more typical operating condition, reducing bias from an empty or unrealistic start.",
        "D. Make sure the simulation results match a closed-form formula precisely."
    ],
    'correct_answer': "C",
    'explanation': (
        "When a model starts from an empty (or non-typical) state, early observations do not represent the long-run behavior. "
        "A warm-up discards early, skewed data."
    ),
    'chapter_information': "Week 1, GPT O1 Generated"
}

question_10_varia2nce_reduction = {
    'question': (
        "One reason Professor Goldsman says variance reduction is so important in simulation is that it allows you to:"
    ),
    'options_list': [
        "A. Eliminate all randomness entirely.",
        "B. Make fewer simulation runs yet still achieve reliable statistical estimates.",
        "C. Force the simulation output to be an i.i.d. normal sample.",
        "D. Skip the warm-up period in steady-state simulations."
    ],
    'correct_answer': "B",
    'explanation': (
        "Variance reduction techniques (e.g., common random numbers, antithetic variates, etc.) help improve precision so that "
        "fewer runs are needed for the same statistical confidence."
    ),
    'chapter_information': "Week 1, GPT O1 Generated"
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_1_MPC = KC_MPC_QUESTIONS[:-1]
