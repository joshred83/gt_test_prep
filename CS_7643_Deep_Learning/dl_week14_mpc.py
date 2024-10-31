

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




KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_14_MPC = KC_MPC_QUESTIONS[:-1]
