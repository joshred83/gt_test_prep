

question_1 = {
    'question': (
        'Which of the following is not a limitation of standard unidirectional language models mentioned in BERT’s introduction?'
    ),
    'options_list': [
        'A) They restrict context understanding to a single direction in the sentence.',
        'B) They prevent the use of task-specific architectures.',  # Correct answer
        'C) They impose constraints on bidirectional information fusion.',
        'D) They limit the effectiveness of fine-tuning approaches in NLP tasks.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Option B is not a limitation mentioned in the paper. Unidirectional models do not prevent the use of task-specific architectures; they may, however, necessitate them.'
    ),
    'chapter_information': 'BERT Paper'
}

question_3 = {
    'question': (
        'When describing pre-trained word embeddings in BERT’s related work, which of the following did not directly improve NLP benchmarks prior to BERT’s development?'
    ),
    'options_list': [
        'A) Using shallow concatenation of left-to-right and right-to-left LMs.',
        'B) Pre-training word embeddings to initialize token representations.',
        'C) Sentence embeddings using denoising autoencoder objectives.',
        'D) Employing task-specific architectures for robust text generation models.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Option D is less directly associated with improving benchmarks through pre-training, as BERT did.'
    ),
    'chapter_information': 'BERT Paper'
}

question_4 = {
    'question': (
        'Which of the following best describes BERT’s pre-training objectives, and why does this matter for sentence-level and token-level tasks?'
    ),
    'options_list': [
        'A) Next Sentence Prediction; it helps in capturing inter-sentence coherence, critical for sentence-level tasks.',
        'B) Masked Language Model; it allows context-independent token prediction, suitable for token-level tasks.',
        'C) Masked Language Model; it enables bidirectional context fusion, beneficial for both sentence-level and token-level tasks.',  # Correct answer
        'D) Next Sentence Prediction; it focuses on sentence-to-token context, optimizing cross-sentence coherence.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C accurately describes the MLM objective, supporting bidirectional context fusion, which benefits both sentence-level and token-level tasks.'
    ),
    'chapter_information': 'BERT Paper'
}

question_5 = {
    'question': (
        'True or False: ELMo, as a feature-based approach, focuses on generating deep bidirectional representations similar to BERT, thereby eliminating the need for fine-tuning during downstream tasks.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'ELMo generates contextualized embeddings by concatenating left-to-right and right-to-left LMs, resulting in shallow bidirectional representations, and does not eliminate the need for fine-tuning.'
    ),
    'chapter_information': 'BERT Paper'
}

question_6 = {
    'question': (
        'Which is the least likely reason BERT outperforms previous models on tasks like SQuAD and MultiNLI?'
    ),
    'options_list': [
        'A) BERT’s reliance on a fine-tuning approach using left-to-right only attention.',  # Correct answer
        'B) BERT’s use of bidirectional context representations via the masked language model objective.',
        'C) BERT’s architectural simplicity compared to task-specific designs.',
        'D) BERT’s ability to integrate contextual embeddings in a pre-trained, transferable format.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'BERT does not rely on left-to-right only attention; it uses bidirectional attention. Therefore, this is the least likely reason for its superior performance.'
    ),
    'chapter_information': 'BERT Paper'
}

question_7 = {
    'question': (
        'Select the correct sequence that highlights a distinct advantage of BERT over OpenAI GPT as mentioned in the paper.'
    ),
    'options_list': [
        'A) OpenAI GPT → unidirectional → bidirectional → BERT enables multi-directional context in sentence tasks.',  # Correct answer
        'B) BERT → unidirectional → left-to-right architecture → OpenAI GPT extends this with bidirectional models.',
        'C) BERT → restricts context → OpenAI GPT resolves this by adding task-specific architectural layers.',
        'D) OpenAI GPT → bidirectional embedding concatenation → BERT omits this approach in fine-tuning.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Option A correctly outlines that OpenAI GPT is unidirectional and BERT is bidirectional, providing an advantage in capturing context.'
    ),
    'chapter_information': 'BERT Paper'
}

question_8 = {
    'question': (
        'True or False: Pre-training objectives used in BERT strictly adhere to unsupervised feature-based objectives without introducing sentence-ranking strategies.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'BERT’s next sentence prediction (NSP) objective introduces a form of sentence-ranking strategy, predicting whether one sentence follows another.'
    ),
    'chapter_information': 'BERT Paper'
}

question_9 = {
    'question': (
        'According to the BERT paper, Which of the following accurately captures BERT’s approach to overcoming left-to-right constraints, according to the paper?'
    ),
    'options_list': [
        'A) It uses supervised objectives derived from sentence concatenation to predict token sequences.',
        'B) By introducing multiple bidirectional language models, it resolves context limitations.',
        'C) Through masked tokens, BERT’s MLM enables bi-directional conditioning across all Transformer layers.',  # Correct answer
        'D) It introduces task-specific layers, allowing each layer to incorporate cross-sentence information.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Option C correctly describes how BERT uses the masked language model objective to achieve bidirectional conditioning.'
    ),
    'chapter_information': 'BERT Paper'
}

question_10 = {
    'question': (
        'Which of the following statements about BERT is FALSE?'
    ),
    'options_list': [
        'A) BERT pre-trains deep bidirectional representations by conditioning on both left and right context.',
        'B) BERT can be fine-tuned with only a single additional output layer for various tasks without changing the architecture.',
        'C) Unlike ELMo, BERT relies on a unidirectional left-to-right training objective.',  # Correct answer
        'D) BERT’s training objectives include both masked language modeling and next sentence prediction.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Unlike ELMo, BERT is trained with a bidirectional objective, unlike left-to-right models.'
    ),
    'chapter_information': 'BERT Paper'
}

question_11 = {
    'question': (
        'What problem does the masked language model (MLM) in BERT aim to solve?'
    ),
    'options_list': [
        'A) The issue of limited context by fusing only left-to-right information.',
        'B) The unidirectionality of standard language models by fusing left and right contexts.',  # Correct answer
        'C) The lack of task-specific architectures in downstream tasks.',
        'D) The restriction on sentence-level tasks in feature-based approaches.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'MLM allows the model to fuse information from both directions, overcoming unidirectionality.'
    ),
    'chapter_information': 'BERT Paper'
}

