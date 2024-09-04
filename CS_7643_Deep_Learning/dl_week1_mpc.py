lecunn_article_question_1 = {
    'question': "What is the primary advantage of deep learning compared to conventional machine-learning techniques?",
    'options_list': [
        'It requires extensive hand-engineering of feature extractors',
        'It can automatically learn representations of data with multiple levels of abstraction',
        'It is limited to processing natural data in raw form',
        'It only works well with small datasets'
    ],
    'correct_answer': 'It can automatically learn representations of data with multiple levels of abstraction',
    'explanation': "Deep learning allows computational models to automatically learn representations of data with multiple levels of abstraction, reducing the need for extensive hand-engineering.",
    'chapter_information': 'Deep Learning in Nature Article'
}

lecunn_article_question_2 = {
    'question': "Which of the following statements about deep convolutional networks (ConvNets) is true?",
    'options_list': [
        'ConvNets are primarily used for sequential data like text and speech',
        'ConvNets require fully connected layers between all adjacent layers',
        'ConvNets are designed to process data that come in the form of multiple arrays',
        'ConvNets cannot be trained using backpropagation'
    ],
    'correct_answer': 'ConvNets are designed to process data that come in the form of multiple arrays',
    'explanation': "ConvNets are particularly well-suited for processing data that come in the form of multiple arrays, such as images, due to their local connections and shared weights.",
    'chapter_information': 'Deep Learning in Nature Article'
}

lecunn_article_question_3 = {
    'question': "What is the main function of pooling layers in a convolutional neural network?",
    'options_list': [
        'To detect local conjunctions of features from the previous layer',
        'To merge semantically similar features into one',
        'To apply a non-linear function like ReLU to the data',
        'To perform gradient descent more efficiently'
    ],
    'correct_answer': 'To merge semantically similar features into one',
    'explanation': "Pooling layers in convolutional neural networks reduce the dimensionality of the representation and help in making the network invariant to small shifts and distortions.",
    'chapter_information': 'Deep Learning in Nature Article'
}

lecunn_article_question_4 = {
    'question': "Why did deep learning methods initially struggle to gain widespread adoption?",
    'options_list': [
        'Because they require very few labeled examples to train',
        'Because gradient descent often got trapped in poor local minima',
        'Because they couldn\'t generalize well to new combinations of features',
        'Because they were too computationally expensive before the advent of GPUs'
    ],
    'correct_answer': 'Because gradient descent often got trapped in poor local minima',
    'explanation': "Deep learning methods initially struggled because gradient descent could get trapped in poor local minima, which made it difficult to optimize large networks effectively.",
    'chapter_information': 'Deep Learning in Nature Article'
}

lecunn_article_question_5 = {
    'question': "How do recurrent neural networks (RNNs) differ from feedforward neural networks?",
    'options_list': [
        'RNNs process input sequences in a random order',
        'RNNs maintain a state vector that contains information about the entire sequence history',
        'RNNs can only be used for image processing tasks',
        'RNNs are unable to learn long-term dependencies'
    ],
    'correct_answer': 'RNNs maintain a state vector that contains information about the entire sequence history',
    'explanation': "Recurrent neural networks differ from feedforward networks by maintaining a state vector that captures the entire sequence history, making them suitable for sequential data.",
    'chapter_information': 'Deep Learning in Nature Article'
}

lecunn_article_question_6 = {
    'question': "What is the significance of the rectified linear unit (ReLU) in deep learning?",
    'options_list': [
        'It smooths the learning process and prevents overfitting',
        'It allows the network to learn much faster, especially in deep networks',
        'It is a linear function that helps in gradient computation',
        'It is a pre-training technique used for initializing weights'
    ],
    'correct_answer': 'It allows the network to learn much faster, especially in deep networks',
    'explanation': "ReLU is significant in deep learning because it allows the network to learn much faster, particularly in deep networks, by providing a non-linear activation function that accelerates training.",
    'chapter_information': 'Deep Learning in Nature Article'
}

