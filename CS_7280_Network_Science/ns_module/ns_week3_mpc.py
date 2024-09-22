degree_distribution_question_1 = {
    'question': "What is the degree distribution of a network?",
    'options_list': [
        "The number of edges in the network",
        "The fraction of nodes with degree k",
        "The probability that a node has exactly k neighbors",
        "The variance of the number of connections in a network"
    ],
    'correct_answer': "The fraction of nodes with degree k",
    'explanation': "The degree distribution shows the fraction of nodes with degree k in a network, which is a fundamental concept when analyzing the structure of graphs.",
    'chapter_information': 'Topic: Degree Distribution, Lesson 3'
}

degree_distribution_question_2 = {
    'question': "In a random graph G(n, p), the degree distribution is best described by which model?",
    'options_list': [
        "Power-law distribution",
        "Exponential distribution",
        "Poisson distribution",
        "Gaussian distribution"
    ],
    'correct_answer': "Poisson distribution",
    'explanation': "In the G(n, p) model, the degree distribution follows a Poisson distribution, which is typical for random graphs.",
    'chapter_information': 'Topic: G(n,p) Model, Lesson 3'
}

friendship_paradox_question_1 = {
    'question': "Which of the following best explains the 'friendship paradox'?",
    'options_list': [
        "Most people have fewer friends than their friends do on average",
        "Most people have more friends than their friends do on average",
        "The average degree in a network is the same for all nodes",
        "In assortative networks, nodes tend to connect to others with similar degrees"
    ],
    'correct_answer': "Most people have fewer friends than their friends do on average",
    'explanation': "The friendship paradox states that on average, your friends are likely to have more friends than you, due to the way high-degree nodes are more likely to be connected.",
    'chapter_information': 'Topic: Friendship Paradox, Lesson 3'
}

ccdf_question_1 = {
    'question': "What does the Complementary Cumulative Distribution Function (C-CDF) represent in the context of degree distribution?",
    'options_list': [
        "The fraction of nodes with degree k",
        "The probability that a node has degree less than or equal to k",
        "The probability that the degree is at least k",
        "The average degree in a network"
    ],
    'correct_answer': "The probability that the degree is at least k",
    'explanation': "The C-CDF represents the probability that the degree of a node is at least k, which is a common way to represent degree distribution in larger networks.",
    'chapter_information': 'Topic: Complementary Cumulative Distribution Function, Lesson 3'
}

exponential_vs_powerlaw_question_1 = {
    'question': "In a log-linear plot, an exponential degree distribution appears as a straight line with what slope?",
    'options_list': [
        "$-\lambda$",
        "$\lambda$",
        "$-\alpha$",
        "$\alpha$"
    ],
    'correct_answer': "$-\lambda$",
    'explanation': "For an exponential degree distribution, the C-CDF decays exponentially, which in a log-linear plot appears as a straight line with a slope of $-\lambda$.",
    'chapter_information': 'Topic: Exponential Distribution, Lesson 3'
}

power_law_distribution_question_1 = {
    'question': "What is the characteristic feature of a power-law degree distribution when plotted on a log-log scale?",
    'options_list': [
        "It appears as a straight line with slope $-\alpha$",
        "It appears as a curve with slope $-\lambda$",
        "It decays exponentially fast with k",
        "It shows a constant probability for all values of k"
    ],
    'correct_answer': "It appears as a straight line with slope $-\alpha$",
    'explanation': "In a log-log plot, a power-law distribution appears as a straight line with slope $-\alpha$, which is a defining feature of scale-free networks.",
    'chapter_information': 'Topic: Power-Law Distribution, Lesson 3'
}

vaccination_target_question_1 = {
    'question': "True or False: The 'friendship paradox' can be used to identify vaccination targets when the network topology is unknown.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The 'friendship paradox' suggests that by vaccinating people with many connections (who are likely to have more connections than their friends), we can effectively target highly connected individuals in the network, even when the network topology is unknown.",
    'chapter_information': 'Topic: Friendship Paradox Application, Lesson 3'
}

degree_correlation_question_1 = {
    'question': "True or False: In assortative networks, nodes tend to connect to others with the same degree.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "In assortative networks, nodes with similar degrees tend to connect with each other, a pattern seen in certain social and biological networks.",
    'chapter_information': 'Topic: Assortative Networks, Lesson 3'
}