question_12 = {
    'question': (
        'In the context of BERT, what role does the next sentence prediction (NSP) objective serve?'
    ),
    'options_list': [
        'A) It allows BERT to understand relationships between sentences in a pair.',  # Correct answer
        'B) It primarily enhances BERT’s token-level accuracy.',
        'C) It improves the model’s intrinsic evaluation metrics.',
        'D) It increases the training speed of the MLM objective.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'NSP helps BERT capture sentence-pair relationships, useful for tasks like question answering and inference.'
    ),
    'chapter_information': 'BERT Paper'
}

question_14 = {
    'question': (
        'What is the primary benefit of using BERT over feature-based language models like ELMo?'
    ),
    'options_list': [
        'A) BERT is trained on both labeled and unlabeled data.',
        'B) BERT requires only a single additional output layer for fine-tuning on various tasks.',  # Correct answer
        'C) BERT uses multiple task-specific architectures for downstream tasks.',
        'D) BERT can only be applied to token-level tasks.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'BERT is designed for simplicity in fine-tuning, requiring only one additional layer.'
    ),
    'chapter_information': 'BERT Paper'
}


question_16 = {
    'question': (
        'True or False: The primary purpose of BERT’s [CLS] token is for separating sentence pairs in pre-training.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'The [CLS] token is used as an aggregate sequence representation for classification tasks.'
    ),
    'chapter_information': 'BERT Paper'
}

question_17 = {
    'question': (
        'True or False: In BERT, the masked language model objective enables pre-training that captures deep bidirectional context by masking some tokens and training the model to predict them.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'This objective allows BERT to capture context from both directions around masked tokens.'
    ),
    'chapter_information': 'BERT Paper'
}

question_18 = {
    'question': (
        'True or False: BERT does not require labeled data during its initial pre-training phase.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'BERT is pre-trained on unlabeled text using the MLM and NSP objectives.'
    ),
    'chapter_information': 'BERT Paper'
}

question_21 = {
    'question': (
        'Which of the following statements about BERT is FALSE?'
    ),
    'options_list': [
        'A) BERT pre-trains deep bidirectional representations by conditioning on both left and right context.',
        'B) BERT can be fine-tuned with only a single additional output layer for various tasks without changing the architecture.',
        'C) Unlike ELMo, BERT relies on a unidirectional left-to-right training objective.',  # Correct answer
        'D) BERT’s training objectives include both masked language modeling and next sentence prediction.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Unlike ELMo, BERT is trained with a bidirectional objective, not a unidirectional one.'
    ),
    'chapter_information': 'BERT Paper'
}

question_22 = {
    'question': (
        'What problem does the masked language model (MLM) in BERT aim to solve?'
    ),
    'options_list': [
        'A) The issue of limited context by fusing only left-to-right information.',
        'B) The unidirectionality of standard language models by fusing left and right contexts.',  # Correct answer
        'C) The lack of task-specific architectures in downstream tasks.',
        'D) The restriction on sentence-level tasks in feature-based approaches.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'MLM allows the model to fuse information from both directions, overcoming unidirectionality.'
    ),
    'chapter_information': 'BERT Paper'
}

question_23 = {
    'question': (
        'In the context of BERT, what role does the next sentence prediction (NSP) objective serve?'
    ),
    'options_list': [
        'A) It allows BERT to understand relationships between sentences in a pair.',  # Correct answer
        'B) It primarily enhances BERT’s token-level accuracy.',
        'C) It improves the model’s intrinsic evaluation metrics.',
        'D) It increases the training speed of the MLM objective.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'NSP helps BERT capture sentence-pair relationships, useful for tasks like question answering and inference.'
    ),
    'chapter_information': 'BERT Paper'
}

question_25 = {
    'question': (
        'Which of the following best describes BERT’s pre-training objectives, and why does this matter for sentence-level and token-level tasks?'
    ),
    'options_list': [
        'A) Next Sentence Prediction; it helps in capturing inter-sentence coherence, critical for sentence-level tasks.',
        'B) Masked Language Model; it allows context-independent token prediction, suitable for token-level tasks.',
        'C) Masked Language Model; it enables bidirectional context fusion, beneficial for both sentence-level and token-level tasks.',  # Correct answer
        'D) Next Sentence Prediction; it focuses on sentence-to-token context, optimizing cross-sentence coherence.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'MLM enables bidirectional context fusion, aiding both sentence-level and token-level tasks.'
    ),
    'chapter_information': 'BERT Paper'
}

question_26 = {
    'question': (
        'Which of the following accurately captures BERT’s approach to overcoming left-to-right constraints, according to the paper?'
    ),
    'options_list': [
        'A) It uses supervised objectives derived from sentence concatenation to predict token sequences.',
        'B) By introducing multiple bidirectional language models, it resolves context limitations.',
        'C) Through masked tokens, BERT’s MLM enables bidirectional conditioning across all Transformer layers.',  # Correct answer
        'D) It introduces task-specific layers, allowing each layer to incorporate cross-sentence information.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Masked tokens allow BERT to condition on both left and right context simultaneously.'
    ),
    'chapter_information': 'BERT Paper'
}

question_27 = {
    'question': (
        'Which of the following statements about BERT’s training objectives is FALSE?'
    ),
    'options_list': [
        'A) The masked language model (MLM) task requires BERT to predict randomly masked tokens in the input sequence.',
        'B) The next sentence prediction (NSP) task involves predicting whether one sentence follows another in context.',
        'C) During pre-training, BERT uses both the [MASK] token and random tokens to replace masked words.',
        'D) BERT only uses the MLM objective, which is sufficient for sentence-pair understanding tasks.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'BERT uses both MLM and NSP tasks; NSP is crucial for sentence-pair understanding.'
    ),
    'chapter_information': 'BERT Paper'
}

