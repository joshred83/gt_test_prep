module_3_lecture_notes_question_1x = {
    'question': "What is the main limitation of k-means clustering demonstrated with the two-ring dataset?",
    'options_list': [
        'It cannot find centroids',
        'It fails to identify non-linear clusters',
        'It is too slow for large datasets',
        'It cannot handle weighted graphs'
    ],
    'correct_answer': 'It fails to identify non-linear clusters',
    'explanation': "K-means clustering struggles with complex data structures, such as the two-ring dataset, where it fails to correctly identify the clusters.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_2x = {
    'question': "Which of the following best describes spectral clustering?",
    'options_list': [
        'A supervised learning method',
        'A method that relies on the spectrum of the graph Laplacian',
        'A technique that only works on unweighted graphs',
        'An alternative name for k-means clustering'
    ],
    'correct_answer': 'A method that relies on the spectrum of the graph Laplacian',
    'explanation': "Spectral clustering is an unsupervised method that uses the spectrum of the graph Laplacian to identify clusters.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_3x = {
    'question': "In the context of spectral clustering, what is an adjacency matrix used for?",
    'options_list': [
        'To measure the distance between centroids',
        'To represent the connections between nodes in a graph',
        'To determine the weights of edges in an unweighted graph',
        'To initialize the centroids in k-means clustering'
    ],
    'correct_answer': 'To represent the connections between nodes in a graph',
    'explanation': "An adjacency matrix represents the connections (edges) between nodes in a graph, crucial for understanding the structure of the network in spectral clustering.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_4x = {
    'question': "Which type of graph has a symmetrical adjacency matrix?",
    'options_list': [
        'Directed graph',
        'Weighted graph',
        'Undirected graph',
        'Non-binary graph'
    ],
    'correct_answer': 'Undirected graph',
    'explanation': "In an undirected graph, edges have no direction, resulting in a symmetrical adjacency matrix.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_5x = {
    'question': "What assumption is typically made about communities in a social network when applying spectral clustering?",
    'options_list': [
        'Communities are weakly connected across different nodes',
        'Communities tend to have fewer edges within them',
        'Communities are strongly connected within themselves',
        'Communities are defined by the number of nodes rather than connections'
    ],
    'correct_answer': 'Communities are strongly connected within themselves',
    'explanation': "Spectral clustering assumes that members of the same community are more interconnected, leading to a denser cluster of edges.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_6x = {
    'question': "Which of the following is NOT true about weighted graphs?",
    'options_list': [
        'The adjacency matrix can have non-binary values',
        'They represent the strength of connections between nodes',
        'The adjacency matrix is always symmetrical',
        'Weighted graphs can be used in machine learning algorithms to represent tight connections'
    ],
    'correct_answer': 'The adjacency matrix is always symmetrical',
    'explanation': "Weighted graphs can have non-symmetrical adjacency matrices, especially in the case of directed graphs where edge weights may differ based on direction.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_7x = {
    'question': "What is the primary difference between directed and undirected graphs?",
    'options_list': [
        'Directed graphs are always unweighted',
        'Directed graphs have edges with specific directions',
        'Undirected graphs are only used in spectral clustering',
        'Directed graphs cannot have an adjacency matrix'
    ],
    'correct_answer': 'Directed graphs have edges with specific directions',
    'explanation': "In directed graphs, edges point from one node to another, whereas in undirected graphs, edges have no direction and are bidirectional.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_1 = {
    'question': "What is the primary role of the graph Laplacian in spectral clustering?",
    'options_list': [
        'To find the centroids of clusters',
        'To measure the connectivity of nodes in a graph',
        'To compute the distance between data points',
        'To initialize the k-means algorithm'
    ],
    'correct_answer': 'To measure the connectivity of nodes in a graph',
    'explanation': "The graph Laplacian measures how connected the nodes are in the graph, which is crucial for identifying clusters in spectral clustering.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_2 = {
    'question': "How is the degree matrix D defined in the context of an undirected graph?",
    'options_list': [
        'As a matrix of all zeros',
        'As a matrix with the sum of edge weights on the diagonal',
        'As a diagonal matrix with vertex degrees on the diagonal',
        'As the inverse of the adjacency matrix'
    ],
    'correct_answer': 'As a diagonal matrix with vertex degrees on the diagonal',
    'explanation': "The degree matrix D is a diagonal matrix where each diagonal entry represents the degree of the corresponding vertex.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_3 = {
    'question': "What does the multiplicity of the eigenvalue 0 in the graph Laplacian indicate?",
    'options_list': [
        'The number of clusters',
        'The number of edges in the graph',
        'The number of disconnected components in the graph',
        'The total number of nodes'
    ],
    'correct_answer': 'The number of disconnected components in the graph',
    'explanation': "The multiplicity of the eigenvalue 0 corresponds to the number of disconnected components in the graph, which spectral clustering uses to identify clusters.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_4 = {
    'question': "Which of the following statements about eigenvectors in spectral clustering is correct?",
    'options_list': [
        'Eigenvectors associated with the smallest eigenvalues provide information about cluster centroids.',
        'Eigenvectors associated with the largest eigenvalues indicate noise in the data.',
        'Eigenvectors associated with eigenvalue 0 correspond to the same connected component in the graph.',
        'Eigenvectors are irrelevant in spectral clustering.'
    ],
    'correct_answer': 'Eigenvectors associated with eigenvalue 0 correspond to the same connected component in the graph.',
    'explanation': "Eigenvectors corresponding to the eigenvalue 0 indicate which nodes belong to the same connected component or cluster in the graph.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_5 = {
    'question': "Why might the graph Laplacian be redefined as L = D^{-1/2} × (D - A) × D^{-1/2} in some spectral clustering variants?",
    'options_list': [
        'To make the eigenvalues smaller',
        'To improve numerical stability when node degrees vary significantly',
        'To simplify the computation of the adjacency matrix',
        'To increase the rank of the Laplacian matrix'
    ],
    'correct_answer': 'To improve numerical stability when node degrees vary significantly',
    'explanation': "This redefinition helps to stabilize the numerical properties of the spectral clustering process, especially when the node degrees are very different.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_6 = {
    'question': "In spectral clustering, what is the purpose of computing the smallest eigenvalues of the graph Laplacian?",
    'options_list': [
        'To determine the optimal number of clusters',
        'To identify the largest connected component in the graph',
        'To find the most central nodes in the graph',
        'To generate feature vectors for clustering'
    ],
    'correct_answer': 'To generate feature vectors for clustering',
    'explanation': "The smallest eigenvalues are used to identify the structure of the clusters, which is then used to create feature vectors for further clustering.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_7 = {
    'question': "Which of the following is true about the nearest neighbor graph used in spectral clustering?",
    'options_list': [
        'It is used to find the centroids of clusters.',
        'It connects each data point to all other points in the dataset.',
        'It connects data points that are within a specified distance or among the k-nearest neighbors.',
        'It ignores the actual distances between data points.'
    ],
    'correct_answer': 'It connects data points that are within a specified distance or among the k-nearest neighbors.',
    'explanation': "The nearest neighbor graph connects data points that are close to each other based on a specified distance metric, which helps in capturing local connectivity.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_8 = {
    'question': "How does spectral clustering handle real-world networks where clusters are not perfectly disconnected?",
    'options_list': [
        'It disregards the weak connections between clusters.',
        'It uses the eigenvectors associated with small but non-zero eigenvalues.',
        'It applies k-means clustering directly to the raw data.',
        'It increases the size of the clusters to include more nodes.'
    ],
    'correct_answer': 'It uses the eigenvectors associated with small but non-zero eigenvalues.',
    'explanation': "In real-world networks, clusters might be weakly connected, and spectral clustering uses eigenvectors corresponding to small eigenvalues to identify these clusters.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_9 = {
    'question': "What is the relationship between the number of small eigenvalues and the number of clusters in spectral clustering?",
    'options_list': [
        'The number of small eigenvalues is always greater than the number of clusters.',
        'The number of small eigenvalues is equal to the number of clusters.',
        'The number of small eigenvalues has no relation to the number of clusters.',
        'The number of small eigenvalues is less than the number of clusters.'
    ],
    'correct_answer': 'The number of small eigenvalues is equal to the number of clusters.',
    'explanation': "In spectral clustering, the number of small eigenvalues (close to zero) typically corresponds to the number of clusters in the data.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_10 = {
    'question': "In the context of spectral clustering, what does it mean for two nodes to have 'similar' feature vectors?",
    'options_list': [
        'They belong to different clusters.',
        'They have the same degree.',
        'They are likely part of the same cluster.',
        'They have the same eigenvalue.'
    ],
    'correct_answer': 'They are likely part of the same cluster.',
    'explanation': "In spectral clustering, similar feature vectors suggest that the nodes belong to the same cluster.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_11 = {
    'question': "Given a simple undirected graph with 4 nodes and the following adjacency matrix:\nA = [[0, 1, 0, 0],\n[1, 0, 1, 0],\n[0, 1, 0, 1],\n[0, 0, 1, 0]],\ncompute the degree matrix D and the graph Laplacian L = D - A. What are the eigenvalues of L?",
    'options_list': [],
    'correct_answer': 'Degree matrix D = diag([1, 2, 2, 1]),\nGraph Laplacian L = [[1, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 1]],\nEigenvalues: 0, 1, 3, 4',
    'explanation': "The degree matrix is calculated by summing the connections for each node, and the graph Laplacian is the difference between the degree matrix and the adjacency matrix. The eigenvalues are found by solving the characteristic equation for L.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_12 = {
    'question': "For the graph Laplacian L = D - A of a graph with 5 nodes, suppose the eigenvalues of L are λ1 = 0, λ2 = 0, λ3 = 2, λ4 = 3, λ5 = 5. How many connected components does the graph have?",
    'options_list': [
        '1',
        '2',
        '3',
        '5'
    ],
    'correct_answer': '2',
    'explanation': "The number of connected components in the graph corresponds to the number of eigenvalues equal to 0.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_13 = {
    'question': "Consider a dataset represented by a 6-node graph with the following degree matrix D and adjacency matrix A:\nD = diag([3, 2, 2, 1, 2, 1]),\nA = [[0, 1, 1, 0, 1, 0],\n[1, 0, 0, 0, 1, 0],\n[1, 0, 0, 1, 0, 0],\n[0, 0, 1, 0, 0, 1],\n[1, 1, 0, 0, 0, 0],\n[0, 0, 0, 1, 0, 0]].\nCompute the graph Laplacian L = D - A. What does the multiplicity of the eigenvalue 0 indicate about the graph's structure?",
    'options_list': [],
    'correct_answer': 'Graph Laplacian L = [[3, -1, -1, 0, -1, 0], [-1, 2, 0, 0, -1, 0], [-1, 0, 2, -1, 0, 0], [0, 0, -1, 1, 0, -1], [-1, -1, 0, 0, 2, 0], [0, 0, 0, -1, 0, 1]],\nMultiplicity of the eigenvalue 0 indicates 2 connected components.',
    'explanation': "The graph Laplacian is calculated by subtracting the adjacency matrix from the degree matrix. The number of eigenvalues equal to 0 indicates the number of disconnected components in the graph.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_14 = {
    'question': "If a graph Laplacian has eigenvalues λ1 = 0, λ2 = 0.01, λ3 = 0.02, λ4 = 1.5, λ5 = 3.0, how many clusters might you expect to find in the data? Justify your answer.",
    'options_list': [
        '1',
        '2',
        '3',
        '5'
    ],
    'correct_answer': '2',
    'explanation': "The small eigenvalues (close to 0) suggest that there are likely 2 clusters in the data.",
    'chapter_information': 'Module 3 Lecture Notes'
}

