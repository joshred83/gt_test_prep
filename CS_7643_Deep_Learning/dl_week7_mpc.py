
# Multiple Choice Questions

question_11 = {
    'question': (
        'What technique do the authors introduce to visualize features at each layer of a DNN in the paper "Understanding Neural Networks Through Deep Visualization"?'
    ),
    'options_list': [
        'a) Deconvolution',
        'b) Regularized optimization in image space',
        'c) Activation maximization',
        'd) Saliency maps'
    ],
    'correct_answer': 'b) Regularized optimization in image space',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_12 = {
    'question': (
        'Which of the following is NOT mentioned as a regularization method used by the authors in "Understanding Neural Networks Through Deep Visualization"?'
    ),
    'options_list': [
        'a) L2 decay',
        'b) Gaussian blur',
        'c) Clipping pixels with small norm',
        'd) Dropout'
    ],
    'correct_answer': 'd) Dropout',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_13 = {
    'question': (
        'According to "Understanding Neural Networks Through Deep Visualization", the authors\' visualization tool allows viewing activations from:'
    ),
    'options_list': [
        'a) Only the final layer',
        'b) Only convolutional layers',
        'c) All layers including pooling and normalization',
        'd) Only fully connected layers'
    ],
    'correct_answer': 'c) All layers including pooling and normalization',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_14 = {
    'question': (
        'In the paper "Understanding Neural Networks Through Deep Visualization", which layer type shows the most variation in patterns according to the authors?'
    ),
    'options_list': [
        'a) First convolutional layer',
        'b) Middle convolutional layers',
        'c) Final convolutional layer',
        'd) Fully connected layers'
    ],
    'correct_answer': 'd) Fully connected layers',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_15 = {
    'question': (
        'According to "Understanding Neural Networks Through Deep Visualization", the authors found that representations on later convolutional layers tend to be:'
    ),
    'options_list': [
        'a) Highly distributed',
        'b) Somewhat local',
        'c) Completely random',
        'd) Identical to early layers'
    ],
    'correct_answer': 'b) Somewhat local',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

# True/False Questions

question_16 = {
    'question': (
        'In "Understanding Neural Networks Through Deep Visualization", the authors\' visualization tool only works with pre-trained networks and cannot be used with custom models.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_17 = {
    'question': (
        'The paper "Understanding Neural Networks Through Deep Visualization" introduces a new architecture that outperforms existing object detection models.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_18 = {
    'question': (
        'According to "Understanding Neural Networks Through Deep Visualization", the authors found that looking at live activations that change in response to user input helps build intuitions about how convnets work.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_19 = {
    'question': (
        'In "Understanding Neural Networks Through Deep Visualization", the authors state that previous methods for visualizing preferred inputs produced highly recognizable natural images.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_20 = {
    'question': (
        'According to "Understanding Neural Networks Through Deep Visualization", the authors\' regularization techniques aim to produce qualitatively clearer, more interpretable visualizations compared to previous methods.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

# Multiple Choice Questions
gradcam_question_1 = {
    'question': 'What does Grad-CAM stand for?',
    'options_list': [
        'a) Gradient-weighted Class Activation Mapping',
        'b) Gradient Convolutional Activation Method',
        'c) Generalized Class Attention Mechanism',
        'd) Guided Convolutional Attention Mapping'
    ],
    'correct_answer': 'a) Gradient-weighted Class Activation Mapping',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_2 = {
    'question': 'Which of the following is NOT mentioned as an advantage of Grad-CAM over previous visualization methods?',
    'options_list': [
        'a) Class-discriminative',
        'b) High-resolution',
        'c) Applicable to a wide variety of CNN models',
        'd) Requires no architectural changes or re-training'
    ],
    'correct_answer': 'b) High-resolution',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_3 = {
    'question': 'According to the paper, Grad-CAM can be used for which of the following tasks?',
    'options_list': [
        'a) Image classification',
        'b) Image captioning',
        'c) Visual question answering',
        'd) All of the above'
    ],
    'correct_answer': 'd) All of the above',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_4 = {
    'question': 'What type of gradient information does Grad-CAM use?',
    'options_list': [
        'a) Gradients of the output with respect to the input image',
        'b) Gradients of the target class score with respect to feature maps',
        'c) Gradients of the loss with respect to model parameters',
        'd) Gradients of intermediate activations with respect to the input'
    ],
    'correct_answer': 'b) Gradients of the target class score with respect to feature maps',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_5 = {
    'question': 'How does Grad-CAM handle negative importance weights?',
    'options_list': [
        'a) It ignores them',
        'b) It uses their absolute values',
        'c) It applies a ReLU to the weighted combination of maps',
        'd) It subtracts them from positive weights'
    ],
    'correct_answer': 'c) It applies a ReLU to the weighted combination of maps',
    'chapter_information': 'GradCAM - Perplexity'
}

# True/False Questions
gradcam_question_6 = {
    'question': 'Grad-CAM can only be applied to CNNs that use global average pooling.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_7 = {
    'question': 'The Grad-CAM localization map has the same spatial dimensions as the final convolutional feature map.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_8 = {
    'question': 'Guided Grad-CAM combines Grad-CAM with Guided Backpropagation to produce high-resolution visualizations.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_9 = {
    'question': 'Grad-CAM requires modifying and retraining the original network architecture.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_10 = {
    'question': 'According to the paper, Grad-CAM visualizations are robust to adversarial perturbations.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'GradCAM - Perplexity'
}






KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_7_MPC = KC_MPC_QUESTIONS[:-1]
