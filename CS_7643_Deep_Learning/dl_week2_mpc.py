monzersaleh_notes_question_1nn = {
    'question': "What is the primary difference between a linear classifier and a simple neural network?",
    'options_list': [
        'A neural network has multiple layers while a linear classifier has only one layer.',
        'A linear classifier uses non-linear activation functions.',
        'A neural network cannot be used for classification tasks.',
        'A linear classifier always has a higher accuracy than a neural network.'
    ],
    'correct_answer': 'A neural network has multiple layers while a linear classifier has only one layer.',
    'explanation': "A simple neural network has a similar structure to a linear classifier but includes multiple layers, whereas a linear classifier typically consists of only one layer.",
    'chapter_information': 'Monzersaleh Notes on Neural Networks'
}

monzersaleh_notes_question_2nn = {
    'question': "In a multi-layer neural network, what is the role of the 'hidden layer'?",
    'options_list': [
        'It directly outputs the final prediction.',
        'It processes the input data to create intermediate representations.',
        'It is used to initialize the weights of the network.',
        'It is only used during backpropagation.'
    ],
    'correct_answer': 'It processes the input data to create intermediate representations.',
    'explanation': "The hidden layer in a neural network is used to process input data, creating intermediate representations that are passed to the output layer for final predictions.",
    'chapter_information': 'Monzersaleh Notes on Neural Networks'
}

monzersaleh_notes_question_3nn = {
    'question': "What is the purpose of backpropagation in a neural network?",
    'options_list': [
        'To initialize the weights of the network randomly.',
        'To update the weights by calculating the gradient of the loss function with respect to each weight.',
        'To add regularization to the network to prevent overfitting.',
        'To ensure that the network converges to a global minimum.'
    ],
    'correct_answer': 'To update the weights by calculating the gradient of the loss function with respect to each weight.',
    'explanation': "Backpropagation calculates the gradient of the loss function with respect to each weight in the network, which is then used to update the weights and reduce the loss.",
    'chapter_information': 'Monzersaleh Notes on Neural Networks'
}

monzersaleh_notes_question_4nn = {
    'question': "What type of function can be used in the layers of a neural network?",
    'options_list': [
        'Only linear functions',
        'Any differentiable function',
        'Only exponential functions',
        'Only sigmoid functions'
    ],
    'correct_answer': 'Any differentiable function',
    'explanation': "In a neural network, any differentiable function can be used as an activation function, allowing for a wide variety of models and architectures.",
    'chapter_information': 'Monzersaleh Notes on Neural Networks'
}

monzersaleh_notes_question_5nn = {
    'question': "What is the key characteristic of a ReLU (Rectified Linear Unit) activation function?",
    'options_list': [
        'It always outputs a negative value.',
        'It provides non-linearity but allows better gradient flow than the sigmoid function.',
        'It is only used in the output layer of the network.',
        'It has a higher computational complexity than sigmoid functions.'
    ],
    'correct_answer': 'It provides non-linearity but allows better gradient flow than the sigmoid function.',
    'explanation': "The ReLU activation function is popular because it introduces non-linearity into the model while allowing better gradient flow, making it more effective than sigmoid functions in many applications.",
    'chapter_information': 'Monzersaleh Notes on Neural Networks'
}

deep_learning_ch6_truefalse_quaestion_1 = {
    'question': "True or False: In a neural network, applying a rectified linear unit (ReLU) activation function element-wise guarantees that the outputs of all neurons will be strictly positive.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "ReLU outputs zero for any negative input, meaning it does not guarantee strictly positive outputs, only non-negative ones.",
    'chapter_information': 'Deep Learning Book Chapter 6.1'
}

deep_learning_ch6_truefalse_qauestion_2 = {
    'question': "True or False: The rectified linear unit (ReLU) activation function is applied element-wise in neural networks and can introduce non-linearity by transforming a linearly inseparable problem into a linearly separable one.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "ReLU introduces non-linearity, which helps in solving problems like XOR that are not linearly separable in the input space.",
    'chapter_information': 'Deep Learning Book Chapter 6.1'
}

deep_learning_ch6a_mpc_question_1 = {
    'question': "Given the affine transformation $h = g(W^T x + c)$, what role does the bias vector $c$ play in this transformation?",
    'options_list': [
        "A) The bias vector scales the output of the transformation.",
        "B) The bias vector shifts the output of the transformation to avoid centering at zero.",
        "C) The bias vector adds non-linearity to the transformation.",
        "D) The bias vector has no effect on the transformation."
    ],
    'correct_answer': 'B',
    'explanation': "The bias vector shifts the output of the transformation, allowing the model to avoid centering at zero and increasing its expressiveness.",
    'chapter_information': 'Deep Learning Book Chapter 6.1'
}

deep_leaarning_ch6_mpc_question_2 = {
    'question': "In the XOR neural network example, after applying the weight matrix $W$ and bias vector $c$, the input is transformed to a space where the points lie on a line with slope 1. Which transformation is applied next to make the points linearly separable?",
    'options_list': [
        "A) Multiplication by the second weight matrix.",
        "B) Applying the ReLU activation function.",
        "C) Adding a new bias term.",
        "D) Multiplying by the final weight vector."
    ],
    'correct_answer': 'B',
    'explanation': "The ReLU activation function is applied element-wise to introduce non-linearity and make the points linearly separable.",
    'chapter_information': 'Deep Learning Book Chapter 6.1'
}