module_3_lecture_notes_question_15 = {
    'question': "For a graph with 10 nodes, you find that the Laplacian matrix has three eigenvalues very close to zero (λ1 = 0, λ2 = 0.001, λ3 = 0.002). How would you determine the number of clusters, and what additional steps would you take in the spectral clustering process?",
    'options_list': [],
    'correct_answer': "The three small eigenvalues indicate the presence of three clusters. After identifying the clusters, you would form the matrix Z from the corresponding eigenvectors and apply k-means clustering to assign the nodes to clusters.",
    'explanation': "Small eigenvalues indicate the number of clusters. The corresponding eigenvectors are used to form feature vectors for the nodes, which are then clustered using k-means.",
    'chapter_information': 'Module 3 Lecture Notes'
}

esl_2_lecture_notes_question_1 = {
    'question': "In the context of spectral clustering, why might traditional methods like K-means fail when dealing with non-convex clusters?",
    'options_list': [
        'K-means only considers Euclidean distance, which is not suitable for non-convex shapes.',
        'K-means assumes all clusters are of equal size.',
        'K-means cannot handle high-dimensional data.',
        'K-means requires the number of clusters to be specified in advance.'
    ],
    'correct_answer': 'K-means only considers Euclidean distance, which is not suitable for non-convex shapes.',
    'explanation': "Traditional methods like K-means rely on spherical or elliptical metrics, which do not work well for non-convex clusters such as concentric circles.",
    'chapter_information': 'ESL 2'
}

