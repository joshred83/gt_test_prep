question_Efficient_Word_Representations_1_1 = {
    'question': (
        'True or False: The use of distributed word representations ensures that words with similar meanings are always mapped close to each other in the vector space.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'While distributed word representations often map similar words close to each other, it\'s not guaranteed. Factors like training data biases, context diversity, and model limitations can affect how words are positioned in the vector space.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 1&2'
}

question_Efficient_Word_Representations_1_3 = {
    'question': (
        'True or False: The accuracy of word vectors, as measured by syntactic and semantic similarity tasks, is directly proportional to the size of the vocabulary.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'While a larger vocabulary can provide more information, accuracy depends on multiple factors, including training data quality, model architecture, and dimensionality. Vocabulary size alone does not guarantee better accuracy.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 1&2'
}

question_Efficient_Word_Representations_1_6 = {
    'question': (
        'Which of the following is not a primary goal of the proposed novel model architectures in the paper Efficient Estimation of Word Representations in Vector Space?'
    ),
    'options_list': [
        'A) Reducing computational cost while improving accuracy of word vector representations.',
        'B) Optimizing for specific in-domain datasets like speech recognition corpora.',
        'C) Learning syntactic and semantic regularities with high accuracy.',
        'D) Preserving linear regularities among words.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The paper focuses on general large-scale datasets, aiming for improved computational efficiency and accuracy, not specifically optimizing for in-domain datasets.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 1&2'
}

question_Efficient_Word_Representations_1_8 = {
    'question': (
        'In the Neural Network Language Model (NNLM) discussed, which factor primarily contributes to its computational complexity?'
    ),
    'options_list': [
        'A) The size of the output layer.',
        'B) The dimensionality of the input and output layers.',
        'C) The hierarchical softmax implementation.',
        'D) The number of epochs required for training.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The computational complexity of the NNLM is largely due to operations involving high-dimensional input and output layers, particularly in the projection and hidden layers.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 1&2'
}

question_Efficient_Word_Representations_1_9 = {
    'question': (
        'True or False: The NNLM architecture requires evaluating outputs for all vocabulary words in every step, leading to high computational complexity.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Without optimization techniques like hierarchical softmax, the NNLM must compute probabilities for every word in the vocabulary at each training step, which is computationally intensive.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 1&2'
}

question_Efficient_Word_Representations_1_10 = {
    'question': (
        'Which of the following accurately describes how Huffman trees reduce computational cost in the NNLM?'
    ),
    'options_list': [
        'A) They reduce the number of input words needed for training.',
        'B) They reduce the number of vocabulary units that need evaluation during output prediction.',
        'C) They help encode words into distributed vectors of lower dimensionality.',
        'D) They eliminate the need for backpropagation in training.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Huffman trees assign shorter codes to frequent words, reducing the number of computations required during the softmax operation in output prediction.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 1&2'
}

question_Efficient_Word_Representations_1_11 = {
    'question': (
        'The hierarchical softmax technique is used to reduce computational complexity in word prediction. What assumption underlies the use of hierarchical softmax in the models?'
    ),
    'options_list': [
        'A) Words appear with uniform frequency across the dataset.',
        'B) Frequent words require more computational resources than infrequent words.',
        'C) Words are represented in binary trees based on their frequency.',
        'D) All words must be evaluated to predict the next word.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Hierarchical softmax organizes words in a binary tree, often using word frequencies to structure the tree, reducing the computational cost of calculating the softmax over large vocabularies.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 1&2'
}

question_Efficient_Word_Representations_3_1 = {
    'question': (
        'Which of the following statements is the most accurate description of the Continuous Bag-of-Words (CBOW) model?'
    ),
    'options_list': [
        'A) CBOW predicts the current word based solely on future words by averaging all context vectors.',
        'B) CBOW uses all word vectors in the training set to classify the middle word by projecting them into the same position.',
        'C) The projection matrix in CBOW is not learned during training, as all words are projected into the same position regardless of context.',
        'D) CBOW relies on a non-linear projection layer to minimize computational complexity by reducing dimensionality.',
        'E) CBOW is simpler than traditional neural networks because it removes the non-linear hidden layer, projecting context words into the same position.'
    ],
    'correct_answer': 'E',
    'explanation': (
        'Option E is correct because the CBOW model simplifies the architecture by removing the non-linear hidden layer and projecting all context words into the same position in the projection layer. This results in an averaged context vector used to predict the target word.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_2 = {
    'question': (
        'Which of the following best explains why the Skip-gram model is considered more computationally complex than the CBOW model?'
    ),
    'options_list': [
        'A) Skip-gram uses R words from the future and the past for predictions, leading to 2×R outputs.',
        'B) The computational complexity increases because Skip-gram uses more context words than CBOW.',
        'C) Skip-gram predicts multiple surrounding words from a given input word, including distant words, which increases computational cost due to additional sampling.',
        'D) Skip-gram requires a non-linear classifier in every layer, unlike CBOW.',
        'E) Skip-gram and CBOW both require projecting words, but Skip-gram does not use context in predictions.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C is correct because the Skip-gram model aims to predict multiple surrounding context words for each target word, including distant ones, which increases computational complexity due to the need for additional computations and sampling.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_3 = {
    'question': (
        'True or False: In the CBOW model, all context word vectors are averaged, making their individual contributions indistinguishable in predicting the current word.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'In the CBOW model, the vectors of all context words are averaged (or summed) to produce a single context representation. This means that while each word contributes to the prediction, their individual contributions are not separately distinguished; the model relies on the combined information from the context words.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_5 = {
    'question': (
        'Which of the following is true about the training complexity of the Continuous Skip-gram model?'
    ),
    'options_list': [
        'A) The training complexity of Skip-gram is proportional only to the vocabulary size V, as the context does not affect computation.',
        'B) Skip-gram reduces complexity by ignoring distant words, focusing only on the nearest surrounding words.',
        'C) Skip-gram training complexity depends on the number of words sampled from distant contexts, which increases computational cost.',
        'D) Skip-gram and CBOW share the same training complexity formula since both use similar projection techniques.',
        'E) Skip-gram simplifies training by predicting only the immediate next word, lowering complexity to log2(V).'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C is correct because the Skip-gram model includes predictions for multiple context words, including distant ones. The training complexity increases with the number of context words sampled for prediction, which affects computational cost.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_6 = {
    'question': (
        'In the Continuous Bag-of-Words (CBOW) model, what key modification is made compared to the traditional feedforward Neural Network Language Model (NNLM)?'
    ),
    'options_list': [
        'A) The projection layer is no longer shared across all words.',
        'B) The non-linear hidden layer is replaced by a linear projection.',
        'C) Words from the future are not considered in training.',
        'D) The projection layer outputs individual word vectors instead of an averaged representation.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is correct because the CBOW model simplifies the NNLM by removing the non-linear hidden layer and using a linear projection layer shared across all context words, resulting in an averaged context vector.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_8 = {
    'question': (
        'True or False: In the CBOW model, words from both the past and future are considered for predicting the current word.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The CBOW model uses a context window that includes words from both before and after the target word to predict the current word, incorporating information from both past and future context.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_9 = {
    'question': (
        'Which of the following correctly describes the output of the CBOW model?'
    ),
    'options_list': [
        'A) It produces individual word vectors for each word in the context.',
        'B) It averages the projections of all context words into a single vector.',
        'C) It applies a softmax function to each individual context word.',
        'D) It uses a non-linear hidden layer to produce a probability distribution over the vocabulary.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is correct because the CBOW model averages the projected vectors of all context words to form a single context vector used to predict the target word.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_10 = {
    'question': (
        'The training complexity of the CBOW model is given by $Q = N×D + D×Xlog2(V)$. What does D represent in this equation?'
    ),
    'options_list': [
        'A) The dimensionality of the projection layer.',
        'B) The number of words in the vocabulary.',
        'C) The number of training examples.',
        'D) The size of the input context window.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Option A is correct because D represents the dimensionality of the word vectors in the projection layer used during training.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_11 = {
    'question': (
        'True or False: The Skip-gram model uses both past and future words to predict the current word in the center of the context window.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'This statement is false because the Skip-gram model does the opposite; it uses the current word to predict the surrounding context words, not to predict the current word from context.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_3_12 = {
    'question': (
        'What primary factor distinguishes the CBOW model from the Skip-gram model in terms of their output?'
    ),
    'options_list': [
        'A) CBOW predicts the current word based on the context, while Skip-gram predicts context words based on the current word.',
        'B) CBOW uses a non-linear activation function, whereas Skip-gram uses a linear function.',
        'C) CBOW has a larger computational complexity than Skip-gram due to more parameters.',
        'D) CBOW only considers future words in the context, while Skip-gram considers both past and future words.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Option A is correct because the fundamental difference is that CBOW predicts the target word from surrounding context words, whereas Skip-gram predicts the surrounding context words from the target word.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 3'
}

question_Efficient_Word_Representations_4_1 = {
    'question': (
        'Which of the following can be deduced from the results comparing semantic and syntactic accuracy of the models (Tables 2 and 3)?'
    ),
    'options_list': [
        'A) Increasing dimensionality of word vectors beyond 500 leads to consistent improvements in semantic accuracy but has minimal effect on syntactic accuracy.',
        'B) Skip-gram outperforms CBOW in both semantic and syntactic tasks because it incorporates more complex projection matrices.',
        'C) Higher dimensionality and larger training datasets generally improve both semantic and syntactic accuracy, but diminishing returns are observed at higher values.',
        'D) The difference in accuracy between CBOW and Skip-gram models can be attributed solely to the number of epochs trained.',
        'E) The accuracy of the NNLM models remains relatively stable across training sizes, indicating they are less sensitive to data augmentation.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C is correct because the results in Tables 2 and 3 show that increasing the dimensionality of word vectors and using larger training datasets generally improve model accuracy on both semantic and syntactic tasks. However, the rate of improvement decreases at higher dimensionalities, indicating diminishing returns.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 4',
    'image': 'images/wv223.png'
}

question_Efficient_Word_Representations_4_3 = {
    'question': (
        'True or False: The training time of the Skip-gram model increases exponentially with the dimensionality of word vectors and the size of the training set.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'While training time for the Skip-gram model does increase with the dimensionality of word vectors and the size of the training set, it does not increase exponentially. The growth is generally linear or sub-linear due to optimization techniques and approximations used in training, such as negative sampling or hierarchical softmax.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 4'
}

question_Efficient_Word_Representations_4_4 = {
    'question': (
        'In Table 5, why does the Skip-gram model achieve better performance than the CBOW model when trained for three epochs on the same data?'
    ),
    'options_list': [
        'A) Skip-gram predicts surrounding words and captures more context, which leads to better accuracy over time.',
        'B) CBOW is limited by its inability to project future words, which lowers its overall accuracy.',
        'C) Skip-gram\'s architecture inherently allows for more efficient training compared to CBOW, making it faster and more accurate.',
        'D) The training set used for Skip-gram was smaller, allowing it to learn more efficiently.',
        'E) None of the above—CBOW actually outperforms Skip-gram with a better optimization function.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Option A is correct because the Skip-gram model predicts multiple surrounding context words for each target word, allowing it to capture more detailed contextual information over time, which can lead to better performance, especially when trained over multiple epochs.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 4',
    'image': 'images/w2vt6.png'
}

question_Efficient_Word_Representations_4_5 = {
    'question': (
        'Which of the following is the best interpretation of the results shown in Table 4 regarding the effect of vector dimensionality on accuracy?'
    ),
    'options_list': [
        'A) Training models with 600-dimensional word vectors consistently leads to the highest accuracy across both semantic and syntactic tasks, but the improvement slows down after 500 dimensions.',
        'B) Increasing vector dimensionality from 50 to 200 results in better semantic accuracy but worsens syntactic performance.',
        'C) There is no noticeable difference between training with 100-dimensional and 600-dimensional vectors, meaning larger dimensionality only increases computational cost without benefiting accuracy.',
        'D) NNLM models perform better than all other models when using higher-dimensional vectors.',
        'E) Dimensionality plays a minimal role in performance once the training word count exceeds 500 million.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Option A is correct because the results indicate that increasing the vector dimensionality up to 600 dimensions improves accuracy on both tasks. However, the rate of improvement decreases beyond 500 dimensions, showing diminishing returns.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 4',
    'image': 'images/w2vt4.png'
}

question_Efficient_Word_Representations_4_7 = {
    'question': (
        'According to the accuracy comparisons in Table 2, what effect does increasing word vector dimensionality have on accuracy?'
    ),
    'options_list': [
        'A) Accuracy consistently increases for both semantic and syntactic tasks.',
        'B) Syntactic accuracy increases, but semantic accuracy decreases.',
        'C) Accuracy improvement diminishes as dimensionality increases.',
        'D) Accuracy remains the same regardless of dimensionality.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C is correct because the data shows that while increasing dimensionality improves accuracy, the gains become smaller at higher dimensions, indicating diminishing returns on both semantic and syntactic tasks.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 4',
    'image': 'images/wv223.png'
}

question_Efficient_Word_Representations_4_8 = {
    'question': (
        'True or False: The CBOW model generally outperforms the NNLM model in both semantic and syntactic tasks when trained with larger vocabularies.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'According to the results in Tables 3 and 4, the CBOW model achieves higher accuracy than the NNLM on both semantic and syntactic tasks when trained on larger datasets, suggesting that CBOW benefits more from larger training vocabularies.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 4'
}

question_Efficient_Word_Representations_6_1 = {
    'question': (
        'Which of the following most accurately reflects the relationship between the word pairs in Table 8?'
    ),
    'options_list': [
        'A) Word vectors consistently reflect analogical relationships, which is why subtracting vectors always results in a precise and correct new vector.',
        'B) The accuracy of the relationship vectors in Table 8 is determined by syntactic regularities between word pairs.',
        'C) The relationships in Table 8 demonstrate that word vectors trained on large datasets will always achieve 100% accuracy in semantic-syntactic tasks.',
        'D) Word pair relationships, such as "Paris - France + Italy = Rome," demonstrate that vector arithmetic can represent both semantic and geographic relationships, but accuracy is not perfect.',
        'E) All word relationships, such as "Obama - Barack," are equally well captured by the learned vectors because the context of the corpus is broad enough.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Option D is correct because the examples in Table 8 illustrate that vector arithmetic can capture both semantic relationships (e.g., "king - man + woman = queen") and geographic relationships (e.g., "Paris - France + Italy = Rome"). However, the models do not achieve perfect accuracy, and not all relationships are equally well represented.'
    ),
        'image': 'images/w2vt8.png',
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 6'
}

question_Efficient_Word_Representations_6_2 = {
    'question': (
        'What is implied by the examples of vector operations presented in Table 8?'
    ),
    'options_list': [
        'A) Vector operations can solve only simple analogies like "big : bigger" or "Paris : France."',
        'B) Using vector arithmetic, complex relationships such as "Sarkozy - France + Merkel = Germany" can be approximated, though the accuracy is not guaranteed.',
        'C) Vector operations primarily work for geographic relationships, such as "Japan : Tokyo."',
        'D) The training set size does not impact the accuracy of vector operations, as the vectors are derived independently of data size.',
        'E) All examples shown in Table 8 would score 100% on the semantic-syntactic test set.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is correct because the examples demonstrate that vector arithmetic can approximate complex relationships involving entities like political leaders and countries. However, the accuracy of these approximations is not guaranteed and depends on factors such as training data size and vector dimensionality.'
    ),
    'image': 'images/w2vt8.png',
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 6'
}

question_Efficient_Word_Representations_6_4 = {
    'question': (
        'In the conclusion (Section 6 Efficient Estimation of Word Representations in Vector Space), which of the following most accurately captures the authors’ view on the future of word vector applications?'
    ),
    'options_list': [
        'A) The authors believe that word vectors are already fully optimized for NLP tasks like translation and sentiment analysis.',
        'B) Distributed word representations will likely become obsolete as more complex architectures are developed.',
        'C) High-quality word vectors will continue to play an important role in NLP tasks, and there is significant potential for their application in tasks such as fact extension in Knowledge Bases.',
        'D) The authors suggest that improvements to word vectors will only result from increasing training data size, and not from architectural changes.',
        'E) The authors plan to shift away from word vector research and focus on alternative NLP techniques, such as Latent Semantic Analysis (LSA).'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C is correct because the authors express optimism about the future applications of high-quality word vectors, including their potential use in extending and verifying facts in Knowledge Bases. They see ongoing value in word vectors for various NLP tasks.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 6'
}

question_Efficient_Word_Representations_6_5 = {
    'question': (
        'Based on Table 8, what operation is used to identify the relationship between words like "Paris" and "France"?'
    ),
    'options_list': [
        'A) Subtract the word vectors for "France" and "Paris," then add the vector for another word like "Italy."',
        'B) Add the word vectors for "Paris" and "France," then subtract the vector for another word like "Italy."',
        'C) Multiply the word vectors for "Paris" and "France" to get the combined relationship.',
        'D) Concatenate the word vectors for "Paris" and "France" and apply a linear transformation.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Option A is correct because the method involves computing vector relationships by performing arithmetic operations: subtracting one word vector from another and then adding a third. For example, "Paris - France + Italy" aims to find the word vector closest to the result, which ideally corresponds to "Rome."'
    ),
    'image': 'images/w2vt8.png',
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 6'
}


question_Efficient_Word_Representations_6_7 = {
    'question': (
        'True or False: The authors of Efficient Estimation of Word Representations in Vector Space suggest that increasing the size of the dataset and using larger dimensionality for word vectors can improve accuracy in solving word pair relationships.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The authors mention that both increasing the size of the training dataset and using higher-dimensional word vectors can lead to significant improvements in accuracy, potentially surpassing the current 60% accuracy level.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 6'
}

question_Efficient_Word_Representations_6_11 = {
    'question': (
        'Which of the following tasks is mentioned as having been successfully tackled using word vectors in the conclusion?'
    ),
    'options_list': [
        'A) Sentiment analysis',
        'B) Machine translation',
        'C) Object detection',
        'D) Neural style transfer'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Option A is correct because the authors mention that word vectors have been successfully applied to tasks like sentiment analysis and paraphrase detection.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space 6'
}

question_Efficient_Word_Representations_3_13 = {
    'question': (
        'Regarding the projection matrices used in both the Continuous Bag-of-Words (CBOW) and Skip-gram models, which of the following statements is incorrect?'
    ),
    'options_list': [
        'A) In the CBOW model, the projection matrix is shared among all context words.',
        'B) The Skip-gram model uses multiple projection matrices depending on the distance of the context words.',
        'C) In the CBOW model, all context words are projected into the same position in the projection layer.',
        'D) The Skip-gram model uses a different projection matrix for predicting each context word.',
        'E) Both CBOW and Skip-gram models aim to minimize computational complexity by reducing dimensionality with projection matrices.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Option D is incorrect because the Skip-gram model does not use a different projection matrix for each context word. Instead, it uses the same projection matrix to predict all surrounding context words. The other options accurately describe aspects of the CBOW and Skip-gram models.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space, Section 3'
}

question_Efficient_Word_Representations_3_14 = {
    'question': (
        'Compared to the CBOW model, how does the training complexity of the Skip-gram model change?'
    ),
    'options_list': [
        'A) It remains the same because both models have similar architectures.',
        'B) It increases because the Skip-gram model predicts multiple context words for each target word.',
        'C) It decreases since the Skip-gram model only focuses on past words instead of both past and future words.',
        'D) It decreases because the projection layer in the Skip-gram model is simplified.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is correct because the training complexity of the Skip-gram model increases compared to the CBOW model. This increase is due to the Skip-gram model\'s objective of predicting multiple surrounding context words for each target word, which requires more computations.'
    ),
    'chapter_information': 'Efficient Estimation of Word Representations in Vector Space, Section 3'
}

KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_11_MPC = KC_MPC_QUESTIONS[:-1]