deep_learning_cah6_mpc_question_3 = {
    'question': "In the XOR problem, the weight matrix $W$ is given as $\\begin{bmatrix} 1 & 1 \\\\ 1 & 1 \\end{bmatrix}$. What does this matrix do when applied to the input vector $x$?",
    'options_list': [
        "A) It computes a weighted sum of the inputs for each neuron in the layer.",
        "B) It applies a non-linear transformation to the input vector.",
        "C) It shifts the input vector by a constant bias.",
        "D) It normalizes the input vector."
    ],
    'correct_answer': 'A',
    'explanation': "The matrix $W$ performs a weighted sum of the inputs, which is the standard operation in a neural network layer.",
    'chapter_information': 'Deep Learning Book Chapter 6.1'
}

deep_learning_ch6_mpc_questioan_4 = {
    'question': "In the XOR solution example, why does multiplying the input by the weight matrix $W$ and applying the ReLU transformation solve the problem?",
    'options_list': [
        "A) The ReLU transformation aligns the inputs into a single line where linear separation is possible.",
        "B) The ReLU activation adds non-linearity, allowing the model to solve the XOR problem, which is not linearly separable in the original input space.",
        "C) The ReLU function increases the dimensionality of the input space, making the problem solvable.",
        "D) The ReLU introduces randomness, which helps in finding the correct solution."
    ],
    'correct_answer': 'B',
    'explanation': "The ReLU activation introduces non-linearity, which allows the network to transform the input space such that the XOR problem becomes linearly separable.",
    'chapter_information': 'Deep Learning Book Chapter 6.1'
}

deep_learning_ch6_mpc_question_5a = {
    'question': "What does the expression $f(x; W, c, w, b) = w^T \\text{max}(0, W^T x + c) + b$ represent in a deep feedforward network?",
    'options_list': [
        "A) A complete neural network with one hidden layer and a ReLU activation.",
        "B) A linear transformation with a bias term.",
        "C) A convolutional neural network with a pooling layer.",
        "D) A recurrent neural network model."
    ],
    'correct_answer': 'A',
    'explanation': "This expression represents a neural network with one hidden layer where the ReLU activation function is applied element-wise.",
    'chapter_information': 'Deep Learning Book Chapter 6.1'
}

deep_learning_ch6_truefalse_question_3 = {
    'question': "True or False: A deep neural network consisting of only linear layers can still approximate non-linear functions.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "A deep network with only linear transformations is equivalent to a single linear transformation. Non-linearity is essential for deep networks to approximate complex functions.",
    'chapter_information': 'Deep Learning Book Chapter 6.2'
}

deep_learning_ch6_truefalse_question_4 = {
    'question': "True or False: The softmax function is commonly used as a hidden unit in most deep feedforward networks to represent probability distributions over a discrete variable.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "The softmax function is usually used in the output layer, not as a hidden unit. It represents a probability distribution over discrete outcomes.",
    'chapter_information': 'Deep Learning Book Chapter 6.3'
}

deep_learning_ch6_mpc_question_4 = {
    'question': "Which of the following is true about the transformation $h = g(W^T x + c)$ when $g(z)$ is a ReLU activation function?",
    'options_list': [
        "A) ReLU always outputs a value greater than 0 for any input.",
        "B) ReLU introduces non-linearity, allowing the model to learn complex functions.",
        "C) ReLU activation function is primarily used in recurrent neural networks.",
        "D) ReLU saturates for positive input values."
    ],
    'correct_answer': 'B',
    'explanation': "ReLU introduces non-linearity, which is crucial for deep networks to approximate complex functions. It outputs zero for negative inputs but does not saturate for positive inputs.",
    'chapter_information': 'Deep Learning Book Chapter 6.2'
}

deep_learning_ch6_mpc_question_5 = {
    'question': "Given the feedforward network with the activation function $g(a) = \\text{softplus}(a) = \\log(1 + e^a)$, which of the following is true?",
    'options_list': [
        "A) The softplus function behaves like the ReLU function for large values of $a$.",
        "B) The softplus function is bounded for large values of $a$.",
        "C) The softplus function is discontinuous.",
        "D) The softplus function tends to zero for negative values of $a$."
    ],
    'correct_answer': 'A',
    'explanation': "The softplus function behaves similarly to ReLU for large values of $a$, but is smooth and differentiable everywhere.",
    'chapter_information': 'Deep Learning Book Chapter 6.3'
}

deep_learning_ch6_mpc_question_6 = {
    'question': "In the radial basis function (RBF) unit, defined as $h_i = \\exp\\left(-\\frac{1}{\\sigma^2} \\| W_{:,i} - x \\|^2 \\right)$, what happens as the input $x$ moves further from the template $W_{:,i}$?",
    'options_list': [
        "A) The RBF unit becomes more active.",
        "B) The RBF unit approaches 1.",
        "C) The RBF unit approaches 0.",
        "D) The RBF unit output remains constant."
    ],
    'correct_answer': 'C',
    'explanation': "As $x$ moves further away from the template $W_{:,i}$, the RBF unit output approaches 0, indicating that it is less active.",
    'chapter_information': 'Deep Learning Book Chapter 6.3'
}