lecunn_article_question_7 = {
    'question': "What role do distributed representations play in deep learning?",
    'options_list': [
        'They increase the complexity of the model without improving performance',
        'They enable the model to generalize to new combinations of features not seen during training',
        'They are used only in unsupervised learning methods',
        'They prevent the model from learning any irrelevant features'
    ],
    'correct_answer': 'They enable the model to generalize to new combinations of features not seen during training',
    'explanation': "Distributed representations in deep learning allow models to generalize to new combinations of features beyond those seen during training, enhancing their ability to handle complex data.",
    'chapter_information': 'Deep Learning in Nature Article'
}

shannon_article_question_8 = {
    'question': "What is Claude E. Shannon's main concern about the popularity of information theory?",
    'options_list': [
        'That it will solve all communication problems effortlessly',
        'That it is being oversold and misapplied in fields beyond its core scope',
        'That it lacks any mathematical foundation',
        'That it is not being used enough in fields like psychology and economics'
    ],
    'correct_answer': 'That it is being oversold and misapplied in fields beyond its core scope',
    'explanation': "Shannon expresses concern that information theory is being oversold and applied inappropriately in fields where it may not be directly relevant.",
    'chapter_information': 'The Bandwagon by Claude E. Shannon'
}

shannon_article_question_9 = {
    'question': "According to Shannon, what is required for the successful application of information theory in fields like psychology and economics?",
    'options_list': [
        'A simple translation of concepts from information theory',
        'Extensive mathematical expertise',
        'A thorough understanding of the mathematical foundation and careful experimental verification',
        'The elimination of redundancy in communication'
    ],
    'correct_answer': 'A thorough understanding of the mathematical foundation and careful experimental verification',
    'explanation': "Shannon argues that successful application in other fields requires a deep understanding of the mathematical basis of information theory and careful experimental testing.",
    'chapter_information': 'The Bandwagon by Claude E. Shannon'
}

shannon_article_question_10 = {
    'question': "What does Shannon suggest as the best way to maintain the credibility and progress of information theory?",
    'options_list': [
        'Publishing as many papers as possible, regardless of quality',
        'Maintaining a scientific attitude and focusing on high-quality research',
        'Expanding the theory to cover as many fields as possible',
        'Simplifying the concepts to make them more accessible'
    ],
    'correct_answer': 'Maintaining a scientific attitude and focusing on high-quality research',
    'explanation': "Shannon emphasizes the importance of maintaining a rigorous scientific approach and prioritizing high-quality research over quantity to ensure the field's continued credibility and progress.",
    'chapter_information': 'The Bandwagon by Claude E. Shannon'
}

yxlows_notes_question_1 = {
    'question': "What is the primary purpose of the loss function in a machine learning model?",
    'options_list': [
        'To randomly adjust the weights of the model',
        'To measure how well the model performs on a given set of data',
        'To generate probabilities for different classes',
        'To optimize the gradient descent algorithm'
    ],
    'correct_answer': 'To measure how well the model performs on a given set of data',
    'explanation': "The loss function is used to quantify how well a model's predictions match the actual data, guiding the optimization process.",
    'chapter_information': 'Module 1: Introduction to Neural Networks - Lesson 1'
}

yxlows_notes_question_2 = {
    'question': "Which loss function is appropriate to use when converting scores to probabilities using the softmax function?",
    'options_list': [
        'Hinge loss',
        'Cross entropy',
        'L1 loss',
        'L2 loss'
    ],
    'correct_answer': 'Cross entropy',
    'explanation': "Cross entropy is the correct loss function to use with the softmax function, as it measures the difference between two probability distributions.",
    'chapter_information': 'Module 1: Introduction to Neural Networks - Lesson 1'
}

yxlows_notes_question_3 = {
    'question': "What is the size of the Jacobian matrix when computing the partial derivative of a scalar loss with respect to a matrix of weights W?",
    'options_list': [
        'A scalar',
        'A column vector',
        'A row vector',
        'A matrix'
    ],
    'correct_answer': 'A matrix',
    'explanation': "The Jacobian matrix contains the partial derivatives of the scalar loss with respect to each element in the matrix of weights W, resulting in a matrix.",
    'chapter_information': 'Module 1: Introduction to Neural Networks - Lesson 1'
}

