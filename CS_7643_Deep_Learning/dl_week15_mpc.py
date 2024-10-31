####NNNEEEED TOOOO HCCEEEEKKK#####

question_101 = {
    'question': (
        'Which of the following statements about Recurrent Neural Networks (RNNs) and Long Short-Term Memory networks (LSTMs) is false?'
    ),
    'options_list': [
        'A) RNNs suffer from the vanishing gradient problem, making it difficult to learn long-term dependencies.',
        'B) LSTMs introduce gating mechanisms that help preserve gradients over long sequences.',
        'C) Both RNNs and LSTMs update their hidden states using the current input and the previous hidden state.',
        'D) LSTMs eliminate all problems related to gradient vanishing and can model infinite-length dependencies without any issues.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'While LSTMs significantly mitigate the vanishing gradient problem through their gating mechanisms, they do not completely eliminate all issues related to gradient vanishing. '
        'LSTMs improve the ability to model long-term dependencies but still face challenges with very long sequences or complex patterns.'
    ),
    'chapter_information': 'General Module 4'
}

question_102 = {
    'question': (
        'In training conditional language models, which technique is used to mitigate exposure bias?'
    ),
    'options_list': [
        'A) Teacher forcing',
        'B) Scheduled sampling',  # Correct answer
        'C) Cross-entropy loss minimization',
        'D) Data augmentation'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Scheduled sampling gradually transitions the model from using ground truth inputs to using its own predictions during training, helping mitigate exposure bias, '
        'which arises when the model is trained on ground truth inputs but is required to generate sequences based on its own predictions during inference.'
    ),
    'chapter_information': 'General Module 4'
}

question_103 = {
    'question': (
        'In the Word2Vec skip-gram model, which of the following statements is correct?'
    ),
    'options_list': [
        'A) The skip-gram model predicts the center word given its surrounding context words.',
        'B) The objective is to maximize the probability of the context words given the center word.',  # Correct answer
        'C) Skip-gram relies on supervised training with labeled data pairs.',
        'D) Word2Vec uses one-hot encoding for word representations during training.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The skip-gram model aims to predict the surrounding context words based on the current center word. It maximizes the conditional probability of context words given the center word.'
    ),
    'chapter_information': 'General Module 4'
}

question_104 = {
    'question': (
        'Which of the following statements is true about t-SNE (t-distributed Stochastic Neighbor Embedding)?'
    ),
    'options_list': [
        'A) t-SNE is a linear dimensionality reduction technique that preserves global data structures.',
        'B) t-SNE clusters data points by maximizing variance along principal components.',
        'C) t-SNE reduces dimensionality by modeling pairwise similarities with probability distributions to preserve local neighbor relationships.',  # Correct answer
        'D) t-SNE is a supervised learning algorithm used for classification tasks.'
    ],
    'correct_answer': 'C',
    'explanation': (
        't-SNE is a nonlinear dimensionality reduction technique that converts high-dimensional data into lower-dimensional space by modeling pairwise similarities between data points. '
        'It focuses on preserving local structures (neighbor relationships) rather than global structures.'
    ),
    'chapter_information': 'General Module 4'
}

question_105 = {
    'question': (
        'In sequence-to-sequence models with an encoder-decoder architecture, the encoder:'
    ),
    'options_list': [
        'A) Generates a fixed-length context vector representing the entire input sequence.',  # Correct answer
        'B) Directly outputs the translated sequence without the need for a decoder.',
        'C) Processes the output sequence and feeds it into the decoder.',
        'D) Is only used during training and discarded during inference.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The encoder processes the input sequence and compresses it into a fixed-length context vector that captures the essential information of the input, '
        'which is then used by the decoder to generate the output sequence.'
    ),
    'chapter_information': 'General Module 4'
}

question_106 = {
    'question': (
        'Beam search in sequence generation tasks:'
    ),
    'options_list': [
        'A) Selects the single most probable token at each time step, building the output sequence greedily.',
        'B) Keeps track of multiple candidate sequences, expanding the most promising ones based on cumulative probabilities.',  # Correct answer
        'C) Guarantees finding the optimal sequence by exploring all possible combinations.',
        'D) Is only applicable when using attention mechanisms.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Beam search maintains a fixed number (beam width) of the most probable sequences at each time step, balancing breadth and depth to explore multiple hypotheses without exhaustively exploring all sequences.'
    ),
    'chapter_information': 'General Module 4'
}

