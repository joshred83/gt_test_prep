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
        'In the Word2vec skip-gram model, which of the following is FALSE regarding how it learns word embeddings?'
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

##############################################################################################

q1uestion_GT_Module_3_21 = {
    'question': (
        'Which of the following is not a key difference between RNNs and LSTMs?'
    ),
    'options_list': [
        'A) LSTMs use forget gates to control the flow of information, while RNNs do not.',
        'B) RNNs suffer from vanishing gradient problems more severely than LSTMs.',
        'C) LSTMs cannot process sequential data because they lack a hidden state mechanism.',  # Correct answer
        'D) LSTMs are better at capturing long-term dependencies due to their memory cell structure.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is incorrect because LSTMs can process sequential data using hidden states, and this statement is deliberately misleading. '
        'A), B), and D) correctly highlight key differences between RNNs and LSTMs.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}
q1uestion_GT_Module_3_23 = {
    'question': (
        'Which of the following is the correct probability equation for the Skip-gram model in word2vec?'
    ),
    'options_list': [
        'A) $P(w_t \mid w_{t-1}, w_{t+1})$',
        'B) $P(w_{context} \mid w_{target})$',
        'C) $P(w_{target} \mid w_{context})$',  # Correct answer
        'D) $P(w_t) = \\frac{1}{Z} \sum P(w_{context} \mid w_t)$'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because Skip-gram aims to predict the target word given its surrounding context. '
        'A) describes a different type of model. '
        'D) introduces an unrelated concept (normalization) but isn\'t correct in this context.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

q1uestion_GT_Module_3_24 = {
    'question': (
        'What is the purpose of using t-SNE in word embedding visualizations?'
    ),
    'options_list': [
        'A) To reduce high-dimensional word embeddings into 2D or 3D for better visualization.',  # Correct answer
        'B) To optimize the training loss for word2vec models.',
        'C) To improve the intrinsic evaluation of word embeddings.',
        'D) To compute the perplexity of the language model.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'A) is correct because t-SNE is primarily used to reduce dimensionality for visualization purposes. '
        'B), C), and D) are unrelated to the primary function of t-SNE.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

q1uestion_GT_Module_3_25 = {
    'question': (
        'True or False: The encoder-decoder model used in seq2seq tasks cannot handle variable-length input and output sequences.'
    ),
    'options_list': [
        'True',
        'False'  # Correct answer
    ],
    'correct_answer': 'False',
    'explanation': (
        'False—encoder-decoder models are specifically designed to handle variable-length sequences by using recurrent layers like LSTMs or transformers.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

q1uestion_GT_Module_3_26 = {
    'question': (
        'Which of the following best describes beam search in the context of sequence prediction?'
    ),
    'options_list': [
        'A) It is a greedy algorithm that selects the highest probability word at each step.',
        'B) Beam search always returns the most probable sequence without exploring alternatives.',
        'C) Beam search keeps a fixed number of hypotheses at each step, balancing exploration and exploitation.',  # Correct answer
        'D) Beam search guarantees finding the global optimum sequence every time.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct as beam search maintains a limited number of candidates at each decoding step to explore a variety of possible sequences. '
        'A), B), and D) are incorrect descriptions of beam search.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

q1uestion_GT_Module_3_27 = {
    'question': (
        'What is the primary function of the attention mechanism in neural networks?'
    ),
    'options_list': [
        'A) To focus on relevant parts of the input sequence when predicting the output.',  # Correct answer
        'B) To apply dropout regularization during training.',
        'C) To compute word embeddings for downstream tasks.',
        'D) To replace all recurrent layers in sequence models.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'A) is correct because attention mechanisms allow models to focus on relevant portions of the input sequence. '
        'B), C), and D) introduce unrelated ideas.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

q1uestion_GT_Module_3_28 = {
    'question': (
        'True or False: In transformers, positional encoding is necessary because the model lacks inherent awareness of sequence order.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'True—transformers do not have a built-in notion of sequence order, so positional encoding provides the necessary information.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

q1uestion_GT_Module_3_29 = {
    'question': (
        'How does byte pair encoding (BPE) help improve language models?'
    ),
    'options_list': [
        'A) It reduces the number of attention heads required for transformers.',
        'B) It splits rare words into more frequent subword units, improving vocabulary efficiency.',  # Correct answer
        'C) It encodes positional information for input sequences.',
        'D) It compresses entire sentences into a single vector for faster computation.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because BPE splits rare words into subword units, improving vocabulary handling in language models. '
        'A), C), and D) are unrelated to BPE\'s main purpose.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

q1uestion_GT_Module_3_30 = {
    'question': (
        'For a transformer model with a hidden size of 512, and an input sequence of length 10, what is the size of the self-attention matrix for the encoder?'
    ),
    'options_list': [
        'A) $10 \\times 512$',
        'B) $512 \\times 512$',
        'C) $10 \\times 10$',  # Correct answer
        'D) $512 \\times 10$'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because self-attention produces a $10 \\times 10$ matrix for a sequence of length 10, where each element attends to every other element.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

# Conceptual Questions

qauestion_1 = {
    'question': (
        'Which of the following statements is incorrect regarding Recurrent Neural Networks (RNNs) and Long Short-Term Memory networks (LSTMs)?'
    ),
    'options_list': [
        'A) RNNs suffer from vanishing gradients when learning long-term dependencies.',
        'B) LSTMs address vanishing gradients through gating mechanisms like forget gates.',
        'C) LSTMs always outperform RNNs in tasks involving sequence data.',  # Correct answer
        'D) RNNs update their hidden states at each time step, conditioned on the previous hidden state.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'While LSTMs are better at handling long-term dependencies, they do not always outperform RNNs, particularly in cases where short-term dependencies dominate.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

qauestion_2 = {
    'question': (
        'True or False: Teacher forcing is a technique used during the training of RNNs and LSTMs in which the ground truth from the training data is used as the next input instead of the model\'s own predictions.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Teacher forcing helps the model learn faster by providing the correct target output as input for the next time step, preventing error accumulation during training.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

qauestion_3 = {
    'question': (
        'Which of the following is the correct formulation of the probability for the Skip-gram model in word2vec?'
    ),
    'options_list': [
        'A) $P(context\\_words \\mid target\\_word)$',  # Correct answer
        'B) $P(target\\_word \\mid context\\_words)$',
        'C) $P(word\\_embeddings \\mid sentences)$',
        'D) $P(context\\_words \\mid word\\_embeddings)$'
    ],
    'correct_answer': 'A',
    'explanation': (
        'In the Skip-gram model, the objective is to predict the surrounding context words given a target word.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

qauestion_4 = {
    'question': (
        'In t-SNE, how are high-dimensional points represented in a lower-dimensional space?'
    ),
    'options_list': [
        'A) By minimizing the Euclidean distance between the points.',
        'B) By preserving the local structure of data points in the high-dimensional space.',  # Correct answer
        'C) By clustering similar points into predefined clusters.',
        'D) By calculating word similarity based on context embeddings.'
    ],
    'correct_answer': 'B',
    'explanation': (
        't-SNE is a technique that reduces dimensionality by preserving the local distances and relationships between points from the original high-dimensional space.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

que3stion_5 = {
    'question': (
        'True or False: The encoder-decoder architecture in RNNs for sequence-to-sequence models generates output sequences by encoding the entire input sequence into a fixed-length vector and then decoding that vector into the target sequence.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'The encoder-decoder model first encodes the input sequence into a single vector (in the context of RNNs or LSTMs), which is then decoded into the target output sequence.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

que3stion_6 = {
    'question': (
        'What does "Beam Search" aim to solve when decoding sequences?'
    ),
    'options_list': [
        'A) The vanishing gradient problem in LSTMs.',
        'B) The issue of generating low-probability sequences during inference.',
        'C) The need for parallel computation of multiple input sequences.',
        'D) The inefficiency of Greedy Search in finding the optimal sequence.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Beam Search maintains a fixed number of the most likely sequences at each time step, providing better results than Greedy Search, which selects only the most likely output at each step.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

qu3estion_7 = {
    'question': (
        'In the Transformer architecture, how does positional encoding work?'
    ),
    'options_list': [
        'A) By adding learned embeddings for positions in the sequence.',
        'B) By scaling the input vectors with sine and cosine functions of different frequencies.',  # Correct answer
        'C) By calculating the difference between consecutive input tokens.',
        'D) By applying convolution to the input sequence to capture position information.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The Transformer uses sine and cosine functions to encode positional information, allowing the model to understand the order of the tokens without recurrent connections.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

# Computation Questions

quest3ion_8 = {
    'question': (
        'In the self-attention mechanism of a Transformer, what are the dimensions of the output matrix of the attention operation in the encoder, assuming input sequence length $n$ and hidden size $d_{model}$?'
    ),
    'options_list': [
        'A) $(n \\times d_{model})$',  # Correct answer
        'B) $(d_{model} \\times d_{model})$',
        'C) $(n \\times n)$',
        'D) $(d_{model} \\times 1)$'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The self-attention mechanism produces an output matrix of size $(n \\times d_{model})$, where $n$ is the sequence length and $d_{model}$ is the hidden size.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

ques3tion_9 = {
    'question': (
        'True or False: In the cross-attention between the encoder and decoder in a Transformer, the query comes from the encoder, and the keys and values come from the decoder.'
    ),
    'options_list': [
        'True',
        'False'  # Correct answer
    ],
    'correct_answer': 'False',
    'explanation': (
        'In cross-attention, the query comes from the decoder, while the keys and values come from the encoder. This allows the decoder to attend to the encoded representations of the input sequence.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}
quest3ion_10 = {
    'question': (
        'In a Transformer with an input sequence length $n=64$, hidden size $d_{model}=512$, and $h=8$ attention heads, what is the size of the key matrix for each attention head, used in the multi-head self-attention mechanism?'
    ),
    'options_list': [
        'A) $(n \\times d_{model})$',
        'B) $(n \\times \\frac{d_{model}}{h})$',  # Correct answer
        'C) $(\\frac{d_{model}}{h} \\times h)$',
        'D) $(n \\times h)$'
    ],
    'correct_answer': 'B',
    'explanation': (
        'For each attention head in multi-head self-attention, the hidden size $d_{model}$ is split equally across all $h$ heads. The key matrix has dimensions corresponding to the input sequence length $n$ and the reduced hidden size $\\frac{d_{model}}{h}$ for each head, resulting in a matrix of size $(n \\times \\frac{d_{model}}{h})$ for each head.'
    ),
    'chapter_information': 'GT lecture lesson 11'
}

# Conceptual Questions

questiony_1 = {
    'question': (
        'Which of the following limitations is specific to Multi-Layer Perceptrons (MLPs) when modeling sequences?'
    ),
    'options_list': [
        'A) They can only handle sequential data with fixed input-output mappings.',
        'B) They have no inherent temporal structure to model time steps.',  # Correct answer
        'C) They require a fixed memory size for each input sequence.',
        'D) They are unable to process word embeddings as inputs.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'MLPs cannot inherently model the time-dependent structure in sequences, unlike RNNs, which capture this temporal structure through recurrent connections.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_2 = {
    'question': (
        'In the context of RNNs, which statement correctly describes "truncated backpropagation through time"?'
    ),
    'options_list': [
        'A) It restricts the forward pass to a fixed number of time steps.',
        'B) It restricts backpropagation to only a fixed number of time steps backward.',  # Correct answer
        'C) It removes the recursive connections in the RNN for efficient computation.',
        'D) It uses gradient clipping to avoid the vanishing gradient problem.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Truncated backpropagation through time allows the state to propagate forward indefinitely but limits the backward pass to a fixed number of time steps to reduce computational cost.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_3 = {
    'question': (
        'Which of the following best describes the use of gates in an LSTM network?'
    ),
    'options_list': [
        'A) Gates in LSTMs perform affine transformations on the hidden state to avoid overfitting.',
        'B) Gates in LSTMs control the flow of information by modulating how much previous information is carried forward and how much new information is added.',  # Correct answer
        'C) Gates in LSTMs prevent the model from learning long-term dependencies.',
        'D) Gates in LSTMs are used to control the learning rate of the network.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'LSTMs use gates (forget, input, output) to decide how much information from previous states to retain or discard and how much of the new input to consider, enabling the network to handle long-term dependencies.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_4 = {
    'question': (
        'In a conditional language model, if $c$ represents a topic context, what does the model learn?'
    ),
    'options_list': [
        'A) The probability of generating a sentence that is grammatically correct.',
        'B) The probability of generating a sentence conditioned on the topic context.',  # Correct answer
        'C) The probability of recognizing speech in noisy environments.',
        'D) The probability of a sentence being syntactically correct.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In a conditional language model, conditioning on context $c$ allows the model to generate sentences or predict words based on specific topics, which enhances context-aware predictions.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_5 = {
    'question': (
        'True or False: RNNs can handle variable-length sequences as inputs, unlike MLPs, because they process one time step at a time while maintaining an internal state.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'RNNs process sequences by maintaining a hidden state that evolves over time, allowing them to handle variable-length inputs and outputs.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

# Computation Questions

questiony_6 = {
    'question': (
        'In an LSTM, which gate decides how much of the previous cell state should be retained?'
    ),
    'options_list': [
        'A) Input gate',
        'B) Forget gate',  # Correct answer
        'C) Output gate',
        'D) Candidate gate'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The forget gate controls how much of the previous cell state is carried forward to the next time step, allowing the model to retain or discard information.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_7 = {
    'question': (
        'What is the main difference between a vanilla RNN and an LSTM in terms of the state update rules?'
    ),
    'options_list': [
        'A) Vanilla RNNs use additive updates for the hidden state, while LSTMs use multiplicative updates.',
        'B) Vanilla RNNs suffer from exploding gradients, while LSTMs do not have this problem.',
        'C) Vanilla RNNs update their state purely through multiplicative operations, while LSTMs introduce additive updates through the cell state.',  # Correct answer
        'D) Vanilla RNNs have no gates, whereas LSTMs introduce input, forget, and output gates.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The cell state in LSTMs allows for additive updates, which help mitigate the vanishing gradient problem, whereas vanilla RNNs rely purely on multiplicative updates.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_8 = {
    'question': (
        'True or False: In a conditional language model for machine translation, if $c$ is the source sentence, the model learns the probability of generating the target sentence conditioned on the source sentence.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'In machine translation, conditional language models predict the probability of generating the target sentence given the source sentence as context.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_9 = {
    'question': (
        'Which of the following correctly describes how vanishing gradients occur in RNNs?'
    ),
    'options_list': [
        'A) When the weight matrices are initialized with very large values, the gradients grow exponentially.',
        'B) When the weights used in the recursive updates are less than one, the gradients shrink exponentially over time.',  # Correct answer
        'C) When the input to the network contains too many time steps, the gradients grow rapidly and cause instability.',
        'D) When the gradients are clipped during backpropagation through time, they become unstable.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In RNNs, when the recursive weights are small, the gradients tend to shrink exponentially during backpropagation through time, causing the vanishing gradient problem.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_10 = {
    'question': (
        'In predictive typing using a language model, how is the next word predicted?'
    ),
    'options_list': [
        'A) By choosing the word with the highest conditional probability based on the history of previous words.',  # Correct answer
        'B) By selecting a random word from the vocabulary.',
        'C) By evaluating all possible combinations of words and picking the one with the highest overall sentence likelihood.',
        'D) By using the history of words and randomly sampling from the context window.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'In predictive typing, language models use the history of previous words to predict the next word based on the conditional probability distribution of the vocabulary.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}


# Conceptual Questions

questiony_31 = {
    'question': (
        'Which of the following is a limitation of using a multi-layer perceptron (MLP) for sequence modeling?'
    ),
    'options_list': [
        'A) MLPs cannot easily handle variable-sized sequences due to their fixed input structure.',  # Correct answer
        'B) MLPs inherently have temporal structure, making them inefficient for sequence processing.',
        'C) MLPs store temporal information from previous time steps, which limits scalability for long sequences.',
        'D) MLPs handle state information using a memory cell, but the state decays over time.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'A) is correct because MLPs struggle with handling variable-sized sequences, requiring hacks to make them work. '
        'B), C), and D) are incorrect; MLPs lack temporal structure and memory mechanisms entirely.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_32 = {
    'question': (
        'What is the primary issue with RNNs when processing long sequences, and how is it mitigated?'
    ),
    'options_list': [
        'A) RNNs suffer from vanishing gradients when processing long sequences, which can be mitigated using LSTMs.',  # Correct answer
        'B) RNNs suffer from exploding gradients when processing short sequences, which can be fixed by truncating the input.',
        'C) RNNs cannot handle sequences longer than the number of training epochs, which is mitigated using multi-layer perceptrons.',
        'D) RNNs cannot perform backpropagation through time, and thus gradients cannot be computed efficiently.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'A) is correct as RNNs suffer from vanishing gradients, and LSTMs mitigate this by using additional mechanisms (like cell states). '
        'B), C), and D) are incorrect; the problem relates to long sequences and vanishing gradients, not exploding gradients or training epochs.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_33 = {
    'question': (
        'True or False: In language modeling, the probability of a sequence is calculated by multiplying the conditional probabilities of each word given the history of previous words.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'True—the chain rule is applied to calculate the probability of a sequence by multiplying conditional probabilities of each word given the preceding words.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_34 = {
    'question': (
        'Which of the following best describes how backpropagation through time (BPTT) works in an RNN?'
    ),
    'options_list': [
        'A) BPTT only propagates errors backward through the network layers without considering the time steps.',
        'B) BPTT performs error propagation backward only for the current time step, ignoring previous inputs.',
        'C) BPTT unrolls the RNN across all time steps and propagates errors backward through the entire sequence.',  # Correct answer
        'D) BPTT propagates errors forward through the sequence, updating the network state in real-time.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct—BPTT unrolls the RNN across time and propagates errors backward through the whole sequence to compute gradients. '
        'A), B), and D) misunderstand how BPTT handles time steps.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_35 = {
    'question': (
        'In an LSTM, which mechanism helps prevent the vanishing gradient problem?'
    ),
    'options_list': [
        'A) The forget gate, which multiplies the input by a value close to 0.',
        'B) The output gate, which prevents too much information from reaching the hidden state.',
        'C) The cell state, which updates additively rather than multiplicatively, allowing information to be carried across time steps.',  # Correct answer
        'D) The input gate, which completely resets the state at each time step.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct—the cell state in an LSTM is updated additively, helping prevent the vanishing gradient issue. '
        'A), B), and D) misunderstand the specific role of each LSTM gate in preventing gradient issues.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_36 = {
    'question': (
        'True or False: The primary advantage of using LSTMs over vanilla RNNs is that LSTMs are capable of handling long-term dependencies more effectively due to their gating mechanisms.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'True—LSTMs are specifically designed to handle long-term dependencies more effectively than vanilla RNNs by using gates like the forget, input, and output gates.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_37 = {
    'question': (
        'Which of the following examples is not a valid use case of a conditional language model?'
    ),
    'options_list': [
        'A) Machine translation, where the source sentence is the conditioning term.',
        'B) Topic-aware language modeling, where the topic of discussion is the conditioning term.',
        'C) Optical character recognition (OCR), where the image of text is the conditioning term.',
        'D) Query completion, where the user\'s search history is ignored to predict future queries.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'D) is correct because query completion typically uses conditioning based on the user\'s past queries (or context). '
        'A), B), and C) are valid examples of conditional language models.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questioyn_38 = {
    'question': (
        'In language modeling, what does the perplexity metric measure?'
    ),
    'options_list': [
        'A) The accuracy of the language model on a test set.',
        'B) The exponential of the average log probability, representing how "confused" the model is about predicting the next word.',  # Correct answer
        'C) The number of parameters in the language model.',
        'D) The difference between the predicted and actual sequence probabilities.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because perplexity measures how well a language model predicts a test set by calculating the exponential of the average log probability. '
        'A), C), and D) introduce unrelated or incorrect ideas.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_39 = {
    'question': (
        'How does truncated backpropagation through time (TBPTT) help in training RNNs with long sequences?'
    ),
    'options_list': [
        'A) TBPTT ignores the previous hidden states to simplify gradient computations.',
        'B) TBPTT backpropagates gradients only through a fixed number of time steps, reducing the computational cost for long sequences.',  # Correct answer
        'C) TBPTT skips certain time steps during forward propagation to shorten the sequence.',
        'D) TBPTT stops gradient updates after each epoch to prevent exploding gradients.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because TBPTT backpropagates gradients only for a limited number of time steps, reducing computational complexity. '
        'A), C), and D) incorrectly describe TBPTT or introduce irrelevant details.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questioyn_40 = {
    'question': (
        'Which of the following steps in LSTM gating decides how much new information from the current input should affect the cell state?'
    ),
    'options_list': [
        'A) Forget gate',
        'B) Input gate',  # Correct answer
        'C) Output gate',
        'D) Cell state update'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because the input gate controls how much new information is added to the cell state based on the current input. '
        'A), C), and D) describe different parts of the LSTM mechanism.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}




KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_11_MPC = KC_MPC_QUESTIONS[:-1]