yxlows_notes_question_4 = {
    'question': "What is the key characteristic of gradient descent that makes it effective for optimizing a machine learning model?",
    'options_list': [
        'It uses random search to find optimal weights',
        'It calculates the steepest descent direction by computing the negative gradient',
        'It only requires a small amount of data to work effectively',
        'It guarantees convergence to the global minimum'
    ],
    'correct_answer': 'It calculates the steepest descent direction by computing the negative gradient',
    'explanation': "Gradient descent optimizes the model by iteratively adjusting weights in the direction that reduces the loss function, guided by the negative gradient.",
    'chapter_information': 'Module 1: Introduction to Neural Networks - Lesson 1'
}

yxlows_notes_question_5 = {
    'question': "In the context of neural networks, what does 'End-to-End learning' refer to?",
    'options_list': [
        'Learning each layer of a network separately',
        'Learning feature extraction, representation, and classification simultaneously from raw data to final output',
        'Training the network only on the final layer',
        'Using a predefined set of features for classification'
    ],
    'correct_answer': 'Learning feature extraction, representation, and classification simultaneously from raw data to final output',
    'explanation': "End-to-End learning involves training the network to learn all parts of the process, from feature extraction to final classification, as part of a unified model.",
    'chapter_information': 'Module 1: Introduction to Neural Networks - Lesson 1'
}

mozersaleh_notes_question_1 = {
    'question': "What is a Linear Classifier primarily based on?",
    'options_list': [
        'Decision Trees',
        'Logistic Regression',
        'Linear Regression',
        'Support Vector Machines'
    ],
    'correct_answer': 'Linear Regression',
    'explanation': "A Linear Classifier is based on the concept of linear regression, which is represented in the form f(x,W)=Wx+b.",
    'chapter_information': 'Mozersaleh Notes on Linear Classifiers and Gradient Descent'
}

mozersaleh_notes_question_2 = {
    'question': "What is the purpose of backpropagation in the context of neural networks?",
    'options_list': [
        'To increase the complexity of the model',
        'To initialize the weights of the model',
        'To compute the gradients with respect to parameters and update them',
        'To perform data augmentation'
    ],
    'correct_answer': 'To compute the gradients with respect to parameters and update them',
    'explanation': "Backpropagation is used to compute the gradients of the loss function with respect to the model's parameters and to update the parameters accordingly.",
    'chapter_information': 'Mozersaleh Notes on Linear Classifiers and Gradient Descent'
}

mozersaleh_notes_question_3 = {
    'question': "Which of the following loss functions is commonly used with a softmax output in classification problems?",
    'options_list': [
        'Hinge loss',
        'Cross-entropy loss',
        'L1 loss',
        'L2 loss'
    ],
    'correct_answer': 'Cross-entropy loss',
    'explanation': "Cross-entropy loss is commonly used with softmax outputs to measure the difference between the predicted probability distribution and the actual distribution.",
    'chapter_information': 'Mozersaleh Notes on Linear Classifiers and Gradient Descent'
}

mozersaleh_notes_question_4 = {
    'question': "Which of the following methods is NOT a common way to compute partial derivatives in gradient descent?",
    'options_list': [
        'Manual differentiation',
        'Symbolic differentiation',
        'Random Search',
        'Automatic differentiation'
    ],
    'correct_answer': 'Random Search',
    'explanation': "Random Search is an optimization technique, not a method for computing partial derivatives. Common methods for differentiation include manual, symbolic, numerical, and automatic differentiation.",
    'chapter_information': 'Mozersaleh Notes on Linear Classifiers and Gradient Descent'
}

mozersaleh_notes_question_5 = {
    'question': "In a Linear Classifier, what is the function of the weight matrix W?",
    'options_list': [
        'To store the bias terms',
        'To map the input features to the output classes',
        'To initialize the model parameters',
        'To calculate the loss function'
    ],
    'correct_answer': 'To map the input features to the output classes',
    'explanation': "The weight matrix W is used to map the input features to the output classes in a linear classifier, where each row of W corresponds to a different class.",
    'chapter_information': 'Mozersaleh Notes on Linear Classifiers and Gradient Descent'
}