deep_learning_ch6_mpc_question_7 = {
    'question': "Consider a neural network where the first layer uses a weight matrix $W$ and the next layer uses weight matrix $U$. If the transformation is factored as $h = g(U^T V^T x + b)$, how does this affect the number of parameters in the model?",
    'options_list': [
        "A) The number of parameters remains the same.",
        "B) The number of parameters is reduced, especially for small $q$.",
        "C) The number of parameters increases.",
        "D) The model becomes less expressive."
    ],
    'correct_answer': 'B',
    'explanation': "Factoring the weight matrix reduces the number of parameters from $np$ to $(n + p)q$, which can be a considerable saving for small $q$.",
    'chapter_information': 'Deep Learning Book Chapter 6.3'
}

deep_learning_ch6_truefalse_ques1tion_5 = {
    'question': "True or False: The backpropagation algorithm applies the chain rule by computing the product of Jacobians and gradients for each operation in the computational graph.",
    'options_list': ["True", "False"],
    'correct_answer': 'True',
    'explanation': "Backpropagation uses the chain rule to compute the gradients by multiplying the Jacobian of each operation by the gradient from the subsequent layer.",
    'chapter_information': 'Deep Learning Book Chapter 6.4'
}

deep_learning_ch6_truefa1lse_question_6 = {
    'question': "True or False: In backpropagation, it is necessary to flatten all tensors into vectors before computing the gradients.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Conceptually, backpropagation works the same for tensors as it does for vectors, but there is no need to flatten tensors into vectors before computing the gradients.",
    'chapter_information': 'Deep Learning Book Chapter 6.4'
}

deep_lear1ning_ch6_mpc_question_8 = {
    'question': "Consider the function $z = f(y)$, where $y = g(x)$, with $x \in \mathbb{R}^m$ and $y \in \mathbb{R}^n$. The chain rule gives the gradient $\\nabla_x z$ as:",
    'options_list': [
        "A) $\\nabla_x z = \\nabla_y z \\cdot \\frac{\\partial y}{\\partial x}$",
        "B) $\\nabla_x z = \\frac{\\partial y}{\\partial x} \\cdot \\nabla_y z$",
        "C) $\\nabla_x z = \\nabla_x y \\cdot \\nabla_y z$",
        "D) $\\nabla_x z = \\nabla_y z \\cdot \\frac{\\partial z}{\\partial x}$"
    ],
    'correct_answer': 'B',
    'explanation': "The chain rule applied in vector notation is $\\nabla_x z = \\frac{\\partial y}{\\partial x} \\nabla_y z$, where $\\frac{\\partial y}{\\partial x}$ is the Jacobian matrix of $g$.",
    'chapter_information': 'Deep Learning Book Chapter 6.4'
}

deep_learning_ch6_mp1c_question_9 = {
    'question': "For a function $Y = g(X)$ and $z = f(Y)$, where $X$ and $Y$ are tensors, how is the chain rule for backpropagation written?",
    'options_list': [
        "A) $\\nabla_X z = \\nabla_Y z \\cdot \\frac{\\partial Y}{\\partial X}$",
        "B) $\\nabla_X z = \\sum_j (\\nabla_X Y_j) \\cdot \\frac{\\partial z}{\\partial Y_j}$",
        "C) $\\nabla_X z = \\frac{\\partial Y}{\\partial X} \\cdot \\nabla_Y z$",
        "D) $\\nabla_X z = \\nabla_X Y \\cdot \\frac{\\partial Y}{\\partial z}$"
    ],
    'correct_answer': 'B',
    'explanation': "For tensors, the chain rule is written as $\\nabla_X z = \\sum_j (\\nabla_X Y_j) \\frac{\\partial z}{\\partial Y_j}$.",
    'chapter_information': 'Deep Learning Book Chapter 6.4'
}

deep_learning_1ch6_mpc_question_10 = {
    'question': "In the equation $\\nabla_X z = \\sum_j (\\nabla_X Y_j) \\cdot \\frac{\\partial z}{\\partial Y_j}$, what does the term $\\nabla_X Y_j$ represent?",
    'options_list': [
        "A) The gradient of $Y_j$ with respect to $z$",
        "B) The Jacobian of $Y_j$ with respect to $X$",
        "C) The Hessian matrix of $X$ with respect to $Y_j$",
        "D) The gradient of $z$ with respect to $X$"
    ],
    'correct_answer': 'B',
    'explanation': "The term $\\nabla_X Y_j$ represents the Jacobian matrix of $Y_j$ with respect to $X$.",
    'chapter_information': 'Deep Learning Book Chapter 6.4'
}


deep_learning_ch6_truefalse_question_7 = {
    'question': "True or False: Backpropagation is the only method available for computing gradients in deep learning.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "Backpropagation is not the only method; there are other methods like automatic differentiation, and higher-order derivatives can be computed using methods like Krylov methods.",
    'chapter_information': 'Deep Learning Book Chapter 6.5'
}