esl_2_lecture_notes_question_2 = {
    'question': "What is the primary role of the graph Laplacian in spectral clustering?",
    'options_list': [
        'To transform the data points into a new space where clustering is easier.',
        'To compute the pairwise distances between data points.',
        'To determine the connectivity between nodes in the similarity graph.',
        'To initialize the centroids for K-means clustering.'
    ],
    'correct_answer': 'To transform the data points into a new space where clustering is easier.',
    'explanation': "The graph Laplacian helps in transforming the data into a space where non-convex clusters can be separated more easily.",
    'chapter_information': 'ESL 2'
}

esl_2_lecture_notes_question_3 = {
    'question': "Why is it important to choose an appropriate scale parameter 'c' when constructing a radial-kernel gram matrix for spectral clustering?",
    'options_list': [
        'It determines the number of clusters.',
        'It influences the density of the similarity graph.',
        'It controls the shape of the clusters.',
        'It affects the computation time of the graph Laplacian.'
    ],
    'correct_answer': 'It influences the density of the similarity graph.',
    'explanation': "The scale parameter 'c' in the radial-kernel gram matrix controls how strongly distant points are connected in the similarity graph, thus influencing the graph's density.",
    'chapter_information': 'ESL 2'
}

esl_2_lecture_notes_question_4 = {
    'question': "How does the concept of a 'mutual K-nearest-neighbor graph' improve the robustness of spectral clustering?",
    'options_list': [
        'By ensuring that all data points have the same number of neighbors.',
        'By allowing clusters to overlap.',
        'By connecting points based on mutual neighborhood, which reflects local relationships more accurately.',
        'By reducing the dimensionality of the data.'
    ],
    'correct_answer': 'By connecting points based on mutual neighborhood, which reflects local relationships more accurately.',
    'explanation': "A mutual K-nearest-neighbor graph connects points that are in each other's K-nearest neighbors, capturing local neighborhood relationships more robustly and reflecting the actual structure of the data better.",
    'chapter_information': 'ESL 2'
}

