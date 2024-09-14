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

gt_lecture_3_mpc_question_1 = {
    'question': "What is the primary function of a max pooling layer in a neural network?",
    'options_list': [
        "A) To increase the spatial dimensions of the input",
        "B) To reduce the dimensionality of the input while retaining important features",
        "C) To perform a convolution operation",
        "D) To average the pixel values across a window"
    ],
    'correct_answer': 'B',
    'explanation': "Max pooling reduces the dimensionality of the input by retaining the maximum value in each window, allowing the network to keep the most important features.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_mpc_question_2 = {
    'question': "Which of the following is a key difference between max pooling and average pooling?",
    'options_list': [
        "A) Max pooling averages pixel values while average pooling selects the maximum value.",
        "B) Max pooling reduces the dimensionality, while average pooling increases dimensionality.",
        "C) Max pooling selects the maximum value in the window, while average pooling calculates the average of values in the window.",
        "D) Max pooling adds learned parameters, while average pooling does not."
    ],
    'correct_answer': 'C',
    'explanation': "Max pooling selects the maximum value within a defined window, while average pooling calculates the average of the values in that window.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_mpc_question_3 = {
    'question': "What type of invariance do pooling layers introduce into neural networks?",
    'options_list': [
        "A) Rotational invariance",
        "B) Translational invariance",
        "C) Scale invariance",
        "D) Equivariance"
    ],
    'correct_answer': 'B',
    'explanation': "Pooling layers introduce translational invariance, meaning small shifts in the input do not drastically change the output.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_mpc_question_4 = {
    'question': "Which of the following hyperparameters is specific to pooling layers?",
    'options_list': [
        "A) Kernel size",
        "B) Stride",
        "C) Number of filters",
        "D) Padding"
    ],
    'correct_answer': 'B',
    'explanation': "In pooling layers, stride controls how much the window moves across the input, similar to convolutional layers.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_mpc_question_5 = {
    'question': "Which of the following pooling types is less commonly used compared to max pooling?",
    'options_list': [
        "A) Global pooling",
        "B) Average pooling",
        "C) Max pooling",
        "D) Fractional max pooling"
    ],
    'correct_answer': 'B',
    'explanation': "Max pooling is more commonly used than average pooling, which calculates the average of values in the pooling window.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_tf_question_1 = {
    'question': "Max pooling retains the maximum value in a defined window, while reducing the input dimensionality.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Max pooling selects the maximum value from a window, reducing the input's spatial dimensions while preserving key features.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_tf_question_2 = {
    'question': "Pooling layers have learned parameters, similar to convolutional layers.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Pooling layers do not have learned parameters; they perform predefined operations like max or average pooling without training any weights.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_tf_question_3 = {
    'question': "Convolution operations are equivariant, meaning that a feature moving in the input causes a corresponding movement in the output.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Convolution is equivariant because when a feature moves in the input, the corresponding activation in the output moves by the same amount.",
    'chapter_information': 'GT Lecture 3'
}

gt_lecture_3_tf_question_4 = {
    'question': "Pooling layers are used to increase the spatial dimensions of the input image.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Pooling layers are used to reduce the spatial dimensions (height and width) of the input while keeping the most important information.",
    'chapter_information': 'GT Lecture 3'
}