deep_learning_ch6_truefalse_question_8 = {
    'question': "True or False: Computing the entire Hessian matrix is feasible in typical deep learning applications involving billions of parameters.",
    'options_list': ["True", "False"],
    'correct_answer': 'False',
    'explanation': "The Hessian matrix for large models can have billions of parameters, making it infeasible to compute directly. Instead, Krylov methods are used to compute Hessian-vector products.",
    'chapter_information': 'Deep Learning Book Chapter 6.5'
}

deep_learning_ch6_mpc_question_11 = {
    'question': "In the context of Hessian-vector products, what is the expression for computing the product between the Hessian matrix $H$ and a vector $v$?",
    'options_list': [
        "A) $H v = \\nabla_x \\langle \\nabla_x f(x) \\rangle v$",
        "B) $H v = \\nabla_x \\langle \\nabla_x f(x) \\cdot v \\rangle$",
        "C) $H v = \\nabla_x ( \\nabla_x f(x) ) v$",
        "D) $H v = \\nabla_x \\langle \\nabla_x f(x) \\rangle \\cdot v$"
    ],
    'correct_answer': 'B',
    'explanation': "The correct expression is $H v = \\nabla_x \\langle \\nabla_x f(x) \\rangle v$, where the Hessian-vector product can be computed using automatic differentiation libraries.",
    'chapter_information': 'Deep Learning Book Chapter 6.5'
}

deep_learning_ch6_mpc_question_12 = {
    'question': "What are Krylov methods used for in deep learning optimization?",
    'options_list': [
        "A) To compute the entire Hessian matrix explicitly.",
        "B) To approximate eigenvalues and eigenvectors of the Hessian matrix using only matrix-vector products.",
        "C) To compute gradients of scalar functions directly.",
        "D) To compute the Jacobian matrix of the model."
    ],
    'correct_answer': 'B',
    'explanation': "Krylov methods are used to approximate the eigenvalues and eigenvectors of the Hessian matrix without explicitly computing the entire matrix, relying only on matrix-vector products.",
    'chapter_information': 'Deep Learning Book Chapter 6.5'
}

automatic_differentiation_mpc_question_1 = {
    'question': "What is the primary distinction between automatic differentiation (AD) and symbolic differentiation, as outlined in Baydin et al. (2018)?",
    'options_list': [
        "A) AD computes exact numerical values of derivatives using the chain rule, while symbolic differentiation computes expressions for the derivatives.",
        "B) AD and symbolic differentiation are identical in functionality but differ in computational complexity.",
        "C) Symbolic differentiation is always more accurate than AD, especially for highly nonlinear functions.",
        "D) AD uses numerical approximations of the gradient, whereas symbolic differentiation computes derivatives exactly."
    ],
    'correct_answer': 'A',
    'explanation': "AD computes exact numerical values by propagating derivative values during code execution, avoiding the expression swell problem common in symbolic differentiation.",
    'chapter_information': 'Baydin et al. (2018), Section 2.2'
}

automatic_differentiation_mpc_question_2 = {
    'question': "Which of the following correctly describes the forward mode of automatic differentiation (AD) as explained in the paper?",
    'options_list': [
        "A) Forward mode AD is efficient for functions with many inputs and few outputs.",
        "B) Forward mode AD computes the gradient by performing backward passes through the computational graph.",
        "C) Forward mode AD is primarily used when the function has fewer inputs and more outputs.",
        "D) Forward mode AD requires n passes for n-dimensional input functions."
    ],
    'correct_answer': 'A',
    'explanation': "Forward mode AD is more efficient when there are few inputs and many outputs, as it calculates the derivative with respect to each input variable in a single pass.",
    'chapter_information': 'Baydin et al. (2018), Section 3.1'
}

automatic_differentiation_mpc_question_3 = {
    'question': "In reverse mode AD, how are gradients computed, as described by Baydin et al. (2018)?",
    'options_list': [
        "A) Gradients are computed by accumulating derivatives in the forward direction.",
        "B) Gradients are computed by propagating adjoints backward from the outputs to the inputs.",
        "C) Reverse mode AD computes the Jacobian matrix row-by-row using a single forward pass.",
        "D) Reverse mode AD is less efficient than forward mode for scalar-valued functions."
    ],
    'correct_answer': 'B',
    'explanation': "In reverse mode AD, gradients are propagated backward from the output using adjoints, which makes it highly efficient for functions with many inputs and few outputs.",
    'chapter_information': 'Baydin et al. (2018), Section 3.2'
}

automatic_differentiation_mpc_question_4 = {
    'question': "According to Baydin et al. (2018), which of the following is a key benefit of using AD in deep learning over manual or numerical differentiation?",
    'options_list': [
        "A) AD provides exact derivatives at machine precision with little computational overhead.",
        "B) AD simplifies the model structure by avoiding the need for control flow operations.",
        "C) Numerical differentiation is always faster than AD for large-scale deep learning models.",
        "D) Manual differentiation is preferred for training deep neural networks due to its flexibility."
    ],
    'correct_answer': 'A',
    'explanation': "AD provides accurate derivatives with only a small constant factor overhead, and it handles control flow and loops, which makes it advantageous for complex machine learning models.",
    'chapter_information': 'Baydin et al. (2018), Section 1'
}

