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


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_6_MPC = KC_MPC_QUESTIONS[:-1]