deep_learning_linear_algebra_question_1 = {
    'question': "What is the result of adding a scalar to a matrix?",
    'options_list': [
        'The scalar is added to each element of the matrix.',
        'The scalar is multiplied by each element of the matrix.',
        'The scalar is added to the diagonal elements of the matrix only.',
        'The scalar is added to the first row of the matrix.'
    ],
    'correct_answer': 'The scalar is added to each element of the matrix.',
    'explanation': "When adding a scalar to a matrix, the scalar is added to each element of the matrix.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_2 = {
    'question': "In matrix multiplication, when is the product of two matrices A and B defined?",
    'options_list': [
        'When the number of columns in A is equal to the number of rows in B.',
        'When A and B are square matrices of the same size.',
        'When the number of rows in A is equal to the number of rows in B.',
        'When the number of columns in A is equal to the number of columns in B.'
    ],
    'correct_answer': 'When the number of columns in A is equal to the number of rows in B.',
    'explanation': "Matrix multiplication is defined when the number of columns in the first matrix (A) matches the number of rows in the second matrix (B).",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_3 = {
    'question': "What is the matrix product C=AB?",
    'options_list': [
        'The element-wise product of matrices A and B.',
        'A matrix where each element Ci,j is the dot product of the i-th row of A and the j-th column of B.',
        'A matrix where each element Ci,j is the sum of the elements of matrices A and B.',
        'The transpose of the matrix A multiplied by matrix B.'
    ],
    'correct_answer': 'A matrix where each element Ci,j is the dot product of the i-th row of A and the j-th column of B.',
    'explanation': "The matrix product C = AB is computed by taking the dot product of each row of A with each column of B to obtain each element Ci,j of the resulting matrix C.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_4 = {
    'question': "What property of matrix multiplication is not true?",
    'options_list': [
        'Matrix multiplication is distributive: A(B + C) = AB + AC.',
        'Matrix multiplication is associative: A(BC) = (AB)C.',
        'Matrix multiplication is commutative: AB = BA.',
        'The transpose of a matrix product is the product of the transposes in reverse order: (AB)ᵀ = BᵀAᵀ.'
    ],
    'correct_answer': 'Matrix multiplication is commutative: AB = BA.',
    'explanation': "Matrix multiplication is generally not commutative, meaning AB ≠ BA in most cases.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_5 = {
    'question': "What is the identity matrix In?",
    'options_list': [
        'A matrix with 1s along the main diagonal and 0s elsewhere.',
        'A matrix that when multiplied by any other matrix results in a zero matrix.',
        'A matrix with all elements equal to 1.',
        'A matrix that has the same dimensions as the original matrix.'
    ],
    'correct_answer': 'A matrix with 1s along the main diagonal and 0s elsewhere.',
    'explanation': "The identity matrix In has 1s along the main diagonal and 0s elsewhere, and it does not change any vector when multiplied by it.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}


deep_learning_linear_algebra_question_6 = {
    'question': "Calculate the result of the following matrix addition: \n\nA = [[2, 4], [6, 8]]\nB = [[1, 3], [5, 7]]. \n\nWhat is A + B?",
    'options_list': [
        '[[3, 7], [11, 15]]',
        '[[3, 7], [6, 8]]',
        '[[3, 7], [11, 15]]',
        '[[3, 7], [11, 15]]'
    ],
    'correct_answer': '[[3, 7], [11, 15]]',
    'explanation': "The sum of matrices A and B is calculated by adding corresponding elements: [[2+1, 4+3], [6+5, 8+7]] = [[3, 7], [11, 15]].",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_7 = {
    'question': "Given the matrices \n\nA = [[1, 2], [3, 4]] and B = [[5, 6], [7, 8]], \n\ncalculate the matrix product AB.",
    'options_list': [
        '[[19, 22], [43, 50]]',
        '[[5, 12], [21, 32]]',
        '[[7, 10], [15, 22]]',
        '[[10, 14], [24, 30]]'
    ],
    'correct_answer': '[[19, 22], [43, 50]]',
    'explanation': "The matrix product AB is calculated as follows:\nRow 1 of A * Column 1 of B: (1*5 + 2*7) = 19, (1*6 + 2*8) = 22\nRow 2 of A * Column 2 of B: (3*5 + 4*7) = 43, (3*6 + 4*8) = 50\nSo AB = [[19, 22], [43, 50]].",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_8 = {
    'question': "Given the vector x = [2, 3] and the matrix A = [[4, 5], [6, 7]], \n\ncalculate the matrix-vector product Ax.",
    'options_list': [
        '[23, 33]',
        '[26, 38]',
        '[20, 29]',
        '[28, 39]'
    ],
    'correct_answer': '[23, 33]',
    'explanation': "The matrix-vector product Ax is calculated as follows:\nRow 1 of A * vector x: (4*2 + 5*3) = 8 + 15 = 23\nRow 2 of A * vector x: (6*2 + 7*3) = 12 + 21 = 33\nSo Ax = [23, 33].",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_9 = {
    'question': "Given the matrix A = [[1, 2], [3, 4]], \n\nfind its inverse A⁻¹.",
    'options_list': [
        '[[-2, 1], [1.5, -0.5]]',
        '[[-4, 2], [2, -1]]',
        '[[-2, 1], [1, -0.5]]',
        '[[-2, 0.5], [1.5, -0.5]]'
    ],
    'correct_answer': '[[-2, 1], [1.5, -0.5]]',
    'explanation': "The inverse of a 2x2 matrix A = [[a, b], [c, d]] is given by (1/(ad-bc)) * [[d, -b], [-c, a]].\nFor A = [[1, 2], [3, 4]], determinant is 1(4) - 2(3) = -2.\nSo A⁻¹ = (1/-2) * [[4, -2], [-3, 1]] = [[-2, 1], [1.5, -0.5]].",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_10 = {
    'question': "If x = [2, 3, 4] and y = [1, 0, -1], \n\ncalculate the dot product x⋅y.",
    'options_list': [
        '2',
        '4',
        '-1',
        '0'
    ],
    'correct_answer': '2',
    'explanation': "The dot product of vectors x and y is calculated as follows:\n(2*1) + (3*0) + (4*-1) = 2 + 0 - 4 = -2.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_11 = {
    'question': "Given the matrix A = [[3, 1], [1, 3]], compute the determinant of A.",
    'options_list': [
        '8',
        '10',
        '9',
        '7'
    ],
    'correct_answer': '8',
    'explanation': "The determinant of a 2x2 matrix A = [[a, b], [c, d]] is given by (ad - bc).\nFor A = [[3, 1], [1, 3]], det(A) = (3*3) - (1*1) = 9 - 1 = 8.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_12 = {
    'question': "Perform Singular Value Decomposition (SVD) on the matrix A = [[1, 0], [0, 2]]. What are the singular values?",
    'options_list': [
        '[1, 2]',
        '[2, 1]',
        '[2, 0]',
        '[1, 1]'
    ],
    'correct_answer': '[2, 1]',
    'explanation': "Singular Value Decomposition (SVD) decomposes a matrix A into UΣVᵀ, where Σ contains the singular values. For A = [[1, 0], [0, 2]], the singular values are 2 and 1.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_13 = {
    'question': "Consider the matrix A = [[1, 2], [2, 1]]. Find the eigenvalues of A.",
    'options_list': [
        '3, -1',
        '1, 3',
        '4, 0',
        '2, 2'
    ],
    'correct_answer': '3, -1',
    'explanation': "To find the eigenvalues of A, solve det(A - λI) = 0. For A = [[1, 2], [2, 1]], the characteristic equation is (1-λ)(1-λ) - 4 = λ² - 2λ - 3 = 0, which factors to (λ - 3)(λ + 1) = 0, giving eigenvalues λ = 3, -1.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_14 = {
    'question': "For a matrix A = [[4, 2], [1, 3]], find the inverse of A using the determinant and the adjugate method.",
    'options_list': [
        '[[0.375, -0.25], [-0.125, 0.5]]',
        '[[0.25, -0.5], [-0.5, 0.25]]',
        '[[0.5, -0.25], [-0.25, 0.5]]',
        '[[0.5, 0.25], [0.25, 0.5]]'
    ],
    'correct_answer': '[[0.375, -0.25], [-0.125, 0.5]]',
    'explanation': "The inverse of a 2x2 matrix A = [[a, b], [c, d]] is (1/det(A)) * [[d, -b], [-c, a]]. For A = [[4, 2], [1, 3]], det(A) = 4(3) - 2(1) = 10. So A⁻¹ = (1/10) * [[3, -2], [-1, 4]] = [[0.375, -0.25], [-0.125, 0.5]].",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_15 = {
    'question': "You are performing Principal Component Analysis (PCA) on a dataset represented by the matrix X. After centering X by subtracting the mean of each feature, what is the next step to find the principal components?",
    'options_list': [
        'Calculate the covariance matrix of X',
        'Normalize the features of X',
        'Perform SVD on X',
        'Calculate the determinant of X'
    ],
    'correct_answer': 'Calculate the covariance matrix of X',
    'explanation': "After centering the dataset, the next step in PCA is to calculate the covariance matrix of X. The principal components are the eigenvectors of this covariance matrix.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_linear_algebra_question_16 = {
    'question': "If a matrix A undergoes a change of basis transformation using matrix P, resulting in A' = P⁻¹AP, what is the relationship between the eigenvalues of A and A'?",
    'options_list': [
        'The eigenvalues of A and A\' are the same.',
        'The eigenvalues of A are the inverse of the eigenvalues of A\'',
        'The eigenvalues of A and A\' are multiplied by the determinant of P.',
        'The eigenvalues of A\' are the square of the eigenvalues of A.'
    ],
    'correct_answer': 'The eigenvalues of A and A\' are the same.',
    'explanation': "A change of basis transformation does not alter the eigenvalues of a matrix. Thus, the eigenvalues of A and A' are the same.",
    'chapter_information': 'Deep Learning Book: Chapter 2 - Linear Algebra'
}

deep_learning_probability_question_1 = {
    'question': "Given a fair 6-sided die, what is the probability of rolling a number greater than 4?",
    'options_list': [
        '1/3',
        '1/2',
        '1/6',
        '1/4'
    ],
    'correct_answer': '1/3',
    'explanation': "There are two outcomes greater than 4: 5 and 6. The probability is therefore 2/6 = 1/3.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_2 = {
    'question': "A bag contains 4 red, 3 green, and 2 blue marbles. If a marble is drawn at random, what is the probability that it is either red or blue?",
    'options_list': [
        '4/9',
        '7/9',
        '5/9',
        '6/9'
    ],
    'correct_answer': '6/9',
    'explanation': "There are a total of 9 marbles, and 4 red + 2 blue = 6 marbles that satisfy the condition. So, the probability is 6/9.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_3 = {
    'question': "A test for a disease is 99% sensitive (true positive rate) and 95% specific (true negative rate). If 0.5% of the population has the disease, what is the probability that a person has the disease given that they tested positive?",
    'options_list': [
        '0.01',
        '0.09',
        '0.50',
        '0.84'
    ],
    'correct_answer': '0.09',
    'explanation': "This is a Bayes' theorem problem. P(Disease|Positive) = [P(Positive|Disease) * P(Disease)] / P(Positive). Calculating this yields approximately 0.09.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_4 = {
    'question': "Suppose you draw two cards consecutively from a standard deck without replacement. What is the probability that both cards are aces?",
    'options_list': [
        '1/221',
        '1/52',
        '1/169',
        '1/13'
    ],
    'correct_answer': '1/221',
    'explanation': "The probability of drawing the first ace is 4/52. After drawing an ace, 3 aces remain out of 51 cards. The probability is therefore (4/52) * (3/51) = 1/221.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_5 = {
    'question': "Calculate the entropy of a random variable X that can take on the values {0, 1} with probabilities P(X=0) = 0.2 and P(X=1) = 0.8.",
    'options_list': [
        '0.72',
        '0.92',
        '1.00',
        '1.12'
    ],
    'correct_answer': '0.72',
    'explanation': "The entropy H(X) = -ΣP(x)log2(P(x)). Substituting the values: H(X) = -(0.2log2(0.2) + 0.8log2(0.8)) ≈ 0.72.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_6 = {
    'question': "For a binary channel with input probabilities P(X=0) = 0.4 and P(X=1) = 0.6, and conditional probabilities P(Y=0|X=0) = 0.9 and P(Y=0|X=1) = 0.2, compute the mutual information I(X;Y).",
    'options_list': [
        '0.05',
        '0.29',
        '0.97',
        '1.00'
    ],
    'correct_answer': '0.29',
    'explanation': "Mutual Information I(X;Y) = H(Y) - H(Y|X). First, calculate the entropy of Y and the conditional entropy H(Y|X), then subtract to find the mutual information.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_7 = {
    'question': "Given a discrete random variable X with the probability mass function P(X=x) = (1/2)^x for x=1, 2, 3,..., calculate the expected value E[X].",
    'options_list': [
        '1',
        '2',
        '3',
        '4'
    ],
    'correct_answer': '2',
    'explanation': "The expected value E[X] is calculated as ΣxP(X=x) for all x. Substituting the values and summing yields an expected value of 2.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

# deep_learning_probability_question_8 = {
#     'question': "Let X be a continuous random variable with probability density function f(x) = 2x for 0 ≤ x ≤ 1. What is the expected value E[X]?",
#     'options_list': [
#         '1/2',
#         '1/3',
#         '2/3',
#         '1/4'
#     ],
#     'correct_answer': '2/3',
#     'explanation': "The expected value E[X] = ∫xf(x)dx. Substituting f(x) = 2x and integrating over the interval [0, 1] gives E[X] = 2/3.",
#     'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
# }

deep_learning_probability_question_9 = {
    'question': "Suppose you have a biased coin where the probability of heads is unknown. You start with a prior belief that P(Heads) follows a Beta distribution with parameters α=2 and β=2. After observing 3 heads and 1 tail, what is the posterior distribution of P(Heads)?",
    'options_list': [
        'Beta(5, 3)',
        'Beta(3, 2)',
        'Beta(4, 3)',
        'Beta(6, 3)'
    ],
    'correct_answer': 'Beta(5, 3)',
    'explanation': "The posterior distribution is Beta(α+number of heads, β+number of tails). So, Beta(2+3, 2+1) = Beta(5, 3).",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_10 = {
    'question': "In a Bayesian inference problem, the prior probability of a model M is P(M) = 0.3, and the likelihood of data D given M is P(D|M) = 0.5. If the marginal likelihood P(D) = 0.4, what is the posterior probability P(M|D)?",
    'options_list': [
        '0.25',
        '0.375',
        '0.45',
        '0.50'
    ],
    'correct_answer': '0.375',
    'explanation': "The posterior probability is given by Bayes' theorem: P(M|D) = P(D|M)P(M) / P(D) = (0.5 * 0.3) / 0.4 = 0.375.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

# deep_learning_probability_question_11 = {
#     'question': "Consider a Markov chain with three states A, B, and C. The transition matrix is given by: \n"
#                 "[[0.2, 0.6, 0.2],\n"
#                 "[0.5, 0.4, 0.1],\n"
#                 "[0.3, 0.3, 0.4]]. \n"
#                 "What is the probability of transitioning from state A to state C in two steps?",
#     'options_list': [
#         '0.18',
#         '0.24',
#         '0.28',
#         '0.32'
#     ],
#     'correct_answer': '0.18',
#     'explanation': "The two-step transition probability is the (1,3) entry of the squared transition matrix. Calculating the square gives a (1,3) entry of 0.18.",
#     'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
# }

deep_learning_probability_question_12 = {
    'question': "Given a Markov chain with states S1, S2, S3, and transition probabilities P(S1 -> S2) = 0.4, P(S2 -> S3) = 0.5, and P(S3 -> S1) = 0.7. If the process starts in state S1, what is the probability that it returns to S1 after 3 steps?",
    'options_list': [
        '0.14',
        '0.16',
        '0.28',
        '0.32'
    ],
    'correct_answer': '0.14',
    'explanation': "The probability of returning to S1 after 3 steps is the product of the probabilities of the transitions S1 -> S2 -> S3 -> S1, which is 0.4 * 0.5 * 0.7 = 0.14.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_13 = {
    'question': "You have a dataset of 100 independent and identically distributed samples drawn from a Gaussian distribution with mean μ and variance σ². If the sample mean is 10 and the sample variance is 4, what is the Maximum Likelihood Estimate (MLE) of μ?",
    'options_list': [
        '8',
        '9',
        '10',
        '11'
    ],
    'correct_answer': '10',
    'explanation': "The MLE for the mean μ of a Gaussian distribution is simply the sample mean, which is 10 in this case.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_14 = {
    'question': "Suppose you observe the following data: {2, 4, 4, 4, 5, 5, 7, 9}. Assuming the data comes from a Poisson distribution, what is the Maximum Likelihood Estimate (MLE) for the rate parameter λ?",
    'options_list': [
        '4',
        '4.25',
        '5',
        '6'
    ],
    'correct_answer': '5',
    'explanation': "The MLE for the rate parameter λ of a Poisson distribution is the sample mean. The sum of the data is 40, and there are 8 data points, so λ = 40/8 = 5.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

# deep_learning_probability_question_15 = {
#     'question': "You have a discrete random variable X with the following probability distribution: P(X=1) = 0.1, P(X=2) = 0.3, P(X=3) = 0.4, P(X=4) = 0.2. Calculate the entropy H(X) in bits.",
#     'options_list': [
#         '1.72',
#         '1.85',
#         '2.00',
#         '2.15'
#     ],
#     'correct_answer': '1.85',
#     'explanation': "The entropy H(X) is calculated as -ΣP(x)log2(P(x)). Substituting the values and summing yields H(X) ≈ 1.85 bits.",
#     'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
# }

# deep_learning_probability_question_16 = {
#     'question': "Consider two random variables X and Y, where P(X=1) = 0.6, P(X=2) = 0.4, and P(Y=1|X=1) = 0.8, P(Y=1|X=2) = 0.3. Compute the conditional entropy H(Y|X).",
#     'options_list': [
#         '0.52',
#         '0.67',
#         '0.89',
#         '1.05'
#     ],
#     'correct_answer': '0.67',
#     'explanation': "The conditional entropy H(Y|X) = ΣP(X=x)H(Y|X=x). Calculating the individual entropies and summing them gives H(Y|X) ≈ 0.67.",
#     'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
# }



deep_learning_probability_question_15 = {
    'question': "You have a discrete random variable $X$ with the following probability distribution: $P(X=1) = 0.1$, $P(X=2) = 0.3$, $P(X=3) = 0.4$, $P(X=4) = 0.2$. Calculate the entropy $H(X)$ in bits.",
    'options_list': [
        '1.72',
        '1.85',
        '2.00',
        '2.15'
    ],
    'correct_answer': '1.85',
    'explanation': "The entropy $H(X)$ is calculated as $-\\sum P(x) \\log_2(P(x))$. Substituting the values and summing yields $H(X) \\approx 1.85$ bits.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_16 = {
    'question': "Consider two random variables $X$ and $Y$, where $P(X=1) = 0.6$, $P(X=2) = 0.4$, and $P(Y=1|X=1) = 0.8$, $P(Y=1|X=2) = 0.3$. Compute the conditional entropy $H(Y|X)$.",
    'options_list': [
        '0.52',
        '0.67',
        '0.89',
        '1.05'
    ],
    'correct_answer': '0.67',
    'explanation': "The conditional entropy $H(Y|X) = \\sum P(X=x)H(Y|X=x)$. Calculating the individual entropies and summing them gives $H(Y|X) \\approx 0.67$.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_11 = {
    'question': "Consider a Markov chain with three states A, B, and C. The transition matrix is given by: \n"
                "[[0.2, 0.6, 0.2],\n"
                "[0.5, 0.4, 0.1],\n"
                "[0.3, 0.3, 0.4]]. \n"
                "What is the probability of transitioning from state A to state C in two steps?",
    'options_list': [
        '0.18',
        '0.24',
        '0.28',
        '0.32'
    ],
    'correct_answer': '0.18',
    'explanation': "The two-step transition probability is the (1,3) entry of the squared transition matrix. Calculating the square gives a (1,3) entry of 0.18.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}

deep_learning_probability_question_8 = {
    'question': "Let $X$ be a continuous random variable with probability density function $f(x) = 2x$ for $0 \\leq x \\leq 1$. What is the expected value $E[X]$?",
    'options_list': [
        '1/2',
        '1/3',
        '2/3',
        '1/4'
    ],
    'correct_answer': '2/3',
    'explanation': "The expected value $E[X] = \\int_0^1 x f(x) dx$. Substituting $f(x) = 2x$ and integrating over the interval [0, 1] gives $E[X] = 2/3$.",
    'chapter_information': 'Deep Learning Book: Chapter 3 - Probability'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_1_MPC = KC_MPC_QUESTIONS[:-1]