friendship_paradox_question_2 = {
    'question': "What is the friendship paradox?",
    'options_list': [
        "A paradox where the average degree of a node is always higher than the degree of its neighbors",
        "A paradox where most people have fewer friends than their friends do on average",
        "A phenomenon where high-degree nodes form more connections than low-degree nodes",
        "A situation where all nodes in a network have the same degree"
    ],
    'correct_answer': "A paradox where most people have fewer friends than their friends do on average",
    'explanation': "The friendship paradox states that on average, people tend to have fewer friends than their friends do. This is because high-degree nodes are more likely to be sampled.",
    'chapter_information': 'Topic: Friendship Paradox, Lesson 3'
}

friendship_paradox_question_3 = {
    'question': "Which of the following conditions increases the difference between the average node degree and the average neighbor's degree?",
    'options_list': [
        "A high variance in the degree distribution",
        "A low average degree",
        "A large number of nodes with the same degree",
        "A random graph with uniform degree distribution"
    ],
    'correct_answer': "A high variance in the degree distribution",
    'explanation': "The difference between the average node degree and the average neighbor's degree increases with the variance in the degree distribution.",
    'chapter_information': 'Topic: Friendship Paradox, Degree Variance, Lesson 3'
}

friendship_paradox_question_4 = {
    'question': "True or False: In a regular network where all nodes have the same degree, the friendship paradox holds.",
    'correct_answer': "False",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "In a regular network where all nodes have the same degree, the average node degree is equal to the average neighbor's degree, and the friendship paradox does not hold.",
    'chapter_information': 'Topic: Friendship Paradox, Regular Networks, Lesson 3'
}

friendship_paradox_question_5 = {
    'question': "What is the expected degree of a randomly selected neighbor in a random graph?",
    'options_list': [
        "$\\frac{k}{\\bar{k}}$",
        "$\\bar{k} + \\frac{\\sigma_k^2}{\\bar{k}}$",
        "$\\sum{k \\cdot q_k}$",
        "$\\frac{1}{\\bar{k}} \\cdot \\sum{k}$"
    ],
    'correct_answer': "$\\bar{k} + \\frac{\\sigma_k^2}{\\bar{k}}$",
    'explanation': "The expected degree of a randomly selected neighbor in a graph is given by $\\bar{k} + \\frac{\\sigma_k^2}{\\bar{k}}$, where $\\bar{k}$ is the average degree, and $\\sigma_k^2$ is the variance of the degree distribution.",
    'chapter_information': 'Topic: Friendship Paradox, Expected Neighbor Degree, Lesson 3'
}

friendship_paradox_question_6 = {
    'question': "True or False: The difference between the average neighbor's degree and the average node degree increases as the variance of the degree distribution decreases.",
    'correct_answer': "False",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The difference between the average neighbor's degree and the average node degree increases as the variance of the degree distribution increases, not decreases.",
    'chapter_information': 'Topic: Friendship Paradox, Degree Variance, Lesson 3'
}

friendship_paradox_question_7 = {
    'question': "In a star network, the hub node has degree:",
    'options_list': [
        "$n-1$",
        "$k=1$ for all nodes except the hub",
        "$2n - 2$",
        "$\\bar{k} = \\frac{2n-2}{n}$"
    ],
    'correct_answer': "$n-1$",
    'explanation': "In a star network, the central hub node has a degree of $n-1$, where $n$ is the total number of nodes in the network.",
    'chapter_information': 'Topic: Friendship Paradox, Star Networks, Lesson 3'
}


gnp_model_question_1 = {
    'question': "What is the G(n, p) model used to describe?",
    'options_list': [
        "A random graph model where each edge is created with probability p between any two nodes",
        "A regular graph where all nodes have the same degree",
        "A star network with one hub node connected to all other nodes",
        "A network where all edges have equal weight"
    ],
    'correct_answer': "A random graph model where each edge is created with probability p between any two nodes",
    'explanation': "The G(n, p) model, also known as the Erdős–Rényi model, describes a random graph where each pair of distinct nodes is connected by an edge with probability p.",
    'chapter_information': 'Topic: G(n, p) Model, Lesson 3'
}

