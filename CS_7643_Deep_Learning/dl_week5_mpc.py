module_2_introduction_mpc_question_1 = {
    'question': "What is the primary purpose of using convolutional layers in CNNs?",
    'options_list': [
        "A) To fully connect each neuron to all neurons in the previous layer.",
        "B) To restrict connections to local regions of the input for feature extraction.",
        "C) To reduce the dimensionality of the input data.",
        "D) To avoid overfitting during training."
    ],
    'correct_answer': 'B',
    'explanation': "Convolutional layers restrict connections to local regions of the input, which allows them to detect specific patterns in the data, such as edges or textures.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_mpc_question_2 = {
    'question': "Which of the following is a correct mathematical expression for the output of a fully connected layer?",
    'options_list': [
        "A) $$y = W x$$",
        "B) $$y = W \\times \\text{Convolve}(x, W)$$",
        "C) $$y = W x + b$$",
        "D) $$y = \\text{max}(x + W)$$"
    ],
    'correct_answer': 'C',
    'explanation': "The output of a fully connected layer is calculated as $$y = W x + b$$, where $$W$$ is the weight matrix and $$b$$ is the bias vector.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_mpc_question_3 = {
    'question': "In a convolutional operation, what role does the kernel play?",
    'options_list': [
        "A) It adds bias to the input image.",
        "B) It transforms the input image into a feature map by detecting specific patterns.",
        "C) It downsamples the input image to control overfitting.",
        "D) It flattens the input image for classification."
    ],
    'correct_answer': 'B',
    'explanation': "The kernel in a convolutional operation detects patterns such as edges, textures, or shapes and converts the input image into a feature map.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_mpc_question_4 = {
    'question': "Which of the following layers is primarily responsible for reducing the size of the feature map in CNNs?",
    'options_list': [
        "A) Fully connected layers.",
        "B) Convolutional layers.",
        "C) Pooling layers.",
        "D) ReLU activation function."
    ],
    'correct_answer': 'C',
    'explanation': "Pooling layers (e.g., max pooling or average pooling) reduce the dimensionality of the feature map by selecting representative values (such as maximum values) from local regions.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_mpc_question_5 = {
    'question': "Which architecture first introduced the use of alternating convolutional layers and pooling layers?",
    'options_list': [
        "A) VGG-16.",
        "B) LeNet.",
        "C) ResNet.",
        "D) Inception."
    ],
    'correct_answer': 'B',
    'explanation': "LeNet, one of the first convolutional neural network architectures, introduced the concept of alternating convolutional and pooling layers.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_mpc_question_6 = {
    'question': "What is the correct update rule for backpropagation when optimizing a parameter $$\\theta$$?",
    'options_list': [
        "A) $$\\theta \\leftarrow \\theta + \\eta \\frac{\\partial L}{\\partial \\theta}$$",
        "B) $$\\theta \\leftarrow \\theta - \\eta \\frac{\\partial L}{\\partial \\theta}$$",
        "C) $$\\theta \\leftarrow \\theta \\times \\frac{\\partial L}{\\partial \\theta}$$",
        "D) $$\\theta \\leftarrow \\theta - \\frac{\\eta}{\\partial \\theta}$$"
    ],
    'correct_answer': 'B',
    'explanation': "In backpropagation, parameters are updated using the rule $$\\theta \\leftarrow \\theta - \\eta \\frac{\\partial L}{\\partial \\theta}$$, where $$\\eta$$ is the learning rate and $$\\frac{\\partial L}{\\partial \\theta}$$ is the gradient of the loss with respect to $$\\theta$$.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_mpc_question_7 = {
    'question': "In object detection networks, what do the multiple branches in the architecture typically predict?",
    'options_list': [
        "A) One branch for predicting object shapes and another for edge detection.",
        "B) One branch for object localization and another for object classification.",
        "C) One branch for pooling operations and another for feature extraction.",
        "D) One branch for fully connected layers and another for ReLU activation."
    ],
    'correct_answer': 'B',
    'explanation': "In object detection networks, different branches are used for separate tasks: one for predicting the location of objects and another for classifying the objects.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_tf_question_1 = {
    'question': "In fully connected layers, each input node is connected to every output node.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "In fully connected layers, each *output* node is connected to every *input* node, not the other way around.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_tf_question_2 = {
    'question': "Pooling layers are primarily used for feature extraction in CNNs.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Pooling layers are used to reduce the dimensionality of the input, not for feature extraction.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_tf_question_3 = {
    'question': "In convolutional layers, local connectivity allows for detecting specific features such as edges and textures.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Local connectivity in convolutional layers enables the detection of features like edges and textures from the input.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_tf_question_4 = {
    'question': "The primary purpose of max pooling is to emphasize the minimum value within a specific region of the input.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Max pooling selects the maximum value within a specific region of the input, not the minimum.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_2_introduction_tf_question_5 = {
    'question': "A CNN can have multiple loss functions for tasks such as object detection.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "In object detection tasks, CNNs often use multiple loss functions, such as one for object localization and another for classification.",
    'chapter_information': 'Module 2 Introduction (Lecture)'
}

module_5_lesson_1_mpc_question_2 = {
    'question': "How does weight sharing in convolutional layers impact the number of parameters?",
    'options_list': [
        "A) Weight sharing reduces the number of parameters from $M \\times N + N$ to $K_1 \\times K_2 + 1$.",
        "B) Weight sharing allows the network to learn a different set of parameters for each location in the image.",
        "C) Weight sharing increases the number of parameters as the kernel must be applied to each pixel individually.",
        "D) Weight sharing has no effect on the number of parameters but only reduces computational cost."
    ],
    'correct_answer': 'A',
    'explanation': "Weight sharing in convolutional layers drastically reduces the number of parameters because the same kernel is applied to multiple locations in the image, resulting in fewer parameters compared to fully connected layers.",
    'chapter_information': 'Module 5, Lesson 1: Convolution Layers'
}

module_5_lesson_1_mpc_question_3 = {
    'question': "Given an input image of size $1024 \\times 1024$ and a filter of size $3 \\times 3$, what is the number of parameters needed for one feature map in a convolutional layer?",
    'options_list': [
        "A) 9",
        "B) 10",
        "C) 1025",
        "D) 1024"
    ],
    'correct_answer': 'B',
    'explanation': "For a $3 \\times 3$ filter, the number of parameters is $3 \\times 3 + 1 = 10$, where the additional parameter is the bias term.",
    'chapter_information': 'Module 5, Lesson 1: Convolution Layers'
}

module_5_lesson_1_mpc_question_4 = {
    'question': "In a convolution layer with $M$ output channels and a filter size of $K_1 \\times K_2$, what is the formula for the total number of parameters?",
    'options_list': [
        "A) $(K_1 \\times K_2 + 1) \\times M$",
        "B) $(K_1 \\times K_2) \\times M$",
        "C) $(M \\times K_1 \\times K_2) + N$",
        "D) $(M \\times N + K_1 \\times K_2)$"
    ],
    'correct_answer': 'A',
    'explanation': "The total number of parameters is $(K_1 \\times K_2 + 1) \\times M$, where $K_1 \\times K_2$ is the size of the filter, $M$ is the number of output channels, and the additional parameter accounts for the bias term.",
    'chapter_information': 'Module 5, Lesson 1: Convolution Layers'
}

module_5_lesson_1_mpc_question_5 = {
    'question': "Why do modern neural networks typically use cross-correlation instead of strict convolution?",
    'options_list': [
        "A) Cross-correlation is computationally more efficient because it avoids flipping the kernel.",
        "B) Cross-correlation has better performance in detecting edges and textures.",
        "C) Cross-correlation provides better gradient flow during backpropagation.",
        "D) Cross-correlation avoids the need for weight sharing, making it more flexible."
    ],
    'correct_answer': 'A',
    'explanation': "Cross-correlation is typically used in modern neural networks because it simplifies the computation by not requiring the kernel to be flipped, while still effectively performing feature detection.",
    'chapter_information': 'Module 5, Lesson 1: Convolution Layers'
}



module_5_lesson_1_tf_question_1 = {
    'question': "Convolution layers significantly reduce the number of parameters compared to fully connected layers because they connect each output node to every input node.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Convolution layers reduce the number of parameters by connecting each node only to local patches of the input, not to every input node as in fully connected layers.",
    'chapter_information': 'Module 5, Lesson 1: Convolution Layers'
}

module_5_lesson_1_tf_question_2 = {
    'question': "In cross-correlation, the kernel is applied without flipping it.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Cross-correlation is similar to convolution, but it does not involve flipping the kernel, making it computationally simpler.",
    'chapter_information': 'Module 5, Lesson 1: Convolution Layers'
}


module_5_lesson_1_tf_question_4 = {
    'question': "The number of parameters in a convolutional layer with multi-channel feature maps is proportional to the number of output channels.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The number of parameters in a convolutional layer is proportional to the number of output channels (or learned features), as each feature map corresponds to a set of parameters for the convolution operation.",
    'chapter_information': 'Module 5, Lesson 1: Convolution Layers'
}




KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_5_MPC = KC_MPC_QUESTIONS[:-1]
