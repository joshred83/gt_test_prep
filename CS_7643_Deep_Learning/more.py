

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



monzersaleh_data_wrangling_question_1 = {
    'question': "What is the purpose of cross-validation in model evaluation?",
    'options_list': [
        'To increase the size of the training dataset.',
        'To estimate the prediction error and avoid overfitting.',
        'To remove outliers from the dataset.',
        'To perform hyperparameter tuning.'
    ],
    'correct_answer': 'To estimate the prediction error and avoid overfitting.',
    'explanation': "Cross-validation is used to estimate the prediction error of a model and help prevent overfitting by using different subsets of the data for training and testing.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_2 = {
    'question': "Which method can be used to handle class imbalance in a dataset?",
    'options_list': [
        'Dropping the minority class.',
        'Using the SMOTE technique.',
        'Ignoring the imbalance and proceeding with training.',
        'Removing all duplicate samples from the majority class.'
    ],
    'correct_answer': 'Using the SMOTE technique.',
    'explanation': "SMOTE (Synthetic Minority OverSampling Technique) is a method used to handle class imbalance by generating synthetic samples for the minority class.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_3 = {
    'question': "What is the main goal of data pre-processing in deep learning?",
    'options_list': [
        'To increase the dimensionality of the dataset.',
        'To improve model convergence by scaling and normalizing data.',
        'To create new features from the existing dataset.',
        'To decrease the model’s computational complexity.'
    ],
    'correct_answer': 'To improve model convergence by scaling and normalizing data.',
    'explanation': "Data pre-processing, such as scaling and normalizing, helps improve model convergence and stability during training.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_4 = {
    'question': "What does the term 'missing at random' imply in the context of missing data?",
    'options_list': [
        'The likelihood of a data observation being missing depends on other observed data features.',
        'The likelihood of a data observation being missing is completely random.',
        'The missing data is related to unobserved outcomes.',
        'The missing data can be ignored without any consequences.'
    ],
    'correct_answer': 'The likelihood of a data observation being missing depends on other observed data features.',
    'explanation': "'Missing at random' means that the likelihood of a data observation being missing depends on other observed features, which can guide the imputation process.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}

monzersaleh_data_wrangling_question_5 = {
    'question': "What is the key advantage of using Focal Loss over Cross Entropy in classification tasks?",
    'options_list': [
        'It simplifies the model architecture.',
        'It down-weights easy examples, focusing more on hard examples.',
        'It reduces the size of the training dataset.',
        'It improves model interpretability.'
    ],
    'correct_answer': 'It down-weights easy examples, focusing more on hard examples.',
    'explanation': "Focal Loss is designed to down-weight easy examples, which allows the model to focus more on difficult and rare examples during training.",
    'chapter_information': 'Monzersaleh Notes on Data Wrangling'
}