question_28 = {
    'question': (
        'Which of the following BEST describes the purpose of the [CLS] token in BERT’s architecture?'
    ),
    'options_list': [
        'A) It serves as a token separator for multi-sentence inputs.',
        'B) It aggregates information from all tokens in the sequence, primarily for classification tasks.',  # Correct answer
        'C) It is a placeholder for masked tokens in the MLM objective.',
        'D) It is used exclusively during pre-training and not fine-tuning.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The [CLS] token acts as an aggregate representation for classification tasks.'
    ),
    'chapter_information': 'BERT Paper'
}

question_29 = {
    'question': (
        'Which of the following is TRUE regarding BERT’s approach to fine-tuning?'
    ),
    'options_list': [
        'A) BERT requires specific task-dependent architectures for each downstream task.',
        'B) BERT’s architecture is modified for each downstream task during fine-tuning.',
        'C) BERT requires no additional parameters when fine-tuning for different tasks.',
        'D) BERT fine-tunes all parameters, allowing it to perform well across diverse tasks with minimal modifications.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'BERT fine-tunes all parameters, adapting to various tasks with minimal changes.'
    ),
    'chapter_information': 'BERT Paper'
}

question_33 = {
    'question': (
        'Which of the following statements about BERT’s fine-tuning on the GLUE benchmark is TRUE?'
    ),
    'options_list': [
        'A) BERT fine-tuning requires task-specific architectures for each GLUE dataset.',
        'B) BERT uses the [SEP] token to aggregate all sentence representations for classification.',
        'C) Only classification layer weights are introduced as new parameters during fine-tuning.',  # Correct answer
        'D) BERT’s GLUE performance closely matches that of BiLSTM+ELMo+Attn on all tasks.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Only classification layer weights are introduced as new parameters for fine-tuning BERT.'
    ),
    'chapter_information': 'BERT Paper'
}

question_34 = {
    'question': (
        'During fine-tuning for the SQuAD v1.1 dataset, which of the following parameters are introduced in addition to the pre-trained BERT model?'
    ),
    'options_list': [
        'A) Position and segment embeddings for the passage.',
        'B) Separate start and end vectors for answer span predictions.',  # Correct answer
        'C) A CRF layer to model dependencies between start and end positions.',
        'D) An additional transformer layer to handle long passages.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Separate start and end vectors are used to predict the answer span within the passage.'
    ),
    'chapter_information': 'BERT Paper'
}

question_35 = {
    'question': (
        'Which of the following most accurately describes the purpose of the "LTR & No NSP" ablation model in BERT’s experiments?'
    ),
    'options_list': [
        'A) To test the performance of BERT with both left-to-right and right-to-left context.',
        'B) To evaluate a model trained without next sentence prediction (NSP) but with bidirectional context.',
        'C) To simulate the performance of a unidirectional left-to-right model like OpenAI GPT.',  # Correct answer
        'D) To demonstrate the impact of bidirectional transformers without the MLM objective.'
    ],
    'correct_answer': 'C',
    'explanation': (
        '"LTR & No NSP" simulates a unidirectional left-to-right model similar to OpenAI GPT.'
    ),
    'chapter_information': 'BERT Paper'
}

question_36 = {
    'question': (
        'According to BERT’s ablation experiments, which of the following statements is TRUE regarding the model size?'
    ),
    'options_list': [
        'A) Increasing the number of layers improves performance on large datasets but degrades small dataset accuracy.',
        'B) Larger models significantly outperform smaller ones, even on small datasets like MRPC.',  # Correct answer
        'C) Increasing the hidden size beyond 1024 reduces accuracy due to overfitting.',
        'D) A model with fewer than 12 layers has higher accuracy on MRPC than BERT_BASE.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Larger models outperform smaller ones on both large and small datasets, including MRPC.'
    ),
    'chapter_information': 'BERT Paper'
}

question_37 = {
    'question': (
        'Which of the following statements incorrectly describes the BERT fine-tuning process for the GLUE benchmark?'
    ),
    'options_list': [
        'A) The [CLS] token’s final hidden vector is used as the aggregate representation.',
        'B) The only new parameters introduced are the classification layer weights.',
        'C) BERT’s architecture relies heavily on additional layers tailored to each GLUE task.',  # Correct answer
        'D) A standard classification loss is computed using the [CLS] token and classification weights.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'BERT does not rely on task-specific architectures; it uses the same architecture with minimal modifications.'
    ),
    'chapter_information': 'BERT Paper'
}

question_38 = {
    'question': (
        'Which of the following reflects the BERT_LARGE model’s leaderboard performance across different datasets and why?'
    ),
    'options_list': [
        'A) BERT_LARGE performs identically to OpenAI GPT in structure but leverages smaller datasets for lower computation.',
        'B) BERT_LARGE shows a significant improvement due to its attention masking strategy similar to OpenAI GPT.',
        'C) BERT_LARGE achieves top scores by relying exclusively on left-to-right constraints, avoiding bidirectional layers.',
        'D) BERT_LARGE exceeds prior results in tasks like MNLI due to the removal of single-direction context limitations.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'BERT_LARGE achieves superior performance by leveraging bidirectional context.'
    ),
    'chapter_information': 'BERT Paper'
}


# True/False Questions

question_41 = {
    'question': (
        'True or False: Ablation studies show that removing the next sentence prediction (NSP) task significantly reduces BERT’s performance on QNLI, MNLI, and SQuAD tasks.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Removing NSP leads to performance drops in tasks requiring understanding of sentence relationships. \
            (non-GPT - they say so in the paper, but the actual difference seems to be just a few basis points)'
    ),
    'chapter_information': 'BERT Paper'
}

question_42 = {
    'question': (
        'True or False: In the SQuAD v2.0 task, BERT uses the [CLS] token to predict if a question has no answer in the passage.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The [CLS] token represents the "no answer" option in SQuAD v2.0. (maybe not super relevant)'
    ),
    'chapter_information': 'BERT Paper'
}

questioden_1 = {
    'question': (
        'Which of the following is TRUE about the Transformer architecture?'
    ),
    'options_list': [
        'A) It combines both recurrent and convolutional neural networks to achieve high parallelization.',
        'B) It uses self-attention to draw global dependencies in both the encoder and decoder layers.',  # Correct answer
        'C) The Transformer requires recurrence to maintain the sequence order.',
        'D) The Transformer uses additive attention exclusively in all attention mechanisms.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The Transformer architecture relies on self-attention for handling dependencies across the entire sequence, without recurrence or convolution.'
    ),
    'chapter_information': 'Attention is All You Need'
}

