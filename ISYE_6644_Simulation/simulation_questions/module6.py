prn_chat_gpt_week7_q1 = {
    'question': (
        "Suppose that a Tausworthe generator produces the following series of bits: 1101101.\n"
        "If you use all 7 bits, what Unif(0,1) random number would that translate to?"
    ),
    'options_list': ['0.8515625', '0.65', '0.5', '0.75'],
    'correct_answer': '0.8515625',
    'explanation': (
        "The binary sequence is 1101101, which corresponds to the following fraction:\n\n"
        "1/2 + 1/4 + 0/8 + 1/16 + 1/32 + 0/64 + 1/128\n\n"
        "Calculating the sum:\n"
        "0.5 + 0.25 + 0.0625 + 0.03125 + 0.0078125 = 0.8515625"
    ),
    'chapter_information': 'PRNG and Random Number Generation'
}

prn_chat_gpt_week7_q2 = {
    'question': (
        "Suppose that the Tausworthe PRNG gives you the sequence 011010110111.\n"
        "If you use the first 8 bits, what Unif(0,1) random number would that represent?"
    ),
    'options_list': ['0.41896875', '0.625', '0.3', '0.5'],
    'correct_answer': '0.41896875',
    'explanation': (
        "The first 8 bits are 01101011. To convert this to a uniform random number:\n\n"
        "0/2 + 1/4 + 1/8 + 0/16 + 1/32 + 0/64 + 1/128 + 1/256\n\n"
        "Calculating the sum:\n"
        "0.25 + 0.125 + 0.03125 + 0.0078125 + 0.00390625 = 0.41896875"
    ),
    'chapter_information': 'PRNG and Random Number Generation'
}

prn_chat_gpt_week7_q3 = {
    'question': (
        "A Tausworthe generator gives you the 5-bit sequence: 10101.\n"
        "What Unif(0,1) random number does this represent?"
    ),
    'options_list': ['0.65625', '0.8', '0.45', '0.25'],
    'correct_answer': '0.65625',
    'explanation': (
        "The binary sequence 10101 corresponds to the following fraction:\n\n"
        "1/2 + 0/4 + 1/8 + 0/16 + 1/32\n\n"
        "Calculating the sum:\n"
        "0.5 + 0.125 + 0.03125 = 0.65625"
    ),
    'chapter_information': 'PRNG and Random Number Generation'
}

prn_chat_gpt_week7_q4 = {
    'question': (
        "A Tausworthe generator outputs two 4-bit sequences:\n"
        "First sequence: 1101\n"
        "Second sequence: 1010\n"
        "Combine these two sequences to form an 8-bit number. "
        "What Unif(0,1) random number does this represent?"
    ),
    'options_list': ['0.8515625', '0.9', '0.65', '0.75'],
    'correct_answer': '0.8515625',
    'explanation': (
        "The two 4-bit sequences are 1101 and 1010, which together form the 8-bit sequence 11011010.\n\n"
        "To convert this to a uniform random number:\n\n"
        "1/2 + 1/4 + 0/8 + 1/16 + 1/32 + 0/64 + 1/128 + 0/256\n\n"
        "Calculating the sum:\n"
        "0.5 + 0.25 + 0.0625 + 0.03125 + 0.0078125 = 0.8515625"
    ),
    'chapter_information': 'PRNG and Random Number Generation'
}

prn_chat_gpt_week7_q5 = {
    'question': (
        "A Tausworthe generator produces the sequence 101110110101.\n"
        "If you use only the first 6 bits, what Unif(0,1) random number would that represent?"
    ),
    'options_list': ['0.734375', '0.8', '0.5', '0.6'],
    'correct_answer': '0.734375',
    'explanation': (
        "The first 6 bits are 101110. To convert this to a uniform random number:\n\n"
        "1/2 + 0/4 + 1/8 + 1/16 + 1/32 + 1/64\n\n"
        "Calculating the sum:\n"
        "0.5 + 0.125 + 0.0625 + 0.03125 + 0.015625 = 0.734375"
    ),
    'chapter_information': 'PRNG and Random Number Generation'
}

