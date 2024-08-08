kc11_question_11_1 = {
    'question': "Building simpler models with fewer factors helps avoid which problems?",
    'options_list': [
        'Overfitting',
        'Low prediction quality',
        'Bias in the most important factors',
        'Difficulty of interpretation'
    ],
    'correct_answer': 'Overfitting',
    'explanation': "Simpler models are less likely to fit the noise in the training data, which helps in avoiding overfitting. Overfitting occurs when a model learns the detail and noise in the training data to the extent that it negatively impacts the performance of the model on new data.",
    'chapter_information': 'Week 11: Variable Selection / Introduction to Variable Selection'
}

kc11_question_11_2 = {
    'question': "Which of these is a key difference between stepwise regression and lasso regression?",
    'options_list': [
        'Lasso regression requires the data to first be scaled',
        'Stepwise regression gives many models to choose from, while lasso gives just one'
    ],
    'correct_answer': 'Lasso regression requires the data to first be scaled',
    'explanation': "Lasso regression penalizes the absolute size of the coefficients, which means that without scaling, variables can be penalized more or less simply because of their scale. This is why data scaling is important in lasso regression to ensure that the penalty is applied uniformly across coefficients.",
    'chapter_information': 'Week 11: Variable Selection / Models for Variable Selection'
}

kc11_question_11_3 = {
    'question': "When two predictors are highly correlated, which of the following statements is true?",
    'options_list': [
        'Lasso regression will usually have positive coefficients for both predictors',
        'Ridge regression will usually have positive coefficients for both predictors'
    ],
    'correct_answer': 'Ridge regression will usually have positive coefficients for both predictors',
    'explanation': "Ridge regression tends to shrink the coefficients of correlated predictors towards each other, which means they'll both have small but non-zero coefficients. This is a result of ridge regression's L2 penalty, which penalizes the square of coefficients and tends to keep all variables in the model with their effects shrunk.",
    'chapter_information': 'Week 11: Variable Selection / Choosing a Variable Selection Model'
}

kc2_question_12_1 = {
    'question': "If we’re testing to see whether red cars sell for higher prices than blue cars, we need to account for the type and age of the cars in our data set. This is called",
    'options_list': [
        'Controlling',
        'Comparing',
        'Combining'
    ],
    'correct_answer': 'Controlling',
    'explanation': "We need to control for the effects of type and age to isolate the impact of the car's color on its selling price.",
    'chapter_information': 'Week 12: Introduction to Design of Experiments / Introduction to Design of Experiments'
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

WEEK_1_MPC = KC_MPC_QUESTIONS[:-1]