questioden_2 = {
    'question': (
        'Which of the following statements about positional encoding in the Transformer is FALSE?'
    ),
    'options_list': [
        'A) Positional encoding uses sine and cosine functions with different frequencies.',
        'B) It is designed to incorporate the order of tokens in the sequence since the Transformer lacks recurrence.',
        'C) Positional encoding values are learned during the training process to adapt to sequence length.',  # Correct answer
        'D) Each dimension of positional encoding corresponds to a different sinusoidal wavelength.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Positional encodings in the Transformer are fixed using sine and cosine functions and are not learned.'
    ),
    'chapter_information': 'Attention is All You Need'
}

questioden_3 = {
    'question': (
        'What is the purpose of the scaling factor $1/√(d_k)$ in Scaled Dot-Product Attention?'
    ),
    'options_list': [
        'A) To increase the dot product values for larger dimensions, enhancing gradients.',
        'B) To reduce the dot product values for larger dimensions, preventing small gradients in softmax.',  # Correct answer
        'C) To normalize the query and key matrices for consistency across attention heads.',
        'D) To enable the model to attend across multiple input sequences simultaneously.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The scaling factor prevents the dot products from becoming too large, which could push the softmax function into regions with small gradients.'
    ),
    'chapter_information': 'Attention is All You Need'
}

questioden_4 = {
    'question': (
        'Which best describes the purpose of multi-head attention in the Transformer model?'
    ),
    'options_list': [
        'A) It allows the model to capture different aspects of the input sequence by focusing on various subspaces.',  # Correct answer
        'B) It improves training efficiency by reducing the number of operations required.',
        'C) It sequentially processes each head’s attention to provide a more comprehensive summary.',
        'D) It restricts attention to local areas of the sequence to reduce computation.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Multi-head attention enables the model to capture diverse representations by focusing on different parts of the sequence in parallel.'
    ),
    'chapter_information': 'Attention is All You Need'
}

questideon_5 = {
    'question': (
        'In the Transformer model, which layer configuration is unique to the decoder but not the encoder?'
    ),
    'options_list': [
        'A) Self-attention sub-layer',
        'B) Feed-forward network',
        'C) Encoder-decoder attention sub-layer',  # Correct answer
        'D) Positional encoding'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The encoder-decoder attention sub-layer is specific to the decoder, allowing it to attend to the encoder’s outputs.'
    ),
    'chapter_information': 'Attention is All You Need'
}

questionde_6 = {
    'question': (
        'Which of the following correctly describes how self-attention in the Transformer model impacts computational efficiency compared to prior RNN and CNN approaches?'
    ),
    'options_list': [
        'A) It reduces the number of sequential operations and allows for constant time complexity per layer.',  # Correct answer
        'B) It introduces an overhead due to masking requirements but speeds up computation on shorter sequences.',
        'C) It achieves logarithmic complexity per layer by learning dependencies via recursive connections.',
        'D) It depends on kernel size adjustments in attention, which restricts computational efficiency on long sequences.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Self-attention reduces sequential operations, enabling parallel computation and constant time complexity per layer.'
    ),
    'chapter_information': 'Attention is All You Need'
}

questioden_8 = {
    'question': (
        'Which of the following is NOT a role of positional encodings in the Transformer model?'
    ),
    'options_list': [
        'A) Enabling the model to capture information about the order of tokens within sequences.',
        'B) Allowing the model to extrapolate to longer sequences than those seen in training.',
        'C) Replacing the need for embeddings by directly encoding token relationships.',  # Correct answer
        'D) Providing fixed or learned frequency-based values added to embeddings.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Positional encodings do not replace embeddings but are added to them to encode positional information.'
    ),
    'chapter_information': 'Attention is All You Need'
}

quedestion_9 = {
    'question': (
        'Which type of attention mechanism in the Transformer is specifically designed to allow the decoder to access encoder outputs across all input positions?'
    ),
    'options_list': [
        'A) Masked attention',
        'B) Encoder-decoder attention',  # Correct answer
        'C) Self-attention in decoder layers',
        'D) Multi-head positional attention'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Encoder-decoder attention enables the decoder to attend to the encoder’s output.'
    ),
    'chapter_information': 'Attention is All You Need'
}

