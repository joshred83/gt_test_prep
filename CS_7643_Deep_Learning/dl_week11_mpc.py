question_GT_Module_3_1 = {
    'question': (
        'Which of the following statements is true regarding Recurrent Neural Networks (RNNs) and their capacity to process sequences?'
    ),
    'options_list': [
        'A) RNNs use unique parameters at each time step, allowing them to capture long-term dependencies without issue.',
        'B) RNNs share the same parameters across time steps, enabling them to process variable-length sequences.',
        'C) RNNs cannot handle variable-length sequences due to the vanishing gradient problem.',
        'D) RNNs require fixed-size input sequences because they cannot share parameters over time.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'RNNs utilize parameter sharing across time steps, allowing them to handle sequences of varying lengths. While RNNs can suffer from the vanishing gradient problem, they are still capable of processing variable-length sequences.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_2 = {
    'question': (
        'True or False: Attention mechanisms in neural networks require input data to be ordered sequentially to function correctly.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'Attention mechanisms do not require input data to be ordered sequentially. They focus on relevant parts of the input, allowing them to function with both ordered (sequential) and unordered data.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_3 = {
    'question': (
        'In the context of attention-based mechanisms, which of the following is not an advantage over traditional RNNs?'
    ),
    'options_list': [
        'A) Ability to focus on all past inputs simultaneously.',
        'B) Eliminates the need for backpropagation through time, thus avoiding vanishing gradients.',
        'C) Requires ordered input sequences to function properly.',
        'D) Can handle variable-sized inputs without a fixed computational cost per input element.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Attention mechanisms can function with unordered input sequences, unlike RNNs, which inherently process data sequentially. Other options describe advantages of attention mechanisms.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_4 = {
    'question': (
        'Which statement about the softmax function in attention mechanisms is false?'
    ),
    'options_list': [
        'A) It can produce a probability distribution over an arbitrary set of items.',
        'B) It requires the input set to be of a fixed size.',
        'C) It can be applied to ordered or unordered sets.',
        'D) It can handle an arbitrary number of elements.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The softmax function does not require the input set to be of a fixed size; it can handle varying sizes and can be applied to both ordered and unordered sets.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_5 = {
    'question': (
        'True or False: Multi-head attention in Transformer models enhances the model\'s ability to learn various aspects of relationships between input components by applying multiple attention mechanisms simultaneously.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Multi-head attention allows a model to focus on different parts of the input sequence simultaneously, learning multiple types of relationships within the data.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

# question_GT_Module_3_6 = {
#     'question': (
#         'Which of the following best describes the primary innovation introduced by Transformer architectures over traditional RNNs?'
#     ),
#     'options_list': [
#         'A) Utilizing convolutional layers to capture local dependencies in sequences.',
#         'B) Introducing an attention mechanism that allows for dynamic weighting of all input elements, regardless of their position.',
#         'C) Employing recurrent structures with shared parameters to process sequences.',
#         'D) Compressing all past inputs into a single state vector for future predictions.'
#     ],
#     'correct_answer': 'B',
#     'explanation': (
#         'Transformers\' primary innovation is the use of self-attention mechanisms that dynamically weigh input elements, enabling the model to handle dependencies without relying on the sequence order.'
#     ),
#     'chapter_information': 'GT Module 3 Introduction'
# }

question_GT_Module_3_6 = {
    'question': (
        'Which of the following best describes the primary innovations introduced by Transformer architectures over traditional RNNs? (Note: Multiple answers may be correct.)'
    ),
    'options_list': [
        'A) Utilizing convolutional layers to capture local dependencies in sequences.',
        'B) Introducing an attention mechanism that allows for dynamic weighting of all input elements, reducing training time significantly.',
        'C) Employing recurrent structures with shared parameters to process sequences efficiently.',
        'D) Compressing all past inputs into a single state vector for future predictions, improving computational efficiency.',
        'E) Removing the need for sequential data processing, enabling parallelization during training and inference.',
        'F) Utilizing positional encodings to retain the order of input elements in a non-recurrent fashion.'
    ],
    'correct_answer': ['B', 'E', 'F'],
    'explanation': (
        'The primary innovations of Transformers include the introduction of the self-attention mechanism (Option B), which allows for dynamic weighting of input elements and enables parallel processing (Option E), drastically speeding up training and inference. Additionally, Transformers use positional encodings (Option F) to retain the order of input elements, unlike RNNs that rely on sequential processing. Options A, C, and D either misattribute the innovation or inaccurately describe the architecture.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}


question_GT_Module_3_7 = {
    'question': (
        'In sequence modeling, which input-output configuration is appropriate for a task like sentiment analysis of a sentence?'
    ),
    'options_list': [
        'A) Many-to-Many',
        'B) Many-to-One',
        'C) One-to-Many',
        'D) One-to-One'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In sentiment analysis, the input is a sequence of words (many), and the output is a single sentiment classification (one), fitting the many-to-one configuration.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}


question_GT_Module_3_8 = {
    'question': (
        'True or False: The vanishing gradient problem in RNNs occurs because gradients become increasingly large as they are backpropagated through time.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The vanishing gradient problem occurs when gradients become increasingly small, not large, as they are backpropagated through time, making it difficult for the network to learn long-term dependencies.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_9 = {
    'question': (
        'Which of the following statements about graph-based neural networks is false?'
    ),
    'options_list': [
        'A) They can capture relationships between entities by learning patterns within graph-structured data.',
        'B) Nodes must represent sequential data for the attention mechanism to function properly.',
        'C) They utilize attention mechanisms that can be generalized to unordered sets.',
        'D) Nodes can have vector representations that are refined using local features and those of their neighbors.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Nodes in graph-based networks do not need to represent sequential data; attention mechanisms can function with unordered sets.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_10 = {
    'question': (
        'Which neural network architectures inherently require input data to be sequentially ordered to function correctly?'
    ),
    'options_list': [
        'A) Only Recurrent Neural Networks (RNNs)',
        'B) Both RNNs and Attention-Based Networks',
        'C) Convolutional Neural Networks (CNNs) and RNNs',
        'D) Fully Connected Neural Networks (FCNNs), CNNs, and RNNs'
    ],
    'correct_answer': 'A',
    'explanation': (
        'RNNs inherently require input data to be sequentially ordered because they process data one element at a time, maintaining a state that depends on previous inputs. Other architectures like attention-based networks and CNNs do not inherently require sequential ordering.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_11 = {
    'question': (
        'Which statement best explains why Graph-Based Networks differ from Attention-Based Networks?'
    ),
    'options_list': [
        'A) Graph-Based Networks require explicit edge definitions between nodes, while Attention-Based Networks define relationships through self-attention.',
        'B) Attention-Based Networks are incapable of handling graph-structured data due to their reliance on sequence order.',
        'C) Graph-Based Networks use residual connections similar to those in Transformer models to enhance feature extraction.',
        'D) Both Graph-Based and Attention-Based Networks use node representations but differ only in their training optimizations.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Graph-Based Networks explicitly define relationships (edges) between nodes, whereas Attention-Based Networks use self-attention to dynamically learn relationships without needing explicit connections.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_12 = {
    'question': (
        'True or False: The self-attention mechanism in Transformer models depends on having prior knowledge of the relationships between elements in the input sequence to produce meaningful results.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The self-attention mechanism does not require prior knowledge of relationships. It learns these relationships dynamically during training, focusing on different parts of the input sequence as needed.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_13 = {
    'question': (
        'When processing sequences, which neural network is least likely to exhibit vanishing or exploding gradients during training?'
    ),
    'options_list': [
        'A) Recurrent Neural Networks, since they share weights over time.',
        'B) Attention-Based Networks, because they update a single compact vector throughout the sequence.',
        'C) Convolutional Neural Networks, as they focus on grid-like image data.',
        'D) Graph-Based Networks, which propagate information through node connections.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Graph-Based Networks do not rely on sequential processing with shared weights, so they are less prone to the vanishing or exploding gradient problems that affect RNNs during backpropagation through time.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_14 = {
    'question': (
        'Which of the following neural network architectures is inherently limited when processing variable-length input sequences?'
    ),
    'options_list': [
        'A) Fully Connected Neural Networks',
        'B) Graph-Based Networks',
        'C) Attention-Based Networks',
        'D) Transformers'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Fully Connected Neural Networks (FCNNs) expect fixed-size input data and do not have mechanisms to handle variable-length sequences natively. In contrast, other architectures like Graph-Based Networks, Attention-Based Networks, and Transformers can handle variable-length inputs.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_15 = {
    'question': (
        'In the context of architectural biases in neural networks, which of the following is most likely incorrect?'
    ),
    'options_list': [
        'A) Convolutional Neural Networks were originally used for text data before more specialized structures were developed.',
        'B) The use of residual connections in Transformer models directly addresses the issue of vanishing gradients in Recurrent Neural Networks.',
        'C) Multi-Head Attention allows a model to simultaneously consider different aspects of relationships between input components.',
        'D) Fully Connected Neural Networks are limited to fixed-size inputs, whereas RNNs can handle variable-length inputs.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'CNNs were initially designed for image processing, exploiting spatial relationships in grid-like data. They have since been adapted for text processing, but they were not originally created for that purpose.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_16 = {
    'question': (
        'In natural language processing (NLP), which of the following statements is least likely to be correct regarding the use of embeddings for words and sequences?'
    ),
    'options_list': [
        'A) Word embeddings rely solely on the fixed window size $2m$ to capture the contextual meaning of each word.',
        'B) Graph embeddings are used to capture the ordering of words in sequential data, representing complex structures beyond just sequences.',
        'C) Attention mechanisms in transformers cannot learn meaningful word representations without a predefined sequential order.',
        'D) Skip-gram models focus on using a target word to predict its context words, thereby learning embeddings that reflect its relationship with other words.'
    ],
    'correct_answer': 'D',
    'explanation': (
        'Option D is correct because the skip-gram model uses a target word to predict its context, learning meaningful embeddings. Options A, B, and C are incorrect: word embeddings are not strictly dependent on the fixed window size, graph embeddings do not primarily capture word order, and attention mechanisms do not need a predefined order to learn meaningful representations.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_17 = {
    'question': (
        'True or False: The mathematical formulation of a sentence probability as a product of conditional probabilities, $p(s) = \prod_i p(w_i \mid w_{i-1}, \dots, w_1)$, implies that language models like RNNs must always consider the entire sequence of previous words to predict the next word effectively.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'This statement is false. While RNNs can theoretically consider the entire history of previous words through their hidden state, in practice, they rely on the hidden state $h_i$ to capture relevant information without explicitly using all previous words at each prediction step.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_18 = {
    'question': (
        'When using attention mechanisms in machine translation, which of the following is most likely a misconception?'
    ),
    'options_list': [
        'A) Attention mechanisms dynamically focus on different parts of the input sequence, aligning with the output sequence during translation.',
        'B) The alignment matrix used in attention mechanisms requires a one-to-one mapping between words in the source and target languages.',
        'C) Attention-based models can handle different grammatical structures in source and target languages.',
        'D) The attention mechanism allows the model to upweight or downweight specific parts of the input sequence based on their relevance to the current output.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is the misconception. The alignment matrix in attention mechanisms does not require a one-to-one mapping; it allows for flexible associations between source and target words. This flexibility is a core feature of attention mechanisms, enabling them to model varying grammatical structures.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_19 = {
    'question': (
        'Which of the following statements about sequence-to-sequence models with attention is least misleading?'
    ),
    'options_list': [
        'A) The encoder-decoder architecture requires the entire input sequence to be compressed into a single vector, limiting the model\'s capacity for long sentences.',
        'B) Attention mechanisms in Seq2Seq models allow the decoder to focus on specific parts of the input sequence, alleviating the need for a compact context vector.',
        'C) Attention in Seq2Seq models guarantees that each word in the input sequence will be used in generating the output sequence.',
        'D) Without attention, the decoder cannot use any information from the input sequence other than the initial context vector provided by the encoder.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is the least misleading because it accurately describes how attention mechanisms allow the decoder to selectively focus on different parts of the input sequence, thus reducing the burden on the context vector. Options A, C, and D introduce inaccuracies: Seq2Seq models with attention do not strictly require a single compact vector, attention does not guarantee the use of every input word, and the decoder can still use the initial context vector even without attention.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_20 = {
    'question': (
        'True or False: Graph embeddings and word embeddings are fundamentally different in that word embeddings are learned using self-supervised tasks, whereas graph embeddings rely exclusively on supervised learning.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'This statement is false. Both word embeddings and graph embeddings can be learned using self-supervised tasks. For example, graph embeddings can be trained through random walk sampling in methods like DeepWalk, which does not rely on explicit supervised labels.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_21 = {
    'question': (
        'In the context of cross-lingual masked language modeling, which of the following is most likely a misinterpretation of the training process?'
    ),
    'options_list': [
        'A) The model is trained by masking parts of sentences in multiple languages and predicting the masked tokens using shared multilingual embeddings.',
        'B) Cross-lingual embeddings ensure that words with similar meanings in different languages have similar vector representations.',
        'C) The model must know the exact word alignments between languages to learn effective cross-lingual embeddings.',
        'D) Masked language modeling allows the model to learn contextual information by predicting words based on their surrounding context.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C is the misinterpretation. Cross-lingual embeddings do not require explicit word alignments between languages. The model learns through context provided by multilingual data, allowing it to capture semantic similarities without needing exact word correspondences.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_22 = {
    'question': (
        'True or False: Beam search, as used in machine translation, is designed to exhaustively explore all possible sequences to ensure the most optimal translation is found.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'This statement is false. Beam search is a heuristic search strategy that explores a limited number of sequences (determined by the beam size $k$) to find a likely translation, but it does not exhaustively explore all possible sequences. The goal is to balance finding a good solution with computational feasibility.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_23 = {
    'question': (
        'Which of the following statements is not necessarily true about the mathematical representation of a sentence\'s probability in language modeling?'
    ),
    'options_list': [
        'A) The joint probability of a sequence of words can be decomposed into a product of conditional probabilities.',
        'B) Each word\'s probability is independent of the previous words when modeling the sentence\'s probability.',
        'C) The probability of a sentence is calculated by multiplying the probabilities of each word given all preceding words.',
        'D) Language models like RNNs utilize this decomposition to capture dependencies between words in a sequence.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is false because, in language modeling, each word\'s probability depends on the previous words, reflecting their dependencies. Option A is true, as it follows the chain rule of probability. Option C accurately describes how language models calculate sentence probability, and Option D is correct in explaining how RNNs utilize this decomposition.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_24 = {
    'question': (
        'In the Word2vec skip-gram model, which of the following is false regarding how it learns word embeddings?'
    ),
    'options_list': [
        'A) It predicts the surrounding context words based on the center word within a fixed window size.',
        'B) It uses the context words to predict the center word, maximizing the probability of the center word given its context.',
        'C) The model aims to maximize the probability of context words given the center word.',
        'D) It treats the prediction of each context word as an independent task.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B describes the Continuous Bag of Words (CBOW) model, not the skip-gram model. The skip-gram model focuses on predicting surrounding context words given the center word. Options A, C, and D correctly describe the workings of the skip-gram model.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_25 = {
    'question': (
        'True or False: In graph embeddings, the goal is to optimize embeddings so that connected nodes have more similar embeddings than unconnected nodes, thereby capturing the graph\'s structure.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Graph embeddings aim to reflect the graph\'s structure by ensuring that nodes with direct connections have more similar embeddings than those without connections, thereby capturing the underlying relational information.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_26 = {
    'question': (
        'Which of the following embeddings is least likely to be directly utilized in the VideoSpace application for classification and recommendation tasks?'
    ),
    'options_list': [
        'A) Page Embedding',
        'B) Video Embedding',
        'C) Word Embedding',
        'D) User Embedding'
    ],
    'correct_answer': 'D',
    'explanation': (
        'The VideoSpace application, as described, focuses on using video, page, and word embeddings for classification and recommendation. There is no mention of using user embeddings directly in this context, making Option D the least likely.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_27 = {
    'question': (
        'Which statement about attention mechanisms in machine translation is incorrect?'
    ),
    'options_list': [
        'A) Attention mechanisms allow the model to focus on relevant parts of the source sentence when generating each target word.',
        'B) They help in aligning target words with specific source words or phrases, especially when languages have different grammatical structures.',
        'C) Attention mechanisms eliminate the need for an encoder-decoder architecture by directly mapping input sentences to output sentences.',
        'D) They address the limitations of compressing the source sentence into a single fixed-length context vector.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Attention mechanisms are often used within encoder-decoder architectures to enhance their performance by focusing on relevant parts of the input. They do not eliminate the need for the encoder-decoder framework. Options A, B, and D correctly describe the benefits and functionalities of attention mechanisms in machine translation.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_28 = {
    'question': (
        'True or False: In a sequence-to-sequence model with an encoder-decoder architecture, the decoder relies solely on the context vector generated by the encoder to produce the output sequence, without any additional inputs at each decoding step.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': (
        'The decoder not only uses the context vector from the encoder but also typically incorporates additional inputs, such as the previous output or a start token, at each decoding step to generate the sequence.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_29 = {
    'question': (
        'When using beam search in sequence prediction tasks, increasing the beam size $k$ will:'
    ),
    'options_list': [
        'A) Reduce computational cost by narrowing down the number of sequences considered at each step.',
        'B) Increase the number of sequences considered, potentially improving accuracy at the expense of computational efficiency.',
        'C) Have no impact on the search process since beam size does not affect the number of hypotheses maintained.',
        'D) Randomly select sequences to consider, introducing stochasticity into the search process.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Increasing the beam size $k$ results in more sequences being explored, which can improve the accuracy of the predictions but at the cost of increased computational requirements. Option A is incorrect as increasing $k$ increases, not reduces, the computational cost. Option C is incorrect because beam size directly impacts the number of hypotheses considered. Option D incorrectly introduces the concept of randomness in beam search, which is a deterministic process.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_30 = {
    'question': (
        'Which of the following statements about cross-lingual masked language modeling is true?'
    ),
    'options_list': [
        'A) It predicts masked words using context from the same language only, requiring separate models for each language.',
        'B) It utilizes embeddings that allow the model to process multilingual input, predicting masked words across different languages.',
        'C) It cannot learn relationships between words in different languages due to the absence of shared vocabulary.',
        'D) It requires all sentences to be translated into a single language before modeling.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Cross-lingual masked language models use shared embeddings to predict masked words across multiple languages, leveraging the multilingual context to learn relationships. Options A, C, and D contain misconceptions about cross-lingual learning.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_31 = {
    'question': (
        'In differentiable selection of a vector from a set using softmax, the attention weights $a_j$ are computed as:'
    ),
    'options_list': [
        'A) $a_j = \\frac{u_j \\cdot q}{\\sum_k u_k \\cdot q}$',
        'B) $a_j = \\frac{e^{u_j + q}}{\\sum_k e^{u_k + q}}$',
        'C) $a_j = \\frac{e^{u_j \\cdot q}}{\\sum_k e^{u_k \\cdot q}}$',
        'D) $a_j = \\frac{e^{u_j \\cdot q}}{e^{u_k \\cdot q}}$'
    ],
    'correct_answer': 'C',
    'explanation': (
        'This formula represents the softmax function applied to the dot product $u_j \\cdot q$, which computes the attention weights. This allows for the differentiable selection of vectors based on their similarity to the query vector $q$.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}

question_GT_Module_3_32 = {
    'question': (
        'True or False: In the Word2vec skip-gram model, the context window size $2m$ is fixed, indicating that a constant number of words before and after the center word are considered as context during training.'
    ),
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'In the skip-gram model, the context window size $2m$ is indeed fixed during training, meaning a constant number of words on either side of the center word are used as context to predict the target.'
    ),
    'chapter_information': 'GT Module 3 Introduction'
}




KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_11_MPC = KC_MPC_QUESTIONS[:-1]
