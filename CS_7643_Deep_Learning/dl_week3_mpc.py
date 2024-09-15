

monzersaleh_optimization_question_1 = {
    'question': "What is the key reason for using deeper networks in neural network architecture?",
    'options_list': [
        'To increase the computational complexity of the model.',
        'To better reflect the compositional nature of the world and achieve parameter efficiency.',
        'To ensure that the model overfits to the training data.',
        'To reduce the number of parameters in the model.'
    ],
    'correct_answer': 'To better reflect the compositional nature of the world and achieve parameter efficiency.',
    'explanation': "Deeper networks are used because they can better reflect the compositional nature of the world, leading to parameter efficiency and the ability to model complex functions.",
    'chapter_information': 'Monzersaleh Notes on Neural Network Optimization'
}

monzersaleh_optimization_question_2 = {
    'question': "What is the main purpose of Batch Normalization in neural networks?",
    'options_list': [
        'To increase the training time by adding extra computation.',
        'To reduce the size of the model.',
        'To normalize the inputs of each layer, improving gradient flow and learning stability.',
        'To remove the need for regularization techniques.'
    ],
    'correct_answer': 'To normalize the inputs of each layer, improving gradient flow and learning stability.',
    'explanation': "Batch Normalization is used to normalize the inputs of each layer, which helps improve gradient flow, leading to more stable and faster learning.",
    'chapter_information': 'Monzersaleh Notes on Neural Network Optimization'
}

monzersaleh_optimization_question_3 = {
    'question': "Why is intelligent initialization of weights important in neural network training?",
    'options_list': [
        'It ensures that the model starts in the optimal solution.',
        'It prevents the network from ever reaching a local minima.',
        'It determines the activation statistics and affects gradient flow, crucial for effective learning.',
        'It makes the model more complex and harder to train.'
    ],
    'correct_answer': 'It determines the activation statistics and affects gradient flow, crucial for effective learning.',
    'explanation': "Intelligent initialization of weights is crucial because it determines the activation statistics and affects the gradient flow, which are both essential for effective learning.",
    'chapter_information': 'Monzersaleh Notes on Neural Network Optimization'
}

monzersaleh_optimization_question_4 = {
    'question': "What challenge does the ReLU activation function help address in deep learning models?",
    'options_list': [
        'It prevents the model from learning complex functions.',
        'It solves the problem of vanishing gradients by maintaining non-zero gradients during training.',
        'It reduces the computational complexity of the model to zero.',
        'It eliminates the need for any data pre-processing.'
    ],
    'correct_answer': 'It solves the problem of vanishing gradients by maintaining non-zero gradients during training.',
    'explanation': "ReLU activation function helps to solve the problem of vanishing gradients, which allows the network to maintain non-zero gradients during training, thus facilitating deeper models.",
    'chapter_information': 'Monzersaleh Notes on Neural Network Optimization'
}

monzersaleh_optimization_question_5 = {
    'question': "Which of the following is a popular adaptive learning rate optimization algorithm that combines the benefits of previous gradient-based methods?",
    'options_list': [
        'SGD with Momentum',
        'RMSProp',
        'Adam',
        'Nesterov Accelerated Gradient'
    ],
    'correct_answer': 'Adam',
    'explanation': "Adam is a popular optimization algorithm that combines the benefits of RMSProp and SGD with Momentum, making it widely used in deep learning.",
    'chapter_information': 'Monzersaleh Notes on Neural Network Optimization'
}


# lesson3_truefalse_question_1 = {
#     'question': "True or False: A neural network with more parameters than training examples is more likely to generalize better due to its larger capacity.",
#     'correct_answer': 'False',
#     'explanation': "Having more parameters than training examples increases the risk of overfitting, where the model memorizes the data instead of generalizing to new data.",
#     'chapter_information': 'Lesson 3 - Lecture Transcripts'
# }

# lesson3_truefalse_question_2 = {
#     'question': "True or False: Initializing neural network weights too close to zero can lead to poor learning performance due to vanishing gradients.",
#     'correct_answer': 'True',
#     'explanation': "When weights are initialized too close to zero, gradients may become very small during backpropagation, leading to slow learning or the vanishing gradient problem.",
#     'chapter_information': 'Lesson 3 - Lecture Transcripts'
# }

# lesson3_truefalse_question_3 = {
#     'question': "True or False: Adding depth to a neural network always leads to parameter efficiency, making it easier to learn any function.",
#     'correct_answer': 'False',
#     'explanation': "While adding depth can improve learning efficiency, it can also introduce challenges such as vanishing gradients, making deeper networks harder to train without careful design.",
#     'chapter_information': 'Lesson 3 - Lecture Transcripts'
# }

# lesson3_truefalse_question_4 = {
#     'question': "True or False: Regularization techniques like dropout are essential only when the model is overfitting and can be ignored otherwise.",
#     'correct_answer': 'False',
#     'explanation': "Dropout can improve model robustness and generalization even when overfitting is not obvious. It helps prevent co-adaptation of neurons, improving generalization.",
#     'chapter_information': 'Lesson 3 - Lecture Transcripts'
# }

# lesson3_truefalse_question_5 = {
#     'question': "True or False: Backpropagation can only be used with neural networks that have fully connected layers.",
#     'correct_answer': 'False',
#     'explanation': "Backpropagation can be applied to various architectures including convolutional and recurrent networks, not just fully connected layers.",
#     'chapter_information': 'Lesson 3 - Lecture Transcripts'
# }


# lesson3_truefalse_question_1 = {
#     'question': "True or False: The vanishing gradient problem occurs only during backpropagation through the non-linear layers and not through linear layers.",
#     'correct_answer': 'False',
#     'explanation': "While non-linear layers can exacerbate the vanishing gradient problem, it can also occur in linear layers, especially with improper weight initialization.",
#     'chapter_information': 'Lesson 3 - Second Lecture'
# }

# lesson3_truefalse_question_2 = {
#     'question': "True or False: Subgradients are only used when the activation function is piecewise linear, and they cannot be applied to non-differentiable points in non-linear functions like sigmoid or tanh.",
#     'correct_answer': 'False',
#     'explanation': "Subgradients can be used at non-differentiable points in functions like ReLU and other piecewise functions. They approximate the gradient at non-smooth points.",
#     'chapter_information': 'Lesson 3 - Second Lecture'
# }

lesson3_mpc_question_1 = {
    'question': "Which of the following statements is TRUE about non-linear activation functions?",
    'options_list': [
        "A) Sigmoid is often preferred over ReLU in deep learning due to its smoother gradient flow.",
        "B) Tanh provides a better balanced output range than ReLU but suffers from gradient saturation at the extremes.",
        "C) Leaky ReLU always outperforms standard ReLU in terms of gradient flow and model accuracy.",
        "D) The computational complexity of tanh is lower than that of ReLU, making it the preferred choice for deep networks."
    ],
    'correct_answer': 'B',
    'explanation': "Tanh is balanced and provides outputs between -1 and 1, but it suffers from vanishing gradients at the extremes, unlike ReLU.",
    'chapter_information': 'Lesson 3 - Second Lecture'
}

lesson3_mpc_question_2 = {
    'question': "Which of the following is FALSE regarding the vanishing gradient and exploding gradient problems?",
    'options_list': [
        "A) Both vanishing and exploding gradient problems can be addressed by using normalization techniques like batch normalization.",
        "B) Exploding gradients can occur when using activation functions with unbounded outputs like ReLU.",
        "C) The vanishing gradient problem is only significant in shallow networks with fewer layers.",
        "D) Proper initialization of weights can help reduce both vanishing and exploding gradient problems."
    ],
    'correct_answer': 'C',
    'explanation': "The vanishing gradient problem is more significant in deep networks, where gradients become progressively smaller as they backpropagate through many layers.",
    'chapter_information': 'Lesson 3 - Second Lecture'
}

lesson3_mpc_question_3 = {
    'question': "Which of the following does NOT contribute to improving gradient flow in a deep neural network?",
    'options_list': [
        "A) Using ReLU or Leaky ReLU activation functions.",
        "B) Proper weight initialization techniques.",
        "C) Adding more linear layers to the network architecture.",
        "D) Using batch normalization or other normalization techniques."
    ],
    'correct_answer': 'C',
    'explanation': "Adding more linear layers does not improve gradient flow. Non-linear activations, weight initialization, and normalization techniques are key to improving gradient flow.",
    'chapter_information': 'Lesson 3 - Second Lecture'
}

deep_learning_ch7_mpc_question_1 = {
    'question': "Which of the following statements about L1 regularization is NOT true?",
    'options_list': [
        "A) L1 regularization induces sparsity by driving some weights to zero.",
        "B) L1 regularization uses the absolute value of weights in the penalty term.",
        "C) The optimal solution for L1 regularization is always sparse, regardless of the value of \( \\alpha \\).",
        "D) L1 regularization can be interpreted as MAP inference with a Laplace prior."
    ],
    'correct_answer': 'C',
    'explanation': "L1 regularization induces sparsity only for large enough values of \( \\alpha \\). If \( \\alpha \\) is too small, the solution may not be sparse.",
    'chapter_information': 'Deep Learning Book Chapter 7.1'
}

# deep_learning_ch7_truefalse_question_1 = {
#     'question': "True or False: L1 regularization can be viewed as equivalent to maximum a posteriori (MAP) Bayesian inference with a Laplace prior over the weights.",
#     'correct_answer': 'True',
#     'explanation': "L1 regularization corresponds to the MAP inference using a Laplace prior on the weights, which induces sparsity.",
#     'chapter_information': 'Deep Learning Book Chapter 7.1'
# }

deep_learning_ch7_mpc_question_2 = {
    'question': "Which of the following describes the relationship between regularization and MAP inference in Bayesian terms?",
    'options_list': [
        "A) L2 regularization corresponds to a Laplace prior, while L1 regularization corresponds to a Gaussian prior.",
        "B) Both L1 and L2 regularization correspond to Gaussian priors.",
        "C) L1 regularization corresponds to a Laplace prior, while L2 regularization corresponds to a Gaussian prior.",
        "D) L2 regularization corresponds to a uniform prior, while L1 regularization corresponds to a Laplace prior."
    ],
    'correct_answer': 'C',
    'explanation': "L1 regularization corresponds to a Laplace prior, and L2 regularization corresponds to a Gaussian prior in the context of MAP inference.",
    'chapter_information': 'Deep Learning Book Chapter 7.1'
}

# deep_learning_ch7_mpc_question_3 = {
#     'question': "In the quadratic approximation of the L1-regularized objective function, the weight \( w_i \\) will be zero if:",
#     'options_list': [
#         "A) \( w^*_i \\leq \\alpha H_{i,i} \\)",
#         "B) \( w^*_i > \\alpha H_{i,i} \\)",
#         "C) \( \\alpha = 0 \\)",
#         "D) \( w^*_i \\neq 0 \\)"
#     ],
#     'correct_answer': 'A',
#     'explanation': "If \( w^*_i \\leq \\alpha H_{i,i} \\), the L1 penalty dominates, and the optimal value of \( w_i \\) is pushed to zero.",
#     'chapter_information': 'Deep Learning Book Chapter 7.1'
# }

deep_learning_ch7_mpc_question_3 = {
    'question': "In the quadratic approximation of the L1-regularized objective function, the weight $w_i$ will be zero if:",
    'options_list': [
        "A) $w^*_i \\leq \\alpha H_{i,i}$",
        "B) $w^*_i > \\alpha H_{i,i}$",
        "C) $\\alpha = 0$",
        "D) $w^*_i \\neq 0$"
    ],
    'correct_answer': 'A',
    'explanation': "If $w^*_i \\leq \\alpha H_{i,i}$, the L1 penalty dominates, and the optimal value of $w_i$ is pushed to zero.",
    'chapter_information': 'Deep Learning Book Chapter 7.1'
}


# deep_learning_ch7_truefalse_question_2 = {
#     'question': "True or False: Both L1 and L2 regularization result in sparse solutions where some parameters are exactly zero.",
#     'correct_answer': 'False',
#     'explanation': "Only L1 regularization results in sparse solutions where some parameters become exactly zero, while L2 regularization generally keeps all parameters nonzero.",
#     'chapter_information': 'Deep Learning Book Chapter 7.1'
# }



lesson3_truefalse_question_1 = {
    'question': "A neural network with more parameters than training examples is more likely to generalize better due to its larger capacity.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Having more parameters than training examples increases the risk of overfitting, where the model memorizes the data instead of generalizing to new data.",
    'chapter_information': 'Lesson 3 - Lecture Transcripts'
}

lesson3_truefalse_question_2 = {
    'question': "Initializing neural network weights too close to zero can lead to poor learning performance due to vanishing gradients.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "When weights are initialized too close to zero, gradients may become very small during backpropagation, leading to slow learning or the vanishing gradient problem.",
    'chapter_information': 'Lesson 3 - Lecture Transcripts'
}

lesson3_truefalse_question_3 = {
    'question': "Adding depth to a neural network always leads to parameter efficiency, making it easier to learn any function.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "While adding depth can improve learning efficiency, it can also introduce challenges such as vanishing gradients, making deeper networks harder to train without careful design.",
    'chapter_information': 'Lesson 3 - Lecture Transcripts'
}

lesson3_truefalse_question_4 = {
    'question': "Regularization techniques like dropout are essential only when the model is overfitting and can be ignored otherwise.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Dropout can improve model robustness and generalization even when overfitting is not obvious. It helps prevent co-adaptation of neurons, improving generalization.",
    'chapter_information': 'Lesson 3 - Lecture Transcripts'
}

lesson3_truefalse_question_5 = {
    'question': "Backpropagation can only be used with neural networks that have fully connected layers.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Backpropagation can be applied to various architectures including convolutional and recurrent networks, not just fully connected layers.",
    'chapter_information': 'Lesson 3 - Lecture Transcripts'
}

lesson3_truefalse_question_6 = {
    'question': "The vanishing gradient problem occurs only during backpropagation through the non-linear layers and not through linear layers.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "While non-linear layers can exacerbate the vanishing gradient problem, it can also occur in linear layers, especially with improper weight initialization.",
    'chapter_information': 'Lesson 3 - Second Lecture'
}

