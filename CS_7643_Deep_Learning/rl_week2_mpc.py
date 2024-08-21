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



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
