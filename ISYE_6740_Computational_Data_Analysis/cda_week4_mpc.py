module_4_lecture_transcripts_question_1 = {
    'question': "Which of the following best describes the purpose of PCA as discussed in the lecture?",
    'options_list': [
        'To increase the dimensionality of data to better capture variability',
        'To reduce the dimensionality of data while preserving as much information as possible',
        'To classify data into predefined categories',
        'To calculate the mean and covariance of data without reducing dimensions'
    ],
    'correct_answer': 'To reduce the dimensionality of data while preserving as much information as possible',
    'explanation': "PCA is used for dimensionality reduction, aiming to preserve as much information as possible in the reduced representation.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_2 = {
    'question': "If the dimensionality of the original data is $n$ and PCA reduces it to $k$, which condition must be true?",
    'options_list': [
        '$k \\geq n$',
        '$k \\leq n$',
        '$k = n$',
        'No specific relationship between $k$ and $n$ is required'
    ],
    'correct_answer': '$k \\leq n$',
    'explanation': "PCA reduces the dimensionality to $k$, where $k$ is typically much smaller than $n$, hence $k \\leq n$.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_3 = {
    'question': "True or False: The eigenvalue decomposition is performed on the mean of the dataset in PCA.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': "Eigenvalue decomposition is performed on the covariance matrix of the data, not on the mean.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_4 = {
    'question': "What does the eigenvector of the covariance matrix represent in the context of PCA?",
    'options_list': [
        'Principal directions of data variability',
        'The mean of the dataset',
        'The actual eigenvalues of the dataset',
        'None of the above'
    ],
    'correct_answer': 'Principal directions of data variability',
    'explanation': "Eigenvectors of the covariance matrix represent the principal directions along which the data variability is maximized.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_5 = {
    'question': "In the lecture's MATLAB demo on PCA, what preprocessing step was applied before finding the covariance matrix?",
    'options_list': [
        'Normalization by subtracting the mean',
        'Normalization by dividing by the standard deviation',
        'Both A and B',
        'None of the above'
    ],
    'correct_answer': 'Both A and B',
    'explanation': "In the MATLAB demo, both subtracting the mean and dividing by the standard deviation (feature scaling) were performed as preprocessing steps.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_6 = {
    'question': "True or False: PCA is a nonlinear dimensionality reduction technique.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': "PCA is a linear dimensionality reduction technique as it involves linear transformations of the data.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_7 = {
    'question': "In the context of the PCA demonstration on leaf species, which feature preprocessing steps were performed before computing the covariance matrix?",
    'options_list': [
        'Normalizing by subtracting the mean and dividing by the variance',
        'Scaling features by their standard deviations and subtracting the mean',
        'Log transformation of each feature',
        'Applying a Fourier transform to each feature'
    ],
    'correct_answer': 'Scaling features by their standard deviations and subtracting the mean',
    'explanation': "Before computing the covariance matrix, the features were scaled by their standard deviations and the mean was subtracted from the data points.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_8 = {
    'question': "What is the dimensionality of the dataset used in the leaf species PCA demo, including the number of samples and features?",
    'options_list': [
        '340 samples and 14 features',
        '340 samples and 16 features',
        '320 samples and 14 features',
        '320 samples and 16 features'
    ],
    'correct_answer': '340 samples and 16 features',
    'explanation': "The dataset used in the demo consists of 340 samples, each with 16 features.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_9 = {
    'question': "True or False: The principal components obtained through PCA are guaranteed to capture the majority of the variability in the dataset.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "Principal components are directions that capture the maximum variance in the data, thus reflecting the majority of the dataset's variability.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_10 = {
    'question': "Which of the following best explains why PCA projects data along the direction of highest variability?",
    'options_list': [
        'To ensure minimal loss of information during dimensionality reduction',
        'To increase the computational efficiency of data processing',
        'To eliminate outliers and noise from the data',
        'To simplify the data structure for easier storage'
    ],
    'correct_answer': 'To ensure minimal loss of information during dimensionality reduction',
    'explanation': "PCA projects data along the direction of highest variability to preserve as much information as possible, ensuring minimal loss during dimensionality reduction.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_11 = {
    'question': "What is the purpose of normalizing the weights vector \( W \) in PCA, such that the norm of \( W \) is less than or equal to 1?",
    'options_list': [
        'To prevent overfitting to the training dataset',
        'To ensure that the optimization problem remains bounded and meaningful',
        'To maximize the correlation between original and projected data',
        'To minimize the computational complexity of the eigenvalue decomposition'
    ],
    'correct_answer': 'To ensure that the optimization problem remains bounded and meaningful',
    'explanation': "Normalizing the weights vector \( W \) with a norm less than or equal to 1 ensures that the optimization problem in PCA remains bounded and meaningful, preventing unbounded increases in magnitude.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_12 = {
    'question': "In the PCA example involving class separation along specific projection directions, what does the term 'spread of the data along these directions' refer to?",
    'options_list': [
        'The mean of the data along the projection direction',
        'The covariance between different features along the projection',
        'The variance of the data along the projected direction',
        'The sum of eigenvalues along the projected direction'
    ],
    'correct_answer': 'The variance of the data along the projected direction',
    'explanation': "The spread of the data along specific directions in PCA refers to the variance of the data along these projected directions.",
    'chapter_information': 'Lecture 4 Transcript'
}


module_4_lecture_transcripts_question_13 = {
    'question': "Given a dataset with covariance matrix $C$, if the eigendecomposition of $C$ results in eigenvalues $\lambda_1, \lambda_2, ..., \lambda_d$, with corresponding eigenvectors $u_1, u_2, ..., u_d$, what is the principal component of a data point $x$ in the direction of the first eigenvector?",
    'options_list': [
        '$u_1^T x$',
        '$\lambda_1 u_1^T x$',
        '$u_1^T x / \sqrt{\lambda_1}$',
        '$u_1^T (x - \mu) / \sqrt{\lambda_1}$'
    ],
    'correct_answer': '$u_1^T (x - \mu) / \sqrt{\lambda_1}$',
    'explanation': "The principal component in the direction of the first eigenvector is given by the projection of the data point $x$, adjusted by the mean $\mu$, onto the eigenvector $u_1$, normalized by the square root of its corresponding eigenvalue $\lambda_1$.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_14 = {
    'question': "If a covariance matrix $C$ is expressed as $C = U \Lambda U^T$, where $U$ is a matrix of eigenvectors and $\Lambda$ is a diagonal matrix of eigenvalues, what represents the variance captured by the first principal component?",
    'options_list': [
        'The first row of $U$',
        'The first diagonal element of $\Lambda$',
        'The first column of $U$',
        'The product of the first row of $U$ and the first column of $\Lambda$'
    ],
    'correct_answer': 'The first diagonal element of $\Lambda$',
    'explanation': "The variance captured by the first principal component is represented by the first diagonal element of $\Lambda$, which corresponds to the largest eigenvalue $\lambda_1$.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_15 = {
    'question': "Consider a dataset projected onto the principal components, with $Z = U^T (X - \mu)$ where $U$ contains the principal eigenvectors and $\mu$ is the mean vector. If $X$ is a matrix where rows are data points, what does the element $z_{ij}$ represent in the matrix $Z$?",
    'options_list': [
        'The covariance between the $i^{th}$ and $j^{th}$ data points',
        'The $j^{th}$ principal component of the $i^{th}$ data point',
        'The deviation of the $i^{th}$ data point from the $j^{th}$ mean',
        'The variance of the $i^{th}$ data point along the $j^{th}$ eigenvector'
    ],
    'correct_answer': 'The $j^{th}$ principal component of the $i^{th}$ data point',
    'explanation': "Each element $z_{ij}$ in the matrix $Z$ represents the $j^{th}$ principal component of the $i^{th}$ data point, indicating how much of the $j^{th}$ eigenvector's variance the $i^{th}$ data point captures.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_16 = {
    'question': "In the optimization problem of PCA to find the first principal component, why is the constraint $||w|| \leq 1$ used?",
    'options_list': [
        'To ensure the problem remains bounded and the solution is meaningful',
        'To maximize the correlation between $w$ and the data points',
        'To simplify the calculation of eigenvalues',
        'To minimize the impact of outliers in the dataset'
    ],
    'correct_answer': 'To ensure the problem remains bounded and the solution is meaningful',
    'explanation': "The constraint $||w|| \leq 1$ ensures that the optimization problem remains bounded and the solution is meaningful, preventing uncontrolled growth in the magnitude of $w$, which would make the optimization trivial otherwise.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_17 = {
    'question': "Given a covariance matrix $C$ where $Cw = \lambda w$, and the optimization objective $w^T C w$, what is the expression for the objective function when $Cw = \lambda w$?",
    'options_list': [
        '$\lambda w^T w$',
        '$\lambda^2 w^T w$',
        '$w^T w$',
        '$\lambda w^T \lambda w$'
    ],
    'correct_answer': '$\lambda w^T w$',
    'explanation': "When substituting the equation $Cw = \lambda w$ into the objective function, it simplifies to $w^T C w = w^T \lambda w = \lambda w^T w$, as $w^T \lambda$ is a scalar multiplication and can be moved outside of the dot product.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_18 = {
    'question': "If $C = U \Lambda U^T$ and we are looking for the first principal component, what property must the vector $w_1$ satisfy relative to the matrix $U$?",
    'options_list': [
        '$w_1$ must be the first column of $U$',
        '$w_1$ must be orthogonal to all columns of $U$',
        '$w_1$ must satisfy $U^T w_1 = 1$',
        '$w_1$ can be any column of $U$'
    ],
    'correct_answer': '$w_1$ must be the first column of $U$',
    'explanation': "For the first principal component, $w_1$ should align with the direction of greatest variance, which corresponds to the first column of $U$ associated with the largest eigenvalue $\lambda_1$ in $\Lambda$.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_19 = {
    'question': "In PCA, if the eigenvectors are calculated as $U = [u_1, u_2, \ldots, u_d]$ from the covariance matrix $C$, and $C = U \Lambda U^T$, what does the matrix $\Lambda$ represent?",
    'options_list': [
        'The matrix of covariance between different principal components',
        'A diagonal matrix of eigenvalues representing the variance along each principal component',
        'The correlation matrix between the features of the dataset',
        'A matrix of loadings that transform the original variables into the principal components'
    ],
    'correct_answer': 'A diagonal matrix of eigenvalues representing the variance along each principal component',
    'explanation': "In the context of PCA, $\Lambda$ is a diagonal matrix where each diagonal element (eigenvalue) represents the variance captured along its corresponding principal component (eigenvector) direction.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_20 = {
    'question': "Considering the PCA optimization problem, how does the requirement that eigenvectors be orthogonal relate to the covariance matrix $C$?",
    'options_list': [
        'It ensures that the covariance matrix $C$ is symmetric',
        'It guarantees that the eigenvectors of $C$ are orthogonal due to the properties of symmetric matrices',
        'It is necessary for $C$ to have a full set of distinct eigenvalues',
        'It simplifies the computation of the inverse of $C$'
    ],
    'correct_answer': 'It guarantees that the eigenvectors of $C$ are orthogonal due to the properties of symmetric matrices',
    'explanation': "In PCA, the covariance matrix $C$ is symmetric. Symmetric matrices have the property that their eigenvectors are orthogonal to each other, a critical aspect for defining principal components that capture independent variance directions.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_21 = {
    'question': "In the context of PCA using Singular Value Decomposition (SVD), what does the matrix $\Sigma$ in the decomposition $M = U \Sigma V^T$ represent?",
    'options_list': [
        'The matrix of covariance between different principal components',
        'A diagonal matrix containing the square roots of the eigenvalues of $MM^T$',
        'The correlation matrix between the features of the dataset',
        'The matrix of loadings for the principal components'
    ],
    'correct_answer': 'A diagonal matrix containing the square roots of the eigenvalues of $MM^T$',
    'explanation': "In SVD used in PCA, $\Sigma$ contains the singular values, which are the square roots of the eigenvalues of the matrix $MM^T$, representing the standard deviations along the principal components.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_22 = {
    'question': "If the objective function in PCA is maximized using Lagrangian optimization, what does the Lagrange multiplier $\lambda$ represent in the equation $Cw = \lambda w$?",
    'options_list': [
        'The constraint that the norm of $w$ must be less than or equal to 1',
        'The maximum variance along the principal component',
        'A penalty for violating the constraint on the norm of $w$',
        'The eigenvalue corresponding to the eigenvector $w$'
    ],
    'correct_answer': 'The eigenvalue corresponding to the eigenvector $w$',
    'explanation': "In the context of PCA, the Lagrange multiplier $\lambda$ in the equation $Cw = \lambda w$ actually represents the eigenvalue associated with the eigenvector $w$, indicating the variance along that principal component.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_23 = {
    'question': "Given a matrix $M$ and its SVD as $M = U \Sigma V^T$, how can the columns of $V$ be interpreted in the context of PCA?",
    'options_list': [
        'As principal components of $M$',
        'As left singular vectors representing the rotation in the feature space',
        'As right singular vectors representing the axis of the data in the original feature space',
        'As coefficients for linear combinations of the original data columns'
    ],
    'correct_answer': 'As right singular vectors representing the axis of the data in the original feature space',
    'explanation': "In SVD used in PCA, the columns of $V$ (right singular vectors) represent the axes or directions in the original feature space along which data variability is maximized.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_24 = {
    'question': "In PCA, if the Lagrangian for the optimization problem is given by $L = w^T Cw - \lambda (||w||^2 - 1)$, what does setting the derivative $\frac{\partial L}{\partial w} = 0$ help us find?",
    'options_list': [
        'The weight vector $w$ that maximizes the variance of projected data',
        'The minimum eigenvalue of the covariance matrix $C$',
        'The mean vector of the data points',
        'The least significant principal component'
    ],
    'correct_answer': 'The weight vector $w$ that maximizes the variance of projected data',
    'explanation': "Setting $\frac{\partial L}{\partial w} = 0$ in the Lagrangian optimization problem of PCA helps find the weight vector $w$ that maximizes the variance of the data when projected onto $w$, aligning with the principal component that captures the most variance.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_4_lecture_transcripts_question_25 = {
    'question': "What is the relationship between the eigenvalues of a covariance matrix $C$ and the singular values of the data matrix $M$ in the context of PCA performed via SVD?",
    'options_list': [
        'Eigenvalues of $C$ are the squares of the singular values of $M$',
        'Singular values of $M$ are the square roots of the eigenvalues of $C$',
        'Eigenvalues of $C$ are the inverse of the singular values of $M$',
        'There is no direct relationship between the eigenvalues of $C$ and the singular values of $M$'
    ],
    'correct_answer': 'Eigenvalues of $C$ are the squares of the singular values of $M$',
    'explanation': "In the context of PCA, when it is performed using SVD, the eigenvalues of the covariance matrix $C$ are equal to the squares of the singular values of the data matrix $M$, reflecting the variance captured along each principal component.",
    'chapter_information': 'Lecture 4 Transcript'
}

module_12_1_bishop_book_question_1 = {
    'question': "What does the covariance matrix \( S \) represent in the context of PCA?",
    'options_list': [
        'The matrix of correlations between different features',
        'A diagonal matrix containing the variances of each feature',
        'The matrix capturing variability and covariance between different dimensions of the data',
        'The correlation matrix scaled by the variance of each feature'
    ],
    'correct_answer': 'The matrix capturing variability and covariance between different dimensions of the data',
    'explanation': "In PCA, the covariance matrix \( S \) represents the measure of variability and the covariance between the different dimensions or features of the data.",
    'chapter_information': 'Bishop Book 12.1'
}

module_12_1_bishop_book_question_2 = {
    'question': "How is the matrix \( \Sigma \) related to the eigenvalues of the covariance matrix in the context of SVD used in PCA?",
    'options_list': [
        'The elements of \( \Sigma \) are the square roots of the eigenvalues of the covariance matrix.',
        'The elements of \( \Sigma \) are the eigenvalues themselves.',
        'The elements of \( \Sigma \) are the inverse of the eigenvalues of the covariance matrix.',
        'There is no direct relationship; \( \Sigma \) and eigenvalues are independent.'
    ],
    'correct_answer': 'The elements of \( \Sigma \) are the square roots of the eigenvalues of the covariance matrix.',
    'explanation': "In PCA, when using SVD, \( \Sigma \) contains the singular values, which are the square roots of the eigenvalues of the covariance matrix created from the data matrix.",
    'chapter_information': 'Bishop Book 12.1'
}

module_12_1_bishop_book_question_3 = {
    'question': "What is the purpose of using a Lagrange multiplier in the optimization problem of PCA?",
    'options_list': [
        'To ensure that the principal components are orthogonal to each other',
        'To maximize the variance along each principal component',
        'To enforce the constraint that the principal component vectors have unit length',
        'To minimize the computational complexity of finding principal components'
    ],
    'correct_answer': 'To enforce the constraint that the principal component vectors have unit length',
    'explanation': "In PCA, the Lagrange multiplier is used to enforce the unit length constraint on the principal component vectors, ensuring that the optimization problem remains bounded and meaningful.",
    'chapter_information': 'Bishop Book 12.1'
}

module_12_1_bishop_book_question_4 = {
    'question': "What does the matrix \( V \) from the SVD \( M = U \Sigma V^T \) represent in PCA?",
    'options_list': [
        'It contains the principal components of the data matrix \( M \).',
        'It holds the left singular vectors that correspond to the basis in the feature space.',
        'It includes the right singular vectors that represent the directions or axes in the original feature space.',
        'It is a diagonal matrix with singular values that denote the importance of each principal component.'
    ],
    'correct_answer': 'It includes the right singular vectors that represent the directions or axes in the original feature space.',
    'explanation': "In the Singular Value Decomposition used in PCA, the matrix \( V \) (right singular vectors) represents the directions or axes in the original feature space, along which the data variability is maximized.",
    'chapter_information': 'Bishop Book 12.1'
}

module_12_1_bishop_book_question_5 = {
    'question': "In the minimum-error formulation of PCA, what does the expression \( J = \sum_{i=M+1}^D u_i^T S u_i \) represent?",
    'options_list': [
        'The total variance explained by the first \( M \) principal components',
        'The remaining variance in the data after projecting onto the first \( M \) principal components',
        'The error between the original data points and their projections onto the principal subspace',
        'The cumulative variance of the data along the directions orthogonal to the principal subspace'
    ],
    'correct_answer': 'The remaining variance in the data after projecting onto the first \( M \) principal components',
    'explanation': "This expression represents the remaining variance in the data that is not captured by the first \( M \) principal components, reflecting the distortion or projection error minimized in PCA.",
    'chapter_information': 'Bishop Book 12.1'
}





KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_4_MPC = KC_MPC_QUESTIONS[:-1]