gnp_model_question_2 = {
    'question': "True or False: In the G(n, p) model, the degree distribution follows a Poisson distribution for large n when p is small.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "For large n and small p, the degree distribution in the G(n, p) model can be approximated by a Poisson distribution because the average degree is much smaller than the total number of nodes.",
    'chapter_information': 'Topic: Degree Distribution, G(n, p) Model, Lesson 3'
}

gnp_model_question_3 = {
    'question': "What happens to the largest connected component (LCC) as the average node degree exceeds a critical value in a G(n, p) network?",
    'options_list': [
        "It begins to shrink",
        "It splits into smaller components",
        "It grows to include most of the nodes in the network",
        "It remains unchanged"
    ],
    'correct_answer': "It grows to include most of the nodes in the network",
    'explanation': "As the average node degree in the G(n, p) model exceeds a critical value, a giant connected component emerges, which eventually includes most of the nodes in the network.",
    'chapter_information': 'Topic: Connected Components in G(n, p), Lesson 3'
}

friendship_paradox_vaccination_question_1 = {
    'question': "How does the acquaintance immunization strategy leverage the friendship paradox?",
    'options_list': [
        "By vaccinating individuals with the highest degree in the network",
        "By vaccinating random individuals",
        "By vaccinating individuals who are connected to those with many contacts",
        "By randomly selecting edges and vaccinating the nodes they connect"
    ],
    'correct_answer': "By vaccinating individuals who are connected to those with many contacts",
    'explanation': "The acquaintance immunization strategy asks randomly selected individuals to identify a contact with many connections, which is effective due to the friendship paradox. The highly connected nodes are more likely to be identified and vaccinated.",
    'chapter_information': 'Topic: Friendship Paradox, Acquaintance Immunization, Lesson 3'
}

gnp_model_question_4 = {
    'question': "True or False: The degree distribution in the G(n, p) model always follows a Poisson distribution regardless of the value of p.",
    'correct_answer': "False",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The degree distribution follows a Poisson distribution only when p is small and the number of nodes is large. For other values of p, the degree distribution may follow a binomial distribution.",
    'chapter_information': 'Topic: Degree Distribution, G(n, p) Model, Lesson 3'
}

gnp_model_question_5 = {
    'question': "Which of the following is true about the degree variance in the G(n, p) model?",
    'options_list': [
        "It increases as p decreases",
        "It is always equal to the average degree",
        "It is proportional to $p \cdot (1 - p) \cdot (n - 1)$",
        "It is larger in regular graphs"
    ],
    'correct_answer': "It is proportional to $p \cdot (1 - p) \cdot (n - 1)$",
    'explanation': "The degree variance in the G(n, p) model is proportional to $p \cdot (1 - p) \cdot (n - 1)$, where p is the probability of an edge existing between two nodes.",
    'chapter_information': 'Topic: Degree Variance, G(n, p) Model, Lesson 3'
}


gnp_lcc_question_1 = {
    'question': "What is the probability, S, that a node belongs to the Largest Connected Component (LCC) in a G(n, p) network?",
    'options_list': [
        "The probability that a node does not belong to the LCC",
        "The expected value of the fraction of nodes in the LCC",
        "The probability that a node belongs to a smaller component",
        "The average degree of a node in the network"
    ],
    'correct_answer': "The expected value of the fraction of nodes in the LCC",
    'explanation': "In the G(n, p) model, S is the probability that a node belongs to the LCC, which is also the expected value of the fraction of nodes that belong to the LCC.",
    'chapter_information': 'Topic: G(n, p), Size of LCC, Lesson 3'
}

gnp_lcc_question_2 = {
    'question': "At what average degree $\\bar{k}$ does a phase transition occur in a G(n, p) model?",
    'options_list': [
        "$\\bar{k} = 0.5$",
        "$\\bar{k} = 1$",
        "$\\bar{k} = 2$",
        "$\\bar{k} = \\ln(n)$"
    ],
    'correct_answer': "$\\bar{k} = 1$",
    'explanation': "A phase transition occurs when the average degree $\\bar{k}$ exceeds 1. This is when a giant connected component emerges in the G(n, p) model.",
    'chapter_information': 'Topic: Phase Transition in G(n, p), Lesson 3'
}