lesson3_truefalse_question_7 = {
    'question': "Subgradients are only used when the activation function is piecewise linear, and they cannot be applied to non-differentiable points in non-linear functions like sigmoid or tanh.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Subgradients can be used at non-differentiable points in functions like ReLU and other piecewise functions. They approximate the gradient at non-smooth points.",
    'chapter_information': 'Lesson 3 - Second Lecture'
}

lesson3_truefalse_question_1 = {
    'question': "The vanishing gradient problem occurs only during backpropagation through the non-linear layers and not through linear layers.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "While non-linear layers can exacerbate the vanishing gradient problem, it can also occur in linear layers, especially with improper weight initialization.",
    'chapter_information': 'Lesson 3 - Second Lecture'
}

lesson3_truefalse_question_2 = {
    'question': "Subgradients are only used when the activation function is piecewise linear, and they cannot be applied to non-differentiable points in non-linear functions like sigmoid or tanh.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Subgradients can be used at non-differentiable points in functions like ReLU and other piecewise functions. They approximate the gradient at non-smooth points.",
    'chapter_information': 'Lesson 3 - Second Lecture'
}

deep_learning_ch7_truefalse_question_1a = {
    'question': "L1 regularization can be viewed as equivalent to maximum a posteriori (MAP) Bayesian inference with a Laplace prior over the weights.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "L1 regularization corresponds to the MAP inference using a Laplace prior on the weights, which induces sparsity.",
    'chapter_information': 'Deep Learning Book Chapter 7.1'
}

deep_learning_ch7_truefalse_question_2a = {
    'question': "Both L1 and L2 regularization result in sparse solutions where some parameters are exactly zero.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Only L1 regularization results in sparse solutions where some parameters become exactly zero, while L2 regularization generally keeps all parameters nonzero.",
    'chapter_information': 'Deep Learning Book Chapter 7.1'
}


deep_learning_ch7_truefalse_question_1b = {
    'question': "True or False: Dataset augmentation can universally improve the performance of neural networks for all tasks, regardless of the type of transformation applied to the dataset.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "While dataset augmentation can improve performance in many tasks, not all transformations are beneficial. For example, rotating characters like 'b' and 'd' in an OCR task can lead to incorrect labels.",
    'chapter_information': 'Deep Learning Book Chapter 7.2-4'
}

deep_learning_ch7_truefalse_question_2b = {
    'question': "True or False: Injecting noise into the input of a neural network during training is considered a form of regularization that increases the model's robustness to noise in the input during test time.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Injecting noise during training can improve the model's robustness by forcing it to learn more stable features. This is also applied in methods like denoising autoencoders.",
    'chapter_information': 'Deep Learning Book Chapter 7.2-4'
}

deep_learning_ch7_truefalse_question_3b = {
    'question': "True or False: Out-of-plane rotations can be easily handled using simple geometric transformations in dataset augmentation for computer vision tasks.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Out-of-plane rotations are not simple geometric transformations and cannot be easily simulated in dataset augmentation for 2D input like images.",
    'chapter_information': 'Deep Learning Book Chapter 7.2-4'
}

deep_learning_ch7_mpc_question_1c = {
    'question': "Which of the following transformations should NOT be used for data augmentation in an optical character recognition (OCR) task?",
    'options_list': [
        "A) Translating the image a few pixels in different directions.",
        "B) Horizontally flipping the image.",
        "C) Adding random noise to the image.",
        "D) Slightly scaling the image."
    ],
    'correct_answer': 'B',
    'explanation': "In OCR tasks, horizontal flipping could result in the confusion between characters like 'b' and 'd,' and '6' and '9,' leading to incorrect classification.",
    'chapter_information': 'Deep Learning Book Chapter 7.2-4'
}

deep_learning_ch7_mpc_question_2c = {
    'question': "Which of the following is a reason why dataset augmentation improves generalization performance?",
    'options_list': [
        "A) It increases the effective size of the training data by providing diverse examples.",
        "B) It directly reduces the test error by injecting noise into the hidden layers.",
        "C) It guarantees that the network will generalize well on out-of-distribution data.",
        "D) It reduces the number of parameters in the model, simplifying the learning task."
    ],
    'correct_answer': 'A',
    'explanation': "Dataset augmentation increases the diversity of the data by generating new examples, effectively increasing the size of the training set.",
    'chapter_information': 'Deep Learning Book Chapter 7.2-4'
}

deep_learning_ch7_mpc_question_3c = {
    'question': "Which of the following is NOT a valid distinction between dataset augmentation and regularization techniques like dropout?",
    'options_list': [
        "A) Dataset augmentation alters the input data, while dropout alters the structure of the network during training.",
        "B) Dropout can be seen as a form of dataset augmentation at the level of hidden units.",
        "C) Dataset augmentation increases robustness to noise in the data, while dropout increases robustness by reducing overfitting.",
        "D) Dropout prevents co-adaptation of neurons, while dataset augmentation primarily combats variance in the input data."
    ],
    'correct_answer': 'C',
    'explanation': "While dataset augmentation introduces variability in the input, dropout addresses overfitting by ensuring that neurons don’t co-adapt during training. Both methods can enhance generalization.",
    'chapter_information': 'Deep Learning Book Chapter 7.2-4'
}


deep_learning_ch7_truefalse_question_4c = {
    'question': "True or False: In the eigenvector space of the Hessian matrix, gradient descent moves along the principal components in proportion to their corresponding eigenvalues.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "In the space of the eigenvectors of the Hessian matrix, gradient descent updates are influenced by the eigenvalues, with larger eigenvalues corresponding to larger updates along their respective directions.",
    'chapter_information': 'Deep Learning Book Chapter 7.4'
}

deep_learning_ch7_truefalse_question_5d = {
    'question': "True or False: Early stopping can be interpreted as a form of L2 regularization under a quadratic approximation of the objective function.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Under the quadratic approximation, early stopping can be shown to result in a similar effect to L2 regularization, as the trajectory length is limited, preventing overfitting.",
    'chapter_information': 'Deep Learning Book Chapter 7.4'
}

deep_learning_ch7_truefalse_question_6da = {
    'question': "True or False: If the eigenvalues $\\lambda_i$ of the Hessian matrix are very small, the number of iterations $\\tau$ in gradient descent has a linear relationship with the L2 regularization coefficient $\\alpha$.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "There is an inverse relationship between $\\tau$ and $\\alpha$, as $\\tau \\approx 1/(\\epsilon \\alpha)$ under the assumptions of small eigenvalues.",
    'chapter_information': 'Deep Learning Book Chapter 7.4'
}

deep_learning_ch7_mpc_question_4ds = {
    'question': "Which of the following best describes the relationship between the learning rate $\\epsilon$, the number of training iterations $\\tau$, and the L2 regularization parameter $\\alpha$ under the quadratic approximation of the objective function?",
    'options_list': [
        "A) $\\tau$ is directly proportional to $\\alpha$ and inversely proportional to $\\epsilon$.",
        "B) $\\alpha$ is inversely proportional to $\\tau \\epsilon$.",
        "C) $\\alpha$ is proportional to $\\epsilon \\tau$.",
        "D) $\\tau$ and $\\alpha$ are both directly proportional to $\\epsilon$."
    ],
    'correct_answer': 'B',
    'explanation': "Under the quadratic approximation, $\\alpha \\approx 1/(\\tau \\epsilon)$, meaning $\\alpha$ is inversely proportional to both $\\tau$ and $\\epsilon$.",
    'chapter_information': 'Deep Learning Book Chapter 7.4'
}

deep_learning_ch7_mpc_question_5dc = {
    'question': "In the context of gradient descent with L2 regularization and early stopping, which of the following is TRUE about the eigenvalue decomposition of the Hessian matrix?",
    'options_list': [
        "A) Directions corresponding to smaller eigenvalues are regularized less than those with larger eigenvalues.",
        "B) Directions with larger eigenvalues experience less regularization, resulting in faster learning.",
        "C) Eigenvalues have no effect on the trajectory of gradient descent under L2 regularization.",
        "D) All eigenvalues contribute equally to the regularization term in L2 regularization."
    ],
    'correct_answer': 'B',
    'explanation': "Directions with larger eigenvalues correspond to directions of higher curvature in the objective function, which leads to faster learning and less regularization.",
    'chapter_information': 'Deep Learning Book Chapter 7.4'
}

deep_learning_ch7_mpc_question_6dv = {
    'question': "Given the following relation $Q^T(w(\\tau) - w^*) = [I - (I - \\epsilon \\Lambda)^\\tau]Q^T w^*$, what does this equation represent?",
    'options_list': [
        "A) The relationship between the gradient of the loss function and the eigenvalue decomposition of the Hessian matrix.",
        "B) The trajectory of the parameter updates in gradient descent expressed in the eigenvector space of the Hessian matrix.",
        "C) The exact solution of the L2 regularized objective function after early stopping.",
        "D) The effect of weight decay on the convergence rate of gradient descent."
    ],
    'correct_answer': 'B',
    'explanation': "This equation shows the parameter trajectory in gradient descent when viewed in the space of the eigenvectors of the Hessian matrix.",
    'chapter_information': 'Deep Learning Book Chapter 7.4'
}

deep_learning_ch7_mpc_question_7df = {
    'question': "In the expression $(I - \\epsilon \\Lambda)^\\tau = ( \\Lambda + \\alpha I )^{-1} \\alpha$, what does this represent under the quadratic approximation of the objective function?",
    'options_list': [
        "A) The equivalence between L2 regularization and early stopping, where $\\alpha$ is the weight decay term.",
        "B) The condition under which the gradient converges to zero in the eigenvector space.",
        "C) The relation between the learning rate and the Hessian matrix for faster convergence.",
        "D) The optimal step size in gradient descent to avoid overfitting."
    ],
    'correct_answer': 'A',
    'explanation': "This expression represents the equivalence between early stopping and L2 regularization, where early stopping limits the trajectory length in a way similar to how L2 regularization constrains the weights.",
    'chapter_information': 'Deep Learning Book Chapter 7.4'
}

deep_learning_ch7_truefalse_question_7dg = {
    'question': "True or False: Dropout acts purely as a bagging technique for neural networks by training multiple models with independent weights.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "While dropout can be seen as an approximate form of bagging, it trains an ensemble of models that share hidden units, forcing each hidden unit to be robust in many contexts, unlike traditional independent model ensembles.",
    'chapter_information': 'Deep Learning Book Chapter 7.9-7.12'
}

deep_learning_ch7_truefalse_question_8dh = {
    'question': "True or False: Applying multiplicative noise to hidden units during training prevents neurons from simply scaling their weights to ignore the noise.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Multiplicative noise prevents neurons from scaling their activations arbitrarily high to ignore the noise, unlike additive noise, which could be bypassed by scaling.",
    'chapter_information': 'Deep Learning Book Chapter 7.9-7.12'
}

deep_learning_ch7_truefalse_question_9fg = {
    'question': "True or False: Batch normalization can act as a form of regularization, making dropout unnecessary in certain cases.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "While batch normalization's primary goal is to improve optimization, the noise it introduces can also act as regularization, and in some cases, it may make dropout unnecessary.",
    'chapter_information': 'Deep Learning Book Chapter 7.9-7.12'
}


deep_learning_ch7_mpc_question_8i8 = {
    'question': "Which of the following is NOT a reason why dropout enhances generalization in neural networks?",
    'options_list': [
        "A) It trains an ensemble of models where hidden units are swapped, ensuring robustness in different contexts.",
        "B) Dropout forces hidden units to encode redundant information, improving feature detection.",
        "C) Dropout applies noise to the input values, effectively masking key features like 'nose' in face detection tasks.",
        "D) It prevents hidden units from co-adapting too closely to each other."
    ],
    'correct_answer': 'C',
    'explanation': "Dropout applies noise to the hidden units, not to the input values, ensuring that important features are detected through multiple independent pathways.",
    'chapter_information': 'Deep Learning Book Chapter 7.9-7.12'
}

deep_learning_ch7_mpc_question_9i8 = {
    'question': "Which of the following best explains why multiplicative noise is more effective than additive noise for training neural networks with rectified linear units (ReLUs)?",
    'options_list': [
        "A) Additive noise makes ReLUs more likely to become saturated, leading to vanishing gradients.",
        "B) Additive noise can be bypassed by increasing the magnitude of activations, while multiplicative noise cannot.",
        "C) Multiplicative noise enhances the gradient flow through ReLU units, unlike additive noise.",
        "D) Additive noise directly modifies the weights, while multiplicative noise modifies only the activations."
    ],
    'correct_answer': 'B',
    'explanation': "Additive noise can be ignored by neurons simply increasing their activations, while multiplicative noise scales the activation itself and cannot be bypassed.",
    'chapter_information': 'Deep Learning Book Chapter 7.9-7.12'
}

deep_learning_ch7_mpc_question_10i8 = {
    'question': "Which of the following mathematical conditions explains the equivalence between dropout with Gaussian noise and Srivastava et al.'s method of multiplying the weights by $\\mu \\sim N(1, I)$?",
    'options_list': [
        "A) $E[\\mu] = 0$, making dropout a centering transformation.",
        "B) $E[\\mu] = 1$, ensuring the weights are scaled appropriately after dropout.",
        "C) $\\mu \\sim N(0, 1)$, which makes the method equivalent to dropout based on binary masks.",
        "D) Dropout is equivalent to using $\\mu \\sim N(1, 0)$, removing the need for further scaling."
    ],
    'correct_answer': 'B',
    'explanation': "Srivastava et al. demonstrated that multiplying the weights by $\\mu \\sim N(1, I)$ ensures $E[\\mu] = 1$, leading to appropriate weight scaling, similar to how dropout scales weights.",
    'chapter_information': 'Deep Learning Book Chapter 7.9-7.12'
}

deep_learning_ch7_mpc_question_118i = {
    'question': "In the context of dropout, what is the primary benefit of applying noise at the hidden unit level rather than the input level?",
    'options_list': [
        "A) It directly reduces the dimensionality of the input.",
        "B) It ensures that the destruction of features uses the model’s learned representations rather than raw input data.",
        "C) It decreases the size of the network, allowing for faster convergence.",
        "D) It makes backpropagation more efficient by reducing the gradient updates."
    ],
    'correct_answer': 'B',
    'explanation': "By applying noise at the hidden unit level, dropout destroys learned features rather than raw input data, forcing the model to learn more robust representations.",
    'chapter_information': 'Deep Learning Book Chapter 7.9-7.12'
}