automatic_differentiation_mpc_question_5 = {
    'question': "What is one major limitation of reverse mode AD in terms of memory usage, as discussed by Baydin et al. (2018)?",
    'options_list': [
        "A) Reverse mode AD requires significantly more computational time than forward mode AD.",
        "B) Reverse mode AD requires the storage of all intermediate values during the forward pass, leading to increased memory usage.",
        "C) Reverse mode AD cannot be used for functions with many outputs.",
        "D) Reverse mode AD has poor numerical stability when dealing with control flow."
    ],
    'correct_answer': 'B',
    'explanation': "Reverse mode AD stores all intermediate values during the forward pass to propagate adjoints, which increases memory usage, especially for long computational graphs.",
    'chapter_information': 'Baydin et al. (2018), Section 3.2'
}


pytorch_mpc_question_2 = {
    'question': "Which of the following is a characteristic of deep learning but not traditional machine learning?",
    'options_list': [
        "A) Consists of manually crafted features",
        "B) Works well with small datasets",
        "C) Requires large amounts of data to perform well",
        "D) Used only for supervised learning tasks"
    ],
    'correct_answer': 'C',
    'explanation': "Deep learning models typically need large datasets to achieve high performance.",
    'chapter_information': 'Packt Coursera PyTorch course, Deep Learning Concepts'
}

pytorch_mpc_question_3 = {
    'question': "Select all the correct statements about the process of gradient descent and the impact of learning rate on the optimization process in deep learning models.",
    'options_list': [
        "A) A very low learning rate can slow down the optimization process, potentially causing it to get stuck in local minima.",
        "B) A very low learning rate can indeed slow down the optimization process and cause it to get stuck in local minima.",
        "C) A very high learning rate can cause the optimization process to overshoot the minimum of the loss function.",
        "D) The optimal learning rate is the same for all types of neural network architectures.",
        "E) The learning rate does not affect the convergence speed of the gradient descent algorithm.",
        "F) Gradient descent is only used in deep learning and not in other machine learning algorithms.",
        "G) Gradient descent updates model parameters in the direction of the gradient of the loss function with respect to the parameters."
    ],
    'correct_answer': ['B', 'C', 'G'],
    'explanation': "A low learning rate slows optimization and can get stuck in local minima. A high learning rate can overshoot, and gradient descent updates parameters in the direction of the gradient of the loss.",
    'chapter_information': 'Packt Coursera PyTorch course, Optimization Techniques'
}

pytorch_mpc_question_4 = {
    'question': "What is the primary role of an optimizer in training a deep learning model?",
    'options_list': [
        "A) Increase the number of layers in the model",
        "B) Select the appropriate activation function",
        "C) Reduce overfitting by adding regularization",
        "D) Minimize the loss function"
    ],
    'correct_answer': 'D',
    'explanation': "The primary role of an optimizer is to minimize the loss function by adjusting model parameters.",
    'chapter_information': 'Packt Coursera PyTorch course, Optimizer Fundamentals'
}

pytorch_mpc_question_5 = {
    'question': "Which of the following activation functions is most likely to cause the vanishing gradient problem in deep neural networks?",
    'options_list': [
        "A) Tanh",
        "B) Softmax",
        "C) ReLU",
        "D) Sigmoid"
    ],
    'correct_answer': 'D',
    'explanation': "Sigmoid activation functions can cause the vanishing gradient problem because their gradients tend to be very small for large input values.",
    'chapter_information': 'Packt Coursera PyTorch course, Activation Functions'
}


pytorch_mpc_question_6 = {
    'question': "Identify the best practices for configuring the output layer in a neural network based on the type of problem.",
    'options_list': [
        "A) Use multiple nodes with Softmax activation for binary classification",
        "B) Use a large number of nodes with ReLU activation for regression problems",
        "C) Use Softmax activation for multi-class classification",
        "D) Use a single node with Sigmoid activation for binary classification",
        "E) Use a single node with Tanh activation for binary classification"
    ],
    'correct_answer': ['C', 'D'],
    'explanation': "Softmax activation is ideal for multi-class classification problems, and a single node with Sigmoid activation is appropriate for binary classification problems.",
    'chapter_information': 'Packt Coursera PyTorch course, Neural Network Output Layer'
}

pytorch_mpc_question_7 = {
    'question': "Select all elements of a Perceptron and their contributions to the functioning of a neural network.",
    'options_list': [
        "A) Bias",
        "B) Optimizer",
        "C) Loss Function",
        "D) Activation Function",
        "E) Weights",
        "F) Learning Rate"
    ],
    'correct_answer': ['A', 'D', 'E'],
    'explanation': "Bias helps to shift the activation function, activation functions determine if a neuron should be activated or not, and weights are learned during training and are used to make predictions.",
    'chapter_information': 'Packt Coursera PyTorch course, Perceptron Elements'
}

pytorch_mpc_question_8 = {
    'question': "Which of the following are advantages of K Fold Cross Validation?",
    'options_list': [
        "A) Reduces the risk of overfitting by testing the model on multiple data sets.",
        "B) Increases the complexity of the model by using more parameters.",
        "C) Eliminates the need for a separate test set.",
        "D) Provides a more reliable estimate of model performance."
    ],
    'correct_answer': ['A', 'C', 'D'],
    'explanation': "K Fold Cross Validation helps assess model generalization and provides a more reliable estimate of performance by averaging results from multiple folds.",
    'chapter_information': 'Packt Coursera PyTorch course, Cross Validation Techniques'
}