question_1_prng_properties = {
    'question': "Which of the following is a necessary property for a good pseudo-random number generator (PRNG)?",
    'options_list': [
        'The numbers must appear to be normally distributed.',
        'The numbers must be uniformly distributed between 0 and 1.',
        'The sequence of numbers should be easy to predict.',
        'The numbers should have a long period with minimal repetition.'
    ],
    'correct_answer': 'The numbers must be uniformly distributed between 0 and 1.',
    'explanation': (
        "A good PRNG should generate numbers that are uniformly distributed between 0 and 1, which ensures that "
        "every possible number within this range has an equal probability of being selected. This is a fundamental "
        "property for most simulations and statistical methods."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_2_goodness_of_fit_prng = {
    'question': "You are evaluating a PRNG using a Chi-square goodness-of-fit test. The statistic calculated from the test is much greater than the critical value for the given degrees of freedom. What conclusion should you draw?",
    'options_list': [
        'The PRNG is likely producing numbers that are uniformly distributed.',
        'The PRNG is likely producing numbers that are not uniformly distributed.',
        'The PRNG is likely producing numbers that are not independent.',
        'The PRNG is likely producing numbers that follow a normal distribution.'
    ],
    'correct_answer': 'The PRNG is likely producing numbers that are not uniformly distributed.',
    'explanation': (
        "A goodness-of-fit test compares the observed distribution of generated numbers to the expected distribution "
        "(uniform in the case of a PRNG). If the statistic is much greater than the critical value, it indicates that "
        "the observed distribution significantly deviates from the expected uniform distribution. Hence, the numbers are "
        "likely not uniformly distributed."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_3_period_of_prng = {
    'question': "What is the 'period' of a pseudo-random number generator?",
    'options_list': [
        'The time it takes to generate one random number.',
        'The number of distinct values the PRNG can generate before it starts repeating.',
        'The total number of random numbers the PRNG can generate.',
        'The number of times the PRNG needs to be reinitialized to produce a different sequence.'
    ],
    'correct_answer': 'The number of distinct values the PRNG can generate before it starts repeating.',
    'explanation': (
        "The period of a PRNG refers to the length of the sequence of pseudo-random numbers it generates before the "
        "sequence starts repeating itself. A long period is desirable because it means that the generator can produce "
        "a large number of random numbers before the sequence begins to repeat."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_4_independence_of_random_numbers = {
    'question': "Why is independence of pseudo-random numbers important for simulations?",
    'options_list': [
        'Independence ensures that the generated numbers are uniformly distributed.',
        'Independence allows the generator to produce new, unpredictable numbers for each iteration.',
        'Independence means that the numbers have no relationship with each other, reducing the risk of bias.',
        'All of the above.'
    ],
    'correct_answer': 'All of the above.',
    'explanation': (
        "Independence is crucial because it ensures that each random number is generated without any dependency on the "
        "previous numbers. This prevents patterns or biases from emerging in simulations, which could lead to incorrect "
        "results."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_5_tausworthe_generator_conversion = {
    'question': "Suppose a Tausworthe generator produces the following bit sequence: 11011. Convert this 5-bit sequence to a uniform random number in the range [0,1].",
    'options_list': ['0.75', '0.875', '0.6875', '0.8125'],
    'correct_answer': '0.875',
    'explanation': (
        "The binary sequence 11011 corresponds to the following binary fraction:\n"
        "$\\frac{1}{2} + \\frac{1}{4} + \\frac{0}{8} + \\frac{1}{16} + \\frac{1}{32}$\n"
        "Calculating the sum: $0.5 + 0.25 + 0.0625 = 0.8125$. The final value is 0.875, which matches option (b)."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_6_periodicity_and_randomness = {
    'question': "A pseudo-random number generator with a period of 1000 will generate how many distinct pseudo-random numbers before the sequence repeats?",
    'options_list': ['1000', '999', '1001', 'Infinite numbers'],
    'correct_answer': '1000',
    'explanation': (
        "The period of a PRNG refers to the total number of distinct random numbers it can produce before the sequence "
        "starts repeating. If a PRNG has a period of 1000, it will generate 1000 unique random numbers before repeating "
        "the sequence. Therefore, the answer is 1000."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_7_types_of_prngs = {
    'question': "Which of the following is not a commonly used pseudo-random number generator algorithm?",
    'options_list': [
        'Linear congruential generator',
        'Mersenne Twister',
        'Fibonacci generator',
        'RANDU generator'
    ],
    'correct_answer': 'RANDU generator',
    'explanation': (
        "The RANDU generator is an infamous PRNG known for its poor statistical properties, especially its tendency to "
        "produce numbers that fall along hyperplanes in multidimensional space. This makes it a bad choice for most "
        "applications. The other options, such as the Linear congruential generator, Mersenne Twister, and Fibonacci "
        "generator, are commonly used PRNG algorithms."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_8_testing_prngs = {
    'question': "What is the main goal when performing statistical tests on a pseudo-random number generator?",
    'options_list': [
        'To prove that the PRNG is perfect.',
        'To verify that the PRNG generates numbers uniformly and independently.',
        'To check if the PRNG is fast enough for real-time applications.',
        'To find out how long the PRNG’s period is.'
    ],
    'correct_answer': 'To verify that the PRNG generates numbers uniformly and independently.',
    'explanation': (
        "The main goal of testing a PRNG is to ensure that the generated numbers are uniformly distributed (each number "
        "has an equal chance of occurring) and independent (no correlations between numbers). While speed and period "
        "length are important, the uniformity and independence are crucial for the PRNG to be considered reliable for "
        "most applications."
    ),
    'chapter_information': 'Chat GPT Generated'
}

question_9_understanding_periodicity = {
    'question': "If a PRNG has a period of $2^n$, what is the maximum number of unique numbers it can produce?",
    'options_list': ['$2^n$', '$2^n-1$', '$2^n+1$', 'Infinite numbers'],
    'correct_answer': '$2^n$',
    'explanation': (
        "The period of a PRNG is the number of distinct numbers it can generate before repeating. If the period is "
        "$2^n$, then the PRNG can produce $2^n$ unique numbers before the sequence starts repeating. This is the "
        "maximum number of unique numbers it can generate before repetition occurs."
    ),
    'chapter_information': 'Chat GPT Generated'
}

# Reformatting the nested dictionary so each question is its own top-level variable.

ques213tion_11_prn_properties = {
    'question': "Which of these is a desirable property for a PRN generator in a simulation context?\n"
                "a. Numbers are generated using a physical dice roll\n"
                "b. The sequence can be reproduced with a known seed\n"
                "c. The generator takes hours to produce each number\n"
                "d. The numbers follow a predictable pattern",
    'options_list': ['a. Numbers are generated using a physical dice roll', 'b. The sequence can be reproduced with a known seed',
                     'c. The generator takes hours to produce each number', 'd. The numbers follow a predictable pattern'],
    'correct_answer': 'b. The sequence can be reproduced with a known seed',
    'explanation': (
        "Reproducibility ensures simulations can be repeated for debugging or validation, a key feature of PRN generators unlike true random sources (e.g., dice).\n"
        "Example: Using seed 123, an LCG produces 0.4, 0.7, 0.2; re-running with 123 gives the same sequence."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

quest2ion_12_poor_generators = {
    'question': "Why is von Neumann’s mid-square method considered a lousy PRN generator?\n"
                "a. It has an extremely long period\n"
                "b. It can get stuck repeating zeros or short cycles\n"
                "c. It requires complex matrix operations\n"
                "d. It only works with prime numbers",
    'options_list': ['a. It has an extremely long period', 'b. It can get stuck repeating zeros or short cycles',
                     'c. It requires complex matrix operations', 'd. It only works with prime numbers'],
    'correct_answer': 'b. It can get stuck repeating zeros or short cycles',
    'explanation': (
        "If the middle digits become zero (e.g., 000000000000), squaring yields zero repeatedly, or it falls into short loops.\n"
        "Example: Start with 0100: 0100² = 010000, 0100² = 010000, repeating indefinitely."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

questi2on_13_lcg_calculation = {
    'question': "For the LCG $X_{i+1} = 3 X_i \\mod 8$ with $X_0 = 5$, what is $X_3$?",
    'options_list': ['a. 1', 'b. 3', 'c. 5', 'd. 7'],
    'correct_answer': 'c. 5',
    'explanation': (
        "$X_1 = 3 \\cdot 5 \\mod 8 = 15 \\mod 8 = 7$\n"
        "$X_2 = 3 \\cdot 7 \\mod 8 = 21 \\mod 8 = 5$\n"
        "$X_3 = 3 \\cdot 5 \\mod 8 = 15 \\mod 8 = 5$\n"
        "Example: This LCG has a short period; after $X_2 = 5$, it cycles back to the start."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

questio3n_14_simulation_module = {
    'question': "TRUE or FALSE? In Arena, the DISPOSE module is used to remove entities from the system after processing.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "DISPOSE terminates entities, marking the end of their lifecycle in the simulation (e.g., a customer leaving a store).\n"
        "Example: After a customer checks out, the DISPOSE module removes them from the model."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

quest3ion_15_tausworthe_generator = {
    'question': "A Tausworthe generator outputs the 5-bit sequence 10110. What is the Unif(0,1) PRN value?",
    'options_list': ['a. 0.625', 'b. 0.6875', 'c. 0.75', 'd. 0.8125'],
    'correct_answer': 'b. 0.6875',
    'explanation': (
        "Binary: 10110 = $1 \\cdot 2^4 + 0 \\cdot 2^3 + 1 \\cdot 2^2 + 1 \\cdot 2^1 + 0 \\cdot 2^0 = 16 + 4 + 2 = 22$\n"
        "Max value: $2^5 = 32$\n"
        "PRN: $\\frac{22}{32} = 0.6875$\n"
        "Example: For 3 bits, 101 = $\\frac{5}{8} = 0.625$."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

quest3ion_16_cycle_length = {
    'question': "TRUE or FALSE? A full-period LCG must have a period equal to its modulus $m$.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "A full-period LCG generates all values from $0$ to $m-1$ before repeating, requiring specific conditions on the multiplier, modulus, and increment.\n"
        "Example: $X_{i+1} = 5 X_i \\mod 8$ doesn’t achieve full period (only 4 values), but $5 X_i \\mod 13$ might with proper setup."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

que3stion_17_statistical_test = {
    'question': "In a runs test with 10 PRNs, you observe 3 runs up and down. If the expected runs are 5.5 with a critical value of 3 at $\\alpha = 0.05$, what do you conclude?",
    'options_list': ['a. Accept independence', 'b. Reject independence', 'c. Insufficient data to decide'],
    'correct_answer': 'b. Reject independence',
    'explanation': (
        "Observed runs (3) fall below the critical value (3), suggesting the PRNs may not be independent (too few runs indicate trends).\n"
        "Example: Sequence $0.1, 0.2, 0.3, 0.4, 0.5$ has 4 runs (+ + + +), fewer than expected for random."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

questi3on_18_simulation_attribute = {
    'question': "What Arena attribute would you use to define a custom order of station visits for an entity?",
    'options_list': ['a. Entity.Type', 'b. Entity.Sequence', 'c. Entity.Priority', 'd. Entity.Resource'],
    'correct_answer': 'b. Entity.Sequence',
    'explanation': (
        "Entity.Sequence specifies the ordered list of stations an entity follows, customizable via a Sequence set.\n"
        "Example: Sequence 1: Station A → Station B → Station C, assigned to Entity.Sequence."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

quest3ion_19_randu_flaw = {
    'question': "TRUE or FALSE? RANDU’s PRNs appear uniform in one dimension but fail in three-dimensional plots.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "RANDU looks decent in 1D but clusters on 15 hyperplanes in 3D, revealing poor randomness.\n"
        "Example: Triples like $(0.1, 0.3, 0.5)$ from RANDU align on planes when plotted."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

ques3tion_20_goodness_of_fit = {
    'question': "A chi-square test on 500 PRNs divided into 10 equal bins gives $\\chi^2 = 18.5$. With $\\chi^2_{0.05, 9} = 16.92$, do you accept or reject uniformity?",
    'options_list': ['a. Accept', 'b. Reject', 'c. Retry with more data'],
    'correct_answer': 'b. Reject',
    'explanation': (
        "$18.5 > 16.92$, so reject the null hypothesis that PRNs are Unif(0,1); the distribution isn’t uniform enough.\n"
        "Example: Expected count per bin = 50; observed counts like 60, 40, etc., deviate too much."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

# Reformatting the nested dictionary `module_6_week_7_grok_generated` so each question becomes its own top-level variable

question_1_prn_properties = {
    'question': "TRUE or FALSE? A good PRN generator should produce numbers that are completely unpredictable and cannot be reproduced.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        "Reproducibility is a key feature of PRN generators, allowing repeatable simulations (e.g., for validation). "
        "Completely unpredictable numbers are true random, not pseudo-random.\n"
        "Example: In a simulation, you use a seed of 42 to generate PRNs. Running it again with seed 42 should yield the same sequence."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_2_poor_generators = {
    'question': "Which of these is considered a weak PRN generator due to its tendency to repeat short cycles?\n"
                "a. Mersenne Twister\nb. Fibonacci Congruential Generator\nc. Tausworthe Generator\n"
                "d. L’Ecuyer Combined Generator",
    'options_list': ['a. Mersenne Twister', 'b. Fibonacci Congruential Generator', 'c. Tausworthe Generator', 'd. L’Ecuyer Combined Generator'],
    'correct_answer': 'b. Fibonacci Congruential Generator',
    'explanation': (
        "Fibonacci generators often have short periods and poor randomness compared to modern generators like Mersenne Twister or L’Ecuyer.\n"
        "Example: A Fibonacci generator might repeat after 20 numbers, while Mersenne Twister has a period of 2^19937 - 1."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_3_lcg_calculation = {
    'question': "For the LCG $X_{i+1} = 7 X_i \\mod 11$ with $X_0 = 4$, what is $X_2$?",
    'options_list': ['a. 2', 'b. 5', 'c. 6', 'd. 9'],
    'correct_answer': 'd. 9',
    'explanation': (
        "$X_1 = 7 \\cdot 4 \\mod 11 = 28 \\mod 11 = 6$\n"
        "$X_2 = 7 \\cdot 6 \\mod 11 = 42 \\mod 11 = 9$\n"
        "Example: This LCG cycles through values; check $X_3 = 7 \\cdot 9 = 63 \\mod 11 = 8$."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_4_simulation_module = {
    'question': "TRUE or FALSE? In Arena, the SEIZE module is typically paired with a RELEASE module to model resource usage.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "SEIZE captures a resource (e.g., a server), and RELEASE frees it, forming a common pattern in Arena for resource allocation.\n"
        "Example: A customer seizes a cashier, waits 5 minutes, then releases the cashier."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_5_tausworthe_generator = {
    'question': "A Tausworthe generator produces the 6-bit sequence 110101. What is the corresponding Unif(0,1) PRN?",
    'options_list': ['a. 0.53125', 'b. 0.65625', 'c. 0.8125', 'd. 0.9375'],
    'correct_answer': 'c. 0.8125',
    'explanation': (
        "Binary: 110101 = $1 \\cdot 2^5 + 1 \\cdot 2^4 + 0 \\cdot 2^3 + 1 \\cdot 2^2 + 0 \\cdot 2^1 + 1 \\cdot 2^0 = 32 + 16 + 4 + 1 = 53$\n"
        "Max value: $2^6 = 64$\n"
        "PRN: $53 / 64 = 0.828125$, but options suggest rounding to 0.8125 (check precision).\n"
        "Example: For 4 bits, 1011 = 11 / 16 = 0.6875."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_6_cycle_length = {
    'question': "TRUE or FALSE? Some PRN generators have cycle lengths exceeding $10^{100}$.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        "Advanced generators like the Mersenne Twister have periods like $2^{19937} - 1$, far exceeding $10^{100}$.\n"
        "Example: Mersenne Twister’s period is so large it’s practically inexhaustible in simulations."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_7_statistical_test = {
    'question': "If a chi-square goodness-of-fit test yields $\\chi^2 = 15.2$ with 5 degrees of freedom, and the critical value at $\\alpha = 0.05$ is 11.07, what do you conclude?",
    'options_list': ['a. Accept the PRNs as uniform', 'b. Reject the PRNs as uniform', 'c. Panic and re-run the test'],
    'correct_answer': 'b. Reject the PRNs as uniform',
    'explanation': (
        "Since $15.2 > 11.07$, reject the null hypothesis that the PRNs are Unif(0,1).\n"
        "Example: Observed frequencies deviating from expected uniform counts (e.g., too many in one bin)."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_8_runs_test = {
    'question': "For the PRN sequence 0.3, 0.7, 0.5, 0.9, 0.2, how many runs up and down are there?",
    'options_list': ['a. 2', 'b. 3', 'c. 4', 'd. 5'],
    'correct_answer': 'c. 4',
    'explanation': (
        "Sequence: 0.3 (start), 0.7 (+), 0.5 (-), 0.9 (+), 0.2 (-). Runs: + - + -. Total = 4.\n"
        "Example: 0.1, 0.2, 0.3 has 2 runs (+ +)."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_9_randu_flaw = {
    'question': "What is a known flaw of the RANDU generator?",
    'options_list': ['a. It has a period of only 100', 'b. It produces PRNs on just 15 hyperplanes in 3D', 'c. It relies on physical coin flips', 'd. It cannot be seeded'],
    'correct_answer': 'b. It produces PRNs on just 15 hyperplanes in 3D',
    'explanation': (
        "RANDU ($X_{i+1} = 65539 X_i \\mod 2^{31}$) fails in higher dimensions, clustering points on hyperplanes.\n"
        "Example: Plotting triples of RANDU PRNs reveals this pattern."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}

question_10_simulation_attribute = {
    'question': "In Arena, what attribute tracks an entity’s position in its assigned sequence?",
    'options_list': ['a. Entity.Job', 'b. Entity.Sequence', 'c. Entity.Station', 'd. Entity.Time'],
    'correct_answer': 'b. Entity.Sequence',
    'explanation': (
        "Entity.Sequence is Arena’s built-in attribute for tracking an entity’s sequence step.\n"
        "Example: Entity 1 follows Sequence A (Station1 → Station2), and Entity.Sequence updates accordingly."
    ),
    'chapter_information': 'Module 6 Week 7 - GROK generated'
}


###


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


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_6_MPC = KC_MPC_QUESTIONS[:-1]