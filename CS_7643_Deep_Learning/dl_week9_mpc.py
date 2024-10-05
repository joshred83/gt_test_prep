question_1 = {
    'question': (
        'In the paper "Fully Convolutional Networks for Semantic Segmentation," what is the key insight of fully convolutional networks (FCNs) for semantic segmentation?'
    ),
    'options_list': [
        'a) Using only convolutional layers',
        'b) Building networks that take input of arbitrary size and produce correspondingly-sized output',
        'c) Transferring learned representations from classification to segmentation',
        'd) All of the above'
    ],
    'correct_answer': 'd) All of the above',
    'explanation': (
        'The paper highlights that fully convolutional networks (FCNs) take input of arbitrary size, use only convolutional layers, and transfer learned representations from classification tasks to segmentation, allowing efficient and flexible segmentation.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_2 = {
    'question': (
        'According to the paper "Fully Convolutional Networks for Semantic Segmentation," which of the following is NOT a method used by the authors to improve FCN performance?'
    ),
    'options_list': [
        'a) Skip connections',
        'b) In-network upsampling',
        'c) Attention mechanisms',
        'd) Fine-tuning pre-trained classification networks'
    ],
    'correct_answer': 'c) Attention mechanisms',
    'explanation': (
        'The paper describes using skip connections, in-network upsampling, and fine-tuning pre-trained networks to enhance FCN performance, but does not mention the use of attention mechanisms.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_3 = {
    'question': (
        'In the paper "Fully Convolutional Networks for Semantic Segmentation," is it true or false that the authors found class balancing crucial for achieving good performance in semantic segmentation tasks?'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The authors state that despite the mildly unbalanced nature of the labels (with about 3/4 being background), class balancing was found to be unnecessary for achieving good performance in semantic segmentation.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_4 = {
    'question': (
        'What is the purpose of the skip architecture in FCNs, as described in the paper "Fully Convolutional Networks for Semantic Segmentation"?'
    ),
    'options_list': [
        'a) To reduce the number of parameters',
        'b) To combine semantic information from deep layers with appearance information from shallow layers',
        'c) To increase the receptive field size',
        'd) To enable transfer learning from classification networks'
    ],
    'correct_answer': 'b) To combine semantic information from deep layers with appearance information from shallow layers',
    'explanation': (
        'The skip architecture in FCNs fuses information from deep, coarse layers with fine, shallow layers, thereby enhancing the segmentation accuracy by leveraging both semantic and appearance information.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_6 = {
    'question': (
        'In the paper "Fully Convolutional Networks for Semantic Segmentation," what key insight allows the authors to adapt classification networks for segmentation tasks?'
    ),
    'options_list': [
        'A) Using superpixels and proposals for post-processing',
        'B) Building fully convolutional networks (FCNs) that accept input of arbitrary size and produce correspondingly-sized output',
        'C) Incorporating recurrent neural networks for better spatial predictions',
        'D) Fine-tuning only the final classifier layer of pre-trained networks'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The authors introduce the concept of fully convolutional networks that accept input of arbitrary size and produce correspondingly-sized output, which is crucial for adapting classification networks for dense prediction tasks like segmentation.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_7 = {
    'question': (
        'According to the paper "Fully Convolutional Networks for Semantic Segmentation," how does the skip architecture in fully convolutional networks enhance segmentation accuracy?'
    ),
    'options_list': [
        'A) By increasing the number of convolutional layers',
        'B) By using only shallow layers for predictions',
        'C) By combining semantic information from deep, coarse layers with appearance information from shallow, fine layers',
        'D) By introducing random field regularization in the network'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The skip architecture enhances segmentation accuracy by fusing the semantic information from deep, coarse layers with the appearance information from shallow, fine layers, producing more accurate segmentation results.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_8 = {
    'question': (
        'What is the primary purpose of converting the fully connected layers of classification networks into convolutional layers, as discussed in the paper "Fully Convolutional Networks for Semantic Segmentation"?'
    ),
    'options_list': [
        'A) To maintain translation invariance across the network',
        'B) To allow the network to handle only fixed-size inputs',
        'C) To produce spatial output maps for dense prediction tasks',
        'D) To minimize the number of parameters in the network'
    ],
    'correct_answer': 'C',
    'explanation': (
        'By converting fully connected layers into convolutional layers, the network can produce spatial output maps, making it suitable for dense prediction tasks such as segmentation.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_9 = {
    'question': (
        'The paper "Fully Convolutional Networks for Semantic Segmentation" mentions the "Shift-and-stitch" method. What is the main limitation of this approach for dense prediction?'
    ),
    'options_list': [
        'A) It decreases the network\'s receptive field size',
        'B) It introduces random noise into the prediction process',
        'C) It significantly increases computational cost due to the need to process multiple shifted inputs',
        'D) It fails to align different layers in the network'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The "Shift-and-stitch" method increases computational cost as it requires the network to process multiple shifted inputs, making it less efficient for dense prediction tasks.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_10 = {
    'question': (
        'In the experiments described in the paper "Fully Convolutional Networks for Semantic Segmentation," which of the following approaches yielded the highest accuracy for the NYUDv2 dataset?'
    ),
    'options_list': [
        'A) Using only RGB images',
        'B) Using only depth (HHA encoding)',
        'C) Early fusion of RGB-D input',
        'D) Late fusion of RGB and HHA predictions'
    ],
    'correct_answer': 'D',
    'explanation': (
        'The authors found that late fusion of RGB and HHA predictions provided the highest accuracy for the NYUDv2 dataset, as it effectively combines complementary information from both modalities.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_11 = {
    'question': (
        'True or False: According to the paper "Fully Convolutional Networks for Semantic Segmentation," the fully convolutional network (FCN) used in the experiments is trained end-to-end, from pixels-to-pixels, without requiring additional machinery like superpixels or proposals.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The FCN is trained end-to-end, directly mapping pixels to pixels for segmentation, eliminating the need for additional steps like superpixels or proposals.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_12 = {
    'question': (
        'True or False: In the paper "Fully Convolutional Networks for Semantic Segmentation," the authors found that training from scratch on segmentation data was more effective than fine-tuning pre-trained classification networks.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The authors discovered that fine-tuning pre-trained classification networks on segmentation data resulted in better performance compared to training from scratch.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_13 = {
    'question': (
        'True or False: The paper "Fully Convolutional Networks for Semantic Segmentation" demonstrates that using a "skip" architecture allows the network to refine the spatial precision of its segmentation output by fusing outputs from different layers.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'By incorporating skip connections, the network can combine information from both deep and shallow layers, refining the spatial precision of its segmentation output.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_14 = {
    'question': (
        'True or False: The authors of "Fully Convolutional Networks for Semantic Segmentation" claim that the main advantage of the "dilation trick" in convolutional networks is that it allows the network to access information at finer scales than the original design.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The "dilation trick" is used to densify the output without reducing the receptive field size, but it does not enable the network to access finer-scale information.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}

question_15 = {
    'question': (
        'True or False: In the paper "Fully Convolutional Networks for Semantic Segmentation," the authors found that their fully convolutional network (FCN) significantly improved the state-of-the-art performance on the PASCAL VOC segmentation challenge, outperforming the previous best results.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The FCN significantly outperformed the previous best results on the PASCAL VOC segmentation challenge, marking a notable advancement in semantic segmentation performance.'
    ),
    'chapter_information': 'Perplexity FCN Paper'
}



question_GTISN_1 = {
    'question': (
        'In the transcript, why are fully connected layers considered unsuitable for segmentation tasks?'
    ),
    'options_list': [
        'A) They require a fixed input size.',
        'B) They throw away spatial information, resulting in outputs that are not spatially organized.',
        'C) They introduce too many parameters into the network.',
        'D) They are unable to handle multiple channels in an image.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Fully connected layers do not preserve the spatial structure of the input, resulting in outputs that lose spatial organization, which is essential for segmentation tasks.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_2 = {
    'question': (
        'What is the main advantage of converting fully connected layers into convolutional layers for segmentation, as described in the transcript?'
    ),
    'options_list': [
        'A) It reduces the computational cost of the network.',
        'B) It allows the network to handle arbitrary input sizes and produce spatially-aware outputs.',
        'C) It increases the depth of the network, enabling extraction of higher-level features.',
        'D) It enables the network to use max pooling more effectively.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'By converting fully connected layers to convolutional layers, the network can accept inputs of varying sizes and maintain spatial information throughout the network, which is crucial for producing accurate segmentation maps.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_3 = {
    'question': (
        'According to the transcript, what is the main role of the "encoder" in an encoder-decoder architecture?'
    ),
    'options_list': [
        'A) To upsample the input image to a higher resolution.',
        'B) To downsample the input image, extracting highly relevant abstract features.',
        'C) To convert feature maps into bounding boxes for object detection.',
        'D) To combine information from different layers for segmentation.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The encoder’s primary function is to progressively downsample the input image, extracting abstract and meaningful features that can later be used by the decoder for generating segmentation maps.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_4 = {
    'question': (
        'The transcript discusses a "transpose convolution" (also known as a deconvolution). What is a key difference between a standard convolution and a transpose convolution?'
    ),
    'options_list': [
        'A) Standard convolutions reduce the input size, while transpose convolutions expand the input size.',
        'B) Standard convolutions use max pooling, while transpose convolutions use average pooling.',
        'C) Transpose convolutions always result in fixed-size outputs.',
        'D) Transpose convolutions only operate on grayscale images.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Transpose convolutions are used to expand the spatial dimensions of the input, effectively reversing the spatial reduction caused by standard convolutions in the encoder part of the network.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_5 = {
    'question': (
        'When applying the concept of "max unpooling," how does the network decide where to place the values in the larger output, according to the transcript?'
    ),
    'options_list': [
        'A) By averaging the values from the encoder stage.',
        'B) By using a learned set of weights to determine the locations.',
        'C) By using the locations of the maximum elements identified during the pooling operation in the encoder stage.',
        'D) By performing random sampling across the input.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Max unpooling uses the indices of maximum values stored during the pooling operation in the encoder stage to place values in the corresponding locations during the upsampling process.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_6 = {
    'question': (
        'True or False: According to the transcript, one limitation of max unpooling layers is that they contain no learnable parameters and therefore do not "learn" how to upsample the input.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Max unpooling is a fixed operation that uses the indices of maximum values from the pooling stage, and thus does not involve any learnable parameters to guide the upsampling.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_7 = {
    'question': (
        'True or False: The transcript explains that an encoder-decoder network typically uses the exact same learned kernels from the encoder in the decoder, but flipped 180 degrees.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'In some encoder-decoder architectures, the kernels used in the encoder can be reused in the decoder by flipping them, allowing the network to effectively reverse the convolutional operations performed during encoding.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_8 = {
    'question': (
        'True or False: In the transcript, it is stated that the main benefit of converting fully connected layers into convolutional layers is to allow for an increase in the network\'s receptive field size.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The main benefit of converting fully connected layers into convolutional layers is to support arbitrary input sizes and maintain spatial information, not to increase the receptive field size.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_9 = {
    'question': (
        'True or False: According to the transcript, "unit" architectures improve segmentation by incorporating skip connections between corresponding layers in the encoder and decoder, allowing the combination of information at multiple resolutions.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Skip connections in "unit" architectures combine information from deeper layers with shallow layers, improving the network’s ability to make more precise segmentation by leveraging multi-scale features.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTISN_10 = {
    'question': (
        'True or False: The transcript suggests that upsampling can be performed using traditional image processing methods like resizing, but this might result in a lower-resolution segmentation output.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Traditional resizing methods can increase the spatial resolution but may lead to a lower-quality segmentation output, as they do not incorporate learned features from the network for accurate upsampling.'
    ),
    'chapter_information': 'GT Image Segmentation Network'
}

question_GTSSD_1 = {
    'question': (
        'What problem does the multi-headed architecture solve in single-stage object detection as discussed in the transcript?'
    ),
    'options_list': [
        'A) It reduces the computational complexity of the network.',
        'B) It allows simultaneous predictions of class labels and bounding boxes.',
        'C) It optimizes the network for specific object categories.',
        'D) It improves the network\'s ability to handle variable image sizes.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The multi-headed architecture in single-stage object detection allows the network to predict class labels and bounding boxes simultaneously, streamlining the detection process.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_2 = {
    'question': (
        'According to the transcript, what is the purpose of using non-maximum suppression (NMS) in object detection?'
    ),
    'options_list': [
        'A) To predict bounding boxes with the highest probability.',
        'B) To convert fully connected layers into convolutional layers.',
        'C) To combine overlapping bounding boxes with similar predictions into a single bounding box.',
        'D) To refine the bounding box predictions by adjusting their aspect ratios.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Non-maximum suppression (NMS) is used to combine overlapping bounding boxes that have similar predictions, ensuring that each detected object is represented by a single, most confident bounding box.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_3 = {
    'question': (
        'In the context of object detection, what does the "grid" over the input image correspond to, as mentioned in the transcript?'
    ),
    'options_list': [
        'A) Convolutional layers’ stride length',
        'B) Positions in the convolutional feature maps at the last layer',
        'C) The aspect ratio of the bounding boxes',
        'D) The size of the input image itself'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The "grid" corresponds to positions in the convolutional feature maps at the last layer, where predictions are made for object presence and bounding boxes.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_4 = {
    'question': (
        'According to the transcript, what is the primary challenge when designing an object detection model using single-stage methods?'
    ),
    'options_list': [
        'A) Predicting a fixed number of bounding boxes',
        'B) Determining candidate regions of varying positions and scales',
        'C) Handling grayscale images effectively',
        'D) Implementing fully connected layers in the architecture'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The main challenge in single-stage object detection is determining candidate regions that vary in both position and scale, requiring the model to be flexible in its predictions.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_5 = {
    'question': (
        'What is a significant difference between SSD (Single Shot Multibox Detector) and YOLO (You Only Look Once) mentioned in the transcript?'
    ),
    'options_list': [
        'A) YOLO uses a pre-trained convolutional neural network backbone, while SSD does not.',
        'B) SSD estimates bounding boxes for each position in the grid using pre-defined aspect ratios.',
        'C) YOLO imposes a grid only on a single feature map, while SSD uses multiple feature maps.',
        'D) SSD uses a custom architecture that eventually leads to fully connected layers.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'SSD estimates bounding boxes for each position in the grid using pre-defined aspect ratios, allowing for more diverse and accurate object detection.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_6 = {
    'question': (
        'True or False: The transcript mentions that single-stage object detection methods like SSD and YOLO rely on a fixed grid over the input image to predict object locations.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Single-stage object detectors, such as SSD and YOLO, use a fixed grid over the input image to generate predictions for object locations, making the detection process fast and efficient.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_7 = {
    'question': (
        'True or False: According to the transcript, the mean average precision (mAP) metric in object detection is calculated by averaging the intersection over union (IoU) values across different bounding boxes in the image.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The mean average precision (mAP) is calculated by averaging precision across different recall levels for each category, not by averaging IoU values.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_8 = {
    'question': (
        'True or False: The multi-headed architecture described in the transcript allows the convolutional neural network to simultaneously perform classification and regression tasks.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The multi-headed architecture enables the network to perform both classification (predicting object classes) and regression (predicting bounding box coordinates) tasks simultaneously.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_9 = {
    'question': (
        'True or False: Non-maximum suppression (NMS) is a deep learning-based technique used in the regression task of object detection to refine bounding box predictions, according to the transcript.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'Non-maximum suppression (NMS) is a traditional computer vision technique used to filter out overlapping bounding boxes, not a deep learning-based technique.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}

question_GTSSD_10 = {
    'question': (
        'True or False: The transcript states that COCO is a more complex dataset for object detection than ImageNet, primarily because it contains more objects per image and more categories.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'COCO is considered more complex than ImageNet as it features more objects per image and a larger number of categories, making object detection more challenging.'
    ),
    'chapter_information': 'GT Lecture Single Stage Detection'
}


question_TSSD_1 = {
    'question': (
        'According to the transcript, what is the main advantage of using a two-stage object detection method over single-stage methods?'
    ),
    'options_list': [
        'A) It provides faster detection speeds.',
        'B) It decomposes the problem into region proposals and classification, resulting in more accurate detections.',
        'C) It requires fewer hyperparameters to optimize.',
        'D) It allows for variable-sized input images without resizing.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Two-stage object detection methods, like Faster R-CNN, first generate region proposals and then classify them, leading to more accurate detections compared to single-stage methods.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_2 = {
    'question': (
        'Why is ROI (Region of Interest) Pooling necessary in two-stage object detection methods, as discussed in the transcript?'
    ),
    'options_list': [
        'A) To reduce the computational cost of feature extraction.',
        'B) To handle the different sizes of regions of interest by equalizing them into a fixed-size grid for fully connected layers.',
        'C) To increase the receptive field size for bounding box predictions.',
        'D) To provide more accurate class labels for overlapping objects.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'ROI Pooling is used to equalize the size of various regions of interest, ensuring they can be fed into the fully connected layers for classification, regardless of their original sizes.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_3 = {
    'question': (
        'The transcript mentions the use of a Region Proposal Network (RPN) in Faster R-CNN. What is the purpose of the RPN?'
    ),
    'options_list': [
        'A) To classify objects based on their bounding box coordinates.',
        'B) To generate a fixed grid of bounding boxes over the entire image.',
        'C) To estimate potential bounding boxes and objectness scores from the feature maps.',
        'D) To perform segmentation within each bounding box.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The RPN in Faster R-CNN generates potential bounding boxes (region proposals) and assigns objectness scores to them, streamlining the process of identifying regions that may contain objects.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_4 = {
    'question': (
        'What is a major drawback of using traditional non-learning-based algorithms for region proposals in object detection, as explained in the transcript?'
    ),
    'options_list': [
        'A) They are difficult to implement in neural networks.',
        'B) They are slow and generate many redundant bounding boxes, often including background areas.',
        'C) They cannot detect small objects in an image.',
        'D) They require extensive training data for accurate region proposals.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Traditional non-learning-based algorithms for region proposals tend to be slow and often generate many redundant bounding boxes, including those that encompass background areas, leading to inefficiency.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_5 = {
    'question': (
        'According to the transcript, how does Faster R-CNN differ from Fast R-CNN in terms of the region proposal process?'
    ),
    'options_list': [
        'A) Faster R-CNN replaces non-learning-based region proposals with a learned Region Proposal Network (RPN).',
        'B) Faster R-CNN uses a custom convolutional architecture, while Fast R-CNN uses pre-trained networks.',
        'C) Fast R-CNN does not perform bounding box regression, while Faster R-CNN does.',
        'D) Faster R-CNN removes the need for ROI pooling.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Faster R-CNN introduces a learned Region Proposal Network (RPN) to replace traditional non-learning-based region proposals, enhancing the efficiency and accuracy of region detection.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_6 = {
    'question': (
        'True or False: The transcript describes how ROI Pooling in two-stage object detection is used to equalize the size of regions of interest before feeding them into fully connected layers.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'ROI Pooling converts regions of interest into a fixed size, allowing them to be processed by the fully connected layers for classification and bounding box regression.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_7 = {
    'question': (
        'True or False: According to the transcript, one of the main benefits of the Region Proposal Network (RPN) in Faster R-CNN is that it can predict an arbitrary number of bounding boxes.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The RPN in Faster R-CNN uses a fixed grid with anchor boxes of various sizes to predict potential bounding boxes, rather than an arbitrary number.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_8 = {
    'question': (
        'True or False: The transcript states that the complexity of two-stage object detection methods like Faster R-CNN includes managing at least four different loss functions during training.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Faster R-CNN manages multiple loss functions, including those for object classification, bounding box regression, region proposals, and objectness scores, contributing to its complexity.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_9 = {
    'question': (
        'True or False: The transcript suggests that two-stage object detection methods, such as Faster R-CNN, are generally faster than single-stage methods like YOLO or SSD.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'Two-stage methods are typically slower due to the additional region proposal step, but they tend to be more accurate than single-stage methods like YOLO or SSD.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_TSSD_10 = {
    'question': (
        'True or False: In the transcript, the term "Mask R-CNN" refers to an extension of Faster R-CNN that includes an additional mask prediction for segmentation within each region of interest.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Mask R-CNN extends Faster R-CNN by adding a branch for predicting segmentation masks within each region of interest, providing both object detection and instance segmentation capabilities.'
    ),
    'chapter_information': 'GT Lecture Two Stage Detection'
}

question_UML15_1 = {
    'question': (
        'Which of the following best explains why the naive sliding window approach is computationally infeasible for object detection in high-resolution images?'
    ),
    'options_list': [
        'A) Because convolutional neural networks cannot process non-square images efficiently.',
        'B) Because the number of possible bounding boxes in an image scales exponentially with the image resolution.',
        'C) Because sliding window methods require evaluating the CNN on every possible region, leading to an impractical number of computations.',
        'D) Because sliding window methods cannot detect objects of varying sizes.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'In the sliding window approach, the CNN classifier is applied to every possible sub-window in the image. High-resolution images contain an enormous number of possible windows (on the order of tens of millions), making it computationally infeasible to process each one.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_2 = {
    'question': (
        'In the R-CNN method, the convolutional neural network is applied independently to each region proposal generated by selective search.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'R-CNN processes each region proposal independently. After generating region proposals using selective search, each proposal is warped to a fixed size and passed individually through the CNN, resulting in computationally expensive processing.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_3 = {
    'question': (
        'What is the primary advantage of Fast R-CNN over R-CNN in object detection?'
    ),
    'options_list': [
        'A) Fast R-CNN uses a different backbone network that is more efficient.',
        'B) Fast R-CNN eliminates the need for region proposals.',
        'C) Fast R-CNN shares computation by applying the CNN to the entire image first, then extracting features for each region proposal.',
        'D) Fast R-CNN uses a more advanced non-max suppression algorithm.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Fast R-CNN processes the entire image with a CNN to generate a shared feature map. Region proposals are then projected onto this feature map, significantly reducing computation by sharing it across all proposals.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_4 = {
    'question': (
        'Non-Max Suppression is used in object detection to combine multiple overlapping detections of the same object into a single detection.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Non-Max Suppression (NMS) is a post-processing step that reduces redundant detections by eliminating overlapping bounding boxes that likely correspond to the same object, keeping only the one with the highest confidence score.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_5 = {
    'question': (
        'In object detection, the Intersection over Union (IoU) metric is used for:'
    ),
    'options_list': [
        'A) Comparing two bounding boxes to determine their similarity.',
        'B) Evaluating the precision and recall of the detector.',
        'C) Calculating the number of objects detected in an image.',
        'D) Adjusting the learning rate during training.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'IoU is a metric that quantifies the overlap between two bounding boxes. It is calculated as the area of the intersection divided by the area of the union, used to assess the accuracy of predicted bounding boxes against ground truth.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_6 = {
    'question': (
        'Which of the following statements about mean Average Precision (mAP) in object detection is FALSE?'
    ),
    'options_list': [
        'A) mAP is computed by averaging the average precision across all object categories.',
        'B) mAP takes into account both the precision and recall of the detector.',
        'C) mAP is computed using the IoU threshold of 0.5 only.',
        'D) mAP provides a single performance metric summarizing the detector\'s accuracy.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Statement C is false. mAP is often computed at multiple IoU thresholds (e.g., 0.5, 0.75) to evaluate the detector\'s performance at different levels of localization accuracy, providing a comprehensive assessment.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_7 = {
    'question': (
        'In Faster R-CNN, the Region Proposal Network (RPN) is trained to generate region proposals and is separate from the backbone CNN.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'In Faster R-CNN, the RPN is not separate; it shares the convolutional layers with the backbone network. The RPN operates on the shared feature maps, making the process efficient by reusing computations.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_8 = {
    'question': (
        'Which of the following best describes the role of anchors in the Region Proposal Network (RPN) of Faster R-CNN?'
    ),
    'options_list': [
        'A) They are predefined bounding boxes of different sizes and aspect ratios used as references for proposals.',
        'B) They are points in the image where the network predicts the existence of keypoints.',
        'C) They are initializations for the network\'s weights.',
        'D) They are labels used to train the network to classify background regions.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Anchors are predefined bounding boxes with various sizes and aspect ratios placed uniformly across the image. The RPN predicts adjustments (bounding box regressions) and objectness scores for these anchors to generate final region proposals.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_9 = {
    'question': (
        'Single-stage object detectors, such as SSD (Single Shot MultiBox Detector), typically offer higher accuracy than two-stage detectors like Faster R-CNN.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'Single-stage detectors prioritize speed by eliminating the second stage of processing region proposals, often at the cost of accuracy. Two-stage detectors like Faster R-CNN generally achieve higher accuracy.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}

question_UML15_10 = {
    'question': (
        'Why is a multi-task loss function used in object detection models like Faster R-CNN?'
    ),
    'options_list': [
        'A) To balance the learning rate of different layers in the network.',
        'B) Because the model simultaneously predicts both object categories and bounding box coordinates.',
        'C) To regularize the network and prevent overfitting.',
        'D) To enable the network to detect objects at multiple scales.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Object detection models perform both classification (object categories) and regression (bounding box coordinates). A multi-task loss function combines these objectives, allowing the network to learn both tasks simultaneously.'
    ),
    'chapter_information': 'U Mich Lesson 15'
}


question_UML16_1 = {
    'question': (
        'What is the main difference between image classification and object detection?'
    ),
    'options_list': [
        'A) Object detection uses convolutional neural networks',
        'B) Object detection outputs multiple objects per image',
        'C) Object detection requires higher resolution images',
        'D) Both B and C'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Object detection involves identifying and localizing multiple objects within an image, which often requires higher resolution for accurate detection. This makes it more complex than image classification, which deals with a single object label per image.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_2 = {
    'question': (
        'In object detection, bounding boxes are typically parameterized using 4 numbers representing the center coordinates, width, and height.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Bounding boxes in object detection are parameterized by four values: the x and y coordinates of the center, along with the width and height, allowing for flexible localization of objects.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_3 = {
    'question': (
        'Which of the following is NOT a challenge specific to object detection compared to image classification?'
    ),
    'options_list': [
        'A) Outputting variable numbers of objects per image',
        'B) Processing higher resolution images',
        'C) Dealing with both classification and localization tasks',
        'D) Using softmax loss for training'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Using softmax loss is common in both image classification and object detection tasks. The challenges specific to object detection involve handling variable object numbers, high-resolution images, and the dual tasks of classification and localization.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_4 = {
    'question': (
        'The R-CNN (Region-based Convolutional Neural Network) method uses selective search to generate region proposals.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'R-CNN relies on selective search, a traditional computer vision technique, to generate region proposals that are then processed by a CNN for classification and bounding box regression.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_5 = {
    'question': (
        'What is the purpose of non-maximum suppression (NMS) in object detection?'
    ),
    'options_list': [
        'A) To generate region proposals',
        'B) To eliminate overlapping detections',
        'C) To compute intersection over union',
        'D) To train the neural network'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Non-maximum suppression (NMS) is used to eliminate multiple overlapping detections of the same object, ensuring that only the most confident detection is kept.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_6 = {
    'question': (
        'Intersection over Union (IoU) is a metric used to compare the similarity between two bounding boxes, with values ranging from 0 to 1.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'IoU measures the overlap between the predicted bounding box and the ground truth box. It is calculated as the area of the intersection divided by the area of the union, resulting in a value between 0 and 1.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_7 = {
    'question': (
        'Which of the following is NOT a component of the R-CNN architecture?'
    ),
    'options_list': [
        'A) Region proposal network',
        'B) Selective search',
        'C) CNN for feature extraction',
        'D) Bounding box regression'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The Region Proposal Network (RPN) is a component of Faster R-CNN, not the original R-CNN. R-CNN uses selective search to generate region proposals.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_8 = {
    'question': (
        'During the training of R-CNN models, how are region proposals labeled?'
    ),
    'options_list': [
        'A) Based on their color histograms.',
        'B) As positive, negative, or neutral depending on their Intersection over Union (IoU) with ground truth boxes.',
        'C) All region proposals are considered positive examples.',
        'D) Only the top 100 region proposals are used for training.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Region proposals are labeled as positive, negative, or neutral based on their IoU with ground truth boxes. High IoU proposals are labeled positive, low IoU ones as negative, and intermediate ones as neutral.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_9 = {
    'question': (
        'In Fast R-CNN, the ROI Pooling operation allows gradients to be backpropagated into both the image features and the bounding box coordinates.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'ROI Pooling snaps the region proposals onto the feature map grid, which introduces misalignment and prevents gradients from flowing back into the bounding box coordinates.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}

question_UML16_10 = {
    'question': (
        'What is the main advantage of ROI Align over ROI Pooling in object detection networks?'
    ),
    'options_list': [
        'A) ROI Align reduces computational complexity by skipping certain regions.',
        'B) ROI Align eliminates the need for region proposals.',
        'C) ROI Align removes the snapping step, preserving spatial alignment and allowing gradients to flow into bounding box coordinates.',
        'D) ROI Align uses max pooling to better capture features.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'ROI Align uses bilinear interpolation to sample the exact fractional locations, preserving spatial alignment and allowing gradients to flow back into both the image features and the bounding box coordinates.'
    ),
    'chapter_information': 'U Mich Lesson 16'
}


# Multiple Choice Questions
gt7_question_1 = {
    'question': 'What does computing the gradient of the loss with respect to the input image allow us to understand?',
    'options_list': [
        'a) How small changes in the input image affect the loss, highlighting important pixels.',
        'b) How the weights of the neural network change during training.',
        'c) The exact activation values of the deepest layer in the network.',
        'd) The performance of the network on unseen data.'
    ],
    'correct_answer': 'a) How small changes in the input image affect the loss, highlighting important pixels.',
    'explanation': 'By computing the gradient of the loss with respect to the input, we can see how small perturbations in each pixel affect the loss. This helps identify which pixels are most important for the network\'s decision, allowing us to create saliency maps.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_2 = {
    'question': 'Why do we often compute the gradient of the classifier score (before softmax) with respect to the input, instead of the gradient of the loss?',
    'options_list': [
        'a) To include the effects of the loss function more explicitly.',
        'b) To avoid complexities introduced by the softmax and loss functions, simplifying the gradients.',
        'c) Because the loss function gradients are always zero.',
        'd) To ensure the gradients are always positive.'
    ],
    'correct_answer': 'b) To avoid complexities introduced by the softmax and loss functions, simplifying the gradients.',
    'explanation': 'Computing the gradient of the classifier score (pre-softmax) avoids additional complexities from the softmax and loss functions, which can introduce interactions between classes and affect the gradients.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_3 = {
    'question': 'What is the main purpose of using guided backpropagation in visualization?',
    'options_list': [
        'a) To speed up the training process.',
        'b) To focus on positive influences by zeroing out negative gradients during backpropagation.',
        'c) To change the architecture of the network dynamically.',
        'd) To enhance the resolution of the input image.'
    ],
    'correct_answer': 'b) To focus on positive influences by zeroing out negative gradients during backpropagation.',
    'explanation': 'Guided backpropagation modifies the backpropagation process to only pass positive gradients where both the forward activation and the gradient are positive, enhancing the visualization of features that positively influence the neuron\'s activation.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_4 = {
    'question': 'What is Grad-CAM primarily used for in neural network visualization?',
    'options_list': [
        'a) Increasing the network\'s classification accuracy.',
        'b) Generating class-specific localization maps using gradients from the last convolutional layers.',
        'c) Reducing the computational complexity of the network.',
        'd) Enhancing the color contrast of input images.'
    ],
    'correct_answer': 'b) Generating class-specific localization maps using gradients from the last convolutional layers.',
    'explanation': 'Grad-CAM (Gradient-weighted Class Activation Mapping) uses gradients flowing into the last convolutional layer to produce a coarse localization map highlighting important regions for a specific class.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_5 = {
    'question': 'What is one way to visualize the most highly activating image patches for a specific neuron or filter in a convolutional neural network?',
    'options_list': [
        'a) Randomly sampling patches from the dataset.',
        'b) Identifying and plotting the image patches that cause maximum activation in that neuron.',
        'c) Visualizing the neuron\'s weights directly as an image.',
        'd) Applying a uniform filter across all images.'
    ],
    'correct_answer': 'b) Identifying and plotting the image patches that cause maximum activation in that neuron.',
    'explanation': 'By finding the image patches from the dataset that cause the highest activation in a specific neuron, we can visualize what kind of input features that neuron is most responsive to.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

# True/False Questions
gt7_question_6 = {
    'question': 'Backpropagating the gradient all the way to the input image enables us to create saliency maps that highlight important regions in the image.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'By backpropagating to the input, we obtain gradients that indicate the sensitivity of the loss to each pixel, allowing us to visualize important regions through saliency maps.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_7 = {
    'question': 'In guided backpropagation, gradients are only passed back through neurons that had positive activations during the forward pass and positive gradients during the backward pass.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Guided backpropagation zeroes out gradients where either the forward activation is negative or the gradient itself is negative, emphasizing positive contributions to the neuron\'s activation.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_8 = {
    'question': 'Saliency maps can help reveal biases in the dataset by showing that the network might be focusing on background elements rather than the object itself.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Saliency maps can indicate when a network relies on background features for classification, exposing potential biases in the training data where certain objects frequently appear with specific backgrounds.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_9 = {
    'question': 'In Grad-CAM, the per-channel weights (alphas) are calculated by performing a global average pooling over the spatial dimensions of the gradients.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'The per-channel weights in Grad-CAM are computed by averaging the gradients of the classifier score with respect to each feature map over all spatial locations, emphasizing channels that contribute most to the class prediction.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_question_10 = {
    'question': 'Computing the gradient of any layer\'s activation with respect to the input image helps us understand how changes in the input affect that specific layer.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'By computing these gradients, we can see how perturbations in the input influence the activations of a particular layer, providing insights into the network\'s hierarchical feature processing.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

# Multiple Choice Questions
gt7_vis_question_1 = {
    'question': 'What is the key idea behind optimizing the input image using gradients in neural networks?',
    'options_list': [
        'a) To increase the network\'s training speed by modifying the input data.',
        'b) To generate images that maximize the activation of certain neurons or class scores by performing gradient ascent on the input image.',
        'c) To reduce overfitting by altering the input images.',
        'd) To create more realistic images by applying random noise.'
    ],
    'correct_answer': 'b) To generate images that maximize the activation of certain neurons or class scores by performing gradient ascent on the input image.',
    'explanation': 'By computing the gradient of the score with respect to the input image, we can perform gradient ascent to modify the image in a way that increases the activation of specific neurons or class scores. This allows us to generate images that the network strongly associates with certain features or classes.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_2 = {
    'question': 'When optimizing an image to maximize the score of a particular class, why is regularization often necessary?',
    'options_list': [
        'a) To ensure the image remains within valid pixel value ranges.',
        'b) To speed up the convergence of the optimization process.',
        'c) To prevent the image from becoming too similar to other classes.',
        'd) To avoid extreme pixel values and encourage smoother images.'
    ],
    'correct_answer': 'd) To avoid extreme pixel values and encourage smoother images.',
    'explanation': 'Regularization terms, such as preferring smaller pixel values or applying Gaussian blurring, help prevent the optimization from producing images with extreme pixel values or high-frequency noise, resulting in smoother and more interpretable images.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_3 = {
    'question': 'What is an adversarial example in the context of neural networks?',
    'options_list': [
        'a) An image generated to minimize the loss function.',
        'b) An input intentionally perturbed to cause the network to make a wrong prediction.',
        'c) A data sample used to train the network for better performance.',
        'd) An example that the network classifies correctly with high confidence.'
    ],
    'correct_answer': 'b) An input intentionally perturbed to cause the network to make a wrong prediction.',
    'explanation': 'An adversarial example is an input that has been slightly modified in a way that causes the neural network to make an incorrect prediction with high confidence, even though the modifications may be imperceptible to humans.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_4 = {
    'question': 'Which of the following is a defense mechanism against adversarial attacks?',
    'options_list': [
        'a) Using smaller networks with fewer parameters.',
        'b) Adding adversarial examples to the training set to improve robustness.',
        'c) Removing activation functions from the network.',
        'd) Increasing the learning rate during training.'
    ],
    'correct_answer': 'b) Adding adversarial examples to the training set to improve robustness.',
    'explanation': 'One defense against adversarial attacks is adversarial training, which involves generating adversarial examples and including them in the training set so that the network learns to be more robust to such perturbations.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_5 = {
    'question': 'What is meant by the term "texture bias" in convolutional neural networks?',
    'options_list': [
        'a) CNNs prefer to classify images based on their color histograms.',
        'b) CNNs rely more heavily on texture information than shape when classifying images.',
        'c) CNNs ignore texture and focus solely on shapes.',
        'd) CNNs are biased towards images with higher resolution textures.'
    ],
    'correct_answer': 'b) CNNs rely more heavily on texture information than shape when classifying images.',
    'explanation': 'Texture bias refers to the tendency of CNNs to rely more on texture information rather than shape when making classifications, which can lead to misclassifications if textures are misleading.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

# True/False Questions
gt7_vis_question_6 = {
    'question': 'Starting from a random image, we can optimize it using gradient ascent to generate images that the network recognizes as belonging to a specific class.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'By performing gradient ascent on a random image and maximizing the score of a particular class, we can generate images that the network interprets as belonging to that class, revealing the features the network has learned.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_7 = {
    'question': 'It is possible to optimize an image to maximize activations in any layer of the neural network, not just the output layer.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'We can perform gradient ascent on the input image to maximize the activation of neurons in any layer of the network, allowing us to visualize the features represented by different layers.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_8 = {
    'question': 'Adversarial attacks are only effective against deep learning models and not against other machine learning methods.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'Adversarial attacks are not specific to deep learning models; other machine learning methods can also be susceptible to such attacks, including linear models.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_9 = {
    'question': 'Humans tend to have a shape bias, focusing more on the shape of objects than their texture when recognizing them.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Human perception is generally more influenced by the shape of objects rather than their texture, which is opposite to the texture bias observed in CNNs.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}

gt7_vis_question_10 = {
    'question': 'Testing the robustness of neural networks to perturbations can help us understand and improve their reliability in real-world applications.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'By evaluating how networks respond to various perturbations, we can identify vulnerabilities and work towards making them more reliable and robust for practical use.',
    'chapter_information': 'GT Lecture 7 - Visualization of Neural Network'
}


# Multiple Choice Questions
gt7_style_transfer_question_1 = {
    'question': 'What is the primary objective of style transfer in neural networks?',
    'options_list': [
        'a) To classify images into different categories.',
        'b) To generate images that combine the content of one image with the style of another.',
        'c) To enhance the resolution of low-quality images.',
        'd) To detect objects within an image.'
    ],
    'correct_answer': 'b) To generate images that combine the content of one image with the style of another.',
    'explanation': 'Style transfer aims to create a new image that preserves the content (structures and objects) of a content image while adopting the style (textures, colors, and patterns) of a style image.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_2 = {
    'question': 'In style transfer, we optimize a generated image by matching its features to those of the content image using a loss function.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'We use a loss function to minimize the difference between the features of the generated image and the content image, ensuring the generated image retains the original content.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_3 = {
    'question': 'Which method is used to represent the style of an image in style transfer?',
    'options_list': [
        'a) Using the raw pixel values of the image.',
        'b) Matching the histogram of gradients.',
        'c) Computing the Gram matrix of feature maps to capture feature correlations.',
        'd) Applying edge detection algorithms.'
    ],
    'correct_answer': 'c) Computing the Gram matrix of feature maps to capture feature correlations.',
    'explanation': 'The Gram matrix is computed from the feature maps of a neural network layer and represents the correlations between different feature channels, effectively capturing the style (textures and patterns) of the image.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_4 = {
    'question': 'The content loss in style transfer is computed by comparing the Gram matrices of the content image and the generated image.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'The content loss is computed by directly comparing the feature maps (activations) of the content image and the generated image, not the Gram matrices. The Gram matrices are used for style loss.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_5 = {
    'question': 'In the context of style transfer, what does the Gram matrix represent?',
    'options_list': [
        'a) The spatial arrangement of pixels in the image.',
        'b) The total variation loss of the image.',
        'c) The correlations between different feature channels in a layer.',
        'd) The distribution of color intensities in the image.'
    ],
    'correct_answer': 'c) The correlations between different feature channels in a layer.',
    'explanation': 'The Gram matrix captures the correlations between feature maps (channels) at a particular layer, summarizing how different features interact, which is useful for representing style.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_6 = {
    'question': 'During style transfer, we use gradient descent to update the weights of the neural network.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'In style transfer, we keep the neural network weights fixed and use gradient descent to optimize the generated image itself by updating its pixel values.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_7 = {
    'question': 'Why do we often use multiple layers of the neural network when computing style loss?',
    'options_list': [
        'a) To capture both low-level and high-level style features across the network.',
        'b) To reduce computational complexity.',
        'c) Because single-layer representations are sufficient.',
        'd) To avoid overfitting the generated image to the style image.'
    ],
    'correct_answer': 'a) To capture both low-level and high-level style features across the network.',
    'explanation': 'Using multiple layers allows us to capture style features at different levels of abstraction, from textures and colors (shallow layers) to more complex patterns (deeper layers).',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_8 = {
    'question': 'The style loss encourages the generated image to have similar feature correlations as the style image, without necessarily matching the exact spatial arrangement.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'By matching the Gram matrices, we focus on the overall texture and patterns (style) rather than the precise spatial arrangement, which allows the generated image to maintain the content from the content image.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_9 = {
    'question': 'What role does the weighting between content loss and style loss play in style transfer?',
    'options_list': [
        'a) It balances the contribution of content and style in the final image.',
        'b) It speeds up the convergence of the optimization process.',
        'c) It determines the resolution of the generated image.',
        'd) It controls the color palette used in the image.'
    ],
    'correct_answer': 'a) It balances the contribution of content and style in the final image.',
    'explanation': 'Adjusting the weights between content loss and style loss allows us to control how much the content and style influence the generated image. Higher content weight preserves more content details, while higher style weight emphasizes stylistic features.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_10 = {
    'question': 'Style transfer can be used as a form of data augmentation to improve a neural network\'s robustness to variations in style and texture.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'By adding stylized images to the training set, we can expose the neural network to a wider range of styles and textures, enhancing its ability to generalize and be robust to such variations.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

# True/False and Multiple Choice Questions (11-20)
gt7_style_transfer_question_11 = {
    'question': 'Which of the following best describes the process of computing the style loss using Gram matrices?',
    'options_list': [
        'a) Comparing the raw pixel values of the style image and the generated image.',
        'b) Matching the high-level semantic content between the style image and the generated image.',
        'c) Measuring the difference between the Gram matrices of the style image and the generated image across selected layers.',
        'd) Calculating the total variation in pixel intensities.'
    ],
    'correct_answer': 'c) Measuring the difference between the Gram matrices of the style image and the generated image across selected layers.',
    'explanation': 'Style loss is calculated by comparing the Gram matrices of the style image and the generated image, which capture the style information through feature correlations at different layers.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_12 = {
    'question': 'Gram matrices are computed by taking the element-wise product of feature maps and summing over all spatial locations.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'The Gram matrix is calculated by performing an element-wise multiplication of pairs of feature maps (channels) and summing over the spatial dimensions, resulting in a matrix representing feature correlations.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_13 = {
    'question': 'In style transfer, why is it important to remove most of the spatial information when capturing the style?',
    'options_list': [
        'a) To reduce the computational load during optimization.',
        'b) Because style is defined by the exact spatial arrangement of features.',
        'c) To focus on textures and patterns rather than specific shapes and structures.',
        'd) To prevent the generated image from matching the content of the style image.'
    ],
    'correct_answer': 'c) To focus on textures and patterns rather than specific shapes and structures.',
    'explanation': 'By removing spatial information, we emphasize textures and patterns (style) without replicating the specific shapes and arrangements, allowing the content from the content image to be preserved.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_14 = {
    'question': 'The optimization process in style transfer adjusts the neural network\'s weights to minimize the loss.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'The neural network\'s weights remain fixed during style transfer. The optimization adjusts the pixel values of the generated image to minimize the combined content and style losses.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_15 = {
    'question': 'Which of the following is a correct statement about the content loss in style transfer?',
    'options_list': [
        'a) It measures the difference between the Gram matrices of the content and generated images.',
        'b) It compares the feature activations of the content and generated images at selected layers.',
        'c) It evaluates the difference in pixel intensities between the content and generated images.',
        'd) It computes the total variation loss to enforce smoothness.'
    ],
    'correct_answer': 'b) It compares the feature activations of the content and generated images at selected layers.',
    'explanation': 'Content loss is calculated by comparing the feature activations (outputs of selected layers) of the content image and the generated image, ensuring the generated image retains the original content\'s structures.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_16 = {
    'question': 'Style transfer demonstrates the power of neural networks to manipulate and generate images using backpropagation and gradient-based optimization.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Style transfer leverages neural networks\' ability to compute gradients through backpropagation, allowing us to optimize images directly and generate new, stylized content.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_17 = {
    'question': 'What is one practical application of style transfer mentioned in the lecture?',
    'options_list': [
        'a) Image compression algorithms.',
        'b) Enhancing network robustness through data augmentation.',
        'c) Object detection in real-time video.',
        'd) Training neural networks without labeled data.'
    ],
    'correct_answer': 'b) Enhancing network robustness through data augmentation.',
    'explanation': 'Stylized images generated through style transfer can be used as data augmentation to improve a neural network\'s robustness to variations in style and texture.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_18 = {
    'question': 'The Gram matrix used in style transfer is always of size 64x64, corresponding to the number of kernels in the layer.',
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'explanation': 'The size of the Gram matrix depends on the number of feature maps (channels) in the layer being considered. While an example used 64x64 (for 64 channels), other layers may have different numbers of channels.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_19 = {
    'question': 'Which of the following best explains why we can sum the losses from multiple layers during style transfer?',
    'options_list': [
        'a) Because losses from different layers do not interact with each other.',
        'b) Because in a computation graph, multiple backward paths to the same node result in summing the gradients.',
        'c) Because it speeds up the optimization process.',
        'd) Because each layer contributes equally to the final image.'
    ],
    'correct_answer': 'b) Because in a computation graph, multiple backward paths to the same node result in summing the gradients.',
    'explanation': 'In backpropagation through a computation graph, when multiple paths lead to the same node, the gradients are summed. This allows us to combine losses from multiple layers effectively.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}

gt7_style_transfer_question_20 = {
    'question': 'Using style transfer, it is possible to generate images that maintain the content of one image while adopting vastly different styles.',
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'explanation': 'Style transfer can produce images that preserve the original content (e.g., objects, structures) while applying different styles (e.g., textures, colors), resulting in visually distinct outputs.',
    'chapter_information': 'GT Lecture 7 - Style Transfer'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_9_MPC = KC_MPC_QUESTIONS[:-1]