question_107 = {
    'question': (
        'In neural networks, attention mechanisms:'
    ),
    'options_list': [
        'A) Allow the model to focus on specific parts of the input when generating each part of the output.',  # Correct answer
        'B) Are only used in convolutional neural networks for image recognition.',
        'C) Require recurrent connections to function properly.',
        'D) Do not improve model performance on sequence tasks.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Attention mechanisms enable models to weigh the importance of different parts of the input when producing outputs, enhancing performance in tasks like machine translation and text summarization.'
    ),
    'chapter_information': 'General Module 4'
}

question_108 = {
    'question': (
        'In the Transformer architecture, positional encoding is necessary because:'
    ),
    'options_list': [
        'A) The self-attention mechanism inherently captures positional information.',
        'B) Transformers lack recurrence and convolution, so positional encoding provides the model with information about the order of the sequence.',  # Correct answer
        'C) It reduces the computational complexity of the model.',
        'D) It replaces the need for attention mechanisms.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Since Transformers do not use recurrence or convolution, they have no inherent way to capture the sequential order of the input tokens. '
        'Positional encoding provides this information to allow the model to process the order of the sequence.'
    ),
    'chapter_information': 'General Module 4'
}

question_109 = {
    'question': (
        'Byte Pair Encoding (BPE) is used in natural language processing to:'
    ),
    'options_list': [
        'A) Compress data by removing redundant bytes.',
        'B) Tokenize text into subword units by iteratively merging the most frequent pairs of characters or character sequences.',  # Correct answer
        'C) Encode bytes using a fixed-length code for efficient storage.',
        'D) Encrypt text data for secure transmission.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Byte Pair Encoding is a subword segmentation algorithm that helps handle rare words and out-of-vocabulary tokens by representing words as sequences of subword units, improving generalization.'
    ),
    'chapter_information': 'General Module 4'
}

question_110 = {
    'question': (
        'In the Transformer model\'s self-attention mechanism, the computational complexity scales:'
    ),
    'options_list': [
        'A) Linearly with the sequence length.',
        'B) Quadratically with the sequence length.',  # Correct answer
        'C) Logarithmically with the sequence length.',
        'D) Independently of the sequence length.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The self-attention mechanism computes attention scores between all pairs of tokens, resulting in a complexity of O(n^2), where n is the sequence length.'
    ),
    'chapter_information': 'General Module 4'
}


question_111 = {
    'question': (
        'Given a Transformer model with a model dimensionality of $d_{model} = 512$ and $h = 8$ attention heads, what is the dimensionality $d_k$ of each head?'
    ),
    'options_list': [
        'A) 512',
        'B) 256',
        'C) 128',
        'D) 64'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Each attention head has a dimensionality of $d_k = d_{model} / h = 512 / 8 = 64$.'
    ),
    'chapter_information': 'General Module 4'
}

question_112 = {
    'question': (
        'In the cross-attention mechanism of the Transformer decoder, the queries come from:'
    ),
    'options_list': [
        'A) The encoder outputs',
        'B) The decoder\'s previous outputs',  # Correct answer
        'C) The decoder inputs',
        'D) The positional encoding vectors'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In cross-attention, the queries are derived from the decoder\'s previous outputs (target sequence embeddings), while the keys and values come from the encoder\'s outputs (source sequence representations).'
    ),
    'chapter_information': 'General Module 4'
}

question_113 = {
    'question': (
        'Which of the following statements is false regarding LSTMs?'
    ),
    'options_list': [
        'A) LSTMs use forget gates to control the flow of information through the cell state.',
        'B) LSTMs can handle long-term dependencies better than standard RNNs.',
        'C) LSTMs are immune to the vanishing gradient problem and can model infinite sequences without any issues.',  # Correct answer
        'D) LSTMs maintain a cell state that is modified through input, output, and forget gates.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'LSTMs mitigate the vanishing gradient problem but do not completely eliminate it. They are not immune to issues that arise with very long sequences or complex tasks.'
    ),
    'chapter_information': 'General Module 4'
}

question_114 = {
    'question': (
        'Knowledge distillation in neural networks involves:'
    ),
    'options_list': [
        'A) Compressing a large model into a smaller one by training the smaller model to mimic the outputs of the larger model.',  # Correct answer
        'B) Using data augmentation to improve model generalization.',
        'C) Training a model on knowledge graphs to improve its reasoning capabilities.',
        'D) Applying dropout to prevent overfitting.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Knowledge distillation transfers the knowledge from a large "teacher" model to a smaller "student" model by having the student learn to produce similar outputs as the teacher, often using the teacher\'s soft targets.'
    ),
    'chapter_information': 'General Module 4'
}

