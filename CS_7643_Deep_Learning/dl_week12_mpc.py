
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

questiony_4 = {
    'question': (
        'In a conditional language model, if $c$ represents a topic context, what does the model learn?'
    ),
    'options_list': [
        'A) The probability of generating a syntactically correct sentence, regardless of context.',
        'B) The probability of generating a sentence conditioned on the topic context $c$.',  # Correct answer
        'C) The probability of generating a sentence based on the bi-grams.',
        'D) The probability of predicting the words around it based on the average word embeddings of the sentence.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In a conditional language model, the context $c$ (e.g., topic, domain) influences the sentence generation process, allowing the model to generate sentences that are contextually appropriate. Options A, C, and D describe simpler models like n-gram models or unconditional language models.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_2 = {
    'question': (
        'In the context of RNNs, which statement correctly describes "truncated backpropagation through time"?'
    ),
    'options_list': [
        'A) It restricts both the forward and backward pass to a fixed number of time steps.',
        'B) It restricts backpropagation to only a fixed number of time steps backward, while allowing the forward pass to proceed over the entire sequence.',  # Correct answer
        'C) It prevents gradients from being computed for certain time steps by skipping them during backpropagation.',
        'D) It uses gradient clipping to limit large gradients during backpropagation across long time steps.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Truncated backpropagation through time (TBPTT) is used in RNNs to limit the backward pass to a fixed number of time steps, reducing computational cost. Option A incorrectly restricts both passes, Option C describes a form of skipping, and Option D refers to gradient clipping, which is a separate technique used to manage exploding gradients.'
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
        'D) When the gradients are clipped during backpropagation through time, and their values become increasingly lower.'
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
questiony_32 = {
    'question': (
        'When processing long sequences, what is the main challenge that RNNs face, and what methods are typically used to overcome it?'
    ),
    'options_list': [
        'A) RNNs suffer from vanishing gradients, which can be mitigated by using advanced architectures like LSTMs or GRUs with gating mechanisms.',  # Correct answer
        'B) RNNs suffer from exploding gradients when processing long sequences, which can be mitigated by using gradient clipping.',
        'C) RNNs have difficulty capturing long-range dependencies, which can be mitigated by incorporating multi-head self-attention from the Transformer architecture.',
        'D) RNNs are computationally inefficient for long sequences, which can be addressed by parallelizing the forward pass using architectures like MLPs.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'A) is correct because RNNs are prone to vanishing gradients, making it difficult for them to learn long-term dependencies. LSTMs and GRUs mitigate this by using gates that help preserve information over longer sequences. '
        'B) is incorrect because gradient clipping helps with exploding gradients, not vanishing gradients. '
        'C) confuses RNNs with Transformers, which use multi-head self-attention to capture long-range dependencies. '
        'D) incorrectly suggests parallelization using MLPs, which are not typically used for sequential data processing.'
    ),
    'chapter_information': 'Lesson 12: Language Models - GT Facebook Lecture'
}

questiony_33 = {
    'question': (
        'In a typical autoregressive language model, how is the probability of a sequence of words calculated?'
    ),
    'options_list': [
        'A) By applying the chain rule, where the probability of each word is conditioned on all previous words in the sequence.',  # Correct answer
        'B) By summing the probabilities of each word in the sequence based on their independent probabilities.',
        'C) By calculating the average log probability of the sequence, factoring in the individual probabilities of each word and normalizing them.',
        'D) By sampling from a predefined distribution of possible word sequences without explicitly calculating conditional probabilities.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'A) is correct because autoregressive models use the chain rule to calculate the probability of a sequence by conditioning each word on all previous words. '
        'B) is incorrect because the probabilities are not independent, they are conditioned on prior words. '
        'C) mixes up log probabilities with the actual probability calculation of the sequence. '
        'D) incorrectly describes random sampling without the use of conditional probabilities, which is not how autoregressive language models operate.'
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

########################################### DEEP LEARNING BOOK ##################################################################


# Chapter 10.1 Deep Learning Book

questio11n_1 = {
    'question': (
        "How does parameter sharing in RNNs affect the model's capacity to learn complex sequences, and what trade-offs does it introduce compared to models without parameter sharing?"
    ),
    'options_list': [
        'A) Parameter sharing allows RNNs to use different sets of parameters for each time step, making the model more flexible.',
        'B) Parameter sharing allows RNNs to generalize across different sequence lengths and time positions by applying the same weights at each time step.',  # Correct answer
        'C) Parameter sharing enables RNNs to learn different patterns of input-output relations for every unique sequence it processes, improving adaptability.',
        'D) Parameter sharing in RNNs reduces the total number of parameters, ensuring that information at the beginning of the sequence is more influential than at later time steps.'
    ],
    'correct_answer': 'B',
    'explanation': (
    "Parameter sharing in RNNs means that the same set of weights is applied at each time step. This reduces the total number of parameters, \
    which helps prevent overfitting and allows the model to generalize to sequences of different lengths. However, this can limit the model's\
        capacity to capture position-specific patterns since it cannot learn unique weights for each time step. The trade-off is between model complexity \
            (and potential overfitting) \
    and the ability to generalize across different sequence lengths and positions."
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

questio11n_2 = {
    'question': (
        'Which of the following is a major limitation of traditional fully connected feedforward networks when applied to sequential data compared to RNNs?'
    ),
    'options_list': [
        'A) Feedforward networks cannot handle large input sizes due to computational constraints, while RNNs can.',
        'B) Feedforward networks do not share parameters across time steps, leading to inefficient learning of sequential patterns.',  # Correct answer
        'C) Feedforward networks require labeled data at every step in the sequence, while RNNs can operate without supervision.',
        'D) Feedforward networks are inherently recursive, leading to difficulties in processing sequences longer than a fixed length.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'A key limitation of feedforward networks when processing sequential data is that they do not share parameters across time steps. '
        'This means they must learn patterns at each position independently, which is inefficient and does not generalize well to sequences of varying lengths.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

questio11n_4 = {
    'question': (
        'Which of the following is the main reason why RNNs are particularly suited for processing sequences with variable lengths?'
    ),
    'options_list': [
        'A) RNNs adjust the number of parameters dynamically based on the length of the input sequence.',
        'B) RNNs can process each time step independently, allowing them to easily handle sequences of any length.',
        'C) RNNs share parameters across all time steps, enabling them to generalize to sequences of different lengths without needing separate weights for each position.',  # Correct answer
        'D) RNNs use dynamic memory allocation to store information about every possible sequence length during training.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'The parameter-sharing mechanism in RNNs ensures that the same set of weights is used across all time steps, allowing them to handle sequences of variable lengths effectively without the need for separate weights for each sequence length.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

questio11n_5 = {
    'question': (
        'In an RNN model, the process of "unrolling" is critical for understanding how the network operates. What does unrolling an RNN imply?'
    ),
    'options_list': [
        'A) It means expanding the computational graph to handle sequences of different lengths during training.',
        'B) It involves creating copies of the RNN for each time step, making the computational graph deep but sequential.',  # Correct answer
        'C) Unrolling refers to splitting the sequence into fixed-length segments for better parallelization.',
        'D) It indicates the process of stacking multiple RNN layers to increase the network\'s depth.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Unrolling an RNN refers to expanding the recurrent computation over time by replicating the network for each time step, forming a deep computational graph where each layer corresponds to a different time step in the sequence.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_6 = {
    'question': (
        'Which of the following challenges can arise in RNN training due to the deep computational graph that results from unrolling the network over long sequences?'
    ),
    'options_list': [
        'A) Overfitting, due to the presence of too many parameters, causing poor generalization to unseen data.',
        'B) Vanishing or exploding gradients, which occur due to the repeated application of weight matrices over many time steps.',  # Correct answer
        'C) Over-parameterization, leading to an excessive number of hidden units that slow down computation.',
        'D) Difficulty in capturing short-term dependencies, as RNNs primarily focus on long-term sequence patterns.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'A well-known issue with training RNNs over long sequences is the vanishing or exploding gradient problem, where gradients can either become too small (vanishing) or too large (exploding) during backpropagation through time, making it difficult to update the weights effectively.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_7 = {
    'question': (
        'Given that RNNs can suffer from vanishing gradients during training, which modification is commonly introduced to mitigate this issue?'
    ),
    'options_list': [
        'A) Using non-linear activation functions like ReLU instead of sigmoid or tanh to prevent the gradient from saturating.',
        'B) Introducing gradient clipping to prevent the exploding gradient problem, but this does not address vanishing gradients.',
        'C) Implementing gated architectures like LSTMs or GRUs, which maintain information over long time steps by using forget gates and memory cells.',  # Correct answer
        'D) Adding more layers to the RNN to distribute the gradients more evenly across the network.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Gated architectures like Long Short-Term Memory (LSTM) networks and Gated Recurrent Units (GRUs) help alleviate the vanishing gradient problem by introducing mechanisms (gates) that control the flow of information over time, preserving important signals over long sequences.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_8 = {
    'question': (
        'Which of the following is a primary benefit of using RNNs over feedforward neural networks for sequence modeling tasks?'
    ),
    'options_list': [
        'A) RNNs use backpropagation, while feedforward networks do not, allowing RNNs to learn more efficiently.',
        'B) RNNs can use reinforcement learning techniques, making them more adaptable for complex tasks.',
        'C) RNNs are able to maintain a hidden state that captures information from previous time steps, enabling them to model temporal dependencies in sequential data.',  # Correct answer
        'D) RNNs do not require labeled data for training, while feedforward networks do, making RNNs more suitable for unsupervised learning.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'RNNs have a hidden state that is updated at each time step and carries information forward in the sequence. This allows them to model temporal dependencies in the data, making them more effective than feedforward networks for sequence tasks.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_9 = {
    'question': (
        'True or False: Parameter sharing in RNNs allows the network to process sequences of different lengths by applying the same set of weights to each time step, regardless of sequence position.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Parameter sharing is a key feature of RNNs that allows them to process sequences of different lengths by applying the same set of weights across all time steps. This ensures that the model can generalize well across varying sequence lengths.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_10 = {
    'question': (
        'Consider an RNN trained on sequences of length 10. If the same RNN is used to process a sequence of length 20, how does the model handle this longer sequence?'
    ),
    'options_list': [
        'A) The RNN will fail because it was only trained on sequences of length 10.',
        'B) The RNN will pad the input to ensure that the length matches 10, discarding the extra time steps.',
        'C) The RNN can handle this longer sequence because it shares the same parameters across all time steps and does not depend on the sequence length during training.',  # Correct answer
        'D) The RNN will generate random predictions for the extra time steps because it was not trained on longer sequences.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Due to parameter sharing, an RNN can generalize to sequences of any length, even if it was only trained on sequences of a certain length. '
        'It processes each time step using the same weights, regardless of the total length of the sequence.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

# Advanced Questions Based on RNNs, LSTMs, and Chapter 10 of Deep Learning


question_52 = {
    'question': (
        'Given the following two sentences: "In 2019, I visited Paris" and "I visited Paris in 2019", how does an RNN handle parameter sharing to effectively capture the relevant temporal information (the year) regardless of its position in the sentence?'
    ),
    'options_list': [
        'A) The RNN uses different sets of weights for each time step, allowing it to capture information in both forward and backward directions.',
        'B) It uses a convolutional operation across time steps to capture local dependencies, ignoring the exact position of words.',
        'C) The RNN applies the same update rule and the same weights at each time step, ensuring that the position of "2019" in the sequence does not affect its ability to learn the relevant temporal information.',  # Correct answer
        'D) The RNN explicitly learns to focus on certain time steps by applying weighted attention to important positions in the sequence.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because an RNN shares parameters across time steps, using the same weights for all time steps. '
        'This allows the network to learn patterns, like recognizing "2019", regardless of where in the sequence it appears. '
        'A), B), and D) either refer to architectures like attention or convolution, or misunderstand how RNNs work. Weight sharing is central to RNNs, unlike D which refers to attention mechanisms.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_53 = {
    'question': (
        'What is the main architectural difference between Recurrent Neural Networks (RNNs) and Time-Delay Neural Networks (TDNNs) when processing sequential data?'
    ),
    'options_list': [
        'A) RNNs maintain hidden states that are updated at each time step, whereas TDNNs use a fixed-size kernel to process local windows of time-delayed input data.',  # Correct answer
        'B) RNNs are more shallow than TDNNs, as RNNs do not contain convolutional layers.',
        'C) TDNNs handle both forward and backward time dependencies by default, while RNNs only process sequences in one direction.',
        'D) TDNNs use parameter sharing across time steps, while RNNs use different parameters at each time step to capture temporal dependencies.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'A) is correct. RNNs update their hidden state recursively across time, while TDNNs use a convolution-like approach to process windows of data over time, making them shallower than RNNs. '
        'RNNs are inherently deeper due to their recurrent nature. '
        'B) and D) incorrectly describe RNNs and TDNNs. C) refers to bidirectional RNNs rather than standard RNNs or TDNNs.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_54 = {
    'question': (
        'Which of the following is a fundamental challenge when using recurrent neural networks (RNNs) to process long sequences?'
    ),
    'options_list': [
        'A) RNNs do not have the ability to model long-range dependencies due to their shallow structure.',
        'B) The weights of the RNN are not shared across time steps, making it difficult to generalize to sequences of varying lengths.',
        'C) The gradients in RNNs can either vanish or explode during backpropagation through time, leading to difficulty in learning long-range dependencies.',  # Correct answer
        'D) RNNs cannot handle sequences where the input at each time step is not uniformly distributed in length or value.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because the vanishing/exploding gradient problems are well-documented challenges in training RNNs, especially for long sequences. '
        'These problems make it difficult for RNNs to learn and retain long-term dependencies. '
        'A) mischaracterizes RNNs, which are designed for sequential processing but face issues with long sequences. B) misunderstands that RNNs do share weights across time steps, and D) is unrelated to the core challenge.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_55 = {
    'question': (
        'One major advantage of Long Short-Term Memory (LSTM) networks over vanilla RNNs is their ability to:'
    ),
    'options_list': [
        'A) Use convolutional layers to process sequences more efficiently.',
        'B) Mitigate the vanishing gradient problem by using gating mechanisms that allow important information to flow unchanged across many time steps.',  # Correct answer
        'C) Eliminate the need for backpropagation through time, reducing computational costs.',
        'D) Capture long-term dependencies by training on sequences of fixed length only, which leads to more stable training.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because LSTMs use gates (input, forget, and output) to control the flow of information, allowing the network to retain important information over long time steps, thereby alleviating the vanishing gradient problem. '
        'A), C), and D) misrepresent the mechanisms and strengths of LSTMs compared to RNNs.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_57 = {
    'question': (
        'What is a key distinction between the way Recurrent Neural Networks (RNNs) and Convolutional Neural Networks (CNNs) handle sequence data?'
    ),
    'options_list': [
        'A) RNNs handle fixed-size sequences, while CNNs are used for variable-length sequences.',
        'B) RNNs process sequences by maintaining a hidden state across time steps, while CNNs process sequences using a sliding window (convolutional filter) across time steps.',  # Correct answer
        'C) CNNs are typically used for time-series prediction, while RNNs are primarily used for image processing.',
        'D) CNNs process the entire sequence simultaneously, whereas RNNs process one element at a time without using hidden states.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because RNNs maintain hidden states and process one element at a time, while CNNs apply filters to local windows of the sequence at each step. '
        'A), C), and D) misunderstand the usage and mechanisms of CNNs and RNNs in sequence modeling.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

question_58 = {
    'question': (
        'In knowledge distillation for neural networks, how does the "teacher model" improve the training of the "student model"?'
    ),
    'options_list': [
        'A) By providing labeled data that the student model uses to pre-train its weights before fine-tuning on the actual task.',
        'B) By offering soft predictions (probability distributions) that guide the student model, allowing it to learn not only the correct prediction but also the relationships between possible incorrect predictions.',  # Correct answer
        'C) By acting as a reinforcement learning agent that rewards the student model for making the correct predictions.',
        'D) By augmenting the student model with additional layers that the student uses to handle more complex data.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because knowledge distillation relies on the soft predictions from the teacher model to help the student model learn a more nuanced probability distribution, improving its generalization ability. '
        'A), C), and D) either misunderstand knowledge distillation or confuse it with other techniques.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}
##################
# Advanced Questions Based on Gradient Computation in RNNs, Bidirectional RNNs, and Chapter 10 of Deep Learning

questasdion_1 = {
    'question': (
        'Based on the gradient formulas provided in Figure 10.22-10.28, which of the following statements regarding the gradient of loss with respect to the parameter $W$ in a simple RNN is correct?'
    ),
    'options_list': [
        'A) The gradient $\\nabla_W L$ is computed as a simple product of the loss and the hidden state at each time step.',
        'B) The gradient $\\nabla_W L$ depends only on the current hidden state and does not involve the previous hidden states.',
        'C) The gradient $\\nabla_W L$ includes a component involving the derivative of the loss $\\nabla_h(t)L$ and is scaled by $(1 - (h(t))^2)$ due to the derivative of the tanh activation function.',  # Correct answer
        'D) The gradient $\\nabla_W L$ is independent of the sequence length $t$ because the RNN shares parameters across time steps.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because the gradient of the loss with respect to the weight parameter $W$ includes terms involving $\\nabla_h(t)L$, scaled by the derivative of the tanh function $(1 - (h(t))^2)$ at each time step, as shown in Equation 10.26.'
    ),
    'image': 'images/dl10_math.png',
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

quasdestion_2 = {
    'question': (
        'Consider a bidirectional RNN used for sequence processing. According to Figure 10.11, which of the following statements is true about the bidirectional RNN’s capacity to model sequence data?'
    ),
    'options_list': [
        'A) The backward RNN $g(t)$ solely focuses on optimizing the prediction at the final time step and is not involved in intermediate time steps.',
        'B) The output at time $t$ is influenced by both past inputs, encoded in $h(t)$, and future inputs, encoded in $g(t)$, allowing for richer representations across the sequence.',  # Correct answer
        'C) The forward recurrence $h(t)$ and the backward recurrence $g(t)$ do not share parameters, and thus they independently optimize the sequence prediction.',
        'D) The forward recurrence in a bidirectional RNN propagates information from the last time step to the first, while the backward recurrence propagates from the first time step to the last.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because the bidirectional RNN processes information from both the past (via $h(t)$) and the future (via $g(t)$) at each time step, creating a more comprehensive representation of the sequence.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

qasuestion_5 = {
    'question': (
        'According to the description of bidirectional RNNs applied to 2D grids (e.g., images), what is the primary advantage of using RNNs for this task compared to traditional convolutional networks?'
    ),
    'options_list': [
        'A) RNNs applied to images are computationally more efficient than convolutional networks due to the use of fewer parameters.',
        'B) RNNs allow for long-range interactions between features in the same feature map, which enables the model to capture dependencies across larger spatial distances.',  # Correct answer
        'C) RNNs outperform convolutional networks for image tasks due to their shallow architecture and the absence of backpropagation.',
        'D) RNNs in 2D grids reduce the computational complexity by avoiding lateral interactions across the feature map.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because RNNs applied to 2D input can model long-range interactions between features in the same feature map, allowing them to capture both local and global dependencies in image data.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}

q1uestio1n_6 = {
    'question': (
        'In the context of training RNNs on minibatches of sequences, what technique is typically employed to handle sequences of different lengths during training?'
    ),
    'options_list': [
        'A) Using the average sequence length across all examples and padding the shorter sequences.',
        'B) Truncating the sequences to the shortest sequence length to avoid processing unnecessary time steps.',
        'C) Padding shorter sequences with a special token and using masking to ensure that padded elements do not affect the gradient updates.',  # Correct answer
        'D) Training each sequence individually without batching to avoid dealing with variable sequence lengths.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because padding shorter sequences with a special token and using masking ensures that shorter sequences can be processed within a minibatch without affecting the gradient updates, which is a common practice in training RNNs with sequences of variable lengths.'
    ),
    'chapter_information': 'Chapter 10.1 Deep Learning Book'
}
# Advanced Challenging Questions Based on RNNs, LSTMs, and Chapter 10

questiyuon_1 = {
    'question': (
        'In a bidirectional recurrent neural network (BRNN), how does the model\'s architecture enable it to effectively leverage both past and future context at a given time step?'
    ),
    'options_list': [
        'A) The forward RNN processes the input sequence in reverse order while the backward RNN processes it in the correct order, allowing the model to consider future context by learning from the past.',
        'B) The forward RNN processes the input sequence from the beginning, while the backward RNN processes it from the end. Each hidden state is a combination of information from the past (forward RNN) and the future (backward RNN) at every time step.',  # Correct answer
        'C) Both the forward and backward RNNs process the input sequence in the same direction, but with different weights, to focus on learning from short-term and long-term dependencies separately.',
        'D) The bidirectional RNN uses attention mechanisms to attend to both past and future information, which is combined to compute a summary at each time step.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because the forward RNN processes the input sequence from the beginning, while the backward RNN processes it from the end. Each hidden state combines information from the past (via forward RNN) and the future (via backward RNN) at each time step.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

questiyuon_2 = {
    'question': (
        'When applying RNNs to two-dimensional input data, such as images, how does the architecture differ compared to a standard convolutional network?'
    ),
    'options_list': [
        'A) The RNN processes the image in patches, scanning the image left-to-right, and then applies a max-pooling layer over the resulting sequence.',
        'B) The RNN applies convolutions across the image pixels and then uses a hidden state to propagate information through time across both the x and y dimensions.',
        'C) Four RNNs are used, each moving in one direction (up, down, left, right), and at each pixel location, the model incorporates local information as well as long-range dependencies via recurrent propagation across the feature map.',  # Correct answer
        'D) The RNN is unrolled along the x-axis of the image, while a 1D convolution is applied along the y-axis, enabling it to learn both spatial and temporal dependencies in image data.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because four RNNs are used (moving in the directions: up, down, left, right), allowing the model to capture local information and long-range dependencies across the feature map in image data.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

questiyuon_4 = {
    'question': (
        'Which of the following is a key advantage of using bidirectional recurrent neural networks (BRNNs) over standard RNNs in sequence modeling tasks?'
    ),
    'options_list': [
        'A) BRNNs are less computationally expensive since they require fewer parameters to model sequences in both directions.',
        'B) BRNNs can process variable-length sequences more effectively than standard RNNs, which are limited to fixed-length inputs.',
        'C) BRNNs are particularly effective because they allow each output to be based on both past and future context, improving tasks like speech recognition and language translation.',  # Correct answer
        'D) BRNNs do not suffer from vanishing gradients, unlike standard RNNs, because they propagate gradients forward and backward simultaneously.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'C) is correct because BRNNs combine information from both past and future contexts at each time step, making them especially useful for tasks like speech recognition and language translation.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

questionyu_5 = {
    'question': (
        'When training RNNs with long sequences, the issue of vanishing gradients often arises. Which of the following techniques is most commonly used to address this issue?'
    ),
    'options_list': [
        'A) Increasing the number of hidden units in each RNN layer to maintain gradient flow.',
        'B) Truncated backpropagation through time (TBPTT), which limits the length of the sequence over which gradients are propagated.',  # Correct answer
        'C) Using bidirectional RNNs, which propagate information in both directions and reduce the likelihood of vanishing gradients.',
        'D) Applying batch normalization after each time step to ensure that the gradient does not vanish.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'B) is correct because truncated backpropagation through time (TBPTT) is commonly used to address the vanishing gradient problem by limiting the number of time steps over which gradients are propagated during training.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}
############################################
# Indexed Questions Starting from 100

question_100 = {
    'question': (
        'Which of the following statements is false regarding RNNs and LSTMs?'
    ),
    'options_list': [
        'A) RNNs suffer from the vanishing gradient problem, which makes it difficult to learn long-term dependencies.',
        'B) LSTMs introduce a memory cell that allows them to retain information over longer time sequences.',
        'C) LSTMs and RNNs use the same update rules but differ in how they handle gradient propagation.',
        'D) RNNs solve the issue of long-term dependencies by using a gating mechanism to control information flow.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'LSTMs, not RNNs, use gating mechanisms to control information flow and solve long-term dependency issues.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_101 = {
    'question': (
        'Which of the following is true about conditional language models and perplexity?'
    ),
    'options_list': [
        'A) Perplexity measures the uncertainty of the model and lower perplexity indicates a better model.',  # Correct answer
        'B) Perplexity measures the uncertainty of the model and higher perplexity indicates a better model.',
        'C) Perplexity measures the error rate of the model’s predictions and lower perplexity indicates a better model.',
        'D) Perplexity measures the error rate of the model’s predictions and higher perplexity indicates a better model.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Perplexity is a common metric for evaluating language models; lower perplexity means the model predicts sequences with higher confidence.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_102 = {
    'question': (
        'In the context of Word2Vec\'s skip-gram model, which of the following statements is correct?'
    ),
    'options_list': [
        'A) The skip-gram model predicts the current word given its context words.',
        'B) The objective of skip-gram is to maximize the probability of the context given the center word.',  # Correct answer
        'C) Skip-gram relies on unsupervised training but does not involve any intrinsic or extrinsic evaluation.',
        'D) Word2Vec uses a one-hot encoding to represent each word in the vocabulary for training.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The skip-gram model aims to maximize the probability of context words given the center word.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_103 = {
    'question': (
        'Which of the following is true about t-SNE?'
    ),
    'options_list': [
        'A) t-SNE is primarily used to reduce the dimensions of data while retaining high-dimensional clusters.',  # Correct answer
        'B) t-SNE is a type of recurrent neural network used for sequence modeling.',
        'C) t-SNE performs linear dimensionality reduction by projecting data into lower-dimensional spaces.',
        'D) t-SNE calculates pairwise Euclidean distances between points to directly optimize high-dimensional coordinates.'
    ],
    'correct_answer': 'A',
    'explanation': (
        't-SNE is used for non-linear dimensionality reduction, primarily focusing on preserving the local structure in high-dimensional data.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_104 = {
    'question': (
        'Which of the following best describes how an encoder-decoder model works in sequence-to-sequence prediction tasks?'
    ),
    'options_list': [
        'A) The encoder generates a fixed-length vector that represents the entire input sequence, which the decoder uses to generate the output sequence.',  # Correct answer
        'B) The decoder generates a fixed-length vector representation of the input sequence, which is used to adjust the encoder\'s predictions.',
        'C) The encoder directly predicts future sequences without the need for a decoder.',
        'D) The encoder-decoder model is used only for classification tasks and not for sequence generation.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The encoder-decoder model typically uses the encoder to create a fixed-length vector from the input sequence, which the decoder then uses to predict the output sequence.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_105 = {
    'question': (
        'In the context of neural attention, which of the following is false?'
    ),
    'options_list': [
        'A) Attention mechanisms allow the model to focus on specific parts of the input sequence rather than processing it equally.',
        'B) Self-attention is used in transformers to compute relationships between different positions in a sequence.',
        'C) Soft attention computes a probability distribution over inputs, but hard attention uses reinforcement learning to select discrete parts of the input.',
        'D) In the "Attention is All You Need" model, attention is applied only in the decoder to focus on specific parts of the input.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'In the "Attention is All You Need" model, attention is applied in both the encoder and decoder, not just the decoder.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_106 = {
    'question': (
        'What is the primary purpose of beam search in sequence generation tasks?'
    ),
    'options_list': [
        'A) Beam search selects the highest probability word at each time step, ignoring future predictions.',
        'B) Beam search keeps track of the top-k most probable sequences at each time step, allowing for more diverse sequence predictions.',  # Correct answer
        'C) Beam search uses reinforcement learning to train sequence-to-sequence models more effectively.',
        'D) Beam search is used exclusively for image classification tasks to optimize prediction accuracy.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Beam search maintains the top-k most probable sequences at each time step to explore a more diverse set of potential sequences.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_107 = {
    'question': (
        'Which of the following is true about Byte Pair Encoding (BPE)?'
    ),
    'options_list': [
        'A) BPE is used for sentence tokenization in recurrent neural networks.',
        'B) BPE applies recursive token merging by finding the most common pair of bytes and replacing them with a new token.',  # Correct answer
        'C) BPE is a compression technique used only for encoding images in convolutional neural networks.',
        'D) BPE is used to optimize the memory consumption of attention mechanisms in transformers.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Byte Pair Encoding is a subword tokenization technique that recursively merges frequent byte pairs to handle out-of-vocabulary words in language models.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

# True/False Questions

question_109 = {
    'question': (
        'True or False: Knowledge distillation allows a smaller "student" model to learn from a larger "teacher" model by mimicking the teacher\'s soft probability outputs rather than only the hard class predictions.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Knowledge distillation works by using soft predictions from the teacher model to guide the learning process of a smaller student model.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_110 = {
    'question': (
        'True or False: Perplexity is a metric used to evaluate the performance of sequence models and is defined as the exponential of the cross-entropy loss.'
    ),
    'options_list': [
        'True',  # Correct answer
        'False'
    ],
    'correct_answer': 'True',
    'explanation': (
        'Perplexity is commonly used to measure the performance of language models and is indeed the exponential of the cross-entropy loss.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

ques1tion_110 = {
    'question': (
        'True or False: Perplexity is a metric used to evaluate the performance of sequence models and is defined as the log of the cross-entropy loss.'
    ),
    'options_list': [
        'True',  
        'False'  # Correct answer
    ],
    'correct_answer': 'False',
    'explanation': (
        'Perplexity is commonly used to measure the performance of language models and is the exponential of the cross-entropy loss.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}


question_111 = {
    'question': (
        'True or False: In the skip-gram model of Word2Vec, the goal is to predict the center word given its surrounding context words.'
    ),
    'options_list': [
        'True',
        'False'  # Correct answer
    ],
    'correct_answer': 'False',
    'explanation': (
        'The skip-gram model predicts the surrounding context words given the center word, not the other way around.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

# Challenging Questions on RNNs and Long-Term Dependencies

question_112 = {
    'question': (
        'Skip connections in RNNs are primarily used to improve the speed of training by bypassing irrelevant time steps, reducing the time needed for gradient propagation.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Skip connections in RNNs are used to facilitate learning long-term dependencies by allowing gradients to propagate more effectively, but their main purpose is not solely to improve training speed by bypassing irrelevant time steps.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_113 = {
    'question': (
        'Which of the following statements is not true about leaky units in RNNs?'
    ),
    'options_list': [
        'A) Leaky units allow information to flow from earlier time steps more effectively by sampling time constants at initialization.',
        'B) The time constants of leaky units can be free parameters, allowing them to be learned during training.',
        'C) Leaky units inherently solve the vanishing gradient problem by eliminating short-term dependencies.',  # Correct answer
        'D) Leaky units are used in echo state networks to handle long-term dependencies in sequences.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Leaky units do not inherently solve the vanishing gradient problem by eliminating short-term dependencies. Instead, they allow information to persist across different time scales through controlled leakage of the hidden state.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_114 = {
    'question': (
        'Regarding the approaches used to handle long-term dependencies in RNNs, which of the following statements is false?'
    ),
    'options_list': [
        'A) Skip connections through time can increase the depth of the network, enabling units to access values from much earlier time steps.',
        'B) Removing short-length connections can force units to operate on longer time scales by only focusing on distant time steps.',
        'C) Leaky units with different time constants allow for handling dependencies over various time scales.',
        'D) Time constants in leaky units are generally fixed during training, making them inflexible for long-term sequence learning.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Time constants in leaky units are often learnable parameters, not fixed, allowing them to adapt to different time scales during training, making them flexible for long-term sequence learning.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_115 = {
    'question': (
        'What is the key difference between skip connections through time and removing short-length connections in RNNs?'
    ),
    'options_list': [
        'A) Skip connections add edges that make it easier to learn short-term dependencies, while removing connections eliminates edges to focus on longer-term dependencies.',  # Correct answer
        'B) Skip connections allow the model to skip over irrelevant time steps, while removing connections helps simplify the model by reducing unnecessary weight updates.',
        'C) Skip connections force the model to memorize the most recent time steps, while removing connections helps retain distant time-step information by skipping intermediate steps.',
        'D) Skip connections ensure continuous learning across all time steps, while removing connections guarantees that the model only learns from the most relevant time steps.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Skip connections help in learning short-term dependencies by adding edges that connect non-consecutive time steps, while removing short-length connections forces the model to focus on long-term dependencies by eliminating edges for shorter time scales.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}


question_117 = {
    'question': (
        'Leaky units in RNNs are inherently better at capturing short-term dependencies than standard RNN units due to their ability to remove connections that are no longer needed.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Leaky units are not specifically designed to capture short-term dependencies. Instead, they help maintain information over various time scales by allowing controlled leakage of hidden states across time steps.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_118 = {
    'question': (
        'Which of the following is least likely to solve the vanishing gradient problem in RNNs?'
    ),
    'options_list': [
        'A) Skip connections through time.',
        'B) Leaky units with adjustable time constants.',
        'C) Removing length-one connections and replacing them with longer connections.',
        'D) Initializing weights with a distribution that favors larger values to prevent gradients from vanishing.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'While initializing weights with larger values can temporarily mitigate vanishing gradients, it does not directly address the underlying problem. Skip connections, leaky units, and longer connections are more targeted approaches for dealing with long-term dependencies and vanishing gradients.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_119 = {
    'question': (
        'Which of the following statements about multiple time scales in RNNs is most likely to be misleading?'
    ),
    'options_list': [
        'A) Leaky units at different time scales can help manage long-term dependencies effectively by maintaining information for varying durations.',
        'B) Skip connections through time can force units to focus on long-term dependencies by completely ignoring short-term dependencies.',  # Correct answer
        'C) Grouping recurrent units to update at different frequencies can be an effective strategy to handle tasks requiring multi-scale temporal dependencies.',
        'D) Leaky units are more flexible than removing connections, as they can both capture short-term and long-term dependencies by adjusting time constants.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Skip connections do not force the model to ignore short-term dependencies. They enable the model to handle both short and long-term dependencies by creating shortcuts through time.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_120 = {
    'question': (
        'Which statement regarding the role of linear self-connections in RNNs is incorrect?'
    ),
    'options_list': [
        'A) Linear self-connections can help mitigate the vanishing gradient problem by propagating gradients more smoothly through time.',
        'B) Linear self-connections are primarily used to handle tasks that require the model to learn from the most recent time steps, ignoring distant steps.',  # Correct answer
        'C) Linear self-connections with a weight near one can allow an RNN unit to access information from earlier time steps without introducing new edges.',
        'D) Linear self-connections adjust real-valued parameters to learn dependencies from the past, unlike skip connections that skip fixed time steps.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Linear self-connections are not primarily used to focus only on the most recent time steps. They allow information from earlier time steps to be retained over long periods, which is the opposite of what is described in option B.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

question_121 = {
    'question': (
        'RNNs with skip connections through time are guaranteed to learn long-term dependencies more effectively than RNNs with linear self-connections.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Skip connections through time may help with long-term dependencies, but they do not guarantee better learning than linear self-connections. Both methods have their strengths and weaknesses depending on the task and data.'
    ),
    'chapter_information': 'Chapter 10: Sequence Modeling'
}

   
#####################

# Conceptual and True/False Questions on Memory-Augmented Networks, Attention Mechanisms, and Transformers

question_122 = {
    'question': (
        'Which of the following is true about memory-augmented networks, like the Neural Turing Machine (NTM)?'
    ),
    'options_list': [
        'A) NTMs rely on standard backpropagation, and explicit memory cells propagate gradients just as in RNNs.',
        'B) The task network in NTMs learns to control the memory by determining where to read and write, using specialized mechanisms for memory addressing.',  # Correct answer
        'C) The memory addressing mechanism in NTMs is always stochastic, making backpropagation impossible.',
        'D) Memory-augmented networks, such as NTMs, are constrained to only move forward through sequences of data, unlike RNNs.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'The task network learns to control the memory and decide where to read and write, using mechanisms similar to attention mechanisms.'
    ),
    'chapter_information': 'Chapter 10: Memory-Augmented Networks'
}

question_123 = {
    'question': (
        'What is a key difference between soft and stochastic memory addressing in neural networks?'
    ),
    'options_list': [
        'A) Soft memory addressing allows for backpropagation, whereas stochastic memory addressing does not allow for any form of optimization.',
        'B) Soft memory addressing uses a weighted average of memory cells, while stochastic memory addressing samples one memory cell based on probabilities.',  # Correct answer
        'C) Stochastic memory addressing always outperforms soft memory addressing due to the lack of gradient vanishing.',
        'D) Both soft and stochastic memory addressing cannot be used in sequence modeling tasks.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Soft memory addressing uses a weighted average of all memory cells, allowing for backpropagation, while stochastic memory addressing samples one cell, using specialized optimization techniques for discrete decisions.'
    ),
    'chapter_information': 'Chapter 10: Memory-Augmented Networks'
}

question_124 = {
    'question': (
        'In the context of neural networks, which of the following is true about attention mechanisms?'
    ),
    'options_list': [
        'A) The first instance of attention mechanisms was introduced for machine translation in 2015 and is used exclusively for translation tasks.',
        'B) Attention mechanisms allow models to focus on different parts of the input sequence dynamically, but only in a forward direction.',
        'C) Attention mechanisms can be used for both sequential data, such as in translation, and tasks with spatial data, like image processing.',  # Correct answer
        'D) Attention mechanisms have replaced recurrent neural networks entirely in sequence modeling, as they provide better performance in every case.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Attention mechanisms are not limited to sequential data but can also be applied to tasks with spatial data, such as image processing.'
    ),
    'chapter_information': 'Chapter 10: Attention Mechanisms'
}

question_125 = {
    'question': (
        'Which of the following is false about the Transformer architecture?'
    ),
    'options_list': [
        'A) The Transformer does not have any recurrence or convolution, relying solely on self-attention mechanisms.',
        'B) Positional encodings are added to the input embeddings in Transformers because they do not have an inherent notion of sequential order.',
        'C) The computational complexity of self-attention is quadratic concerning the sequence length, making it expensive for long sequences.',
        'D) Transformers cannot be used for any task that involves sequence-to-sequence prediction due to their lack of recurrence.'  # Correct answer
    ],
    'correct_answer': 'D',
    'explanation': (
        'Transformers are widely used for sequence-to-sequence prediction tasks, such as translation, even without recurrence.'
    ),
    'chapter_information': 'Chapter 10: Transformer Architecture'
}

question_126 = {
    'question': (
        'Which of the following is the best definition of perplexity in the context of language models?'
    ),
    'options_list': [
        'A) Perplexity measures the uncertainty of a probability distribution, and higher perplexity is always better.',
        'B) Perplexity is the exponential of the negative log-likelihood of a sequence, representing how well a language model predicts a sequence of words.',  # Correct answer
        'C) Perplexity is defined as the average loss over all words in a sequence and must always be lower than cross-entropy.',
        'D) Perplexity is a loss function for training neural networks in machine translation tasks.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Perplexity measures the uncertainty of the model and is the exponential of the cross-entropy loss, with lower perplexity indicating better predictions.'
    ),
    'chapter_information': 'Chapter 10: Perplexity in Language Models'
}

# True/False Questions

question_127 = {
    'question': (
        'True or False: The task network in memory-augmented models like the Neural Turing Machine only learns to read from memory, and writing is performed automatically by the network.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'The task network controls both reading from and writing to the memory using specialized mechanisms.'
    ),
    'chapter_information': 'Chapter 10: Memory-Augmented Networks'
}

question_128 = {
    'question': (
        'True or False: Memory-augmented models allow for more effective handling of long-term dependencies in sequential tasks compared to standard RNNs or LSTMs.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Memory-augmented models can better manage long-term dependencies by explicitly storing and accessing memory.'
    ),
    'chapter_information': 'Chapter 10: Memory-Augmented Networks'
}

question_129 = {
    'question': (
        'True or False: In machine translation, attention mechanisms can focus on different parts of both the input and the output sequences at each time step.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Attention mechanisms allow models to focus dynamically on different parts of the input and output sequences during tasks like machine translation.'
    ),
    'chapter_information': 'Chapter 10: Attention Mechanisms'
}

question_130 = {
    'question': (
        'True or False: In the context of neural networks, the attention mechanism was first introduced for handwriting generation tasks, but later found widespread use in machine translation.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'The attention mechanism was first introduced for handwriting generation by Graves in 2013, then adopted in machine translation by Bahdanau et al. in 2015.'
    ),
    'chapter_information': 'Chapter 10: Attention Mechanisms'
}

question_131 = {
    'question': (
        'True or False: Beam search improves sequence generation by considering the most likely sequence at each step without exploring multiple possible sequences.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Beam search explores the top-k most likely sequences at each step, allowing for more diverse sequence predictions.'
    ),
    'chapter_information': 'Chapter 10: Beam Search'
}

question_132 = {
    'question': (
        'True or False: Byte Pair Encoding (BPE) is a subword tokenization technique that helps handle out-of-vocabulary words by splitting words into more frequent subword units.'
    ),
    'options_list': [
        'A) True',  # Correct answer
        'B) False'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Byte Pair Encoding is used to create subword units that help in dealing with rare or out-of-vocabulary words in language models.'
    ),
    'chapter_information': 'Chapter 10: Byte Pair Encoding'
}

# Challenging Questions on Explicit Memory Networks, Attention Mechanisms, and Neural Turing Machines

question_133 = {
    'question': (
        'Which of the following statements about explicit memory networks is most misleading?'
    ),
    'options_list': [
        'A) Explicit memory in networks allows for storing facts outside of the recurrent part of the model, making information propagation more efficient.',
        'B) Explicit memory networks rely solely on back-propagation through time to propagate gradients across long sequences, making them more scalable.',  # Correct answer
        'C) Using explicit memory, models can store facts in dedicated cells, and task networks control where to read and write, allowing for more complex reasoning tasks.',
        'D) Memory addressing in explicit memory networks can be optimized with either deterministic algorithms or stochastic architectures that rely on discrete decisions.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Explicit memory networks do not solely rely on back-propagation through time for scalability. They leverage mechanisms like attention or stochastic decisions for efficient memory usage.'
    ),
    'chapter_information': 'Chapter 10: Explicit Memory Networks'
}

question_134 = {
    'question': (
        'In explicit memory networks, stochastic reading from memory cells allows for efficient gradient propagation during backpropagation through time.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Stochastic reading from memory cells complicates gradient propagation due to the discrete nature of memory addressing, requiring alternative methods like REINFORCE or other gradient estimators.'
    ),
    'chapter_information': 'Chapter 10: Explicit Memory Networks'
}

question_135 = {
    'question': (
        'Which of the following best captures the role of attention mechanisms in explicit memory models?'
    ),
    'options_list': [
        'A) Attention mechanisms are responsible for ensuring memory cells are updated in a strictly sequential manner, thereby preventing information loss.',
        'B) Attention mechanisms allow the model to selectively focus on different parts of the sequence or memory, regardless of prior attention steps.',  # Correct answer
        'C) Attention mechanisms enforce that only the most recent time step is considered, simplifying the training of sequential data.',
        'D) Attention mechanisms were first introduced in the context of neural Turing machines and do not apply to tasks like machine translation.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'Attention mechanisms allow models to selectively focus on different parts of the sequence or memory, enabling flexible updates and recall from any part of the sequence.'
    ),
    'chapter_information': 'Chapter 10: Attention Mechanisms in Memory Networks'
}

question_136 = {
    'question': (
        'Which of the following is not true about the attention mechanism described in the context of neural networks?'
    ),
    'options_list': [
        'A) The attention mechanism for neural networks was first introduced for handwriting generation but was limited to moving forward through sequences.',
        'B) Attention in machine translation allows the model to focus on a completely different position in the sequence at each step.',
        'C) The attention mechanism used in explicit memory networks ensures deterministic decisions are made at each step, reducing the need for backpropagation.',  # Correct answer
        'D) Whether soft or hard, the mechanism for choosing a memory address in explicit memory networks is closely related to the attention mechanism.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'Attention mechanisms can support both deterministic and stochastic decisions. However, deterministic decisions do not eliminate the need for backpropagation in memory-augmented networks.'
    ),
    'chapter_information': 'Chapter 10: Attention Mechanisms in Memory Networks'
}

question_137 = {
    'question': (
        'In explicit memory networks, training stochastic architectures that make discrete decisions is easier than training deterministic ones that use soft decisions.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Stochastic architectures that make discrete decisions are harder to train because gradients cannot easily propagate through discrete choices, unlike soft decision mechanisms that allow backpropagation.'
    ),
    'chapter_information': 'Chapter 10: Training Stochastic Memory Networks'
}

question_138 = {
    'question': (
        'Which of the following is least likely to be true about the role of task networks in explicit memory models?'
    ),
    'options_list': [
        'A) The task network interacts with the memory cells by deciding where to read and write, effectively controlling memory updates.',
        'B) The task network is responsible for storing long-term information that needs to persist across the sequence, while memory cells handle short-term information.',  # Correct answer
        'C) The task network in an explicit memory model is a representation network, typically recurrent, responsible for manipulating and using stored facts.',
        'D) The task network reads from and writes to memory cells via a mechanism similar to attention, making it capable of flexible memory control.'
    ],
    'correct_answer': 'B',
    'explanation': (
        'In explicit memory models, the memory cells, not the task network, are responsible for storing long-term information, while the task network handles operations like reading and writing.'
    ),
    'chapter_information': 'Chapter 10: Task Networks in Memory Models'
}

question_139 = {
    'question': (
        'Which of the following statements about training explicit memory networks is false?'
    ),
    'options_list': [
        'A) Memory addressing coefficients in explicit memory networks can be interpreted as probabilities, allowing for stochastic reading of a single memory cell.',
        'B) Models with explicit memory are typically harder to train when they make discrete decisions, requiring specialized optimization algorithms.',
        'C) Explicit memory networks require explicit backpropagation through time for training, as stochastic mechanisms do not allow for gradient-based optimization.',  # Correct answer
        'D) Soft decision mechanisms in explicit memory networks are more commonly used since they allow for back-propagation, unlike stochastic hard decisions.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'While explicit memory networks may use backpropagation, they do not always require backpropagation through time. Stochastic mechanisms can still be trained using methods like REINFORCE.'
    ),
    'chapter_information': 'Chapter 10: Training Explicit Memory Networks'
}

question_140 = {
    'question': (
        'In explicit memory models, the writing mechanism is responsible for propagating gradients backward in time, while the reading mechanism is responsible for forward propagation.'
    ),
    'options_list': [
        'A) True',
        'B) False'  # Correct answer
    ],
    'correct_answer': 'B',
    'explanation': (
        'Both reading and writing mechanisms contribute to forward and backward propagation. Writing influences how information is stored, while reading affects how information is used.'
    ),
    'chapter_information': 'Chapter 10: Memory Propagation in Explicit Memory Models'
}

question_141 = {
    'question': (
        'The key challenge when using stochastic reading and writing in explicit memory networks is:'
    ),
    'options_list': [
        'A) Ensuring that stochastic decisions align with the correct memory cells during training, which can lead to unstable gradient propagation.',  # Correct answer
        'B) Making sure that stochastic memory cells are only accessed in the correct sequential order to avoid unnecessary memory overwrites.',
        'C) Guaranteeing that the task network can write to memory cells in real-time, preventing memory from becoming corrupted by noise.',
        'D) Stochastic addressing creates challenges with gradient calculation, since gradients are directly propagated through the weighted averages of memory cells.'
    ],
    'correct_answer': 'A',
    'explanation': (
        'Stochastic reading and writing introduce challenges in ensuring gradients can propagate correctly, which can destabilize learning when memory cells are accessed incorrectly.'
    ),
    'chapter_information': 'Chapter 10: Stochastic Reading and Writing in Memory Networks'
}

question_142 = {
    'question': (
        'Which statement about neural Turing machines (NTM) in the context of explicit memory networks is most accurate?'
    ),
    'options_list': [
        'A) NTMs are restricted to making only soft decisions when addressing memory, as hard decisions would make backpropagation intractable.',
        'B) NTMs rely on recurrent task networks to propagate information both forward and backward through the sequence, similar to bidirectional RNNs.',
        'C) NTMs separate the task of reading and writing into distinct sub-networks, each controlling a different aspect of the memory\'s input-output mechanism.',  # Correct answer
        'D) NTMs use an attention-like mechanism to select which memory cell to read from, but this mechanism only applies in deterministic settings.'
    ],
    'correct_answer': 'C',
    'explanation': (
        'NTMs separate reading and writing into distinct mechanisms, allowing the model to control each aspect of memory interaction independently, making it highly flexible for complex reasoning tasks.'
    ),
    'chapter_information': 'Chapter 10: Neural Turing Machines and Memory Networks'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_12_MPC = KC_MPC_QUESTIONS[:-1]
