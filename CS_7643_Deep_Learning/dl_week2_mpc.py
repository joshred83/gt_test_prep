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



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