question_115 = {
    'question': (
        'Perplexity is a metric commonly used to evaluate:'
    ),
    'options_list': [
        'A) Image classification models',
        'B) Language models',  # Correct answer
        'C) Clustering algorithms',
        'D) Reinforcement learning agents'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Perplexity measures how well a language model predicts a sample and is a standard metric for evaluating language models.'
    ),
    'chapter_information': 'General Module 4'
}

question_116 = {
    'question': (
        'Which of the following is false about the skip-gram model in Word2Vec?'
    ),
    'options_list': [
        'A) It predicts surrounding context words given the current center word.',
        'B) It captures both syntactic and semantic word relationships.',
        'C) It relies on predicting the next word in a sequence given all previous words.',  # Correct answer
        'D) It can be trained efficiently on large corpora using negative sampling.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C describes a traditional language model, not the skip-gram model. The skip-gram model focuses on predicting context words surrounding a center word, not sequential next-word prediction.'
    ),
    'chapter_information': 'General Module 4'
}

question_117 = {
    'question': (
        'In the context of neural attention mechanisms, which type of attention allows a model to focus on different positions within its own input sequence?'
    ),
    'options_list': [
        'A) Encoder-decoder attention',
        'B) Self-attention',  # Correct answer
        'C) Global attention',
        'D) Hierarchical attention'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Self-attention enables a model to consider the relationships between all elements in its input sequence, allowing each position to attend to other positions within the same sequence.'
    ),
    'chapter_information': 'General Module 4'
}

question_118 = {
    'question': (
        'Which of the following best describes scheduled sampling in training sequence models?'
    ),
    'options_list': [
        'A) Gradually reducing the learning rate during training to improve convergence.',
        'B) Introducing randomness in the input data to prevent overfitting.',
        'C) Mixing ground truth tokens with the model\'s predicted tokens during training to mitigate exposure bias.',  # Correct answer
        'D) Using multiple models trained on different data subsets to improve robustness.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Scheduled sampling transitions the model from using ground truth inputs to using its own predictions during training, helping it to better handle the discrepancies between training and inference.'
    ),
    'chapter_information': 'General Module 4'
}

question_119 = {
    'question': (
        'In the Transformer architecture, multi-head attention allows the model to:'
    ),
    'options_list': [
        'A) Attend to different positions of the sequence using multiple attention mechanisms in parallel.',  # Correct answer
        'B) Process multiple sequences simultaneously.',
        'C) Reduce the computational complexity of the attention mechanism.',
        'D) Eliminate the need for positional encoding.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Multi-head attention enables the model to capture different types of relationships by allowing each head to focus on different aspects or positions of the input.'
    ),
    'chapter_information': 'General Module 4'
}

question_120 = {
    'question': (
        'What is the primary benefit of using Byte Pair Encoding (BPE) in language modeling?'
    ),
    'options_list': [
        'A) It reduces computational complexity by limiting the vocabulary size.',
        'B) It enables the model to handle out-of-vocabulary words by representing rare words as subword units.',  # Correct answer
        'C) It improves the encryption of text data for secure communication.',
        'D) It increases the size of the vocabulary to capture more linguistic nuances.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'BPE helps in dealing with rare or unseen words by breaking them down into subword units, which the model can learn and combine to understand new words.'
    ),
    'chapter_information': 'General Module 4'
}


