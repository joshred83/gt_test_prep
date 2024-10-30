
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

WEEK_14_MPC = KC_MPC_QUESTIONS[:-1]