qdeuestion_10 = {
    'question': (
        'What function does the feed-forward layer serve in each layer of the encoder and decoder stacks in the Transformer?'
    ),
    'options_list': [
        'A) It captures global dependencies in sequence positions through recurrent layers.',
        'B) It applies nonlinear transformations uniformly across sequence positions.',  # Correct answer
        'C) It normalizes attention heads to ensure balanced gradient flows.',
        'D) It aligns the input and output embedding spaces for smoother model convergence.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The feed-forward layer applies position-wise nonlinear transformations to each token independently.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_100 = {
    'question': (
        'Which of the following is NOT an advantage of self-attention over recurrent or convolutional layers?'
    ),
    'options_list': [
        'A) Constant number of sequential operations required.',
        'B) Improved ability to learn long-range dependencies with short paths.',
        'C) Lower computational complexity for all sequence lengths.',  # Correct answer
        'D) Increased parallelization due to lack of sequential dependency.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Self-attention has lower complexity than recurrent layers but may be less efficient than convolutional layers for very long sequences.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_101 = {
    'question': (
        'In the Transformer model, what is the primary purpose of scaling the dot product in the Scaled Dot-Product Attention by 1/√(d_k)?'
    ),
    'options_list': [
        'A) To normalize the output values to a consistent range across layers.',
        'B) To prevent softmax gradients from vanishing for large dimensions.',  # Correct answer
        'C) To align key and query dimensions to improve attention accuracy.',
        'D) To increase the range of values in attention scores for better distinctiveness.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The scaling factor prevents large magnitudes in the dot product, which would otherwise push the softmax function into regions with small gradients.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_102 = {
    'question': (
        'How does the Transformer handle positional information, given that it lacks recurrence and convolution?'
    ),
    'options_list': [
        'A) By using positional embeddings learned during training.',
        'B) By adding fixed sinusoidal positional encodings to token embeddings.',  # Correct answer
        'C) By modifying the attention mechanism to incorporate token positions.',
        'D) By relying on multi-head attention layers to infer position from context.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The Transformer uses sinusoidal positional encodings to add positional information directly to the embeddings.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_103 = {
    'question': (
        'Which of the following correctly describes how self-attention mechanisms in the Transformer help with long-range dependencies?'
    ),
    'options_list': [
        'A) Self-attention limits path length between tokens, facilitating global dependency learning.',  # Correct answer
        'B) Self-attention uses recurrent connections to maintain dependencies across distant tokens.',
        'C) Self-attention introduces sequential computations to preserve context across time steps.',
        'D) Self-attention layers rely on kernel-based local connections to capture dependencies.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Self-attention allows shorter path lengths between tokens, enabling efficient learning of long-range dependencies.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_104 = {
    'question': (
        'In the Transformer, what effect does label smoothing have during training?'
    ),
    'options_list': [
        'A) It encourages higher confidence predictions by narrowing the probability distribution.',
        'B) It reduces overfitting by adding noise to labels and improves generalization.',  # Correct answer
        'C) It modifies embeddings to learn smooth transitions between classes.',
        'D) It penalizes lower probabilities for incorrect answers, reinforcing the highest probabilities.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Label smoothing discourages overconfidence by adding noise to labels, thus improving generalization.'
    ),
    'chapter_information': 'Attention is All You Need'
}

# True/False Questions

question_105 = {
    'question': (
        'True or False: Self-attention layers have a constant path length between any two tokens, unlike recurrent and convolutional layers, making them more effective at learning long-range dependencies.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Self-attention enables direct connections between all tokens in a single layer.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_106 = {
    'question': (
        'True or False: For long sequences, the computational complexity of self-attention is lower than that of convolutional layers with a kernel width equal to the sequence length.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Self-attention has lower complexity when convolutional layers require large kernels to cover the sequence.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_107 = {
    'question': (
        'True or False: During training, label smoothing is used to improve BLEU scores by encouraging the model to be more uncertain in its predictions.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Label smoothing prevents the model from becoming overconfident, which can enhance performance metrics like BLEU.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_108 = {
    'question': (
        'True or False: The primary purpose of the warm-up steps in the learning rate schedule is to gradually increase the learning rate for the initial steps before decaying.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'This helps stabilize training and avoid issues with large initial gradients.'
    ),
    'chapter_information': 'Attention is All You Need'
}

question_109 = {
    'question': (
        'True or False: The motivation for using sinusoidal positional encoding in the Transformer model, compared to learned positional embeddings, is that sinusoidal encoding adapts more readily to sequence lengths unseen during training.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Sinusoidal functions allow the model to extrapolate to longer sequences.'
    ),
    'chapter_information': 'Attention is All You Need'
}
#######################
question_200 = {
    'question': (
        'What is the primary objective of StarSpace as a neural embedding model?'
    ),
    'options_list': [
        'A) To provide a model focused solely on text classification.',
        'B) To create embeddings that work only within single-task settings.',
        'C) To embed a wide range of entities into a common space for tasks like classification, ranking, and recommendation.',  # Correct answer
        'D) To use recurrent neural networks to improve classification results.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'StarSpace embeds various types of entities into a common space, enabling it to handle a range of tasks, including classification, ranking, and recommendation.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_201 = {
    'question': (
        'In StarSpace, what role does the similarity function play?'
    ),
    'options_list': [
        'A) It generates embeddings for new entities in the test set.',
        'B) It defines how entities are compared in embedding space, influencing tasks like ranking and classification.',  # Correct answer
        'C) It ensures that all embeddings lie within a fixed radius in the embedding space.',
        'D) It computes the loss function by sampling negative pairs.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The similarity function in StarSpace is used to compare embeddings of entities, which is central to tasks like ranking and classification.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_202 = {
    'question': (
        'Which of the following describes a key feature of StarSpace’s approach to collaborative filtering with out-of-sample users?'
    ),
    'options_list': [
        'A) It creates embeddings for new users based on their IDs.',
        'B) It uses a fixed set of items to estimate preferences of new users.',
        'C) It represents a user by the embeddings of items they like, allowing for new users without predefined embeddings.',  # Correct answer
        'D) It requires pre-trained embeddings for all users and items in the dataset.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'StarSpace represents users by the sum of the embeddings of items they like, enabling it to handle new users who were not part of the training set.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_204 = {
    'question': (
        'In StarSpace, how is sentence similarity learned when training sentence embeddings?'
    ),
    'options_list': [
        'A) By predicting a middle word within a sentence based on surrounding words.',
        'B) By creating embeddings of words first and then summing them to form sentence embeddings.',
        'C) By sampling sentence pairs from the same document as positive pairs and from different documents as negative pairs.',  # Correct answer
        'D) By clustering sentences based on topic and training within clusters.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Sentence similarity is learned by using sentence pairs from the same document as positive pairs and from different documents as negative pairs.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_205 = {
    'question': (
        'What role do negative entities (b-) play during training in the StarSpace model?'
    ),
    'options_list': [
        'A) They are compared directly with all possible positive pairs.',
        'B) They provide contrast by being sampled randomly from all potential entity types.',  # Correct answer
        'C) They contribute to optimizing the embeddings to differentiate between similar entities.',
        'D) They are used exclusively in link prediction tasks.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Negative entities are sampled randomly to provide contrast during training.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_208 = {
    'question': (
        'Which type of task can be combined with other tasks in StarSpace’s multi-task learning framework?'
    ),
    'options_list': [
        'A) Only unsupervised tasks such as word embeddings.',
        'B) Only supervised tasks such as sentence matching.',
        'C) Any task with shared features in the base dictionary.',  # Correct answer
        'D) Only multi-relational graph tasks to improve collaborative filtering outcomes.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Any task with shared features in the base dictionary can be combined in multi-task learning.'
    ),
    'chapter_information': 'StarSpace Paper'
}

# True/False Questions

question_209 = {
    'question': (
        'True or False: StarSpace’s embeddings can compare entities of different types, such as documents and labels, by learning a shared embedding space.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'StarSpace embeds different types of entities into a common space to enable cross-type comparisons.'
    ),
    'chapter_information': 'StarSpace Paper'
}


question_211 = {
    'question': (
        'True or False: StarSpace uses only cosine similarity as its similarity function, regardless of the specific task.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'StarSpace can use either cosine similarity or inner product, depending on the task.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_212 = {
    'question': (
        'True or False: StarSpace’s negative sampling strategy involves selecting random entities as negative examples for comparison during training.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Negative sampling helps the model distinguish between similar and dissimilar pairs.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_213 = {
    'question': (
        'True or False: StarSpace can handle both supervised and unsupervised tasks by varying the positive and negative pair generation strategy.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Adjusting the sampling strategy allows StarSpace to tackle different types of tasks.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_214 = {
    'question': (
        'True or False: Multi-task learning in StarSpace is possible by sharing base dictionary features across different tasks, which can enable semi-supervised learning setups.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Shared features facilitate multi-task and semi-supervised learning.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_215 = {
    'question': (
        'What distinguishes StarSpace from other embedding models when applied to a variety of tasks?'
    ),
    'options_list': [
        'A) It requires minimal training data across different tasks due to its unsupervised nature.',
        'B) It embeds entities of different types into a shared space, enabling meaningful cross-type comparisons.',  # Correct answer
        'C) It relies exclusively on supervised data, resulting in faster training times.',
        'D) It utilizes complex recurrent neural networks to improve entity comparisons.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'StarSpace embeds entities from different types in a shared space for meaningful comparisons.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_217 = {
    'question': (
        'In the text classification experiments, how was StarSpace configured to ensure a fair comparison with fastText?'
    ),
    'options_list': [
        'A) By matching the embedding dimension and using an identical vocabulary and n-gram features.',  # Correct answer
        'B) By increasing the embedding dimension and using different dictionaries to test robustness.',
        'C) By incorporating recurrent layers to match the model complexity of fastText.',
        'D) By employing unsupervised pre-training before supervised fine-tuning to improve accuracy.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'StarSpace used the same embedding dimension and an identical dictionary with the same n-gram features.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_218 = {
    'question': (
        'In the context of document recommendation, what is the main purpose of embedding both documents and users in StarSpace?'
    ),
    'options_list': [
        'A) To simplify user preferences by classifying them into a fixed set of labels.',
        'B) To model user preferences as continuous profiles by aggregating embeddings of items they like.',  # Correct answer
        'C) To represent the entire user-item interaction matrix with a single embedding vector.',
        'D) To create immutable user embeddings that remain constant after initial training.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'StarSpace models user preferences as a continuous profile using embeddings of items they like.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_219 = {
    'question': (
        'What is a major difference between StarSpace and traditional collaborative filtering models in handling new users or items?'
    ),
    'options_list': [
        'A) StarSpace trains unique embeddings for new users from scratch, requiring retraining.',
        'B) StarSpace represents users by combining embeddings of items they interact with, accommodating new users dynamically.',  # Correct answer
        'C) StarSpace ignores new items as out-of-sample data, focusing only on known items.',
        'D) StarSpace is limited to collaborative filtering without the ability to incorporate content-based features.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'StarSpace can represent new users by summing embeddings of items they like, allowing for dynamic profiles.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_224 = {
    'question': (
        'In the Wikipedia Sentence Matching task, which training approach led StarSpace to achieve the best performance?'
    ),
    'options_list': [
        'A) Training exclusively on individual words without considering sentence context.',
        'B) Training on full articles without focusing on sentence-level embeddings.',
        'C) Employing multi-task training that combines word-level and sentence-level embeddings.',  # Correct answer
        'D) Utilizing a deep recurrent neural network to capture sequential dependencies.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Multi-task training with both word- and sentence-level embeddings led to the best performance.'
    ),
    'chapter_information': 'StarSpace Paper'
}

# True/False Questions

question_225 = {
    'question': (
        'True or False: StarSpace can only be used with supervised training data, limiting its application in unsupervised tasks.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'StarSpace can handle both supervised and unsupervised tasks by adjusting its training strategy.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_226 = {
    'question': (
        'True or False: In StarSpace, embedding models can be directly applied to recommendation tasks for unseen users and items.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'StarSpace can represent new users and items through embeddings, enabling recommendations for unseen data.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_227 = {
    'question': (
        'True or False: One unique feature of StarSpace is its ability to handle multi-relational graphs, allowing it to perform link prediction in knowledge bases.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'StarSpace can work with multi-relational data for tasks like link prediction.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_229 = {
    'question': (
        'True or False: During training, StarSpace’s similarity function is optimized specifically for document search and recommendation tasks, making it less adaptable to other domains.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'The similarity function in StarSpace is general-purpose, allowing it to adapt to various tasks and domains.'
    ),
    'chapter_information': 'StarSpace Paper'
}

question_300 = {
    'question': (
        'What is the main purpose of the Softmax function in neural attention models?'
    ),
    'options_list': [
        'A) To ensure a differentiable process for selecting elements from a set based on relevance to a query vector',  # Correct answer
        'B) To randomly select any element from a set regardless of relevance to a query',
        'C) To enforce a one-to-one mapping between input and output elements',
        'D) To convert all negative values in the set to positive values'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The Softmax function is used to create a differentiable selection process where elements of the set are selected with probabilities based on their relevance to a query vector.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_301 = {
    'question': (
        'How does the Softmax function respond when the input values are scaled up (e.g., doubled)?'
    ),
    'options_list': [
        'A) It scales up the output values proportionally.',
        'B) It keeps the outputs unchanged but increases the certainty on the maximum value.',  # Correct answer
        'C) It scales the output down by reducing all values.',
        'D) It changes the order of values based on their size.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'When inputs are scaled up, Softmax increases the certainty by concentrating more probability mass on the highest value, without changing the sum of outputs.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_302 = {
    'question': (
        'In the context of attention, what does "hard attention" refer to?'
    ),
    'options_list': [
        'A) Computing a summary over all inputs',
        'B) Selecting only a subset of relevant inputs',
        'C) Applying Softmax to compute weighted averages',
        'D) Using a non-differentiable process to choose the input'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Hard attention refers to selecting an input in a non-differentiable manner, typically by choosing a single relevant item without computing a weighted summary.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_303 = {
    'question': (
        'What is the role of "position embedding" in neural networks that handle sequences?'
    ),
    'options_list': [
        'A) It removes the dependency on the order of inputs in a sequence.',
        'B) It provides a differentiable method for element selection in sets.',
        'C) It encodes the position information of each element in the sequence.',  # Correct answer
        'D) It acts as a controller state for attention layers.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Position embedding encodes each element’s position in the sequence, helping the network capture temporal or causal structures in ordered data.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_304 = {
    'question': (
        'In a multi-layer attention model, what role does the "controller state" (q) play?'
    ),
    'options_list': [
        'A) It acts as a static reference across all layers of the model.',
        'B) It updates at each layer based on weighted inputs, guiding subsequent attention layers.',  # Correct answer
        'C) It computes the Softmax weights for the last layer only.',
        'D) It remains unchanged throughout the layers to maintain consistency.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The controller state updates layer-by-layer, using weighted inputs to compute new attention layers, progressively focusing on different parts of the input set.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

# True/False Questions

question_305 = {
    'question': (
        'True or False: The Softmax function outputs a probability distribution by assigning each input a positive value and summing to 1.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Softmax exponentiates the inputs, normalizes them, and ensures they sum to 1, forming a probability distribution over the inputs.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_306 = {
    'question': (
        'True or False: In neural attention, the Softmax function is invariant to the order of elements within the input set.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Softmax is permutation-invariant, meaning it generates the same output distribution regardless of input order.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_307 = {
    'question': (
        'True or False: Position embeddings are applied in attention models to make the model completely independent of input order.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Position embeddings encode the order, allowing the model to take temporal or sequential information into account.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_308 = {
    'question': (
        'True or False: In a multi-layer attention network, the same initial controller state is used at each layer without modification.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'The controller state is updated at each layer, using information from the weighted input to guide the focus of attention in subsequent layers.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_309 = {
    'question': (
        'True or False: In neural attention layers, using only the largest Softmax weight for selection would result in a non-differentiable process.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Selecting based on the highest weight alone is a non-differentiable action, which is why Softmax uses weighted probabilities for smooth, differentiable selection.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

# Additional Multiple-Choice Questions

question_310 = {
    'question': (
        'What is a primary reason for using the Softmax function in neural attention mechanisms?'
    ),
    'options_list': [
        'A) It allows differentiable selection of inputs based on similarity to a query.',  # Correct answer
        'B) It normalizes the outputs to a fixed value.',
        'C) It eliminates the need for additional memory in neural networks.',
        'D) It applies a threshold to ignore low-confidence outputs.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Softmax allows for differentiable selection based on similarity to a query, making it useful for attention mechanisms.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_311 = {
    'question': (
        'In the Softmax function, how does scaling the inputs affect the output?'
    ),
    'options_list': [
        'A) It results in a scaled output where all values increase proportionally.',
        'B) It concentrates more weight on the largest input values.',  # Correct answer
        'C) It applies a linear transformation to the outputs.',
        'D) It spreads the output distribution more evenly across all inputs.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Scaling the inputs increases the proportion of the output weight assigned to the largest values.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_312 = {
    'question': (
        'In attention mechanisms, why is a query vector typically used in conjunction with Softmax?'
    ),
    'options_list': [
        'A) To directly select the maximum input value.',
        'B) To make the layer invariant to input permutations.',
        'C) To compute similarity scores for weighting the inputs.',  # Correct answer
        'D) To combine inputs based on temporal sequence order.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The query vector computes similarity scores with the inputs, which Softmax then uses for weighting.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_313 = {
    'question': (
        'Which of the following best describes the purpose of position embeddings in an attention model?'
    ),
    'options_list': [
        'A) They add a layer of randomness to improve model generalization.',
        'B) They distinguish the sequence order or temporal structure of inputs.',  # Correct answer
        'C) They eliminate the need for recurrent layers.',
        'D) They increase the dimensionality of the input space for higher accuracy.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Position embeddings provide information on sequence order or temporal structure, which is useful in models dealing with ordered data.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_314 = {
    'question': (
        'What is the main benefit of using attention mechanisms over traditional recurrent neural networks for tasks like translation?'
    ),
    'options_list': [
        'A) Attention models are less computationally demanding for small datasets.',
        'B) They can capture long-range dependencies more effectively.',  # Correct answer
        'C) Attention models do not require training on labeled data.',
        'D) They avoid the need for a transformer architecture.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Attention mechanisms capture long-range dependencies more effectively, which is useful in tasks like translation.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

# Additional True/False Questions

question_315 = {
    'question': (
        'True or False: In a neural attention layer, hard attention is typically more commonly used than soft attention.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Soft attention, often implemented with Softmax, is more commonly used as it allows for differentiable selection.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_316 = {
    'question': (
        'True or False: The Softmax function respects the permutation of inputs, meaning the order of inputs does not affect the output distribution.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Softmax is permutation invariant, making it insensitive to the order of inputs.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_317 = {
    'question': (
        'True or False: In a multi-layer attention model, each layer updates the controller state based on weighted input vectors to guide the next layer’s attention.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Each attention layer refines the controller state by weighting input vectors, guiding the subsequent attention layers.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_318 = {
    'question': (
        'True or False: The controller state in an attention layer represents the output, while the weighted sum of inputs is used as the query vector.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'The controller state is often the query, while the weighted sum of inputs is the output.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_319 = {
    'question': (
        'True or False: Adding position embeddings to inputs in a transformer model is essential for encoding sequence information.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Position embeddings are added to encode sequence order, crucial for tasks with temporal or causal dependencies.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}


question_320 = {
    'question': (
        'What is the primary purpose of "multi-head attention" in Transformer models?'
    ),
    'options_list': [
        'A) To use different attention mechanisms on a single chunk of input data',
        'B) To split the controller state into parts, apply attention separately to each, and then recombine the results',  # Correct answer
        'C) To enhance computational efficiency by reducing the number of layers',
        'D) To increase training speed by skipping certain input tokens'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Multi-head attention divides the controller state, applies attention to each segment independently, and then recombines them, allowing the model to capture different aspects of the input.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_321 = {
    'question': (
        'What role do position embeddings play in Transformers when applied to natural language processing (NLP) tasks?'
    ),
    'options_list': [
        'A) They replace token embeddings to capture word order.',
        'B) They add sequence information to each token, preserving the order of tokens.',  # Correct answer
        'C) They help differentiate between words of similar meanings.',
        'D) They mask irrelevant words in a sequence to focus on the main context.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Position embeddings add positional information to each token, preserving the sequence structure, which is essential for ordered data like language.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_322 = {
    'question': (
        'In the context of Transformer training for NLP, what is the purpose of causal attention?'
    ),
    'options_list': [
        'A) To allow bidirectional context for each word in the sequence',
        'B) To mask out tokens that come after the current token, enforcing a left-to-right structure',  # Correct answer
        'C) To dynamically adjust attention weights based on token frequency',
        'D) To ensure all tokens in the sequence are treated equally'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Causal attention masks future tokens, maintaining a left-to-right order, which is crucial in tasks like language modeling where future context should not influence predictions.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_323 = {
    'question': (
        'Why are residual connections important in Transformer models?'
    ),
    'options_list': [
        'A) They enable parallel computation across multiple heads.',
        'B) They simplify the model architecture by removing certain layers.',
        'C) They help stabilize training by allowing gradients to flow more effectively through layers.',  # Correct answer
        'D) They ensure each layer receives inputs only from the previous layer.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Residual connections help gradients propagate through layers, making training more stable and efficient, which is particularly important in deep architectures like Transformers.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_324 = {
    'question': (
        'How does multi-query attention differ from the standard attention mechanism in Transformers?'
    ),
    'options_list': [
        'A) It creates a unique controller state for each input, enabling independent attention.',  # Correct answer
        'B) It applies the same attention weights to each layer of the Transformer.',
        'C) It reduces the computational complexity of self-attention by using a single controller state.',
        'D) It applies attention only to specific, predefined queries rather than all inputs.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Multi-query or self-attention provides each input token with its own controller state, allowing each token to compute its own attention weights independently, enhancing the model’s ability to capture contextual relationships.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

# True/False Questions

question_325 = {
    'question': (
        'True or False: In multi-head attention, each head computes attention independently on a segment of the controller state, which are then recombined through a fully connected layer.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Multi-head attention divides the controller state into segments, applies attention to each independently, and recombines the results through a fully connected layer.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_327 = {
    'question': (
        'True or False: Transformers can use causal attention to predict each token simultaneously, enhancing training speed for NLP tasks.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Causal attention allows Transformers to predict each token simultaneously, which increases training efficiency by outputting predictions for all tokens at once rather than sequentially.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_328 = {
    'question': (
        'True or False: LayerNorm in Transformers contributes primarily to stabilizing the learning rate across different parts of the model.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'LayerNorm is used to stabilize training by normalizing inputs within each layer, helping gradients flow more smoothly, but it doesn’t specifically stabilize the learning rate.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_329 = {
    'question': (
        'True or False: Transformers operate well on unordered sets or sequences due to the structure of self-attention.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Self-attention in Transformers allows them to work effectively on sets without a strict order, as it processes each input relative to all others without needing sequence order.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

# Additional Multiple-Choice Questions

question_330 = {
    'question': (
        'What is the primary advantage of using self-attention in Transformers over a traditional multi-layer attention model?'
    ),
    'options_list': [
        'A) It reduces computational costs for large inputs.',
        'B) It assigns a unique controller state to each input, scaling with input size.',  # Correct answer
        'C) It ensures that each input contributes equally to the output.',
        'D) It simplifies the architecture by removing residual connections.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Self-attention in Transformers provides a controller state for each input, allowing the model’s representation to grow with input size.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_331 = {
    'question': (
        'What is the role of multi-head attention in the Transformer architecture?'
    ),
    'options_list': [
        'A) To compute attention weights by combining multiple inputs into a single head.',
        'B) To allow attention to focus on different aspects of the inputs by creating independent attention heads.',  # Correct answer
        'C) To capture the inherent sequential order of language inputs, such as left-to-right context.',
        'D) To sequentially compute attention across all inputs before recombining them.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Multi-head attention divides the input into chunks, enabling the model to attend to different input aspects independently.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_332 = {
    'question': (
        'Why are position embeddings used in Transformers for NLP tasks?'
    ),
    'options_list': [
        'A) To speed up training by reducing the number of layers required.',
        'B) To capture the inherent sequential order of language inputs, such as left-to-right context.',  # Correct answer
        'C) To assign a unique embedding to each unique word in the vocabulary.',
        'D) To increase model capacity by adding more parameters.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Position embeddings capture the sequential order in language, which is crucial in NLP tasks where the order of tokens matters.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_333 = {
    'question': (
        'In the context of Transformers, what does causal attention achieve?'
    ),
    'options_list': [
        'A) It allows each token to attend to any other token, regardless of order.',
        'B) It prevents tokens from attending to future positions, enforcing left-to-right information flow.',  # Correct answer
        'C) It assigns a constant weight to all tokens regardless of relevance.',
        'D) It speeds up training by ignoring context.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Causal attention prevents a token from attending to future tokens, enforcing a left-to-right order.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}

question_334 = {
    'question': (
        'What implementation trick is commonly used to speed up Transformer training on NLP tasks?'
    ),
    'options_list': [
        'A) Using multi-head attention only on the final layer.',
        'B) Masking out the embeddings of less important tokens.',
        'C) Outputting a prediction for each token in the sequence simultaneously.',  # Correct answer
        'D) Replacing position embeddings with causal embeddings.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Outputting a prediction for each token simultaneously significantly speeds up Transformer training.'
    ),
    'chapter_information': 'GT Lesson 14 Facebook Lecture'
}







KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_14_MPC = KC_MPC_QUESTIONS[:-1]
