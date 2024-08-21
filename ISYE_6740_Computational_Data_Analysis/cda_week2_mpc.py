module_2_lecture_notes_question_1 = {
    'question': "What is the primary goal of clustering in the context of image databases?",
    'options_list': [
        'To label each image correctly',
        'To group images into clusters based on their similarity',
        'To compress image data',
        'To increase the resolution of images'
    ],
    'correct_answer': 'To group images into clusters based on their similarity',
    'explanation': "The goal of clustering is to divide the objects into groups such that the objects within a group are more similar to each other than to those in different groups.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_2 = {
    'question': "In the example of handwritten digits, what is the main task that clustering is used to achieve?",
    'options_list': [
        'Recognizing individual digits',
        'Grouping similar handwritten digits together',
        'Improving the resolution of digit images',
        'Digitizing handwritten documents'
    ],
    'correct_answer': 'Grouping similar handwritten digits together',
    'explanation': "Clustering is used to group similar images of handwritten digits together, such as grouping all images of the digit '7' into one cluster.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_3 = {
    'question': "How are images represented in the context of clustering handwritten digits?",
    'options_list': [
        'As vectors of pixel values',
        'As 3D models',
        'As sequences of numbers',
        'As matrices of color values'
    ],
    'correct_answer': 'As vectors of pixel values',
    'explanation': "Images are represented by vectorizing the matrix of pixel values, turning each image into a long vector.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_4 = {
    'question': "What is the first step in the K-means algorithm?",
    'options_list': [
        'Assigning data points to clusters',
        'Calculating the centroids',
        'Initializing the centroids randomly',
        'Sorting the data points'
    ],
    'correct_answer': 'Initializing the centroids randomly',
    'explanation': "The first step in the K-means algorithm is to initialize the centroids randomly.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_5 = {
    'question': "Why might different initializations in K-means lead to different results?",
    'options_list': [
        'Because K-means is a convex optimization problem',
        'Because K-means always finds the global minimum',
        'Because K-means solves a non-convex optimization problem',
        'Because K-means uses a deterministic algorithm'
    ],
    'correct_answer': 'Because K-means solves a non-convex optimization problem',
    'explanation': "Different initializations can lead to different results because K-means is solving a non-convex optimization problem, which may lead to different local minima.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_6 = {
    'question': "What property of the K-means objective function ensures that the algorithm converges?",
    'options_list': [
        'It is non-monotonic',
        'It is convex',
        'It is monotonic and decreasing',
        'It can oscillate'
    ],
    'correct_answer': 'It is monotonic and decreasing',
    'explanation': "The K-means objective function is monotonic and decreasing, which ensures that the algorithm will converge.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_7 = {
    'question': "In general, why is clustering using the exact global optimal solution for K-means considered NP-hard?",
    'options_list': [
        'Because it requires solving a non-linear system',
        'Because the number of possibilities is \( k^m \), where \( k \) is the number of centroids and \( m \) is the number of data points',
        'Because it involves continuous optimization',
        'Because it can only be solved using dynamic programming'
    ],
    'correct_answer': 'Because the number of possibilities is \( k^m \), where \( k \) is the number of centroids and \( m \) is the number of data points',
    'explanation': "Clustering using the exact global optimal solution is considered NP-hard because the number of possibilities is \( k^m \), making it computationally infeasible for large datasets.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_8 = {
    'question': "How can K-means be generalized to account for different definitions of similarity?",
    'options_list': [
        'By changing the number of clusters',
        'By using a different similarity or dissimilarity function',
        'By initializing centroids differently',
        'By increasing the number of iterations'
    ],
    'correct_answer': 'By using a different similarity or dissimilarity function',
    'explanation': "K-means can be generalized by using a different similarity or dissimilarity function instead of the standard Euclidean distance.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_9 = {
    'question': "What is a dendrogram, as used in hierarchical clustering?",
    'options_list': [
        'A plot showing the assignment of data points to clusters',
        'A tree structure representing the hierarchy of clusters',
        'A type of decision tree used for classification',
        'A matrix representing distances between points'
    ],
    'correct_answer': 'A tree structure representing the hierarchy of clusters',
    'explanation': "A dendrogram is a tree structure that represents the hierarchy of clusters formed during hierarchical clustering.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_10 = {
    'question': "What distinguishes hierarchical clustering from K-means?",
    'options_list': [
        'Hierarchical clustering requires a predefined number of clusters',
        'Hierarchical clustering works best with large datasets',
        'Hierarchical clustering organizes data in a hierarchical fashion',
        'Hierarchical clustering is faster than K-means'
    ],
    'correct_answer': 'Hierarchical clustering organizes data in a hierarchical fashion',
    'explanation': "Hierarchical clustering is distinguished from K-means by its approach of organizing data into a hierarchy, typically represented by a dendrogram.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_11 = {
    'question': "What is the role of the centroid in the K-means algorithm?",
    'options_list': [
        'It determines the number of clusters',
        'It represents the center of a cluster and is used to assign data points to the nearest cluster',
        'It is a measure of the distance between clusters',
        'It is a threshold value for stopping the algorithm'
    ],
    'correct_answer': 'It represents the center of a cluster and is used to assign data points to the nearest cluster',
    'explanation': "In K-means, a centroid represents the center of a cluster, and each data point is assigned to the cluster with the nearest centroid.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_12 = {
    'question': "How does the K-means algorithm adjust the centroids during each iteration?",
    'options_list': [
        'By moving them to the geometric median of the assigned data points',
        'By calculating the average of all data points assigned to each cluster',
        'By randomly selecting new data points',
        'By minimizing the sum of squared distances between data points and the centroid'
    ],
    'correct_answer': 'By calculating the average of all data points assigned to each cluster',
    'explanation': "During each iteration of K-means, the centroids are adjusted by calculating the average (mean) of all data points assigned to each cluster, moving the centroid to this new position.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_13 = {
    'question': "Which property of the K-means algorithm ensures that it will eventually terminate?",
    'options_list': [
        'The algorithm's use of Euclidean distance',
        'The finite number of possible data point assignments',
        'The ability to find the global minimum',
        'The use of non-linear optimization techniques'
    ],
    'correct_answer': 'The finite number of possible data point assignments',
    'explanation': "K-means will eventually terminate because there is a finite number of possible assignments of data points to clusters, and the algorithm is designed to reduce the objective function at each step.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_14 = {
    'question': "Why might the K-means algorithm fail to find the global minimum of the objective function?",
    'options_list': [
        'Because it uses a non-convex objective function',
        'Because it always converges to a global minimum',
        'Because it only considers the first two data points',
        'Because it randomly initializes centroids each time'
    ],
    'correct_answer': 'Because it uses a non-convex objective function',
    'explanation': "K-means might fail to find the global minimum because it uses a non-convex objective function, leading to convergence at local minima depending on the initialization.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_15 = {
    'question': "What is the significance of the 'triangle inequality' in the context of distance functions?",
    'options_list': [
        'It ensures that the distance between two points is never negative',
        'It is used to compute centroids in K-means',
        'It ensures that the distance between two points plus a third point is minimized',
        'It guarantees that the direct distance between two points is always less than or equal to the sum of distances via a third point'
    ],
    'correct_answer': 'It guarantees that the direct distance between two points is always less than or equal to the sum of distances via a third point',
    'explanation': "The triangle inequality ensures that the direct distance between two points is always less than or equal to the sum of the distances when traveling via a third point, which is a key property for defining a valid distance metric.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_16 = {
    'question': "In hierarchical clustering, what happens when you cut the dendrogram at a certain level?",
    'options_list': [
        'You define the number of clusters',
        'You merge all clusters into one',
        'You separate the data points into different clusters based on the cut level',
        'You optimize the centroid positions'
    ],
    'correct_answer': 'You separate the data points into different clusters based on the cut level',
    'explanation': "Cutting the dendrogram at a certain level separates the data points into clusters, with each cut level corresponding to a different number of clusters.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_17 = {
    'question': "What is a key difference between K-means and K-medoids algorithms?",
    'options_list': [
        'K-means uses centroids while K-medoids uses actual data points as cluster centers',
        'K-means is faster than K-medoids',
        'K-means is used for larger datasets, while K-medoids is used for smaller datasets',
        'K-means requires more memory than K-medoids'
    ],
    'correct_answer': 'K-means uses centroids while K-medoids uses actual data points as cluster centers',
    'explanation': "The key difference between K-means and K-medoids is that K-means uses the average of data points as the centroid, while K-medoids selects actual data points as the cluster centers.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_18 = {
    'question': "How does the K-means algorithm handle noisy data?",
    'options_list': [
        'It excludes noisy data points from the clusters',
        'It assigns noisy data points to the nearest cluster, which may lead to incorrect clustering',
        'It creates a separate cluster for noisy data',
        'It ignores noisy data during the clustering process'
    ],
    'correct_answer': 'It assigns noisy data points to the nearest cluster, which may lead to incorrect clustering',
    'explanation': "The K-means algorithm assigns noisy data points to the nearest cluster, which can sometimes result in incorrect clustering as these points may not fit well into any cluster.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_19 = {
    'question': "Why is the L2 (Euclidean) distance commonly used in the K-means algorithm?",
    'options_list': [
        'Because it is the simplest to calculate',
        'Because it ensures a global minimum',
        'Because it is a smooth and differentiable function',
        'Because it minimizes the squared distance, making it suitable for averaging'
    ],
    'correct_answer': 'Because it minimizes the squared distance, making it suitable for averaging',
    'explanation': "The L2 (Euclidean) distance is commonly used in K-means because it minimizes the squared distance between points and centroids, which is consistent with the averaging process used to adjust the centroids.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_20 = {
    'question': "What is one advantage of hierarchical clustering over K-means?",
    'options_list': [
        'It is faster for large datasets',
        'It requires less memory',
        'It provides a complete picture of how data points are related at various levels of granularity',
        'It always finds the global minimum'
    ],
    'correct_answer': 'It provides a complete picture of how data points are related at various levels of granularity',
    'explanation': "One advantage of hierarchical clustering is that it provides a complete picture of how data points are related at various levels of granularity, unlike K-means, which gives a single partition of the data.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_21 = {
    'question': "Given two vectors \( \mathbf{x} = [1, 2] \) and \( \mathbf{y} = [4, 6] \), calculate the Euclidean distance between them.",
    'options_list': [
        '2',
        '3',
        '5',
        '7'
    ],
    'correct_answer': '5',
    'explanation': "The Euclidean distance between the vectors \( \mathbf{x} \) and \( \mathbf{y} \) is calculated as \( \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5 \).",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_22 = {
    'question': "If a dataset consists of three 2-dimensional data points \((1, 2)\), \((3, 4)\), and \((5, 6)\), and the initial centroids for K-means are chosen as \((1, 2)\) and \((5, 6)\), which centroid will the point \((3, 4)\) be assigned to after the first iteration?",
    'options_list': [
        'Centroid at (1, 2)',
        'Centroid at (5, 6)',
        'A new centroid',
        'Cannot be determined'
    ],
    'correct_answer': 'Centroid at (1, 2)',
    'explanation': "The point \((3, 4)\) is closer to \((1, 2)\) than \((5, 6)\). The Euclidean distance to \((1, 2)\) is \( \sqrt{(3-1)^2 + (4-2)^2} = \sqrt{8} \) and to \((5, 6)\) is \( \sqrt{8} \), so the point \((3, 4)\) is equidistant to both centroids.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_23 = {
    'question': "Compute the Manhattan distance between the points \( \mathbf{p} = [3, 5] \) and \( \mathbf{q} = [1, 1] \).",
    'options_list': [
        '4',
        '5',
        '6',
        '7'
    ],
    'correct_answer': '6',
    'explanation': "The Manhattan distance is calculated as the sum of the absolute differences between corresponding entries: \( |3-1| + |5-1| = 2 + 4 = 6 \).",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_24 = {
    'question': "For a K-means algorithm with \( k = 3 \) clusters and \( m = 100 \) data points, what is the time complexity of one iteration?",
    'options_list': [
        'O(m)',
        'O(k)',
        'O(mk)',
        'O(m^2k)'
    ],
    'correct_answer': 'O(mk)',
    'explanation': "The time complexity of one iteration in the K-means algorithm is \( O(mk) \), as each data point needs to be compared to all \( k \) centroids.",
    'chapter_information': 'Module 2 Lecture Notes'
}

module_2_lecture_notes_question_25 = {
    'question': "What is the space complexity of the K-means algorithm, assuming \( m \) data points and \( k \) clusters?",
    'options_list': [
        'O(m + k)',
        'O(mk)',
        'O(m)',
        'O(k)'
    ],
    'correct_answer': 'O(m + k)',
    'explanation': "The space complexity of the K-means algorithm is \( O(m + k) \) as it needs to store all data points and the centroids of the clusters.",
    'chapter_information': 'Module 2 Lecture Notes'
}

k_medoid_paper_question_1 = {
    'question': "What is the relationship between the medoid in squared `2 norm and the mean of the data points in a cluster?",
    'options_list': [
        'The medoid is always the geometric median.',
        'The medoid is equivalent to the mean of the data points.',
        'The medoid is the data point closest to the mean.',
        'The medoid is unrelated to the mean of the data points.'
    ],
    'correct_answer': 'The medoid is the data point closest to the mean.',
    'explanation': "The paper concludes that finding the medoid in squared `2 norm is equivalent to finding the mean of the data points and then identifying the data point closest to that mean.",
    'chapter_information': 'K-medoid Paper by Yao Xie'
}

k_medoid_paper_question_2 = {
    'question': "Given three data points \((1, 2)\), \((3, 4)\), and \((5, 6)\) in 2D space, which point is the medoid under the squared `2 norm?",
    'options_list': [
        '(1, 2)',
        '(3, 4)',
        '(5, 6)',
        'None of the above'
    ],
    'correct_answer': '(3, 4)',
    'explanation': "The mean of the points is \( \mu = (3, 4) \). The point closest to the mean is \( (3, 4) \), making it the medoid.",
    'chapter_information': 'K-medoid Paper by Yao Xie'
}

k_medoid_paper_question_3 = {
    'question': "Which of the following best describes the cost function used to find the medoid in squared `2 norm?",
    'options_list': [
        'mΣ_{i=1}^{m} ||x_j||^2 + Σ_{i=1}^{m} ||x_i||^2 + 2mμ̂^T x_j',
        'm||x_j||^2 + Σ_{i=1}^{m} ||x_i||^2 - 2mμ̂^T x_j',
        'Σ_{i=1}^{m} ||x_j||^2 + 2Σ_{i=1}^{m} ||x_i||^2 - mμ̂^T x_j',
        'Σ_{i=1}^{m} ||x_j - μ̂ ||^2'
    ],
    'correct_answer': 'm||x_j||^2 + Σ_{i=1}^{m} ||x_i||^2 - 2mμ̂^T x_j',
    'explanation': "The cost function for finding the medoid in squared `2 norm is given by \( m||x_j||^2 + Σ_{i=1}^{m} ||x_i||^2 - 2mμ̂^T x_j \).",
    'chapter_information': 'K-medoid Paper by Yao Xie'
}

k_medoid_paper_question_4 = {
    'question': "Why can certain terms be dropped from the cost function when finding the medoid?",
    'options_list': [
        'The terms are negligible and do not affect the result.',
        'The terms are constants that do not change with the choice of medoid.',
        'The terms are redundant and cancel out.',
        'Dropping the terms simplifies the computation without affecting the outcome.'
    ],
    'correct_answer': 'The terms are constants that do not change with the choice of medoid.',
    'explanation': "Certain terms can be dropped because they are constants and do not affect the optimal solution when minimizing the cost function.",
    'chapter_information': 'K-medoid Paper by Yao Xie'
}

k_medoid_paper_question_5 = {
    'question': "What is the time complexity of finding the medoid in a dataset with \( m \) data points using the squared `2 norm?",
    'options_list': [
        'O(m)',
        'O(m^2)',
        'O(m^3)',
        'O(\log m)'
    ],
    'correct_answer': 'O(m^2)',
    'explanation': "Finding the medoid involves calculating the distance between all pairs of points, which leads to a time complexity of \( O(m^2) \).",
    'chapter_information': 'K-medoid Paper by Yao Xie'
}

k_medoid_paper_question_6 = {
    'question': "What is the space complexity of storing the distance matrix when calculating the medoid for \( m \) data points?",
    'options_list': [
        'O(m + k)',
        'O(mk)',
        'O(m)',
        'O(m^2)'
    ],
    'correct_answer': 'O(m^2)',
    'explanation': "The distance matrix requires storing \( m \times m \) distances, leading to a space complexity of \( O(m^2) \).",
    'chapter_information': 'K-medoid Paper by Yao Xie'
}




KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_2_MPC = KC_MPC_QUESTIONS[:-1]
