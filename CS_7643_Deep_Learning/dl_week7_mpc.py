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
    'explanation': (
        'The authors introduce regularized optimization in image space to better visualize features at each layer. They apply several regularization techniques (like L2 decay and Gaussian blur) to produce clearer, more interpretable images than previous methods.'
    ),
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
    'explanation': (
        'The authors mention using L2 decay, Gaussian blur, and clipping pixels with small norm as regularization techniques for visualization. Dropout is not mentioned as a regularization method in this context.'
    ),
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
    'explanation': (
        'The visualization tool introduced by the authors allows users to view activations from all layers, including convolutional, pooling, and normalization layers, to gain better insights into how the network processes input images.'
    ),
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
    'explanation': (
        'The authors observed that the fully connected layers exhibit the most variation in patterns, indicating increasingly invariant representations learned as the network processes input through its layers.'
    ),
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
    'explanation': (
        'The authors found that representations on later convolutional layers are surprisingly local, with detectors for specific objects like text, flowers, and faces, rather than being purely distributed representations.'
    ),
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

# True/False Questions

question_16 = {
    'question': (
        'In "Understanding Neural Networks Through Deep Visualization", the authors\' visualization tool only works with pre-trained networks and cannot be used with custom models.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        'The authors designed their visualization tool to work with both pre-trained networks and custom models, allowing for flexibility in analyzing various deep neural network architectures.'
    ),
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_17 = {
    'question': (
        'The paper "Understanding Neural Networks Through Deep Visualization" introduces a new architecture that outperforms existing object detection models.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        'The paper does not introduce a new architecture for object detection. Instead, it presents tools for visualizing and understanding the inner workings of existing deep neural network architectures.'
    ),
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_18 = {
    'question': (
        'According to "Understanding Neural Networks Through Deep Visualization", the authors found that looking at live activations that change in response to user input helps build intuitions about how convnets work.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        'The authors describe how observing live activations in response to user input can help build intuitions about how convolutional neural networks (convnets) respond to different patterns and changes in input.'
    ),
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_19 = {
    'question': (
        'In "Understanding Neural Networks Through Deep Visualization", the authors state that previous methods for visualizing preferred inputs produced highly recognizable natural images.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': (
        'The authors mention that previous visualization methods often resulted in images that did not resemble natural images, but rather contained extreme pixel values and structured high-frequency patterns.'
    ),
    'chapter_information': 'Deep Viz Paper - Perplexity'
}

question_20 = {
    'question': (
        'According to "Understanding Neural Networks Through Deep Visualization", the authors\' regularization techniques aim to produce qualitatively clearer, more interpretable visualizations compared to previous methods.'
    ),
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': (
        'The paper introduces new regularization techniques that produce clearer and more interpretable visualizations, improving upon the images generated by previous gradient-based approaches.'
    ),
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
    'explanation': 'Grad-CAM uses the gradients of any target concept flowing into the final convolutional layer to produce a coarse localization map that highlights the important regions in the image for predicting the concept.',
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
    'explanation': 'Grad-CAM provides a class-discriminative localization map applicable to various CNN models without requiring changes to the architecture or retraining. While it can be combined with Guided Backpropagation to create high-resolution visualizations, high-resolution is not an inherent advantage of Grad-CAM alone.',
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
    'explanation': 'Grad-CAM can be used to visualize and interpret decisions of CNN-based models in image classification, image captioning, and visual question answering, making it a versatile tool across multiple tasks.',
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
    'explanation': 'Grad-CAM uses the gradients of the target class score with respect to the feature maps of a convolutional layer to generate a localization map that highlights regions relevant for predicting the class.',
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
    'explanation': 'Grad-CAM applies a ReLU to the weighted combination of feature maps to focus on regions that have a positive influence on the class of interest, filtering out negative influences that might belong to other categories.',
    'chapter_information': 'GradCAM - Perplexity'
}

# True/False Questions
gradcam_question_6 = {
    'question': 'Grad-CAM can only be applied to CNNs that use global average pooling.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'Grad-CAM generalizes the concept of Class Activation Mapping (CAM) and can be applied to a wide variety of CNN architectures, not just those using global average pooling.',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_7 = {
    'question': 'The Grad-CAM localization map has the same spatial dimensions as the final convolutional feature map.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'The Grad-CAM localization map retains the spatial dimensions of the final convolutional feature map, highlighting important regions in the input image for the target class.',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_8 = {
    'question': 'Guided Grad-CAM combines Grad-CAM with Guided Backpropagation to produce high-resolution visualizations.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Guided Grad-CAM combines the coarse localization map from Grad-CAM with the fine-grained details from Guided Backpropagation, resulting in high-resolution, class-discriminative visualizations.',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_9 = {
    'question': 'Grad-CAM requires modifying and retraining the original network architecture.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'One of the key advantages of Grad-CAM is that it does not require any modification to the original network architecture or retraining. It works on pre-trained models to produce visual explanations.',
    'chapter_information': 'GradCAM - Perplexity'
}

gradcam_question_10 = {
    'question': 'According to the paper, Grad-CAM visualizations are robust to adversarial perturbations.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'The paper demonstrates that Grad-CAM visualizations are fairly robust to adversarial noise, highlighting the correct regions even when the network is fooled by adversarial examples.',
    'chapter_information': 'GradCAM - Perplexity'
}


# Multiple Choice Questions
uml14_question_1 = {
    'question': 'What was the main impact of deep learning on object detection performance from 2013-2016?',
    'options_list': [
        'a) It caused a plateau in performance',
        'b) It led to small, incremental improvements',
        'c) It resulted in massive improvements and overcame a previous plateau',
        'd) It had no significant impact'
    ],
    'correct_answer': 'c) It resulted in massive improvements and overcame a previous plateau',
    'explanation': 'The lecture notes state that starting in 2013, when deep learning was first applied to object detection, there was a "huge jump" in performance that overcame the previous plateau from 2010-2012. This led to "massive improvements in object detection" from 2013-2016.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_2 = {
    'question': 'What was the key difference between Fast R-CNN and the original (slow) R-CNN?',
    'options_list': [
        'a) Fast R-CNN used a different loss function',
        'b) Fast R-CNN swapped the order of convolution and pooling',
        'c) Fast R-CNN used a different region proposal method',
        'd) Fast R-CNN added more convolutional layers'
    ],
    'correct_answer': 'b) Fast R-CNN swapped the order of convolution and pooling',
    'explanation': 'The notes state that Fast R-CNN "swapped the order of convolution and pooling" compared to the original slow R-CNN. This gave accuracy improvements and significant speed gains.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_3 = {
    'question': 'What was used to generate region proposals in early R-CNN models?',
    'options_list': [
        'a) Convolutional neural networks',
        'b) Selective search',
        'c) Random sampling',
        'd) Manual annotation'
    ],
    'correct_answer': 'b) Selective search',
    'explanation': 'The notes mention that "back in the days, people used to use things like selective search" as the region proposal method, treating it as a black box separate from the neural network.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_4 = {
    'question': 'Why is directly visualizing higher-layer convolutional filters (e.g., as images) not very informative?',
    'options_list': [
        'a) Because higher-layer filters are too simple and lack complexity.',
        'b) Because higher-layer filters have weights that cannot be represented as RGB images.',
        'c) Because higher-layer filters have too few parameters to visualize.',
        'd) Because higher-layer filters are not trained during backpropagation.'
    ],
    'correct_answer': 'b) Because higher-layer filters have weights that cannot be represented as RGB images.',
    'explanation': 'Higher-layer convolutional filters operate on feature maps with many channels (not just RGB), making it difficult to represent their weights as RGB images. The filters span multiple input channels, so their weights do not correspond directly to interpretable visual patterns when visualized as images.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_5 = {
    'question': 'What is the main idea behind using "maximally activating patches" to understand a neuron\'s behavior?',
    'options_list': [
        'a) Training the network on patches with maximum pixel values.',
        'b) Finding input patches from the dataset that cause maximum activation of a specific neuron.',
        'c) Generating random noise images to see neuron responses.',
        'd) Visualizing the weights of the neuron directly as an image.'
    ],
    'correct_answer': 'b) Finding input patches from the dataset that cause maximum activation of a specific neuron.',
    'explanation': 'By finding and examining the input patches from real images that cause a specific neuron to activate the most, we can infer what features the neuron is sensitive to. This method helps reveal the visual patterns that the neuron detects.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_6 = {
    'question': 'What is the purpose of using "guided backpropagation" instead of standard backpropagation when generating visualizations?',
    'options_list': [
        'a) To increase computational efficiency during training.',
        'b) To zero out both negative activations and negative gradients during backpropagation to produce clearer visualizations.',
        'c) To incorporate adversarial examples into the training process.',
        'd) To prevent overfitting by modifying the ReLU activation function.'
    ],
    'correct_answer': 'b) To zero out both negative activations and negative gradients during backpropagation to produce clearer visualizations.',
    'explanation': 'Guided backpropagation modifies the backpropagation process by zeroing out negative gradients during the backward pass through ReLU layers, in addition to zeroing out gradients where the forward activation is negative. This results in sharper and more interpretable visualizations.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_7 = {
    'question': 'In neural style transfer, what is the role of the Gram matrix?',
    'options_list': [
        'a) It captures the spatial layout of features in the image.',
        'b) It represents the statistical correlations between different feature maps, capturing style information.',
        'c) It stores the learned weights of the neural network layers.',
        'd) It normalizes the activations to prevent vanishing gradients.'
    ],
    'correct_answer': 'b) It represents the statistical correlations between different feature maps, capturing style information.',
    'explanation': 'The Gram matrix computes the correlations between feature maps at a particular layer, effectively capturing the texture and style information of an image while discarding spatial arrangements.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_8 = {
    'question': 'What is the main advantage of using feed-forward networks for fast neural style transfer compared to optimization-based methods?',
    'options_list': [
        'a) They can apply any style without retraining the network.',
        'b) They require less training data.',
        'c) They can generate stylized images in real-time since the style transfer happens in a single forward pass.',
        'd) They produce higher-quality results than optimization-based methods.'
    ],
    'correct_answer': 'c) They can generate stylized images in real-time since the style transfer happens in a single forward pass.',
    'explanation': 'Feed-forward networks are trained to perform style transfer in a single forward pass, making them much faster than optimization-based methods that require iterative optimization per image, enabling real-time style transfer.',
    'chapter_information': 'U Michigan lecture 14'
}

# True/False Questions
uml14_question_9 = {
    'question': 'Saliency maps computed via gradient backpropagation can help identify which pixels in the input image most affect the final class score.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Saliency maps highlight the regions of the input image that have the greatest influence on the network\'s output. By computing the gradient of the class score with respect to the input pixels, we can see which pixels contribute most to the decision.',
    'chapter_information': 'U Michigan lecture 14'
}

uml14_question_10 = {
    'question': 'Instance normalization was originally developed to improve the training of generative adversarial networks (GANs) for image generation tasks.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'Instance normalization was originally introduced to improve the quality of images generated by fast neural style transfer models. It normalizes feature maps on a per-instance basis, which helps in capturing stylistic features effectively.',
    'chapter_information': 'U Michigan lecture 14'
}

# Multiple Choice Questions
gt7_question_1 = {
    'question': 'In the paper "Understanding Neural Networks Through Deep Visualization" by Yosinski et al., which of the following is NOT mentioned as a tool introduced for visualizing neural networks?',
    'options_list': [
        'a) A tool that visualizes activations on each layer of a trained convnet',
        'b) A tool for visualizing features via regularized optimization in image space',
        'c) A tool for generating adversarial examples',
        'd) A tool that works on a pretrained convnet with minimal setup'
    ],
    'correct_answer': 'c) A tool for generating adversarial examples',
    'explanation': 'The paper introduces two main tools - one for visualizing activations and another for visualizing features via regularized optimization. It does not mention a tool specifically for generating adversarial examples.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_2 = {
    'question': 'What is a common method for visualizing what a convolutional neural network has learned after training?',
    'options_list': [
        'a) Plotting the loss curve over epochs',
        'b) Visualizing the convolutional kernel weights as images',
        'c) Analyzing the random initialization of weights',
        'd) Examining the raw data inputs'
    ],
    'correct_answer': 'b) Visualizing the convolutional kernel weights as images',
    'explanation': 'Visualizing the convolutional kernels (filters) by reshaping their weights into images allows us to see what features the network has learned to detect, such as edges, textures, or colors.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_3 = {
    'question': 'Why might it be more challenging to visualize convolutional kernels in modern neural networks?',
    'options_list': [
        'a) Modern networks do not use convolutional layers',
        'b) Modern networks use very small kernels (e.g., 3x3), making meaningful visualization difficult',
        'c) The kernels are encoded in a way that cannot be converted to images',
        'd) Visualization tools are incompatible with modern architectures'
    ],
    'correct_answer': 'b) Modern networks use very small kernels (e.g., 3x3), making meaningful visualization difficult',
    'explanation': 'Modern networks often use small convolutional kernels like 3x3, which makes it harder to interpret the patterns when visualized because they capture less spatial information.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_4 = {
    'question': 'What is one reason individual neurons in a neural network might be difficult to interpret?',
    'options_list': [
        'a) Neurons are not involved in learning features',
        'b) Neurons learn distributed representations and may not correspond to single, interpretable features',
        'c) All neurons perform identical functions, making them redundant',
        'd) Neurons only process noise and have no meaningful output'
    ],
    'correct_answer': 'b) Neurons learn distributed representations and may not correspond to single, interpretable features',
    'explanation': 'Neural networks learn distributed representations, meaning that individual neurons contribute to multiple features, and features are represented across many neurons, making individual interpretation challenging.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_5 = {
    'question': 'What is the main advantage of their regularized optimization method for feature visualization compared to previous methods, according to "Understanding Neural Networks Through Deep Visualization" by Yosinski et al.?',
    'options_list': [
        'a) It produces faster results',
        'b) It generates more recognizable images',
        'c) It requires less computational power',
        'd) It works on untrained networks'
    ],
    'correct_answer': 'b) It generates more recognizable images',
    'explanation': 'The paper emphasizes that their new regularization methods "combine to produce qualitatively clearer, more interpretable visualizations" compared to previous methods.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_6 = {
    'question': 'What is one way to visualize the most highly activating image patches for a specific neuron or filter in a convolutional neural network?',
    'options_list': [
        'a) Randomly sampling patches from the dataset',
        'b) Identifying and plotting the image patches that cause maximum activation in that neuron',
        'c) Visualizing the neuron\'s weights directly as an image',
        'd) Applying a uniform filter across all images'
    ],
    'correct_answer': 'b) Identifying and plotting the image patches that cause maximum activation in that neuron',
    'explanation': 'By finding the image patches from the dataset that cause the highest activation in a specific neuron, we can visualize what kind of input features that neuron is most responsive to.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

# True/False Questions
gt7_question_7 = {
    'question': 'Visualizing the activation maps (also known as feature maps) of a convolutional neural network can help us understand which features the network responds to in an input image.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Activation maps show the responses of different filters to an input image. By visualizing them, we can see which parts of the image activate certain filters, revealing the features the network has learned.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_8 = {
    'question': 'Using gradients can provide insights into what a neural network has learned and help identify its weaknesses or biases.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Gradients are fundamental to training neural networks and can be analyzed to understand the network\'s learning process, as well as to test robustness and detect biases.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_9 = {
    'question': 'Visualizations of weights and activations are not useful for debugging neural networks.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'Visualizations can be very helpful in debugging by revealing unexpected patterns, redundancies, or issues in the network\'s learning, allowing developers to make necessary adjustments.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_10 = {
    'question': 'Techniques like t-SNE can be used to reduce high-dimensional activation vectors to two dimensions for visualization purposes.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 't-SNE is a dimensionality reduction technique that projects high-dimensional data into lower dimensions (typically two or three) while preserving the structure, enabling visualization of complex data like neural network activations.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}





KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_7_MPC = KC_MPC_QUESTIONS[:-1]