pytorch_mpc_question_9 = {
    'question': "In the context of training a neural network from scratch, which of the following is a key step in preprocessing the training data for heart attack detection?",
    'options_list': [
        "A) Initializing weights to zero",
        "B) Removing outliers by deleting rows with missing values",
        "C) Randomly shuffling the labels",
        "D) Scaling the features to a standard range"
    ],
    'correct_answer': 'D',
    'explanation': "Scaling features improves the convergence rate of the training algorithm by ensuring that all features are on a similar scale.",
    'chapter_information': 'Packt Coursera PyTorch course, Data Preprocessing'
}

pytorch_mpc_question_10 = {
    'question': "During the forward pass of a simple neural network, which mathematical operation is performed between the input features and the weights?",
    'options_list': [
        "A) Element-wise multiplication",
        "B) Dot product",
        "C) Matrix inversion",
        "D) Cross product"
    ],
    'correct_answer': 'B',
    'explanation': "The dot product operation is essential for computing the weighted sum of inputs in a neural network.",
    'chapter_information': 'Packt Coursera PyTorch course, Neural Network Forward Pass'
}

pytorch_mpc_question_11 = {
    'question': "Which of the following steps are involved in the training loop of a neural network?",
    'options_list': [
        "A) Hyperparameter tuning",
        "B) Backward pass",
        "C) Preprocessing data",
        "D) Forward pass",
        "E) Updating weights"
    ],
    'correct_answer': ['B', 'D', 'E'],
    'explanation': "The forward pass is used to compute the network's predictions, the backward pass calculates the gradients, and the weights are updated using the calculated gradients.",
    'chapter_information': 'Packt Coursera PyTorch course, Training Loops'
}

pytorch_mpc_question_12 = {
    'question': "What is the primary role of the optimizer in a neural network?",
    'options_list': [
        "A) To compute the forward pass outputs",
        "B) To preprocess input data",
        "C) To initialize the network's parameters",
        "D) To update weights and biases based on the calculated derivatives"
    ],
    'correct_answer': 'D',
    'explanation': "The optimizer modifies the weights and biases to minimize the loss function.",
    'chapter_information': 'Packt Coursera PyTorch course, Optimizers'
}

pytorch_mpc_question_13 = {
    'question': "Why is the derivative of the Sigmoid function significant during the neural network's forward pass?",
    'options_list': [
        "A) It improves the computational efficiency of the forward pass.",
        "B) It helps in updating the weights and biases during backpropagation.",
        "C) It initializes the network's parameters.",
        "D) It reduces the dimensionality of the input data."
    ],
    'correct_answer': 'B',
    'explanation': "The derivative of the Sigmoid function is used in backpropagation to update weights and biases.",
    'chapter_information': 'Packt Coursera PyTorch course, Activation Functions'
}

pytorch_mpc_question_14 = {
    'question': "In PyTorch, what is the role of the function torch.autograd.grad?",
    'options_list': [
        "A) It computes the gradient of a given tensor with respect to some scalar value.",
        "B) It creates a new tensor that tracks gradient computations.",
        "C) It initializes the weights of a neural network.",
        "D) It updates the tensors' values during training."
    ],
    'correct_answer': 'A',
    'explanation': "The torch.autograd.grad function computes the gradient of a specified tensor with respect to a scalar value, which is useful in the backward pass of neural networks.",
    'chapter_information': 'Packt Coursera PyTorch course, Autograd'
}

pytorch_mpc_question_15 = {
    'question': "When setting up a neural network model from scratch in PyTorch, which of the following components is essential to define the architecture of the model?",
    'options_list': [
        "A) The nn.Module class",
        "B) The DataLoader class",
        "C) The torch.optim module",
        "D) The torch.nn.functional module"
    ],
    'correct_answer': 'A',
    'explanation': "The nn.Module class is fundamental in PyTorch to define the architecture of your neural network model.",
    'chapter_information': 'Packt Coursera PyTorch course, Neural Network Setup'
}

pytorch_mpc_question_16 = {
    'question': "Which of the following are steps involved in the training loop of a PyTorch model?",
    'options_list': [
        "A) Set the model to evaluation mode.",
        "B) Initialize the model's parameters.",
        "C) Compute the loss based on the model's predictions and the true labels.",
        "D) Update the model's parameters using the optimizer.",
        "E) Perform backpropagation to compute gradients.",
        "F) Save the model's state dictionary."
    ],
    'correct_answer': ['C', 'D', 'E'],
    'explanation': "Computing the loss, updating the model's parameters, and performing backpropagation are essential steps in the training loop.",
    'chapter_information': 'Packt Coursera PyTorch course, Training Loop Steps'
}