deep_learning_ch7_truefalse_question_i10 = {
    'question': "True or False: Tangent propagation explicitly generates new input points to train the model on transformed versions of the data.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Tangent propagation analytically regularizes the model to resist perturbations in specific directions, without explicitly generating new input points, unlike dataset augmentation.",
    'chapter_information': 'Deep Learning Book Chapter 7.13'
}

deep_learning_ch7_truefalse_questioin_11 = {
    'question': "True or False: Tangent propagation works better with models based on rectified linear units (ReLUs) than with models based on sigmoid units, due to the ReLU’s ability to handle inﬁnitesimal perturbations effectively.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Tangent propagation struggles with ReLU-based models because they cannot shrink derivatives easily. Sigmoid and tanh units can shrink derivatives by saturating, making them better suited for tangent propagation.",
    'chapter_information': 'Deep Learning Book Chapter 7.13'
}

deep_learning_ch7_truefalse_iquestion_12 = {
    'question': "True or False: Adversarial training can be seen as the non-inﬁnitesimal version of double backpropagation.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Adversarial training is a non-inﬁnitesimal extension of double backprop, where the model is trained to produce the same output for small perturbations in all directions.",
    'chapter_information': 'Deep Learning Book Chapter 7.13'
}

deep_learning_ch7_mpc_question_12 = {
    'question': "Which of the following describes a key difference between tangent propagation and dataset augmentation?",
    'options_list': [
        "A) Tangent propagation works with larger transformations, while dataset augmentation is limited to inﬁnitesimal perturbations.",
        "B) Tangent propagation analytically regularizes against small perturbations, while dataset augmentation explicitly trains the model on new, transformed inputs.",
        "C) Dataset augmentation is better suited for models based on ReLU units, while tangent propagation works well for models based on rectified linear units.",
        "D) Tangent propagation applies random transformations to input data, whereas dataset augmentation uses fixed transformations."
    ],
    'correct_answer': 'B',
    'explanation': "Tangent propagation regularizes the model by analytically resisting small perturbations, while dataset augmentation creates new inputs through explicit transformations.",
    'chapter_information': 'Deep Learning Book Chapter 7.13'
}

deep_learning_ch7_mpc_question_13 = {
    'question': "What is a major limitation of tangent propagation when applied to models using rectified linear units (ReLU)?",
    'options_list': [
        "A) ReLU units saturate, preventing small derivatives.",
        "B) ReLU units can only shrink derivatives by turning off, making them ineffective for resisting small perturbations.",
        "C) ReLU units cannot handle inﬁnitesimal perturbations, resulting in large-scale output changes.",
        "D) ReLU units perform poorly under dataset augmentation but excel with tangent propagation."
    ],
    'correct_answer': 'B',
    'explanation': "ReLU units cannot shrink derivatives smoothly and can only handle perturbations by turning off or shrinking their weights, which limits their effectiveness in tangent propagation.",
    'chapter_information': 'Deep Learning Book Chapter 7.13'
}

deep_learning_ch7_mpc_question_14 = {
    'question': "Which of the following best describes the relationship between double backpropagation and adversarial training?",
    'options_list': [
        "A) Double backpropagation focuses on regularizing the model for large perturbations, while adversarial training focuses on small ones.",
        "B) Both methods focus on resisting small perturbations, but adversarial training explicitly finds nearby inputs to train the model on.",
        "C) Adversarial training is limited to a few transformations, while double backpropagation works with all types of perturbations.",
        "D) Double backpropagation trains on new input points, whereas adversarial training only trains on original inputs."
    ],
    'correct_answer': 'B',
    'explanation': "Both methods aim to regularize the model against small perturbations, but adversarial training explicitly searches for inputs near the original ones to train the model on.",
    'chapter_information': 'Deep Learning Book Chapter 7.13'
}

deep_learning_ch7_mpc_question_15 = {
    'question': "Which of the following is NOT true about the manifold tangent classifier?",
    'options_list': [
        "A) It eliminates the need for manually specifying tangent vectors.",
        "B) It uses autoencoders to estimate tangent vectors from the data.",
        "C) It only regularizes the model against transformations like translation, scaling, and rotation.",
        "D) It can learn object-specific transformations that go beyond simple geometric transformations."
    ],
    'correct_answer': 'C',
    'explanation': "The manifold tangent classifier can regularize against object-specific transformations, not just classical transformations like translation, scaling, and rotation.",
    'chapter_information': 'Deep Learning Book Chapter 7.13'
}


deep_learning_ch8_truefalse_question_13 = {
    'question': "True or False: Stochastic gradient descent (SGD) provides an unbiased estimate of the generalization error for the entire training process, even when training examples are repeated across epochs.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "SGD provides an unbiased estimate of the generalization error only during the first epoch. When examples are reused in subsequent epochs, the estimates become biased because they are based on already-seen data.",
    'chapter_information': 'Deep Learning Book Chapter 8'
}

deep_learning_ch8_truefalse_question_14 = {
    'question': "True or False: In online learning, the learner receives a stream of data, where each example is a new sample drawn from the data-generating distribution.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "In online learning, the learner continually receives new data points drawn from the data-generating distribution, and these examples are never repeated.",
    'chapter_information': 'Deep Learning Book Chapter 8'
}

deep_learning_ch8_truefalse_question_15 = {
    'question': "True or False: Using a very large dataset in stochastic gradient descent eliminates the risk of overfitting.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "While a very large dataset reduces the risk of overfitting, it doesn't eliminate it entirely. Overfitting can still occur if the model is too complex or training is conducted for too many epochs.",
    'chapter_information': 'Deep Learning Book Chapter 8'
}


deep_learning_ch8_mpc_question_16 = {
    'question': "Which of the following is TRUE about the gradient computed by stochastic gradient descent (SGD) during the first epoch of training?",
    'options_list': [
        "A) It is a biased estimate of the gradient of the generalization error.",
        "B) It provides an unbiased estimate of the gradient of the generalization error.",
        "C) It introduces noise into the estimate by using random subsets of the data.",
        "D) It is only unbiased if all training examples are seen an equal number of times."
    ],
    'correct_answer': 'B',
    'explanation': "During the first epoch, SGD provides an unbiased estimate of the gradient of the generalization error, as the examples are seen for the first time and sampled from the data-generating distribution.",
    'chapter_information': 'Deep Learning Book Chapter 8'
}

deep_learning_ch8_mpc_question_17 = {
    'question': "What happens to the estimate of the gradient when minibatch stochastic gradient descent (SGD) is used with repeated examples across epochs?",
    'options_list': [
        "A) The estimate remains unbiased throughout the training process.",
        "B) The estimate becomes biased after the first epoch because of resampling already-seen data.",
        "C) The estimate becomes progressively less noisy with each epoch, improving generalization.",
        "D) The estimate is unaffected by repeating examples across epochs."
    ],
    'correct_answer': 'B',
    'explanation': "The estimate of the gradient becomes biased after the first epoch when using minibatch SGD because it starts resampling examples that have already been used, rather than sampling new ones.",
    'chapter_information': 'Deep Learning Book Chapter 8'
}

deep_learning_ch8_mpc_question_18 = {
    'question': "Which of the following scenarios best describes a situation where only one pass through the training data is sufficient?",
    'options_list': [
        "A) When the training set is extremely large, and the concern is primarily computational efficiency.",
        "B) When the training set is small, and generalization error is a concern.",
        "C) When the training set is of medium size, and underfitting is the predominant problem.",
        "D) When the model is simple, and overfitting is the primary concern."
    ],
    'correct_answer': 'A',
    'explanation': "In scenarios with extremely large datasets, making only one pass through the data can be computationally efficient and sufficient, as overfitting is less of a concern with large datasets.",
    'chapter_information': 'Deep Learning Book Chapter 8'
}

deep_learning_ch8_truefalse_question_16 = {
    'question': "True or False: The theoretical limits of optimization prove that it is impossible to efficiently optimize any neural network model in practice.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Theoretical results show that certain problem classes are intractable, but in practice, we can often find solutions using larger networks or by optimizing for sufficient reduction in the objective function rather than the exact minimum.",
    'chapter_information': 'Deep Learning Book Chapter 8.2'
}

deep_learning_ch8_truefalse_question_17 = {
    'question': "True or False: Local descent algorithms like gradient descent may struggle in regions with poor conditioning or wide flat regions of the objective function.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Gradient descent and other local descent methods struggle in poorly conditioned regions or wide flat regions because the gradient provides little or no information about the direction to the solution.",
    'chapter_information': 'Deep Learning Book Chapter 8.2'
}

deep_learning_ch8_truefalse_question_18 = {
    'question': "True or False: Optimization algorithms for neural networks are most effective when solving for critical points like Newton’s method does.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Optimization methods that solve explicitly for critical points, such as Newton’s method, can lead to issues like landing on plateaus or saddle points, where local information provides no guidance for further optimization.",
    'chapter_information': 'Deep Learning Book Chapter 8.2'
}

deep_learning_ch8_truefalse_question_19 = {
    'question': "True or False: Initializing biases to zero is generally compatible with most weight initialization schemes, but certain models benefit from nonzero bias initialization to match the marginal distribution of the output.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Zero bias initialization is common, but nonzero bias values can be useful for aligning with the marginal distribution of the output, such as in softmax classifiers or models like autoencoders.",
    'chapter_information': 'Deep Learning Book Chapter 8.3-4'
}

deep_learning_ch8_truefalse_question_20 = {
    'question': "True or False: Variance or precision parameters in a model like linear regression can safely be initialized to zero without impacting the model's performance.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Initializing variance or precision parameters to zero would be problematic, as it would cause division by zero in models like linear regression. A safe choice is to initialize them to 1.",
    'chapter_information': 'Deep Learning Book Chapter 8.3-4'
}

deep_learning_ch8_truefalse_question_21 = {
    'question': "True or False: Machine learning-based parameter initialization, such as pretraining with an unsupervised model, can improve both convergence speed and generalization in some models.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Pretraining using unsupervised learning or a related supervised task can encode prior information into the model's initial parameters, leading to faster convergence and better generalization.",
    'chapter_information': 'Deep Learning Book Chapter 8.3-4'
}

deep_learning_ch8_mpc_question_19 = {
    'question': "Which of the following is a known limitation of local descent algorithms like gradient descent?",
    'options_list': [
        "A) They can handle nonlocal moves, providing a global solution for any optimization problem.",
        "B) They are efficient in wide flat regions of the objective function where the gradient is close to zero.",
        "C) They may follow a path that is computationally expensive and inefficient, even if it eventually leads to a solution.",
        "D) They can directly solve for critical points, ensuring convergence to the global minimum."
    ],
    'correct_answer': 'C',
    'explanation': "Local descent algorithms like gradient descent may follow an inefficient path to the solution, especially when dealing with poorly conditioned regions or flat areas of the objective function.",
    'chapter_information': 'Deep Learning Book Chapter 8.2'
}

deep_learning_ch8_mpc_question_20 = {
    'question': "Which of the following describes a scenario where local descent fails to define a path to a solution?",
    'options_list': [
        "A) When the objective function has poor conditioning and the gradient is small.",
        "B) When the algorithm makes nonlocal moves that avoid critical points.",
        "C) When the function has wide flat regions or the method lands on a critical point.",
        "D) When the gradient is continuously increasing in steep regions."
    ],
    'correct_answer': 'C',
    'explanation': "Local descent methods fail when encountering wide flat regions or when the algorithm lands on a critical point, where the gradient provides little guidance for further optimization.",
    'chapter_information': 'Deep Learning Book Chapter 8.2'
}

deep_learning_ch8_mpc_question_21 = {
    'question': "Given the following gradient descent update formula with poor conditioning, how does the computational cost scale? Assume the step size $\\epsilon$ is much larger than $\\delta$, where $\\delta$ is the precision of the estimated gradient.",
    'options_list': [
        "A) The cost scales linearly with the number of gradient steps $\\delta$.",
        "B) The cost scales quadratically with the number of steps due to the difference between $\\epsilon$ and $\\delta$.",
        "C) The cost remains constant, regardless of the step size.",
        "D) The cost scales inversely with the number of steps $\\epsilon$."
    ],
    'correct_answer': 'B',
    'explanation': "The computational cost scales quadratically when the step size $\\epsilon$ is much larger than the precision $\\delta$, as many small steps are needed to account for poor conditioning, increasing the overall cost.",
    'chapter_information': 'Deep Learning Book Chapter 8.2'
}

deep_learning_ch8_mpc_question_22 = {
    'question': "Which of the following mathematical conditions may result in a local descent path that does not lead to a solution?",
    'options_list': [
        "A) $\\nabla J(\\theta) \\approx 0$ in flat regions of the objective function.",
        "B) $\\nabla J(\\theta) > 0$ in regions with high curvature.",
        "C) $\\nabla J(\\theta) \\ll 0$, providing clear direction for descent.",
        "D) $\\nabla J(\\theta) = \\nabla f(x, y)$, where the gradient consistently decreases."
    ],
    'correct_answer': 'A',
    'explanation': "When the gradient is approximately zero in flat regions of the objective function, local descent algorithms fail to provide a path to the solution as no clear direction for descent exists.",
    'chapter_information': 'Deep Learning Book Chapter 8.2'
}