andrew_ng_c4w1_mpc_question_1 = {
    'question': "What is the primary function of a max pooling layer in a convolutional neural network?",
    'options_list': [
        "A) To increase the spatial dimensions of the input",
        "B) To reduce the dimensionality of the input while retaining important features",
        "C) To perform a convolution operation",
        "D) To average the pixel values across a window"
    ],
    'correct_answer': 'B',
    'explanation': "Max pooling reduces the dimensionality of the input by retaining the maximum value in each window, allowing the network to keep the most important features.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_2 = {
    'question': "Which of the following is a key difference between max pooling and average pooling?",
    'options_list': [
        "A) Max pooling averages pixel values while average pooling selects the maximum value.",
        "B) Max pooling reduces the dimensionality, while average pooling increases dimensionality.",
        "C) Max pooling selects the maximum value in the window, while average pooling calculates the average of values in the window.",
        "D) Max pooling adds learned parameters, while average pooling does not."
    ],
    'correct_answer': 'C',
    'explanation': "Max pooling selects the maximum value within a defined window, while average pooling calculates the average of the values in that window.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_3 = {
    'question': "What type of invariance do pooling layers introduce into neural networks?",
    'options_list': [
        "A) Rotational invariance",
        "B) Translational invariance",
        "C) Scale invariance",
        "D) Equivariance"
    ],
    'correct_answer': 'B',
    'explanation': "Pooling layers introduce translational invariance, meaning small shifts in the input do not drastically change the output.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_4 = {
    'question': "Which of the following hyperparameters is specific to pooling layers?",
    'options_list': [
        "A) Kernel size",
        "B) Stride",
        "C) Number of filters",
        "D) Padding"
    ],
    'correct_answer': 'B',
    'explanation': "In pooling layers, stride controls how much the window moves across the input, similar to convolutional layers.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_5 = {
    'question': "Which of the following pooling types is less commonly used compared to max pooling?",
    'options_list': [
        "A) Global pooling",
        "B) Average pooling",
        "C) Max pooling",
        "D) Fractional max pooling"
    ],
    'correct_answer': 'B',
    'explanation': "Max pooling is more commonly used than average pooling, which calculates the average of values in the pooling window.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_tf_question_1 = {
    'question': "Max pooling retains the maximum value in a defined window, while reducing the input dimensionality.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Max pooling selects the maximum value from a window, reducing the input's spatial dimensions while preserving key features.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_tf_question_2 = {
    'question': "Pooling layers have learned parameters, similar to convolutional layers.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Pooling layers do not have learned parameters; they perform predefined operations like max or average pooling without training any weights.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_tf_question_3 = {
    'question': "Convolution operations are equivariant, meaning that a feature moving in the input causes a corresponding movement in the output.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Convolution is equivariant because when a feature moves in the input, the corresponding activation in the output moves by the same amount.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_tf_question_4 = {
    'question': "Pooling layers are used to increase the spatial dimensions of the input image.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "Pooling layers are used to reduce the spatial dimensions (height and width) of the input while keeping the most important information.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_6 = {
    'question': "What is the main purpose of parameter sharing in ConvNets?",
    'options_list': [
        "A) It allows parameters to be shared across different tasks for transfer learning.",
        "B) It reduces the total number of parameters, helping to prevent overfitting.",
        "C) It allows a feature detector to be applied in multiple locations across the input.",
        "D) It ensures that the gradients for multiple layers remain the same."
    ],
    'correct_answer': 'C',
    'explanation': "Parameter sharing allows the same feature detector (kernel) to be applied across different regions of the input, reducing the number of parameters and enabling the network to detect features across the entire image.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_7 = {
    'question': "If you have an input volume of 63x63x16 and convolve it with 32 filters of size 7x7, using a stride of 2 and no padding, what is the output volume?",
    'options_list': [
        "A) 16x16x32",
        "B) 29x29x16",
        "C) 29x29x32",
        "D) 16x16x16"
    ],
    'correct_answer': 'C',
    'explanation': "The output volume is calculated by applying the formula for convolution: $$H_{out} = \\frac{(H_{in} - K)}{S} + 1$$, giving a 29x29x32 output.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_8 = {
    'question': "You have a 300x300 RGB image, and you apply a convolutional layer with 100 filters, each 5x5. How many parameters does the layer have, including bias terms?",
    'options_list': [
        "A) 2,500",
        "B) 7,500",
        "C) 2,600",
        "D) 7,600"
    ],
    'correct_answer': 'D',
    'explanation': "The number of parameters is calculated as $$K_H \\times K_W \\times C_{in} + 1$$ (for the bias term), and then multiplied by the number of filters: $$5 \\times 5 \\times 3 + 1 = 76$$ per filter, so the total is $$76 \\times 100 = 7,600$$.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_mpc_question_9 = {
    'question': "What is the output volume when you apply max pooling with a stride of 2 and filter size of 2 to an input volume of 32x32x16?",
    'options_list': [
        "A) 16x16x16",
        "B) 32x32x8",
        "C) 15x15x16",
        "D) 32x32x16"
    ],
    'correct_answer': 'A',
    'explanation': "Max pooling with a stride of 2 reduces the height and width by a factor of 2, so the output volume will be 16x16x16.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_tf_question_5 = {
    'question': "Pooling layers do not affect the backpropagation (derivatives) calculation because they do not have parameters.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "While pooling layers do not have parameters, they still affect the gradient flow during backpropagation as the max operation influences which values contribute to the next layer.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_tf_question_6 = {
    'question': "In convolutional networks, sparsity of connections means that each filter is only connected to a small region of the input.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Sparsity of connections in ConvNets refers to the fact that each filter operates on only a small portion of the input (a local receptive field), reducing the number of connections.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

andrew_ng_c4w1_tf_question_7 = {
    'question': "In a convolutional layer with multiple channels (e.g., an RGB image), each kernel has the same depth as the input channels.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "In convolutional layers, the depth of each kernel matches the number of input channels (e.g., 3 for RGB images), allowing the kernel to operate across all input channels.",
    'chapter_information': 'Andrew Ng Deep Learning C4W1'
}

uc_boulder_dl_cnn_question_1 = {
    'question': "Consider a convolutional neural network model with three convolution layers. The first layer has 50 filters, the second layer has 100 filters, and the third layer has 200 filters. All convolution layers have a stride of 2 and the same padding. The input images are 300x400 pixels with RGB channels, and the filter size is 3x3. How many trainable parameters does the CNN model have?",
    'options_list': ["Do the computation"],
    'correct_answer': '226700',
    'explanation': "Parameters in 1st layer: 50 filters with 3x3x3 size + 1 bias = 50x(3x3x3+1) = 1400\nParameters in 2nd layer: 100 filters with (3x3x50 + 1) = 45100\nParameters in 3rd layer: 200 filters with (3x3x100+1) = 180200\nTotal parameters = 1400 + 45100 + 180200 = 226700",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_5 = {
    'question': "How many convolutional layers with 3x3 filters would you need to have the same receptive field as a convolutional layer with 11x11 filters? Assume stride=1 and no padding.",
    'options_list': ["Do the computation"],
    'correct_answer': '5',
    'explanation': "The correct answer is 5 layers. The receptive field grows from 1->3->5->7->9->11 with each layer.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_4 = {
    'question': "True or False: You can use bigger strides in a convolutional layer instead of a max-pooling layer for better accuracy.",
    'options_list': [
        "A) True",
        "B) False"
    ],
    'correct_answer': 'A',
    'explanation': "A convolutional layer with stride two can subsample equivalently with a max-pooling layer with a 2x2 filter size. It costs more parameters, but the convolutional layer is learnable, so it tends to have better accuracy.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_3 = {
    'question': "While training a CNN model, you receive the OOM (out of memory) error message. What can you do to resolve the issue? Choose all that apply.",
    'options_list': [
        "A) Reduce the batch size",
        "B) Reduce the number of epochs",
        "C) Reduce the number of filters in convolution layers",
        "D) Reduce the stride of convolution layers",
        "E) Reduce the number of layers"
    ],
    'correct_answer': " A, C, and E",
    'explanation': "Reducing the mini-batch size will require less memory per batch. Reducing the number of filters can reduce the feature map depth. Reducing the number of layers will give fewer parameters and feature maps.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_2 = {
    'question': "Consider a convolutional neural network model with three convolution layers. The first layer has 50 filters, the second layer has 100 filters, and the third layer has 200 filters. All convolution layers have a stride of 2 and the same padding. The input images are 300x400 pixels with RGB channels. What is the feature map size after the third convolution layer?",
    'options_list': [
        "A) 150x200x50",
        "B) 38x50x200",
        "C) 75x100x100"
    ],
    'correct_answer': 'B',
    'explanation': "After applying the first convolutional layer, the first feature map size is 150x200x50. After the second layer, the feature map size is 75x100x100. After the third layer, the feature map size is 38x50x200. The width 75 gets padded to 77, then divided by two to get 38.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_6 = {
    'question': "Consider a convolutional neural network with an input volume of 64x64x3 (RGB image). You apply a convolutional layer with 32 filters of size 5x5, using stride=1 and same padding. How many trainable parameters does this layer have?",
    'options_list': ["Do the computation"],
    'correct_answer': '2432',
    'explanation': "The number of parameters is calculated as (5x5x3 + 1) per filter (for the bias term), and then multiplied by the number of filters: (5x5x3 + 1) x 32 = 2432 parameters.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_7 = {
    'question': "You have a convolutional layer with 64 filters of size 7x7, using stride=2 and no padding. The input volume is 128x128x32. What is the output feature map size after applying the convolutional layer?",
    'options_list': ["Do the computation"],
    'correct_answer': '61x61x64',
    'explanation': "Using the formula for the output size of a convolutional layer: $$H_{out} = \\frac{H_{in} - K}{S} + 1$$, we get $$H_{out} = \\frac{128 - 7}{2} + 1 = 61$$. Thus, the output feature map size is 61x61x64.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_8 = {
    'question': "Consider a CNN with a 224x224x3 input. You apply a convolutional layer with 128 filters of size 3x3 and stride=1. If the output volume is 224x224x128, how many trainable parameters are there in this layer?",
    'options_list': ["Do the computation"],
    'correct_answer': '3,712',
    'explanation': "The number of parameters is calculated as (3x3x3 + 1) per filter (for the bias term), and then multiplied by the number of filters: (3x3x3 + 1) x 128 = 3712 parameters.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_9 = {
    'question': "If you have an input volume of 150x150x64 and convolve it with 256 filters of size 5x5, using a stride of 2 and same padding, what is the output volume size?",
    'options_list': ["Do the computation"],
    'correct_answer': '75x75x256',
    'explanation': "The output size is calculated using the formula: $$H_{out} = \\frac{H_{in}}{S}$$ when padding is applied. Here, $$H_{out} = \\frac{150}{2} = 75$$. Therefore, the output volume is 75x75x256.",
    'chapter_information': 'UC Boulder DL Course'
}

uc_boulder_dl_cnn_question_10 = {
    'question': "You have an input volume of 256x256x32, and you apply a max-pooling layer with a 2x2 filter and stride of 2. What is the output volume size after applying the max-pooling layer?",
    'options_list': ["Do the computation"],
    'correct_answer': '128x128x32',
    'explanation': "Max-pooling reduces the spatial dimensions by a factor of the stride. So, the output size is $$\\frac{256}{2} = 128$$. The depth remains unchanged, so the output is 128x128x32.",
    'chapter_information': 'UC Boulder DL Course'
}







KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_5_MPC = KC_MPC_QUESTIONS[:-1]