esl_2_lecture_notes_question_5 = {
    'question': "What challenge does one face when choosing the number of eigenvectors to extract in spectral clustering?",
    'options_list': [
        'The number of eigenvectors required may vary with the number of clusters.',
        'There may not be a clear separation between the smallest eigenvalues, making it difficult to determine how many eigenvectors to select.',
        'The eigenvectors may not correspond directly to the number of clusters.',
        'The smallest eigenvalues may sometimes be negative, complicating the selection process.'
    ],
    'correct_answer': 'There may not be a clear separation between the smallest eigenvalues, making it difficult to determine how many eigenvectors to select.',
    'explanation': "In the toy example, the top-right panel shows that there is no strong separation between the smallest eigenvalues, making it unclear how many eigenvectors to use for clustering.",
    'chapter_information': 'ESL 2'
}

esl_2_lecture_notes_question_6 = {
    'question': "Given a similarity matrix \( S \) defined by \( s_{ii'} = \exp(-d^2_{ii'} / c) \), where \( d_{ii'} \) is the Euclidean distance between points \( x_i \) and \( x_{i'} \), and \( c = 2.5 \). Calculate the similarity value \( s_{ii'} \) for two points with \( d_{ii'} = 3 \).",
    'options_list': [
        '0.0015',
        '0.1054',
        '0.2231',
        '0.6065'
    ],
    'correct_answer': '0.2231',
    'explanation': "The similarity value is calculated as \( s_{ii'} = \exp(-3^2 / 2.5) \approx \exp(-9 / 2.5) \approx 0.2231 \).",
    'chapter_information': 'ESL 2'
}

esl_2_lecture_notes_question_7 = {
    'question': "Consider a dataset with 5 points, and you are constructing a mutual K-nearest-neighbor graph with K=2. Given the following Euclidean distances between the points:\n\nD = [[0, 1, 4, 7, 3],\n [1, 0, 2, 6, 5],\n [4, 2, 0, 5, 3],\n [7, 6, 5, 0, 2],\n [3, 5, 3, 2, 0]].\n\nWhich pairs of points will be connected in the mutual K-nearest-neighbor graph?",
    'options_list': [
        '(1,2), (1,5), (2,3), (4,5)',
        '(1,2), (1,5), (2,3), (3,5), (4,5)',
        '(1,2), (2,3), (3,5), (4,5)',
        '(1,2), (2,3), (3,4), (4,5)'
    ],
    'correct_answer': '(1,2), (1,5), (2,3), (4,5)',
    'explanation': "For K=2, we connect points that are mutual neighbors. Based on the distance matrix, point 1 is connected to points 2 and 5, point 2 is connected to points 1 and 3, point 3 is connected to point 2, and point 4 is connected to point 5.",
    'chapter_information': 'ESL 2'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