pytorch_mpc_question_17 = {
    'question': "In the context of linear regression using PyTorch, what is the primary purpose of the Model class?",
    'options_list': [
        "A) To define the structure of the linear regression model and its forward pass.",
        "B) To handle data preprocessing steps like normalization and scaling.",
        "C) To implement the training loop and loss calculation.",
        "D) To save and load the model's parameters."
    ],
    'correct_answer': 'A',
    'explanation': "The primary purpose of the Model class is to define the structure of the linear regression model and its forward pass.",
    'chapter_information': 'Packt Coursera PyTorch course, Model Class'
}

pytorch_mpc_question_18 = {
    'question': "What is the primary benefit of partitioning data into batches during model training in PyTorch?",
    'options_list': [
        "A) It speeds up the training process by parallelizing computation.",
        "B) It helps in reducing overfitting by using batch normalization.",
        "C) It increases the model's accuracy by using smaller datasets.",
        "D) It enables the use of different optimization algorithms."
    ],
    'correct_answer': 'A',
    'explanation': "Partitioning data into batches speeds up the training process by parallelizing computation and improving memory efficiency.",
    'chapter_information': 'Packt Coursera PyTorch course, Batch Processing'
}

pytorch_mpc_question_19 = {
    'question': "In PyTorch, which method is used to manually modify the parameters of a neural network model?",
    'options_list': [
        "A) model.parameters()",
        "B) model.load_state_dict()",
        "C) model.state_dict()",
        "D) model.zero_grad()"
    ],
    'correct_answer': 'A',
    'explanation': "The model.parameters() method can be used to access and manually modify the parameters of a neural network model.",
    'chapter_information': 'Packt Coursera PyTorch course, Model Parameters'
}

pytorch_mpc_question_20 = {
    'question': "What is the primary advantage of using PyTorch for deep learning projects?",
    'options_list': [
        "A) Dynamic computational graphs",
        "B) Better GPU support than TensorFlow",
        "C) Simpler syntax for linear algebra",
        "D) Larger community and support"
    ],
    'correct_answer': 'A',
    'explanation': "Dynamic graphs are a key feature of PyTorch, allowing flexibility and ease of debugging.",
    'chapter_information': 'Packt Coursera PyTorch course, PyTorch Advantages'
}

pytorch_mpc_question_21 = {
    'question': "Which application is an example of artificial intelligence in the present day?",
    'options_list': [
        "A) Personalized recommendations on streaming services",
        "B) Static content websites",
        "C) Traditional programming loops",
        "D) Manual data entry"
    ],
    'correct_answer': 'A',
    'explanation': "Personalized recommendations on streaming services use AI to suggest content based on user preferences.",
    'chapter_information': 'Packt Coursera PyTorch course, AI Applications'
}

pytorch_mpc_question_22 = {
    'question': "What differentiates machine learning from classical programming?",
    'options_list': [
        "A) Machine learning models are always more accurate than classical programming",
        "B) Machine learning models do not need any data, while classical programming requires large datasets",
        "C) Machine learning models learn from data, while classical programming relies on explicit instructions",
        "D) Machine learning is only used in academic research, while classical programming is used in commercial applications"
    ],
    'correct_answer': 'C',
    'explanation': "Machine learning models use data to improve their performance, whereas classical programming relies on predefined rules.",
    'chapter_information': 'Packt Coursera PyTorch course, ML vs Classical Programming'
}

pytorch_mpc_question_23 = {
    'question': "Which activation function is most commonly used in hidden layers of a neural network due to its non-linear properties and ability to mitigate the vanishing gradient problem?",
    'options_list': [
        "A) Sigmoid",
        "B) Hyperbolic Tangent (Tanh)",
        "C) ReLU (Rectified Linear Unit)",
        "D) Softmax"
    ],
    'correct_answer': 'C',
    'explanation': "ReLU is widely used in hidden layers for its simplicity and effectiveness in mitigating the vanishing gradient problem.",
    'chapter_information': 'Packt Coursera PyTorch course, Activation Functions'
}

pytorch_mpc_question_24 = {
    'question': "What is the primary reason for the popularity and improvement of deep learning in recent years?",
    'options_list': [
        "A) Reduction in the cost of cloud storage",
        "B) Availability of large datasets",
        "C) Improvement in classical machine learning algorithms",
        "D) Advances in computational power, especially GPUs"
    ],
    'correct_answer': 'D',
    'explanation': "Advances in computational power, particularly GPUs, have significantly contributed to the rise of deep learning.",
    'chapter_information': 'Packt Coursera PyTorch course, Deep Learning Advancements'
}

pytorch_mpc_question_25 = {
    'question': "Which of the following statements about underfitting in machine learning models are correct?",
    'options_list': [
        "A) Underfitting typically results in high training error but low validation error.",
        "B) A model with high bias is likely to underfit the data.",
        "C) Data augmentation is a common technique used to address underfitting.",
        "D) Underfitting occurs when a model is too simple to capture the underlying patterns in the data.",
        "E) Underfitting can often be addressed by adding more features to the model or increasing its complexity.",
        "F) Underfitting can be diagnosed by evaluating the model's performance on the test set alone."
    ],
    'correct_answer': ['B', 'D', 'E'],
    'explanation': "High bias in a model often leads to underfitting as the model is too simplistic to capture the data's complexity. Underfitting is usually the result of a model that is too simple or lacks sufficient complexity, and increasing complexity or adding more features can help address underfitting.",
    'chapter_information': 'Packt Coursera PyTorch course, Underfitting in Machine Learning'
}