question_121 = {
    'question': (
        'Which of the following examples best illustrates the ambiguity problem in machine translation?'
    ),
    'options_list': [
        'A) The sentence “The dog barked” has multiple possible translations in Japanese.',
        'B) “I saw her duck” can be interpreted in multiple ways because "duck" can refer to both an animal and a gesture.',  # Correct answer
        'C) Translating the sentence “I went to the store” from English to French requires special handling of verb tense.',
        'D) Japanese and English sentences often differ in word order, making word alignment tricky.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The ambiguity comes from the word "duck," which can be interpreted in different ways based on context, illustrating the challenge of disambiguation in translation.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_122 = {
    'question': (
        'Which of the following is true about sequence-to-sequence (seq2seq) models used in machine translation?'
    ),
    'options_list': [
        'A) The encoder takes in the target sentence and the decoder generates the source sentence.',
        'B) The decoder predicts the output tokens one at a time, conditioned on both the encoder output and the previous decoder tokens.',  # Correct answer
        'C) Seq2seq models always use beam search for decoding because greedy decoding does not work in machine translation.',
        'D) Seq2seq models cannot be trained using recurrent neural networks due to the complexity of the task.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The decoder generates tokens one at a time, conditioned on previous tokens and the entire encoded input sequence.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_123 = {
    'question': (
        'Which of the following is not a characteristic of beam search used in machine translation?'
    ),
    'options_list': [
        'A) Beam search maintains multiple hypotheses at each time step and expands them based on their probabilities.',
        'B) Increasing the beam size leads to more hypotheses being explored, which guarantees better results.',  # Correct answer
        'C) Beam search approximates the best target sentence because exact search is intractable.',
        'D) Beam size determines how many hypotheses are considered at each step of the decoding process.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Increasing beam size can improve results but does not guarantee better results, as it also increases computational cost.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_124 = {
    'question': (
        'What is the main purpose of using Byte Pair Encoding (BPE) in machine translation?'
    ),
    'options_list': [
        'A) To handle out-of-vocabulary words by splitting them into subword units.',  # Correct answer
        'B) To speed up training by reducing the total number of parameters in the model.',
        'C) To compress the translation model by removing unused characters from the vocabulary.',
        'D) To predict multiple words simultaneously during beam search.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'BPE breaks down rare or unseen words into subword units, allowing the model to generalize and handle out-of-vocabulary words more effectively.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_125 = {
    'question': (
        'Which of the following is not a strategy used to improve inference efficiency in neural machine translation?'
    ),
    'options_list': [
        'A) Using quantization to reduce the precision of computations from 32-bit floating point to 16-bit or 8-bit.',
        'B) Performing non-autoregressive machine translation, which predicts all tokens in the sequence simultaneously.',
        'C) Increasing the model depth by adding more layers to maximize computational efficiency.',  # Correct answer
        'D) Reducing the output vocabulary by sub-selecting from the most probable words based on the input sentence.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Increasing model depth (adding more layers) would typically slow down inference, as it increases the number of sequential computations.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_126 = {
    'question': (
        'True or False: In beam search, a larger beam size will always lead to a more accurate translation.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'A larger beam size can improve translation quality, but it also increases computational cost and does not always guarantee better accuracy.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_127 = {
    'question': (
        'True or False: Byte Pair Encoding (BPE) can help handle unseen words during translation by breaking them into smaller subword units.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'BPE splits words into more frequent subword units, which helps the model generalize to unseen or rare words.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_128 = {
    'question': (
        'True or False: One of the key bottlenecks in neural machine translation inference is the matrix multiplication involved in the output projection step, especially when the vocabulary size is large.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The output projection involves multiplying by a matrix of the size of the vocabulary, which can be computationally expensive when the vocabulary is large.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_129 = {
    'question': (
        'True or False: Non-autoregressive machine translation solves the efficiency problem by predicting all tokens in the target sequence at once, but it is still not state-of-the-art due to coordination challenges.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Non-autoregressive models are faster but face challenges in predicting sequences where the tokens need to coordinate well, so they are not yet state-of-the-art.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_130 = {
    'question': (
        'True or False: In the context of machine translation, the encoder in a seq2seq model generates a hidden representation of the source sentence, while the decoder uses this representation to generate the target sentence one token at a time.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The encoder generates a hidden representation, and the decoder uses this representation to generate the target sequence token by token.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_131 = {
    'question': (
        'Which of the following best captures the challenge in machine translation as mentioned by James?'
    ),
    'options_list': [
        'A) Machine translation is straightforward because all sentences have one canonical translation.',
        'B) Ambiguity in language can be resolved simply by applying beam search at every step of the translation.',
        'C) Languages have different structures, which means identical sentences in different languages always have corresponding function words.',
        'D) The challenge of translation is that one input sentence can have multiple possible translations with varying nuances.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Machine translation is difficult because the same sentence can have multiple correct translations depending on context, nuance, and structure. Beam search helps explore hypotheses but cannot resolve ambiguity itself.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_132 = {
    'question': (
        'True or False: Exact search in machine translation is computationally efficient due to the manageable number of possible output sentences.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Exact search is intractable because the number of possible output sentences grows exponentially with sequence length, making it computationally expensive.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_133 = {
    'question': (
        'Which of the following is most incorrect about beam search in machine translation?'
    ),
    'options_list': [
        'A) Beam search limits the number of hypotheses at each step by using a fixed beam size.',
        'B) The beam size determines how many possible translations are expanded at each decoding step.',
        'C) Beam search exhaustively considers every possible hypothesis for each token in the sequence.',  # Correct answer
        'D) Beam search is used to approximate the best target sentence due to the intractability of exact search.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Beam search does not exhaustively consider all hypotheses; it only explores the most likely sequences up to a fixed beam size.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_134 = {
    'question': (
        'True or False: In neural machine translation, auto-regressive generation refers to predicting multiple output tokens simultaneously, reducing the overall computational complexity.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Auto-regressive generation means predicting tokens one at a time, where each token depends on the previously predicted tokens.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_135 = {
    'question': (
        'Which of the following misconceptions about the sequence-to-sequence framework is most misleading?'
    ),
    'options_list': [
        'A) The encoder processes the entire source sentence to create an intermediate representation, which the decoder uses to predict each output token sequentially.',
        'B) The auto-regressive property of the decoder ensures that each predicted token depends only on the previously predicted token and the input sentence.',  # Correct answer
        'C) In sequence-to-sequence models, each token in the input sequence is projected directly into the output space without intermediate layers.',
        'D) The sequence-to-sequence model includes both an encoder that processes input tokens and a decoder that predicts output tokens one at a time.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The decoder not only depends on the previously predicted token and input but also on intermediate hidden states or embeddings produced by the encoder.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_136 = {
    'question': (
        'True or False: The causal self-attention mechanism in transformers processes all tokens in parallel, with no restriction on left-to-right dependencies in sequence generation.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'In transformers, causal self-attention ensures that tokens only attend to previous tokens in the sequence (left-to-right) when generating text.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_137 = {
    'question': (
        'Which of the following statements about subword vocabularies is most counterintuitive?'
    ),
    'options_list': [
        'A) Subword vocabularies break frequent words into their constituent characters to allow for more flexible modeling of rare words.',  # Correct answer
        'B) Subword vocabularies enable the model to generalize across unseen or rare words by decomposing them into smaller units.',
        'C) Subword vocabularies strike a balance between modeling frequent words as whole tokens and breaking up less frequent words into parts.',
        'D) Using subword vocabularies increases efficiency by reducing the size of the output space, despite the potential increase in sequence length for rare words.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Subword vocabularies generally preserve frequent words as full tokens, not break them into characters. Breaking into characters is done for rare or unseen words.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_138 = {
    'question': (
        'True or False: In neural machine translation, reducing the size of the output vocabulary always increases sequence length, thus negating the computational gains.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'While reducing the vocabulary size can increase sequence length, this does not always negate computational gains. The trade-off can still lead to efficiency improvements.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_139 = {
    'question': (
        'Which of the following is least relevant to improving inference efficiency in neural machine translation?'
    ),
    'options_list': [
        'A) Reducing the size of the output vocabulary through techniques like subword tokenization.',
        'B) Using layer drop to prune decoder layers during training, speeding up inference with minimal accuracy loss.',
        'C) Replacing the most frequent words with randomly assigned byte-pairs to ensure faster decoding.',  # Correct answer
        'D) Increasing the number of layers in the model to take full advantage of hardware acceleration like GPUs.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Byte-pair encoding does not randomly replace frequent words; it merges frequent character pairs into tokens to optimize vocabularies.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}

question_140 = {
    'question': (
        'Which of the following is not a limitation of non-autoregressive machine translation as compared to autoregressive models?'
    ),
    'options_list': [
        'A) Non-autoregressive models predict all tokens at once, making them less prone to sequential dependencies.',
        'B) Coordinating all predicted tokens simultaneously in non-autoregressive models poses challenges in ensuring coherent output.',
        'C) Non-autoregressive models require less computational time but are still not state-of-the-art due to difficulties in structured prediction.',
        'D) Non-autoregressive models outperform autoregressive models in all tasks, including those requiring high precision.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Non-autoregressive models are not better than autoregressive models in all tasks, particularly those requiring high precision. They still face difficulties in coherence.'
    ),
    'chapter_information': 'Chapter 15 - NMT Lectures'
}


uc_boulder_dl_attention_question_1 = {
    'question': (
        "In a transformer model with an input sequence length of 128 tokens, a model dimension of 512, "
        "and 8 attention heads, each attention head projects the input embeddings into matrices Q, K, and V with a reduced dimension. "
        "What would be the shape of the Q matrix for one head after the projection?"
    ),
    'options_list': ["Choose the correct shape for Q matrix"],
    'correct_answer': "[128, 64]",
    'explanation': (
        "Each head reduces the model dimension to 64 (512 / 8), while preserving the sequence length of 128, resulting in a Q matrix of shape [128, 64]."
    ),
    'chapter_information': 'multi-head self-attention. Shape Computation'
}

uc_boulder_dl_attention_question_2 = {
    'question': (
        "In the same transformer model with 8 attention heads, each head produces an output matrix of shape [128, 64] "
        "after applying attention weights to V. If we concatenate the outputs of all 8 heads, what would be the shape "
        "of the resulting concatenated matrix, commonly denoted as Z?"
    ),
    'options_list': ["Choose the correct shape for concatenated matrix Z"],
    'correct_answer': "[128, 512]",
    'explanation': (
        "After computing attention separately in each head, all 8 outputs of shape [128, 64] are concatenated along the last dimension, "
        "resulting in a final shape of [128, 512] for Z."
    ),
    'chapter_information': 'multi-head self-attention. Shape Computation'
}

uc_boulder_dl_attention_question_3 = {
    'question': (
        "After concatenating the outputs from the 8 heads in a transformer model, the matrix Z of shape [128, 512] "
        "is projected back to the original embedding dimension using a weight matrix \( W_O \) with shape [512, 512]. "
        "What would be the shape of the final output matrix Z after this projection back to the model dimension?"
    ),
    'options_list': ["Choose the correct shape for the final projected matrix Z"],
    'correct_answer': "[128, 512]",
    'explanation': (
        "The concatenated Z matrix of shape [128, 512] is projected back to the model dimension (512) using a weight matrix of shape [512, 512], "
        "maintaining the output shape at [128, 512]."
    ),
    'chapter_information': 'multi-head self-attention. Shape Computation'
}

uc_boulder_dl_attenti1on_question_1 = {
    'question': (
        "In an encoder self-attention layer of a transformer model, the input sequence has:\n"
        "- Sequence length (seq_len) = 128\n"
        "- Model dimension (d_model) = 512\n"
        "- Number of heads (h) = 8\n\n"
        "Each head projects the input embeddings into Q, K, and V matrices with a reduced dimension. "
        "Calculate the shape of each Q, K, and V matrix for one head in this encoder self-attention layer. "
        "Then, determine the shape of the final concatenated multi-head attention output before it passes through the final projection layer."
    ),
    'options_list': ["Choose the correct shapes for Q, K, V, and final concatenated output"],
    'correct_answer': (
        "Each Q, K, and V matrix for one head has shape: (128, 64). "
        "The final concatenated multi-head attention output has shape: (128, 512)."
    ),
    'explanation': (
        "Each head reduces the model dimension from 512 to 64 using learned projections (d_k = d_model / h = 512 / 8 = 64). "
        "Each head’s Q, K, and V matrices thus have shape (128, 64), where 128 is the sequence length, and 64 is the reduced dimension per head. "
        "After computing attention for each head, the 8 outputs are concatenated, resulting in a final shape of (128, 512) (128 tokens, each represented by 512 dimensions)."
    ),
    'chapter_information': 'Encoder Self-Attention Shape Calculation'
}

uc_boulder_dl_att1ention_question_2 = {
    'question': (
        "In a decoder self-attention layer during training, a causal mask is applied to prevent attending to future tokens in the sequence. Given:\n"
        "- Target sequence length (target_seq_len) = 64\n"
        "- Model dimension (d_model) = 512\n"
        "- Number of heads (h) = 8\n\n"
        "Calculate the shape of each QK^T matrix after computing scaled dot-product attention for one head, and explain why the mask needs to match this shape. "
        "What would be the shape of the multi-head attention output after concatenation across all heads?"
    ),
    'options_list': ["Choose the correct shapes for QK^T and final concatenated output"],
    'correct_answer': (
        "Shape of each QK^T matrix: (64, 64). "
        "Shape of the multi-head attention output after concatenation: (64, 512)."
    ),
    'explanation': (
        "Each head projects the target sequence into Q and K matrices of shape (64, 64). "
        "Computing QK^T results in a matrix of shape (64, 64), representing attention scores for each token in the target sequence relative to every other token. "
        "The causal mask, also of shape (64, 64), is applied to QK^T to ensure each token only attends to itself and past tokens, not future ones. "
        "After computing attention for all heads, the outputs are concatenated to form a final shape of (64, 512)."
    ),
    'chapter_information': 'Decoder Self-Attention with Masked Attention'
}

uc_boulder_dl_a1ttention_question_3 = {
    'question': (
        "In the encoder-decoder attention layer (cross-attention) of the decoder, the model attends to the encoder’s output while generating the target sequence. "
        "Given:\n"
        "- Encoder sequence length (encoder_seq_len) = 128\n"
        "- Target sequence length (target_seq_len) = 64\n"
        "- Model dimension (d_model) = 512\n"
        "- Number of heads (h) = 8\n\n"
        "Calculate the shapes of the Q, K, and V matrices in this cross-attention layer. Then, find the shape of the resulting QK^T matrix for one head "
        "and explain its dimensions in terms of the relationship between the target and encoder sequences."
    ),
    'options_list': ["Choose the correct shapes for Q, K, V, QK^T, and final concatenated output"],
    'correct_answer': (
        "Shape of Q for one head: (64, 64). "
        "Shape of K and V for one head: (128, 64). "
        "Shape of QK^T matrix for one head: (64, 128). "
        "Final concatenated multi-head attention output shape: (64, 512)."
    ),
    'explanation': (
        "In cross-attention, Q is derived from the target sequence, while K and V come from the encoder’s output. "
        "Each Q matrix has shape (64, 64) (target sequence length by head dimension). "
        "Each K and V matrix has shape (128, 64) (encoder sequence length by head dimension). "
        "Computing QK^T produces a matrix of shape (64, 128), indicating how each target token attends to every token in the encoder sequence. "
        "After softmax and applying attention to V, each head produces an output of shape (64, 64), and concatenating the heads yields a final shape of (64, 512)."
    ),
    'chapter_information': 'Cross-Attention (Encoder-Decoder Attention) Shape Calculation'
}

uc_boulder_dl_attention_question_4 = {
    'question': (
        "In an encoder self-attention layer, we have:\n"
        "- Model dimension (d_model) = 512\n"
        "- Number of heads (h) = 8\n\n"
        "Each head has separate learned weight matrices for Q, K, and V of shape (512, 64). "
        "Calculate the total number of parameters required for Q, K, and V projections across all heads."
    ),
    'options_list': ["Calculate the total parameters for Q, K, and V projections"],
    'correct_answer': "Total parameters for Q, K, and V projections = 98,304",
    'explanation': (
        "Each head has three projection matrices: W_Q, W_K, and W_V, each with shape (512, 64). "
        "Each matrix contains 512 × 64 = 32,768 parameters. "
        "For 8 heads, the total number of parameters is 32,768 × 3 × 8 = 98,304."
    ),
    'chapter_information': 'Self-Attention Parameter Count'
}

uc_boulder_dl_attention_question_5 = {
    'question': (
        "In a multi-head attention layer, we concatenate the outputs of each head before passing it through a final linear projection. "
        "If each head produces an output of shape (128, 64) and the sequence length is 128 tokens, what will be the shape of the concatenated output across all heads?"
    ),
    'options_list': ["Determine the shape of the concatenated output"],
    'correct_answer': "Shape of the concatenated output across all heads = (128, 512)",
    'explanation': (
        "Each head’s output is (128, 64). Concatenating 8 heads along the last dimension gives 128 × (64 × 8) = (128, 512). "
        "This concatenated output combines information from all heads before being passed through a linear projection layer."
    ),
    'chapter_information': 'Multi-Head Attention Concatenation Shape Verification'
}

uc_boulder_dl_attention_question_6 = {
    'question': (
        "After concatenating the outputs of all heads in a multi-head attention layer, we pass the result through a final linear projection. "
        "If the concatenated output has shape (128, 512) and the linear projection weight matrix has shape (512, 512), "
        "calculate the total number of parameters in this linear projection layer."
    ),
    'options_list': ["Calculate the total parameters in the final linear projection"],
    'correct_answer': "Total parameters in the final linear projection layer = 262,144",
    'explanation': (
        "The linear projection weight matrix has shape (512, 512), so it has 512 × 512 = 262,144 parameters. "
        "This projection maps the multi-head attention output back to the original model dimension, d_model = 512."
    ),
    'chapter_information': 'Final Linear Projection in Multi-Head Attention'
}

uc_boulder_dl_attention_question_7 = {
    'question': (
        "In an encoder-decoder attention (cross-attention) layer, the model attends to the encoder’s output while generating the target sequence. Given:\n"
        "- Encoder sequence length (encoder_seq_len) = 100\n"
        "- Target sequence length (target_seq_len) = 50\n"
        "- Model dimension (d_model) = 512\n"
        "- Number of heads (h) = 8\n\n"
        "Calculate the shape of the QK^T matrix for one head."
    ),
    'options_list': ["Determine the shape of the QK^T matrix for one head"],
    'correct_answer': "Shape of QK^T matrix for one head = (50, 100)",
    'explanation': (
        "In cross-attention, Q is derived from the target sequence and has shape (50, 64) for one head. "
        "K is derived from the encoder sequence and has shape (100, 64). "
        "QK^T results in shape (50, 64) × (64, 100) = (50, 100), showing how each target token attends to all encoder tokens."
    ),
    'chapter_information': 'Cross-Attention QK^T Shape with Different Sequence Lengths'
}

uc_boulder_dl_attention_question_8 = {
    'question': (
        "In a transformer layer with a model dimension (d_model) of 512, layer normalization is applied after the multi-head attention and feed-forward layers. "
        "Calculate the total number of parameters in one layer normalization operation."
    ),
    'options_list': ["Calculate the total parameters for one layer normalization operation"],
    'correct_answer': "Total parameters for one layer normalization = 1,024",
    'explanation': (
        "Layer normalization includes two sets of parameters: a scaling parameter (gamma) and an offset parameter (beta), both of shape (d_model). "
        "With d_model = 512, each parameter set has 512 values, totaling 512 × 2 = 1,024 parameters for one layer normalization."
    ),
    'chapter_information': 'Layer Normalization Parameter Count'
}

uc_boulder_dl_attention_question_9 = {
    'question': (
        "In a self-attention layer with:\n"
        "- Batch size = 32\n"
        "- Sequence length (seq_len) = 128\n"
        "- Number of heads (h) = 8\n"
        "- Model dimension (d_model) = 512\n\n"
        "Each head computes QK^T to produce the attention scores. Calculate the total shape of QK^T across all heads and batches."
    ),
    'options_list': ["Determine the shape of QK^T across all heads and batches"],
    'correct_answer': "Shape of QK^T across all heads and batches = (32, 8, 128, 128)",
    'explanation': (
        "For one head, QK^T has shape (128, 128). Across 8 heads, the shape is (8, 128, 128). "
        "Including the batch dimension of 32, the final shape becomes (32, 8, 128, 128), where each batch has 8 heads producing an attention score matrix for each token pair in the sequence."
    ),
    'chapter_information': 'Attention Scores Calculation for One Batch'
}

uc_boulder_dl_attention_question_10 = {
    'question': (
        "In a transformer’s feed-forward network, each layer consists of two linear transformations with a ReLU activation in between. If:\n"
        "- Model dimension (d_model) = 512\n"
        "- Inner layer dimension = 2,048\n\n"
        "Calculate the total number of parameters in this feed-forward network layer."
    ),
    'options_list': ["Calculate the total parameters in the feed-forward network layer"],
    'correct_answer': "Total parameters = 2,621,440",
    'explanation': (
        "The feed-forward network consists of:\n"
        "1. A linear transformation from 512 → 2,048, with 512 × 2,048 = 1,048,576 weights plus 2,048 biases.\n"
        "2. A second linear transformation from 2,048 → 512, with 2,048 × 512 = 1,048,576 weights plus 512 biases.\n"
        "Total parameters: 1,048,576 + 2,048 + 1,048,576 + 512 = 2,099,712 + 521,728 = 2,621,440."
    ),
    'chapter_information': 'Feed-Forward Network Parameter Calculation'
}

uc_boulder_dl_attention_question_11 = {
    'question': (
        "In a decoder self-attention layer, given:\n"
        "- Target sequence length (target_seq_len) = 100\n"
        "- Model dimension (d_model) = 512\n"
        "- Number of heads (h) = 8\n\n"
        "What is the shape of the final output of the multi-head attention layer after concatenation and projection, and why does this shape remain consistent with the input?"
    ),
    'options_list': ["Determine the shape of the final output after concatenation and projection"],
    'correct_answer': "Shape of the final output after concatenation and projection = (100, 512)",
    'explanation': (
        "Each head’s output shape is (100, 64), where 64 is the per-head dimension (d_k = 64). "
        "Concatenating all 8 heads gives (100, 512). This concatenated output is projected back to d_model = 512, "
        "so the shape remains (100, 512), matching the input dimension, which ensures compatibility with subsequent layers in the transformer model."
    ),
    'chapter_information': 'Final Output of Multi-Head Attention in Decoder Self-Attention'
}


KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_15_MPC = KC_MPC_QUESTIONS[:-1]