gnp_lcc_question_3 = {
    'question': "True or False: In a G(n, p) network, when the average degree $\\bar{k}$ is less than 1, the Largest Connected Component (LCC) includes almost zero nodes.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "When $\\bar{k} < 1$, the LCC is very small, and the majority of nodes are in very small, disconnected components.",
    'chapter_information': 'Topic: G(n, p) Model, Size of LCC, Lesson 3'
}

gnp_lcc_question_4 = {
    'question': "Which of the following is true about the phase transition in G(n, p) networks?",
    'options_list': [
        "The LCC forms only when $\\bar{k} > \\ln(n)$",
        "The LCC forms as soon as $\\bar{k} > 0.5$",
        "The LCC forms when the average degree is greater than 1",
        "The LCC never forms in sparse networks"
    ],
    'correct_answer': "The LCC forms when the average degree is greater than 1",
    'explanation': "In a G(n, p) model, the phase transition occurs when the average degree exceeds 1. This is the point at which a giant connected component emerges.",
    'chapter_information': 'Topic: Phase Transition in G(n, p), Lesson 3'
}

gnp_single_component_question_1 = {
    'question': "What is the minimum value of p required for the G(n, p) model to have a single connected component?",
    'options_list': [
        "$p = \\frac{1}{n}$",
        "$p = \\frac{\\ln n}{n}$",
        "$p = \\frac{n - 1}{2n}$",
        "$p = \\frac{n}{2 \\ln n}$"
    ],
    'correct_answer': "$p = \\frac{\\ln n}{n}$",
    'explanation': "For the G(n, p) model to have a single connected component, the connection probability must be at least $p = \\frac{\\ln n}{n}$.",
    'chapter_information': 'Topic: Single Connected Component in G(n, p), Lesson 3'
}

gnp_single_component_question_2 = {
    'question': "True or False: The G(n, p) model forms a single connected component when the average degree is less than the natural logarithm of the network size.",
    'correct_answer': "False",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The G(n, p) model forms a single connected component when the average degree is greater than the natural logarithm of the network size, $\\bar{k} > \\ln(n)$.",
    'chapter_information': 'Topic: G(n, p) Single Connected Component, Lesson 3'
}


degree_correlations_question_1 = {
    'question': "What is the probability that a node of degree k is connected to another node of degree k' in a neutral network?",
    'options_list': [
        "The probability is independent of the degree of the neighbor",
        "The probability depends on the degree of the neighbor",
        "The probability is proportional to the degree of the neighbor",
        "The probability is inversely proportional to the degree of the neighbor"
    ],
    'correct_answer': "The probability is independent of the degree of the neighbor",
    'explanation': "In a neutral network, the probability that a node connects to another node is independent of the degree of the neighbor.",
    'chapter_information': 'Topic: Degree Correlations, Neutral Networks, Lesson 3'
}

degree_correlations_question_2 = {
    'question': "Which of the following statements best describes an assortative network?",
    'options_list': [
        "Higher-degree nodes tend to connect to lower-degree nodes",
        "Higher-degree nodes tend to connect to other higher-degree nodes",
        "The degree of connected nodes is independent of each other",
        "Nodes tend to form hubs connected by low-degree nodes"
    ],
    'correct_answer': "Higher-degree nodes tend to connect to other higher-degree nodes",
    'explanation': "In assortative networks, high-degree nodes are more likely to connect to other high-degree nodes, as seen in social networks where celebrities often connect with other celebrities.",
    'chapter_information': 'Topic: Assortative Networks, Lesson 3'
}

degree_correlations_question_3 = {
    'question': "True or False: Disassortative networks are characterized by higher-degree nodes connecting to lower-degree nodes.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "In disassortative networks, high-degree nodes are more likely to connect to low-degree nodes, such as in infrastructure networks where backbone routers connect to low-degree devices.",
    'chapter_information': 'Topic: Disassortative Networks, Lesson 3'
}

degree_correlations_question_4 = {
    'question': "How can we measure degree correlations in a network?",
    'options_list': [
        "By calculating the total number of edges in the network",
        "By modeling the relationship between the average nearest-neighbor degree and the node degree using a power law",
        "By counting the number of triangles in the network",
        "By measuring the number of components in the network"
    ],
    'correct_answer': "By modeling the relationship between the average nearest-neighbor degree and the node degree using a power law",
    'explanation': "Degree correlations can be measured by approximating the relationship between the average nearest-neighbor degree $k_{nn}(k)$ and the degree $k$ of a node using a power law.",
    'chapter_information': 'Topic: Measuring Degree Correlations, Lesson 3'
}

