
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

WEEK_12_MPC = KC_MPC_QUESTIONS[:-1]
