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



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

SIM_MODULE_6_MPC = KC_MPC_QUESTIONS[:-1]