deep_learning_ch8_truefalse_question_26 = {
    'question': "True or False: Nonlinear conjugate gradients require frequent resets due to the fact that the objective function is not guaranteed to be quadratic.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Nonlinear conjugate gradients cannot guarantee conjugate directions stay at the minimum when the objective is non-quadratic, so it occasionally resets the algorithm.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}

deep_learning_ch8_truefalse_question_27 = {
    'question': "True or False: The BFGS algorithm can be applied efficiently to deep learning models with millions of parameters because it avoids the need to store the inverse Hessian.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "BFGS requires storing the inverse Hessian matrix, which makes it computationally expensive (O(n^2) memory). This limitation is addressed by L-BFGS, which avoids storing the full inverse Hessian.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}

deep_learning_ch8_truefalse_question_28 = {
    'question': "True or False: L-BFGS approximates the inverse Hessian by assuming it to be the identity matrix and updates it iteratively, avoiding the need for large memory storage.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "L-BFGS starts with the identity matrix as the inverse Hessian approximation and updates it iteratively, requiring much less memory compared to full BFGS.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}


deep_learning_ch8_mpc_question_22 = {
    'question': "Which of the following describes an effective method for choosing initial weight scales in a neural network?",
    'options_list': [
        "A) Initialize all weights to zero to prevent saturation.",
        "B) Adjust the weight scales manually based on the range or standard deviation of activations in a minibatch.",
        "C) Set all weights to one to maximize the gradient flow through the network.",
        "D) Use a single large minibatch to train weights with high variance."
    ],
    'correct_answer': 'B',
    'explanation': "Manually adjusting the weight scales based on the range or standard deviation of activations is an effective strategy for achieving balanced activations throughout the network, preventing issues like vanishing gradients.",
    'chapter_information': 'Deep Learning Book Chapter 8.3-4'
}

deep_learning_ch8_mpc_question_23 = {
    'question': "For a linear regression model with a conditional variance estimate $p(y | x) = N(y | w^T x + b, 1/\\beta)$, which of the following is the safest way to initialize $\\beta$?",
    'options_list': [
        "A) Set $\\beta = 0$ to allow the model to learn the precision from the data.",
        "B) Set $\\beta = 1$, assuming the precision parameter can later be optimized.",
        "C) Initialize $\\beta$ to a random value based on the variance of the target variable.",
        "D) Set $\\beta$ to the marginal variance of the output in the training set."
    ],
    'correct_answer': 'B',
    'explanation': "Setting $\\beta = 1$ is a safe and commonly used approach when initializing the precision parameter, as it provides a reasonable starting point before further optimization.",
    'chapter_information': 'Deep Learning Book Chapter 8.3-4'
}

deep_learning_ch8_mpc_question_24 = {
    'question': "In neural networks, initializing biases to small nonzero values can be useful in which of the following scenarios?",
    'options_list': [
        "A) To avoid strong bias input into the random walk initialization scheme.",
        "B) To prevent saturation in activation functions like ReLU during initialization.",
        "C) To ensure that the hidden units output the exact value of their input during the first few epochs.",
        "D) To initialize the marginal distribution of the input data directly in the hidden layers."
    ],
    'correct_answer': 'B',
    'explanation': "Setting the bias of ReLU hidden units to a small nonzero value (e.g., 0.1) helps avoid saturation during initialization, which can prevent the unit from becoming inactive early in training.",
    'chapter_information': 'Deep Learning Book Chapter 8.3-4'
}

deep_learning_ch8_mpc_question_25 = {
    'question': "Given a softmax output layer with a bias term $b$ and marginal class probabilities $c$, what is the correct equation for initializing the bias such that the output matches the marginal statistics?",
    'options_list': [
        "A) $b = \\log(c)$",
        "B) $\\text{softmax}(b) = c$",
        "C) $b = \\exp(c)$",
        "D) $b = \\text{sigmoid}(c)$"
    ],
    'correct_answer': 'B',
    'explanation': "The bias $b$ should be initialized by solving $\\text{softmax}(b) = c$ to match the marginal class probabilities to the output distribution.",
    'chapter_information': 'Deep Learning Book Chapter 8.3-4'
}

deep_learning_ch8_mpc_question_29 = {
    'question': "Which of the following is a key difference between the BFGS and conjugate gradient methods?",
    'options_list': [
        "A) Conjugate gradient methods require more storage than BFGS.",
        "B) BFGS does not depend on performing an exact line search, while conjugate gradient methods do.",
        "C) Conjugate gradient methods use second-order information, whereas BFGS uses first-order derivatives only.",
        "D) BFGS always converges faster than conjugate gradients for neural networks."
    ],
    'correct_answer': 'B',
    'explanation': "BFGS can handle inexact line searches better than conjugate gradient methods, which rely more on finding the exact minimum along the search direction.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}

deep_learning_ch8_mpc_question_30 = {
    'question': "In the BFGS algorithm, the parameter update rule is $\\theta_{t+1} = \\theta_t + \\epsilon^* \\rho_t$, where $\\rho_t$ is the descent direction. How is $\\rho_t$ calculated?",
    'options_list': [
        "A) $\\rho_t = M_t^{-1} g_t$, where $M_t$ is the inverse Hessian approximation.",
        "B) $\\rho_t = H g_t$, where $H$ is the Hessian matrix.",
        "C) $\\rho_t = M_t g_t$, where $M_t$ is the inverse Hessian approximation.",
        "D) $\\rho_t = \\epsilon_t g_t$, where $\\epsilon_t$ is the learning rate."
    ],
    'correct_answer': 'C',
    'explanation': "In BFGS, $\\rho_t = M_t g_t$, where $M_t$ is the inverse Hessian approximation and $g_t$ is the gradient.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}

deep_learning_ch8_mpc_question_31 = {
    'question': "The L-BFGS algorithm reduces memory usage by:",
    'options_list': [
        "A) Using exact line searches to avoid storing any Hessian information.",
        "B) Computing the inverse Hessian using only a few vectors from previous iterations.",
        "C) Storing the entire Hessian matrix for only the first few steps.",
        "D) Approximating the Hessian using first-order derivatives only."
    ],
    'correct_answer': 'B',
    'explanation': "L-BFGS reduces memory usage by storing only a few vectors from previous iterations, which are used to approximate the inverse Hessian.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}

deep_learning_ch8_mpc_question_34 = {
    'question': "Which of the following is a potential failure point of continuation methods?",
    'options_list': [
        "A) The cost function becomes convex but may track to a local rather than a global minimum.",
        "B) The cost function may fail to become convex no matter how much it is blurred.",
        "C) Continuation methods may require many incremental cost functions, making the entire procedure computationally expensive.",
        "D) All of the above."
    ],
    'correct_answer': 'D',
    'explanation': "Continuation methods can fail in multiple ways, including tracking to a local minimum, failing to become convex, or requiring many incremental cost functions that increase computational cost.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}

deep_learning_ch8_mpc_question_35 = {
    'question': "In the context of curriculum learning, which of the following describes how it helps improve neural network optimization?",
    'options_list': [
        "A) Curriculum learning starts by learning simple concepts and progresses to more complex ones, which helps reduce flat regions and improve gradient estimates.",
        "B) Curriculum learning primarily focuses on reducing memory usage by eliminating the need for minibatch processing.",
        "C) It directly minimizes the Hessian matrix and improves its conditioning without altering the training data distribution.",
        "D) Curriculum learning is unrelated to the optimization of neural networks and focuses only on data augmentation."
    ],
    'correct_answer': 'A',
    'explanation': "Curriculum learning improves optimization by starting with simple concepts and gradually introducing more complex ones, reducing issues like flat regions and poor gradient conditioning.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}

deep_learning_ch8_mpc_question_36 = {
    'question': "If curriculum learning is viewed as a continuation method, what role do the earlier cost functions \( J^{(i)} \) play?",
    'options_list': [
        "A) They increase the influence of simpler examples, making the initial phases of learning easier.",
        "B) They introduce harder examples first, forcing the model to learn faster.",
        "C) They focus only on increasing the capacity of the model without changing the learning process.",
        "D) They are designed to overfit the training data to improve generalization."
    ],
    'correct_answer': 'A',
    'explanation': "In curriculum learning, the earlier cost functions are designed to increase the influence of simpler examples, which makes the initial phases of learning easier and gradually increases the complexity of the task.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}

deep_learning_ch8_mpc_question_37 = {
    'question': "In the curriculum learning approach proposed by Zaremba and Sutskever (2014) for training recurrent neural networks, what differentiates the stochastic curriculum from the deterministic curriculum?",
    'options_list': [
        "A) The stochastic curriculum presents a random mix of easy and difficult examples, with the proportion of difficult examples gradually increasing.",
        "B) The stochastic curriculum always presents the most difficult examples first.",
        "C) The deterministic curriculum uses random ordering, while the stochastic curriculum uses a fixed sequence of examples.",
        "D) Both approaches lead to the same optimization outcomes."
    ],
    'correct_answer': 'A',
    'explanation': "The stochastic curriculum gradually increases the proportion of difficult examples, which has been shown to provide better results in training recurrent neural networks, unlike the deterministic curriculum which did not show improvement.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}


deep_learning_ch8_mpc_question_33 = {
    'question': "For the conjugate gradient method, if $\\theta_{t+1} = \\theta_t + \\epsilon_t p_t$, where $p_t$ is the conjugate direction and $\\epsilon_t$ is found via a line search, which of the following ensures that $p_t$ is conjugate?",
    'options_list': [
        "A) $p_{t+1} = -g_{t+1} + \\beta_t p_t$, where $\\beta_t = \\frac{g_{t+1}^T g_{t+1}}{g_t^T g_t}$",
        "B) $p_{t+1} = g_{t+1} + \\alpha_t p_t$, where $\\alpha_t = \\frac{g_t^T p_t}{p_t^T p_t}$",
        "C) $p_{t+1} = g_{t+1} + \\beta_t g_t$, where $\\beta_t = \\frac{g_t^T p_t}{p_t^T p_t}$",
        "D) $p_{t+1} = g_{t+1} - \\alpha_t p_t$, where $\\alpha_t = \\frac{g_t^T g_t}{p_t^T p_t}$"
    ],
    'correct_answer': 'A',
    'explanation': "In the conjugate gradient method, the conjugate direction $p_t$ is updated using the formula $p_{t+1} = -g_{t+1} + \\beta_t p_t$, where $\\beta_t = \\frac{g_{t+1}^T g_{t+1}}{g_t^T g_t}$. This ensures that $p_t$ is conjugate with respect to the previous direction.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}

deep_learning_ch8_mpc_question_32 = {
    'question': "Given the BFGS update formula for the parameters $\\theta_{t+1} = \\theta_t + \\epsilon^* \\rho_t$, and knowing that $\\rho_t = M_t g_t$, what is the computational complexity of storing $M_t$ in the BFGS algorithm?",
    'options_list': [
        "A) O(n)",
        "B) O(n^2)",
        "C) O(n^3)",
        "D) O(n \\log n)"
    ],
    'correct_answer': 'B',
    'explanation': "Storing the inverse Hessian approximation $M_t$ requires O(n^2) memory, making BFGS computationally expensive for large models.",
    'chapter_information': 'Deep Learning Book Chapter 8.5-6'
}

deep_learning_ch8_math_question_38 = {
    'question': "Suppose you are applying a continuation method to optimize a cost function $J(\\theta)$, where $J(\\theta)$ becomes convex when blurred by a Gaussian kernel with variance $\\sigma^2$. If the blur makes $J(\\theta)$ convex for $\\sigma^2 = 0.1$, but the continuation method fails to find the global minimum. What could be a possible reason for failure?",
    'options_list': [
        "A) The blurred function tracks to a local minimum instead of a global minimum.",
        "B) The cost function $J(\\theta)$ is still non-convex after blurring with $\\sigma^2 = 0.1$.",
        "C) The number of incremental cost functions required is too high, making the procedure computationally expensive.",
        "D) Both A and C."
    ],
    'correct_answer': 'D',
    'explanation': "The continuation method can fail if the blurred function tracks to a local minimum or if the procedure requires too many incremental cost functions, making it computationally expensive.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}

deep_learning_ch8_math_question_39 = {
    'question': "Consider a curriculum learning task where the cost function $J(\\theta)$ is progressively modified. If we approximate the cost function with $J^{(i)}(\\theta)$ for the $i$-th stage, how would the rate of convergence change if the proportion of difficult examples is introduced too early?",
    'options_list': [
        "A) The rate of convergence would increase as the model learns faster with more difficult examples.",
        "B) The convergence rate would decrease due to the model being overwhelmed by complexity too soon.",
        "C) The convergence rate remains unaffected by the difficulty of examples introduced.",
        "D) The convergence rate is solely dependent on the optimizer and not on the curriculum learning process."
    ],
    'correct_answer': 'B',
    'explanation': "Introducing difficult examples too early can slow down the convergence rate because the model may not have learned simpler concepts that are necessary to understand the more difficult examples.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}

deep_learning_ch8_math_question_40 = {
    'question': "Given that continuation methods can be applied by progressively 'blurring' a non-convex function, the function $J(\\theta) = -\\theta^T \\theta$ cannot be made convex by blurring. Why is this the case?",
    'options_list': [
        "A) $J(\\theta) = -\\theta^T \\theta$ is already convex.",
        "B) The quadratic form of the function means no amount of blurring can alter its shape.",
        "C) The function is concave, and no blurring operation can convert it into a convex function.",
        "D) Blurring operations are only applicable to smooth functions, and $J(\\theta)$ is not smooth."
    ],
    'correct_answer': 'C',
    'explanation': "The function $J(\\theta) = -\\theta^T \\theta$ is concave, and no amount of blurring can change it into a convex function.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}

deep_learning_ch8_math_question_41 = {
    'question': "In a continuation method applied to an NP-hard optimization problem, you are given a sequence of cost functions $J^{(1)}, J^{(2)}, ..., J^{(n)}$. Each cost function is blurred by adding a Gaussian noise term with variance $\\sigma^2$. How would increasing $\\sigma^2$ too much affect the optimization process?",
    'options_list': [
        "A) It would smooth out the cost function too much, causing the optimizer to converge to a local minimum that is far from the global minimum.",
        "B) It would cause the function to remain non-convex, leading to poor convergence.",
        "C) The optimization process would become faster as the function becomes more convex.",
        "D) The effect would be negligible as the optimizer always finds the global minimum, regardless of the amount of blur."
    ],
    'correct_answer': 'A',
    'explanation': "Blurring the cost function too much (increasing $\\sigma^2$) can cause the optimizer to converge to a local minimum that is far from the global minimum by over-smoothing the function.",
    'chapter_information': 'Deep Learning Book Chapter 8.7'
}

lesson_3_3_initialization_mpc_question_1 = {
    'question': "Why is proper initialization crucial for training deep neural networks?",
    'options_list': [
        "A) It simplifies the model by reducing the number of layers required.",
        "B) It ensures that weights start with large values to accelerate learning.",
        "C) It helps maintain effective gradient flow during training, avoiding vanishing or exploding gradients.",
        "D) It eliminates the need for optimization algorithms."
    ],
    'correct_answer': 'C',
    'explanation': "Proper initialization ensures effective gradient flow, preventing issues like vanishing or exploding gradients, which can hinder learning.",
    'chapter_information': 'Lesson 3.3: Initialization, Section 1: Importance of Initialization'
}

lesson_3_3_initialization_mpc_question_2 = {
    'question': "If weights are initialized to very small values, what happens to the activations in a deep neural network?",
    'options_list': [
        "A) The activations remain in the linear region of non-linear functions, allowing for stronger gradients.",
        "B) The network will experience gradient explosion due to small weights.",
        "C) It prevents learning, as all neurons produce the same output.",
        "D) Weights initialized with small values saturate the network."
    ],
    'correct_answer': 'A',
    'explanation': "Initializing weights to small values keeps activations in the linear region of non-linear functions, promoting better gradient flow and learning.",
    'chapter_information': 'Lesson 3.3: Initialization, Section 2: How Initialization Affects Neural Networks'
}

lesson_3_3_initialization_mpc_question_3 = {
    'question': "Which of the following initialization strategies is most suitable for tanh activation functions?",
    'options_list': [
        "A) He initialization",
        "B) Constant initialization",
        "C) Xavier initialization",
        "D) Zero initialization"
    ],
    'correct_answer': 'C',
    'explanation': "Xavier initialization works well for tanh activations as it maintains similar variances across layers, helping avoid vanishing gradients.",
    'chapter_information': 'Lesson 3.3: Initialization, Section 8: Initialization for Different Activation Functions'
}

lesson_3_3_initialization_mpc_question_4 = {
    'question': "What is the purpose of Xavier initialization in neural networks?",
    'options_list': [
        "A) To maintain the variance of activations between layers.",
        "B) To prevent activations from saturating non-linearities like ReLU.",
        "C) To simplify the network by reducing the number of weights.",
        "D) To initialize biases instead of weights."
    ],
    'correct_answer': 'A',
    'explanation': "Xavier initialization ensures that the variance of activations remains stable across layers, preventing vanishing or exploding gradients.",
    'chapter_information': 'Lesson 3.3: Initialization, Section 6: Maintaining Variance Across Layers'
}

lesson_3_3_initialization_mpc_question_5 = {
    'question': "The Xavier initialization samples weights from a uniform distribution given by the formula:\n"
                "$W \\sim U \\left( -\\frac{\\sqrt{6}}{\\sqrt{n_{in} + n_{out}}}, \\frac{\\sqrt{6}}{\\sqrt{n_{in} + n_{out}}} \\right)$.\n"
                "What do $n_{in}$ and $n_{out}$ represent in this formula?",
    'options_list': [
        "A) The number of neurons in the input and output layers, respectively.",
        "B) The number of inputs to and outputs from a neuron in a particular layer.",
        "C) The learning rate and the batch size.",
        "D) The weights and biases in the network."
    ],
    'correct_answer': 'B',
    'explanation': "$n_{in}$ is the number of inputs to a neuron, and $n_{out}$ is the number of outputs from a neuron. Xavier initialization ensures that the variance of the weights is proportional to the layer's size.",
    'chapter_information': 'Lesson 3.3: Initialization, Section 6: Maintaining Variance Across Layers'
}

lesson_3_3_initialization_mpc_question_6 = {
    'question': "How does He initialization differ from Xavier initialization for ReLU activation functions?",
    'options_list': [
        "A) He initialization introduces an additional scaling factor of 2.",
        "B) He initialization is only used for recurrent neural networks.",
        "C) He initialization scales weights based on the number of output units instead of input units.",
        "D) He initialization is used to initialize biases instead of weights."
    ],
    'correct_answer': 'A',
    'explanation': "He initialization introduces an additional scaling factor of 2 to account for the nature of ReLU activations, ensuring better gradient flow during training.",
    'chapter_information': 'Lesson 3.3: Initialization, Section 8: Initialization for Different Activation Functions'
}

lesson_3_3_initialization_mpc_question_7 = {
    'question': "In deep networks, poor initialization can lead to the vanishing gradient problem. What is the vanishing gradient problem?",
    'options_list': [
        "A) Gradients become very small in deeper layers, preventing effective learning.",
        "B) Gradients grow too large, causing unstable training.",
        "C) Gradients fluctuate rapidly between layers, causing oscillations.",
        "D) Gradients become zero at the output layer, halting the backpropagation process."
    ],
    'correct_answer': 'A',
    'explanation': "The vanishing gradient problem occurs when gradients become very small in deeper layers, which significantly slows down or prevents learning.",
    'chapter_information': 'Lesson 3.3: Initialization, Section 5: Challenges with Deeper Networks'
}


lesson_3_4_optimization_mpc_question_1 = {
    'question': "What is the purpose of adding momentum to Stochastic Gradient Descent (SGD)?",
    'options_list': [
        "A) To reduce the learning rate as training progresses.",
        "B) To accelerate learning and help navigate flatter regions of the loss surface.",
        "C) To completely eliminate the vanishing gradient problem.",
        "D) To increase the batch size during training."
    ],
    'correct_answer': 'B',
    'explanation': "Momentum adds velocity to the weight updates, allowing the optimizer to build momentum and traverse flatter regions of the loss surface more effectively.",
    'chapter_information': 'Lesson 3.4: Optimization, Section 4: Momentum-Based Optimization'
}

lesson_3_4_optimization_mpc_question_2 = {
    'question': "What is the role of the Hessian matrix in second-order optimization methods?",
    'options_list': [
        "A) It adjusts the learning rate during each iteration.",
        "B) It approximates the curvature of the loss surface to scale gradient updates.",
        "C) It prevents the model from overfitting.",
        "D) It computes the gradient of the loss function for large datasets."
    ],
    'correct_answer': 'B',
    'explanation': "The Hessian matrix provides information about the curvature of the loss surface, helping second-order methods scale gradient updates for faster convergence.",
    'chapter_information': 'Lesson 3.4: Optimization, Section 5: Second-Order Optimization'
}

lesson_3_4_optimization_mpc_question_3 = {
    'question': "What is the main limitation of Adagrad as an optimizer?",
    'options_list': [
        "A) It does not adapt the learning rate for different parameters.",
        "B) It accumulates gradients indefinitely, causing the learning rate to shrink too much over time.",
        "C) It is computationally expensive and slow to converge.",
        "D) It requires the use of a momentum term for stability."
    ],
    'correct_answer': 'B',
    'explanation': "Adagrad tends to shrink the learning rate too much over time due to the accumulation of past squared gradients, which can slow down learning in later stages of training.",
    'chapter_information': 'Lesson 3.4: Optimization, Section 6: Adaptive Learning Rate Methods'
}

lesson_3_4_optimization_mpc_question_4 = {
    'question': "Which of the following optimizers combines the benefits of RMSProp and momentum?",
    'options_list': [
        "A) Adagrad",
        "B) SGD with momentum",
        "C) Adam",
        "D) Nesterov momentum"
    ],
    'correct_answer': 'C',
    'explanation': "Adam combines the adaptive learning rate of RMSProp with the momentum update rule to produce more stable and effective learning.",
    'chapter_information': 'Lesson 3.4: Optimization, Section 6: Adaptive Learning Rate Methods'
}

lesson_3_4_optimization_mpc_question_5 = {
    'question': "How does Nesterov momentum improve upon standard momentum?",
    'options_list': [
        "A) It introduces a new learning rate scheduler for faster convergence.",
        "B) It uses a lookahead step to calculate the gradient at the new point before updating weights.",
        "C) It applies second-order derivatives to compute the update.",
        "D) It reduces the variance in gradient estimates during training."
    ],
    'correct_answer': 'B',
    'explanation': "Nesterov momentum improves standard momentum by making a lookahead step before calculating the gradient, which accelerates learning by predicting the direction of the gradient.",
    'chapter_information': 'Lesson 3.4: Optimization, Section 4: Momentum-Based Optimization'
}

lesson_3_5_regularization_mpc_question_1 = {
    'question': "Why is regularization important in deep learning models?",
    'options_list': [
        "A) It increases the model's complexity and prevents underfitting.",
        "B) It helps reduce overfitting by encouraging smaller weights or sparsity.",
        "C) It speeds up training by using fewer features.",
        "D) It ensures that the model focuses on specific features during training."
    ],
    'correct_answer': 'B',
    'explanation': "Regularization techniques, such as L1 or L2 regularization, help reduce overfitting by penalizing large weights, thus encouraging simpler models that generalize better to new data.",
    'chapter_information': 'Lesson 3.5: Regularization, Section 1: Why Regularization is Crucial in Deep Learning'
}

lesson_3_5_regularization_mpc_question_2 = {
    'question': "What is the main purpose of dropout regularization?",
    'options_list': [
        "A) To ensure that all neurons are always active during training.",
        "B) To prevent the model from relying too heavily on specific features or neurons.",
        "C) To increase the number of parameters in the model.",
        "D) To scale the weights of neurons during testing."
    ],
    'correct_answer': 'B',
    'explanation': "Dropout prevents the network from relying too heavily on specific neurons or features by randomly deactivating neurons during training, encouraging the model to distribute learning across the entire network.",
    'chapter_information': 'Lesson 3.5: Regularization, Section 2: Dropout Regularization'
}

lesson_3_5_regularization_mpc_question_3 = {
    'question': "How does dropout work during the training phase?",
    'options_list': [
        "A) It deactivates all neurons for certain batches.",
        "B) It keeps neurons active with a probability P and sets inactive neurons' outputs to zero.",
        "C) It scales neuron activations by a factor of P during every iteration.",
        "D) It activates all neurons at each iteration but with reduced weights."
    ],
    'correct_answer': 'B',
    'explanation': "During training, dropout works by keeping each neuron active with a probability P (e.g., 0.5) and setting the outputs of inactive neurons to zero. This helps reduce the network's reliance on specific neurons.",
    'chapter_information': 'Lesson 3.5: Regularization, Section 2: Dropout Regularization'
}

lesson_3_5_regularization_mpc_question_4 = {
    'question': "What is a key difference between training and testing when using dropout?",
    'options_list': [
        "A) All neurons are used during testing, while some are deactivated during training.",
        "B) The probability P of keeping a neuron changes between training and testing.",
        "C) Dropout is only applied during the testing phase, not during training.",
        "D) Neuron outputs are scaled up by a factor of P during testing."
    ],
    'correct_answer': 'A',
    'explanation': "During training, neurons are randomly dropped with a probability P, but during testing, all neurons are used to ensure full network capacity and consistent outputs.",
    'chapter_information': 'Lesson 3.5: Regularization, Section 3: Handling Training vs. Testing Differences'
}

lesson_3_5_regularization_mpc_question_5 = {
    'question': "Why does dropout work effectively in preventing overfitting?",
    'options_list': [
        "A) It forces the network to learn with varying subsets of neurons, preventing over-reliance on specific features.",
        "B) It increases the number of parameters, leading to better learning.",
        "C) It reduces the size of the model, making it faster to train.",
        "D) It applies L1 regularization to the weights of dropped neurons."
    ],
    'correct_answer': 'A',
    'explanation': "Dropout helps prevent overfitting by forcing the network to function well with different subsets of neurons during training, ensuring it does not rely too heavily on any one neuron or feature.",
    'chapter_information': 'Lesson 3.5: Regularization, Section 4: Why Dropout Works'
}

deep_learning_book_9_1_mpc_question_1 = {
    'question': "What is the mathematical relationship between convolution and cross-correlation as described in the text?",
    'options_list': [
        "A) They are identical operations",
        "B) Cross-correlation flips the kernel, convolution does not",
        "C) Convolution flips the kernel, cross-correlation does not",
        "D) They are inverse operations of each other"
    ],
    'correct_answer': 'C',
    'explanation': "Convolution involves flipping the kernel before applying it to the input, while cross-correlation applies the kernel directly without flipping. Both operations are often referred to as 'convolution' in machine learning libraries.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_mpc_question_2 = {
    'question': "Which of the following matrix types corresponds to 2D discrete convolution?",
    'options_list': [
        "A) Toeplitz matrix",
        "B) Circulant matrix",
        "C) Doubly block circulant matrix",
        "D) Sparse matrix"
    ],
    'correct_answer': 'C',
    'explanation': "In two dimensions, 2D convolution corresponds to a doubly block circulant matrix, which captures the structure of shifting blocks across the input.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_mpc_question_3 = {
    'question': "According to the text, why do many machine learning libraries implement cross-correlation but call it convolution?",
    'options_list': [
        "A) It's mathematically more accurate",
        "B) It's computationally more efficient",
        "C) It's a common convention in the field",
        "D) The difference is irrelevant for neural networks"
    ],
    'correct_answer': 'C',
    'explanation': "Many machine learning libraries use cross-correlation but call it convolution because it has become a common convention, despite the technical difference.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_mpc_question_4 = {
    'question': "What property of convolution arises from flipping the kernel relative to the input?",
    'options_list': [
        "A) Associativity",
        "B) Distributivity",
        "C) Commutativity",
        "D) Transitivity"
    ],
    'correct_answer': 'C',
    'explanation': "Flipping the kernel in convolution ensures that the operation is commutative, a property that is useful in theoretical proofs but not always critical for neural network implementations.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_mpc_question_5 = {
    'question': "What is the advantage of using convolution in neural networks, as described in the text?",
    'options_list': [
        "A) It allows the model to learn global patterns across the input",
        "B) It significantly reduces the number of parameters through weight sharing",
        "C) It makes the network non-commutative",
        "D) It eliminates the need for dense connections between layers"
    ],
    'correct_answer': 'B',
    'explanation': "Convolution reduces the number of parameters by sharing weights across local patches, making it highly efficient for tasks like image recognition.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_tf_question_1 = {
    'question': "Discrete convolution can always be represented as multiplication by a dense matrix.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Convolutions are typically represented by sparse matrices (such as Toeplitz or doubly block circulant matrices), as the kernel is much smaller than the input.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_tf_question_2 = {
    'question': "The commutative property of convolution is crucial for neural network implementations.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "While the commutative property of convolution is useful in theoretical contexts, it is not crucial for neural network implementations. In practice, cross-correlation (which does not involve flipping) is often used.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_tf_question_3 = {
    'question': "In machine learning applications, convolution is typically used with multidimensional arrays of parameters adapted by the learning algorithm.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "In deep learning, convolution is typically applied to multidimensional arrays (tensors), and the parameters (kernels) are adapted through training.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_tf_question_4 = {
    'question': "Convolutional neural networks strictly require the use of kernel flipping to function properly.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Kernel flipping is not strictly required for convolutional neural networks. Many machine learning libraries use cross-correlation (without flipping) and still refer to it as convolution.",
    'chapter_information': 'Deep Learning Book 9.1'
}

deep_learning_book_9_1_tf_question_5 = {
    'question': "The text suggests that for practical machine learning, the distinction between convolution and cross-correlation is often not critical.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "In practical machine learning applications, the distinction between convolution (with kernel flipping) and cross-correlation (without flipping) is often not critical, as the model will learn the appropriate patterns regardless.",
    'chapter_information': 'Deep Learning Book 9.1'
}


deep_learning_book_9_2_9_3_mpc_question_1 = {
    'question': "What is the primary purpose of pooling layers in convolutional neural networks?",
    'options_list': [
        "A) To increase the spatial dimensions of feature maps",
        "B) To add non-linearity to the network",
        "C) To reduce the spatial dimensions of feature maps and control overfitting",
        "D) To perform convolution operations"
    ],
    'correct_answer': 'C',
    'explanation': "Pooling layers reduce the spatial dimensions of feature maps, which helps control overfitting and reduces computational complexity in the next layers.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_mpc_question_2 = {
    'question': "Which of the following is NOT a common type of pooling operation?",
    'options_list': [
        "A) Max pooling",
        "B) Average pooling",
        "C) Global pooling",
        "D) Median pooling"
    ],
    'correct_answer': 'D',
    'explanation': "Median pooling is not commonly used in CNNs, whereas max pooling, average pooling, and global pooling are typical pooling operations.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_mpc_question_3 = {
    'question': "How does max pooling typically operate on a 2x2 region of a feature map?",
    'options_list': [
        "A) It computes the average of the 4 values",
        "B) It selects the maximum value among the 4",
        "C) It sums up all 4 values",
        "D) It multiplies all 4 values together"
    ],
    'correct_answer': 'B',
    'explanation': "Max pooling selects the maximum value from the 2x2 region, which helps reduce the spatial dimensions while retaining the most prominent features.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_mpc_question_4 = {
    'question': "What is a key benefit of pooling layers introducing spatial invariance?",
    'options_list': [
        "A) It allows the network to detect features regardless of their exact location",
        "B) It increases the number of parameters in the network",
        "C) It makes the network more sensitive to small translations",
        "D) It expands the spatial dimensions of feature maps"
    ],
    'correct_answer': 'A',
    'explanation': "Pooling layers, especially max pooling, introduce spatial invariance by enabling the network to detect features irrespective of small translations in the input.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_tf_question_1 = {
    'question': "Pooling layers always use a stride equal to the size of the pooling window.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Pooling layers can use a stride smaller than the pooling window, resulting in overlapping pooling regions.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_tf_question_2 = {
    'question': "Max pooling tends to work better than average pooling for most computer vision tasks.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Max pooling is often more effective than average pooling because it captures the most prominent features in an input, which is crucial for tasks like object detection.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_tf_question_3 = {
    'question': "Pooling layers increase the computational complexity of convolutional neural networks.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Pooling layers reduce computational complexity by downsampling the input and reducing the number of parameters for subsequent layers.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_tf_question_4 = {
    'question': "The choice of pooling operation and pooling region size has no impact on a CNN's performance.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The choice of pooling operation and the pooling region size can significantly affect the performance of a CNN, influencing factors such as spatial resolution and feature retention.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}

deep_learning_book_9_2_9_3_tf_question_5 = {
    'question': "Pooling layers can help make CNNs more robust to small positional changes of features in the input.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Pooling introduces spatial invariance, which helps CNNs become more robust to small positional changes in the input features.",
    'chapter_information': 'Deep Learning Book 9.2 and 9.3'
}


deep_learning_book_9_4_9_5_mpc_question_1 = {
    'question': "What does the function g(G, V, s) compute in the context of training a convolutional network?",
    'options_list': [
        "A) The forward pass output",
        "B) The gradient with respect to the input",
        "C) The gradient with respect to the kernel weights",
        "D) The loss function"
    ],
    'correct_answer': 'C',
    'explanation': "The function g(G, V, s) computes the gradient with respect to the kernel weights in the context of backpropagation during training.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_mpc_question_2 = {
    'question': "In the equation for h(K, G, s), what does this function represent?",
    'options_list': [
        "A) The forward convolution operation",
        "B) The gradient with respect to the input V",
        "C) The gradient with respect to the kernel K",
        "D) The transpose convolution operation"
    ],
    'correct_answer': 'B',
    'explanation': "The function h(K, G, s) computes the gradient with respect to the input V, which is used for backpropagating the error in convolutional networks.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_mpc_question_3 = {
    'question': "For a convolutional autoencoder, which function is used to perform the transpose of the convolution operation?",
    'options_list': [
        "A) c(K, V, s)",
        "B) g(G, V, s)",
        "C) h(K, G, s)",
        "D) J(V, K)"
    ],
    'correct_answer': 'C',
    'explanation': "In convolutional autoencoders, h(K, G, s) is used to perform the transpose of the convolution operation.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_mpc_question_4 = {
    'question': "How are biases typically shared in convolutional layers?",
    'options_list': [
        "A) One bias per input channel",
        "B) One bias per output channel, shared across locations",
        "C) One unique bias for each output location",
        "D) Biases are not used in convolutional layers"
    ],
    'correct_answer': 'B',
    'explanation': "In convolutional layers, biases are typically shared across all locations for each output channel.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_tf_question_1 = {
    'question': "The function c(K, V, s) represents the forward pass of a strided convolution operation.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The function c(K, V, s) represents the forward pass of a convolution operation with strides.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_tf_question_2 = {
    'question': "In convolutional autoencoders, g(H, E, s) is used to compute the gradient with respect to the encoder weights.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The function g(H, E, s) is used to compute the gradient with respect to the kernel in the decoder, not the encoder.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_tf_question_3 = {
    'question': "Using separate biases for each output location always improves the statistical efficiency of the model.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Using separate biases for each output location may reduce the statistical efficiency of the model, though it allows the model to account for differences in image statistics at different locations.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_tf_question_4 = {
    'question': "The equations presented in the text are for the two-dimensional, single example version of convolutional operations.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The equations presented focus on the two-dimensional, single example version of convolutional operations.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}

deep_learning_book_9_4_9_5_tf_question_5 = {
    'question': "Tiled convolution uses the same bias sharing pattern as the kernel tiling pattern.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Tiled convolution shares biases in the same pattern as the tiling of kernels across the input, ensuring consistency in parameter sharing.",
    'chapter_information': 'Deep Learning Book 9.4 and 9.5'
}


deep_learning_book_9_6_9_8_mpc_question_1 = {
    'question': "What are the three basic strategies mentioned for obtaining convolution kernels without supervised training?",
    'options_list': [
        "A) Random initialization, hand-designed kernels, unsupervised learning",
        "B) Supervised learning, transfer learning, fine-tuning",
        "C) Gradient descent, momentum, Adam optimization",
        "D) Data augmentation, regularization, early stopping"
    ],
    'correct_answer': 'A',
    'explanation': "The text mentions three strategies for obtaining convolution kernels without supervised training: random initialization, hand-designed kernels, and unsupervised learning.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_mpc_question_2 = {
    'question': "According to the text, what is an advantage of learning features with an unsupervised criterion?",
    'options_list': [
        "A) It always results in better classification accuracy",
        "B) It allows features to be determined separately from the classifier layer",
        "C) It eliminates the need for a classifier layer entirely",
        "D) It requires less training data than supervised methods"
    ],
    'correct_answer': 'B',
    'explanation': "Learning features with an unsupervised criterion allows them to be determined separately from the classifier layer, enabling feature extraction to occur independently.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_mpc_question_3 = {
    'question': "What approach did Coates et al. (2011) use to learn convolution kernels in an unsupervised manner?",
    'options_list': [
        "A) Principal Component Analysis (PCA)",
        "B) Autoencoders",
        "C) K-means clustering",
        "D) Generative Adversarial Networks (GANs)"
    ],
    'correct_answer': 'C',
    'explanation': "Coates et al. (2011) used k-means clustering to learn convolution kernels from small image patches in an unsupervised manner.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_mpc_question_4 = {
    'question': "What is the 'canonical example' of greedy layer-wise pretraining for convolutional models mentioned in the text?",
    'options_list': [
        "A) LeNet-5",
        "B) AlexNet",
        "C) Convolutional Deep Belief Network",
        "D) VGGNet"
    ],
    'correct_answer': 'C',
    'explanation': "The convolutional deep belief network is mentioned as the canonical example of greedy layer-wise pretraining for convolutional models.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_tf_question_1 = {
    'question': "Random filters often perform poorly in convolutional networks compared to learned filters.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Random filters have been shown to work surprisingly well in convolutional networks, particularly when followed by pooling layers.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_tf_question_2 = {
    'question': "Greedy layer-wise pretraining allows training very large models with high computational cost only at inference time.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Greedy layer-wise pretraining allows for efficient training of large models by reducing computational cost during training and incurring higher cost only at inference time.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_tf_question_3 = {
    'question': "As of the writing of this text, most convolutional networks are trained using unsupervised pretraining methods.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Most convolutional networks today are trained using fully supervised methods, with unsupervised pretraining being more common when labeled datasets were smaller.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_tf_question_4 = {
    'question': "Unsupervised pretraining may offer regularization benefits compared to purely supervised training.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Unsupervised pretraining may offer regularization benefits, though the exact causes of these benefits are not entirely understood.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

deep_learning_book_9_6_9_8_tf_question_5 = {
    'question': "The text suggests that the benefits of unsupervised pretraining are fully understood and can be clearly attributed to specific causes.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The text mentions that the benefits of unsupervised pretraining are not fully understood and it is difficult to attribute them to specific causes.",
    'chapter_information': 'Deep Learning Book 9.6-9.8'
}

# chapter_2_quiz_prep_mpc_question_1 = {
#     'question': "You have an input volume of 32×32×3. What are the dimensions of the resulting volume after convolving a 5×5 kernel with 0 padding (valid convolution), stride of 1, and 2 filters?",
#     'options_list': [
#         "A) 32×32×2",
#         "B) 28×28×2",
#         "C) 30×30×2",
#         "D) 28×28×3"
#     ],
#     'correct_answer': 'B',
#     'explanation': "For a valid convolution, the output size is reduced due to no padding. Using a 5×5 kernel with stride 1 results in an output size of 28×28 in each spatial dimension and 2 filters give a depth of 2.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_2 = {
#     'question': "How many weights and biases does the layer described in the previous question (input volume of 32×32×3, 5×5 kernel, valid convolution, stride of 1, and 2 filters) have?",
#     'options_list': [
#         "A) 150",
#         "B) 160",
#         "C) 152",
#         "D) 180"
#     ],
#     'correct_answer': 'C',
#     'explanation': "The number of parameters is calculated as (5×5×3)×2 + 2 biases, which gives 152 total parameters.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_3 = {
#     'question': "You want to process time-series data with a 1D CONV that has the same configuration as the layer described earlier (5×5 kernel, valid convolution, stride of 1, and 2 filters) but with a kernel size of 5. The input volume of shape T×3 models three fluctuating values over time. How many weights and biases does this layer have?",
#     'options_list': [
#         "A) 30",
#         "B) 32",
#         "C) 25",
#         "D) 28"
#     ],
#     'correct_answer': 'B',
#     'explanation': "For 1D CONV with a kernel size of 5, the number of parameters is (5×3)×2 filters + 2 biases, which results in 32.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_4 = {
#     'question': "Suppose you have an input volume of dimension 64×64×16. How many parameters would a single 1×1 convolutional filter have, including the bias?",
#     'options_list': [
#         "A) 16",
#         "B) 64",
#         "C) 17",
#         "D) 1"
#     ],
#     'correct_answer': 'C',
#     'explanation': "For a 1×1 convolutional filter with an input depth of 16, the number of parameters is 16 weights + 1 bias, which gives a total of 17 parameters.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_5 = {
#     'question': "Suppose your input is a 300×300 color (RGB) image, and you use a convolutional layer with 100 filters that are each 5×5. How many parameters does this layer have, including the bias parameters?",
#     'options_list': [
#         "A) 7600",
#         "B) 7500",
#         "C) 7200",
#         "D) 7800"
#     ],
#     'correct_answer': 'A',
#     'explanation': "The number of parameters is calculated as (5×5×3)×100 filters + 100 biases, which results in 7600 parameters.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_6 = {
#     'question': "You have an input volume that is 63×63×16 and convolve it with 32 filters that are each 7×7, with a stride of 1. You want to use a 'same' convolution. What is the padding?",
#     'options_list': [
#         "A) 1",
#         "B) 2",
#         "C) 3",
#         "D) 4"
#     ],
#     'correct_answer': 'C',
#     'explanation': "For a 'same' convolution with a 7×7 kernel, padding of 3 is required to maintain the input size of 63×63.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_7 = {
#     'question': "What is the output volume of a 32×32×16 input data after applying max pooling with a square kernel of size 2 and stride = 2?",
#     'options_list': [
#         "A) 32×32×16",
#         "B) 16×16×16",
#         "C) 16×16×32",
#         "D) 32×16×16"
#     ],
#     'correct_answer': 'B',
#     'explanation': "Max pooling with a 2×2 kernel and stride 2 reduces each spatial dimension by half, resulting in an output of 16×16×16.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_8 = {
#     'question': "What is the resulting volume of padding a 15×15×8 input volume using pad=2?",
#     'options_list': [
#         "A) 17×17×8",
#         "B) 19×19×8",
#         "C) 20×20×8",
#         "D) 15×15×8"
#     ],
#     'correct_answer': 'B',
#     'explanation': "Padding the input with pad=2 adds 2 units to each spatial dimension, resulting in a volume of 19×19×8.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

# chapter_2_quiz_prep_mpc_question_9 = {
#     'question': "You have an input volume of 101×101×3. What is the resulting width after performing a convolution with the following parameters: kernel size=7, stride=5, no padding?",
#     'options_list': [
#         "A) 20",
#         "B) 19",
#         "C) 18",
#         "D) 21"
#     ],
#     'correct_answer': 'B',
#     'explanation': "With no padding and a stride of 5, the resulting width is calculated as (101−7)/5 + 1 = 19.",
#     'chapter_information': 'Chapter 2 Quiz Prep'
# }

perplexity_quiz_prep_mpc_question_1 = {
    'question': "You have an input volume of 64×64×3. What are the dimensions of the resulting volume after applying a convolutional layer with 16 filters of size 3×3, stride of 2, and 'same' padding?",
    'options_list': [
        "A) 32×32×16",
        "B) 31×31×16",
        "C) 64×64×16",
        "D) 62×62×16"
    ],
    'correct_answer': 'A',
    'explanation': "With 'same' padding and a stride of 2, the output spatial dimensions are halved, giving an output volume of 32×32×16 with 16 filters.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_mpc_question_2 = {
    'question': "How many parameters (weights and biases) does a convolutional layer have with the following configuration: 64 filters of size 5×5, input volume 128×128×3?",
    'options_list': [
        "A) 4,800",
        "B) 4,864",
        "C) 9,600",
        "D) 9,664"
    ],
    'correct_answer': 'D',
    'explanation': "The number of parameters is calculated as (5×5×3)×64 filters + 64 biases, which results in 9,664 parameters.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_mpc_question_3 = {
    'question': "What is the output volume size after applying max pooling with a 2×2 kernel and stride of 2 to an input volume of 56×56×32?",
    'options_list': [
        "A) 28×28×32",
        "B) 27×27×32",
        "C) 28×28×16",
        "D) 54×54×32"
    ],
    'correct_answer': 'A',
    'explanation': "Max pooling with a 2×2 kernel and stride 2 reduces each spatial dimension by half, resulting in an output volume of 28×28×32.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_mpc_question_4 = {
    'question': "You have a 3D input volume of 16×16×16×8 (width×height×depth×channels). What is the output volume size after applying a 3D convolution with 32 filters of size 3×3×3, stride of 1, and 'valid' padding?",
    'options_list': [
        "A) 14×14×14×32",
        "B) 16×16×16×32",
        "C) 18×18×18×32",
        "D) 14×14×14×8"
    ],
    'correct_answer': 'A',
    'explanation': "For 'valid' padding, the output spatial dimensions are reduced by the size of the kernel minus 1 (3−1=2), giving an output volume of 14×14×14×32.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_tf_question_1 = {
    'question': "A 1×1 convolution with 64 filters applied to an input volume of 32×32×128 will result in an output volume of 32×32×64.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "A 1×1 convolution reduces only the depth of the input volume based on the number of filters used, resulting in 32×32×64 for 64 filters.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_tf_question_2 = {
    'question': "Applying 'same' padding to a convolutional layer always results in an output volume with the same spatial dimensions as the input volume, regardless of the kernel size and stride.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "While 'same' padding preserves spatial dimensions for stride=1, increasing the stride will reduce the output dimensions.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_tf_question_3 = {
    'question': "The number of parameters in a convolutional layer is independent of the input volume size.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The number of parameters in a convolutional layer depends on the kernel size and number of filters, not on the size of the input volume.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_tf_question_4 = {
    'question': "A max pooling layer with a 3×3 kernel and stride of 2 will reduce the spatial dimensions of the input by exactly one-third.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "A stride of 2 reduces the spatial dimensions by approximately half, not one-third.",
    'chapter_information': 'Perplexity Quiz Prep'
}

perplexity_quiz_prep_tf_question_5 = {
    'question': "In a 3D convolution, the number of channels in the output volume is always equal to the number of filters used, regardless of the number of input channels.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "In 3D convolutions, the number of output channels is determined by the number of filters, regardless of the input channels.",
    'chapter_information': 'Perplexity Quiz Prep'
}

university_of_michigan_lecture_8_mpc_question_1 = {
    'question': "You have an input volume of size 227×227×3. A convolutional layer applies 64 filters, each of size 11×11, with a stride of 4 and padding of 2. What are the dimensions of the resulting feature map after the convolution?",
    'options_list': [
        "A) 64×56×56",
        "B) 64×27×27",
        "C) 64×32×32",
        "D) 64×28×28"
    ],
    'correct_answer': 'A',
    'explanation': "For a convolutional layer with padding=2, stride=4, and kernel size=11, the formula for output size is: [(input size - kernel size + 2×padding) / stride] + 1. Thus, the resulting feature map dimensions are 64×56×56.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_2 = {
    'question': "You have an input volume of size 27×27×192. A max pooling layer with a 3×3 kernel, stride of 2, and padding of 0 is applied. What are the dimensions of the resulting volume after pooling?",
    'options_list': [
        "A) 192×27×27",
        "B) 192×13×13",
        "C) 192×14×14",
        "D) 192×6×6"
    ],
    'correct_answer': 'B',
    'explanation': "Max pooling with a 3×3 kernel, stride 2, and no padding reduces the size using the formula [(input size - kernel size) / stride] + 1. This gives an output size of 192×13×13.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_3 = {
    'question': "An input volume of size 13×13×192 is processed by a convolutional layer with 384 filters, each of size 3×3, with a stride of 1 and padding of 1. What are the dimensions of the resulting feature map?",
    'options_list': [
        "A) 384×27×27",
        "B) 384×13×13",
        "C) 256×13×13",
        "D) 192×13×13"
    ],
    'correct_answer': 'B',
    'explanation': "With padding of 1 and stride of 1, the spatial dimensions remain the same as the input, so the output volume size will be 384×13×13.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_4 = {
    'question': "You have an input volume of size 13×13×256. A convolutional layer applies 256 filters, each of size 3×3, with stride of 1 and padding of 1. What are the dimensions of the resulting feature map?",
    'options_list': [
        "A) 384×13×13",
        "B) 256×13×13",
        "C) 256×7×7",
        "D) 192×13×13"
    ],
    'correct_answer': 'B',
    'explanation': "With padding of 1 and a stride of 1, the output feature map dimensions will match the input dimensions, resulting in 256×13×13.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_5 = {
    'question': "A max pooling layer with a 3×3 kernel, stride of 2, and no padding is applied to an input volume of size 13×13×256. What are the dimensions of the resulting feature map?",
    'options_list': [
        "A) 256×13×13",
        "B) 256×6×6",
        "C) 256×7×7",
        "D) 256×8×8"
    ],
    'correct_answer': 'B',
    'explanation': "Max pooling reduces the dimensions based on the formula: [(input size - kernel size) / stride] + 1. This results in a feature map size of 256×6×6.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_6 = {
    'question': "You have an input volume of size 6×6×256. After flattening the output volume, what is the total number of features in the flattened output?",
    'options_list': [
        "A) 9216",
        "B) 4608",
        "C) 256",
        "D) 4096"
    ],
    'correct_answer': 'A',
    'explanation': "To flatten a 6×6×256 input, multiply the dimensions together: 6×6×256 = 9216 features.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_7 = {
    'question': "In a convolutional layer, what does $C_{\text{out}}$ represent?",
    'options_list': [
        "A) Input channels",
        "B) Output channels",
        "C) Kernel height",
        "D) Stride"
    ],
    'correct_answer': 'B',
    'explanation': "In a convolutional layer, $C_{\text{out}}$ refers to the number of output channels or filters.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_8 = {
    'question': "Which CNN architecture introduced the concept of residual connections?",
    'options_list': [
        "A) AlexNet",
        "B) VGG",
        "C) GoogleNet",
        "D) ResNet"
    ],
    'correct_answer': 'D',
    'explanation': "ResNet introduced the concept of residual connections, which allow the gradient to flow more easily through deep networks.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_9 = {
    'question': "What is the output height ($H'$) for a convolution with input height $H=32$, kernel size $K=3$, padding $P=1$, and stride $S=2$?",
    'options_list': [
        "A) 16",
        "B) 17",
        "C) 18",
        "D) 19"
    ],
    'correct_answer': 'A',
    'explanation': "Using the formula $H' = \frac{H - K + 2P}{S} + 1$, the output height is calculated as $H' = \frac{32 - 3 + 2(1)}{2} + 1 = 16$.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_mpc_question_10 = {
    'question': "Which of the following is NOT a common kernel size for CNNs?",
    'options_list': [
        "A) 1×1",
        "B) 3×3",
        "C) 5×5",
        "D) 7×7"
    ],
    'correct_answer': 'D',
    'explanation': "While 1×1, 3×3, and 5×5 kernels are common, 7×7 kernels are less frequently used.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_tf_question_1 = {
    'question': "The Pre-Activation ResNet Block applies BatchNorm and ReLU before each convolution.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The Pre-Activation ResNet block moves BatchNorm and ReLU before each convolutional layer for better gradient flow.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_tf_question_2 = {
    'question': "3D convolution is primarily used for processing 2D image data.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "3D convolution is used for processing volumetric data, such as video or medical scans, not 2D image data.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_tf_question_3 = {
    'question': "Global average pooling in GoogleNet replaced fully connected layers.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "GoogleNet used global average pooling to replace fully connected layers, reducing the number of parameters in the network.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_tf_question_4 = {
    'question': "The weight matrix in a convolutional layer has dimensions $C_{\text{out}} \times C_{\text{in}} \times K_H \times K_W$.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The weight matrix in a convolutional layer is defined by the number of filters (output channels) and their dimensions.",
    'chapter_information': 'University of Michigan Lecture 8'
}

university_of_michigan_lecture_8_tf_question_5 = {
    'question': "After ResNet, the focus in CNN architecture design shifted towards increasing network complexity.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "After ResNet, the focus shifted towards building more efficient networks rather than increasing complexity.",
    'chapter_information': 'University of Michigan Lecture 8'
}

gt_lecture_5_2_mpc_question_1 = {
    'question': "Given an input image of size 7×7×3 and a convolutional layer with a 3×3 kernel, stride of 1, and no padding, what will be the height and width of the output feature map?",
    'options_list': [
        "A) 5×5",
        "B) 6×6",
        "C) 7×7",
        "D) 3×3"
    ],
    'correct_answer': 'A',
    'explanation': "Using the formula $H_{\text{out}} = \frac{H_{\text{in}} - K + 2P}{S} + 1$, with no padding (P=0) and stride of 1, the output height and width are $5×5$.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_mpc_question_2 = {
    'question': "If you apply a convolutional layer with 6 kernels, each of size 3×3×3, to an input image of size 5×5×3 with padding of 1 and stride of 1, how many total parameters are involved in this layer (including biases)?",
    'options_list': [
        "A) 54",
        "B) 112",
        "C) 168",
        "D) 58"
    ],
    'correct_answer': 'B',
    'explanation': "Each kernel has 3×3×3 = 27 parameters, and each kernel has an additional bias term, making it 28 parameters per kernel. With 6 kernels, the total number of parameters is $28 × 6 = 168$.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_mpc_question_3 = {
    'question': "For an input volume of size 32×32×3, what is the output size after applying a convolutional layer with a 5×5 kernel, stride of 2, padding of 0, and 16 output channels?",
    'options_list': [
        "A) 16×16×16",
        "B) 14×14×16",
        "C) 32×32×16",
        "D) 28×28×16"
    ],
    'correct_answer': 'B',
    'explanation': "Using the formula $H_{\text{out}} = \frac{H_{\text{in}} - K + 2P}{S} + 1$, with $H_{\text{in}} = 32$, $K = 5$, $P = 0$, and $S = 2$, we get an output size of 14×14×16.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_mpc_question_4 = {
    'question': "In a convolutional layer, what does padding primarily control?",
    'options_list': [
        "A) The size of the input",
        "B) The number of output channels",
        "C) The spatial size of the output",
        "D) The number of kernels"
    ],
    'correct_answer': 'C',
    'explanation': "Padding is used to control the spatial size of the output by adding values (often zeros) around the input. It can help preserve the input size in the output.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_mpc_question_5 = {
    'question': "How does stride affect the output size in a convolution operation?",
    'options_list': [
        "A) Increases the depth of the output",
        "B) Reduces the spatial dimensions of the output",
        "C) Adds additional channels to the output",
        "D) Does not influence the output size"
    ],
    'correct_answer': 'B',
    'explanation': "Increasing the stride reduces the spatial dimensions of the output feature map by skipping pixels during the convolution process.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_tf_question_1 = {
    'question': "A stride larger than 1 reduces the spatial dimensions of the output feature map.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "When the stride is larger than 1, the kernel moves over the input faster, skipping pixels, which results in a reduced output size.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_tf_question_2 = {
    'question': "The depth of a kernel in a convolutional layer always matches the number of channels in the input image.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "For multi-channel inputs like RGB images, the kernel’s depth must match the number of input channels for proper convolution.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_tf_question_3 = {
    'question': "Zero-padding is used to ensure that the output size of a convolution layer is the same as the input size.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Zero-padding is commonly used to preserve the spatial dimensions of the input after convolution by padding the borders with zeros.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_tf_question_4 = {
    'question': "In a multi-kernel convolutional layer, the number of output channels is equal to the number of input channels.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The number of output channels is determined by the number of kernels, not the number of input channels. Each kernel produces its own output feature map.",
    'chapter_information': 'GT Lecture 5.2'
}

gt_lecture_5_2_tf_question_5 = {
    'question': "The output size formula for a convolution without padding is $H_{\text{out}} = \frac{H_{\text{in}} - K}{S} + 1$.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "For convolution without padding, the formula for the output size is $H_{\text{out}} = \frac{H_{\text{in}} - K}{S} + 1$.",
    'chapter_information': 'GT Lecture 5.2'
}

andrew_ng_regularization_quiz_1_question_1 = {
    'question': "If you have 10,000,000 examples, how would you split the train/dev/test set in a machine learning task to ensure sufficient data for both training and evaluation?",
    'options_list': [
        "A) 98% train, 1% dev, 1% test",
        "B) 33% train, 33% dev, 33% test",
        "C) 60% train, 20% dev, 20% test"
    ],
    'correct_answer': 'A',
    'explanation': "For large datasets like 10,000,000 examples, it is common to allocate a majority to training (e.g., 98%) while using smaller portions for dev and test (1% each) to maintain enough training data while still evaluating the model.",
    'chapter_information': 'Andrew Ng Regularization Quiz 1'
}

andrew_ng_regularization_quiz_1_question_2 = {
    'question': "In a supervised learning problem, how should the dev and test sets be chosen?",
    'options_list': [
        "A) Come from the same distribution",
        "B) Come from different distributions",
        "C) Be identical to each other (same X/y pairs)",
        "D) Have the same number of examples"
    ],
    'correct_answer': 'A',
    'explanation': "The dev and test sets should come from the same distribution to ensure that model evaluation is consistent and reflects real-world performance.",
    'chapter_information': 'Andrew Ng Regularization Quiz 1'
}

andrew_ng_regularization_quiz_1_question_3 = {
    'question': "If your neural network model seems to have high bias (indicating underfitting), what of the following would be promising things to try? (Check all that apply)",
    'options_list': [
        "A) Make the neural network deeper",
        "B) Get more test data",
        "C) Get more training data",
        "D) Increase the number of units in each hidden layer",
        "E) Add regularization"
    ],
    'correct_answer': ['A', 'D'],
    'explanation': "High bias indicates underfitting, which can often be mitigated by making the network deeper or increasing the number of units in each hidden layer. Getting more data or adding regularization would not necessarily help in this case.",
    'chapter_information': 'Andrew Ng Regularization Quiz 1'
}

andrew_ng_regularization_quiz_1_question_4 = {
    'question': "You are building a classifier for apples, bananas, and oranges, and your model shows a training error of 0.5% and a dev set error of 7%. Which of the following are promising things to try to improve the classifier's performance? (Check all that apply)",
    'options_list': [
        "A) Increase the regularization parameter lambda",
        "B) Decrease the regularization parameter lambda",
        "C) Get more training data",
        "D) Use a bigger neural network"
    ],
    'correct_answer': ['B', 'C'],
    'explanation': "A high dev set error relative to the training error often indicates overfitting. Decreasing the regularization parameter and getting more training data can help reduce this overfitting.",
    'chapter_information': 'Andrew Ng Regularization Quiz 1'
}

andrew_ng_regularization_quiz_1_question_5 = {
    'question': "In the context of neural networks, what is weight decay?",
    'options_list': [
        "A) A regularization technique such as L2 regularization that results in gradient descent shrinking the weights on every iteration.",
        "B) Gradual corruption of the weights in the neural network if it is trained on noisy data.",
        "C) The process of gradually decreasing the learning rate during training.",
        "D) A technique to avoid vanishing gradient by imposing a ceiling on the values of the weights."
    ],
    'correct_answer': 'A',
    'explanation': "Weight decay is another term for L2 regularization, which applies a penalty on large weights during training by shrinking the weights after each iteration.",
    'chapter_information': 'Andrew Ng Regularization Quiz 1'
}

andrew_ng_regularization_quiz_1_question_6 = {
    'question': "What happens when you increase the regularization hyperparameter lambda in a neural network model?",
    'options_list': [
        "A) Weights are pushed toward becoming smaller (closer to 0)",
        "B) Weights are pushed toward becoming bigger (further from 0)",
        "C) Doubling lambda should roughly result in doubling the weights",
        "D) Gradient descent takes bigger steps with each iteration (proportional to lambda)"
    ],
    'correct_answer': 'A',
    'explanation': "Increasing lambda encourages weight shrinkage, pushing weights toward 0, which helps prevent overfitting by reducing model complexity.",
    'chapter_information': 'Andrew Ng Regularization Quiz 1'
}

andrew_ng_regularization_quiz_1_question_7 = {
    'question': "With the inverted dropout technique, what happens at test time during the forward pass?",
    'options_list': [
        "A) You apply dropout (randomly eliminating units) but keep the 1/keep_prob factor in the calculations used in training.",
        "B) You do not apply dropout (do not randomly eliminate units) and do not keep the 1/keep_prob factor in the calculations used in training.",
        "C) You apply dropout (randomly eliminating units) and do not keep the 1/keep_prob factor in the calculations used in training."
    ],
    'correct_answer': 'B',
    'explanation': "In the inverted dropout technique, dropout is not applied during test time, and the keep_prob scaling is not used in the test calculations.",
    'chapter_information': 'Andrew Ng Regularization Quiz 1'
}

andrew_ng_optimization_algorithms_quiz_2_question_2 = {
    'question': "Which of these statements about mini-batch gradient descent do you agree with?",
    'options_list': [
        "A) One iteration of mini-batch gradient descent (computing on a single mini-batch) is faster than one iteration of batch gradient descent.",
        "B) Training one epoch (one pass through the training set) using mini-batch gradient descent is faster than training one epoch using batch gradient descent.",
        "C) You should implement mini-batch gradient descent without an explicit for-loop over different mini-batches, so that the algorithm processes all mini-batches at the same time (vectorization)."
    ],
    'correct_answer': 'A',
    'explanation': "One iteration of mini-batch gradient descent processes fewer examples than batch gradient descent, which is why it is typically faster.",
    'chapter_information': 'Andrew Ng Optimization Algorithms Quiz 2'
}

andrew_ng_optimization_algorithms_quiz_2_question_3 = {
    'question': "Why is the best mini-batch size usually not 1 and not m (the full training set), but instead something in-between?",
    'options_list': [
        "A) If the mini-batch size is m, you end up with batch gradient descent, which has to process the whole training set before making progress.",
        "B) If the mini-batch size is m, you end up with stochastic gradient descent, which is usually slower than mini-batch gradient descent.",
        "C) If the mini-batch size is 1, you lose the benefits of vectorization across examples in the mini-batch.",
        "D) If the mini-batch size is 1, you end up having to process the entire training set before making any progress."
    ],
    'correct_answer': ['A', 'C'],
    'explanation': "Mini-batch gradient descent strikes a balance between processing multiple examples for vectorization efficiency while making progress faster than batch gradient descent (which processes the entire training set).",
    'chapter_information': 'Andrew Ng Optimization Algorithms Quiz 2'
}

andrew_ng_optimization_algorithms_quiz_2_question_5 = {
    'question': "Suppose the temperature in Casablanca over the first three days of January is constant: $ \theta_1 = 10^{\circ}C $, $ \theta_2 = 10^{\circ}C $. You use an exponentially weighted average with $ \beta = 0.5 $ to track the temperature: $ v_0 = 0 $, $ v_t = \beta v_{t-1} + (1 - \beta) \theta_t $. If $ v_2 $ is the value computed after day 2 without bias correction and $ v_2^{\text{corrected}} $ is the value you compute with bias correction, what are these values?",
    'options_list': [
        "A) $ v_2 = 7.5, v_2^{\text{corrected}} = 10 $",
        "B) $ v_2 = 10, v_2^{\text{corrected}} = 10 $",
        "C) $ v_2 = 10, v_2^{\text{corrected}} = 7.5 $",
        "D) $ v_2 = 7.5, v_2^{\text{corrected}} = 7.5 $"
    ],
    'correct_answer': 'A',
    'explanation': "Without bias correction, the exponentially weighted average is $ v_2 = 7.5 $, but with bias correction, it compensates for the initialization and yields $ v_2^{\text{corrected}} = 10 $.",
    'chapter_information': 'Andrew Ng Optimization Algorithms Quiz 2'
}

andrew_ng_optimization_algorithms_quiz_2_question_6 = {
    'question': "Which of these is NOT a good learning rate decay scheme? Here, t is the epoch number.",
    'options_list': [
        "A) $ \alpha = \frac{1}{1 + 2 + 3 + t} \alpha_0 $",
        "B) $ \alpha = 0.95^t \alpha_0 $",
        "C) $ \alpha = e^t \alpha_0 $",
        "D) $ \alpha = \frac{1}{\sqrt{t}} \alpha_0 $"
    ],
    'correct_answer': 'C',
    'explanation': "A learning rate that increases exponentially as the epoch progresses is not suitable as it would cause divergence during training. The other decay schemes gradually reduce the learning rate.",
    'chapter_information': 'Andrew Ng Optimization Algorithms Quiz 2'
}

andrew_ng_optimization_algorithms_quiz_2_question_9 = {
    'question': "Suppose batch gradient descent in a deep network is taking excessively long to find parameter values that achieve a small value for the cost function $ J(\mathbf{w}^{[1]}, \mathbf{b}^{[1]}, \ldots, \mathbf{w}^{[L]}, \mathbf{b}^{[L]}) $. Which of the following techniques could help find parameter values that attain a small value for $ J $? (Check all that apply)",
    'options_list': [
        "A) Try using Adam",
        "B) Try better random initialization for the weights",
        "C) Try tuning the learning rate $ \alpha $",
        "D) Try initializing all the weights to zero",
        "E) Try mini-batch gradient descent"
    ],
    'correct_answer': ['A', 'B', 'C', 'E'],
    'explanation': "Using Adam, better initialization, tuning the learning rate, and using mini-batch gradient descent can all help speed up convergence in deep networks.",
    'chapter_information': 'Andrew Ng Optimization Algorithms Quiz 2'
}

andrew_ng_optimization_algorithms_quiz_2_question_10 = {
    'question': "Which of the following statements about the Adam optimization algorithm is false?",
    'options_list': [
        "A) We usually use 'default' values for the hyperparameters $ \beta_1, \beta_2 $ and $ \epsilon $ in Adam ($ \beta_1 = 0.9, \beta_2 = 0.999, \epsilon = 10^{-8} $).",
        "B) The learning rate hyperparameter $ \alpha $ in Adam usually needs to be tuned.",
        "C) Adam combines the advantages of RMSProp and momentum.",
        "D) Adam should be used with batch gradient computations, not with mini-batches."
    ],
    'correct_answer': 'D',
    'explanation': "Adam is designed to work well with mini-batches. The statement that it should be used with batch gradient computations is false.",
    'chapter_information': 'Andrew Ng Optimization Algorithms Quiz 2'
}


andrew_ng_hyperparameter_tuning_quiz_3_question_1 = {
    'question': "If searching among a large number of hyperparameters, you should try values in a grid rather than random values so that you can carry out the search more systematically and not rely on chance. True or False?",
    'options_list': [
        "A) True",
        "B) False"
    ],
    'correct_answer': 'B',
    'explanation': "While grid search may seem systematic, random search is often more efficient and can cover a broader range of values, leading to better hyperparameter optimization.",
    'chapter_information': 'Andrew Ng Hyperparameter Tuning Quiz 3'
}

andrew_ng_hyperparameter_tuning_quiz_3_question_2 = {
    'question': "Every hyperparameter, if set poorly, can have a huge negative impact on training, and so all hyperparameters are about equally important to tune well. True or False?",
    'options_list': [
        "A) True",
        "B) False"
    ],
    'correct_answer': 'B',
    'explanation': "Not all hyperparameters are equally important. For example, the learning rate tends to be more critical than other hyperparameters like the batch size.",
    'chapter_information': 'Andrew Ng Hyperparameter Tuning Quiz 3'
}

andrew_ng_hyperparameter_tuning_quiz_3_question_3 = {
    'question': "During hyperparameter search, whether you try to babysit one model ('Panda' strategy) or train a lot of models in parallel ('Caviar' strategy) is largely determined by:",
    'options_list': [
        "A) Whether you use batch or mini-batch optimization",
        "B) The presence of local minima (and saddle points) in your neural network",
        "C) The amount of computational power you can access",
        "D) The number of hyperparameters you have to tune"
    ],
    'correct_answer': 'C',
    'explanation': "The 'Caviar' strategy (training many models in parallel) requires more computational power than the 'Panda' strategy (babysitting one model).",
    'chapter_information': 'Andrew Ng Hyperparameter Tuning Quiz 3'
}

andrew_ng_hyperparameter_tuning_quiz_3_question_4 = {
    'question': "If you think $ \beta $ (hyperparameter for momentum) is between 0.9 and 0.99, which of the following is the recommended way to sample a value for $ \beta $?",
    'options_list': [
        "A) beta = 0.9 + random.rand()",
        "B) beta = 0.9 + (0.99 - 0.9) * random.rand()",
        "C) beta = 1 - 10^{(random.rand() - 1)}"
    ],
    'correct_answer': 'C',
    'explanation': "The recommended method for sampling a value of $ \beta $ is to use $ \beta = 1 - 10^{(random.rand() - 1)} $, as it samples effectively from the logarithmic scale.",
    'chapter_information': 'Andrew Ng Hyperparameter Tuning Quiz 3'
}

andrew_ng_hyperparameter_tuning_quiz_3_question_5 = {
    'question': "Finding good hyperparameter values is very time-consuming. So typically you should do it once at the start of the project and try to find very good hyperparameters so that you don’t ever have to revisit tuning them again. True or False?",
    'options_list': [
        "A) True",
        "B) False"
    ],
    'correct_answer': 'B',
    'explanation': "Hyperparameter tuning is often an iterative process. It is common to revisit and adjust hyperparameters throughout the project as needed.",
    'chapter_information': 'Andrew Ng Hyperparameter Tuning Quiz 3'
}

andrew_ng_hyperparameter_tuning_quiz_3_question_6 = {
    'question': "In batch normalization as presented in the videos, if you apply it on the $l$-th layer of your neural network, what are you normalizing?",
    'options_list': [
        "A) $y^{(l)}$",
        "B) $z^{(l)}$",
        "C) $b^{(l)}$",
        "D) $a^{(l)}$"
    ],
    'correct_answer': 'B',
    'explanation': "In batch normalization, the normalization is applied to $z^{(l)}$, which is the input to the activation function for layer $l$.",
    'chapter_information': 'Andrew Ng Hyperparameter Tuning Quiz 3'
}

andrew_ng_hyperparameter_tuning_quiz_3_question_7 = {
    'question': "In the normalization formula $z_{norm} = \frac{z - \mu}{\sqrt{\sigma^2 + \epsilon}}$, why do we use epsilon?",
    'options_list': [
        "A) To speed up convergence",
        "B) To have a more accurate normalization",
        "C) In case $ \mu $ is too small",
        "D) To avoid division by zero"
    ],
    'correct_answer': 'D',
    'explanation': "The $ \epsilon $ term is added to avoid division by zero in case $ \sigma^2 $ is very small.",
    'chapter_information': 'Andrew Ng Hyperparameter Tuning Quiz 3'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_3_MPC = KC_MPC_QUESTIONS[:-1]
