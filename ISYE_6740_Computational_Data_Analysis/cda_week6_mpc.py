lesson_6_kde_question_1 = {
    'question': "What is the most critical factor that influences the performance of Kernel Density Estimation (KDE)?",
    'options_list': [
        "A) Choice of kernel function",
        "B) The number of data points used in estimation",
        "C) Kernel bandwidth",
        "D) The use of parametric methods alongside KDE"
    ],
    'correct_answer': 'C',
    'explanation': "The kernel bandwidth is crucial because it controls the smoothness of the density estimate, directly impacting the result.",
    'chapter_information': 'Lesson 6: Kernel Density Estimation (KDE)'
}

lesson_6_kde_question_2 = {
    'question': "Which of the following statements about Silverman's Rule of Thumb for bandwidth selection is correct?",
    'options_list': [
        "A) The optimal bandwidth is inversely proportional to the square root of the sample size.",
        "B) The optimal bandwidth increases as the number of data points increases.",
        "C) The rule of thumb bandwidth for a Gaussian kernel is 1.06×σ×m^(-1/5), where σ is the standard deviation of the data.",
        "D) Silverman's Rule of Thumb only applies to parametric density estimation methods."
    ],
    'correct_answer': 'C',
    'explanation': "Silverman's rule of thumb is commonly used to estimate an optimal bandwidth, especially for Gaussian kernels.",
    'chapter_information': 'Lesson 6: Kernel Density Estimation (KDE)'
}

lesson_6_kde_question_3 = {
    'question': "Which of the following is NOT a common choice for the kernel function used in KDE?",
    'options_list': [
        "A) Gaussian kernel",
        "B) Cosine kernel",
        "C) Exponential kernel",
        "D) Logarithmic kernel"
    ],
    'correct_answer': 'D',
    'explanation': "Logarithmic kernels are not commonly used in KDE; Gaussian, Cosine, and Exponential kernels are more typical choices.",
    'chapter_information': 'Lesson 6: Kernel Density Estimation (KDE)'
}

lesson_6_kde_question_4 = {
    'question': "In KDE, if the bandwidth is too large, what will be the most likely outcome?",
    'options_list': [
        "A) The estimate will have too many sharp peaks and valleys, making the density noisy.",
        "B) The estimate will be too smooth, potentially missing important modes in the distribution.",
        "C) The estimate will overfit the data, capturing all individual data points.",
        "D) The estimate will collapse into a uniform distribution over the range of the data."
    ],
    'correct_answer': 'B',
    'explanation': "If the bandwidth is too large, the KDE will be overly smooth, leading to the loss of important features in the distribution.",
    'chapter_information': 'Lesson 6: Kernel Density Estimation (KDE)'
}

lesson_6_density_estimation_tf_question_1 = {
    'question': "True or False: In the context of density estimation, parametric models like Gaussian distributions assume a fixed form for the distribution and estimate a finite number of parameters.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Parametric models assume a fixed form for the distribution and estimate parameters like the mean and covariance in a Gaussian model.",
    'chapter_information': 'Lesson 6: Density Estimation'
}

lesson_6_density_estimation_tf_question_2 = {
    'question': "True or False: A major limitation of non-parametric methods like KDE is that they require fewer assumptions about the data but often require more memory to store all data points.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "KDE is flexible because it does not assume a specific form for the distribution but requires storing all data points to evaluate the density function.",
    'chapter_information': 'Lesson 6: Density Estimation'
}

lesson_6_density_estimation_tf_question_3 = {
    'question': "True or False: In Kernel Density Estimation (KDE), the bandwidth parameter $h$ controls the smoothness of the estimated density, with larger bandwidths leading to noisier density estimates.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Larger bandwidths lead to smoother density estimates, while smaller bandwidths make the estimate noisier and more sensitive to individual data points.",
    'chapter_information': 'Lesson 6: Density Estimation'
}

lesson_6_density_estimation_tf_question_4 = {
    'question': "True or False: The covariance matrix in a multivariate Gaussian distribution must have all its eigenvalues greater than or equal to zero for the matrix to be valid.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The covariance matrix must be positive semi-definite, meaning all its eigenvalues must be non-negative.",
    'chapter_information': 'Lesson 6: Multivariate Gaussian Distribution'
}

lesson_6_density_estimation_tf_question_5 = {
    'question': "True or False: In a probabilistic graphical model (PGM), a directed edge between two variables means that they are conditionally independent of each other given the state of all other variables.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "A directed edge represents conditional dependence, not independence, between variables.",
    'chapter_information': 'Lesson 6: Probabilistic Graphical Models (PGMs)'
}

lesson_6_density_estimation_tf_question_6 = {
    'question': "True or False: One advantage of using maximum likelihood estimation (MLE) is that maximizing the log-likelihood rather than the likelihood simplifies the optimization problem, as it transforms products into sums.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Maximizing the log-likelihood makes the optimization problem easier to solve by turning products into sums, which are easier to handle in gradient-based methods.",
    'chapter_information': 'Lesson 6: Maximum Likelihood Estimation (MLE)'
}