degree_correlations_question_5 = {
    'question': "What is the interpretation of a positive exponent $\\mu$ in the relationship $k_{nn}(k) = \\alpha \\cdot k^{\\mu}$?",
    'options_list': [
        "The network is neutral",
        "The network is disassortative",
        "The network is assortative",
        "The network has no significant degree correlations"
    ],
    'correct_answer': "The network is assortative",
    'explanation': "A positive exponent $\\mu$ indicates that the network is assortative, meaning that high-degree nodes tend to connect with other high-degree nodes.",
    'chapter_information': 'Topic: Degree Correlations, Lesson 3'
}

degree_correlations_question_6 = {
    'question': "True or False: In a neutral network, the degree of a node is correlated with the degree of its neighbors.",
    'correct_answer': "False",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "In a neutral network, the degree of a node is independent of the degree of its neighbors, so there is no correlation.",
    'chapter_information': 'Topic: Neutral Networks, Lesson 3'
}

degree_correlations_question_7 = {
    'question': "Which of the following describes the behavior of a disassortative network?",
    'options_list': [
        "Lower-degree nodes tend to connect with other lower-degree nodes",
        "Higher-degree nodes tend to connect with other higher-degree nodes",
        "Higher-degree nodes tend to connect with lower-degree nodes",
        "The degree of nodes is independent of the degree of their neighbors"
    ],
    'correct_answer': "Higher-degree nodes tend to connect with lower-degree nodes",
    'explanation': "In disassortative networks, higher-degree nodes tend to connect with lower-degree nodes, which is common in technological networks.",
    'chapter_information': 'Topic: Disassortative Networks, Lesson 3'
}

lesson_summary_question_1 = {
    'question': "What does the degree distribution of a network tell you?",
    'options_list': [
        "The total number of edges in the network",
        "The probability that two nodes are connected based on their degrees",
        "The network's connectivity, including average node degree, degree variability, and common degree modes",
        "The structure of the largest connected component"
    ],
    'correct_answer': "The network's connectivity, including average node degree, degree variability, and common degree modes",
    'explanation': "The degree distribution provides a concise description of a network's connectivity, including properties like average node degree, degree variability, and whether there are nodes with very high degrees.",
    'chapter_information': 'Topic: Degree Distribution, Lesson 3 Summary'
}

lesson_summary_question_2 = {
    'question': "Which of the following best describes the friendship paradox?",
    'options_list': [
        "Most people have more friends than their friends do",
        "Most people have fewer friends than their friends do",
        "The degree distribution is normally distributed",
        "High-degree nodes are more connected than low-degree nodes"
    ],
    'correct_answer': "Most people have fewer friends than their friends do",
    'explanation': "The friendship paradox states that most people have fewer friends than their friends do on average, which is due to the fact that high-degree nodes are more likely to be connected to others.",
    'chapter_information': 'Topic: Friendship Paradox, Lesson 3 Summary'
}

lesson_summary_question_3 = {
    'question': "True or False: The degree distribution of G(n, p) random graphs can be approximated by a Poisson distribution.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The degree distribution in G(n, p) random graphs can be approximated by a Poisson distribution when the graph is sparse (small p and large n).",
    'chapter_information': 'Topic: G(n, p) Networks, Lesson 3 Summary'
}

lesson_summary_question_4 = {
    'question': "Which of the following is NOT something that can be inferred from the degree distribution alone?",
    'options_list': [
        "The average node degree",
        "Degree variability in the network",
        "Whether there are degree correlations between connected nodes",
        "The presence of nodes with very high degrees"
    ],
    'correct_answer': "Whether there are degree correlations between connected nodes",
    'explanation': "Degree correlations cannot be inferred from the degree distribution alone. They require additional information about how nodes of different degrees are connected.",
    'chapter_information': 'Topic: Degree Correlations, Lesson 3 Summary'
}

