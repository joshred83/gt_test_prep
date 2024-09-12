lecture_5_isomap_question_1 = {
    'question': "Why is the Euclidean distance insufficient for datasets with nonlinear structures such as the Swiss Roll dataset?",
    'options_list': [
        "A) Euclidean distance only captures short-range relationships.",
        "B) Euclidean distance does not consider the geometry of the data.",
        "C) Euclidean distance can only be used in linear dimensionality reduction methods.",
        "D) Euclidean distance becomes unstable with high-dimensional data."
    ],
    'correct_answer': 'B',
    'explanation': "In nonlinear structures, Euclidean distance does not account for the true geometric relationships in the data, such as the 'walking distance' or geodesic distance in the Swiss Roll dataset.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_2 = {
    'question': "What is the purpose of constructing the weighted nearest neighbor graph in the ISOMAP algorithm?",
    'options_list': [
        "A) To identify K-nearest neighbors for each data point.",
        "B) To compute geodesic distances between data points.",
        "C) To reduce the dimensionality of the data.",
        "D) To ensure the dataset has the correct number of neighbors."
    ],
    'correct_answer': 'B',
    'explanation': "The weighted nearest neighbor graph is used to compute geodesic distances between data points, which are essential for preserving the nonlinear structure of the data.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_3 = {
    'question': "In ISOMAP, what is the role of the matrix $H = I - \\frac{1}{n} 11^T$?",
    'options_list': [
        "A) To compute the geodesic distances between data points.",
        "B) To normalize the data points.",
        "C) To center the data points by removing the mean.",
        "D) To scale the eigenvectors."
    ],
    'correct_answer': 'C',
    'explanation': "The matrix $H$ is used to center the data points, meaning it subtracts the mean from each point, which is crucial for dimensionality reduction.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_4 = {
    'question': "Given a distance matrix $D$ of size $m \\times m$, and the centering matrix $H$, the ISOMAP algorithm constructs the matrix $C$ as $C = -\\frac{1}{2} H D^2$. What does this matrix $C$ represent?",
    'options_list': [
        "A) The weighted adjacency matrix of the nearest neighbor graph.",
        "B) The pairwise geodesic distances squared.",
        "C) The Euclidean distances between data points.",
        "D) The centered pairwise geodesic distances."
    ],
    'correct_answer': 'D',
    'explanation': "The matrix $C = -\\frac{1}{2} H D^2$ represents the centered pairwise geodesic distances between data points, which are used to capture the structure of the data.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_5 = {
    'question': "In the ISOMAP algorithm, after constructing the matrix $C$, the next step is to compute the eigenvectors and eigenvalues of $C$. Why are the top $K$ eigenvectors chosen?",
    'options_list': [
        "A) To ensure the eigenvalues are positive.",
        "B) To reduce the dimensionality to $K$ dimensions.",
        "C) To find the eigenvectors with the smallest eigenvalues.",
        "D) To scale the data to the original dimensions."
    ],
    'correct_answer': 'B',
    'explanation': "The top $K$ eigenvectors are chosen to reduce the dimensionality of the data to $K$ dimensions, as these eigenvectors capture the most important variance in the data.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_6 = {
    'question': "In K-ISOMAP, what is the advantage of using a K-nearest neighbors approach over an $\\epsilon$-neighborhood approach?",
    'options_list': [
        "A) K-nearest neighbors guarantee each point has the same number of neighbors.",
        "B) K-nearest neighbors are faster to compute.",
        "C) K-nearest neighbors work better with dense datasets.",
        "D) K-nearest neighbors avoid overfitting to the data."
    ],
    'correct_answer': 'A',
    'explanation': "In K-ISOMAP, using K-nearest neighbors ensures that each point has at least $K$ neighbors, which is beneficial for sparse datasets where points may be far apart.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_tf_question_1 = {
    'question': "In ISOMAP, geodesic distance is used instead of Euclidean distance to better capture the true structure of nonlinear datasets like the Swiss Roll.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "Geodesic distance accounts for the data's manifold structure, making it more suitable for nonlinear datasets compared to Euclidean distance.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_tf_question_2 = {
    'question': "The final dimensionality reduction in ISOMAP is achieved by selecting the eigenvectors with the smallest eigenvalues.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "In ISOMAP, the eigenvectors with the largest eigenvalues are selected, as they represent the directions of maximum variance in the data.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_tf_question_3 = {
    'question': "The purpose of using the matrix $H$ in ISOMAP is to compute the Euclidean distance between data points.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The matrix $H$ is used for centering the data, not for computing Euclidean distances.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}


lecture_5_isomap_question_7 = {
    'question': "What is the primary purpose of the geodesic distance in the ISOMAP algorithm?",
    'options_list': [
        "A) To calculate the Euclidean distance between points in the original high-dimensional space.",
        "B) To approximate the true distance between points that are connected by a manifold structure.",
        "C) To construct a nearest neighbor graph using the Euclidean distance.",
        "D) To reduce the computational complexity of dimensionality reduction."
    ],
    'correct_answer': 'B',
    'explanation': "Geodesic distance approximates the true distance between points on a manifold by considering the shortest path over the data's geometry, not just straight-line Euclidean distance.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_8 = {
    'question': "What does the **D** matrix represent in the ISOMAP algorithm?",
    'options_list': [
        "A) The adjacency matrix of the nearest neighbor graph.",
        "B) The pairwise geodesic distances between data points.",
        "C) The original Euclidean distances between data points.",
        "D) The eigenvectors of the data points."
    ],
    'correct_answer': 'B',
    'explanation': "The **D** matrix in ISOMAP represents the pairwise geodesic distances, capturing how far apart data points are in terms of the data manifold.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_9 = {
    'question': "The ISOMAP algorithm involves the construction of a weighted nearest neighbor graph. What is the purpose of weighting the graph?",
    'options_list': [
        "A) To ensure each point has the same number of neighbors.",
        "B) To measure the geodesic distance by accumulating the local distances between neighbors.",
        "C) To make the graph symmetric.",
        "D) To apply regularization to the dimensionality reduction process."
    ],
    'correct_answer': 'B',
    'explanation': "Weighting the nearest neighbor graph allows ISOMAP to accumulate the local distances between neighbors, which are used to calculate the geodesic distances.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_10 = {
    'question': "The matrix \( C = -\\frac{1}{2} H D^2 \) in ISOMAP is derived from the pairwise distance matrix **D**. What role does the matrix **H** play in this formulation?",
    'options_list': [
        "A) It scales the geodesic distances.",
        "B) It centers the data by removing the mean.",
        "C) It ensures that the distance matrix is symmetric.",
        "D) It normalizes the data by dividing by the standard deviation."
    ],
    'correct_answer': 'B',
    'explanation': "The matrix **H** centers the data, ensuring that the mean of the data points is removed, which is essential for dimensionality reduction.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_11 = {
    'question': "After computing the matrix **C** in ISOMAP, what is the next step in reducing the dimensionality of the data?",
    'options_list': [
        "A) Applying principal component analysis (PCA) to the matrix **C**.",
        "B) Finding the geodesic distance using Dijkstra's algorithm.",
        "C) Performing eigen-decomposition on the matrix **C** to obtain the top eigenvectors.",
        "D) Constructing the nearest neighbor graph based on geodesic distances."
    ],
    'correct_answer': 'C',
    'explanation': "After constructing **C**, the ISOMAP algorithm performs eigen-decomposition to find the top eigenvectors, which are used to represent the data in a lower-dimensional space.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_question_12 = {
    'question': "What does the eigenvector decomposition in ISOMAP achieve?",
    'options_list': [
        "A) It minimizes the geodesic distance between data points.",
        "B) It finds the new coordinates of the data points in a lower-dimensional Euclidean space.",
        "C) It constructs the adjacency matrix for the nearest neighbor graph.",
        "D) It normalizes the data to improve the dimensionality reduction."
    ],
    'correct_answer': 'B',
    'explanation': "The eigen-decomposition in ISOMAP is used to find new coordinates for the data points in a lower-dimensional Euclidean space while preserving the pairwise geodesic distances.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_tf_question_4 = {
    'question': "In ISOMAP, the Euclidean distance is used to compute the geodesic distance between points in the nearest neighbor graph.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "The Euclidean distance is only used locally in the nearest neighbor graph, but the geodesic distance, which is the shortest path distance through the manifold, is computed for the full dataset.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_tf_question_5 = {
    'question': "The MDS (Multidimensional Scaling) algorithm used in ISOMAP helps in constructing new coordinates by preserving the pairwise geodesic distances.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'True',
    'explanation': "MDS reconstructs the coordinates of the data points in a lower-dimensional space while preserving the geodesic distances from the high-dimensional space.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}

lecture_5_isomap_tf_question_6 = {
    'question': "In ISOMAP, the eigen-decomposition step only uses the eigenvectors with the smallest eigenvalues to reduce the dimensionality of the data.",
    'options_list': [
        "True",
        "False"
    ],
    'correct_answer': 'False',
    'explanation': "ISOMAP selects the eigenvectors with the largest eigenvalues because they capture the most important variance in the data.",
    'chapter_information': 'Lecture 5: Nonlinear Dimensionality Reduction (ISOMAP)'
}


isomap_paper_question_1 = {
    'question': "In the Isomap algorithm, what is the purpose of the matrix \( H = I - \\frac{1}{m} \\mathbf{1} \\mathbf{1}^T \)?",
    'options_list': [
        "A) It centers the data points by removing the mean.",
        "B) It scales the geodesic distances.",
        "C) It computes the adjacency matrix for the nearest neighbor graph.",
        "D) It normalizes the data by dividing by the standard deviation."
    ],
    'correct_answer': 'A',
    'explanation': "The matrix \( H \) is used in the Isomap algorithm to center the data points by removing the mean, a crucial step for dimensionality reduction.",
    'chapter_information': 'Isomap Paper'
}

isomap_paper_question_2 = {
    'question': "The Isomap algorithm relies on the geodesic distance. How is the geodesic distance between two points calculated in Isomap?",
    'options_list': [
        "A) By directly measuring the Euclidean distance between the points.",
        "B) By summing the shortest path distances through the nearest neighbor graph.",
        "C) By using principal component analysis (PCA) to approximate the distances.",
        "D) By constructing a weighted graph of all the data points and computing the Frobenius norm."
    ],
    'correct_answer': 'B',
    'explanation': "In Isomap, the geodesic distance between two points is calculated as the shortest path through the nearest neighbor graph.",
    'chapter_information': 'Isomap Paper'
}

isomap_paper_question_3 = {
    'question': "Given that the geodesic distance matrix \( D \) is \( m \\times m \), how is the matrix \( C = - \\frac{1}{2} H D^2 H \) constructed?",
    'options_list': [
        "A) By squaring each entry in the distance matrix \( D \), applying the centering matrix \( H \), and scaling by \( -\\frac{1}{2} \).",
        "B) By normalizing the distance matrix \( D \) and then applying singular value decomposition (SVD).",
        "C) By calculating the inverse of the geodesic distance matrix \( D \) and applying it to the original data.",
        "D) By applying the eigenvectors of \( D \) to the adjacency matrix of the graph."
    ],
    'correct_answer': 'A',
    'explanation': "The matrix \( C \) is constructed by squaring each entry of the geodesic distance matrix \( D \), applying the centering matrix \( H \), and scaling by \( -\\frac{1}{2} \).",
    'chapter_information': 'Isomap Paper'
}

isomap_paper_question_4 = {
    'question': "In the final step of Isomap, what is the goal of performing eigen-decomposition on the matrix \( C \)?",
    'options_list': [
        "A) To identify the principal components of the data and reduce dimensionality.",
        "B) To compute the pairwise distances between the data points.",
        "C) To find the eigenvectors that correspond to the reduced representation of the data in the lower-dimensional space.",
        "D) To ensure that the geodesic distances are preserved in the new coordinate system."
    ],
    'correct_answer': 'C',
    'explanation': "Eigen-decomposition of the matrix \( C \) allows us to find the eigenvectors that correspond to the reduced representation of the data in a lower-dimensional space.",
    'chapter_information': 'Isomap Paper'
}

isomap_paper_question_5 = {
    'question': "The Isomap algorithm is guaranteed to converge to the true manifold under what conditions?",
    'options_list': [
        "A) When the input data are uniformly distributed across the high-dimensional space.",
        "B) When the graph distances approximate the geodesic distances as the number of data points increases.",
        "C) When the PCA algorithm is used to initialize the nearest neighbor graph.",
        "D) When the radius of curvature of the manifold is minimized during the distance computation."
    ],
    'correct_answer': 'B',
    'explanation': "Isomap is guaranteed to converge to the true manifold as the number of data points increases, causing the graph distances to approximate the true geodesic distances.",
    'chapter_information': 'Isomap Paper'
}

isomap_paper_question_6 = {
    'question': "What is the primary benefit of using geodesic distances over Euclidean distances in the Isomap algorithm?",
    'options_list': [
        "A) Geodesic distances capture the global structure of nonlinear manifolds, while Euclidean distances only capture local relationships.",
        "B) Geodesic distances are faster to compute than Euclidean distances.",
        "C) Geodesic distances minimize the variance in the high-dimensional data.",
        "D) Geodesic distances simplify the process of constructing the nearest neighbor graph."
    ],
    'correct_answer': 'A',
    'explanation': "Geodesic distances capture the global structure of nonlinear manifolds, which is crucial in preserving the true geometry of the data, unlike Euclidean distances that only capture local relationships.",
    'chapter_information': 'Isomap Paper'
}

isomap_paper_question_7 = {
    'question': "What role do the eigenvalues and eigenvectors play in the dimensionality reduction process of the Isomap algorithm?",
    'options_list': [
        "A) Eigenvalues determine the weights of the new dimensions, while eigenvectors represent the directions of maximum variance.",
        "B) Eigenvalues and eigenvectors are used to compute the distance matrix for the new lower-dimensional representation.",
        "C) Eigenvectors determine the centroids of each cluster in the reduced space.",
        "D) Eigenvalues are used to rescale the original data points, and eigenvectors identify the principal components."
    ],
    'correct_answer': 'A',
    'explanation': "In Isomap, the eigenvalues determine the weights of the new dimensions in the lower-dimensional space, while the eigenvectors represent the directions of maximum variance.",
    'chapter_information': 'Isomap Paper'
}





KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
