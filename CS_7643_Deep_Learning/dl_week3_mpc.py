

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







KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_3_MPC = KC_MPC_QUESTIONS[:-1]