pytorch_mpc_question_26 = {
    'question': "Which of the following statements are true about K-fold Cross-Validation?",
    'options_list': [
        "A) It ensures that the training and validation sets are completely independent.",
        "B) It minimizes the bias in the performance estimate compared to a single train-test split.",
        "C) It helps in assessing the model's ability to generalize.",
        "D) It eliminates the need for a separate validation set."
    ],
    'correct_answer': ['B', 'C'],
    'explanation': "K-fold Cross-Validation reduces bias as every observation is used for both training and validation. It also provides a good estimate of model performance on unseen data.",
    'chapter_information': 'Packt Coursera PyTorch course, Cross-Validation Techniques'
}

pytorch_mpc_question_27 = {
    'question': "Which of the following metrics can be used to evaluate a neural network's performance?",
    'options_list': [
        "A) Training time",
        "B) Loss function value",
        "C) Learning rate",
        "D) Accuracy",
        "E) Confusion matrix"
    ],
    'correct_answer': ['B', 'D', 'E'],
    'explanation': "The loss function value indicates how well the neural network is performing. Accuracy is a primary metric used to evaluate performance, and the confusion matrix provides insights into classification performance.",
    'chapter_information': 'Packt Coursera PyTorch course, Performance Metrics'
}

pytorch_mpc_question_28 = {
    'question': "How is the derivative of the Sigmoid function significant in a neural network's forward pass?",
    'options_list': [
        "A) It is used to compute the activation of neurons.",
        "B) It is used during backpropagation to calculate gradients.",
        "C) It helps in setting the learning rate.",
        "D) It helps in normalizing the input data."
    ],
    'correct_answer': 'B',
    'explanation': "The derivative of the Sigmoid function is crucial during backpropagation as it helps in calculating the gradients.",
    'chapter_information': 'Packt Coursera PyTorch course, Activation Functions'
}

pytorch_mpc_question_29 = {
    'question': "Which of the following best describes the role of the optimizer in neural network training?",
    'options_list': [
        "A) It computes the loss function.",
        "B) It normalizes the input data.",
        "C) It updates the weights and biases using the calculated gradients.",
        "D) It adjusts the learning rate during training."
    ],
    'correct_answer': 'C',
    'explanation': "The optimizer uses the gradients calculated during backpropagation to update the weights and biases, thereby minimizing the loss.",
    'chapter_information': 'Packt Coursera PyTorch course, Optimizers in Neural Networks'
}

pytorch_mpc_question_30 = {
    'question': "Which function is used to perform a backward pass in PyTorch?",
    'options_list': [
        "A) autograd()",
        "B) forward()",
        "C) tensor()",
        "D) backward()"
    ],
    'correct_answer': 'D',
    'explanation': "The backward() function in PyTorch is used to perform a backward pass to compute the gradient of a tensor.",
    'chapter_information': 'Packt Coursera PyTorch course, Backward Pass'
}

pytorch_mpc_question_31 = {
    'question': "What is the primary purpose of the Autograd module in PyTorch?",
    'options_list': [
        "A) To create and manipulate tensors",
        "B) To build neural network layers",
        "C) To load and preprocess data",
        "D) To automatically calculate gradients"
    ],
    'correct_answer': 'D',
    'explanation': "The Autograd module in PyTorch is specifically designed to automatically calculate gradients, which are essential for optimizing neural networks.",
    'chapter_information': 'Packt Coursera PyTorch course, Autograd Module'
}

pytorch_mpc_question_32 = {
    'question': "What is the primary purpose of partitioning data into batches during model training?",
    'options_list': [
        "A) To increase the complexity of the model",
        "B) To efficiently use computational resources and stabilize gradient updates",
        "C) To ensure different data distributions are used in training",
        "D) To simplify the implementation of the model"
    ],
    'correct_answer': 'B',
    'explanation': "Partitioning data into batches helps efficiently use computational resources and stabilizes gradient updates.",
    'chapter_information': 'Packt Coursera PyTorch course, Data Batching'
}

pytorch_mpc_question_33 = {
    'question': "Which of the following hyperparameters can impact the performance of a neural network model?",
    'options_list': [
        "A) Batch size",
        "B) Number of layers",
        "C) Activation function",
        "D) Output data type",
        "E) Learning rate"
    ],
    'correct_answer': ['A', 'B', 'C', 'E'],
    'explanation': "Batch size affects the stability and efficiency of training, while the number of layers impacts the model's capacity to learn. The activation function and learning rate are also crucial as they influence the model's non-linearity and gradient descent step size, respectively.",
    'chapter_information': 'Packt Coursera PyTorch course, Hyperparameters'
}

pytorch_mpc_question_34 = {
    'question': "What is the role of the torch.save function in PyTorch?",
    'options_list': [
        "A) To save the state dictionary of a model for future use",
        "B) To train the model",
        "C) To initialize model parameters",
        "D) To define the model architecture"
    ],
    'correct_answer': 'A',
    'explanation': "The torch.save function is used to save the state dictionary of a model so it can be loaded and used later.",
    'chapter_information': 'Packt Coursera PyTorch course, Model Saving'
}

KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
