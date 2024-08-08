

kc2_question_13_3_1 = {
    'question': "If the time between customer arrivals to a restaurant at lunchtime fits the exponential distribution, then which of the following is true?",
    'options_list': [
        'The number of arrivals per unit time follows the Weibull distribution',
        'The number of arrivals per unit time follows the Poisson distribution'
    ],
    'correct_answer': 'The number of arrivals per unit time follows the Poisson distribution',
    'explanation': "If the interarrival times are exponentially distributed, then the count of arrivals in any given time period follows the Poisson distribution.",
    'chapter_information': 'Week 13: Probability-Based Models / Poisson, Exponential and Weibull Distributions'
}

kc2_question_13_3_2 = {
    'question': "What is the difference between the interpretations of the geometric and Weibull distributions?",
    'options_list': [
        'The geometric distribution models how many tries it takes for something to happen, while the Weibull distribution models how long it takes',
        'The Weibull distribution models how many tries it takes for something to happen, while the geometric distribution models how long it takes'
    ],
    'correct_answer': 'The geometric distribution models how many tries it takes for something to happen, while the Weibull distribution models how long it takes',
    'explanation': "The geometric distribution is discrete and models the number of trials until the first success. The Weibull distribution is continuous and can model time until an event occurs.",
    'chapter_information': 'Week 13: Probability-Based Models / Poisson, Exponential and Weibull Distributions'
}

kc2_question_13_5 = {
    'question': "Which of these is a queuing model not appropriate for?",
    'options_list': [
        'Determining the average wait time on a customer service hotline',
        'Estimating the length of the checkout lines at a grocery store',
        'Predicting the number of customers who will come to a restaurant tomorrow'
    ],
    'correct_answer': 'Predicting the number of customers who will come to a restaurant tomorrow',
    'explanation': "Queuing models are designed to handle scenarios involving waiting lines and service processes, not predicting total arrivals without a context of waiting or queue formation.",
    'chapter_information': 'Week 13: Probability-Based Models / Queuing'
}

kc2_question_13_6_1 = {
    'question': "Why should a stochastic simulation be run many times?",
    'options_list': [
        'To verify that the same thing happens each time',
        'One random outcome might not be representative of system performance in the range of different situations that could arise'
    ],
    'correct_answer': 'One random outcome might not be representative of system performance in the range of different situations that could arise',
    'explanation': "Running a stochastic simulation multiple times allows for the assessment of system performance across a variety of possible scenarios, reflecting the inherent randomness and variability.",
    'chapter_information': 'Week 13: Probability-Based Models / Simulation Basics'
}

kc2_question_13_6_2 = {
    'question': "Why is it important to validate a simulation by comparing it to real data as much as possible?",
    'options_list': [
        'If the simulation isn’t a good reflection of reality, then any insights we gain from studying the simulation might not be applicable in reality'
    ],
    'correct_answer': 'If the simulation isn’t a good reflection of reality, then any insights we gain from studying the simulation might not be applicable in reality',
    'explanation': "Validation ensures that the simulation accurately represents real-world conditions, which is crucial for the reliability and applicability of the insights derived from the simulation.",
    'chapter_information': 'Week 13: Probability-Based Models / Simulation Basics'
}

kc1_gpt_question_13_3 = {
    'question': "(GPT generated) What distribution best describes the length of time a customer spends waiting on hold with customer service before being connected to an agent?",
    'options_list': [
        'Binomial',
        'Exponential',
        'Geometric',
        'Poisson'
    ],
    'correct_answer': 'Exponential',
    'explanation': "The exponential distribution is commonly used to model the time between occurrences in a Poisson process, such as waiting times.",
    'chapter_information': 'Chapter 13: Probability-Based Models'
}

kc1_gpt_question_13_4 = {
    'question': "(GPT generated) If you're modeling the occurrence of rare natural events in a given year, which distribution would be the most suitable?",
    'options_list': [
        'Binomial',
        'Exponential',
        'Geometric',
        'Poisson'
    ],
    'correct_answer': 'Poisson',
    'explanation': "The Poisson distribution is well-suited for modeling the count of randomly occurring rare events over a specified period of time or in a specified area.",
    'chapter_information': 'Chapter 13: Probability-Based Models'
}

kc11__gpt_question_11_4 = {
    'question': "(GPT generated) Which formula represents the objective of Ridge Regression?",
    'options_list': [
        'Minimize: ∑(yi−∑βjxij)^2 subject to ∑|βj|≤t',
        'Minimize: ∑(yi−∑βjxij)^2 + λ1∑|βj| + λ2∑βj^2',
        'Minimize: ∑(yi−∑βjxij)^22 + λ∑βj^2',
        'Minimize: ∑(yi−∑βjxij)^2 + λ∑βj'
    ],
    'correct_answer': 'Minimize: ∑(yi−∑βjxij)^2 + λ∑βj^2',
    'explanation': "Ridge Regression aims to minimize the sum of squared residuals with a penalty on the size of the coefficients, controlled by λ, to avoid overfitting.",
    'chapter_information': 'Chapter 11: Variable Selection'
}

kc11__gpt_question_11_5 = {
    'question': "(GPT generated) Which variable selection method combines both Lasso and Ridge approaches?",
    'options_list': [
        'Forward Selection',
        'Backward Elimination',
        'Stepwise Regression',
        'Elastic Net'
    ],
    'correct_answer': 'Elastic Net',
    'explanation': "Elastic Net is a variable selection method that combines the L1 penalty of Lasso for sparsity and the L2 penalty of Ridge for coefficient shrinkage.",
    'chapter_information': 'Chapter 11: Variable Selection'
}

kc11__gpt_question_11_6 = {
    'question': "(GPT generated) In Ridge Regression, what does the tuning parameter λ control?",
    'options_list': [
        'The size of coefficients.',
        'The sum of the absolute values of the coefficients.',
        'The number of factors in the model.',
        'The p-value thresholds.'
    ],
    'correct_answer': 'The size of coefficients.',
    'explanation': "In Ridge Regression, the tuning parameter λ controls the extent of shrinkage applied to the coefficients; higher values of λ lead to greater shrinkage.",
    'chapter_information': 'Chapter 11: Variable Selection'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