lesson_summary_question_5 = {
    'question': "What property of a network is illustrated by the friendship paradox?",
    'options_list': [
        "The presence of very high-degree nodes",
        "The importance of degree variability",
        "The size of the largest connected component",
        "The degree correlation between nodes"
    ],
    'correct_answer': "The importance of degree variability",
    'explanation': "The friendship paradox illustrates the importance of degree variability in networks, showing that high-degree nodes are more likely to have a large number of connections.",
    'chapter_information': 'Topic: Friendship Paradox, Lesson 3 Summary'
}

lesson_summary_question_6 = {
    'question': "True or False: The size of the largest connected component in a G(n, p) network can be analyzed mathematically.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The size of the largest connected component in G(n, p) networks can be analyzed mathematically, and a phase transition occurs when the average degree exceeds a critical value.",
    'chapter_information': 'Topic: G(n, p) Networks, Lesson 3 Summary'
}

lesson_summary_question_7 = {
    'question': "Why is G(n, p) considered a fundamental model for random graphs?",
    'options_list': [
        "Because it always forms a connected component",
        "Because its degree distribution follows a normal distribution",
        "Because it serves as a baseline network for understanding random graph properties",
        "Because it explains degree correlations in all networks"
    ],
    'correct_answer': "Because it serves as a baseline network for understanding random graph properties",
    'explanation': "G(n, p) is a fundamental model of random graphs and is used as a baseline for understanding the properties of random networks.",
    'chapter_information': 'Topic: G(n, p) Model, Lesson 3 Summary'
}

lesson_summary_question_1 = {
    'question': "What does the degree distribution of a network tell you?",
    'options_list': [
        "The total number of edges in the network",
        "The probability that two nodes are connected based on their degrees",
        "The network's connectivity, including average node degree, degree variability, and common degree modes",
        "The structure of the largest connected component"
    ],
    'correct_answer': "The network's connectivity, including average node degree, degree variability, and common degree modes",
    'explanation': "The degree distribution provides a concise description of a network's connectivity, including properties like average node degree, degree variability, and whether there are nodes with very high degrees.",
    'chapter_information': 'Topic: Degree Distribution, Lesson 3 Summary'
}

lesson_summary_question_2 = {
    'question': "Which of the following best describes the friendship paradox?",
    'options_list': [
        "Most people have more friends than their friends do",
        "Most people have fewer friends than their friends do",
        "The degree distribution is normally distributed",
        "High-degree nodes are more connected than low-degree nodes"
    ],
    'correct_answer': "Most people have fewer friends than their friends do",
    'explanation': "The friendship paradox states that most people have fewer friends than their friends do on average, which is due to the fact that high-degree nodes are more likely to be connected to others.",
    'chapter_information': 'Topic: Friendship Paradox, Lesson 3 Summary'
}

lesson_summary_question_3 = {
    'question': "True or False: The degree distribution of G(n, p) random graphs can be approximated by a Poisson distribution.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The degree distribution in G(n, p) random graphs can be approximated by a Poisson distribution when the graph is sparse (small p and large n).",
    'chapter_information': 'Topic: G(n, p) Networks, Lesson 3 Summary'
}

lesson_summary_question_4 = {
    'question': "Which of the following is NOT something that can be inferred from the degree distribution alone?",
    'options_list': [
        "The average node degree",
        "Degree variability in the network",
        "Whether there are degree correlations between connected nodes",
        "The presence of nodes with very high degrees"
    ],
    'correct_answer': "Whether there are degree correlations between connected nodes",
    'explanation': "Degree correlations cannot be inferred from the degree distribution alone. They require additional information about how nodes of different degrees are connected.",
    'chapter_information': 'Topic: Degree Correlations, Lesson 3 Summary'
}

lesson_summary_question_5 = {
    'question': "What property of a network is illustrated by the friendship paradox?",
    'options_list': [
        "The presence of very high-degree nodes",
        "The importance of degree variability",
        "The size of the largest connected component",
        "The degree correlation between nodes"
    ],
    'correct_answer': "The importance of degree variability",
    'explanation': "The friendship paradox illustrates the importance of degree variability in networks, showing that high-degree nodes are more likely to have a large number of connections.",
    'chapter_information': 'Topic: Friendship Paradox, Lesson 3 Summary'
}