lesson_6_mle_tf_question_1 = {
    'question': "True or False: In the Bernoulli coin flip example, the log-likelihood function is maximized when the parameter $\\theta$ is equal to the proportion of heads observed in the data.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The MLE for $\\theta$ is the ratio of the number of heads to the total number of tosses.",
    'chapter_information': 'Lesson 6: Maximum Likelihood Estimation (MLE)'
}

lesson_6_mle_tf_question_2 = {
    'question': "True or False: The MLE for the mean $\\mu$ in a Gaussian distribution is the median of the data points.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The MLE for $\\mu$ is the arithmetic mean, not the median.",
    'chapter_information': 'Lesson 6: Maximum Likelihood Estimation (MLE)'
}

lesson_6_mle_tf_question_3 = {
    'question': "True or False: In the Gaussian MLE, the log-likelihood function includes a term $\\log(2\\pi\\sigma^2)$, which is independent of the observed data and can be ignored during optimization.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The term $\\log(2\\pi\\sigma^2)$ appears in the log-likelihood but does not depend on the data, so it can be ignored when optimizing with respect to $\\mu$ and $\\sigma^2$.",
    'chapter_information': 'Lesson 6: Maximum Likelihood Estimation (MLE)'
}

lesson_6_mle_tf_question_4 = {
    'question': "True or False: The MLE for the variance $\\sigma^2$ in a Gaussian distribution divides by $m - 1$ to account for the degrees of freedom, ensuring an unbiased estimate.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The MLE for $\\sigma^2$ divides by $m$, not $m - 1$, because it is derived from the likelihood function, which does not include a correction for bias.",
    'chapter_information': 'Lesson 6: Maximum Likelihood Estimation (MLE)'
}

lesson_6_mle_tf_question_5 = {
    'question': "True or False: In Maximum Likelihood Estimation, taking the logarithm of the likelihood function does not change the location of the maximum, but it simplifies the computation of the derivative.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The logarithm is a monotonic function, so taking the log does not change the location of the maximum but simplifies differentiation and optimization.",
    'chapter_information': 'Lesson 6: Maximum Likelihood Estimation (MLE)'
}

lesson_6_mle_tf_question_6 = {
    'question': "True or False: The MLE for the probability $\\theta$ in a biased coin example is calculated by minimizing the squared error between observed heads and predicted heads.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "MLE maximizes the likelihood of the observed data, not the squared error.",
    'chapter_information': 'Lesson 6: Maximum Likelihood Estimation (MLE)'
}

esl_ii_kde_tf_question_1 = {
    'question': "True or False: In Kernel Density Estimation, the Gaussian kernel is preferred because it counts all observations equally, regardless of their distance from the target point $x_0$.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The Gaussian kernel assigns higher weights to observations closer to $x_0$, so it does not count all observations equally.",
    'chapter_information': 'ESL II: Kernel Density Estimation'
}

esl_ii_kde_tf_question_2 = {
    'question': "True or False: The Parzen density estimate smooths the empirical distribution by adding independent Gaussian noise to each observation.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The Parzen estimate smooths the empirical distribution by adding Gaussian noise to each observation, making the estimate less jumpy.",
    'chapter_information': 'ESL II: Kernel Density Estimation'
}

esl_ii_kde_tf_question_3 = {
    'question': "True or False: When using Kernel Density Estimation for classification, the posterior probabilities are derived by applying kernel density estimates to different class distributions and then normalizing the results.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Posterior probabilities are derived by applying KDE to different class distributions and then normalizing to form the posterior estimate.",
    'chapter_information': 'ESL II: Kernel Density Estimation'
}

esl_ii_kde_tf_question_4 = {
    'question': "True or False: In the equation $\\hat{f}_X(x_0) = \\frac{1}{N(2\\lambda^2\\pi)^{p/2}} \\sum_{i=1}^{N} e^{-\\frac{1}{2}(\\frac{||x_i - x_0||}{\\lambda})^2}$, the exponent term $-\\frac{1}{2}(\\frac{||x_i - x_0||}{\\lambda})^2$ reflects the similarity between $x_0$ and the observed data points $x_i$.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The exponent term in the Gaussian product kernel reflects the similarity between $x_0$ and the observed data points, with smaller distances resulting in larger exponent values.",
    'chapter_information': 'ESL II: Kernel Density Estimation'
}

esl_ii_kde_tf_question_5 = {
    'question': "True or False: In the right panel of Figure 6.14, the posterior probabilities for CHD are estimated by fitting a uniform kernel to the systolic blood pressure data.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The posterior probabilities for CHD are estimated using a Gaussian kernel, not a uniform kernel.",
    'chapter_information': 'ESL II: Kernel Density Estimation'
}

esl_ii_kde_tf_question_6 = {
    'question': "True or False: The Gaussian product kernel used for KDE in higher dimensions is a direct extension of the one-dimensional Gaussian kernel, applied separately to each dimension.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The Gaussian product kernel is a direct extension of the one-dimensional Gaussian kernel and applies independently to each dimension in multi-dimensional data.",
    'chapter_information': 'ESL II: Kernel Density Estimation'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_6_MPC = KC_MPC_QUESTIONS[:-1]
