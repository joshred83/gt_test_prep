module_2_convolutional_backprop_oh_mpc_question_1 = {
    'question': "When computing the gradient of the loss with respect to the weights in a convolutional layer:",
    'options_list': [
        "A) The resulting gradient tensor has the same dimensions as the input image.",
        "B) The resulting gradient tensor has the same dimensions as the kernel.",
        "C) The resulting gradient tensor is a scalar.",
        "D) The resulting gradient tensor has dimensions equal to the number of receptive fields multiplied by the input image size."
    ],
    'correct_answer': 'B',
    'explanation': "The gradient of the loss with respect to the weights has the same dimensions as the kernel since each weight contributes to the convolutional operation in the same spatial regions.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_mpc_question_2 = {
    'question': "Which of the following is true when computing the gradient of the loss with respect to the input during backpropagation in a convolutional layer?",
    'options_list': [
        "A) The gradient is computed by convolving the output gradients with the original kernel, without any modifications.",
        "B) The gradient is computed by convolving the output gradients with a flipped version of the kernel.",
        "C) The gradient is computed by adding the output gradients directly to the input tensor.",
        "D) The gradient computation is independent of the receptive fields of the input image."
    ],
    'correct_answer': 'B',
    'explanation': "During backpropagation, the gradient with respect to the input is computed by convolving the output gradients with a flipped version of the kernel.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_mpc_question_3 = {
    'question': "In a convolutional layer with a 4x4 input image and a 2x2 kernel, using a stride of 1 and no padding, what is the shape of the gradient of the loss with respect to the input during backpropagation?",
    'options_list': [
        "A) 4x4",
        "B) 3x3",
        "C) 2x2",
        "D) 5x5"
    ],
    'correct_answer': 'A',
    'explanation': "The gradient of the loss with respect to the input has the same dimensions as the input image, which is 4x4 in this case.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_mpc_question_4 = {
    'question': "When applying a convolutional operation on a multi-channel input (e.g., a 3-channel RGB image), how does the convolutional kernel adapt?",
    'options_list': [
        "A) The kernel's depth matches the number of input channels, and each depth slice has independently initialized weights.",
        "B) The kernel's depth is set to 1 and applied independently across each input channel.",
        "C) The kernel's weights are duplicated across the depth dimension to match the input channels.",
        "D) A separate kernel is used for each channel, and the outputs are averaged to produce the final feature map."
    ],
    'correct_answer': 'A',
    'explanation': "In a convolutional layer, the kernel's depth must match the input's number of channels, with each slice of the kernel being initialized independently.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_mpc_question_5 = {
    'question': "Consider a convolutional layer that uses padding in the input. How does this padding affect the backpropagation through the layer?",
    'options_list': [
        "A) Padding does not affect the backpropagation as it only alters the input dimensions during the forward pass.",
        "B) During backpropagation, gradients corresponding to the padding are discarded.",
        "C) Padding introduces additional gradient sources in the input tensor that must be accounted for during backpropagation.",
        "D) The padding is convolved with the output gradients to compute the final input gradient."
    ],
    'correct_answer': 'C',
    'explanation': "During backpropagation, padding affects the gradient calculation because it introduces additional sources of gradient at the edges of the input tensor.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_tf_question_1 = {
    'question': "During the backward pass in a convolutional layer, the gradient of the loss with respect to the weights is computed by summing the gradients of all receptive fields in the input image.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The gradient with respect to the weights is obtained by summing the contributions from all receptive fields that the kernel interacted with during the forward pass.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_tf_question_2 = {
    'question': "In a convolutional layer, the dimensions of the gradient of the loss with respect to the input always match the dimensions of the input image, regardless of padding or stride.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The dimensions of the gradient with respect to the input depend on the padding and stride used during the forward pass.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_tf_question_3 = {
    'question': "In backpropagation through a convolutional layer, if the input image has padding, the resulting gradient with respect to the input must include the padded elements.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The gradient with respect to the input includes contributions from the padded elements since padding affects how the kernel interacts with the image.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_tf_question_4 = {
    'question': "When multiple kernels are used in a convolutional layer, the gradient of the loss with respect to each kernel is computed independently, and the gradients are summed together at the end.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "While the gradients with respect to each kernel are computed independently, they are not summed together. Each kernel updates its own weights based on its respective gradient.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_convolutional_backprop_oh_tf_question_5 = {
    'question': "During the backward pass of a convolutional layer, the derivative of the loss with respect to the input is computed by an element-wise multiplication of the input with the kernel's gradient.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The derivative with respect to the input is computed by convolving the output gradients with the flipped kernel, not by element-wise multiplication.",
    'chapter_information': 'Convolutional Module 2: Backprop OH'
}

module_2_cb_focal_loss_oh_mpc_question_1 = {
    'question': "In the context of class imbalance, what problem arises when using standard stochastic gradient descent for training?",
    'options_list': [
        "A) The model tends to overfit to the minority classes.",
        "B) The model assigns equal importance to all classes, regardless of frequency.",
        "C) The model's weights are biased towards optimizing the majority class, neglecting the minority class.",
        "D) The loss function becomes unstable, leading to vanishing gradients."
    ],
    'correct_answer': 'C',
    'explanation': "Standard stochastic gradient descent tends to push the model's weights in a direction that optimizes for the majority class, often at the expense of the minority class.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_mpc_question_2 = {
    'question': "Which of the following terms is introduced in the focal loss to down-weight the loss for well-classified examples?",
    'options_list': [
        "A) Alpha term",
        "B) Cross-entropy term",
        "C) Focal term",
        "D) Inverse class frequency term"
    ],
    'correct_answer': 'C',
    'explanation': "The focal term in focal loss is introduced to down-weight the loss for well-classified examples, thereby focusing more on hard examples.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_mpc_question_3 = {
    'question': "In the class-balanced loss paper, what concept is introduced to more effectively handle class imbalance?",
    'options_list': [
        "A) Inverse class frequency weighting",
        "B) Effective number of samples",
        "C) Hard negative mining",
        "D) Logit scaling"
    ],
    'correct_answer': 'B',
    'explanation': "The class-balanced loss paper introduces the concept of the 'effective number of samples' to better account for the class imbalance when defining the loss weights.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_mpc_question_4 = {
    'question': "How does the focal loss handle well-classified examples during training?",
    'options_list': [
        "A) It assigns them a higher weight in the loss function.",
        "B) It down-weights their contribution to the loss using a focal term.",
        "C) It ignores them in the training process.",
        "D) It increases the learning rate for these examples."
    ],
    'correct_answer': 'B',
    'explanation': "Focal loss down-weights the loss for well-classified examples using a focal term, allowing the model to focus more on hard-to-classify cases.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_mpc_question_5 = {
    'question': "In the focal loss equation, what role does the hyperparameter $$\\gamma$$ play?",
    'options_list': [
        "A) It controls the class weighting in the loss function.",
        "B) It scales the learning rate for minority classes.",
        "C) It adjusts the focus on hard examples by modulating the loss based on the model's confidence.",
        "D) It decides the threshold for classifying an example as positive or negative."
    ],
    'correct_answer': 'C',
    'explanation': "The hyperparameter $$\\gamma$$ in the focal loss modulates the focus on hard examples by adjusting the loss based on how confident the model is in its predictions.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_tf_question_1 = {
    'question': "Inverse class frequency weighting is the most sophisticated way to handle class imbalance in deep learning.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "While inverse class frequency weighting is a straightforward approach, more sophisticated methods like focal loss and class-balanced loss are designed to address class imbalance more effectively.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_tf_question_2 = {
    'question': "The class-balanced loss uses the concept of 'effective number of samples' to weigh each class in the loss function.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Class-balanced loss introduces the concept of 'effective number of samples' to better estimate the importance of each class when computing the loss.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_tf_question_3 = {
    'question': "In focal loss, a high $$\\gamma$$ value means the model will focus more on correctly classified examples.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "A high $$\\gamma$$ value in focal loss means the model focuses more on hard examples, not well-classified ones.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_tf_question_4 = {
    'question': "Focal loss was originally developed for binary classification tasks in object detection.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Focal loss was initially developed to address the imbalance problem in binary classification within single-stage object detection tasks.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

module_2_cb_focal_loss_oh_tf_question_5 = {
    'question': "The class-balanced focal loss implementation must handle both the class-balanced term and the focal term simultaneously.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The class-balanced focal loss involves both the class-balanced term from the class-balanced loss paper and the focal term from the focal loss paper.",
    'chapter_information': 'Module 2: CB Focal Loss OH'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_1 = {
    'question': "What is the primary reason for calculating the backward pass of a convolution layer?",
    'options_list': [
        "A) To improve forward pass speed.",
        "B) To understand how to manually implement automatic differentiation.",
        "C) To derive a vectorized linear algebra operation for efficient GPU implementation.",
        "D) To simplify the convolution operation for smaller datasets."
    ],
    'correct_answer': 'C',
    'explanation': "Calculating the backward pass of a convolution layer helps derive a vectorized linear algebra operation that can be efficiently implemented on GPUs.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_2 = {
    'question': "In the derivation of the convolution layer's backward pass, what is the role of the upstream gradient?",
    'options_list': [
        "A) It contains the input data to be convolved.",
        "B) It represents the gradient of the loss with respect to the output of the current layer.",
        "C) It determines the stride and padding of the convolution.",
        "D) It controls the learning rate during training."
    ],
    'correct_answer': 'B',
    'explanation': "The upstream gradient represents the gradient of the loss with respect to the output of the current layer, which is used in the backward pass to compute gradients for the input and weights.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_3 = {
    'question': "When calculating the gradient with respect to the weights of the convolution layer, why do we need to sum over all output pixels?",
    'options_list': [
        "A) Each weight affects only one specific output pixel.",
        "B) Each weight affects all output pixels, so we must sum the contributions.",
        "C) To normalize the gradient values.",
        "D) To ensure the gradient is zero-centered."
    ],
    'correct_answer': 'B',
    'explanation': "Each weight in the convolution kernel affects all output pixels as it strides across the input, so the gradients need to be summed over all output pixels.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_4 = {
    'question': "What is the mathematical operation used to compute the gradient with respect to the weights in a convolution layer?",
    'options_list': [
        "A) Matrix inversion",
        "B) Cross-correlation between the input and the upstream gradient",
        "C) Dot product of the input and the kernel",
        "D) Element-wise multiplication of input and output"
    ],
    'correct_answer': 'B',
    'explanation': "The gradient with respect to the weights is computed as the cross-correlation between the input and the upstream gradient.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_5 = {
    'question': "What does the chain rule help us achieve in the backward pass of a convolution layer?",
    'options_list': [
        "A) It simplifies the forward pass operation.",
        "B) It allows us to compute the gradients with respect to both the input and the weights.",
        "C) It normalizes the kernel values during training.",
        "D) It optimizes the learning rate for gradient descent."
    ],
    'correct_answer': 'B',
    'explanation': "The chain rule allows us to compute the gradients with respect to both the input and the weights by linking the upstream gradients to the local gradients in the convolution layer.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_tf_question_1 = {
    'question': "The backward pass of a convolution layer is computed using the cross-correlation operation.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "In the backward pass of a convolution layer, the gradient with respect to the weights is computed as a cross-correlation between the input and the upstream gradient.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_tf_question_2 = {
    'question': "In the backward pass, the kernel needs to be flipped when computing the gradient with respect to the input.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "When computing the gradient with respect to the input during the backward pass, the kernel is flipped and a cross-correlation is performed with the upstream gradient.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_tf_question_3 = {
    'question': "In a convolution layer, the gradient with respect to a single kernel pixel only affects one output pixel during the backward pass.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "A single kernel pixel affects multiple output pixels during the forward pass, so its gradient affects all those output pixels during the backward pass.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_tf_question_4 = {
    'question': "The output gradient size in the backward pass is the same as the input size because of padding.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Padding is added to the input to ensure that the output gradient size in the backward pass matches the input size.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_tf_question_5 = {
    'question': "The gradient with respect to the input is computed as a convolution between the upstream gradient and the kernel.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "The gradient with respect to the input is computed as a convolution of the upstream gradient and the kernel, highlighting the duality between forward and backward passes.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}


lesson_6_lecture_gradient_conv_layer_mpc_question_1 = {
    'question': "Given a 3x3 input $$X$$ and a 2x2 kernel $$K$$, the forward pass generates a 2x2 output matrix $$Y$$. Suppose the input $$X$$ is:\n"
                "$$X = \\begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \\end{bmatrix}$$\n"
                "and the kernel $$K = \\begin{bmatrix} k_{1,1} & k_{1,2} \\\\ k_{2,1} & k_{2,2} \\end{bmatrix}$$. If the loss gradient from the next layer $$\\frac{\\partial L}{\\partial Y} = \\begin{bmatrix} 1 & 1 \\\\ 1 & 1 \\end{bmatrix}$$, what is the gradient with respect to the kernel element $$k_{1,1}$$?",
    'options_list': [
        "A) 9",
        "B) 10",
        "C) 12",
        "D) 14"
    ],
    'correct_answer': 'C',
    'explanation': "The gradient for $$k_{1,1}$$ is calculated by summing the contributions from each output pixel where $$k_{1,1}$$ interacts with the input values: "
                   "$$(1 \\times 1) + (1 \\times 2) + (1 \\times 4) + (1 \\times 5) = 12$$.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_2 = {
    'question': "Given a 3x3 input $$X = \\begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \\end{bmatrix}$$ and a 2x2 kernel $$K = \\begin{bmatrix} k_{1,1} & k_{1,2} \\\\ k_{2,1} & k_{2,2} \\end{bmatrix}$$, the forward pass generates a 2x2 output matrix $$Y$$. Assuming the loss gradient from the next layer $$\\frac{\\partial L}{\\partial Y} = \\begin{bmatrix} 2 & 2 \\\\ 2 & 2 \\end{bmatrix}$$, what is the gradient with respect to the input pixel $$X(0,0)$$?",
    'options_list': [
        "A) $$2k_{1,1}$$",
        "B) $$4k_{1,1}$$",
        "C) $$k_{1,1}$$",
        "D) $$8k_{1,1}$$"
    ],
    'correct_answer': 'A',
    'explanation': "The gradient with respect to $$X(0,0)$$ is influenced by $$Y(0,0)$$. Using the chain rule: "
                   "$$\\frac{\\partial L}{\\partial X(0,0)} = \\frac{\\partial L}{\\partial Y(0,0)} \\times k_{1,1} = 2 \\times k_{1,1}$$.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_3 = {
    'question': "Suppose we have a 4x4 input $$X$$ and a 3x3 kernel $$K$$. The resulting output $$Y$$ is a 2x2 matrix. If the kernel "
                "$$K = \\begin{bmatrix} k_{1,1} & k_{1,2} & k_{1,3} \\\\ k_{2,1} & k_{2,2} & k_{2,3} \\\\ k_{3,1} & k_{3,2} & k_{3,3} \\end{bmatrix}$$ "
                "and the loss gradient $$\\frac{\\partial L}{\\partial Y} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix}$$, which input pixel contributes to the gradient of $$k_{2,2}$$ when calculating $$\\frac{\\partial L}{\\partial k_{2,2}}$$?",
    'options_list': [
        "A) $$X(1,1), X(1,2), X(2,1), X(2,2)$$",
        "B) $$X(0,0), X(1,1), X(2,2), X(3,3)$$",
        "C) $$X(0,1), X(1,0), X(2,2), X(3,3)$$",
        "D) $$X(1,1), X(2,2)$$"
    ],
    'correct_answer': 'A',
    'explanation': "The kernel element $$k_{2,2}$$ interacts with the input pixels $$X(1,1), X(1,2), X(2,1), X(2,2)$$ during the forward pass. Hence, their values contribute to the gradient when calculating $$\\frac{\\partial L}{\\partial k_{2,2}}$$.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}


lesson_6_lecture_gradient_conv_layer_mpc_question_4 = {
    'question': "Given the input matrix $X$ and a $2 \\times 2$ kernel $K$, the output $Y$ is calculated through cross-correlation. Suppose the input $X$ and kernel $K$ are given by:\n\n"
                 "$X = \\begin{bmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \\end{bmatrix}$, \n\n"
                 "$K = \\begin{bmatrix} k_{1,1} & k_{1,2} \\\\ k_{2,1} & k_{2,2} \\end{bmatrix}$.\n\n"
                 "If the gradient from the next layer $\\frac{\\partial L}{\\partial Y}$ is:\n\n"
                 "$\\frac{\\partial L}{\\partial Y} = \\begin{bmatrix} 2 & 0.5 \\\\ -1 & 1.5 \\end{bmatrix}$,\n\n"
                 "what is the gradient with respect to $k_{1,1}$?",
    'options_list': [
        "A) 12",
        "B) 15.5",
        "C) 5",
        "D) 10.5"
    ],
    'correct_answer': 'D',
    'explanation': "The gradient with respect to $k_{1,1}$ is computed by summing the product of each element in $\\frac{\\partial L}{\\partial Y}$ with the corresponding input elements affected by $k_{1,1}$:\n\n"
                   "$\\frac{\\partial L}{\\partial k_{1,1}} = (2 \\times 1) + (0.5 \\times 2) + (-1 \\times 4) + (1.5 \\times 5) = 2 + 1 - 4 + 7.5 = 10.5$.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_5 = {
    'question': "Suppose we have the input $X$ and a $2 \\times 2$ kernel $K$ defined as:\n\n"
                 "$X = \\begin{bmatrix} 1 & 3 & 5 \\\\ 7 & 9 & 11 \\\\ 13 & 15 & 17 \\end{bmatrix}$, \n\n"
                 "$K = \\begin{bmatrix} k_{1,1} & k_{1,2} \\\\ k_{2,1} & k_{2,2} \\end{bmatrix}$.\n\n"
                 "The gradient from the next layer $\\frac{\\partial L}{\\partial Y}$ is:\n\n"
                 "$\\frac{\\partial L}{\\partial Y} = \\begin{bmatrix} 0.5 & -0.2 \\\\ 1.3 & -0.7 \\end{bmatrix}$.\n\n"
                 "What is the gradient with respect to $k_{2,2}$?",
    'options_list': [
        "A) 5.1",
        "B) -3.6",
        "C) 8.4",
        "D) 10.7"
    ],
    'correct_answer': 'A',
    'explanation': "The gradient with respect to $k_{2,2}$ is computed by summing the product of each element in $\\frac{\\partial L}{\\partial Y}$ with the input elements affected by $k_{2,2}$:\n\n"
                   "$\\frac{\\partial L}{\\partial k_{2,2}} = (0.5 \\times 9) + (-0.2 \\times 11) + (1.3 \\times 15) + (-0.7 \\times 17) = 4.5 - 2.2 + 19.5 - 11.9 = 5.1$.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_lecture_gradient_conv_layer_mpc_question_6 = {
    'question': "Given the input matrix $X$ and a $2 \\times 2$ kernel $K$, the output $Y$ is calculated through cross-correlation. Suppose the input $X$ and kernel $K$ are:\n\n"
                 "$X = \\begin{bmatrix} 2 & 4 & 6 \\\\ 8 & 10 & 12 \\\\ 14 & 16 & 18 \\end{bmatrix}$, \n\n"
                 "$K = \\begin{bmatrix} k_{1,1} & k_{1,2} \\\\ k_{2,1} & k_{2,2} \\end{bmatrix}$.\n\n"
                 "The gradient from the next layer $\\frac{\\partial L}{\\partial Y}$ is:\n\n"
                 "$\\frac{\\partial L}{\\partial Y} = \\begin{bmatrix} -0.5 & 0.3 \\\\ 0.8 & -0.4 \\end{bmatrix}$.\n\n"
                 "What is the gradient with respect to $k_{1,2}$?",
    'options_list': [
        "A) 1.8",
        "B) -2.7",
        "C) 0.6",
        "D) -4.4"
    ],
    'correct_answer': 'B',
    'explanation': "The gradient with respect to $k_{1,2}$ is computed by summing the product of each element in $\\frac{\\partial L}{\\partial Y}$ with the input elements affected by $k_{1,2}$:\n\n"
                   "$\\frac{\\partial L}{\\partial k_{1,2}} = (-0.5 \\times 4) + (0.3 \\times 6) + (0.8 \\times 10) + (-0.4 \\times 12) = -2 + 1.8 + 8 - 4.8 = -2.7$.",
    'chapter_information': 'Lesson 6 Lecture Gradient for conv layer'
}

lesson_6_3_cnn_mpc_question_1 = {
    'question': "What happens to the receptive field of a neuron in deeper layers of a Convolutional Neural Network (CNN)?",
    'options_list': [
        "A) It decreases as it processes fewer regions of the input image.",
        "B) It remains the same size regardless of the network's depth.",
        "C) It increases as it combines information from larger regions of the input image.",
        "D) It only changes when the kernel size is modified."
    ],
    'correct_answer': 'C',
    'explanation': "The receptive field of a neuron in deeper layers increases because it combines information from progressively larger regions of the input image, allowing the network to extract more abstract features.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

lesson_6_3_cnn_mpc_question_2 = {
    'question': "In a Convolutional Neural Network, what is the purpose of alternating convolutional layers with non-linearities like ReLU?",
    'options_list': [
        "A) To reduce the size of the input image.",
        "B) To increase the network's representational power.",
        "C) To keep the network linear.",
        "D) To replace pooling layers."
    ],
    'correct_answer': 'B',
    'explanation': "Non-linearities like ReLU are used in CNNs to introduce non-linearity into the network, thereby increasing its representational power. Without these non-linearities, the network would only perform linear operations, which limits its ability to model complex functions.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

lesson_6_3_cnn_mpc_question_3 = {
    'question': "Which of the following best describes the equivariance property of convolutional layers in CNNs?",
    'options_list': [
        "A) The network can handle changes in scale.",
        "B) Feature detection in the output maps shifts correspondingly when the input image is shifted.",
        "C) The network can classify images regardless of their rotation.",
        "D) The depth of the output changes with each convolution."
    ],
    'correct_answer': 'B',
    'explanation': "Equivariance in convolutional layers means that if the input image is shifted, the detected features in the output maps will also shift correspondingly, preserving spatial information.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

lesson_6_3_cnn_mpc_question_4 = {
    'question': "When building a CNN, which of the following factors determines the depth of the output in a convolutional layer?",
    'options_list': [
        "A) The number of channels in the input image.",
        "B) The number of kernels used in the convolutional layer.",
        "C) The size of the kernel.",
        "D) The type of activation function used."
    ],
    'correct_answer': 'B',
    'explanation': "The depth of the output in a convolutional layer is determined by the number of kernels (or filters) used in that layer. Each kernel produces a separate feature map, contributing to the overall depth of the output.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

lesson_6_3_cnn_mpc_question_5 = {
    'question': "Which of the following statements about pooling layers in a CNN is true?",
    'options_list': [
        "A) Pooling layers reduce the input's depth while keeping the width and height constant.",
        "B) Pooling layers increase the network's computational complexity.",
        "C) Pooling layers do not have learnable parameters.",
        "D) Pooling layers must always follow a fully connected layer."
    ],
    'correct_answer': 'C',
    'explanation': "Pooling layers do not have learnable parameters. They perform a fixed operation (e.g., max-pooling) to reduce the spatial dimensions (height and width) of the input, while keeping the depth constant.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

# Question 1: Number of Parameters in a Convolutional Layer
lesson_6_3_cnn_computational_question_1 = {
    'question': "Consider a convolutional layer with an input of size (batch size, channels, height, width) = (1, 3, 32, 32) and 10 filters of size 5x5. How many trainable parameters are in this layer, including the biases?",
    'options_list': [
        "A) 250",
        "B) 760",
        "C) 7600",
        "D) 1510"
    ],
    'correct_answer': 'D',
    'explanation': "The number of parameters in a convolutional layer is given by (number of filters) × (filter size in height × filter size in width × number of input channels) + (number of filters for biases). In this case: (10 filters) × (5 × 5 × 3) + (10 biases) = 750 + 10 = 1510.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

# Question 2: Memory Requirements for Activations
lesson_6_3_cnn_computational_question_2 = {
    'question': "A convolutional layer has an input size of (1, 3, 64, 64) and 16 filters of size 3x3 with a stride of 1 and padding of 1. What is the size of the output tensor, and how much memory (in number of elements) does it occupy?",
    'options_list': [
        "A) (1, 16, 62, 62) - 61,504 elements",
        "B) (1, 16, 64, 64) - 65,536 elements",
        "C) (1, 16, 32, 32) - 16,384 elements",
        "D) (1, 16, 64, 64) - 16,384 elements"
    ],
    'correct_answer': 'B',
    'explanation': "The output size for a convolutional layer with padding of 1, stride of 1, and kernel size 3x3 is the same as the input size, i.e., (64, 64) for each of the 16 filters. Thus, the output tensor is of size (1, 16, 64, 64). The total number of elements is 1 × 16 × 64 × 64 = 65,536.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

# Question 3: Gradient Calculation in Convolution
lesson_6_3_cnn_computational_question_3 = {
    'question': "Given an input tensor of size (1, 1, 3, 3) and a single 2x2 filter with a stride of 1, the forward convolution produces an output of size (1, 1, 2, 2). If the upstream gradient (∂L/∂Y) is a tensor of ones with size (1, 1, 2, 2), what is the gradient with respect to the bias in this convolutional layer?",
    'options_list': [
        "A) 1",
        "B) 2",
        "C) 3",
        "D) 4"
    ],
    'correct_answer': 'D',
    'explanation': "The gradient with respect to the bias in a convolutional layer is the sum of all elements in the upstream gradient (∂L/∂Y). Since the upstream gradient tensor has four elements, each being 1, the sum is 1 + 1 + 1 + 1 = 4.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

# Question 4: Transposed Convolution Output Size
lesson_6_3_cnn_computational_question_4 = {
    'question': "For a transposed convolution with an input size of (1, 1, 3, 3), a kernel size of 2x2, stride of 1, and padding of 0, what will be the output size?",
    'options_list': [
        "A) (1, 1, 2, 2)",
        "B) (1, 1, 4, 4)",
        "C) (1, 1, 5, 5)",
        "D) (1, 1, 6, 6)"
    ],
    'correct_answer': 'C',
    'explanation': "The output size for a transposed convolution is calculated as: (input size - 1) × stride + kernel size - 2 × padding. In this case, (3 - 1) × 1 + 2 = 5 for both height and width. So, the output size is (1, 1, 5, 5).",
    'chapter_information': '6.3 Convolutional Neural Networks'
}

# Question 5: Backward Computation of Convolution
lesson_6_3_cnn_computational_question_5 = {
    'question': "In the backward pass of a convolutional layer, given an input of size (1, 1, 4, 4) and a 2x2 kernel, which statement about the gradient with respect to the input (∂L/∂X) is true?",
    'options_list': [
        "A) The gradient has the same size as the output tensor.",
        "B) The gradient has the same size as the input tensor.",
        "C) The gradient has double the size of the input tensor.",
        "D) The gradient only affects the regions where the kernel was applied."
    ],
    'correct_answer': 'B',
    'explanation': "In the backward pass of a convolutional layer, the gradient with respect to the input (∂L/∂X) has the same size as the input tensor, allowing the gradients to be propagated correctly to the previous layers.",
    'chapter_information': '6.3 Convolutional Neural Networks'
}



# Question 1
mquest1ion_1 = {
    'question': "In a convolutional neural network (CNN) layer, given an input size of 227x227x3 (height x width x channels), 96 filters, and a filter size of 11x11 with a stride of 4 and no padding, calculate the output size of this convolutional layer.",
    'options_list': [
        "56x56x96",
        "55x55x96",
        "112x112x96",
        "28x28x96"
    ],
    'correct_answer': "55x55x96",
    'explanation': (
        "The output dimensions can be calculated using the formula:\n"
        "output_dim = ((input_dim - kernel_size) / stride) + 1\n"
        "output_dim = ((227 - 11) / 4) + 1 = 55\n"
        "Thus, the output size is 55x55 with 96 filters as the depth."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 2
mqu1estion_2 = {
    'question': "If a convolutional layer has an output size of 64x56x56, calculate the memory required to store the activations of this layer assuming 32-bit floating-point precision.",
    'options_list': [
        "784 KB",
        "1,134 KB",
        "500 KB",
        "1,024 KB"
    ],
    'correct_answer': "784 KB",
    'explanation': (
        "Number of elements in the output = 64 * 56 * 56 = 200,704\n"
        "Bytes per element = 4 (32-bit floating point)\n"
        "Total memory (in bytes) = 200,704 * 4 = 802,816 bytes\n"
        "Convert to kilobytes: 802,816 / 1,024 ≈ 784 KB."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 3
mqu1estion_3 = {
    'question': (
        "Consider a convolutional layer in a CNN with the following properties:\n"
        "- Input channels: 3\n"
        "- Output channels (filters): 64\n"
        "- Kernel size: 11x11\n"
        "- Stride: 1\n"
        "- Padding: 0\n\n"
        "Calculate the total number of parameters (weights) in this convolutional layer, including biases."
    ),
    'options_list': [
        "23,296",
        "34,944",
        "72,000",
        "1,728"
    ],
    'correct_answer': "23,296",
    'explanation': (
        "The number of weights = output channels * input channels * kernel width * kernel height\n"
        "= 64 * 3 * 11 * 11 = 23,232\n"
        "The number of biases = 64 (one bias per output channel)\n"
        "Total parameters = 23,232 (weights) + 64 (biases) = 23,296."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 4
mquestio1n_4 = {
    'question': "Given the output size of a convolutional layer is 55x55x96 and each activation is stored as a 32-bit float, calculate the total memory size in kilobytes required to store these activations.",
    'options_list': [
        "784 KB",
        "1,134 KB",
        "1,024 KB",
        "512 KB"
    ],
    'correct_answer': "1,134 KB",
    'explanation': (
        "Number of elements in the output = 55 * 55 * 96 = 290,400\n"
        "Bytes per element = 4 (32-bit floating point)\n"
        "Total memory (in bytes) = 290,400 * 4 = 1,161,600 bytes\n"
        "Convert to kilobytes: 1,161,600 / 1,024 ≈ 1,134 KB."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 5
mques1tion_5 = {
    'question': (
        "For a convolutional layer with the following specifications:\n"
        "- Input size: 224x224x3\n"
        "- Number of filters: 64\n"
        "- Filter size: 3x3\n"
        "- Stride: 1\n"
        "- Padding: 1 (same padding)\n\n"
        "Calculate the number of floating point operations (FLOPs) for one forward pass through this layer."
    ),
    'options_list': [
        "150,000",
        "72,855,552",
        "1,728",
        "3,200,000"
    ],
    'correct_answer': "72,855,552",
    'explanation': (
        "Number of output elements = 224 * 224 * 64 = 3,211,264\n"
        "Number of operations per output element = 3 * 3 * 3 = 27 (since each filter operates over a 3x3 window across 3 input channels)\n"
        "Total FLOPs = 3,211,264 * 27 = 72,855,552."
    ),
    'chapter_information': "Michigan Lecture 8"
}


# Question 6
question_6 = {
    'question': (
        "A convolutional neural network (CNN) layer has an output of size 112x112x128. "
        "Assuming each activation is stored as a 32-bit float, calculate the total memory required to store the activations of this layer in kilobytes."
    ),
    'options_list': [
        "1,280 KB",
        "512 KB",
        "6,144 KB",
        "4,096 KB"
    ],
    'correct_answer': "6,144 KB",
    'explanation': (
        "Number of elements in the output = 112 * 112 * 128 = 1,605,632\n"
        "Bytes per element = 4 (32-bit floating point)\n"
        "Total memory (in bytes) = 1,605,632 * 4 = 6,422,528 bytes\n"
        "Convert to kilobytes: 6,422,528 / 1,024 = 6,144 KB."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 7
question_7 = {
    'question': (
        "Given a convolutional layer with an output size of 28x28x256 and using 32-bit floating-point precision, "
        "calculate the total memory required to store the activations of this layer in kilobytes."
    ),
    'options_list': [
        "100 KB",
        "800 KB",
        "3,200 KB",
        "4,096 KB"
    ],
    'correct_answer': "800 KB",
    'explanation': (
        "Number of elements in the output = 28 * 28 * 256 = 200,704\n"
        "Bytes per element = 4 (32-bit floating point)\n"
        "Total memory (in bytes) = 200,704 * 4 = 802,816 bytes\n"
        "Convert to kilobytes: 802,816 / 1,024 ≈ 800 KB."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 8
question_8 = {
    'question': (
        "If a fully connected layer has 4,096 output nodes and receives an input of size 7x7x512, "
        "calculate the memory required to store the weights of this layer in megabytes, assuming 32-bit floating-point precision."
    ),
    'options_list': [
        "16 MB",
        "102 MB",
        "4 MB",
        "50 MB"
    ],
    'correct_answer': "102 MB",
    'explanation': (
        "Number of weights = input size * output size = (7 * 7 * 512) * 4096 = 102,760,448\n"
        "Bytes per element = 4 (32-bit floating point)\n"
        "Total memory (in bytes) = 102,760,448 * 4 = 411,041,792 bytes\n"
        "Convert to megabytes: 411,041,792 / (1024 * 1024) ≈ 102 MB."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 9
question_9 = {
    'question': (
        "A CNN layer has an input of size 224x224x3 and produces an output of size 112x112x64. "
        "Calculate the memory required to store both the input and output activations in kilobytes, assuming 32-bit floating-point precision."
    ),
    'options_list': [
        "1,600 KB",
        "2,500 KB",
        "3,200 KB",
        "4,096 KB"
    ],
    'correct_answer': "2,500 KB",
    'explanation': (
        "Memory for input = 224 * 224 * 3 * 4 = 602,112 bytes\n"
        "Convert to kilobytes: 602,112 / 1,024 ≈ 588 KB\n"
        "Memory for output = 112 * 112 * 64 * 4 = 3,211,264 bytes\n"
        "Convert to kilobytes: 3,211,264 / 1,024 ≈ 3,136 KB\n"
        "Total memory = 588 KB + 3,136 KB = 2,500 KB."
    ),
    'chapter_information': "Michigan Lecture 8"
}

# Question 10
question_10 = {
    'question': (
        "A convolutional layer has an output size of 14x14x512. Assuming 32-bit floating-point precision, "
        "what is the total memory required to store the activations of this layer in kilobytes?"
    ),
    'options_list': [
        "400 KB",
        "500 KB",
        "800 KB",
        "1,000 KB"
    ],
    'correct_answer': "400 KB",
    'explanation': (
        "Number of elements in the output = 14 * 14 * 512 = 100,352\n"
        "Bytes per element = 4 (32-bit floating point)\n"
        "Total memory (in bytes) = 100,352 * 4 = 401,408 bytes\n"
        "Convert to kilobytes: 401,408 / 1,024 ≈ 400 KB."
    ),
    'chapter_information': "Michigan Lecture 8"
}






KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_6_MPC = KC_MPC_QUESTIONS[:-1]