lesson_summary_question_6 = {
    'question': "True or False: The size of the largest connected component in a G(n, p) network can be analyzed mathematically.",
    'correct_answer': "True",
        'options_list': [
        "True",
        "False"
    ],
    'explanation': "The size of the largest connected component in G(n, p) networks can be analyzed mathematically, and a phase transition occurs when the average degree exceeds a critical value.",
    'chapter_information': 'Topic: G(n, p) Networks, Lesson 3 Summary'
}

lesson_summary_question_7 = {
    'question': "Why is G(n, p) considered a fundamental model for random graphs?",
    'options_list': [
        "Because it always forms a connected component",
        "Because its degree distribution follows a normal distribution",
        "Because it serves as a baseline network for understanding random graph properties",
        "Because it explains degree correlations in all networks"
    ],
    'correct_answer': "Because it serves as a baseline network for understanding random graph properties",
    'explanation': "G(n, p) is a fundamental model of random graphs and is used as a baseline for understanding the properties of random networks.",
    'chapter_information': 'Topic: G(n, p) Model, Lesson 3 Summary'
}

graph_degree_question = {
    'question': "Given a graph with 800 nodes and 1000 edges, what is the probability that a random edge connects to a node of degree 5? You are given that the probability that a node has degree 5 is 1/3.",
    'options_list': [
        "2/3",
        "1/3",
        "3/4",
        "4/5"
    ],
    'correct_answer': "2/3",
    'explanation': "The correct answer is 2/3. Given that 1/3 of the nodes have degree 5, the probability of connecting to a node of degree 5 is higher due to its higher number of edges. The formula takes into account both the degree of the node and the fraction of nodes with that degree.",
    'chapter_information': 'Topic: Degree Distribution, G(n,p) Model'
}

vaccination_strategy_question = {
    'question': "Assume we can only vaccinate 100 people but we don’t know the topology of the contact network. Which of the following strategies would be better to mitigate the spread of a virus?",
    'options_list': [
        "A. Select randomly 100 individuals and vaccinate them.",
        "B. Select randomly 100 individuals and ask each of them to report the neighbor with the highest number of contacts. Vaccinate the 100 reported nodes (i.e., you can assume that the reported nodes are distinct).",
        "C. Select randomly 100 individuals and ask each of them to report either the neighbor with the highest number of contacts – or themselves if they have more contacts than all their neighbors. Vaccinate the 100 reported nodes (i.e., you can assume that the reported nodes are distinct).",
        "D. There is no difference between B and C."
    ],
    'correct_answer': "C. Select randomly 100 individuals and ask each of them to report either the neighbor with the highest number of contacts – or themselves if they have more contacts than all their neighbors. Vaccinate the 100 reported nodes (i.e., you can assume that the reported nodes are distinct).",
    'explanation': "Strategy C is more effective because it leverages the friendship paradox, where individuals with the most contacts are more likely to spread the virus. By identifying and vaccinating the most connected individuals, the spread of the virus is mitigated more effectively.",
    'chapter_information': 'Topic: Friendship Paradox, Vaccination Strategy'
}

gnp_critical_probability_question = {
    'question': "Consider the G(n,p) model of random graphs with n=1000 nodes. What is the critical probability threshold for the emergence of a large connected component? Your answer should be in the form of a fraction (for example, 1/10) -- do not make any approximations in this question.",
    'options_list': [
        "1/1000",
        "1/999",
        "1/500",
        "1/499"
    ],
    'correct_answer': "1/999",
    'explanation': "The critical probability threshold for the emergence of a large connected component is given by \( p = 1/(n-1) \). For n = 1000, the critical threshold is 1/999.",
    'chapter_information': 'Topic: G(n,p) Model, Phase Transition'
}

friendship_paradox_assumption_question = {
    'question': "In the Friendship Paradox section of this lecture, we derived the average neighbor degree. What is the key assumption in those derivations?",
    'options_list': [
        "The Friendship Paradox applies to any network",
        "The network is neutral",
        "The network follows the Poisson degree distribution",
        "The network is connected"
    ],
    'correct_answer': "The network is neutral",
    'explanation': "The key assumption in the derivation of the average neighbor degree is that the network is neutral, meaning that there are no degree correlations. This simplifies the calculations by making the probability of connection independent of node degree.",
    'chapter_information': 'Topic: Friendship Paradox, Average Neighbor Degree'
}



KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

WEEK_3_MPC = KC_MPC_QUESTIONS[:-1]
